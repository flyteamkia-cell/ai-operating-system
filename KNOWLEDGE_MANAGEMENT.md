# Knowledge Management

Canonical policy. Detailed rationale remains in `knowledge/README.md` and in the archived source notes under `docs/source-notes/`; this document is the enforceable summary.

## Conversation → Knowledge
Chat and session history are temporary. Anything with durable value — a decision, a brand fact, a lesson, a corrected assumption — is written into its owning file in `knowledge/` or `docs/` before the session ends. If it is not written down, it does not exist for the next cycle.

## No Duplicate Knowledge
Before writing, check whether an owning file already exists for this fact. A near-duplicate file is a defect, not a convenience. Duplicates are merged into the canonical file; they never coexist.

## Update Existing Documents
Default action is **update in place**, not create-new. A new file is justified only when no existing file owns the topic, and even then it must declare its owner immediately, per the one-owner-per-file rule already in `agents/README.md`.

## Knowledge Review
Knowledge is reviewed, not just accumulated. Periodically (see the Brand Curator cadence, `agents/brand-curator.md`) the full set is checked for contradictions, staleness (no update in 90+ days), and structural fit. A structure that no longer fits is a candidate for restructuring, proposed for human approval — never silently reorganized.

## Knowledge Curator (Future)
The Brand Curator agent (already specified in `agents/brand-curator.md`) is the eventual implementation of this policy, per Constitution Article IX — the policy exists now; the persistent agent is scheduled, not built in this pass. Until it is implemented, this policy is executed manually by the operator at the end of each working session and monthly.

## ADR Integration
Architectural decisions are knowledge, not chat output. Every decision with a lasting consequence — a technology choice, a scope cut, a reversal — produces or updates an ADR in `docs/decisions/`. The Constitution and this document sit above ADRs: an ADR may implement a principle but may never contradict one without first amending the Constitution itself.
