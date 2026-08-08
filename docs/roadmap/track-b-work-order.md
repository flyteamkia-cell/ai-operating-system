# Work Order — Track B, Content Intelligence

**Context for whoever picks this up:** read `02-roles-and-responsibilities.md` first, then `PROJECT_CONSTITUTION.md` and `docs/roadmap/roadmap.md` in the repository.

**Governing rule:** the Change Approval Workflow applies to every task below. Analyze → identify affected files → propose the exact minimal diff → wait for `APPLY` / `IMPLEMENT` / `EXECUTE`. Nothing is written to the repository before approval. Prefer minimal diffs over document rewrites.

---

## Why "Track B"

The repository roadmap's Phase 1 (Foundation) depends on Instagram API access and is blocked on open questions. Track B is a parallel line that depends on none of that: reference posts are collected manually, so the content intelligence loop can start immediately and prove its value before any API work.

Track A (API ingestion) stays on the roadmap unchanged. The two converge later: once the API pipeline exists, it feeds the same evidence layer that Track B feeds by hand.

**Track B's thesis:** the risky assumption in this project is not "can we ingest data" — that is well understood and fully specified. The risky assumption is "does the system actually produce better content than the operator would alone." Track B tests that assumption first, cheaply.

---

## Task list

Tasks are ordered by dependency. Each produces value on its own and can be stopped after.

---

### T1 — Preserve the two source documents in the repository
**Why:** `KNOWLEDGE_MANAGEMENT.md` cites a design document that exists only outside the repo. The audit flagged this: it contradicts "git is the source of truth," and a reader who clones the repo cannot open the cited file.
**Do:** copy the two Google Drive documents (`social-media-project-instructions.md`, `content-system-handoff.md`) into `docs/source-notes/`, then fix the citation in `KNOWLEDGE_MANAGEMENT.md` to point at the local path.
**Done when:** no document in the repository cites a file that is not in the repository.
**Size:** small.

---

### T2 — Fix the two broken internal links
**Why:** audit finding. `docs/critique.md` and `docs/decisions/ADR-0005` both reference `architecture/0X-....md` without the `docs/` prefix — neither link resolves.
**Do:** correct both paths.
**Done when:** every internal link in the repo resolves.
**Size:** trivial. (Arguably a typo fix, but it touches an ADR, so propose it rather than applying silently.)

---

### T3 — Write ADR-0007: Change Approval Workflow
**Why:** the workflow currently governs this project by convention only. It exists in no file, so a future session or a second engineer cannot discover it.
**Do:** write the ADR as previously proposed (context, decision, alternatives considered, consequences), plus a short operational section in `.claude/CLAUDE.md`.
**Done when:** the rule is discoverable by anyone reading the repository cold.
**Size:** small.

---

### T4 — Write ADR-0008: Track B and the relationship to viral-content-lab
**Why:** this is the largest strategic decision made since Phase 0 and it currently exists only in chat. It must record: the existence of the installed skill, that its two engines are the evidence/intelligence/execution layers (not to be rebuilt), the decision to run a manual-evidence track in parallel with the API track, and the naming convention that prevents the two "Phase 1"s from colliding.
**Do:** write the ADR. Update `docs/roadmap/roadmap.md` minimally — add Track B alongside the existing phases; do not rewrite the existing phases.
**Done when:** someone reading only the repo understands why there are two parallel tracks and what each depends on.
**Size:** medium. **This is the highest-value documentation task in the list.**

---

### T5 — Add the roles document
**Why:** four parties with overlapping capabilities and no shared channel. Without written role boundaries, work gets done twice and decisions get made by the wrong party.
**Do:** add `02-roles-and-responsibilities.md` to the repo as `docs/governance/roles.md`.
**Done when:** committed and referenced from `README.md`'s map.
**Size:** small.

---

### T6 — Reconcile the collection schema (documentation only, no code)
**Why:** the proposed 5-sheet structure and the existing swipe-file schema must not diverge, or the existing Python parser stops working and has to be rewritten for no benefit.
**Do:** write a short document mapping the collection schema to the repository's SQLite tables (`competitor_post`, `content`, `publication`, `metric_snapshot`). Note explicitly which columns are permanently unavailable for competitor accounts and why.
**Done when:** one document answers "where does each collected field end up, and which fields are structurally always empty."
**Size:** small.
**Note:** documentation only. Do not write ingestion code yet — the collected data does not exist yet, and code written against imagined data is code written twice.

---

### T7 — Set up the collection surfaces
**Why:** nothing downstream can start without real reference posts.
**Do (Owner + team, not Claude):**
- Create the Telegram group with topics; pin the `#سواپ` message template from `03-team-collection-guide-fa.md`.
- Create the Google Sheet with the exact column schema from T6.
- Distribute the team guide.
**Done when:** the team has submitted its first 5 posts correctly.
**Size:** small, but it is the gate for everything after it.

---

### T8 — First real analysis run
**Why:** this is the first moment the system produces something that could not have been produced without it.
**Do:** once 20–30 reference posts are collected — run `parse_telegram_export.py` (if Telegram) then `analyze_swipe_file.py`, read the completeness report **before** forming any opinion, run the teardown rubric on the top-ranked posts, and produce the first `patterns.md`.
**Done when:** `patterns.md` exists with patterns ranked by evidence strength, single-occurrence patterns explicitly labelled as hypotheses rather than findings, and an honest statement if the sample is too thin to support any of it.
**Size:** medium.
**Hard rule:** if the completeness report shows most entries are missing saves/sends, say so plainly and downgrade the output to qualitative. A confident-looking ranking built on gaps will cost weeks.

---

### T9 — First generation run
**Why:** closes the loop end to end for the first time.
**Do:** generate 5 content concepts from `patterns.md` using the skill's Phase 3 structure. Each concept references which pattern it came from, targets exactly one algorithmic signal, has one CTA, and carries an honest risk line. Spread across at least three distinct psychological mechanisms — five variations of one mechanism is one idea, not five.
**Done when:** the Owner can approve or kill each idea in under ten seconds without reading a full script.
**Size:** medium.

---

### T10 — Close the learning loop
**Why:** without this the system is a generator, not an intelligence system — and Article III of the Constitution is unmet.
**Do:** after published pieces have real performance data, append to `patterns.md` under "validated on our account," explicitly promoting or demoting patterns. Patterns confirmed on our own audience outrank anything inferred from competitors.
**Done when:** at least one pattern has been explicitly demoted or refuted. A system that only ever confirms is not measuring anything.
**Size:** ongoing.

---

## Success criterion for Track B

The track has succeeded when this sequence works once, end to end:

> 20–30 reference posts collected → `patterns.md` built from evidence → 5 content concepts generated from those patterns → at least one published → its real performance fed back and a pattern explicitly promoted or demoted.

Not when the architecture is complete. Not when everything is automated.

---

## Explicitly deferred — do not build these now

| Item | Why deferred |
|---|---|
| Instagram API ingestion | Track A; still blocked on open questions and not needed for Track B |
| Telegram bot writing directly to the Sheet | Weekly manual export is sufficient; a bot is a separate service for marginal gain |
| LLM abstraction layer implementation | Constitutionally required, but only once code actually makes provider calls |
| Any scheduling or automation | Premature. Automating a loop that has not yet run manually is how projects die |
| The four repository agents as running processes | Article IX: role first, agent later. They run as roles inside the skill for now |
| Dashboard, SaaS, multi-platform publishing | Later phases, unchanged |

---

## Open business questions that still block quality (not blocking start)

- **Conversion event.** Without it, the system optimizes for reach — the cheapest and least valuable outcome for a financial-markets brand. This determines the CTA on every piece of content generated in T9.
- **Baseline numbers.** Needed to set sample thresholds. With low volume, most week-over-week comparisons are noise, and the system must be configured to say "inconclusive" rather than invent causes.
- **The competitor account list.** T7 cannot be scoped without it.

Track B can start without these. It cannot produce *good* output without the first one.
