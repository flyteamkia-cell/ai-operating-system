# 04 — Collection Schema Mapping

Documentation only. Ingestion code is deliberately not written yet: code written against imagined data is code written twice.

This maps the manual collection format (swipe-file CSV / Telegram `#سواپ` capture / Google Sheet) onto the fact tables in `01-data-model.md`, and states which fields are permanently unobtainable.

## Field mapping

| Collected field | Destination | Notes |
|---|---|---|
| `post_id` | — | Local sequence only. Replaced by `content_id` on import; never used as a key. |
| `account` | `competitor_account.username` | Own posts skip this table. |
| `account_followers` | `competitor_post.followers_at_capture` | **Mandatory.** Without it no cross-account comparison is valid. |
| `platform`, `format` | `content.format` / `publication.platform` | |
| `post_url` | `publication.permalink` | |
| `post_date` | `publication.published_at` | |
| `topic` | `content.topics` | Free text today; see taxonomy note below. |
| `views` | `metric_snapshot.views` | |
| `likes`, `comments` | `metric_snapshot.likes` / `.comments` | Public — available for any account. |
| `shares_sends` | `metric_snapshot.shares` | **Own account only.** |
| `saves` | `metric_snapshot.saves` | **Own account only.** |
| `duration_sec` | `publication.duration_seconds` | Required for `hold_rate`. |
| `avg_watch_sec` | `metric_snapshot.avg_watch_seconds` | Own account only. |
| `retention_pct` | derived, not stored | Computed from watch time and duration. |
| `transcript_file` | `content.brief_path` sibling | Text lives outside the fact store. |
| `why_i_picked_it` | — | Human hunch. Never treated as a finding. |

## Structural fields (added for Track B)

These carry the transcript-level dimension the numeric data lacks. All are objective — two people reading the same post should produce the same value. See `docs/governance/extraction-template-fa.md` for the operator-facing version.

| Field | Type | Status |
|---|---|---|
| `hook_verbatim` | text, word-for-word | Never paraphrase — analysis runs on the actual words |
| `hook_type` | enum, data-derived taxonomy | Validated |
| `has_specific_number` | bool | Validated |
| `actionable` | yes / partial / no | **Validated — the strongest variable in the dataset** |
| `promise_kept` | yes / partial / no | Validated |
| `cta_verbatim` | text | |
| `cta_type` | enum | Validated |
| `evergreen` | bool | Not yet tested |

**Rejected fields.** A multi-model proposal included `hook_strength`, `curiosity`, `emotion`, `authority`, `cta_strength`, `complexity`, and `virality_score`. All are model judgements rather than observations. Learning that "high model-rated curiosity correlates with sends" discovers the model's scoring habit, not a property of the content — a closed loop. `virality_score` is worse still: it is an *outcome*, and having a model assign it substitutes prediction for measurement.

Rule: **if two independent people cannot fill a field identically, it is not data.**

## Permanently unavailable for competitor accounts

`saves` · `shares_sends` · `reach` · `avg_watch_sec` · `retention_pct` · story metrics · follower demographics

Platform limitation, not a system limitation; no automation resolves it (ADR-0005). Consequences:
- Competitor ranking uses `(likes + comments) / followers_at_capture` and is comparable **only within the competitor set**.
- Never place competitor proxies and own-account private metrics in the same comparison.
- Peer accounts sharing their own insights are a distinct, higher tier — they do have saves and sends. Keep in separate files with their own confidence weighting: **own > peer > competitor**.

## Topic taxonomy — open issue

Topic labels are currently free text ("تحلیل", "همستر", "ارز جدید"), which forced keyword-based clustering during analysis and produced a mislabelled cluster — this is what caused the initial "analysis underperforms" claim later refuted in `knowledge/content/patterns.md`.

A standard taxonomy is needed, built on **function** rather than subject matter. Functional grouping is what predicts performance; subject grouping does not. Deferred until enough labelled data exists to derive the categories from evidence rather than inventing them.
