# ADR-0001 — Platform shape: modular monolith, file-first

Status: Accepted · Date: 2026-07-25 · Owner: Architecture

## Context
Single operator, one brand today, additional business domains (VIP channel, market analysis, CRM, education) expected within 1–3 years. The initial design proposed a distributed set of services, an orchestrator, a vector database and a dashboard before any data existed.

## Decision
One TypeScript repository, modular monolith, exposed as a single CLI. Modules are separated by domain boundary (`connectors`, `ingest`, `analysis`, `context`, `knowledge`, `reporting`) with explicit interfaces and no cross-module imports except through published module APIs. Git is the source of truth for everything a human should be able to review.

## Alternatives
- **Distributed services from day one** — rejected: operational cost with no scaling requirement; each service multiplies failure modes for one user.
- **No-code workflow platform as the backbone** — rejected: logic outside version control cannot be reviewed, tested or diffed (ADR-0003).
- **Notion/Airtable as the store** — rejected: vendor becomes the schema owner; migration cost grows with data.

## Consequences
+ New business domains are added as modules on the same core; no re-platforming.
+ Every behaviour is testable locally and reviewable in a diff.
+ Onboarding a future developer requires one repository.
− Long-running or event-driven workloads will eventually require a scheduler and possibly a queue. Trigger to revisit: any workflow needing sub-hourly reaction to external events, or a second human operator.
