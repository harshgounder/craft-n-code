"""Small Monte Carlo replay for Cyclone Fani (Odisha, 2019).

Propagates hazard uncertainty (surge height, inundation extent, loss per
hectare) into a district crop-loss posterior and compares it against the
real OSDMA anchors:

    Fani: 108,220 ha crop area affected, Rs 1,304.58 cr crop loss,
          storm surge ~1.5 m at landfall.

Convergence follows pilot + main with a precision gate: run a pilot
sample; if the standard error of the posterior mean (as a fraction of
the mean) is below the gate, stop. Otherwise run the main sample and
report the final precision.

Every output is labeled SIMULATED; the anchors are the only Odisha-
measured quantities. Paddy GCA for the district is a SCENARIO-ASSUMPTION
that the affected-fraction prior is calibrated against.
"""
from __future__ import annotations

import random
from statistics import mean, pstdev, quantiles

FANI_ANCHOR_HA = 108220.0
FANI_ANCHOR_RS = 1304.58e7          # Rs 1,304.58 crore
FANI_SURGE_M = 1.5

PADDY_GCA_PURI_HA = 150000.0
"""SCENARIO-ASSUMPTION: district paddy gross cropped area used only to
convert an affected fraction into hectares; the fraction prior is
calibrated so the posterior mean lands on the OSDMA anchor."""

SURGE_SENSITIVITY = 0.20
"""SCENARIO-ASSUMPTION: fractional shift in affected area per meter of
surge above the 1.5 m anchor."""

BETA_SHAPE_A = 40.0
"""Beta shape for the affected-fraction prior; the B shape is derived so
the prior mean equals the calibrated fraction."""

LOSS_CV = 0.20
"""SCENARIO-ASSUMPTION: coefficient of variation of loss per affected
hectare, carried as a Gamma distribution."""

DEFAULT_PILOT_N = 300
DEFAULT_MAIN_N = 3000
DEFAULT_PRECISION_GATE = 0.02


def _anchor_fraction() -> float:
    return FANI_ANCHOR_HA / PADDY_GCA_PURI_HA


def sample_fani(rng: random.Random) -> dict:
    """One Monte Carlo draw of the Fani-like event."""
    surge = max(0.0, rng.gauss(FANI_SURGE_M, 0.2))
    frac_mean = _anchor_fraction() + (surge - FANI_SURGE_M) * SURGE_SENSITIVITY
    frac_mean = min(0.99, max(0.02, frac_mean))
    b = BETA_SHAPE_A * (1.0 - frac_mean) / max(frac_mean, 1e-9)
    frac = rng.betavariate(BETA_SHAPE_A, b)
    affected_ha = PADDY_GCA_PURI_HA * frac

    loss_mean = FANI_ANCHOR_RS / FANI_ANCHOR_HA
    shape = 1.0 / (LOSS_CV * LOSS_CV)
    scale = loss_mean * (LOSS_CV * LOSS_CV)
    loss_per_ha = rng.gammavariate(shape, scale)
    total_rs = affected_ha * loss_per_ha

    return {
        "surge_m": surge,
        "affected_ha": affected_ha,
        "loss_per_ha": loss_per_ha,
        "total_rs": total_rs,
    }


def _posterior(samples: list[dict]) -> dict:
    ha = [s["affected_ha"] for s in samples]
    rs = [s["total_rs"] for s in samples]
    surge = [s["surge_m"] for s in samples]

    def band(values):
        cuts = quantiles(values, n=40)   # 2.5th and 97.5th percentiles
        return {"mean": mean(values), "p2_5": cuts[0], "p97_5": cuts[-1]}

    return {"affected_ha": band(ha), "total_rs": band(rs), "surge_m": band(surge)}


def fani_posterior(pilot_n: int = DEFAULT_PILOT_N,
                   main_n: int = DEFAULT_MAIN_N,
                   precision_gate: float = DEFAULT_PRECISION_GATE,
                   seed: int = 20190503) -> dict:
    """Pilot + main Monte Carlo with a precision gate on the posterior mean."""
    rng = random.Random(seed)
    pilot = [sample_fani(rng) for _ in range(pilot_n)]

    def se_cv(values):
        n = max(len(values), 1)
        return (pstdev(values) / max(mean(values), 1e-9)) / (n ** 0.5)

    cv = se_cv([s["affected_ha"] for s in pilot])
    stage, converged, samples = "pilot", False, pilot

    if cv <= precision_gate:
        converged = True
    else:
        main = [sample_fani(rng) for _ in range(main_n)]
        samples = pilot + main
        stage = "main"
        cv = se_cv([s["affected_ha"] for s in samples])
        converged = cv <= precision_gate

    posterior = _posterior(samples)
    anchor_ha_in_band = (FANI_ANCHOR_HA >= posterior["affected_ha"]["p2_5"]
                         and FANI_ANCHOR_HA <= posterior["affected_ha"]["p97_5"])
    explanation = ("OSDMA anchor 108,220 ha lies inside the 95% posterior band."
                   if anchor_ha_in_band else
                   "Anchor outside band: prior was not calibrated to the anchor; "
                   "the band is the honest uncertainty of this SIMULATED replay.")

    return {
        "event": "Fani (2019)",
        "stage": stage,
        "pilot_n": pilot_n,
        "main_n": main_n if stage == "main" else 0,
        "total_samples": len(samples),
        "precision_gate": precision_gate,
        "se_cv": cv,
        "converged": converged,
        "posterior": posterior,
        "anchor": {
            "affected_ha": FANI_ANCHOR_HA,
            "loss_rs_cr": 1304.58,
            "surge_m": FANI_SURGE_M,
        },
        "anchor_ha_in_band": anchor_ha_in_band,
        "explanation": explanation,
        "simulated": True,
        "label": "SIMULATED replay - hazard uncertainty propagated, anchors from OSDMA reports",
    }


def main() -> None:
    res = fani_posterior()
    band = res["posterior"]["affected_ha"]
    print(f"[replay] {res['event']} stage={res['stage']} n={res['total_samples']} "
          f"se_cv={res['se_cv']:.5f} converged={res['converged']}")
    print(f"[replay] affected_ha band p2.5={band['p2_5']:.0f} mean={band['mean']:.0f} "
          f"p97.5={band['p97_5']:.0f} (anchor {FANI_ANCHOR_HA:.0f}) in_band={res['anchor_ha_in_band']}")
    print(f"[replay] {res['label']}")


if __name__ == "__main__":
    main()
