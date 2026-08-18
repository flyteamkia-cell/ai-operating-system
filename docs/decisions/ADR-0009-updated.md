# ADR-0009 — Target audience and conversion event

Status: Accepted (conversion event superseded 2026-08-08) · Date: 2026-08-08 · Owner: Human (operator)

## Context

Backlog item B2 was the longest-standing blocker in the project. Without a defined conversion event, the system optimizes for reach — the cheapest and least valuable outcome for a financial-markets brand — and every generated CTA is a guess.

The brand has four revenue lines: exchange/broker affiliate, VIP channel, copy trading, and education. All four declined together. That pattern indicates the problem is not audience selection but that the account stopped being categorizable — under Instagram's current mechanics, an account the algorithm cannot classify loses distribution, and users can now remove a topic category from their own feed.

## Decision

**Primary audience: the trader who has entered the market and lost money.**

Rationale — it is the only audience segment that feeds all four revenue lines:

| Audience | Affiliate | VIP | Copy trading | Education |
|---|---|---|---|---|
| Complete beginner | ✅ | ❌ | ❌ | ✅ |
| **Has lost money** | ✅ | ✅ | ✅ | ✅ |
| Semi-professional | ⚠️ | ✅ | ⚠️ | ❌ |

A beginner buys two of four; a semi-professional buys two of four; the loss-experienced trader is a candidate for all four. They may switch brokers, seek guidance, want to learn, or conclude they should copy rather than trade themselves.

This segment also aligns with the content mechanism that carries the highest share rate: recognition — content that names an experience the viewer has had but not articulated.

**Conversion event (Track B): follower growth driven by saves and shares — not likes or comments.**

Rationale: `knowledge/content/patterns.md` (P-004) found engagement (likes/comments) has no relationship with growth — correlation of comment rate with non-follower reach is r=−0.05, like rate is r=−0.17. A post with 6,800 comments had a lower send rate than four weak posts. Optimizing for "engagement" would repeat the mechanism that already failed.

Additionally, Instagram's current link restrictions make an external CTA (Telegram) structurally weaker than an in-platform one. CTAs stay in-platform (e.g. "send to a friend who...", "save this") until the account's follower base and distribution are healthy. Multi-stage funnel CTAs (VIP, copy trading, broker) are deferred until this base stage is measurably working — once it is, Telegram becomes the next funnel stage, not the first one.

## Alternatives considered

- **Complete beginner** — rejected: highest volume but lowest monetizable surface; only reaches two of four revenue lines.
- **Semi-professional** — rejected: strongest for VIP but structurally excludes education, and it is the hardest segment to win on credibility without a public track record.
- **A full multi-stage funnel with stage-specific CTAs**, as proposed by the collaborating model — deferred, not rejected. The funnel framing is correct, but assigning CTAs to stages before any stage is instrumented would produce untestable content. Revisit once Telegram entry is measurable.
- **Telegram entry as the conversion event** — superseded 2026-08-08: Instagram's link restrictions make an external CTA structurally weaker right now, and the account's underlying distribution problem (P-004: engagement ≠ growth) needs fixing first. Telegram remains the next funnel stage once follower growth is healthy.

## Consequences

+ Every generated CTA now has a defined target rather than a guess.
+ Content pillars and hook selection can be evaluated against a single audience definition.
− Narrowing risks alienating existing followers who came for other content. Mitigated by the finding in `knowledge/content/patterns.md` that specificity, not topic, drives distribution — narrowing the audience does not require narrowing the topic range.
− "Qualified audience" in `README.md`'s North Star Metric can now be defined concretely; that refinement is pending and tracked as follow-up.
