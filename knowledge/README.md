# Knowledge

Human-reviewable judgement. Numbers live in SQLite, not here.

Every file starts with front-matter:
```yaml
---
owner: brand-curator          # exactly one owning agent
lang: fa-IR                   # or en
status: draft | active | superseded
updated: 2026-07-25
sources: [c_20260801_x, ...]  # content_ids or permalinks backing the claims
---
```

```
brand/      voice, mission-vision, positioning, beliefs, glossary, banned-patterns
audience/   personas, insights (evidence-backed), comment/DM themes
content/    pillars, plan/<week>.md, briefs/<content_id>.md, hook-library
market/     competitor set, patterns, saturation, manual-observations
journal/    decisions and lessons, one file per month
_archive/   superseded material, never deleted
```

Rules for writing here: see `KNOWLEDGE_MANAGEMENT.md` (canonical policy) and `agents/README.md` (file ownership). In short: one owner per file, update in place, cite `content_id`s for performance claims.
