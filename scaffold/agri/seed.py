"""Seed data: Asha + high-field farm profiles, Fani/Yaas incident
archives, and sample advisories.

Profiles carry the consented farm-profile fields (THE-PLAN Part 5).
Incident archives carry only the real OSDMA/IMD anchors and are labeled
SIMULATED where anything is reconstructed. Every farm-facing advisory in
the seed carries a SIMULATED label.
"""
from __future__ import annotations


def asha_farm() -> dict:
    """Asha Behera: the low-lying tenant profile (Puri)."""
    return {
        "id": "asha-001",
        "name": "Asha Behera",
        "district": "Puri",
        "elevation_m": 2.5,
        "soil_salinity_ds_m": 2.2,
        "waterlogging_history": "frequent",
        "drainage_ok": False,
        "crop": "paddy",
        "variety": "Swarna",
        "stage": "tillering",
        "area_ha": 0.95,
        "expected_yield_kg_ha": 3500,
        "price_rs_kg": 19.0,
        "owns_land": False,
        "tenancy_permitted": True,
        "available_labor_hours": 12,
        "cash_rs": 2000,
        "credit_limit_rs": 10000,
        "livestock_count": 2,
        "vegetable_need": True,
        "stores_seed": True,
        "has_pond": False,
        "suitable_soil": False,
        "drainage_outlet": False,
        "field_accessible": True,
        "harvest_labor_hours_per_ha": 12,
        "wage_rs_per_hour": 100,
    }


def high_field_farm() -> dict:
    """Pramod Das: the elevated, owned-land contrast profile."""
    return {
        "id": "highfield-002",
        "name": "Pramod Das",
        "district": "Jagatsinghpur",
        "elevation_m": 8.0,
        "soil_salinity_ds_m": 1.2,
        "waterlogging_history": "rare",
        "drainage_ok": True,
        "crop": "paddy",
        "variety": "Swarna-Sub1",
        "stage": "harvest_window",
        "area_ha": 2.5,
        "expected_yield_kg_ha": 4000,
        "price_rs_kg": 19.0,
        "owns_land": True,
        "tenancy_permitted": True,
        "available_labor_hours": 120,
        "cash_rs": 25000,
        "credit_limit_rs": 50000,
        "livestock_count": 0,
        "vegetable_need": False,
        "stores_seed": True,
        "has_pond": True,
        "suitable_soil": True,
        "drainage_outlet": True,
        "field_accessible": True,
        "harvest_labor_hours_per_ha": 12,
        "wage_rs_per_hour": 100,
    }


def flood_warning_incident() -> dict:
    """A SIMULATED flood advisory used for the two-farm contrast."""
    return {
        "id": "demo-2026",
        "hazard": "flood",
        "severity": "warning",
        "alert_type": "flood warning",
        "lead_hours": 24,
        "district": "Puri",
        "issue_time": "2026-08-16 09:00",
        "validity": "2026-08-17 09:00",
        "official_alert": True,
        "severe_alert": True,
        "flood_risk": True,
        "water_may_reach_storage": True,
        "freshwater_waterlogging": True,
        "water_falling": True,
        "field_accessible": True,
        "drainage_connectable": True,
        "route_cutoff_approaching": True,
        "shelter_confirmed": True,
        "flood_probability": 0.7,
        "deep_flood_share": 0.4,
        "inundation_days_mean": 3,
        "label": "SIMULATED advisory scenario",
    }


def fani_archive() -> dict:
    """Cyclone Fani (2019) calibration archive."""
    return {
        "id": "fani-2019",
        "name": "Cyclone Fani",
        "year": 2019,
        "landfall": {"date": "2019-05-03", "district": "Puri"},
        "surge_m": 1.5,
        "surge_badge": "ODISHA-MEASURED",
        "affected_ha": 108220.0,
        "loss_rs_cr": 1304.58,
        "loss_badge": "ODISHA-MEASURED",
        "label": "SIMULATED replay archive - anchors from OSDMA reports",
    }


def yaas_archive() -> dict:
    """Cyclone Yaas (2021) calibration archive."""
    return {
        "id": "yaas-2021",
        "name": "Cyclone Yaas",
        "year": 2021,
        "landfall": {"date": "2021-05-26", "district": "Balasore/Bhadrak"},
        "surge_m_range": [2.0, 4.0],
        "surge_note": "2-4 m surge over full-moon tide (ODISHA-MEASURED)",
        "rain_chandbali_cm": 29.0,
        "rain_note": "29 cm rain at Chandbali (ODISHA-MEASURED)",
        "label": "SIMULATED replay archive",
    }


def sample_advisories() -> list[dict]:
    """Sample farmer-facing advisories, every one labeled SIMULATED."""
    return [
        {"id": "adv-1", "rule": "R1", "farmer": "asha-001",
         "text": "Official flood warning for Puri: relay the IMD wording verbatim. "
                 "Notify the village relay and the extension desk. SIMULATED advisory."},
        {"id": "adv-2", "rule": "R3", "farmer": "asha-001",
         "text": "Asha: dry and label your seed, seal an inner container, move it above "
                 "the predicted water, duplicate a lot at a second safe site. SIMULATED advisory."},
        {"id": "adv-3", "rule": "R4", "farmer": "asha-001",
         "text": "Asha: identify animals and owners, move early by species order, carry "
                 "fodder and medicines, confirm head count at the shelter. SIMULATED advisory."},
    ]
