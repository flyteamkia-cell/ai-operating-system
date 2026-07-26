# 00 — System Overview

## Shape
Modular monolith, TypeScript, one repository, one CLI binary. Git is the source of truth for knowledge and configuration; SQLite is the source of truth for measurements. No service mesh, no message bus, no orchestrator in v1 (ADR-0001, ADR-0003).

## Pipeline
```
 external APIs ──► ingest ──► raw store (JSONL, immutable, date-partitioned)
                                  │
                                  ▼
                            normalize ──► SQLite (facts, idempotent upsert)
                                  │
                                  ▼
                            analysis (deterministic: aggregation, ranking, deltas, cohorts)
                                  │
                                  ▼
                          context packs (≤8k tokens, deterministically assembled)
                                  │
                                  ▼
                    reasoning (Claude) ──► artifacts: briefs, reports, proposed knowledge diffs
                                  │
                                  ▼
                     human gate ──► knowledge/ (git commit) ──► next cycle
```

## The five rules that make this scale
1. **Deterministic before probabilistic.** Anything countable is counted in code. The model is never asked to compute, only to judge, name patterns, and write.
2. **Context Packs, not file dumps.** `src/context/` builds a bounded, cached, versioned pack per agent invocation. Cost and quality are governed here, not inside prompts.
3. **Append-only raw layer.** Ingested payloads are never mutated. Every derived table can be rebuilt from raw; a normalization bug is never data loss.
4. **Human gate on knowledge writes.** Agents propose diffs to `knowledge/`; a human (or an explicit `--auto` flag with a passing eval) merges. Self-writing knowledge without a gate degrades within weeks.
5. **One writer per file.** Every file under `knowledge/` and `docs/` has exactly one owning agent, declared in front-matter. No concurrent authorship.

## Component ownership
| Component | Path | Owner |
|---|---|---|
| Ingestion connectors | `src/connectors/` | Architecture |
| Fact store | `src/db/` | Architecture |
| Deterministic analysis | `src/analysis/` | Architecture |
| Context packs | `src/context/` | Architecture |
| Brand knowledge | `knowledge/brand/` | Brand Curator agent |
| Audience & performance knowledge | `knowledge/audience/` | Performance Analyst agent |
| Market/competitor knowledge | `knowledge/market/` | Market Signal agent |
| Briefs & scripts | `knowledge/content/` | Content Strategist agent |
| ADRs, roadmap | `docs/` | Human + Architecture |

## What the system is explicitly not doing in v1
Auto-publishing; video generation; multi-platform distribution; real-time market data; CRM; any autonomous action with external side effects. All side effects in v1 are: read external APIs, write local files, open a git branch.
