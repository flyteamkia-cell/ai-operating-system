# Evidence

Manually collected performance data (Track B, ADR-0008). Own-account data only — see `docs/architecture/02-instagram-data-strategy.md` for why competitor saves/sends can never appear here.

| File | n | Contents |
|---|---|---|
| `own-account-151-posts.csv` | 151 | Reels and carousels: likes, comments, shares, saves, reach, follows, non-follower % |
| `own-account-20-transcribed.csv` | 20 | Subset with full transcripts, coded for hook type, CTA type, actionability, promise-kept. 10 labelled good, 10 weak by the operator |

Analysis: `scripts/analyze_own_account.py`. Findings: `knowledge/content/patterns.md`.

## Known data quality issues

These are recorded rather than silently corrected. A guessed value is worse than a flagged gap.

**1. Duplicate source, rows 17 and 18** (`own-account-20-transcribed.csv`) — both rows carry the same `reel/DHNmHS8tsRw` URL and the same transcript, but different metrics. One of the two is mis-sourced; row 18 ("مسیر ترید اصولی") appears to have inherited row 17's transcript. **Neither row is used for any transcript-level finding.** Their metrics are similar enough that including or excluding them does not change any conclusion in `patterns.md`. Needs re-extraction.

**2. Missing average watch time on the five highest performers** (rows 6–10). The watch-time comparison in P-104 therefore rests on half the sample and is likely an underestimate. Flagged in `patterns.md`.

**3. Missing views on row 5** — reach is present, so all rate calculations are unaffected.

**4. `repost` column is empty or zero throughout** — appears to be an artefact of the newer Instagram insights layout rather than genuine zeros.

**5. Obviously invalid rows in the 151-post set** — e.g. views recorded as 219,651 against a reach of 10,284. Corrected where the intended value was unambiguous, dropped where it was not.

## Rules for adding to this directory

- Never fabricate, estimate, or round a missing metric. Leave it blank.
- Always record follower count at time of posting; without it no cross-account comparison is valid.
- Weak posts are required, not optional. A set containing only winners produces false patterns.
- Never merge peer or competitor data into these files. Different metric availability, different confidence tier — keep them in separate files.
