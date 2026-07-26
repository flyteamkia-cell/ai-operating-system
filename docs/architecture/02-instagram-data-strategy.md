# 02 — Instagram Data Strategy

This is the highest-risk dependency in the system. It is isolated behind `src/connectors/instagram/` so that a platform change is a one-module rewrite.

## What is actually obtainable

**Own account (Instagram Graph API, requires a Business/Creator account linked to a Facebook Page):**
media list, captions, permalinks, timestamps, media type, and per-media insights — reach, impressions/views, likes, comments, saves, shares, plays, average watch time for reels, plus account-level follower counts, profile visits and audience demographics (demographics require a follower-count threshold). Story insights are available only within their lifetime, so stories **must** be captured on a schedule or their data is lost permanently.

**Competitor accounts (`business_discovery` on the Graph API):**
username, followers_count, media_count, and per-media: caption, media_type, timestamp, permalink, like_count, comments_count. Target accounts must themselves be Business/Creator accounts.

**Not obtainable for competitors, by any supported means:** saves, shares, reach, watch time, retention, story data, follower demographics.

## Consequence for the analysis design
Competitor comparison must use a **followers-normalized public engagement proxy** — `(likes + comments) / followers_count` — and must never be compared numerically against own-account metrics that include saves/shares/reach. Mixing them produces confident nonsense. The Market Signal agent is therefore restricted to structural and topical conclusions (hook patterns, formats, topics, cadence, caption structure, comment sentiment) plus relative ranking *within* the competitor set.

## Rejected: scraping / browser automation as the primary path
Fragile against UI changes, rate-limited by anti-automation systems, violates platform terms, and risks the account that the entire business depends on. Permitted only as a **manual, human-triggered, low-frequency** fallback for qualitative sampling, never as a scheduled job the system depends on.

## Backfill limitation
Insights are not retroactive for periods before the account became a Business account, and historical windows are limited. Baseline capture starts on day one of Phase 1 — every day of delay is permanently lost data. Any pre-existing history must be captured manually via account data export.

## Failure policy
Token expiry (long-lived tokens require periodic refresh), rate limiting and API version deprecation are expected, not exceptional. The connector implements: token-refresh job with expiry alerting ≥7 days ahead, exponential backoff with jitter, per-run partial-failure reporting, and a hard rule that a failed ingest never overwrites a prior good snapshot.
