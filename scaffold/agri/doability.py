"""Doability layer (d37, d39): feasibility scoring per action.

The thesis of KrishiSetu is that an advisory without a feasibility check
is noise (d39). Every action carries labor hours, cost, credit context,
and a tenancy flag. `score` returns a plain dict so it composes with the
pure compiler and CVaR modules.

Resource figures (labor_hours, cost_rs, credit_needed) are scenario
assumptions pending Odisha field trials; the registry labels them with
SCENARIO-ASSUMPTION (d41 section 4: operational thresholds missing).
"""
from __future__ import annotations

INFEASIBLE_PENALTY = 1_000_000_000.0
"""Arbitrary large penalty so any infeasible action ranks below every
feasible one in the compiler. This is an ordering constant, not a claim
about Odisha economics."""


def score(farm: dict, requires: dict) -> dict:
    """Return the feasibility record for one action on one farm.

    `requires` mirrors the rule registry resources block:
      labor_hours, cost_rs, credit_needed, tenancy_required (bool).
    `farm` must carry available_labor_hours, cash_rs, credit_limit_rs,
    owns_land and/or tenancy_permitted.

    Result keys:
      labor_hours, cost_rs, credit_needed, tenancy_ok, feasible,
      infeasible_reason, penalty
    """
    labor_hours = max(0.0, float(requires.get("labor_hours", 0)))
    cost_rs = max(0.0, float(requires.get("cost_rs", 0)))
    credit_needed = bool(requires.get("credit_needed", False))
    tenancy_required = bool(requires.get("tenancy_required", False))

    avail_labor = max(0.0, float(farm.get("available_labor_hours", 0)))
    cash = max(0.0, float(farm.get("cash_rs", 0)))
    credit_limit = max(0.0, float(farm.get("credit_limit_rs", 0)))
    owns_land = bool(farm.get("owns_land", False))
    tenancy_permitted = bool(farm.get("tenancy_permitted", False))
    tenancy_ok = (not tenancy_required) or owns_land or tenancy_permitted

    reasons = []
    shortfall = 0.0

    labor_ok = avail_labor >= labor_hours
    if not labor_ok:
        reasons.append(f"needs {labor_hours:.0f} labor hours, has {avail_labor:.0f}")
        shortfall += (labor_hours - avail_labor) / max(labor_hours, 1.0)

    affordable = (cash + credit_limit) >= cost_rs
    if not affordable:
        reasons.append(
            f"needs Rs {cost_rs:.0f}, has Rs {cash:.0f} cash plus "
            f"Rs {credit_limit:.0f} credit")
        shortfall += max(0.0, cost_rs - cash - credit_limit) / max(cost_rs, 1.0)

    if not tenancy_ok:
        reasons.append("requires owned or long-term permitted land (tenancy)")
        shortfall += 1.0

    if credit_needed and credit_limit <= 0:
        reasons.append("action assumes credit access but farm credit limit is zero")
        shortfall += 1.0

    feasible = not reasons
    penalty = 0.0 if feasible else INFEASIBLE_PENALTY + shortfall

    return {
        "labor_hours": labor_hours,
        "cost_rs": cost_rs,
        "credit_needed": credit_needed,
        "tenancy_ok": tenancy_ok,
        "feasible": feasible,
        "infeasible_reason": "; ".join(reasons) if reasons else None,
        "penalty": penalty,
    }


def infeasibility_penalty(feas_record: dict) -> float:
    """Extract the penalty term used by the compiler and CVaR objectives."""
    return float(feas_record.get("penalty", INFEASIBLE_PENALTY if not feas_record.get("feasible", True) else 0.0))
