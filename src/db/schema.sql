-- AIOS fact store. SQLite, WAL. Migrations are additive and checked in.
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS experiment (
  experiment_id   TEXT PRIMARY KEY,
  hypothesis      TEXT NOT NULL,
  variable        TEXT NOT NULL,              -- exactly one manipulated variable
  control_def     TEXT NOT NULL,
  success_metric  TEXT NOT NULL,
  min_sample      INTEGER NOT NULL DEFAULT 3,
  started_at      TEXT NOT NULL,
  closed_at       TEXT,
  verdict         TEXT NOT NULL DEFAULT 'pending'
                  CHECK (verdict IN ('pending','supported','refuted','inconclusive')),
  verdict_note    TEXT
);

CREATE TABLE IF NOT EXISTS content (
  content_id    TEXT PRIMARY KEY,             -- c_YYYYMMDD_slug
  slug          TEXT NOT NULL,
  format        TEXT NOT NULL CHECK (format IN ('reel','carousel','story','post','live','article')),
  pillar        TEXT NOT NULL,
  status        TEXT NOT NULL CHECK (status IN ('idea','briefed','recorded','edited','scheduled','published','archived')),
  hook_type     TEXT,
  cta_type      TEXT,
  topics        TEXT,                          -- JSON array
  experiment_id TEXT REFERENCES experiment(experiment_id),
  brief_path    TEXT,
  created_at    TEXT NOT NULL,
  updated_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_content_pillar_status ON content(pillar, status);

CREATE TABLE IF NOT EXISTS publication (
  publication_id    TEXT PRIMARY KEY,
  content_id        TEXT NOT NULL REFERENCES content(content_id),
  platform          TEXT NOT NULL,
  platform_media_id TEXT NOT NULL,
  permalink         TEXT,
  media_type        TEXT,
  duration_seconds  REAL,
  published_at      TEXT NOT NULL,
  UNIQUE (platform, platform_media_id)
);
CREATE INDEX IF NOT EXISTS idx_pub_published_at ON publication(published_at);

-- Fixed age buckets: cross-post comparison is invalid at arbitrary ages.
CREATE TABLE IF NOT EXISTS metric_snapshot (
  publication_id     TEXT NOT NULL REFERENCES publication(publication_id),
  age_bucket         TEXT NOT NULL CHECK (age_bucket IN ('h24','h72','d7','d30')),
  captured_at        TEXT NOT NULL,
  reach              INTEGER,
  views              INTEGER,
  likes              INTEGER,
  comments           INTEGER,
  saves              INTEGER,
  shares             INTEGER,
  avg_watch_seconds  REAL,
  total_watch_seconds REAL,
  profile_visits     INTEGER,
  follows            INTEGER,
  schema_version     TEXT NOT NULL,
  raw_json           TEXT NOT NULL,
  PRIMARY KEY (publication_id, age_bucket)
);

CREATE TABLE IF NOT EXISTS account_snapshot (
  captured_on     TEXT PRIMARY KEY,            -- date
  followers       INTEGER NOT NULL,
  follows         INTEGER,
  media_count     INTEGER,
  profile_views   INTEGER,
  raw_json        TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS competitor_account (
  account_id   TEXT PRIMARY KEY,
  username     TEXT NOT NULL UNIQUE,
  tier         TEXT,                            -- follower band for fair comparison
  tracked_since TEXT NOT NULL,
  active       INTEGER NOT NULL DEFAULT 1
);

-- Public metrics only. saves/shares/reach/retention are NOT available (ADR-0005).
CREATE TABLE IF NOT EXISTS competitor_post (
  account_id            TEXT NOT NULL REFERENCES competitor_account(account_id),
  media_id              TEXT NOT NULL,
  media_type            TEXT,
  caption               TEXT,
  permalink             TEXT,
  posted_at             TEXT NOT NULL,
  like_count            INTEGER,
  comments_count        INTEGER,
  followers_at_capture  INTEGER NOT NULL,
  captured_at           TEXT NOT NULL,
  PRIMARY KEY (account_id, media_id)
);
CREATE INDEX IF NOT EXISTS idx_cpost_posted_at ON competitor_post(posted_at);

CREATE TABLE IF NOT EXISTS ingest_run (
  run_id       TEXT PRIMARY KEY,
  source       TEXT NOT NULL,
  window_from  TEXT,
  window_to    TEXT,
  started_at   TEXT NOT NULL,
  finished_at  TEXT,
  status       TEXT NOT NULL CHECK (status IN ('running','ok','partial','failed')),
  item_count   INTEGER DEFAULT 0,
  error        TEXT
);

CREATE TABLE IF NOT EXISTS llm_call (
  call_id       TEXT PRIMARY KEY,
  occurred_at   TEXT NOT NULL,
  agent         TEXT NOT NULL,
  prompt_id     TEXT NOT NULL,
  prompt_version TEXT NOT NULL,
  model         TEXT NOT NULL,
  pack_hash     TEXT NOT NULL,
  input_tokens  INTEGER NOT NULL,
  output_tokens INTEGER NOT NULL,
  cost_usd      REAL NOT NULL,
  latency_ms    INTEGER,
  outcome       TEXT NOT NULL
);
