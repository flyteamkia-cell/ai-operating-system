# ADR-0004 — Language of record

Status: Accepted · Date: 2026-07-25 · Owner: Architecture

## Decision
- Code, schemas, ADRs, architecture docs, agent specs, prompts' structural sections: **English**.
- Brand knowledge content, audience insights, hooks, scripts, captions, and all generated content artifacts: **Persian (fa-IR)**, since that is the audience language.
- Every knowledge file declares `lang:` in front-matter. Prompts declare the required output language explicitly; it is never inferred.

## Rationale
Mixed-language technical documentation degrades both retrieval and model performance and doubles maintenance. Content artifacts must be native-language because tone, hook rhythm and idiom do not survive translation. Persian-specific handling (RTL, transliterated finance terms, Persian numerals in on-screen text) is a first-class requirement of the content prompts, not an afterthought.
