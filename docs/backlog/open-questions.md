# Open Questions

`[B]` = blocks Phase 1. `[N]` = needed later, not blocking. Answers are recorded here and promoted into ADRs or knowledge files.

## Blocking
**[B1] Instagram account configuration.** Is the account a Business or Creator account, connected to a Facebook Page, with admin access to create a Meta app? If not, this is the first task; nothing downstream works without it, and *insight history does not backfill* — every day before conversion is permanently lost data.
*Resolved for Phase 1 by ADR-0006: Development Mode (no App Review) is sufficient for own-account ingestion — just add the account as Admin/Tester on the Meta app.* Still open: confirm the account type itself.

**[B1b] `business_discovery` access tier.** Re-verify at Phase 4, against Meta's current docs (not assumed from training data), whether reading competitor public data still sits under Standard/self-serve access or now requires Advanced Access + App Review. Not a Phase 1 blocker.

**[B2] Conversion event.** ✅ **RESOLVED — ADR-0009.** Audience: the trader who has entered the market and lost money (the only segment feeding all four revenue lines). Conversion event for Track B: entry into the Telegram channel. Original text below for context.

~~[B2]~~ What is the business outcome content exists to produce — VIP channel subscription, course sale, lead capture, brand deals, something else? What is its current monthly volume and value? Without this the system optimizes reach, which is the cheapest and least valuable outcome. This determines the entire KPI tree and cannot be deferred.

**[B3] Current baseline.** Follower count, posting cadence, average reach/saves/shares over the last 30 days, and how long the account has been a Business account. Needed to set experiment sample thresholds — with low volume, most week-over-week comparisons are noise and the system must be told to say "inconclusive" rather than invent causes.

**[B4] Execution environment and budget.** *Resolved by ADR-0006: no VPS needed — GitHub Actions (free tier) is the scheduler, Claude Code runs via a pay-per-token Console API key (no Pro/Max subscription required).* Still open: the actual monthly spend ceiling to configure at console.anthropic.com (suggested starting point: $10; adjust after Phase 1's first real cost data).

**[B5] Competitor set.** 🔄 **In progress** — 5 peer/competitor accounts collected (~10–20 posts each). Note: peers sharing their *own* insights are a higher confidence tier than competitors observed publicly; keep separate (see `docs/architecture/04-collection-schema-mapping.md`). Original text below.

~~[B5]~~ Which 15–25 accounts, and are they Business/Creator accounts (required for `business_discovery`)? Personal accounts are invisible to the supported API path (ADR-0005).

## Non-blocking
**[N1]** Existing knowledge assets — past scripts, notes, transcripts, an existing Notion/Obsidian vault — that should seed `knowledge/`.
**[N2]** Reels in Persian: is transcription of past content wanted (Whisper) to mine hook patterns from existing material?
**[N3]** Editing toolchain and whether generated editing prompts must target a specific tool.
**[N4]** Telegram/other channels: audience overlap and whether they enter the data layer in Phase 7.
**[N5]** Compliance: financial-content disclaimer requirements and any claim language that must never appear in generated copy. Candidate for `knowledge/brand/banned-patterns.md`.
**[N6]** Is anyone else (editor, assistant) touching the workflow? Changes the concurrency and permission model.
