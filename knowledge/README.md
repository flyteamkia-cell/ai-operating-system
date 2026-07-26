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

Rules: one owner per file · update in place, do not fork near-duplicates · claims about performance cite `content_id`s · superseded content moves to `_archive/` with a reason.
