"""The 11-state incident machine with CAP semantics.

MONITOR -> PRE_CYCLONE_WATCH (72h) -> CYCLONE_ALERT (48h) ->
CYCLONE_WARNING (24h) -> POST_LAND_FALL_OUTLOOK (12h) ->
IMPACT_SUSPECTED -> IMPACT_CONFIRMED -> RESPONSE -> RECOVERY ->
NEXT_SEASON -> CLOSED.

Rules:
  * CAP semantics: a same-state event for the same incident is an update,
    never a duplicate (THE-PLAN Part 2).
  * Severity batching under 100x spikes groups by severity, never by
    timestamp.
  * The machine never closes on the first recession: RECOVERY is fed by
    RESPONSE and feeds NEXT_SEASON; CLOSED is reachable only from
    NEXT_SEASON. A recession event in RECOVERY is an update, and a second
    flood returns the machine to IMPACT_SUSPECTED (second-flood semantics).
"""
from __future__ import annotations

from datetime import datetime
from typing import Optional

STATES = [
    "MONITOR",
    "PRE_CYCLONE_WATCH",
    "CYCLONE_ALERT",
    "CYCLONE_WARNING",
    "POST_LAND_FALL_OUTLOOK",
    "IMPACT_SUSPECTED",
    "IMPACT_CONFIRMED",
    "RESPONSE",
    "RECOVERY",
    "NEXT_SEASON",
    "CLOSED",
]

# Allowed forward and downgrade transitions.
TRANSITIONS = {
    "MONITOR": ["PRE_CYCLONE_WATCH"],
    "PRE_CYCLONE_WATCH": ["CYCLONE_ALERT", "MONITOR"],
    "CYCLONE_ALERT": ["CYCLONE_WARNING", "PRE_CYCLONE_WATCH"],
    "CYCLONE_WARNING": ["POST_LAND_FALL_OUTLOOK", "CYCLONE_ALERT"],
    "POST_LAND_FALL_OUTLOOK": ["IMPACT_SUSPECTED"],
    "IMPACT_SUSPECTED": ["IMPACT_CONFIRMED"],
    "IMPACT_CONFIRMED": ["RESPONSE"],
    "RESPONSE": ["RECOVERY"],
    "RECOVERY": ["NEXT_SEASON", "IMPACT_SUSPECTED"],
    "NEXT_SEASON": ["CLOSED"],
    "CLOSED": [],
}

SEVERITY_RANK = {"LOW": 0, "MODERATE": 1, "HIGH": 2, "SEVERE": 3, "UNSPECIFIED": 9}


class IncidentMachine:
    """One versioned incident. Same incident id + same state = update,
    never a duplicate CAP record."""

    def __init__(self, incident_id: str, start: str = "MONITOR"):
        if start not in STATES:
            raise ValueError(f"unknown start state: {start}")
        self.incident_id = incident_id
        self.state = start
        self.events: list[dict] = []
        self.transition_log: list[dict] = []
        self.updates = 0

    def apply(self, event: dict) -> dict:
        """Apply one CAP-style event. Returns a record describing the result.

        event keys: state (target state), severity, ts, source, payload.
        Special kinds: 'recession' and 'flood_renewed' drive the
        never-close-on-first-recession and second-flood semantics.
        """
        kind = event.get("kind", "state")
        ts = event.get("ts") or datetime.now().isoformat(timespec="seconds")
        base = {"incident_id": self.incident_id, "ts": ts,
                "severity": event.get("severity", "UNSPECIFIED"),
                "source": event.get("source", "signal")}

        if kind == "recession":
            if self.state in ("RECOVERY", "NEXT_SEASON"):
                self.updates += 1
                self.events.append({**base, "kind": "recession",
                                    "note": "first recession does not close the incident"})
                return {"state": self.state, "kind": "update",
                        "note": "never close on first recession"}
            return {"state": self.state, "kind": "rejected",
                    "reason": "recession event outside RECOVERY"}

        if kind == "flood_renewed":
            if self.state in ("RECOVERY", "NEXT_SEASON"):
                return self._transition("IMPACT_SUSPECTED", {**base, "kind": "flood_renewed"})
            return {"state": self.state, "kind": "rejected",
                    "reason": "flood_renewed only meaningful from RECOVERY"}

        target = event.get("state")
        if target not in STATES:
            return {"state": self.state, "kind": "rejected", "reason": f"unknown state {target}"}

        if target == self.state:
            self.updates += 1
            self.events.append({**base, "kind": "state", "state": target,
                                "note": "CAP update, no duplicate"})
            return {"state": self.state, "kind": "update"}
        return self._transition(target, {**base, "kind": "state"})

    def _transition(self, target: str, event: dict) -> dict:
        if target not in TRANSITIONS.get(self.state, []):
            return {"state": self.state, "kind": "rejected",
                    "reason": f"no transition {self.state} -> {target}"}
        self.transition_log.append({"from": self.state, "to": target, "ts": event.get("ts")})
        self.state = target
        self.events.append({**event, "kind": event.get("kind", "state")})
        return {"state": self.state, "kind": "transition"}

    def transition_count(self) -> int:
        return len(self.transition_log)


def batch_by_severity(events: list[dict]) -> list[tuple]:
    """CAP-style batching under spikes: group by severity, never by
    timestamp. Returns ordered (severity, [events]) groups, HIGH to LOW."""
    buckets: dict[str, list] = {}
    for ev in events:
        sev = ev.get("severity", "UNSPECIFIED")
        buckets.setdefault(sev, []).append(ev)
    return sorted(buckets.items(), key=lambda kv: SEVERITY_RANK.get(kv[0], 9))
