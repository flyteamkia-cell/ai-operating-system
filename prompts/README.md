# Prompts as software

Every prompt is a versioned artifact with an owner, a typed I/O contract, examples, evaluation criteria and known failure cases. Prompts are never edited in place without a version bump; the running version is recorded in every artifact's front-matter so any output can be traced to the exact prompt that produced it.

Layout: `prompts/<domain>/<id>.md`. Fixtures: `prompts/<domain>/evals/<id>/*.json`.
Changing a prompt requires re-running its fixtures and recording the result in the changelog section.
