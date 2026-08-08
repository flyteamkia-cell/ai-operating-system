# 00 — System Overview

## Organizing Principle: Goal-Driven, Capability-Based
The system organizes around **capabilities** — ingest, analyze, plan, draft, curate, publish, learn — mapped to **goals**: grow qualified audience (see `README.md` § North Star Metric), sustain brand voice, minimize cost, minimize vendor risk. It does not organize around a fixed org chart of named agents. A capability can be served by a human, a script, or a model call, through any compliant provider, without changing how the rest of the system invokes it. An Agent (see `agents/`) is one possible implementation of a capability, adopted per `PROJECT_CONSTITUTION.md` Article IX — not the default unit of design.

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

## LLM Abstraction Layer (Multi-Provider)
No module, agent, or workflow calls a provider SDK directly (`PROJECT_CONSTITUTION.md` Article IV). Every reasoning request passes through a `ProviderManager` behind one interface (`complete`, `stream`, and `embed` if ever needed), implemented as pluggable adapters.

```
Capability / Agent / Workflow
              │
      LLM Abstraction Layer
              │
        Provider Manager
              │
   ─────────────────────────
   1. Claude   (default — see 03-cost-and-model-policy.md for Opus/Sonnet/Haiku tiering)
   2. OpenAI
   3. Gemini
   4. Other compatible providers
   5. Local models (future)
```

- **Smart routing** evaluates task complexity, context length, reasoning/coding requirement, latency need, expected tokens, cost, availability and rate limits before selecting a model; default to the smallest/cheapest model meeting the quality bar. The strongest model is never the default choice.
- **Failover**: preferred provider unavailable → retry → fall back down the priority list → log the reason. A workflow never hard-stops on a single provider outage.
- **Business logic never knows which provider served a request.** Provider identity is routing metadata, not a business input.
- Gateways (e.g. OpenRouter, LiteLLM) and official SDKs are both permitted adapter implementations; the choice per provider is a documented trade-off — advantages, disadvantages, migration impact, cost — not a fixed rule.
- Note: this layer selects *which provider*; `03-cost-and-model-policy.md`'s tiering selects *which model within the active provider*. The two are independent axes.
- This layer is a documentation and interface commitment as of Phase 0; implementation lands in Phase 1/2 (`docs/roadmap/roadmap.md`), not before.

## Orchestrator and Event-Driven Stance
No workflow orchestrator platform in the current phases (ADR-0003): typed CLI + cron carries Phases 0–4. Adoption is reconsidered only against ADR-0003's three stated triggers. Consistently, the default execution model is synchronous, scheduled, and sequential — a pipeline, not an event bus. Event-driven mechanisms (webhooks, queues, pub/sub) are introduced only for a specific, named requirement — never as general infrastructure ahead of that need (`PROJECT_CONSTITUTION.md` Article VIII).

## Learning Loop as First-Class Architecture
The feedback loop shown at the bottom of the pipeline above — human gate → knowledge/ → next cycle — is not a downstream feature; it is the reason the identity spine (`content_id`, see `01-data-model.md`) exists at all. Every phase from Phase 1 onward (`docs/roadmap/roadmap.md`) keeps this loop intact even as its automation level changes (`PROJECT_CONSTITUTION.md` Article III).

## SaaS-Ready Constraints (apply now, activate later)
Phases 0–5 are single-tenant, but the following are enforced from the start so a future SaaS phase does not require re-architecture:
- No core interface hard-codes an assumption of exactly one Instagram account, one knowledge base, or one operator identity — a tenant boundary exists conceptually even while the config has one entry.
- The cost ledger and provider routing are already per-request-attributable, a prerequisite for multi-tenant billing.
- Knowledge storage and the fact store stay filesystem/SQLite-portable so a future multi-tenant migration is additive, not a rewrite.
- No feature is built in a way that assumes it can never be exposed to a second operator.

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
| ADRs | `docs/decisions/` | Human + Architecture |
| Roadmap | `docs/roadmap/roadmap.md` | Human + Architecture |

## What the system is explicitly not doing in v1
Auto-publishing; video generation; multi-platform distribution; real-time market data; CRM; any autonomous action with external side effects. All side effects in v1 are: read external APIs, write local files, open a git branch.
