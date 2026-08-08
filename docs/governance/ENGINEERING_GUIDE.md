# Engineering Guide

The canonical handbook for how engineers and AI assistants work inside this repository. It defines process, not product. It contains no architecture, roadmap, decisions, or implementation status—those live in their own canonical documents. This guide is intended to remain stable over time and defines only how work is performed.

---

# 1. Purpose

**Rule:** This document is the single source of truth for engineering workflow, documentation practice, Git discipline, and review process.

**Reason:** A single process owner prevents every engineer or AI assistant from inventing different ways of working.

**Rule:** This guide defines process only. Product behavior, architecture, roadmap, and implementation belong elsewhere.

**Reason:** Process and product evolve at different speeds and must remain independent.

---

# 2. Roles

## Human Maintainer

- Owns strategic direction.
- Approves all consequential changes.
- Has final authority.

## AI Assistant

- Analyzes.
- Identifies affected files.
- Proposes exact changes.
- Waits for approval.
- Never makes repository changes without approval.

---

# 3. Canonical Documents

Always modify the canonical owner.

Never duplicate information.

Canonical ownership:

| Topic | Canonical document |
|--------|--------------------|
| Project overview | README.md |
| Architecture | docs/architecture/ |
| Architectural decisions | docs/decisions/ |
| Roadmap | docs/roadmap/ |
| Open questions | docs/backlog/ |
| Long-term AI memory | PROJECT_MEMORY.md |

When information already exists elsewhere, reference it instead of copying it.

---

# 4. Development Workflow

Every feature follows the same lifecycle:

1. Understand
2. Design
3. Document
4. Implement
5. Test
6. Review
7. Merge

If information is missing:

- record an Open Question
- avoid guessing
- ask only when progress is blocked

Documentation always precedes implementation.

---

# 5. Atomic Change Policy

Every change must contain exactly one logical concern.

Principles:

- minimal scope
- minimal files
- reversible
- reviewable

Never:

- batch unrelated work
- rewrite whole documents unnecessarily
- include opportunistic cleanup

After every approved change:

Stop.

Wait for the next instruction.

---

# 6. Change Approval

Before changing repository files, always provide:

- purpose
- affected files
- exact diff summary
- expected impact
- rollback strategy

Only proceed after explicit approval such as:

- APPLY
- IMPLEMENT
- EXECUTE

Approval is valid only for that single change.

---

# 7. Git Workflow

One atomic change equals one commit.

Commit messages describe intent, not implementation.

Keep commits small.

Never commit generated artifacts as canonical source.

---

# 8. Documentation Rules

Documentation is updated together with the work.

Never create parallel documents covering the same topic.

Prefer extending existing canonical documents.

Promote durable knowledge into canonical documentation.

Conversation is never considered documentation.

---

# 9. Architecture Rules

Architecture is owned by:

```
docs/architecture/
docs/decisions/
```

This guide never redefines architecture.

Architectural decisions should record:

- context
- decision
- alternatives
- consequences

Prefer the simplest design satisfying today's requirements.

Avoid speculative abstraction.

---

# 10. Code Rules

Code implements documented design.

Not the opposite.

Prefer:

- modularity
- strong typing
- single responsibility
- replaceable components

Respect architectural boundaries.

Every component should be testable and observable.

---

# 11. Review Checklist

Before proposing completion verify:

- single concern
- minimal files
- documentation updated
- no duplicated canonical content
- rollback exists
- no unrequested scope

Review as an engineer protecting the repository.

Not as an assistant trying to satisfy the user.

---

# 12. Definition of Done

A change is Done only when:

- single concern
- documented
- reviewed
- reversible
- approved

No canonical document may contradict the completed change.

---

# 13. Anti-Patterns

Avoid:

- batching unrelated work
- duplicate documentation
- rewriting large files for small edits
- acting without approval
- assuming approval carries forward
- speculative infrastructure
- premature abstraction
- unnecessary dependencies

Every unnecessary abstraction becomes permanent maintenance cost.