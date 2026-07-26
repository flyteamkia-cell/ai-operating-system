# ADR-0003 — No workflow orchestrator until Phase 6

Status: Accepted · Date: 2026-07-25 · Owner: Architecture

## Context
The initial design put n8n at the centre as "the automation engine". Workflows are the part of this system most likely to change weekly.

## Decision
Phases 1–5 use typed CLI commands (`aios ingest`, `aios analyze`, `aios cycle`) invoked by cron or GitHub Actions. Every workflow is code: reviewable, testable, diffable, and reproducible on a laptop. Orchestrator adoption is reconsidered at Phase 6 against explicit criteria.

## Adoption criteria for an orchestrator (all three must hold)
1. ≥3 external systems requiring event-driven fan-out (not schedules).
2. A non-engineer needs to modify workflows.
3. Retry/queue semantics beyond what a CLI + cron + a job table provides.

## Consequences
+ No hosted service, no second logic store, no vendor lock-in during the phase where the design changes most.
+ Workflow bugs are caught by tests, not discovered in production.
− Schedules are the operator's responsibility; mitigated by `aios doctor` (health/freshness check) and failure notifications from Phase 1.
