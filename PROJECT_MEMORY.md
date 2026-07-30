# Project Memory

Long-lived memory for future AI sessions. This file holds only what an assistant
could realistically lose across long-term development. It does **not** restate the
README, ADRs, Architecture, Roadmap, or Constitution — see references below.

---

## Project Identity

Persian-language financial-markets personal brand on Instagram. The deliverable is
an operating platform, not a content generator.

## Long-term Vision

A modular AI operating system that ingests data, runs deterministic analytics,
manages knowledge, generates content briefs, watches competitors, and learns from
its own results. Each business domain (content, VIP channel, market analysis, CRM)
mounts as an independent module on a stable core, added without rewriting it.

## Current Phase

Phase 0 — documentation only. No `src/` code exists or should be written.
Code follows documentation. Phase 1 does not begin until blockers B1–B5 are cleared.

## Active Blockers (B1–B5)

These gate Phase 1. All open.

- **B1** — Instagram Business/Creator account status confirmation.
- **B2** — Definition of the primary conversion event driving content strategy.
- **B3** — Current account performance baseline.
- **B4** — Execution environment and monthly cost ceiling (partially resolved by ADR-0006).
- **B5** — List of 15–25 competitor accounts.

## Stable Architectural Invariants (not documented elsewhere)

Cross-cutting rules that no single ADR fully owns and that are easy to lose mid-development:

- `content_id` is the architectural spine: idea → published content → performance metrics → lessons learned. It must remain stable and never be reassigned.
- Reports and generated analytical output are always **derived**, never canonical. Canonical state lives in SQLite (facts, metrics, lineage) and `docs/` (decisions, brand, knowledge).
- Chat is temporary; knowledge is permanent. Durable conclusions are promoted into canonical documents, not left in conversation or in generated reports.
- No module, agent, or workflow calls an LLM provider directly. All AI requests pass through the abstraction boundary — even while only one provider exists and its interfaces remain deferred under YAGNI.
- No workflow orchestrator is introduced until the defined trigger conditions are met.
- Competitor data comes only from the Instagram Graph API `business_discovery` endpoint. No scraping.

## References to Canonical Documents

Do not duplicate these; consult them.

- `README.md` — entry point and document index.
- `docs/adr/` — ADR-0001 through ADR-0006 (locked architectural decisions).
- Architecture docs — system structure and data model.
- `docs/roadmap/roadmap.md` — phases and acceptance criteria.
- Constitution / agent specs — Performance Analyst, Market Signal, Content Strategist, Brand Curator.

## Important Reminders for Future Implementation

- **Workflow is Atomic Change + approval-gated.** One logical concern per change; minimal files; extend canonical docs rather than create new ones; propose exact diffs and wait for explicit `APPLY` / `IMPLEMENT` / `EXECUTE` before modifying any file. Typo fixes exempt. Stop after each approved change.
- **Documentation-first.** Docs precede code. No architecture expansion without approval.
- **Deferred items** (parked, do not action unless explicitly requested): Reports Ownership Proposal, LLM roadmap YAGNI amendment, SQLite-durability-on-ephemeral-runners risk.
- **Known unresolved architectural risk** (tracked mentally, not yet in a backlog file): the canonical SQLite database has no defined persistence mechanism across ephemeral GitHub Actions runners. Must be resolved before the first stateful scheduled workflow.
- **Environment:** Windows, PowerShell, Git. Repo at `C:\projects\ai-operating-system`. Watch for PowerShell/Git first-time pitfalls (command spacing, multi-line paste, `Expand-Archive` requiring a `.zip` extension).
