# Storage abstraction layer (BUILD-SPEC B9): one interface, two backends.
#
#   SQLiteStorage  - default backend. Stdlib only, reuses the existing
#                    signal.db exactly as the legacy sqlite3 code did, so
#                    behavior is byte-identical when DATABASE_URL is unset.
#   PostgresStorage - optional backend. Active only when DATABASE_URL is
#                    set AND psycopg is importable AND the server responds.
#                    Any of those conditions failing makes get_storage()
#                    fall back to SQLite with a logged warning. No crash.
#
# The public API each backend implements is the Storage interface below:
# connect, migrate, insert_item, get_item, list_items, insert_approval,
# list_audit, upsert_feed, get_feed.
#
# Both backends share one query dialect (question-mark placeholders and
# dict-like rows): the Postgres backend returns a small adapter around a
# psycopg connection that speaks the same mini-API as sqlite3. Parameterized
# queries only, no string-built SQL anywhere.
from __future__ import annotations

import json
import logging
import os
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional

logger = logging.getLogger("storage")

DEFAULT_DB_PATH = Path(__file__).parent / "signal.db"
MIGRATIONS_DIR = Path(__file__).resolve().parent.parent / "migrations"
INIT_SQL_PATH = MIGRATIONS_DIR / "0001_init.sql"

FEED_KEY = "default"

# Tables in the canonical schema (migrations/0001_init.sql). Ordered for
# dump/backup tooling; "audit" and "consent" are append-only log tables.
CANONICAL_TABLES = ["items", "approvals", "audit", "feed_cache", "consent"]

# Postgres does not accept the sqlite AUTOINCREMENT keyword. These are the
# only sqlite-isms in 0001_init.sql and the translation is applied before
# the script is executed on the Postgres backend.
_PG_TRANSLATIONS = [
    ("INTEGER PRIMARY KEY AUTOINCREMENT", "SERIAL PRIMARY KEY"),
]


def _read_init_sql() -> str:
    return INIT_SQL_PATH.read_text()


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


class Storage:
    """Interface every persistence backend implements."""

    def connect(self):
        raise NotImplementedError

    def migrate(self) -> None:
        raise NotImplementedError

    def insert_item(self, item: dict) -> None:
        raise NotImplementedError

    def get_item(self, source_id: str) -> Optional[dict]:
        raise NotImplementedError

    def list_items(self) -> list[dict]:
        raise NotImplementedError

    def insert_approval(self, proposal: dict) -> None:
        raise NotImplementedError

    def list_audit(self) -> list[dict]:
        raise NotImplementedError

    def upsert_feed(self, feed: dict) -> None:
        raise NotImplementedError

    def get_feed(self) -> Optional[dict]:
        raise NotImplementedError


class SQLiteStorage(Storage):
    """Default backend: stdlib sqlite3, same file and semantics as before."""

    def __init__(self, db_path=DEFAULT_DB_PATH):
        self.db_path = Path(db_path)

    def connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, timeout=10)
        conn.row_factory = sqlite3.Row
        return conn

    def migrate(self) -> None:
        conn = self.connect()
        try:
            conn.executescript(_read_init_sql())
            conn.commit()
        finally:
            conn.close()

    def insert_item(self, item: dict) -> None:
        conn = self.connect()
        try:
            conn.execute(
                "INSERT INTO items (channel, source_id, sender, subject, body, "
                "received_at, summary, rank_score, deadline_iso, is_urgent, kind) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (item.get("channel"), item.get("source_id"), item.get("sender"),
                 item.get("subject"), item.get("body"), item.get("received_at"),
                 item.get("summary"), item.get("rank_score", 0.0),
                 item.get("deadline_iso"), int(bool(item.get("is_urgent", False))),
                 item.get("kind")))
            conn.commit()
        finally:
            conn.close()

    def get_item(self, source_id: str) -> Optional[dict]:
        conn = self.connect()
        try:
            row = conn.execute(
                "SELECT * FROM items WHERE source_id=?", (source_id,)).fetchone()
            return dict(row) if row is not None else None
        finally:
            conn.close()

    def list_items(self) -> list[dict]:
        conn = self.connect()
        try:
            rows = conn.execute("SELECT * FROM items").fetchall()
            return [dict(r) for r in rows]
        except sqlite3.OperationalError:
            return []
        finally:
            conn.close()

    def insert_approval(self, proposal: dict) -> None:
        conn = self.connect()
        try:
            conn.execute(
                "INSERT INTO approvals (id, tool, params, reason, evidence, confidence, "
                "status, created_at, decided_at, actor) VALUES (?,?,?,?,?,?,?,?,?,?) "
                "ON CONFLICT (id) DO UPDATE SET tool=excluded.tool, params=excluded.params, "
                "reason=excluded.reason, evidence=excluded.evidence, "
                "confidence=excluded.confidence, status=excluded.status, "
                "created_at=excluded.created_at, decided_at=excluded.decided_at, "
                "actor=excluded.actor",
                (proposal["id"], proposal["tool"], json.dumps(proposal.get("params") or {}),
                 proposal.get("reason"), json.dumps(proposal.get("evidence") or []),
                 proposal.get("confidence", 0.0), proposal.get("status"),
                 proposal.get("created_at"), proposal.get("decided_at"),
                 proposal.get("actor")))
            conn.commit()
        finally:
            conn.close()

    def list_audit(self) -> list[dict]:
        conn = self.connect()
        try:
            rows = conn.execute(
                "SELECT ts, actor, decision, proposal_id, tool, params, evidence, reason "
                "FROM audit ORDER BY id DESC").fetchall()
            return [dict(r) for r in rows]
        finally:
            conn.close()

    def upsert_feed(self, feed: dict) -> None:
        conn = self.connect()
        try:
            conn.execute(
                "INSERT INTO feed_cache (key, value, updated_at) VALUES (?,?,?) "
                "ON CONFLICT (key) DO UPDATE SET value=excluded.value, "
                "updated_at=excluded.updated_at",
                (FEED_KEY, json.dumps(feed), _now()))
            conn.commit()
        finally:
            conn.close()

    def get_feed(self) -> Optional[dict]:
        conn = self.connect()
        try:
            row = conn.execute(
                "SELECT value FROM feed_cache WHERE key=?", (FEED_KEY,)).fetchone()
            if row is None:
                return None
            return json.loads(row["value"])
        except Exception:
            return None
        finally:
            conn.close()


class _CursorAdapter:
    """Dict-row cursor returned by the Postgres connection adapter."""

    def __init__(self, cursor):
        self._cursor = cursor
        self.description = cursor.description

    def _cols(self) -> list:
        return [d[0] for d in self.description] if self.description else []

    def _to_dict(self, row) -> dict:
        return dict(zip(self._cols(), row))

    def fetchone(self) -> Optional[dict]:
        row = self._cursor.fetchone()
        return self._to_dict(row) if row is not None else None

    def fetchall(self) -> list[dict]:
        return [self._to_dict(r) for r in self._cursor.fetchall()]


class _PsycopgAdapter:
    """Thin sqlite-like facade over a psycopg connection.

    Lets the rest of the scaffold (approval.py, serve.py, export tooling)
    run identical SQL on either backend: question-mark placeholders are
    translated to psycopg %s, executescript applies the sqlite-ism
    translation, and rows come back as dicts.
    """

    def __init__(self, psycopg, url: str):
        self._psycopg = psycopg
        self._conn = psycopg.connect(url)
        self.row_factory = None  # sqlite-compat: rows are dict-able already

    def _translate(self, sql: str) -> str:
        return sql.replace("?", "%s")

    def execute(self, sql: str, params=()):
        cur = self._conn.cursor()
        cur.execute(self._translate(sql), params)
        return _CursorAdapter(cur)

    def executescript(self, sql: str) -> None:
        for old, new in _PG_TRANSLATIONS:
            sql = sql.replace(old, new)
        for stmt in sql.split(";"):
            stmt = stmt.strip()
            if stmt:
                with self._conn.cursor() as cur:
                    cur.execute(stmt)

    def commit(self) -> None:
        self._conn.commit()

    def rollback(self) -> None:
        self._conn.rollback()

    def close(self) -> None:
        self._conn.close()


class PostgresStorage(Storage):
    """Optional backend: psycopg (guarded import). Same SQL-ish ops, only
    parameterized queries. translate placeholders / rows to the shared dialect."""

    def __init__(self, url: str):
        self.url = url

    @staticmethod
    def _pg():
        import psycopg  # noqa: PLC0415 - guarded: only reached when importable
        return psycopg

    def connect(self):
        return _PsycopgAdapter(self._pg(), self.url)

    def migrate(self) -> None:
        conn = self.connect()
        try:
            conn.executescript(_read_init_sql())
            conn.commit()
        finally:
            conn.close()

    def insert_item(self, item: dict) -> None:
        conn = self.connect()
        try:
            conn.execute(
                "INSERT INTO items (channel, source_id, sender, subject, body, "
                "received_at, summary, rank_score, deadline_iso, is_urgent, kind) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (item.get("channel"), item.get("source_id"), item.get("sender"),
                 item.get("subject"), item.get("body"), item.get("received_at"),
                 item.get("summary"), item.get("rank_score", 0.0),
                 item.get("deadline_iso"), int(bool(item.get("is_urgent", False))),
                 item.get("kind")))
            conn.commit()
        finally:
            conn.close()

    def get_item(self, source_id: str) -> Optional[dict]:
        conn = self.connect()
        try:
            row = conn.execute(
                "SELECT * FROM items WHERE source_id=?", (source_id,)).fetchone()
            return row
        finally:
            conn.close()

    def list_items(self) -> list[dict]:
        conn = self.connect()
        try:
            return conn.execute("SELECT * FROM items").fetchall()
        except Exception:
            return []
        finally:
            conn.close()

    def insert_approval(self, proposal: dict) -> None:
        conn = self.connect()
        try:
            conn.execute(
                "INSERT INTO approvals (id, tool, params, reason, evidence, confidence, "
                "status, created_at, decided_at, actor) VALUES (?,?,?,?,?,?,?,?,?,?) "
                "ON CONFLICT (id) DO UPDATE SET tool=excluded.tool, params=excluded.params, "
                "reason=excluded.reason, evidence=excluded.evidence, "
                "confidence=excluded.confidence, status=excluded.status, "
                "created_at=excluded.created_at, decided_at=excluded.decided_at, "
                "actor=excluded.actor",
                (proposal["id"], proposal["tool"], json.dumps(proposal.get("params") or {}),
                 proposal.get("reason"), json.dumps(proposal.get("evidence") or []),
                 proposal.get("confidence", 0.0), proposal.get("status"),
                 proposal.get("created_at"), proposal.get("decided_at"),
                 proposal.get("actor")))
            conn.commit()
        finally:
            conn.close()

    def list_audit(self) -> list[dict]:
        conn = self.connect()
        try:
            return conn.execute(
                "SELECT ts, actor, decision, proposal_id, tool, params, evidence, reason "
                "FROM audit ORDER BY id DESC").fetchall()
        finally:
            conn.close()

    def upsert_feed(self, feed: dict) -> None:
        conn = self.connect()
        try:
            conn.execute(
                "INSERT INTO feed_cache (key, value, updated_at) VALUES (?,?,?) "
                "ON CONFLICT (key) DO UPDATE SET value=excluded.value, "
                "updated_at=excluded.updated_at",
                (FEED_KEY, json.dumps(feed), _now()))
            conn.commit()
        finally:
            conn.close()

    def get_feed(self) -> Optional[dict]:
        conn = self.connect()
        try:
            row = conn.execute(
                "SELECT value FROM feed_cache WHERE key=?", (FEED_KEY,)).fetchone()
            if row is None:
                return None
            return json.loads(row["value"])
        except Exception:
            return None
        finally:
            conn.close()


_storage_cache: dict = {}


def _build_storage(url: str, db_path) -> Storage:
    if not url:
        return SQLiteStorage(db_path or DEFAULT_DB_PATH)
    try:
        import psycopg  # noqa: PLC0415 - optional dependency, guarded
    except ImportError:
        logger.warning(
            "DATABASE_URL is set but psycopg is not installed; "
            "falling back to SQLite (offline default)")
        return SQLiteStorage(db_path or DEFAULT_DB_PATH)
    try:
        storage = PostgresStorage(url)
        probe = storage.connect()
        probe.close()
    except Exception as e:  # noqa: BLE001 - any connect failure falls back
        logger.warning(
            "DATABASE_URL is set but Postgres is unreachable (%s); "
            "falling back to SQLite", e)
        return SQLiteStorage(db_path or DEFAULT_DB_PATH)
    logger.info("storage backend: Postgres (host=%s)", url.split("@")[-1])
    return storage


def get_storage(db_path=None) -> Storage:
    """Factory: DATABASE_URL + importable psycopg + reachable server choose
    PostgresStorage, anything else falls back to SQLiteStorage. Cached per
    (url, path) so a broken DATABASE_URL warns once and keeps serving."""
    url = os.environ.get("DATABASE_URL", "").strip()
    key = (url, str(db_path or DEFAULT_DB_PATH))
    cached = _storage_cache.get(key)
    if cached is not None:
        return cached
    storage = _build_storage(url, db_path)
    _storage_cache[key] = storage
    return storage
