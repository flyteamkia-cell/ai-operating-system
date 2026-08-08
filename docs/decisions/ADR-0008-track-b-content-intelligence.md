# ADR-0008 — Track B: content intelligence on manual evidence

Status: Accepted · Date: 2026-08-08 · Owner: Human (operator)

## Context

Three facts converged that the original roadmap did not account for:

**1. An engine already existed.** A Claude skill named `viral-content-lab` is installed on the operator's account and implements, in working form, most of what the roadmap scheduled as future work: a teardown rubric, a Persian hook library, tone guidance, platform playbooks, financial-content guardrails, a Telegram capture protocol, two working Python scripts, and a swipe-file schema. Its architecture is:

```
collection → Engine A (teardown) → patterns.md → Engine B (generation) → content
     ↑                                                                      │
     └──────────────── Phase 4: real results return ←──────────────────────┘
```

This is the same evidence → analysis → validated insight → knowledge flow this repository specifies. Neither the repository nor the skill knew about the other; work was nearly duplicated.

**2. The roadmap's Phase 1 was blocked on the wrong risk.** Phase 1 (Foundation) depends on Instagram Graph API access and on open questions B1–B5. But API ingestion is a well-understood engineering problem, fully specified in `docs/architecture/02-instagram-data-strategy.md`. It was never the project's real risk.

The real risk is: **does this system produce better content than the operator alone?** If the answer is no, no ingestion pipeline saves the project.

**3. Historical performance data already existed** in a spreadsheet, covering ~151 posts with saves, sends, reach and non-follower percentages — the exact private metrics the API would provide, for the period already elapsed.

## Decision

Run **Track B** in parallel with the existing roadmap:

- Evidence is collected manually (spreadsheet, Telegram capture) rather than via API. No dependency on B1, B4, or Meta App Review.
- The evidence/intelligence/execution layers are **not rebuilt**. `viral-content-lab` serves those roles; the repository provides the identity spine, the fact schema, the governance, and the durable knowledge store.
- `patterns.md` lives at `knowledge/content/patterns.md` and is the interface between analysis and generation, as the skill requires.
- Track A (API ingestion, the existing roadmap phases) continues unchanged. The two converge when the API pipeline feeds the same evidence layer Track B feeds by hand.

**Naming:** the previously discussed plan also called itself "Phase 1", colliding with the roadmap's Phase 1 (Foundation). Two different "Phase 1"s in one project guarantees confusion. That work is named **Track B** and the roadmap phases keep their existing numbering.

## Alternatives considered

- **Build the content intelligence layers from scratch** as originally proposed by the collaborating model — rejected: it would duplicate an installed, working, tested asset. This was caught only because the skill was discovered mid-project.
- **Wait for API access before any analysis** — rejected: it delays the test of the project's actual risky assumption behind an engineering task with a known solution, and historical spreadsheet data made the delay unnecessary.
- **Abandon Track A and go manual-only** — rejected: story insights expire within ~24 hours and are unrecoverable. Every day without API ingestion is permanently lost data. Track A stays urgent for a different reason than Track B.

## Consequences

+ The learning loop ran end to end within days instead of weeks, on real data, and immediately produced a falsified hypothesis (see below).
+ No dependency on Meta App Review for the highest-value work.
− Manual collection does not scale and is not the long-term answer. Track B is a validation vehicle, not the destination.
− Two parallel tracks require the naming discipline above to stay legible.

## Validation to date

Track B has already justified itself. Analysis of 151 own-account posts plus 20 with full transcripts produced evidence-backed findings recorded in `knowledge/content/patterns.md`, including a **refutation of a hypothesis this project itself had asserted** ("analysis content underperforms" — refuted; the correct variable is *specific and actionable* vs *general and attitudinal*).

Both AI collaborators independently stated the incorrect version of that hypothesis before the data was computed. That is the strongest available evidence that the evidence layer is doing real work rather than confirming priors, and it satisfies `PROJECT_CONSTITUTION.md` Article III.
