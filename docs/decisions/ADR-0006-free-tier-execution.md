# ADR-0006 — Execution under free-tier constraints

Status: Accepted · Date: 2026-07-26 · Owner: Architecture

## Context
Three "free" constraints apply simultaneously: (1) a free claude.ai account, not Pro/Max, (2) a Meta Developer app in Development Mode (no App Review completed), (3) no paid server/hosting. Verified against current sources rather than assumed (Anthropic and Meta docs, July 2026):

1. **claude.ai free plan** does not include Claude Code, Cowork, or Design. It does include Projects, Memory, web search, file/code creation, and MCP connectors, subject to a rolling 5-hour message cap.
2. **Claude Code does not require a claude.ai subscription at all.** It authenticates two independent ways: OAuth (needs Pro/Max) *or* an `ANTHROPIC_API_KEY` from console.anthropic.com, billed purely per-token with no subscription and no monthly minimum. The two are mutually exclusive per session (`/status` shows which is active).
3. **Instagram Graph API Development Mode** restricts the app to accounts holding a role (admin/developer/tester) on that Meta app — this fully covers the operator's own Business/Creator account with **zero App Review**. `business_discovery` (competitor read access) has historically sat under lower-tier access than publishing/DM permissions, but this must be re-verified against Meta's current permission table at Phase 4, not assumed now.
4. **No server** is not a real gap: GitHub Actions provides free scheduled compute (cron-triggered, generous free minutes on a personal repo) sufficient for deterministic ingestion and for invoking Claude via API key. Nothing in Phases 1–5 requires an always-on process; the tightest timing requirement (Story insights expiring in ~24h) only needs hourly-granularity cron, not a persistent server.

## Decision
- **Do not upgrade claude.ai to Pro to unblock this project.** Use claude.ai (free) for architecture conversations, review, and reading reports. Use **Claude Code authenticated via a Console API key** as the implementation engine, with a hard spending cap set at console.anthropic.com (start at $10/month; the cost policy in `03-cost-and-model-policy.md` is designed to keep steady-state spend low and flat).

> **Superseded in part — 2026-08-08.** The operator purchased **Claude Pro**, chosen over Max pending evidence that the higher usage ceiling is needed. Claude Code is therefore accessed through the subscription's OAuth login rather than a metered Console API key, and the $10 API cap above no longer applies to interactive work.
>
> The reasoning in this ADR is retained because it remains correct and load-bearing: nothing in this project *requires* a subscription, and the API-key path stays the documented fallback if the subscription is dropped or if unattended automation (which cannot use OAuth) needs to make model calls. Items 2–4 below — Meta Development Mode, GitHub Actions as scheduler, and the action items — are unaffected.
>
> Revisit trigger for Max: hitting the Pro usage ceiling during normal weekly-cycle work, not merely during an unusually heavy session.
- **Do not wait for Meta App Review to start Phase 1.** Add the operator's own Instagram account as Admin/Tester on the Meta app now; own-account ingestion, insights and the whole feedback loop work fully in Development Mode. Defer the App Review question to Phase 4 and re-verify the current permission requirement for `business_discovery` at that time — Meta's access tiers change and must not be assumed from training-era knowledge.
- **Do not provision a server.** GitHub Actions (free tier, personal account) is the scheduler for both `weekly-cycle` and `post-publish-capture` (ADR-0003 already chose CLI+cron over an orchestrator; this just names the free host for that cron). Secrets (`IG_LONG_LIVED_TOKEN`, `ANTHROPIC_API_KEY`, etc.) go in GitHub Actions encrypted secrets, never committed.

## Consequences
+ Zero recurring subscription cost is required to build and run Phases 1–5. The only spend is metered API usage, capped and logged.
+ The human-in-the-loop principle (ADR already implicit in the agent specs) is reinforced by necessity: with a small API budget, the weekly agent steps should default to `--dry-run`-reviewed output before any auto-merge into `knowledge/`.
− GitHub Actions free-tier cron is best-effort timing (can lag under load), not real-time. Acceptable for hourly/weekly cadences; unacceptable if a future requirement needs sub-minute reaction — trigger to revisit is the same as ADR-0003's orchestrator trigger.
− `business_discovery` access tier is an open verification item, tracked as backlog item **[B1b]**, not a blocker for Phase 1.

## Action items (do this week, no cost)
1. Confirm Instagram account is Business/Creator, linked to a Facebook Page (resolves core of B1). If not, convert it — required regardless of budget.
2. Create the Meta Developer app (Business type), add the Instagram Graph API product, add yourself as Admin/Tester. Test one `GET` call for own media insights.
3. Create a free GitHub account/repo (private is fine) and push this project skeleton.
4. Create an Anthropic Console account, generate an API key, set a monthly spend cap (e.g. $10). Do not set `ANTHROPIC_API_KEY` globally in a shell that also runs a paid claude.ai OAuth Claude Code session elsewhere, to avoid accidental double billing (see auth precedence note above).
