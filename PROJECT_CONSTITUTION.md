# Project Constitution

Non-negotiable principles. Unlike an ADR, an article here is not revisited for convenience — amending one requires an explicit, documented decision at the same level as this document, not a routine trade-off.

## Article I — AI Does Not Make the Final Decision
The system proposes: plans, briefs, analyses, knowledge diffs, provider routing. A human approves before anything becomes real — before a knowledge file is merged, before content is published, before a strategy changes. This is permanent, not a v1 training-wheel.

## Article II — Publish Is Manual in MVP
No component publishes to any platform on its own during Phases 0–3. Automated (unattended) publishing is reconsidered only from Phase 4 onward, and even then stays behind the approval gate in Article I.

## Article III — The System Must Learn
A cycle that produces content without producing a measurable verdict on a prior hypothesis has not done its job. From Phase 1 onward, the identity spine and feedback loop make "inconclusive," "supported," and "refuted" the required vocabulary of every retrospective — a system that never says "refuted" is not measuring anything.

## Article IV — No Vendor Lock-in
No module, agent, or workflow calls a specific AI provider directly. All reasoning goes through the LLM Abstraction Layer (`docs/architecture/00-system-overview.md`). Switching or adding a provider is a configuration change, never a rewrite. The same preference applies to infrastructure — replaceable, standard interfaces over provider-specific APIs wherever the cost of doing so is reasonable.

## Article V — Documentation First
Requirement → analysis → documentation → architecture → implementation → test → doc update → commit. Code or configuration that lands before its governing document is a defect, regardless of who wrote it.

## Article VI — Human Approval
Every irreversible or externally visible action — publish, knowledge merge, a provider change with cost impact, a schema migration — requires an explicit, logged human approval step.

## Article VII — Cost First
Every architectural and model-routing decision states its cost impact. The cheapest provider/model/approach that meets the quality bar is the default; the strongest model is a deliberate exception, never a default.

## Article VIII — Simplicity First
Prefer the simplest architecture that solves the actual, current problem. An abstraction is added only when it solves a real, present problem — never speculatively. A framework, service, or pattern justified only by "we might need it later" is rejected unless it names a concrete trigger condition.

## Article IX — Role First, Agent Later
Define a responsibility as a **role** — inputs, outputs, decision rules — before it is implemented as a formal, standing Agent. A role can be executed manually, by a script, or by a one-off prompt. It graduates to a persistent Agent only when recurrence and complexity justify the added surface (ownership, memory, evaluation) an Agent carries. This keeps agent count deliberate, never default.
