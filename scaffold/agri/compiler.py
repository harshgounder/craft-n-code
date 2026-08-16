"""Advisory compiler: farm profile + incident state -> ranked action list.

Pure functions only; no I/O in this module. Rules are read from
rules.json by the loader (used by tests and scripts); the matcher and
ranker take the rule list as an argument so they stay pure and
testable.

Ranking = expected-loss comparator + doability infeasibility penalty:

    rank_score = expected_loss_reduction(rule, farm, incident) - penalty

Expected loss reduction uses the badged loss anchors from cvar.py
(stage fragility, Swarna-Sub1 Odisha RCT, salinity transfer prior).
An infeasible action carries INFEASIBLE_PENALTY so every feasible
action ranks above every infeasible one.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from doability import score as doability_score, INFEASIBLE_PENALTY
from cvar import (
    expected_crop_loss_fraction,
    exposed_crop_value,
    LIVESTOCK_VALUE_PER_HEAD_RS,
    VEGETABLE_VALUE_RS,
    LIVESTOCK_FLOOD_LOSS,
)

CYCLONE_CROP_LOSS_FRACTION = 0.35
"""SCENARIO-ASSUMPTION: cyclone wind loss fraction for an exposed standing
crop. Used only as a comparative rank driver, never as an Odisha claim."""

DEFAULT_RULES_PATH = Path(__file__).resolve().parent / "rules.json"

GRADE_ORDER = {"A": 0, "A governance rule": 0, "B": 1, "B/C": 1, "C": 2, "D": 3}
BADGES = {"ODISHA-MEASURED", "TRANSFER-PRIOR", "SCENARIO-ASSUMPTION", "UNKNOWN"}


def load_rules(path=None) -> list[dict]:
    """Load the R1-R16 registry JSON as a list of rule dicts (indexed)."""
    path = Path(path) if path else DEFAULT_RULES_PATH
    data = json.loads(path.read_text())
    rules = list(data["rules"])
    for i, rule in enumerate(rules):
        rule["index"] = i
    return rules


def _condition_ok(farm: dict, incident: dict, trigger: dict) -> bool:
    for key in trigger.get("farm_has", []):
        if not farm.get(key):
            return False
    for key, minimum in trigger.get("farm_min", {}).items():
        if float(farm.get(key, 0)) < float(minimum):
            return False
    for key in trigger.get("incident_has", []):
        if not incident.get(key):
            return False
    return True


def match_rule(farm: dict, incident: dict, rule: dict) -> bool:
    """True when the rule's hazard x crop x stage x lead trigger fires."""
    tr = rule.get("trigger", {})
    if rule.get("admin_only"):
        return False

    if incident.get("hazard") not in tr.get("hazard", []):
        return False

    crop = farm.get("crop")
    crops = tr.get("crop", [])
    if "any" not in crops and crop not in crops:
        return False

    stage = farm.get("stage")
    stages = tr.get("stage", [])
    if "any" not in stages and stage not in stages:
        return False

    lead = incident.get("lead_hours")
    lh = tr.get("lead_hours", {})
    if lh.get("any"):
        pass
    else:
        if lh.get("min") is not None and (lead is None or lead < lh["min"]):
            return False
        if lh.get("max") is not None and (lead is not None and lead > lh["max"]):
            return False

    return _condition_ok(farm, incident, tr)


def _asset_value(farm: dict, asset: str) -> float:
    if asset == "livestock":
        return float(farm.get("livestock_count", 0)) * LIVESTOCK_VALUE_PER_HEAD_RS
    if asset == "vegetable":
        return VEGETABLE_VALUE_RS if farm.get("vegetable_need") else 0.0
    return exposed_crop_value(farm)


def _asset_loss_fraction(farm: dict, incident: dict, asset: str) -> float:
    p = min(1.0, max(0.0, float(incident.get("flood_probability", 1.0))))
    if asset == "livestock":
        return LIVESTOCK_FLOOD_LOSS * p
    if incident.get("hazard") == "cyclone":
        return CYCLONE_CROP_LOSS_FRACTION
    return expected_crop_loss_fraction(farm, incident)


def expected_loss_reduction(farm: dict, incident: dict, rule: dict) -> float:
    """Rupee value of loss the rule averts: exposed value x expected loss
    fraction x the rule's protection share (SCENARIO-ASSUMPTION)."""
    value = _asset_value(farm, rule.get("asset", "crop"))
    loss_frac = _asset_loss_fraction(farm, incident, rule.get("asset", "crop"))
    protection = float(rule.get("protection", 0.0))
    return value * loss_frac * protection


def compute_deadline(incident: dict, rule: dict) -> dict:
    """Deadline derived from the rule's lead window and advisory time."""
    tr = rule.get("trigger", {}).get("lead_hours", {})
    if tr.get("any"):
        return {"note": "immediate relay" if rule.get("id") in ("R1", "R2", "R5", "R15") else "as scheduled"}
    lead = incident.get("lead_hours")
    max_h = tr.get("max") or lead
    base = incident.get("advisory_at")
    if base and max_h is not None:
        try:
            dt = datetime.fromisoformat(str(base))
            return {"by_iso": (dt + timedelta(hours=max_h)).isoformat(timespec="minutes"),
                    "note": f"within {max_h}h of the advisory"}
        except (ValueError, TypeError):
            pass
    return {"note": f"within {max_h}h of the advisory" if max_h is not None else "as scheduled"}


def build_action(farm: dict, incident: dict, rule: dict) -> dict:
    """Render one fired rule into a ranked action object."""
    tpl = rule.get("action_template", "")
    fmt = {
        "hazard": str(incident.get("hazard", "hazard")).replace("_", " "),
        "district": incident.get("district", "the district"),
        "issue_time": incident.get("issue_time", "as issued"),
        "validity": incident.get("validity", "as specified"),
        "alert_type": incident.get("alert_type", "official alert"),
        "crop": farm.get("crop", "crop"),
        "variety": farm.get("variety", "approved variety"),
        "stage": farm.get("stage", "current stage"),
        "farm_name": farm.get("name", farm.get("id", "farmer")),
    }
    try:
        action_text = tpl.format(**fmt)
    except (KeyError, IndexError):
        action_text = tpl

    feas = doability_score(farm, rule.get("resources", {}))
    reduction = expected_loss_reduction(farm, incident, rule)
    penalty = float(feas.get("penalty", INFEASIBLE_PENALTY if not feas.get("feasible") else 0.0))
    score_value = round(reduction - penalty, 2)

    return {
        "rule_id": rule["id"],
        "action": action_text,
        "deadline": compute_deadline(incident, rule),
        "grade": rule.get("grade"),
        "badge": rule.get("badge"),
        "guardrail": rule.get("guardrail"),
        "source": rule.get("source", {}).get("title", ""),
        "expected_loss_reduction_rs": round(reduction, 2),
        "doability": feas,
        "infeasibility_penalty": penalty,
        "rank_score": score_value,
        "simulated": True,
        "label": "SIMULATED advisory action - rule from registry, coefficients badged",
    }


def compile_actions(farm: dict, incident: dict, rules: list[dict],
                    include_admin: bool = False) -> list[dict]:
    """Match rules against the farm and incident, then rank the actions.

    Rank descending by rank_score (expected-loss reduction minus
    infeasibility penalty); ties resolved by registry order so results
    are stable and order-independent across rule dicts.
    """
    fired = []
    for rule in rules:
        if rule.get("admin_only") and not include_admin:
            continue
        if match_rule(farm, incident, rule):
            fired.append(build_action(farm, incident, rule))

    fired.sort(key=lambda a: (-a["rank_score"], a["rule_id"]))
    for i, a in enumerate(fired, start=1):
        a["rank"] = i
    return fired
