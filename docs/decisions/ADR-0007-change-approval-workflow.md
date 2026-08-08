# ADR-0007 — Change approval workflow for repository modifications

Status: Accepted · Date: 2026-08-08 · Owner: Human (operator)

## Context
Early sessions applied repository changes directly within a turn. That was fast, but it produced large commits that were hard to review and hard to revert selectively, and it gave the operator no opportunity to redirect a change before it landed.

A stricter workflow was introduced mid-project and governed subsequent work by convention only — it existed in no file, so a future session or a second engineer could not discover it. This ADR records it.

## Decision
For every requested repository change, the implementation engine must:

1. Analyze the request.
2. Identify the affected files.
3. Explain why each file needs to change.
4. Propose the exact modification, as a minimal diff.
5. Estimate architectural impact.
6. **Stop and wait for explicit approval.**

Files are modified only after the operator replies `APPLY`, `IMPLEMENT`, or `EXECUTE`. Small typo fixes are exempt.

Minimal diffs are preferred over document rewrites. Full regeneration is acceptable only when the change is itself structural — for example a repo-wide rename or a directory move.

## Amendment — 2026-08-08: standing approval for pre-agreed work
The operator does not wish to act as a data-entry step. Where a change has already been proposed in detail and explicitly approved in conversation, the engine performs the work in full without re-proposing each file individually, and reports what was done afterwards.

The approval gate itself is unchanged: nothing lands without an explicit approval word. What changed is its granularity — approval may cover a defined batch of pre-agreed work rather than each file. Anything **not** previously discussed still requires its own proposal and its own approval.

## Alternatives considered
- **Direct apply plus a post-hoc changelog** (original practice) — rejected: no opportunity to redirect before a change lands.
- **Approval only for "large" changes** — rejected: "large" is a judgement call and drifts over time; a bright line is enforceable, a vague one is not.
- **Approval per file, always** — rejected in the amendment above: it made the operator a bottleneck on work they had already approved in substance, which delayed the repository by several days.

## Consequences
+ Every commit is reviewable and revertible in isolation.
+ The operator retains veto over direction without doing mechanical work.
− Slower per-change iteration; mitigated by keeping proposals diff-scoped and by batching pre-agreed work.
− The engine cannot push to the remote (no credentials). It prepares the complete working tree; the operator runs `git add/commit/push`. This is a hard boundary, not a workflow choice.

## Scope note
This operationalizes `PROJECT_CONSTITUTION.md` Article VI (Human Approval) for repository file changes. It does not amend the Constitution and does not weaken Articles I or II: publishing and knowledge merges remain separately gated.
