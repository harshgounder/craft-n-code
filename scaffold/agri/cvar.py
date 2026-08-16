"""Sample-based 95% CVaR and the harvest decision.

The harvest decision answers: wait, partial, or immediate harvest when a
flood or cyclone warning arrives and the crop is near harvest. Objective:

    a* = argmin_a  CVaR_95(total loss | a) + cost(a) + infeasibility(a)

Every coefficient wears a badge. Calibration anchors (all SIMULATED
unless marked ODISHA-MEASURED):

  Swarna-Sub1 RCT (Odisha, J-PAL): +64 kg/ha per flood day,
    ~718 kg/ha under severe submergence, 180 kg/ha neutral when no flood.
  Early harvest: 5.76% cost (32-study meta, TRANSFER-PRIOR).
  Tillering rice: no loss below 4 days inundation, 80% at 6 days.
  Waterlogging repro loss: 32.9% global prior (TRANSFER-PRIOR).
  Salinity: 1.9 dS/m threshold plus 9.1% per dS/m (TRANSFER-PRIOR).

The scenario sampler is stratified so that exactly p x n samples carry a
flood. That removes binomial sampling noise and makes the decision
reproducible under a fixed seed.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass, asdict
from typing import Optional

# ---------------------------------------------------------------------
# Evidence anchors with badges. Every number a product says must wear one
# of the four badges (ODISHA-MEASURED / TRANSFER-PRIOR / SCENARIO-ASSUMPTION / UNKNOWN).
# ---------------------------------------------------------------------
EARLY_HARVEST_COST = 0.0576
"""5.76% early-harvest yield cost, 32-study meta-analysis. TRANSFER-PRIOR."""

WATERLOGGING_PRIOR = 0.329
"""32.9% global waterlogging yield-loss prior. TRANSFER-PRIOR, never presented as Odisha truth."""

TILLERING_DAYS_NO_LOSS = 4
"""Tillering rice shows no loss below 4 days of inundation."""

TILLERING_DAYS_TOTAL_LOSS = 6
"""Tillering rice reaches ~80% loss at 6 days of inundation."""

TILLERING_LOSS_AT_TOTAL = 0.80
"""80% loss anchor at 6 days (TRANSFER-PRIOR)."""

SUB1_PER_FLOOD_DAY_KG_HA = 64.0
"""Swarna-Sub1 gains ~64 kg/ha per flood day over the non-tolerant check. ODISHA-MEASURED."""

SUB1_SEVERE_SUBMERGENCE_KG_HA = 718.0
"""Swarna-Sub1 advantage under severe submergence. ODISHA-MEASURED."""

SUB1_NO_FLOOD_KG_HA = 180.0
"""Swarna-Sub1 neutral-to-positive yield when no flood. ODISHA-MEASURED."""

SALINITY_THRESHOLD_DS_M = 1.9
"""Yield loss starts above 1.9 dS/m. TRANSFER-PRIOR."""

SALINITY_LOSS_PER_DS_M = 0.091
"""9.1% yield loss per dS/m above threshold. TRANSFER-PRIOR."""

MATURITY_DEEP_FLOOD_LOSS = 0.90
"""SCENARIO-ASSUMPTION: mature grain submerged by deep flood spoils at ~90%.
Not an Odisha measurement; used only for the wait-vs-harvest comparator."""

LIVESTOCK_FLOOD_LOSS = 0.20
"""SCENARIO-ASSUMPTION: livestock loss fraction under flood if not moved."""

LIVESTOCK_VALUE_PER_HEAD_RS = 8000.0
"""SCENARIO-ASSUMPTION: replacement value per head for the loss comparator."""

VEGETABLE_VALUE_RS = 3000.0
"""SCENARIO-ASSUMPTION: household vegetable plot value for the loss comparator."""

EVIDENCE = {
    "early_harvest_cost": {"value": EARLY_HARVEST_COST, "unit": "fraction of yield",
                           "badge": "TRANSFER-PRIOR",
                           "note": "5.76% cost, 32-study meta"},
    "waterlogging_prior": {"value": WATERLOGGING_PRIOR, "unit": "fraction",
                           "badge": "TRANSFER-PRIOR",
                           "note": "32.9% global prior, not Odisha truth"},
    "tillering_loss": {"value": [{"days": 4, "loss": 0.0}, {"days": 6, "loss": 0.80}],
                       "unit": "loss fraction by inundation days",
                       "badge": "TRANSFER-PRIOR",
                       "note": "no loss <4 days, 80% at 6 days"},
    "swarna_sub1": {"value": {"per_flood_day_kg_ha": SUB1_PER_FLOOD_DAY_KG_HA,
                              "severe_submergence_kg_ha": SUB1_SEVERE_SUBMERGENCE_KG_HA,
                              "no_flood_kg_ha": SUB1_NO_FLOOD_KG_HA},
                    "unit": "kg/ha", "badge": "ODISHA-MEASURED",
                    "note": "J-PAL Swarna-Sub1 RCT in Odisha"},
    "salinity": {"value": {"threshold_ds_m": SALINITY_THRESHOLD_DS_M,
                           "loss_per_ds_m": SALINITY_LOSS_PER_DS_M},
                 "unit": "dS/m", "badge": "TRANSFER-PRIOR",
                 "note": "1.9 dS/m + 9.1% per dS/m"},
    "maturity_deep_flood": {"value": MATURITY_DEEP_FLOOD_LOSS, "unit": "fraction",
                            "badge": "SCENARIO-ASSUMPTION",
                            "note": "not an Odisha measurement"},
}


def cvar_95(samples) -> float:
    """Mean of the worst 5% of loss samples. Raises on an empty list."""
    if not samples:
        raise ValueError("cvar_95 requires at least one sample")
    k = max(1, int(math.ceil(len(samples) * 0.05)))
    tail = sorted(samples)[-k:]
    return sum(tail) / len(tail)


def flood_loss_fraction(farm: dict, days: int, severity: str) -> float:
    """Stage- and variety-aware flood loss fraction, 0..1.

    tillering: documented curve (0% <= 4 days, 80% at 6+ days).
    Swarna-Sub1: Odisha RCT advantage removes up to 718 kg/ha of loss.
    other stages: 32.9% waterlogging prior; deep flood on a mature,
    non-tolerant crop uses the labeled maturity scenario assumption.
    """
    days = max(0, int(days))
    if severity == "none":
        return 0.0

    stage = farm.get("stage", "vegetative")
    if stage == "tillering":
        if days <= TILLERING_DAYS_NO_LOSS:
            return 0.0
        if days >= TILLERING_DAYS_TOTAL_LOSS:
            return TILLERING_LOSS_AT_TOTAL
        t = (days - TILLERING_DAYS_NO_LOSS) / (TILLERING_DAYS_TOTAL_LOSS - TILLERING_DAYS_NO_LOSS)
        return t * TILLERING_LOSS_AT_TOTAL

    if farm.get("variety") == "Swarna-Sub1":
        kg_loss = min(SUB1_PER_FLOOD_DAY_KG_HA * days, SUB1_SEVERE_SUBMERGENCE_KG_HA)
        yield_kg = max(float(farm.get("expected_yield_kg_ha", 3500)), 1.0)
        return min(1.0, kg_loss / yield_kg)

    if severity == "deep":
        return MATURITY_DEEP_FLOOD_LOSS
    return WATERLOGGING_PRIOR


def expected_crop_loss_fraction(farm: dict, incident: dict) -> float:
    """Probability-weighted expected crop loss fraction used as the
    compiler's expected-loss comparator. Adds the transfer-prior salinity
    term when the farm soil exceeds 1.9 dS/m."""
    p = min(1.0, max(0.0, float(incident.get("flood_probability", 1.0))))
    deep_share = min(1.0, max(0.0, float(incident.get("deep_flood_share", 0.4))))
    shallow_days = max(1, int(incident.get("inundation_days_mean", 3)))
    deep_days = max(6, shallow_days + 3)
    loss_shallow = flood_loss_fraction(farm, shallow_days, "shallow")
    loss_deep = flood_loss_fraction(farm, deep_days, "deep")
    frac = p * (deep_share * loss_deep + (1.0 - deep_share) * loss_shallow)

    dsm = float(farm.get("soil_salinity_ds_m", 0.0))
    if dsm > SALINITY_THRESHOLD_DS_M:
        frac = min(1.0, frac + SALINITY_LOSS_PER_DS_M * (dsm - SALINITY_THRESHOLD_DS_M))
    return frac


@dataclass
class HarvestOption:
    """One candidate action in the harvest decision, with its CVaR objective."""
    action: str
    cvar_rs: float
    cost_rs: float
    feasible: bool
    infeasible_reason: Optional[str]
    objective: float
    n: int

    def as_dict(self):
        return asdict(self)


def sample_flood_scenarios(n: int, incident: dict, rng: random.Random):
    """Stratified flood scenario draw: exactly round(p x n) floods.

    Returns a list of (severity, days) tuples, shuffled for realism but
    with a fixed composition so CVaR is reproducible under a fixed seed.
    """
    p = min(1.0, max(0.0, float(incident.get("flood_probability", 1.0))))
    deep_share = min(1.0, max(0.0, float(incident.get("deep_flood_share", 0.4))))
    mean_days = max(1, int(incident.get("inundation_days_mean", 3)))
    n_flood = int(round(p * n))

    scenarios = []
    for i in range(n):
        if i < n_flood:
            if rng.random() < deep_share:
                days = max(6, int(rng.uniform(mean_days, mean_days + 4)))
                scenarios.append(("deep", days))
            else:
                days = max(1, min(4, int(rng.uniform(1, mean_days + 1))))
                scenarios.append(("shallow", days))
        else:
            scenarios.append(("none", 0))
    rng.shuffle(scenarios)
    return scenarios


HARVEST_READY_STAGES = {"grain_fill", "harvest_window", "maturity"}


def action_cost(farm: dict, action: str, partial_fraction: float = 0.5) -> tuple:
    """(cost_rs, feasible, infeasible_reason) for a harvest action.

    Labor requirement is a SCENARIO-ASSUMPTION: harvest_labor_hours_per_ha
    (default 12) at wage_rs_per_hour (default 100). Immediate harvest
    needs the full labor; partial harvest needs the fraction. Harvest
    actions are infeasible until the crop is harvest-ready, so the module
    never recommends cutting green paddy.
    """
    if action != "wait" and farm.get("stage") not in HARVEST_READY_STAGES:
        return 0.0, False, "crop not harvest-ready (harvesting green paddy is destructive)"

    area = float(farm.get("area_ha", 0))
    labor_per_ha = float(farm.get("harvest_labor_hours_per_ha", 12.0))
    wage = float(farm.get("wage_rs_per_hour", 100.0))
    avail_labor = float(farm.get("available_labor_hours", 0))
    cash = float(farm.get("cash_rs", 0))
    credit = float(farm.get("credit_limit_rs", 0))

    if action == "wait":
        return 0.0, True, None

    fraction = partial_fraction if action == "partial" else 1.0
    labor = fraction * labor_per_ha * area
    cost = labor * wage

    reasons = []
    if avail_labor < labor:
        reasons.append(f"needs {labor:.0f} labor hours, has {avail_labor:.0f}")
    if cash + credit < cost:
        reasons.append(f"needs Rs {cost:.0f}, has Rs {cash:.0f} cash")
    return cost, (not reasons), "; ".join(reasons) if reasons else None


def harvest_decision(farm: dict, incident: dict, n: int = 2000,
                     seed: Optional[int] = None, partial_fraction: float = 0.5) -> dict:
    """Wait vs partial vs immediate under flood risk.

    a* = argmin_a CVaR_95(total loss | a) + cost(a) + infeasibility(a)
    """
    rng = random.Random(seed)
    exposed = exposed_crop_value(farm)
    options = {}

    for action in ("wait", "partial", "immediate"):
        scenarios = sample_flood_scenarios(n, incident, rng)
        losses = []
        for severity, days in scenarios:
            loss_frac = flood_loss_fraction(farm, days, severity)
            if action == "wait":
                loss = exposed * loss_frac
            elif action == "immediate":
                loss = exposed * EARLY_HARVEST_COST
            else:
                loss = (partial_fraction * exposed * EARLY_HARVEST_COST
                        + (1.0 - partial_fraction) * exposed * loss_frac)
            losses.append(loss)
        c = cvar_95(losses)
        cost, feasible, reason = action_cost(farm, action, partial_fraction)
        penalty = 0.0 if feasible else 1_000_000_000.0
        options[action] = HarvestOption(
            action=action, cvar_rs=round(c, 2), cost_rs=round(cost, 2),
            feasible=feasible, infeasible_reason=reason,
            objective=round(c + cost + penalty, 2), n=n)

    best = min(options, key=lambda a: options[a].objective)
    return {
        "best": best,
        "exposed_crop_value_rs": round(exposed, 2),
        "options": {a: options[a].as_dict() for a in options},
        "partial_fraction": partial_fraction,
        "simulated": True,
        "label": "SIMULATED harvest decision - sample-based CVaR, coefficients badged in EVIDENCE",
        "evidence": EVIDENCE,
    }


def exposed_crop_value(farm: dict) -> float:
    """Exposed value of the standing crop in rupees: area x yield x price."""
    area = float(farm.get("area_ha", 0))
    yield_kg = float(farm.get("expected_yield_kg_ha", 3500))
    price = float(farm.get("price_rs_kg", 19.0))
    return area * yield_kg * price
