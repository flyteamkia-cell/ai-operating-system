# 03 — Cost, Model and Token Policy

Cost is a first-class architectural constraint. The design target is a **stable monthly AI spend that does not grow with corpus size**. That property comes from the Context Pack layer, not from prompt discipline.

## Model tiering
| Task class | Model tier | Rationale |
|---|---|---|
| Architecture decisions, weekly strategy, monthly retro, experiment verdicts | Frontier (Opus-class) | Low frequency, high leverage, irreversible consequences |
| Brief writing, script/hook/caption drafting, competitor pattern naming, knowledge diff proposals | Mid (Sonnet-class) | High volume, quality-sensitive, bounded |
| Tagging, classification, dedup detection, formatting, transcription cleanup | Small (Haiku-class) | Mechanical, verifiable, high volume |
| Counting, ranking, aggregation, comparison, thresholds | **No model** | Deterministic code |

## Context Pack contract
Every agent invocation receives exactly one pack, assembled by `src/context/`:
- Hard ceiling: 8,000 tokens (brand core ≤2k, performance summary ≤3k, market signal ≤2k, task input ≤1k).
- The brand core segment is byte-stable between changes so it can be served from prompt cache.
- Packs are content-addressed and logged with each run; any output can be reproduced from its pack hash.
- Growth of `knowledge/` must not grow the pack. If a pack exceeds ceiling, the fix is better selection, never a bigger budget.

## Ledger
Every model call appends to `data/logs/llm.jsonl`: timestamp, agent, prompt id+version, model, input/output tokens, cost, pack hash, latency, outcome. `aios cost --month` produces the report. A weekly cycle whose cost exceeds the configured ceiling fails loudly instead of silently spending.

## Caching
- Raw API responses cached by (endpoint, params, day). Re-runs of an analysis cost zero API calls.
- Deterministic analysis outputs cached by input hash.
- Prompt caching for the stable brand core segment.

## Anti-patterns, banned
Sending raw metric JSON to a model. Asking a model to compute an average or pick a maximum. Re-summarizing the same document every run instead of storing the summary. Multi-agent "discussion" loops. Unbounded retries.
