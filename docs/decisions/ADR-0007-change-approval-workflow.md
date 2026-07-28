# ADR-0007 — Change approval workflow for repository modifications
Status: Accepted · Date: 2026-07-28 · Owner: Human (operator)

## Context
Prior sessions applied changes directly within a turn — efficient, but commits were large,
hard to review, and hard to revert selectively.

## Decision
For every requested repository change: analyze → identify affected files → explain why each
changes → propose exact modifications as minimal diffs → estimate architectural impact →
wait for explicit approval (APPLY / IMPLEMENT / EXECUTE). Small typo fixes are exempt.
Minimal diffs preferred over full-document rewrites; full regeneration only when the change
is itself structural (e.g. a repo-wide rename).

## Alternatives considered
- Direct apply + post-hoc changelog (previous practice) — rejected: no chance to redirect
  before the change lands.
- Approval only for "large" changes — rejected: "large" is a judgment call prone to drift.

## Consequences
+ Every commit reviewable and revertible in isolation.
− Slower per-change iteration; mitigated by keeping proposals diff-scoped.

## Scope note
Operationalizes Constitution Article VI for repository file changes; does not amend the
Constitution.
