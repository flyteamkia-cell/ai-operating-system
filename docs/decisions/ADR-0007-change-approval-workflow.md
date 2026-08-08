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
5. State the expected impact and how to roll it back.
6. **Stop and wait for explicit approval.**

Files are modified only after the operator replies `APPLY`, `IMPLEMENT`, or `EXECUTE`. Small typo fixes are exempt.

Minimal diffs are preferred over document rewrites. Full regeneration is acceptable only when the change is itself structural — for example a repo-wide rename or a directory move.

## Atomic change policy
Every change contains **exactly one logical concern**:

- Minimal scope, minimal files touched.
- Reversible, and reviewable in a single sitting.
- No batching of unrelated work into one change.
- No opportunistic cleanup alongside a requested edit — if cleanup is warranted, it is proposed as its own change.
- Large files are not rewritten to make small edits.

After each approved change: stop, and wait for the next instruction rather than continuing into adjacent work.

## Git workflow
- One atomic change equals one commit.
- Commit messages describe **intent**, not implementation.
- Commits stay small. A commit that cannot be summarized in one line is doing more than one thing.
- Generated artifacts are never committed as canonical source.

## Amendment — 2026-08-08: standing approval for pre-agreed work
The operator does not wish to act as a data-entry step. Where a change has already been proposed in detail and explicitly approved in conversation, the engine performs the work in full without re-proposing each file individually, and reports what was done afterwards.

The approval gate itself is unchanged: nothing lands without an explicit approval word. What changed is its **granularity** — approval may cover a defined batch of pre-agreed work rather than each file. Anything **not** previously discussed still requires its own proposal and its own approval.

This supersedes the earlier rule that approval is valid for exactly one change. That rule was correct in principle but made the operator a bottleneck on work they had already approved in substance, which delayed the repository by several days.

## Alternatives considered
- **Direct apply plus a post-hoc changelog** (original practice) — rejected: no opportunity to redirect before a change lands.
- **Approval only for "large" changes** — rejected: "large" is a judgement call and drifts over time; a bright line is enforceable, a vague one is not.
- **Approval per file, always** — rejected in the amendment above: it made the operator a bottleneck on work they had already approved in substance, which delayed the repository by several days.

## Consequences
+ Every commit is reviewable and revertible in isolation.
+ The operator retains veto over direction without doing mechanical work.
− Slower per-change iteration; mitigated by keeping proposals diff-scoped and by batching pre-agreed work.
− The engine cannot push to the remote (no credentials). It prepares the complete working tree; the operator runs `git add/commit/push`. This is a hard boundary, not a workflow choice.

## Known failure mode — version drift
Twice during August 2026, work committed directly to the repository was overwritten because the engine's working copy was reconstructed from its own last delivered archive rather than from the live repository. Both times, files the engine had never seen were silently deleted.

**Mitigation:** before preparing any batch of changes, the engine requests `git ls-files` output from the operator and reconciles it against its working copy. A file present in the repository but absent from the working copy is treated as a conflict requiring explicit resolution — never as a deletion.

## Scope note
This operationalizes `PROJECT_CONSTITUTION.md` Article VI (Human Approval) for repository file changes. It does not amend the Constitution and does not weaken Articles I or II: publishing and knowledge merges remain separately gated.
