#!/usr/bin/env python3
"""Export every storage table to JSON Lines (BUILD-SPEC B9).

Dumps the canonical schema (items, approvals, audit, feed_cache, consent)
row by row. Each line is one JSON object with a "_table" field so the
dataset can be split back out. Default output is stdout.

Usage:
    python3 scripts/export_data.py [--out file.jsonl] [--db /path/signal.db]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCAFFOLD = HERE.parent
if str(SCAFFOLD / "engine") not in sys.path:
    sys.path.insert(0, str(SCAFFOLD / "engine"))

import storage  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Dump storage tables to JSON Lines")
    ap.add_argument("--out", default="", help="output file (default stdout)")
    ap.add_argument("--db", default="", help="sqlite db path override")
    args = ap.parse_args()

    db_path = Path(args.db) if args.db else None
    store = storage.get_storage(db_path)
    store.migrate()

    conn = store.connect()
    lines = 0
    out_fh = open(args.out, "w") if args.out else sys.stdout
    try:
        for table in storage.CANONICAL_TABLES:
            try:
                rows = conn.execute(f"SELECT * FROM {table}").fetchall()
            except Exception:
                continue
            for row in rows:
                record = dict(row)
                record["_table"] = table
                out_fh.write(json.dumps(record) + "\n")
                lines += 1
    finally:
        conn.close()
        if out_fh is not sys.stdout:
            out_fh.close()

    print(f"[export] {lines} rows across {len(storage.CANONICAL_TABLES)} tables",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
