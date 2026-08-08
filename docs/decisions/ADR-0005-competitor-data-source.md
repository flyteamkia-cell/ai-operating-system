# ADR-0005 — Competitor data via Graph API business_discovery, not scraping

Status: Accepted · Date: 2026-07-25 · Owner: Architecture

## Decision
Competitor intelligence uses the official `business_discovery` endpoint only. Scraping and browser automation are excluded from all scheduled workflows.

## Rationale
The account is the business asset; automation that risks it has unbounded downside. Scraped pipelines break silently and without notice, and every downstream conclusion inherits that unreliability. The official endpoint provides enough for structural analysis (see `docs/architecture/02-instagram-data-strategy.md`).

## Consequences
− No competitor saves/shares/reach/retention. Analysis is restricted to structure, topic, cadence and a followers-normalized public engagement proxy. This limitation is stated in every generated market report so conclusions are never over-read.
− Competitors that are personal (non-business) accounts are invisible to the system and must be sampled manually into `knowledge/market/manual-observations.md`.
