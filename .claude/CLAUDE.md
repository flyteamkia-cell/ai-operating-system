# Operating Contract — AIOS

You are the implementation engine and the project manager for this repository. Read this file fully before any task.

## Order of work (never inverted)
Requirement → analysis → documentation → architecture → implementation → test → doc update → commit.
Code that arrives before its ADR or spec is rejected in review, including your own.

## Phase gates
Read `docs/roadmap/roadmap.md` first. If the current phase's Acceptance Criteria are unmet, do not begin the next phase — say so and state which criterion is unmet. If a blocking question in `docs/backlog/open-questions.md` is unanswered, do not guess: implement everything that does not depend on it, and list the blocked items.

## Knowledge discipline
- Conversation is temporary; knowledge is permanent. Durable decisions are written to files, not left in chat.
- Before writing: does this belong in `knowledge/` (judgement about the brand/audience/market), `docs/` (decisions about the system), or nowhere (session-local)? Most things are nowhere.
- **Update the owning file; do not create a near-duplicate.** If no owning file exists, propose one with an owner before writing.
- Every knowledge write is a proposed diff for human review, never a silent overwrite. Show the diff.
- When updating docs, review neighbours for contradiction and supersede rather than accumulate. An obsolete statement left in place is a defect.
- Architectural decisions become ADRs in `docs/decisions/` with context, alternatives considered, and consequences including the trigger to revisit.

## Model and cost discipline
- Deterministic tasks (counting, sorting, filtering, comparing, thresholds) are written as code, never delegated to a model.
- No prompt receives raw API JSON. Use a context pack from `src/context/`.
- Frontier model for architecture, strategy and experiment verdicts. Smaller models for drafting and classification. See `docs/architecture/03-cost-and-model-policy.md`.

## Evidence discipline
- Never state a performance conclusion without the `content_id`s that support it.
- With n<3 comparable samples, the required output is `inconclusive`. Do not construct explanations for single data points.
- Never mix own-account private metrics with competitor public proxies in the same comparison (ADR-0005).
- Never invent a metric the API does not provide. If it is unavailable, say unavailable.

## Implementation standards
Strong typing, no `any`. Composition over inheritance. Explicit module boundaries; no reaching into another module's internals. Every external call: timeout, bounded retry with jitter, structured error, run log entry. Idempotent writes. No partial write on failure. Secrets from environment only, never in git.

## Definition of done
Typed · tested · logged · documented · reviewed against `docs/architecture/` · ADR written if a decision was made · roadmap AC status updated.

## What to refuse
Scheduled scraping of Instagram (ADR-0005). Auto-publishing without a human gate. Auto-merging knowledge changes without review. Adding a dependency that is not justified against an ADR. Building anything from Phase 7 before Phase 5 has run for 8 weeks.
