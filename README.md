# AIOS — AI Social Media Operating System

Status: **Phase 0 — Architecture** (blocked on open questions, see below)
Owner: single operator (solo) · Language of record: English for system docs, Persian (fa-IR) for content artifacts (ADR-0004)

## Product
An **AI Social Media Operating System** for a personal brand in financial-markets content — not a "content generator." Content generation is one capability among several (ingestion, analysis, knowledge management, planning, learning); the product is the operating core that connects them.

## Mission
Give one operator the leverage of a full marketing team — strategist, analyst, researcher, writer — while keeping every consequential decision in human hands.

## Vision
A domain-agnostic operating core (identity spine, knowledge base, learning loop, provider-agnostic reasoning layer) that runs this brand today and any additional business domain — VIP community, paid research, education products — tomorrow, and can eventually be offered as a product to other operators (SaaS).

## What this is, mechanically
A long-lived platform where **git is the source of truth**, **deterministic code moves data**, and **the LLM only makes judgements**. Every piece of content carries a stable `content_id` from idea → publish → metrics → lesson; without it the feedback loop is fiction. It is not a script collection and not an agent framework — see `docs/architecture/00-system-overview.md` for the full architecture and `PROJECT_CONSTITUTION.md` for the principles that govern every decision.

## North Star Metric
**Growth of Qualified Audience** — not followers, not raw reach. "Qualified" is defined against the conversion event, currently unanswered (backlog item B2). Until B2 is answered, the working proxy is a cohort trend of save rate + share rate + comment depth on pillar-aligned content — never a single-post vanity count. Refined, not replaced, once B2 is answered.

## MVP Scope (Phases 0–3)
Single Instagram account, own-account data only · deterministic ingestion, SQLite fact store, `content_id` spine · brand/audience/market knowledge base · weekly plan + content briefs for human recording · manual publish · manual review of every knowledge write.

## Future Scope (Phase 4+)
Engagement support (comment/DM triage) · unattended weekly cycle behind approval gates · additional business domains on the same core (VIP channel, education, CRM) · multi-tenant SaaS packaging · multi-platform publishing.

## Out of Scope (indefinitely, until explicitly revisited)
Autonomous publishing without human sign-off · autonomous (unreviewed) knowledge-base writes · vector database/semantic search (`docs/critique.md`; revisit at >2,000 knowledge chunks) · dashboard UI (Markdown/CLI until Phase 6) · workflow orchestrator platform (ADR-0003 has the exact revisit criteria).

## Success Criteria
Idea → recordable brief ≤20 minutes · weekly cycle sustained unattended ≥14 consecutive days · ≥1 experiment closed with an explicit verdict (including refutations) per month · monthly AI cost within a configured ceiling · North Star Metric trending up over rolling 8-week windows, evaluated only once ≥3 comparable data points exist.

## Map
```
PROJECT_CONSTITUTION.md         non-negotiable principles (the Constitution)
KNOWLEDGE_MANAGEMENT.md         how knowledge is written, reviewed, and kept single-sourced
.claude/CLAUDE.md               operating contract for the implementation engine
docs/roadmap/roadmap.md         phases + acceptance criteria (the gate); Track A and Track B
docs/architecture/              system overview (incl. LLM abstraction layer), data model,
                                ingestion strategy, cost policy, collection schema mapping
docs/decisions/                 ADRs (immutable once accepted)
docs/governance/                roles, team collection guide, extraction template
docs/source-notes/              archived external documents cited by this repo
docs/backlog/open-questions.md  unresolved decisions; blockers marked [B]
docs/critique.md                why the original design was cut down
knowledge/                      brand, audience, content (incl. patterns.md), market, journal
data/evidence/                  manually collected performance data + known-issues log
agents/                         agent specifications (contract, not code)
prompts/                        prompts as versioned software artifacts
skills/                         Claude Code skills (executable procedures)
scripts/                        analysis scripts
workflows/                      scheduled/triggered process definitions
src/                            TypeScript modular monolith
```

## Start here
1. `PROJECT_CONSTITUTION.md` — the principles nothing else may contradict.
2. `docs/roadmap/roadmap.md` — phases, gates, and the two parallel tracks.
3. `docs/decisions/ADR-0008-track-b-content-intelligence.md` — why the active work runs outside the numbered phases.
4. `knowledge/content/patterns.md` — what the data actually says. The project's primary asset.
5. `docs/architecture/00-system-overview.md` — architecture, incl. the LLM Abstraction Layer.
6. `docs/governance/roles.md` — who decides what, and why there is one human bridge.
7. `docs/backlog/open-questions.md` — remaining blockers.
