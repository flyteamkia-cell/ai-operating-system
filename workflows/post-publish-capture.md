# Workflow: post-publish-capture

**Trigger.** Scheduled hourly; picks up publications due for a snapshot bucket.

**Purpose.** Capture `h24`, `h72`, `d7`, `d30` snapshots. Story insights expire — stories are captured within their lifetime or the data is lost permanently. This is the single most time-sensitive job in the system.

**Validation.** Publication must have a `content_id` (an untracked post is reported as a defect, not silently ingested). Bucket must not already exist — snapshots are write-once.
**Retry.** 3 attempts within the bucket window; if the window closes unfilled, the snapshot is recorded as `missing` rather than backfilled with a later, non-comparable value.
**Error handling.** Never overwrite a good snapshot with a failed fetch.
**Notification.** Any missed story capture alerts immediately; missed stories are unrecoverable.
**Audit.** `ingest_run` row per execution.
