-- 0001_init.sql - canonical storage schema (BUILD-SPEC B9).
-- Applied by Storage.migrate() on both backends. Idempotent: every
-- statement uses IF NOT EXISTS, so running migrate() twice is a no-op.
-- sqlite executes this file directly. The Postgres backend translates
-- the one sqlite-ism before execution (AUTOINCREMENT -> SERIAL, see
-- PostgresStorage.migrate).

CREATE TABLE IF NOT EXISTS items (
    channel TEXT,
    source_id TEXT,
    sender TEXT,
    subject TEXT,
    body TEXT,
    received_at TEXT,
    summary TEXT,
    rank_score REAL,
    deadline_iso TEXT,
    is_urgent INTEGER,
    kind TEXT
);

CREATE TABLE IF NOT EXISTS approvals (
    id TEXT PRIMARY KEY,
    tool TEXT,
    params TEXT,
    reason TEXT,
    evidence TEXT,
    confidence REAL,
    status TEXT,
    created_at TEXT,
    decided_at TEXT,
    actor TEXT
);

CREATE TABLE IF NOT EXISTS audit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT,
    actor TEXT,
    decision TEXT,
    proposal_id TEXT,
    tool TEXT,
    params TEXT,
    evidence TEXT,
    reason TEXT
);

CREATE TABLE IF NOT EXISTS feed_cache (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS consent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    scope TEXT,
    granted_by TEXT,
    granted_at TEXT,
    revoke_at TEXT,
    UNIQUE(subject, scope)
);
