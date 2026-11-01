# ADR-0010 — Saga as agent session memory (dev tooling only)

Status: Accepted · Date: 2026-11-01 · Owner: Architecture

## Context
Claude Code sessions start blank; project context is re-derived every session. `.saga/` (mopanc/saga topic notes) already exists in the repo since 6e47cc1 but is not wired in.

## Decision
Use mopanc/saga, pinned to v1.0.0-rc.6, as developer tooling for agent memory: project-scoped MCP server (`.mcp.json`) plus UserPromptSubmit/PreToolUse hooks (`.claude/settings.json`). It is not a runtime dependency of `src/` and holds no product data.

## Constraints
- Notes in `.saga/topics/` are knowledge writes: reviewed as diffs (Constitution Art. VI), never merged unreviewed.
- Hooks are no-ops when the binary is absent; a missing install must never break a session.
- Distinct from SAGA_SERVER (Telegram collection connector).

## Consequences
+ Decisions and context persist across sessions.
− Pre-1.0 tool; pinned version, upgrade by explicit change. Rollback: delete the two config files.
