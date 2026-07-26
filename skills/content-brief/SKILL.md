---
name: content-brief
description: Produce a production-ready Instagram content brief (hook variants, timed script, on-screen text, CTA, caption, shot checklist, editing notes) for this brand from an approved plan item. Use this whenever the user asks for a reel/carousel/story idea, script, hook, caption, or says they want to record something — even casually phrased, and even if they don't say "brief". Also use when converting a raw idea into something recordable.
---

# Content Brief

## Preconditions — check before writing anything
1. `knowledge/brand/voice.md` and `knowledge/brand/banned-patterns.md` exist and are `status: active`. If `draft`, stop and say the brand core is not ready (Phase 2 gate) — a brief written on a draft voice file trains the operator to distrust the system.
2. A `content_id` exists or is minted now via `aios content new --slug <slug>`. Never write a brief without one; unlinked content cannot be measured.
3. The plan item declares a hypothesis and exactly one manipulated variable. If it declares two, split it into two items.

## Procedure
1. Build the pack: `aios pack build --agent content-strategist --content <content_id>`. Do not read `knowledge/` files ad hoc — packs are what keeps cost flat and outputs reproducible.
2. Apply `prompts/content/brief-writer.md` at its current version.
3. Validate the draft against the output contract and the banned-patterns list. Fix violations before showing anything.
4. Write to `knowledge/content/briefs/<content_id>.md` with front-matter: content_id, prompt version, pack hash, created date.
5. Register the row: `aios content set --id <content_id> --status briefed --brief <path>`.

## Output
Persian, spoken register. Three genuinely distinct hook angles — not three rewordings. One CTA. Timed script.

## Refuse to proceed if
The brand core is still draft · no content_id · two manipulated variables · the pack is missing a required segment (output `BLOCKED: <segment>` rather than inventing context).
