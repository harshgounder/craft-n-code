"""PMFBY claim packet builder and exporters.

The claim rail (THE-PLAN Part 6): photo + voice + geo evidence, a 72-hour
intimation clock from the damaging event, and a 33% yield-loss threshold
for eligibility. The 72-hour clock is ODISHA-MEASURED (PMFBY intimation
norms); the 33% threshold is ODISHA-MEASURED (Odisha SRC assessment
threshold, d20/d22).

Exporters are pure string builders plus a small writer that emits the
packet as text, a self-contained printable HTML form, and one SVG damage
tag image per evidence item. All exports are SIMULATED packet drafts, not
filed claims.
"""
from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

INTIMATION_WINDOW_HOURS = 72
LOSS_THRESHOLD = 0.33
"""33% yield-loss eligibility threshold. Odisha SRC (State Revenue Cell)
assessment threshold (d20/d22)."""

REQUIRED_EVIDENCE = ["geo", "photo"]


def build_packet(claim: dict, now: Optional[datetime] = None) -> dict:
    """Assemble and gate a claim packet.

    `claim` keys: claim_id, farmer, incident, event_time (ISO or datetime),
    loss_fraction, evidence (list of {type, ts, file, note}).
    Returns the packet with intimation and threshold gates evaluated.
    """
    now = now or datetime.now()
    event_time = claim.get("event_time")
    if isinstance(event_time, str):
        event_time = datetime.fromisoformat(event_time)
    event_time_unknown = event_time is None
    if event_time_unknown:
        event_time = now

    deadline = event_time + timedelta(hours=INTIMATION_WINDOW_HOURS)
    on_time = now <= deadline
    hours_since = (now - event_time).total_seconds() / 3600.0

    loss_frac = float(claim.get("loss_fraction", 0.0))
    eligible = loss_frac >= LOSS_THRESHOLD

    evidence = list(claim.get("evidence", []))
    present = {e.get("type") for e in evidence}
    missing = [t for t in REQUIRED_EVIDENCE if t not in present]

    return {
        "claim_id": claim.get("claim_id", "CLAIM-UNSET"),
        "farmer": claim.get("farmer", {}),
        "incident": claim.get("incident", {}),
        "event_time": event_time.isoformat(timespec="seconds"),
        "event_time_unknown": event_time_unknown,
        "intimation_deadline": deadline.isoformat(timespec="seconds"),
        "intimation_on_time": on_time,
        "hours_since_event": round(hours_since, 1),
        "intimation_window_hours": INTIMATION_WINDOW_HOURS,
        "loss_fraction": round(loss_frac, 4),
        "threshold": LOSS_THRESHOLD,
        "eligible": eligible,
        "evidence": evidence,
        "required_evidence": REQUIRED_EVIDENCE,
        "missing_evidence": missing,
        "simulated": True,
        "label": "SIMULATED claim packet draft - not a filed PMFBY claim",
    }


def export_text(packet: dict) -> str:
    """Plain-text rendering of the claim packet."""
    farmer = packet.get("farmer", {})
    incident = packet.get("incident", {})
    lines = [
        f"CLAIM PACKET {packet['claim_id']}",
        "=" * 40,
        f"Farmer: {farmer.get('name', farmer.get('id', 'unknown'))}",
        f"Farm: {farmer.get('id', '')} ({farmer.get('district', '')})",
        f"Incident: {incident.get('name', incident.get('id', ''))}",
        f"Event time: {packet['event_time']}",
        f"Intimation deadline (within {packet['intimation_window_hours']}h): "
        f"{packet['intimation_deadline']}",
        f"Intimation on time: {packet['intimation_on_time']} "
        f"(hours since event: {packet['hours_since_event']})",
        f"Loss fraction: {packet['loss_fraction']} "
        f"(threshold {packet['threshold']}) -> eligible: {packet['eligible']}",
        f"Evidence: {[e.get('type') for e in packet['evidence']]}",
        f"Missing required evidence: {packet['missing_evidence'] or 'none'}",
        f"Label: {packet['label']}",
    ]
    return "\n".join(lines)


def export_printable(packet: dict) -> str:
    """Self-contained printable HTML (no external assets)."""
    farmer = packet.get("farmer", {})
    incident = packet.get("incident", {})
    evidence_rows = "\n".join(
        f"<tr><td>{e.get('type')}</td><td>{e.get('ts')}</td>"
        f"<td>{e.get('file') or ''}</td></tr>"
        for e in packet["evidence"]
    )
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Claim {packet['claim_id']}</title>
<style>
  body {{ font-family: Arial, sans-serif; margin: 2rem; color: #111; }}
  h1 {{ font-size: 1.3rem; }} table {{ border-collapse: collapse; width: 100%; }}
  td, th {{ border: 1px solid #444; padding: 6px 10px; text-align: left; }}
  .gate {{ padding: 4px 10px; display: inline-block; border-radius: 4px; color: #fff; }}
  .ok {{ background: #1a7f37; }} .no {{ background: #b42318; }}
</style></head><body>
<h1>PMFBY claim packet draft: {packet['claim_id']}</h1>
<p>Farmer: {farmer.get('name', farmer.get('id', ''))} | Farm: {farmer.get('id', '')} |
District: {farmer.get('district', '')}</p>
<p>Incident: {incident.get('name', incident.get('id', ''))}</p>
<table>
<tr><th>Event time</th><td>{packet['event_time']}</td></tr>
<tr><th>Intimation deadline (72h)</th><td>{packet['intimation_deadline']}</td></tr>
<tr><th>Intimation on time</th>
<td><span class="gate {'ok' if packet['intimation_on_time'] else 'no'}">
{'ON TIME' if packet['intimation_on_time'] else 'LATE'}</span></td></tr>
<tr><th>Loss fraction</th><td>{packet['loss_fraction']}</td></tr>
<tr><th>Eligibility (threshold {packet['threshold']})</th>
<td><span class="gate {'ok' if packet['eligible'] else 'no'}">
{'ELIGIBLE' if packet['eligible'] else 'BELOW THRESHOLD'}</span></td></tr>
</table>
<h2>Evidence</h2>
<table><tr><th>Type</th><th>Timestamp</th><th>File</th></tr>{evidence_rows}</table>
<p>{packet['label']}</p>
</body></html>
"""


def export_svg_tag(packet: dict, evidence: dict, index: int) -> str:
    """One SVG damage-tag image per evidence item (pure stdlib string)."""
    cid = packet["claim_id"]
    etype = evidence.get("type", "evidence")
    ts = evidence.get("ts", "no timestamp")
    color = {"photo": "#1a7f37", "voice": "#4f46e5", "geo": "#b45309"}.get(etype, "#334155")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="360" height="200" viewBox="0 0 360 200">
  <rect width="360" height="200" fill="#f8fafc" stroke="#334155" stroke-width="2"/>
  <rect width="360" height="46" fill="{color}"/>
  <text x="14" y="30" fill="#ffffff" font-family="monospace" font-size="18" font-weight="bold">
    KrishiSetu damage tag</text>
  <text x="14" y="78" fill="#111" font-family="monospace" font-size="15">Claim: {cid}</text>
  <text x="14" y="104" fill="#111" font-family="monospace" font-size="15">Evidence #{index}: {etype}</text>
  <text x="14" y="130" fill="#111" font-family="monospace" font-size="15">Timestamp: {ts}</text>
  <text x="14" y="160" fill="#475569" font-family="monospace" font-size="12">SIMULATED packet draft</text>
</svg>
"""


def export_packet(packet: dict, out_dir) -> list[Path]:
    """Write the packet as text, printable HTML, and one SVG image per
    evidence item. Returns the list of written file paths."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    cid = packet["claim_id"]
    written = []

    txt = out_dir / f"claim_{cid}.txt"
    txt.write_text(export_text(packet))
    written.append(txt)

    html = out_dir / f"claim_{cid}.html"
    html.write_text(export_printable(packet))
    written.append(html)

    for i, ev in enumerate(packet.get("evidence", []), start=1):
        svg = out_dir / f"claim_{cid}_evidence_{i}.svg"
        svg.write_text(export_svg_tag(packet, ev, i))
        written.append(svg)

    return written
