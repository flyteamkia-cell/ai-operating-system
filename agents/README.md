# Agents

Four agents in v1. Adding a fifth requires an ADR justifying why an existing agent cannot own the responsibility.

An agent is a **contract**, not a process: role, inputs, outputs, tools, permissions, failure modes, evaluation, KPIs. Agents never call each other. The cycle workflow calls them in sequence and passes artifacts through the filesystem — this keeps every step inspectable and independently re-runnable.

| Agent | Owns (write access) | Model tier | Cadence |
|---|---|---|---|
| Performance Analyst | `knowledge/audience/` | Mid | Weekly |
| Market Signal | `knowledge/market/` | Mid | Weekly |
| Content Strategist | `knowledge/content/` | Frontier (plan) / Mid (drafts) | Weekly + on demand |
| Brand Curator | `knowledge/brand/`, `docs/` hygiene | Mid | End of session + monthly |

Write access is exclusive. No file has two owners.
