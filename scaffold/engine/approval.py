# Approval gate - typed tools, policy gate, and audit trail.
# Part 1 of BUILD-SPEC: a trustworthy agent with approved tools + audit trail.
#
# Pure stdlib. Reuses scaffold/engine/signal.db (never drops the items table).

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "signal.db"

# Side-effect classes
READ_ONLY = "read-only"
REVERSIBLE = "reversible"
SIDE_EFFECTING = "side-effecting"

# Proposal statuses
PENDING = "pending"
APPROVED = "approved"
REJECTED = "rejected"
EXECUTED = "executed"
SNOOZED = "snoozed"


@dataclass
class Tool:
    name: str
    description: str
    params: dict
    side_effect: str


TOOL_REGISTRY: dict[str, Tool] = {
    "lookup_room": Tool(
        name="lookup_room",
        description="Look up a room or venue for an event or meeting",
        params={"query": "str"},
        side_effect=READ_ONLY,
    ),
    "send_reminder": Tool(
        name="send_reminder",
        description="Send a reminder to a person or group about a deadline",
        params={"who": "str", "what": "str", "when": "str"},
        side_effect=REVERSIBLE,
    ),
    "submit_form": Tool(
        name="submit_form",
        description="Submit a form on the user's behalf",
        params={"form_id": "str", "answers": "dict"},
        side_effect=SIDE_EFFECTING,
    ),
    "pay_fee": Tool(
        name="pay_fee",
        description="Pay a fee for the user",
        params={"amount": "number", "ref": "str"},
        side_effect=SIDE_EFFECTING,
    ),
}


@dataclass
class Proposal:
    id: str
    tool: str
    params: dict
    reason: str
    evidence: list
    confidence: float
    status: str
    created_at: str
    decided_at: str | None = None
    actor: str | None = None

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "tool": self.tool,
            "params": self.params,
            "reason": self.reason,
            "evidence": self.evidence,
            "confidence": self.confidence,
            "status": self.status,
            "created_at": self.created_at,
            "decided_at": self.decided_at,
            "actor": self.actor,
        }


def gate(tool: Tool) -> str:
    """Policy gate: read-only auto-executes, reversible suggests, side-effecting requires."""
    if tool.side_effect == READ_ONLY:
        return "auto"
    if tool.side_effect == REVERSIBLE:
        return "suggest"
    return "require"


# ────────────────────────────────────────────────────────────────
# SQLite persistence
# ────────────────────────────────────────────────────────────────

_SCHEMA = """
CREATE TABLE IF NOT EXISTS proposals (
    id TEXT PRIMARY KEY, tool TEXT, params TEXT, reason TEXT,
    evidence TEXT, confidence REAL, status TEXT,
    created_at TEXT, decided_at TEXT, actor TEXT);
CREATE TABLE IF NOT EXISTS audit_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT, actor TEXT,
    decision TEXT, proposal_id TEXT, tool TEXT, params TEXT,
    evidence TEXT, reason TEXT);
"""


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(_SCHEMA)
    return conn


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _next_proposal_id(conn: sqlite3.Connection) -> str:
    rows = conn.execute("SELECT id FROM proposals").fetchall()
    mx = 0
    for r in rows:
        try:
            mx = max(mx, int(r["id"].split("-")[1]))
        except Exception:
            pass
    return f"P-{mx + 1}"


def save_proposal(proposal: Proposal) -> None:
    conn = _connect()
    conn.execute(
        "INSERT INTO proposals (id, tool, params, reason, evidence, confidence, status, "
        "created_at, decided_at, actor) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (proposal.id, proposal.tool, json.dumps(proposal.params), proposal.reason,
         json.dumps(proposal.evidence), proposal.confidence, proposal.status,
         proposal.created_at, proposal.decided_at, proposal.actor))
    conn.commit()
    conn.close()


def _write_audit(conn: sqlite3.Connection, actor: str, decision: str, proposal: Proposal) -> None:
    conn.execute(
        "INSERT INTO audit_events (ts, actor, decision, proposal_id, tool, params, "
        "evidence, reason) VALUES (?,?,?,?,?,?,?,?)",
        (_now(), actor, decision, proposal.id, proposal.tool, json.dumps(proposal.params),
         json.dumps(proposal.evidence), proposal.reason))


def decide(proposal_id: str, decision: str, actor: str = "user") -> Proposal | None:
    """Apply a decision. Audit row is written BEFORE the status flips."""
    conn = _connect()
    row = conn.execute("SELECT * FROM proposals WHERE id=?", (proposal_id,)).fetchone()
    if row is None:
        conn.close()
        return None
    proposal = _row_to_proposal(row)
    tool = TOOL_REGISTRY.get(proposal.tool)
    decision_l = decision.lower()

    if proposal.status not in (PENDING, SNOOZED):
        conn.close()
        return proposal

    new_status = proposal.status
    if decision_l == "approve":
        if tool is not None and tool.side_effect == REVERSIBLE:
            new_status = APPROVED
        else:
            new_status = EXECUTED
    elif decision_l == "reject":
        new_status = REJECTED
    elif decision_l == "snooze":
        new_status = SNOOZED

    _write_audit(conn, actor, decision_l, proposal)
    conn.execute(
        "UPDATE proposals SET status=?, decided_at=?, actor=? WHERE id=?",
        (new_status, _now(), actor, proposal_id))
    conn.commit()
    proposal.status = new_status
    proposal.decided_at = _now()
    proposal.actor = actor
    conn.close()
    return proposal


def _row_to_proposal(row: sqlite3.Row) -> Proposal:
    return Proposal(
        id=row["id"],
        tool=row["tool"],
        params=json.loads(row["params"] or "{}"),
        reason=row["reason"],
        evidence=json.loads(row["evidence"] or "[]"),
        confidence=row["confidence"],
        status=row["status"],
        created_at=row["created_at"],
        decided_at=row["decided_at"],
        actor=row["actor"],
    )


def list_proposals() -> list[Proposal]:
    conn = _connect()
    rows = conn.execute("SELECT * FROM proposals ORDER BY created_at DESC").fetchall()
    conn.close()
    return [_row_to_proposal(r) for r in rows]


def list_audit() -> list[dict]:
    conn = _connect()
    rows = conn.execute(
        "SELECT ts, actor, decision, proposal_id, tool, params, evidence, reason "
        "FROM audit_events ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def propose(tool_name: str, params: dict, reason: str, evidence: list,
            confidence: float) -> Proposal:
    """Create and persist a proposal, applying the policy gate.

    Read-only tools auto-execute immediately (still audited). Reversible and
    side-effecting tools stay pending until a human decides.
    """
    conn = _connect()
    pid = _next_proposal_id(conn)
    tool = TOOL_REGISTRY.get(tool_name)
    gate_mode = gate(tool) if tool else "suggest"
    proposal = Proposal(
        id=pid, tool=tool_name, params=params, reason=reason, evidence=evidence,
        confidence=confidence, status=PENDING, created_at=_now())
    if gate_mode == "auto":
        proposal.status = EXECUTED
        proposal.decided_at = _now()
        proposal.actor = "system"
        _write_audit(conn, "system", "auto-execute", proposal)
    conn.execute(
        "INSERT INTO proposals (id, tool, params, reason, evidence, confidence, status, "
        "created_at, decided_at, actor) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (proposal.id, proposal.tool, json.dumps(proposal.params), proposal.reason,
         json.dumps(proposal.evidence), proposal.confidence, proposal.status,
         proposal.created_at, proposal.decided_at, proposal.actor))
    conn.commit()
    conn.close()
    return proposal
