# Workflow: weekly-cycle

**Trigger.** Monday 08:00 local, cron/GitHub Actions. Manual: `aios cycle --week <ISO>`.

**Steps.**
1. `ingest:instagram-own` — media + insights for the window. Validation: token valid ≥7 days, schema version matches, item count > 0.
2. `ingest:instagram-competitors` — business_discovery for the active set. Partial failure tolerated up to 20% of accounts; above that the step fails.
3. `normalize` — upsert into SQLite, idempotent by (publication_id, age_bucket).
4. `analyze` — deterministic aggregates, baselines, experiment sample checks. No model.
5. `pack` — build context packs; abort if any pack exceeds its token ceiling.
6. `agent:performance-analyst` → `reports/weekly/<week>/performance.md`
7. `agent:market-signal` → `reports/weekly/<week>/market.md`
8. `agent:content-strategist` → weekly plan + briefs (frontier model)
9. `curate` — Brand Curator proposes knowledge diffs.
10. `deliver` — open a git branch `cycle/<week>`, notify with a summary and the cost of the run.

**Validation.** Each step declares preconditions; a failed precondition aborts the cycle and leaves prior state untouched.
**Retry.** Network steps: 3 attempts, exponential backoff with jitter. Model steps: 1 retry, then fail — silent retries on nondeterministic output hide defects.
**Logging.** One JSONL line per step: run_id, step, duration, item counts, cost, outcome.
**Error handling.** Ingestion failure → cycle aborts before any model spend. Model failure → prior reports remain valid; the cycle is resumable from the failed step.
**Notification.** Success: one summary message with cost and the week's slate. Failure: step name, error class, and the remediation command.
**Metrics.** Cycle duration, cost, ingest completeness, brief acceptance (recorded later by the operator).
**Recovery.** `aios rebuild` replays raw → SQLite. `aios cycle --resume <run_id>`.
**Audit.** Every artifact records run_id, pack hash and prompt version in its front-matter.
