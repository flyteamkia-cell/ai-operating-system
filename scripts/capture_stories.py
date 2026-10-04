"""Capture own-account Instagram stories and their insights into the evidence log.

Stories (and their insights) are only readable for 24h after posting, so this runs
on a schedule (.github/workflows/capture-stories.yml, every 6h). Each run upserts
one row per story id: a story seen again gets its newer metrics, so the last
capture before expiry wins. Deterministic code only; no model calls.

Env: IG_LONG_LIVED_TOKEN, IG_BUSINESS_ACCOUNT_ID (required)
     IG_GRAPH_VERSION (default v23.0), IG_APP_ID + IG_APP_SECRET (optional, enables
     the token-expiry check, which fails the run when <7 days remain).
"""

from __future__ import annotations

import csv
import json
import os
import random
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "evidence" / "own-account-stories-api.csv"
FIELDS = ["id", "timestamp", "media_type", "permalink", "reach", "replies", "shares",
          "total_interactions", "follows", "profile_visits", "navigation", "captured_at"]
METRICS = ["reach", "replies", "shares", "total_interactions", "follows", "profile_visits", "navigation"]
TIMEOUT_S = 30
MAX_ATTEMPTS = 4
EXPIRY_WARN_DAYS = 7


class GraphError(Exception):
    pass


def log(event: str, **data: object) -> None:
    print(json.dumps({"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"), "event": event, **data}), flush=True)


def graph_get(path: str, params: dict[str, str]) -> dict:
    version = os.environ.get("IG_GRAPH_VERSION") or "v23.0"
    url = f"https://graph.facebook.com/{version}/{path}?{urllib.parse.urlencode(params)}"
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(url, timeout=TIMEOUT_S) as res:
                return json.loads(res.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")[:300]
            # 4xx other than rate limiting is a request/token problem: retrying won't help.
            if e.code < 500 and e.code != 429:
                raise GraphError(f"HTTP {e.code} on {path}: {body}") from None
            reason = f"HTTP {e.code}"
        except (urllib.error.URLError, TimeoutError) as e:
            reason = str(getattr(e, "reason", e))
        if attempt == MAX_ATTEMPTS:
            raise GraphError(f"{path}: gave up after {attempt} attempts ({reason})")
        delay = 2 ** attempt + random.uniform(0, 1)
        log("retry", path=path, attempt=attempt, reason=reason, delay_s=round(delay, 1))
        time.sleep(delay)
    raise AssertionError("unreachable")


def check_token_expiry(token: str) -> None:
    app_id, app_secret = os.environ.get("IG_APP_ID"), os.environ.get("IG_APP_SECRET")
    if not (app_id and app_secret):
        log("token_check_skipped", reason="IG_APP_ID/IG_APP_SECRET not set")
        return
    data = graph_get("debug_token", {"input_token": token, "access_token": f"{app_id}|{app_secret}"})["data"]
    expires = int(data.get("expires_at") or 0)
    if not data.get("is_valid"):
        raise GraphError("token is not valid")
    if expires == 0:
        log("token_ok", expires="never")
        return
    days_left = (expires - time.time()) / 86400
    log("token_ok", days_left=round(days_left, 1))
    if days_left < EXPIRY_WARN_DAYS:
        raise GraphError(f"token expires in {days_left:.1f} days; refresh it and update the IG_LONG_LIVED_TOKEN secret")


def fetch_stories(account_id: str, token: str) -> list[dict[str, str]]:
    stories = graph_get(f"{account_id}/stories", {"fields": "id,timestamp,media_type,permalink", "access_token": token}).get("data", [])
    captured_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows = []
    for s in stories:
        insights = graph_get(f"{s['id']}/insights", {"metric": ",".join(METRICS), "access_token": token}).get("data", [])
        values = {m["name"]: (m.get("values") or [{}])[0].get("value", m.get("total_value", {}).get("value", "")) for m in insights}
        rows.append({"id": s["id"], "timestamp": s.get("timestamp", ""), "media_type": s.get("media_type", ""),
                     "permalink": s.get("permalink", ""), **{m: values.get(m, "") for m in METRICS}, "captured_at": captured_at})
    return rows


def upsert(rows: list[dict[str, str]]) -> tuple[int, int]:
    existing: dict[str, dict[str, str]] = {}
    if CSV_PATH.exists():
        with CSV_PATH.open(newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                existing[r["id"]] = r
    added = sum(1 for r in rows if r["id"] not in existing)
    for r in rows:
        existing[r["id"]] = r
    ordered = sorted(existing.values(), key=lambda r: r["timestamp"])
    # Write to a temp file first: a failed run must never leave a truncated log behind.
    tmp = CSV_PATH.with_suffix(".csv.tmp")
    with tmp.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(ordered)
    tmp.replace(CSV_PATH)
    return added, len(rows) - added


def main() -> int:
    token = os.environ.get("IG_LONG_LIVED_TOKEN", "")
    account_id = os.environ.get("IG_BUSINESS_ACCOUNT_ID", "")
    if not token or not account_id:
        log("config_error", missing=[k for k, v in {"IG_LONG_LIVED_TOKEN": token, "IG_BUSINESS_ACCOUNT_ID": account_id}.items() if not v])
        return 2
    try:
        check_token_expiry(token)
        rows = fetch_stories(account_id, token)
    except GraphError as e:
        log("capture_failed", error=str(e))
        return 1
    added, updated = upsert(rows)
    log("capture_ok", active_stories=len(rows), added=added, updated=updated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
