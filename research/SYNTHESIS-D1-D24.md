# SYNTHESIS-D1-D24.md — The KrishiSetu Data Wave, Analyzed

Date: 2026-08-16, all 24 ultra8x runs + d3 refire landed and read.
Every claim below carries the report's own grade. Verdict pattern across all 24:
PROTOTYPE GO, PILOT GATED, overall PARTIAL. That is the honest floor.

## 1. THE PRODUCT IS REAL, WITH PHYSICS

Your edge-AI vision survives contact with evidence, corrected in 3 places:

1. The phone runs a 1B Q4 model, not 3B. Llama 3.2 1B Q4 = 0.81 GB file,
   ~1.9-2.3 GB RSS measured on a flagship. 3B measured 3.7-4.1 GB RSS. A
   Lava Blaze 3 5G (Rs 10,999, 6 GB) is the target device. Qwen3 0.6B is
   the Odia candidate (Oriya in its 119-language list), Llama 3.2 1B is the
   Hindi/control model. llama.cpp first, ExecuTorch second, MediaPipe out.
   [d10]

2. "Fine-tunes all the time" = server-side LoRA, pushed as signed adapters.
   On-phone continuous LLM training is research-stage (MobiLLM needed an
   A100 server). The honest loop: phones log feedback -> server trains
   QLoRA when evidence gates pass -> 11-49 MB signed adapter -> canary ->
   A/B slots -> rollback. 12 GB GPU for 1B, 24 GB for 3-4B. 500-1,000
   reviewed cases is the seed range (LIMA), 5% selected data beats full
   (LESS), synthetic data only behind a real anchor (model collapse is
   published). [d11]

3. The LLM is the accessibility layer, NOT the predictive core. The core
   is: official IMD/CWC alert state + sensor trend + farm vulnerability +
   crop stage + a calibrated, audited rules table. The LLM converts the
   selected action into Odia SMS/IVR. If the model fails, the fixed warning
   still ships. "Village nodes detect a cyclone before satellite" is
   contradicted by the evidence: IMD gave Fani 90h watch / 66h alert / 36h
   warning. Sensors confirm locally; officials lead. [d10][d13]

## 2. THE DATA FOUNDATION (d1-d9)

- Cyclone science: IMD scale is machine-codable (17 kt depression -> 90 kt
  extremely severe). Two BoB seasons: May-June pre-monsoon, Oct-Nov peak.
  Detection is layered: INSAT-3DR, Oceansat-3, ASCAT, Paradip/Gopalpur DWRs.
  Formal lead times: watch 72h, alert 48h, warning 24h. Track errors 66/84/
  116 km at 24/48/72h. 1999: 48h+ warning, 9,893 deaths: warnings alone do
  nothing. Phailin proved evacuation works. [d1]
- Floods: CWC 325 stations, yellow/orange/red semantics (orange 3h, red 1h
  cadence), 19 flood-forecast sites in Odisha (12 level + 7 inflow), hourly
  levels on NWDP. The flood chain is compound: upstream rain + reservoir +
  surge + tide. Recession clock, not static duration. [d2][d7]
- Cascades: Dana surge 1-2 m. Yaas: flooded != salinized, 5,882 ha seawater
  one month on. Waterlogging yield loss meta: 32.9% mean, 41.9% at
  reproductive stage vs 34.75% vegetative. Blast disease needs 92-96% RH
  + 25-28 C, lesions in 3-5 days: scouting prompts, not outbreak forecasts.
  PMFBY covers flood/inundation/lightning/storm/cyclone, 72h loss
  intimation, max 2-week post-harvest window. Positive use is real when
  engineered: Phulbani farm-pond experiment, Koraput case. Groundwater
  recharge 17.46 BCM is a baseline, not an event meter. [d3-refire][d6]
- Crops: paddy is 44% of gross cropped area (41.24 lakh ha, 2024-25);
  Bargarh/Mayurbhanj/Kalahandi top. District calendars differ by region.
  Swarna-Sub1 (145d, 5.2 t/ha, 45% yield advantage after 10d submergence in
  a 128-village RCT) is the flood-tolerant anchor. Salinity threshold 1.9
  dS/m with 9.1% yield-decline slope. No joint crop fragility curve exists
  publicly; the Myanmar model (1 m, 8 days: 50% vegetative / 40%
  reproductive) is a provisional prior only. [d4][d9]
- Land: SRTM/AW3D30/CartoDEM are 30-32 m, NOT parcel-level. Bhuvan LULC
  1:50k/1:250k + SIS-DP 1:10k. BHOOMI soils + Soil Health Cards (12 params,
  nominal 2.5/10 ha). SAC's Yaas maps are inundation, not salinity. [d5]
- Farmers: 4.866M holdings, 0.95 ha average, 3.637M marginal, 5.82%
  tenancy (India's highest), 40.5% rural households indebted (avg Rs
  31,000). Fani: 90% of affected farmers small/marginal. Phones: 84% of
  rural households have a mobile, 53% smartphone-only. [d6]
- Prior art: GKMS Tue/Fri cadence (the gap is real), KCC 22 languages
  06:00-22:00 with expert escalation, mKisan cumulative 1,044 cr SMSs, Ama
  Krushi = the closest Odisha voice precedent, Odisha Crop Contingency Plan
  2025 + ICAR-CRIDA district plans = the rules seed. [d8][d15]
- Math: Holland 1980 wind field is the hazard spine, but the "Kalsi 2006 B
  fit" is NOT verifiable (flagged). Bates & De Roo diffusion-wave is the
  flood method. SDRF/NDRF norms: 33% crop-loss threshold, Rs 8,500/ha
  rainfed, Rs 17,000/ha irrigated. R = Sy x dh/dt for recharge. [d9]

## 3. THE EDGE-AI STACK (d10-d14)

- Sensor node at Rs 2,899 total: ESP32 (Rs 232-385), BMP280 pressure (Rs
  85, +/-0.12 hPa relative), DHT22 (Rs 120), capacitive soil moisture (Rs
  49), waterproof ultrasonic water level (Rs 249), DIY anemometer (Rs 300),
  DIY tipping bucket, solar. UV omitted: no decision value for storms.
  Pressure tendency is the strongest cheap signal, but NO universal hPa/hour
  trigger exists: Phailin's 66 hPa is a total fall, not a rate. BOCPD runs
  pruned on the phone for regime change; it detects change, not cyclones.
  [d12][d13]
- No verified full loop exists anywhere: sensors -> offline phone LLM ->
  Odia SMS/IVR -> outcome -> daily update. That is the white space. Closest:
  PlantVillage Nuru (offline Android diagnosis, 2 GB RAM), OSDMA EWDS (122
  siren towers, 6 coastal districts, GPRS/VHF + satellite fallback + solar),
  Ama Krushi (voice at scale). [d14][d20]

## 4. PRODUCT REALITY (d15-d20)

- Odia voice: Ama Krushi proves the channel (50K calls/month, 30 districts,
  155333 line). IndicTrans2 200M covers translation. NO Google/Azure Odia
  TTS exists; IndicF5 0.4B MIT is the open path. ASR: IndicVoices WER 23.4,
  dialect splits unpublished. Tokenizer trap: SentencePiece F1 81 vs BPE 0.
  IVR pattern: CGNet-style missed-call callback, one decision per prompt,
  DTMF confirm, KCC escalation. SMS is a receipt, not proof of
  understanding: Haryana 70% could read SMS, 25% had smartphones, no yield
  effect; Andhra RCT: learning but no production effect. Impact claims are
  GATED on comprehension testing. [d15]
- Feeds: IMD CAP RSS is the free machine-readable trigger. IMD API
  registration is GOV/NIC-gated: the prototype uses CAP + RSMC bulletins,
  the pilot needs a government partner. CWC India-WRIS API works (1,000
  record ceiling). INCOIS products are public but no hazard API contract
  exists. Bhuvan WMS + 32 m CartoDEM free. Open-Meteo free fallback (never
  to downgrade an official warning). Six-tier source hierarchy. [d16]
- Infrastructure: Fani took out power + telecom in 4 districts, 9 days to
  restore; Dana took out Rajnagar + Chandabali blocks entirely. Average 23.4
  h/day rural supply hides the tail. 86.9% rural households have a phone,
  30.9% have internet: offline-first is not a feature, it is the product.
  Solar: 5.5 kWh/m2/day, ~300 clear days. [d17]
- Who pays: 81.3% WTP for a small co-pay in a 30-district Odisha study.
  Voice + 3 reminders: 38% adoption vs 18% face-to-face. Lead payer = ATMA
  (60:40 Centre-State) or FPOs (Rs 18L support + Rs 15L matching) or PMFBY's
  0.5% premium earmark for awareness. Bajaj Allianz Farmitra ran free
  advisory for non-customers: precedent exists. [d18]
- Training data: IMD daily 0.25-degree rainfall 1901-2024 (NetCDF, free),
  temp 1x1, GodL license. Best Tracks 1982-2026 XLSX (the "1961-present"
  claim is wrong). CWC hydrology free. Odisha Ag Stats PDFs. e-Chasa crop
  survey, Soil Health Cards, J-PAL flood-tolerant rice evaluation. [d19]
- Ecosystem: OSDMA = the integration partner (post-1999 autonomous, EWDS,
  ODRAF 20 units). Dana: cyclogenesis flagged 7.5 days out, 21 bulletins,
  842 permanent + 5,402 temporary shelters. 33% loss threshold with 2-day
  eye + 3-day objective survey = the claims workflow. Krushak Odisha portal
  = the Aadhaar-linked farm-data bridge. [d20]

## 5. EVENT REPLAY (d21-d24): THE VALIDATION ENGINE

- Tracks: IBTrACS v4.01 = normalized table for all 7 cyclones (CSV/netCDF).
  IMD reports add 3-hourly tracks (Fani/Amphan/Yaas/Dana), Phailin has
  hourly coastal obs. NOAA ISD = open hourly station obs (station audit
  needed). IMERG Final V07 (30-min, 0.1 deg, June 2000-present) = the common
  rainfall spine for every event. CWC/NWDP = hourly river levels. [d21][d24]
- Damage truth is event-dependent: Fani DLNA (district crop tables,
  108,220 ha, Rs 1,304.58 cr), Amphan memorandum (10,726 ha, 3,393 ha
  >=33%), Phailin (651,490 ha >50%, Rs 2,300 cr). Yaas + Aug 2022 flood have
  the strongest satellite validation cores (Sentinel-1 SAR + NRSC maps).
  1999/Hudhud/Yaas/Dana lack district crop tables. PMFBY is district
  aggregate only: no event IDs, no settlement dates. [d21][d22][d24]
- Ground truth: Phailin evacuated 983,642; Hudhud 255,043/2,143 shelters;
  the ONLY dated crop-specific pre-landfall advisory found is ICAR-NRRI's
  Dana rice-drainage advisory (23 Oct 2024). Early harvest costs 5.76% yield
  (35-days-after-heading comparator): the cost-of-waiting numbers must come
  from this literature, not invention. [d22]
- Methodology: a 5-event portfolio (Phailin, Titli, Fani, Yaas, Aug 2022
  floods) covers wind + rain + river + coastal. Best track != hazard field:
  observed data (Gopalpur station) corrects the parametric model. The
  "Ariadne discipline" is project-set acceptance gates, not a universal
  standard (the report corrected this honestly). Monte Carlo: start 2,500
  realizations, add 500 until district mean loss drifts <2% and P90 <
  threshold. Counterfactual claims need behavior evidence: receipt ->
  comprehension -> feasibility -> action -> timing, modeled separately.
  CRITICAL guardrail: advisory-timing replays must freeze the best-track to
  avoid leaking final outcomes into the engine. [d23]

## 6. THE VERDICT MAP

| Layer | Verdict | What we can honestly claim |
|---|---|---|
| Advisory engine (rules + profile + IMD/CWC + SMS/IVR) | GO | "Given this hazard and connectivity state, this farmer receives this prioritized action, offline-capable." |
| Sensor node (Rs 2,899 BOM) | GO (demo) | Local confirmation of official alerts, not independent detection |
| Phone hub (1B Q4 offline LLM) | GO (prototype) | Bounded rendering of approved advice in Odia/Hindi |
| Server LoRA loop | GO (prototype) | Logged feedback -> server training -> signed adapter -> rollback |
| Odia TTS/ASR | GATED | No native cloud TTS; IndicF5 + human recordings, comprehension tests |
| Live IMD/CWC production feed | GATED | CAP RSS now; API needs GOV/NIC partner |
| Crop-loss reduction claims | GATED | No yield-effect evidence anywhere; measured comprehension + action only |
| Real-event replay | GO (partial) | Tracks, rainfall, river stages, district damage for 5 events; plot-level GATED |
| Federated phone training | FILLER | Small classifier proof only |
| "AI predicts cyclones" | FILLER + unsafe | Contradicted by evidence |

## 7. WHAT THIS MEANS FOR THE BUILD

The prototype stack, in order: IMD CAP RSS ingest -> farm profile ->
deterministic agri rules (Odisha contingency plans as seed) -> advisory
with deadline/source/cost-of-waiting -> Odia template SMS/IVR -> offline
queue -> damage evidence -> claim packet (33% threshold, SDRF/PMFBY norms)
-> replay harness (IBTrACS + IMERG + CWC + Fani DLNA as validation) ->
sensor demo (BMP280 + ultrasonic on ESP32, BLE to phone) -> 1B Q4 phone
LLM rendering layer -> server LoRA loop (signed adapter, A/B, rollback).

The replay is the differentiator no other team will have: a validation
harness that runs our advisory engine against what actually happened in
Fani/Yaas/Dana and shows the trace.
