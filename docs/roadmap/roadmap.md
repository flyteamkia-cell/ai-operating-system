# Roadmap — phases and gates

Rule: a phase does not start until every Acceptance Criterion of the previous phase is verifiably met. Criteria are measurable; "it feels good" is not a criterion. Durations assume a part-time operator.

---
## Phase 0 — Architecture (current)
Deliverables: this repository, ADRs 0001–0005, data model, ingestion strategy, cost policy, agent specs, open-questions backlog.
**AC:** all five blocking questions in `docs/backlog/open-questions.md` answered; API access confirmed working with a live token.
Blocked on: [B1]–[B5].

---
## Phase 1 — Truth Layer (1–2 weeks)
Own-account ingestion, SQLite schema, `content_id` spine, daily/scheduled snapshot capture, `aios doctor`, run logging.
**AC:**
1. All available own-account history in SQLite; a full `rebuild` from raw reproduces it byte-identically.
2. Story insights captured on schedule for 7 consecutive days with zero gaps.
3. Every post published from now on has a `content_id` present before publication.
4. `aios report --weekly` produces a factual performance report with no LLM involvement.

Deliberately no AI in this phase. A model on top of unreliable data produces confident errors.

---
## Phase 2 — Brand Knowledge Core (1–2 weeks)
`knowledge/brand/` populated (voice, mission/vision, positioning, beliefs, banned patterns), audience personas grounded in actual comment/DM data, content pillars defined with a measurable definition each.
**AC:**
1. Blind test: 5 captions, mixed system-drafted and operator-written; operator rates system drafts ≥4/5 on voice fidelity.
2. Every pillar has a written definition precise enough that two people classify 20 past posts with ≥90% agreement.
3. `banned-patterns.md` exists and the drafting prompt provably respects it across 10 samples.

---
## Phase 3 — Content Engine (2 weeks)
Brief generation (hook, script, CTA, caption, on-screen text, shot checklist, editing prompt), one Claude Code skill, prompt versioning + eval fixtures.
**AC:**
1. 8 briefs generated; ≥6 used with <15 minutes of operator editing each.
2. Time from idea to ready-to-record script ≤20 minutes.
3. Every brief carries a hypothesis and exactly one manipulated variable.

---
## Phase 4 — Market Signal (1–2 weeks)
`business_discovery` ingestion for the tracked account set, structural pattern extraction, weekly market report with stated limitations.
**AC:**
1. ≥15 accounts ingested weekly with <5% failure rate.
2. Weekly report identifies ≥3 structural patterns, each traceable to specific media IDs.
3. No report conflates competitor public proxies with own-account private metrics.

---
## Phase 5 — Learning Loop (2 weeks)
Experiment registry, verdicts at sample thresholds, monthly retro, curated lessons, knowledge diffs proposed against `knowledge/`.
**AC:**
1. ≥6 experiments closed with explicit verdicts including at least one `refuted`. (A system that never refutes anything is not measuring.)
2. Monthly retro generated automatically and merged after human review.
3. Every lesson references ≥3 `content_id`s. Single-sample lessons are rejected.

---
## Phase 6 — Automation & Reliability (1–2 weeks)
Unattended scheduling, retries, alerting, cost ceilings, orchestrator decision reviewed against ADR-0003 criteria.
**AC:** 14 consecutive days of unattended weekly cycles; every failure produced a notification within 1 hour; monthly cost within ceiling.

---
## Phase 7 — Expansion (ongoing)
Second domain module (VIP channel / market research / education) on the same core, publishing automation, reporting surface. Not before Phases 1–5 have run for 8 weeks with real content.
