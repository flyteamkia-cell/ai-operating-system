# Roadmap

Canonical phase list and gates — the single authoritative roadmap for this project. Rule: a phase does not start until every Acceptance Criterion (AC) of the previous phase is verifiably met (`PROJECT_CONSTITUTION.md` Article V). Criteria are measurable; "it feels good" is not a criterion. Durations assume a part-time operator.

---

## Two parallel tracks

**Track A** — the numbered phases below. API-driven, builds the durable platform.
**Track B** — content intelligence on manually collected evidence (ADR-0008). No API dependency; validates the project's actual risky assumption. **Currently active and ahead of Track A.**

The two converge when Track A's ingestion feeds the same evidence layer Track B feeds by hand.

### Track B status
| Step | State |
|---|---|
| Historical performance data collected (151 posts) | ✅ |
| 20 posts with full transcripts, good/weak labelled | ✅ |
| `knowledge/content/patterns.md` built from evidence | ✅ v2 |
| First hypothesis refuted on own data | ✅ (Article III satisfied) |
| Peer-account data (5 accounts) | 🔄 in progress |
| 20 further mid/weak own posts | ⬜ |
| First content generated from validated patterns | ⬜ next |
| Published, results returned, pattern promoted or demoted | ⬜ |

**Track B gate:** the loop closes once at least one generated piece is published and its real performance has promoted or demoted a pattern in `patterns.md`.

---
## Phase 0 — Architecture (current)
Deliverables: this repository, ADRs 0001–0006, Constitution, Brief (`README.md`), Architecture, Knowledge Management, data model, ingestion strategy, cost policy, agent specs, open-questions backlog.
**AC:** all five blocking questions in `docs/backlog/open-questions.md` answered; API access confirmed working with a live token; free-tier execution path confirmed (ADR-0006).

---
## Phase 1 — Foundation (1–2 weeks)
Own-account ingestion, SQLite schema, `content_id` spine, daily/scheduled snapshot capture, `aios doctor`, run logging.
**AC:**
1. All available own-account history in SQLite; a full `rebuild` from raw reproduces it byte-identically.
2. Story insights captured on schedule for 7 consecutive days with zero gaps.
3. Every post published from now on has a `content_id` present before publication.
4. `aios report --weekly` produces a factual performance report with no LLM involvement.

Deliberately no AI in this phase. A model on top of unreliable data produces confident errors.

---
## Phase 2 — Intelligence (2–4 weeks)
Merges what was previously two separate phases (Brand Knowledge Core, Market Signal) into one Intelligence phase — brand, audience, and market knowledge form one connected layer, not sequential silos.

**Brand & Audience:**
`knowledge/brand/` populated (voice, mission/vision, positioning, beliefs, banned patterns), audience personas grounded in actual comment/DM data, content pillars defined with a measurable definition each.
**AC:**
1. Blind test: 5 captions, mixed system-drafted and operator-written; operator rates system drafts ≥4/5 on voice fidelity.
2. Every pillar has a written definition precise enough that two people classify 20 past posts with ≥90% agreement.
3. `banned-patterns.md` exists and the drafting prompt provably respects it across 10 samples.

**Market Signal:**
`business_discovery` ingestion for the tracked account set, structural pattern extraction, weekly market report with stated limitations.
**AC:**
4. ≥15 accounts ingested weekly with <5% failure rate.
5. Weekly report identifies ≥3 structural patterns, each traceable to specific media IDs.
6. No report conflates competitor public proxies with own-account private metrics (ADR-0005).

---
## Phase 3 — Content (2 weeks)
Brief generation (hook, script, CTA, caption, on-screen text, shot checklist, editing prompt), one Claude Code skill, prompt versioning + eval fixtures.
**AC:**
1. 8 briefs generated; ≥6 used with <15 minutes of operator editing each.
2. Time from idea to ready-to-record script ≤20 minutes.
3. Every brief carries a hypothesis and exactly one manipulated variable.

---
## Phase 4 — Engagement
New phase, not present in the original design. Comment/DM triage support and community-signal capture — sentiment, recurring questions, and the qualified-audience signals that feed the North Star Metric (`README.md`) — still human-in-the-loop for any reply (`PROJECT_CONSTITUTION.md` Article I).
**AC:** defined at phase start, per Article V; deferred until Phase 3 closes. Must include a concrete operational definition of "qualified audience" once backlog item B2 is answered.

---
## Phase 5 — Automation (3–4 weeks)
Merges what was previously two separate phases (Learning Loop, Automation & Reliability) — automating a loop that isn't already working manually is premature, so they land together. Experiment registry, verdicts at sample thresholds, monthly retro, curated lessons, knowledge diffs proposed against `knowledge/`, unattended scheduling, retries, alerting, cost ceilings, the LLM Abstraction Layer fully implemented across all agent calls, orchestrator decision reviewed against ADR-0003 criteria.
**AC:**
1. ≥6 experiments closed with explicit verdicts including at least one `refuted`. (A system that never refutes anything is not measuring.)
2. Monthly retro generated automatically and merged after human review.
3. Every lesson references ≥3 `content_id`s. Single-sample lessons are rejected.
4. 14 consecutive days of unattended weekly cycles; every failure produced a notification within 1 hour; monthly cost within ceiling.

---
## Phase 6 — SaaS (ongoing)
Renamed from "Expansion" to make the SaaS ambition explicit. Multi-tenant packaging of the core (per `docs/architecture/00-system-overview.md` SaaS-Ready constraints), a second business domain or a second operator as the first real multi-tenant test, publishing automation, and any reporting surface beyond Markdown/CLI.
**AC:** not started before Phases 1–5 have run for 8 weeks with real content.
