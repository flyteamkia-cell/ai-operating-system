# Critique of the initial design (v1.0 PDD)

Kept: layered separation, knowledge-management-as-architecture, documentation-first, feedback loop as the core asset, module-per-business-domain long-term shape.

Cut or deferred, with reasons:

| Proposed | Verdict | Reason |
|---|---|---|
| 9–12 concurrent agents | Cut to 4 | Agent count is a cost and failure surface, not capability. Each agent needs evals, a memory policy and an owner. Four cover the whole loop. |
| n8n as the automation engine | Deferred to Phase 6 | Adds a hosted service and a second source of truth for logic — un-diffable, un-testable workflow state. A typed CLI + cron gives the same result inside git history. Adopt n8n only when >3 external systems need event fan-out. |
| Vector DB (Qdrant/pgvector) | Deferred indefinitely | At 10²–10³ documents, deterministic selection by tag/date/performance beats embedding retrieval. Trigger to revisit: >2,000 knowledge chunks. |
| PostgreSQL / Supabase | Deferred | Single writer, single user, <10⁶ rows. SQLite is the correct scale answer; migration path is trivial (ADR-0002). |
| Next.js dashboard | Deferred to Phase 7 | A dashboard for one person who already reads Markdown is a maintenance liability. Weekly reports are generated files. |
| Langfuse / OpenTelemetry / Sentry | Deferred | Observability is required; a vendor stack is not. Structured JSONL run logs + a cost ledger cover Phases 1–5. |
| Browser automation / scrapers for competitors | Rejected as primary path | Instagram Graph `business_discovery` is the supported, stable path and covers most of the requirement (ADR-0005). Scraping guarantees silent breakage on someone else's schedule. |
| Multi-platform publishing (X, LinkedIn, TikTok, YouTube) | Deferred | Publishing automation optimizes the cheapest step in the chain. The expensive steps are judgement and feedback. |
| "Curator reviews every chat message" | Reshaped | Continuous interception is unbounded token cost. Curation runs as an explicit end-of-session and weekly diff-based job. |

Two things the original design **missed entirely**, now central:

1. **The identity spine.** Nothing linked an idea to a published media ID to its metrics. Every "learning" claim would have been unfalsifiable. Fixed by `content_id` (`architecture/01-data-model.md`).
2. **Falsifiability.** "Analyze why reel #23 worked" over a sample of one, with no declared hypothesis, produces confident narrative and zero knowledge. Every brief now declares a hypothesis and exactly one manipulated variable (`Experiment`).

One correction on the business framing: the proposed KPI set (reach, saves, retention, follower growth) is entirely upstream. Without a defined conversion event the system will optimize for reach — the cheapest and least valuable outcome for a financial-markets brand. Open question **[B2]**.
