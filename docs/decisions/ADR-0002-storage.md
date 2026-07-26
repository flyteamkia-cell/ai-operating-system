# ADR-0002 — Storage: SQLite for facts, Markdown+git for knowledge

Status: Accepted · Date: 2026-07-25 · Owner: Architecture

## Context
Two data kinds with opposite requirements: metrics need joins, aggregation and idempotent upserts; brand knowledge needs human review, diffs and history.

## Decision
SQLite (single file, WAL, checked-in migrations) for facts. Markdown with YAML front-matter in git for knowledge. Raw payloads as immutable JSONL. Media outside git.

## Alternatives
- **Postgres/Supabase now** — rejected: no concurrency requirement, adds hosting, credentials and cost. Migration later is mechanical because all access goes through a repository layer.
- **Everything in Markdown** — rejected: metric aggregation across hundreds of posts in Markdown is unreliable and forces the model to do arithmetic.
- **Everything in a database, including knowledge** — rejected: kills reviewability, which is the mechanism that keeps knowledge quality from decaying.
- **Vector database** — rejected for now: see `docs/critique.md`. Revisit trigger: >2,000 chunks or a retrieval-quality failure that deterministic selection cannot fix.

## Consequences
+ Zero operational surface; backup is a file copy plus a git remote.
+ Knowledge changes are pull-requestable.
− Concurrent writers are not supported. Trigger to migrate to Postgres: a second writer, a hosted dashboard, or >10⁶ metric rows.
