"""Research index: the EVIDENCE-INDEX.md report map as searchable JSON.

Parses every table row in research-inputs/EVIDENCE-INDEX.md into
{id, description, proof, feeds, wave} and exposes search + JSON export.
The index is the source of truth; only the rows present in the file are
indexed (the file covers waves 1-6; report ids d21-d24 are absent from
the index and are never invented).
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Optional

DEFAULT_INDEX_PATH = Path(__file__).resolve().parent.parent.parent / "research-inputs" / "EVIDENCE-INDEX.md"

_WAVE_RE = re.compile(r"^##\s+WAVE\s+(\d+)", re.I)
_ROW_RE = re.compile(r"^\|\s*(d\d+[a-z]*)\s*([^|]*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load_index(path=None) -> list[dict]:
    """Parse EVIDENCE-INDEX.md into a list of report dicts."""
    path = Path(path) if path else DEFAULT_INDEX_PATH
    rows: list[dict] = []
    wave = "UNKNOWN"
    for line in path.read_text().splitlines():
        m = _WAVE_RE.match(line)
        if m:
            wave = f"wave{m.group(1)}"
            continue
        m = _ROW_RE.match(line)
        if m:
            rows.append({
                "id": m.group(1),
                "description": _clean(m.group(2)),
                "proof": _clean(m.group(3)),
                "feeds": _clean(m.group(4)),
                "wave": wave,
            })
    for i, row in enumerate(rows):
        row["index"] = i
    return rows


def search(rows: list[dict], query: str) -> list[dict]:
    """Case-insensitive substring search across id, description, proof,
    feeds, and wave. Returns matching rows in index order."""
    q = query.strip().lower()
    if not q:
        return list(rows)
    hits = []
    for row in rows:
        hay = " ".join(str(row.get(k, "")) for k in ("id", "description", "proof", "feeds", "wave")).lower()
        if q in hay:
            hits.append(row)
    return hits


def get(rows: list[dict], report_id: str) -> Optional[dict]:
    """Look up one report by id (for example 'd31')."""
    for row in rows:
        if row["id"].lower() == report_id.lower():
            return row
    return None


def to_json(rows: list[dict]) -> dict:
    """The searchable index as a JSON document."""
    return {
        "schema": "krishisetu-research-index-v1",
        "source": "research-inputs/EVIDENCE-INDEX.md",
        "count": len(rows),
        "waves": sorted({r["wave"] for r in rows}),
        "reports": rows,
    }


if __name__ == "__main__":
    index = load_index()
    doc = to_json(index)
    print(json.dumps({"count": doc["count"], "waves": doc["waves"]}))
