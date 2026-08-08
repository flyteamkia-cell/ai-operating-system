# Roles and Responsibilities

Status: Accepted · 2026-08-08 · Owner: Human (operator)

Four parties collaborate on this project. This document exists so no work is done twice and no decision is made by the wrong party. It sits under `PROJECT_CONSTITUTION.md`: where this document and the Constitution disagree, the Constitution wins.

---

## The four parties

| Party | One-line mandate |
|---|---|
| **Owner (Kia)** | Sets goals, approves everything, is the only bridge between the two AIs |
| **Team** | Collects raw material. Does not analyze. |
| **GPT** | Design, strategy, and critical review. Not operations. |
| **Claude** | Analysis, generation, repository work, execution. Not business decisions. |

---

## Owner (Kia)

**Owns:** campaign goals, the conversion event definition, brand voice, final approval of every published piece, and the decision on any architectural disagreement between GPT and Claude.

**Exclusive responsibilities — nobody else may do these:**
- Approve or reject any change to the repository (per the Change Approval Workflow: nothing is modified without an explicit `APPLY` / `IMPLEMENT` / `EXECUTE`).
- Approve any content before publication. Publishing is manual by constitutional rule.
- Merge any change into `knowledge/`. Agents propose diffs; the owner merges.
- Carry context between GPT and Claude — they have no shared channel and never will.

**Explicitly not responsible for:** running scripts, formatting data, writing documentation.

---

## Team

**Owns:** collection only.

**Does:**
- Forward reference posts into the Telegram collection group, with the fixed `#سواپ` message template underneath.
- Fill the Google Sheet using the agreed column schema.
- Send in weak/low-performing posts too, tagged as such — a swipe file of only winners produces false patterns.
- Leave a field blank when the number is unavailable.

**Does not:**
- Analyze, interpret, or explain why something worked. The `چرا:` line is a one-sentence human hunch, not analysis.
- Invent, estimate, or round a metric. A guessed number is worse than a blank, because it silently corrupts the ranking.
- Write into the repository, the knowledge base, or `patterns.md`.

---

## GPT

**Owns:** system design, campaign strategy, rule design, and adversarial review.

**Does:**
- Propose architecture and challenge Claude's architecture.
- Design campaign strategy and content direction at the level above individual posts.
- Act as critical reviewer of Claude's output — the second opinion that prevents a single model's blind spot from becoming the project's blind spot.
- Design skill and rule structures.

**Does not:**
- Perform repetitive operational work (teardowns, per-post analysis, data normalization). This is expensive and it is Claude's job.
- Write to the repository. GPT has no repository access; all its output reaches the repo through the Owner and then through Claude.
- Make final decisions. It proposes; the Owner decides.

**Known constraint:** GPT has no access to the repository, Google Drive, or the installed skill. It only knows what the Owner tells it. **Every time the project state changes materially, GPT must be re-briefed** — otherwise it designs against a stale picture, which is exactly what happened in the first Phase 1 proposal.

---

## Claude

Two distinct surfaces, deliberately separated:

### Claude (chat / architect)
**Does:** architecture, ADRs, documentation, audits, teardowns, content generation via `viral-content-lab`, reviewing GPT's proposals, and preparing exact diffs for approval.
**Does not:** modify repository files without explicit approval; make business decisions; publish anything.

### Claude Code (implementation engine)
**Does:** writes and runs code in the repository, runs the Python scripts, executes workflows, applies approved diffs, commits.
**Does not:** start a phase whose predecessor's acceptance criteria are unmet; write knowledge without a human gate; call an AI provider directly (must go through the abstraction layer once it exists).

**Hard rules binding both surfaces:**
- Never state a performance conclusion without citing the specific posts supporting it.
- With fewer than 3 comparable samples, the required answer is `inconclusive`. Do not construct an explanation for a single data point.
- Never compare our private metrics (saves/shares/reach) against competitor public proxies.
- Never invent a metric the data does not contain.

---

## Decision rights — who decides what

| Decision | Decided by | Input from |
|---|---|---|
| Business goals, conversion event | Owner | GPT |
| Campaign strategy | Owner | GPT proposes, Claude reviews |
| System architecture | Owner | GPT proposes, Claude reviews (or vice versa) |
| What goes into the repository | Owner | Claude proposes the exact diff |
| Which content gets published | Owner | Claude generates, Owner edits |
| What counts as a validated pattern | Claude (evidence rules) | Owner overrides only with evidence |
| Whether a sample is large enough | Claude — non-negotiable | — |

The last two rows are deliberate: the whole point of the system is that it refuses to tell a satisfying story about noise. If that judgement is overridable by preference, the system's output becomes decorative.

---

## Shared workspace

The three parties cannot all reach the same place. This is a hard constraint, so the design routes around it rather than pretending otherwise.

| Location | Owner | Claude | GPT | Purpose |
|---|---|---|---|---|
| **GitHub repo** | ✅ | ✅ | ❌ | Single source of truth. Everything durable ends here. |
| **Google Drive folder** | ✅ | ✅ | ⚠️ manual | Exchange layer: inputs, drafts, briefs, digests |
| **Google Sheet** | ✅ | ✅ | ⚠️ manual | Structured collection |
| **Telegram group** | ✅ team | ⚠️ via export | ❌ | Low-friction collection |

**Rules that make this work:**
1. **The repository is the only source of truth.** Drive, Sheets and Telegram are input surfaces. Nothing is considered decided until it is in the repo.
2. **Drive is the exchange layer**, because it is the one place both the Owner and Claude can read directly. Proposed structure:
   ```
   AIOS-Exchange/
     inbox/        raw material awaiting processing
     briefs/       documents being passed between GPT and Claude
     digests/      current repo snapshot for briefing GPT
     analysis/     patterns.md, normalized reports
   ```
3. **GPT is briefed by document, not by conversation.** Before asking GPT for any design work, the Owner sends it the current repository digest. Design produced against a stale picture is wasted work.
4. **Anything durable is promoted into the repo**, with a commit. If it only exists in a chat, it does not exist.

---

## The failure mode this document exists to prevent

Two capable models, working from different pictures of reality, each producing confident and internally coherent designs that cannot be combined. The first Phase 1 proposal was exactly this: a well-reasoned plan to build a system that already existed and was already installed.

The defence is procedural, not technical: **one human bridge, one source of truth, and a re-brief before every design request.**
