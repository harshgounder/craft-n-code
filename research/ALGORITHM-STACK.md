# ALGORITHM-STACK.md — The Actual Math, Front and Center

Date: 2026-08-16. Every algorithm below is evidence-backed (report +
source) and runs WITHOUT API keys, most without internet.

## A. THE ADVISORY ENGINE (the product, deterministic core)

A1. STAGE-AWARE CROP FRAGILITY FUNCTIONS (the agronomy math)
- Submergence: damage(stage, depth, days). Myanmar model: 1.0 m x 8
  days = 50% loss vegetative, 40% reproductive (d9, provisional prior).
  Swarna-Sub1: 45% yield advantage after 10 days submerged, 128-village
  RCT (d9, the Odisha anchor).
- Waterlogging meta: mean yield loss 32.9%; 41.9% at reproductive
  stage vs 34.75% vegetative (d3-refire).
- Salinity: threshold 1.9 dS/m, yield-decline slope 9.1% per unit
  (d4). Post-Yaas: 5,882 ha Balasore + 1,400 ha Bhadrak seawater, one
  month persistence (d3-refire, d22).
- Wind: IMD wind polygon severity x stage; no published universal
  threshold, so the engine uses stage x wind-band rules (d1, d13).
- Harvest timing: early harvest penalty 5.76% yield (35-day comparator,
  d22). This is the COST OF WAITING vs cost of acting.

A2. ACTION RANKING: expected-loss comparator
For each candidate action a in the approved rule set:
  cost(a) = cost of acting now (harvest loss, labor, input)
  risk(a) = expected loss if not acting, from fragility functions
  benefit(a) = risk(a) - cost(a)
Rank by benefit, emit the top action with its deadline, source, and
confidence. This is a decision table, not prose. Deterministic,
testable, auditable.

A3. DEADLINE CALCULATION
- Official lead time: Watch 72h / Alert 48h / Warning 24h / Post-landfall
  (d1). Deadline = event time - action execution window.
- Rule deadlines are expressed in hours-before-event, resolved to local
  wall-clock at advisory generation. No floating time claims.

A4. CLAIM PACKET LOGIC (the money rail)
- 33% crop-loss threshold (SDRF/NDRF norms), Rs 8,500/ha rainfed,
  Rs 17,000/ha irrigated (d9).
- PMFBY: 72-hour loss intimation window, evidence routes, max two-week
  post-harvest coverage (d6, d3-refire).
- The packet = farm profile + advisory sent + observed damage evidence
  + timestamps. Deterministic assembly, exportable.

A5. OFFLINE RENDERING (no LLM required)
- Fixed Odia templates: action + deadline + source + cost-of-waiting
  in a 262-char SMS envelope (IMD ceiling, d15).
- IVR script: one decision per prompt, replay, DTMF confirm, KCC
  escalation (CGNet pattern, d15).
- The LLM, when present, only re-renders the same structured fields.

## B. THE BACKUP HAZARD LAYER (only fires when official message missed)

B1. BAYESIAN ONLINE CHANGEPOINT DETECTION (BOCPD)
Adams-MacKay posterior over run length, pruned, per stream:
pressure tendency, water level, rain intensity. Runs on the node or
phone (d13: edge-feasible with pruning, log-space arithmetic, capped
run-length hypotheses). Detects regime change, never "predicts a
cyclone". The trigger is a regime change DURING an official alert
window or when the official alert is absent but multiple streams
agree.

B2. EWMA + PERSISTENCE + HYSTERESIS (false-alarm suppression)
z_t = lambda*x_t + (1-lambda)*z_(t-1) (NIST, d13). A lone spike never
alerts; a persistent, corroborated trend does. Two evaluation cycles
minimum before escalation (Google SRE guidance, d13).

B3. SCALAR KALMAN FILTER (sensor denoising)
Per-sensor state + noise model. Water level and pressure only; never
fuse unlike variables (d13).

B4. ONLINE ISOLATION FOREST (anomaly detection)
True streaming variant (ICML 2024, d13), fixed features, bounded
window. Answers "is this feature vector unusual", separate from BOCPD
and Kalman, never blended into one opaque score (d13).

B5. ANTECEDENT PRECIPITATION INDEX (API)
Recursive: API_t = k*API_(t-1) + rain_t, k fitted per soil class and
drainage (d13). Wetness prior for waterlogging and flood sensitivity.

B6. PRESSURE-TENDENCY TREND (the cheap precursor)
BMP280 relative accuracy +/-0.12 hPa; rate-of-fall over 5/15/60-min
windows, station-fitted from replay data (d12, d13). NO universal
hPa/hour rule: the threshold is learned from the event replay, per
station. That is the honest version of the user's "predict" ask.

B7. MULTI-STREAM ESCALATION POLICY
Alert fires only when: official alert active OR (2+ independent
streams show regime change AND persistence AND corroboration). The
advisory engine is triggered, not a new hazard claim. This is the
"in case the message is not reached" backup, nothing more.

## C. THE REPLAY + VALIDATION MATH (the differentiator)

C1. HOLLAND 1980 WIND FIELD, fitted per event from best-track (d9,
d23). The Kalsi-2006 B fit is unverifiable: fit B from observed station
data instead (d9 correction).

C2. BATES AND DE ROO DIFFUSION-WAVE FLOOD ROUTING on 30-32 m DEM
(SRTM/AW3D30/CartoDEM, d5), validated against CWC hourly gauges and
NRSC Sentinel-1 flood extents (d23, d24).

C3. MONTE CARLO with convergence gates: start 2,500 realizations, add
500 until district mean loss drifts <2% and P90 stabilizes (d23).

C4. CVaR DECISION SURFACE (from Ariadne): the advisory engine's worst-
5% expected loss per action, not the mean. "Harvest by 18:00 or face
X% in the worst 5% of outcomes."

C5. EVENT REPLAY VALIDATION: freeze the best-track at advisory issue
time (no leakage, d21), compare simulated vs observed district damage
(Fani DLNA 108,220 ha Rs 1,304.58 cr; Phailin 651,490 ha >50% loss;
Amphan 10,726 ha) with hold-out districts (d21, d23).

C6. EXTREME VALUE THEORY (GEV/GPD) return periods from Mahanadi flood
frequency analysis (d13, d9) as plot-depth priors, flagged non-
stationary (d13).

## D. WHAT RUNS WHERE (zero-API, self-dependent)

| Tier | Hardware | Algorithms |
|---|---|---|
| Node (optional, Rs 1,324) | ESP32 + BMP280 + ultrasonic + rain | Median despike, EWMA, rate-of-rise, battery health |
| Phone or laptop (the hub) | Any Android or this laptop | BOCPD, Kalman, Online-iForest, API, fragility math, action ranking, templates |
| Replay + training | Laptop GTX 1650 (1B QLoRA ok) | Holland, Bates-De Roo, Monte Carlo, CVaR, LoRA |
| Delivery | SMS/IVR gateways (simulated in demo) | Templates, retry, DTMF, receipts |

No API key in the critical path. IMD CAP RSS is cached when reachable
and the system runs on its absence.
