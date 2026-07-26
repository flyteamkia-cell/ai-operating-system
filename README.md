# AIOS — AI Operating System for Personal Brand & Content Intelligence

Status: **Phase 0 — Architecture (blocked on open questions)**
Owner: single operator (solo) · Reasoning engine: Claude Code · Language of record: English (see ADR-0004)

## What this is
A long-lived operating platform where **git is the source of truth**, **deterministic code moves data**, and **the LLM only makes judgements**. It is not a script collection and not an agent framework.

## Non-negotiables
1. Every piece of content has a stable `content_id` from idea → publish → metrics → lesson. Without this the feedback loop is fiction.
2. Numbers live in SQLite. Knowledge lives in versioned Markdown. They never mix.
3. No LLM call receives raw API JSON. It receives a deterministic **Context Pack**.
4. No phase starts before the previous phase's Acceptance Criteria are met (`docs/roadmap/roadmap.md`).
5. Every architectural decision becomes an ADR in `docs/decisions/`.

## Map
```
.claude/CLAUDE.md              operating contract for the implementation engine
docs/architecture/             system, data model, ingestion strategy, cost policy
docs/decisions/                ADRs (immutable once accepted)
docs/roadmap/roadmap.md        phases + acceptance criteria (the gate)
docs/backlog/open-questions.md unresolved decisions; blockers marked [B]
knowledge/                     brand, audience, content, market, journal (Markdown, human-owned)
agents/                        agent specifications (contract, not code)
prompts/                       prompts as versioned software artifacts
skills/                        Claude Code skills (executable procedures)
workflows/                     scheduled/triggered process definitions
src/                           TypeScript modular monolith
```

## Start here
1. `docs/critique.md` — why the original design was cut down.
2. `docs/architecture/00-system-overview.md`
3. `docs/decisions/ADR-0006-free-tier-execution.md` — how this runs with $0 subscriptions (Claude Code via API key, Meta Development Mode, GitHub Actions as the free scheduler).
4. `docs/backlog/open-questions.md` — remaining blockers before Phase 1.
