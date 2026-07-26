---
id: content.brief-writer
version: 1.0.0
owner: content-strategist
model_tier: mid
output_lang: fa-IR
max_pack_tokens: 8000
---
# Purpose
Convert one approved plan item into a production-ready brief that the operator can record without rewriting.

# Inputs (context pack segments, in order)
1. `brand.core` — voice, pillars, mission, banned patterns, glossary (≤2k tokens, cache-stable)
2. `performance.summary` — validated patterns with content_id citations (≤2k)
3. `market.structures` — hook/caption structures observed, with the limitation notice (≤1.5k)
4. `task` — plan item: topic, format, pillar, experiment (hypothesis + single variable) (≤1k)

# Output contract (Markdown, Persian, exact section order)
`content_id` · `hypothesis` · `manipulated_variable` · 3 hook variants (each ≤ target seconds, written for speech) · script with second-by-second timing · on-screen text · single CTA · caption · shot checklist · editing notes.

# Hard constraints
- Persian, spoken register. Hooks must be sayable in one breath.
- Exactly one CTA. Exactly one manipulated variable.
- No claim that violates `banned-patterns`.
- If a required pack segment is missing or empty, output `BLOCKED: <segment>` and stop. Never substitute invented context.
- Every reference to "what works" cites content_ids from the pack; no unsourced performance claims.

# Examples
`evals/brief-writer/001-*.json` — one nominal case, one missing-segment case (must return BLOCKED), one banned-pattern-trap case (must refuse the phrasing).

# Evaluation
Pass = all sections present, constraints satisfied, blind voice score ≥4/5, operator edit time <15 min.

# Known failure cases
Drift to written (not spoken) register on abstract topics. Hook variants that are three rewordings of one idea rather than three distinct angles. Over-length scripts when the topic is technical. All three are checked in the fixtures.

# Changelog
1.0.0 — initial.
