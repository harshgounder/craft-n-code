# PRODUCT-CORE.md — KrishiSetu, Corrected Emphasis

Date: 2026-08-16. Supersedes the earlier framing where hazard detection led.
The statement is an AGRICULTURE ADVISORY SYSTEM. The crop and soil
advisory is the product. Cyclone/flood sensing is the BACKUP for when
the official message does not arrive.

## 1. THE HIERARCHY (what is the product vs what is backup)

1. CORE: crop + soil + stage data in, staged agronomic action out.
   Pre-disaster: harvest, drain, shelter livestock, secure seed.
   Post-disaster: saline flush, re-sowing, pest scouting, claims.
2. INTEGRATES IMD alerts: the official warning is the primary trigger.
   We ingest it when it is reachable. No API key needed: public CAP RSS.
3. BACKUP: local sensors + algorithms detect regime change so the same
   advisory engine fires when the official message never reaches the
   farm (tower down, bulletin missed, paper loop broken).
4. FEATURE, not dependency: the phone. The product works on a basic
   phone via SMS/IVR. An "okish" Android phone makes it richer, never
   required. The on-device LLM is optional rendering, not the brain.

## 2. SELF-DEPENDENCE RULES (from the user)

- Zero API keys required to run. Public CAP RSS is a bonus feed, cached.
- Zero internet required after first sync. All rules, profiles, and
  advisories live locally.
- Zero cloud required. The engine runs on a laptop, a Raspberry Pi,
  or a phone. Server training is a growth feature, not a dependency.
- Feature phones first: SMS + IVR are the primary delivery rails.
- The LLM is a feature: when absent, fixed Odia templates ship the
  same advisory.

## 3. THE CORE LOOP

FARM PROFILE (crop, stage, soil class, elevation, phone type, language)
+ LOCAL DATA (soil moisture, rain, water level, pressure when present)
+ OFFICIAL ALERT (CAP RSS when reachable, else absent)
-> AGRI ADVISORY ENGINE (deterministic, evidence-tuned, audited)
-> ACTION with deadline, source, cost of waiting
-> DELIVER via SMS/IVR (feature phone) or app (okish phone)
-> RECOVERY + CLAIM PACKET (33% threshold, SDRF/PMFBY norms)
-> OUTCOME LOG (local, uploaded when possible)

The advisory engine never needs the hazard predictor. The hazard
predictor exists only to trigger the advisory engine when the official
message is missed.

## 4. WHAT CHANGED FROM THE PREVIOUS FRAMING

| Layer | Before (wrong) | After (correct) |
|---|---|---|
| Hero | Cyclone detection + edge AI | Crop/soil advisory engine |
| Sensors | Prove detection | Local confirmation + backup trigger |
| LLM on phone | Core architecture | Optional rendering feature |
| IMD | One input among many | The primary trigger, ingested free |
| Algorithm story | Buried | Front and center (see ALGORITHM-STACK.md) |
| API keys | Assumed | Zero required |
