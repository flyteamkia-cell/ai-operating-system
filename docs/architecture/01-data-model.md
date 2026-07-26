# 01 — Data Model

## The spine
```
Experiment 1─n Content 1─n Publication 1─n MetricSnapshot
                  │
                  └─n Lesson (markdown, references content_id)
```
`content_id` is minted **at idea time**, before any work exists, and never changes:
`c_<YYYYMMDD>_<slug>` e.g. `c_20260801_liquidity-trap-hook`.
It appears in: the brief filename, the git branch, the recording file name, the caption draft, the DB row, the lesson. This is the only thing that makes the feedback loop auditable.

## Split of responsibility
| Data kind | Store | Why |
|---|---|---|
| Counts, timestamps, IDs, metric snapshots | SQLite | Queryable, joinable, idempotent |
| Judgements, voice, strategy, lessons, briefs | Markdown + YAML front-matter in git | Diffable, reviewable, human-editable, model-readable |
| Raw API payloads | JSONL under `data/raw/<source>/<date>/` | Replayable, immutable |
| Media (video/images) | Outside git (local/cloud path referenced by ID) | Never bloat the repo |

## Entities
**Experiment** — `experiment_id`, hypothesis, manipulated variable (exactly one), control definition, success metric, minimum sample, start/end, verdict (`pending|supported|refuted|inconclusive`).

**Content** — `content_id`, slug, format (`reel|carousel|story|post|live|article`), pillar, status (`idea|briefed|recorded|edited|scheduled|published|archived`), `experiment_id?`, `brief_path`, hook_type, cta_type, topic tags, created/updated.

**Publication** — `publication_id`, `content_id`, platform, `platform_media_id`, permalink, `published_at`. Unique on (platform, platform_media_id). A single Content may have several Publications (reel + story teaser).

**MetricSnapshot** — (`publication_id`, `age_bucket`) primary key, buckets `h24|h72|d7|d30`. Fixed buckets, not arbitrary timestamps: without them cross-post comparison is meaningless because posts are measured at different ages. Stores normalized columns plus the full `raw_json`.

**CompetitorAccount / CompetitorPost** — public metrics only (see `02-instagram-data-strategy.md`), with `followers_at_capture` so engagement can be normalized retroactively.

**IngestRun** — every ingestion writes a run row: source, window, started/finished, status, item count, error. No silent partial ingests.

## Derived metrics (computed, never stored raw)
- `engagement_rate = (likes+comments+saves+shares) / reach`
- `save_rate`, `share_rate` — the two that actually predict distribution for educational finance content
- `hold_rate = avg_watch_seconds / video_length_seconds` (own account only)
- `follower_conversion = follows / reach`
- `pillar_index` = pillar mean vs. account mean, z-scored over trailing 90 days

## Rebuild guarantee
`aios rebuild` drops all derived tables and replays `data/raw/` into SQLite. Any analysis bug is a code fix plus a replay, never a data-recovery incident.
