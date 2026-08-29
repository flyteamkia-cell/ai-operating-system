# Content Production Roles

Status: Accepted · Added: 2026-08-29 · Owner: content-strategist

This document formalizes the four-role pipeline every Track B content piece passes through before it is recorded. It sits below `docs/governance/roles.md` (which defines the four *parties* — Owner, Team, GPT, Claude) and above individual briefs: it is the internal production discipline Claude follows when asked to turn a topic into a finished, recordable piece.

## Why this exists
An earlier content package left research fields as placeholders ("check this yourself," "coordinate with your analysis team") instead of doing the research. That is a defect, not a stylistic choice: a brief with gaps forces the operator to redo the work the system was supposed to do. This document exists so that failure mode doesn't repeat, for this piece or any future one.

## The four roles

### Role 0 — Data / Research Analyst
**Responsibility:** find the real, current, load-bearing facts the piece depends on — exact dates, exact price/technical levels, exact figures — from credible sources. Nothing downstream may proceed on a placeholder.
**Output:** a sourced facts block: what happened, when, the specific numbers, and the next dated catalyst if one exists.
**Hard rule:** if a fact cannot be found or verified, that is stated explicitly as a limitation — it is never left as an unfilled blank for the operator to complete.

### Role 1 — Scenario Writer (سناریست)
**Responsibility:** take Role 0's facts and shape them into the strongest narrative structure for the stated goal (currently: follower growth via saves/shares, ADR-0009). Decides the psychological mechanism, the narrative angle, and which concrete numbers carry the story.
**Output:** the structural decisions and their justification — why this angle, why this split between on-post and DM content, why this specific CTA and return-date.

### Role 2 — Screenwriter (فیلمنامه‌نویس)
**Responsibility:** convert Role 1's structure into the final, word-for-word script — every sequence, every line of dialogue, every on-screen text — plus the finished caption and, where the piece uses a DM mechanism, the finished auto-reply text. No sequence is left as a description of what should be said; it is what will be said.
**Output:** sequence-by-sequence storyboard (visual + dialogue + on-screen text per sequence), final caption, final DM auto-reply text.

### Role 3 — Art Director (کارگردان هنری)
**Responsibility:** the shot list — framing, lighting, on-screen graphic design, color treatment, editing rhythm — for every sequence Role 2 defined, plus any graphics that accompany a DM auto-reply.
**Output:** a shot-by-shot table mapped to Role 2's sequences.

## Rules that apply across all four roles
- **No placeholders in the final deliverable.** A gap is acceptable only when the underlying fact is genuinely unknowable in advance (e.g. the exact live price at recording time) — and even then, the piece must say exactly which line is affected and how to update it, not leave the field blank.
- **The operator's edit is a choice, not a requirement.** The output must be usable as-is; whether the operator changes it afterward is their call, not a gap this pipeline leaves for them to close.
- **Financial-integrity constraints apply to every role**, not just the script: Role 0's numbers must be accurately sourced, Role 1's scenario framing must present possibilities not certainties, Role 2's wording must avoid promise language, Role 3's graphics must carry the same disclaimer the script carries.
- **Every deliverable states its content_id** and links back to the pattern(s) or hypothesis it draws on, per existing knowledge-management rules.

## Relationship to existing artifacts
- `prompts/content/brief-writer.md` remains the prompt contract for routine Track B briefs generated from `knowledge/content/patterns.md`. This four-role pipeline is the fuller version used when a piece depends on external, time-sensitive research (a news event, a macro release) that the existing prompt does not cover.
- `docs/governance/roles.md` defines who does what across Owner/Team/GPT/Claude. This document defines how Claude's own content-production work is internally sequenced.
