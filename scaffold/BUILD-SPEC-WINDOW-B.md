# BUILD-SPEC-WINDOW-B.md: KrishiSetu farmer UI + operator console (frontend lane)

Author: Hermes (window B, frontend lane). Implemented by: opencode.
Deadline: 16:00 merge. One file, one shot, no build step.

## SCOPE AND BOUNDARIES (hard)

- Create EXACTLY ONE new file: scaffold/webapp/static/krishi.html
- Do NOT modify any other file. Not serve.py, not index.html, not
  sw.js, not manifest.json, not engine/, not tests/, not fixtures/.
- No new backend endpoints. No fetch() calls at runtime at all: the
  page must work when opened straight from disk (file://) with zero
  network. All data below is embedded in the file.
- The page must be a single self-contained HTML file: all CSS and JS
  inline, no <link> to external CSS, no external fonts, no CDN, no
  images, no external requests of any kind.
- No em dashes anywhere in the file (the character U+2014 is banned).
- Banned words, never used in visible text: delve, leverage, robust,
  synergy, seamless, furthermore, moreover, additionally,
  cutting-edge, state-of-the-art, harness, unlock, streamline,
  notably, significantly, ultimately, essentially, platform (only
  when it means computing base, use "system"), revolutionize,
  transformative.
- stdlib demo rule: the page must never die on stage. No external
  deps. If JS throws, catch it and render a fallback div.
- Do NOT git commit. Do NOT git add.

## FILE: scaffold/webapp/static/krishi.html

Dark theme matching the scaffold palette:
--bg:#0B1020; --panel:#141B33; --panel2:#1B2440; --line:#263055;
--txt:#E8ECF8; --mut:#93A0C4; --accent:#6C5CE7; --accent2:#00CE8F;
--warn:#FFB020; --danger:#FF5470; --chip:#202A4E.
Font stack: Inter, 'Segoe UI', system-ui, sans-serif (no webfont).

Layout: top header (brand, current incident state chip, offline
toggle), horizontal tab bar, then tab panels, then a fixed honesty
strip at the bottom of the viewport, always visible.

Header brand: "କୃଷିସେତୁ KrishiSetu" (Odia script first, romanized
after) with subtitle "cyclone and flood resilient advisory, Odisha".

Tabs (button row, one visible panel at a time):
1. FARMER VIEW (default, label "ଚାଷୀ Farmer")
2. TWO-FARM CONTRAST (label "ଦୁଇ ଫାର୍ମ Two farms")
3. DELIVERY LADDER (label "ପହଞ୍ଚାଣ Ladder")
4. RESEARCH MACHINE (label "ଗବେଷଣା Research")
5. OPERATOR CONSOLE (label "ଅପରେଟର Console")

## TAB 1: FARMER VIEW

### 1a. Farm profile card (Asha)
Title: "ଅଶା Asha, farm profile". Rows (label: value), each value
carries its badge where it is a number (see badge system):
- crop: paddy (ଧାନ), variety Swarna
- stage: flowering (28+ days to maturity) [badge TRANSFER-PRIOR on the
  days figure: stage calendar from d4]
- plot: low-lying, flood-prone, lowest in village
- embankment: weak, unrepaired since last season
- land: LEASED, owner lives in town (tenancy flag ON)
- soil: sandy loam
- holding: 0.9 ha [badge ODISHA-MEASURED: 0.95 ha Odisha average, d6]
- labor: 2 adults
- phone: feature phone, SMS + IVR only, no data
- language: Odia
- debt: one KCC loan (40.5% of Odisha farm households carry debt,
  d6) [badge ODISHA-MEASURED]
- ack status: ACKED via IVR at 14:12 (SIMULATOR label)

### 1b. Incident state stepper (11 states)
Horizontal stepper, ordered, current state highlighted:
MONITOR -> PRE_CYCLONE_WATCH (72h) -> CYCLONE_ALERT (48h) ->
CYCLONE_WARNING (24h) -> POST_LAND_FALL_OUTLOOK (12h) ->
IMPACT_SUSPECTED -> IMPACT_CONFIRMED -> RESPONSE -> RECOVERY ->
NEXT_SEASON -> CLOSED.
Current: CYCLONE_WARNING (24h lead). Past states show a filled dot,
current shows a pulsing ring, future states dim.
Under the stepper, one line: "CAP-linked: every update replaces the
previous bulletin, never duplicates it (SIMULATED FEED)."
Second line: "The machine never closes on the first recession:
second-flood semantics keep RECOVERY open until NEXT_SEASON."

### 1c. Incident header (SIMULATED FEED)
"SIMULATED FEED: Cyclone warning for coastal Odisha, 24h lead, wind
175-185 km/h, surge 1.5-2 m over low-lying coast, rain 200+ mm in
24h. Source: IMD CAP bulletin (cached sample, live feed in Round 1)."
[badge SCENARIO-ASSUMPTION on the specific numbers, they are a demo
storm, not a live bulletin]

### 1d. Advisory list
Title: "ପରାମର୍ଶ Advisories, ranked by what Asha can do"
Each advisory card shows ALL of:
- rank number and Odia action title + romanized fallback
- action text (plain, short sentences)
- deadline (relative + clock time, e.g. "before 06:00 tomorrow")
- source line: "source: R7 (rule registry)" or "source: d35 (report)"
- cost of waiting line, starts with "cost of waiting:"
- doability line: "doability: 8h labor, Rs 1,200, credit: KCC ok,
  tenancy: owner approval required"
- its four-badge label(s) as small colored tags
- status chip: QUEUED / SENT / ACKED / DONE (SIMULATED)

Asha advisory rows, in this order:
A1 rank 1: "ଫସଲ କାଟ ନାହିଁ Do not harvest"
  text: flowering stage, grain not formed; harvesting now loses the
  whole season. Early-harvest studies at maturity put the loss at
  5.76% (d32); at flowering the loss is total. Protect the crop
  instead.
  deadline: not applicable (no harvest option)
  source: d32 (early-harvest meta), d33 (stage science)
  cost of waiting: 0, harvest is not an option at flowering
  doability: 0h labor, Rs 0, no credit, no tenancy issue
  badges: TRANSFER-PRIOR (5.76% meta), SCENARIO-ASSUMPTION (stage
  calendar)
A2 rank 2: "ବନ୍ଧ ମରାମତି Reinforce the weak embankment"
  text: weak embankment, low plot: a 1.5-2 m surge can overtop it.
  Sandbag the weakest 30 m stretch.
  deadline: before 06:00 tomorrow (12h)
  source: R7 (fragility rule), d9 (fragility math)
  cost of waiting: an overtopped embankment adds standing water days
  on a low plot; waterlogging alone reprocesses 41.9% of the crop
  (d3)
  doability: 8h labor, Rs 1,200 sandbags, credit: KCC ok, tenancy:
  owner approval required, request sent via IVR (SIMULATOR), pending
  badges: SCENARIO-ASSUMPTION (Rs 1,200 cost), TRANSFER-PRIOR (d3)
A3 rank 3: "ବୀଜ ଉଚ୍ଚ ସ୍ଥାନକୁ Move seed stock and grain to high ground"
  text: seed is next season's capital. Move stored seed and harvested
  grain to the raised platform or the neighbor's high room.
  deadline: before 18:00 today
  source: R6 (seed protection), d35 (Koraput storage wisdom)
  cost of waiting: a flooded seed stock means no re-sowing and relief
  dependence next season (d37)
  doability: 2h labor, Rs 0, no credit, no tenancy issue
  badges: TRANSFER-PRIOR
A4 rank 4: "ଜନ୍ତୁ ଆଶ୍ରୟ Livestock to raised shelter"
  text: move livestock to the raised shelter or high ground before
  dark.
  deadline: before 18:00 today
  source: R8 (livestock rule), d46 (effects catalog)
  cost of waiting: livestock loss is a capital loss on a small
  holding
  doability: 3h labor, Rs 0
  badges: TRANSFER-PRIOR
A5 rank 5: "ଦାବି ପ୍ରସ୍ତୁତି Claim packet prep: photo + 72h clock"
  text: photograph the standing crop now with a time stamp. PMFBY
  intimation must be filed within 72h of loss; 33% crop damage is the
  threshold (d6).
  deadline: photo now, intimation within 72h of loss
  source: d6 (PMFBY rules)
  cost of waiting: a missed intimation window can void the claim
  doability: 30 min labor, Rs 0, phone camera not needed: the photo
  can be taken by the volunteer
  badges: ODISHA-MEASURED (72h clock, 33% threshold)
A6 rank 6: "ନାଳ ସଫା Clear the drainage outlet"
  text: low plot drains through one outlet. Clear it before the rain.
  deadline: before 20:00 today
  source: R9 (drainage rule), d3 (waterlogging)
  cost of waiting: standing water duration decides the loss share
  doability: 4h labor, Rs 0
  badges: TRANSFER-PRIOR
A7 rank 7 (queued for next state, label "NEXT STATE: RESPONSE"):
  "ଲୁଣ ପରୀକ୍ଷା Test sediment before re-sowing"
  text: after water recedes, test sediment salinity before re-sowing;
  Saltol seedlings hold saline patches (d33). This fires in RESPONSE
  or RECOVERY, not now.
  deadline: after recession (state-gated)
  source: d33 (Saltol), d5 (SAC salinity mapping)
  cost of waiting: re-sowing into saline soil wastes seed and labor
  doability: 1h labor, Rs 0
  badges: TRANSFER-PRIOR

### 1e. Offline toggle
A switch in the header labeled "ଅଫଲାଇନ Offline (SIMULATED)". Flipping
it:
- adds a visible queue banner: "3 actions queued, syncs when
  bandwidth returns (SIMULATED)"
- the advisory list still renders fully (it renders from embedded
  local state, which is the point)
- nothing else changes. No network calls exist, so no errors.

## TAB 2: TWO-FARM CONTRAST

Title: "Same warning, different advice: ଅଶା Asha vs high field"
One line intro: "Both farms received the same 24h cyclone warning.
The compiler produces different actions because the profiles differ:
stage, plot, embankment, tenancy, labor."
Two-column layout. Left column = Asha (profile summary: flowering
paddy, low plot, weak embankment, leased, 2 adults). Right column =
high-field farm (profile summary: mature paddy, high plot, strong
embankment, owned, 5 adults + hired labor).
A toggle button above the columns: "compare: [Asha] [High field]".
Active farm column is highlighted; both columns always show their
own full advisory list (top 5 each) so the contrast is visible in
one glance without clicks.
High-field farm (label "ଉଚ୍ଚ ଜମି ଫାର୍ମ High field farm"):
H1 rank 1: "ଫସଲ କାଟ Harvest now"
  text: mature paddy, ~10 days early. Early harvest costs about
  5.76% on average (d32); a flooded mature crop can be a total loss.
  Harvest before landfall.
  deadline: before 06:00 tomorrow
  source: d32 (early-harvest meta), d9 (replay math)
  cost of waiting: each day of flood water on mature paddy risks the
  full crop; Swarna-Sub1 buys ~64 kg/ha per flood day of survival
  edge (d33), but 5-7 days under water still cuts yield
  doability: 40 person-hours (5 adults + 3 hired), Rs 2,500 hired
  labor, credit: KCC ok, tenancy: owned, no block
  badges: TRANSFER-PRIOR (5.76%, 64 kg/ha/day), SCENARIO-ASSUMPTION
  (Rs 2,500 cost)
H2 rank 2: "ଗୋଦାମ ନିରାପଦ Secure stored grain in the stilt granary"
  text: move stored grain to the stilt granary, off the floor.
  deadline: before 18:00 today
  source: d35, d42 (storage wisdom)
  cost of waiting: floor-level grain wicks moisture in one night
  doability: 3h labor, Rs 0
  badges: TRANSFER-PRIOR
H3 rank 3: "ବନ୍ଧ ମରାମତି Reinforce the embankment"
  text: strong embankment, owned land: top it up and sandbag the
  joints. Feasible without any approval.
  deadline: before 06:00 tomorrow
  source: R7, d9
  cost of waiting: overtopping floods the field for days
  doability: 8h labor, Rs 1,500 sandbags, credit: KCC ok, tenancy:
  owned, no block
  badges: SCENARIO-ASSUMPTION (Rs 1,500), TRANSFER-PRIOR
H4 rank 4: "ପମ୍ପ ଉଠାଅ Move pump and equipment above the flood line"
  text: one hour of labor saves the pump from immersion.
  deadline: before 20:00 today
  source: R10 (equipment rule)
  cost of waiting: an immersed pump is days of recovery delay
  doability: 1h labor, Rs 0
  badges: TRANSFER-PRIOR
H5 rank 5: "ଦାବି ପ୍ରସ୍ତୁତି Claim packet prep: photo + 72h clock"
  same fields as A5, source d6, badge ODISHA-MEASURED
Under the two columns, a contrast strip listing the three structural
differences that changed the advice:
1. stage: flowering (harvest impossible) vs mature (harvest first)
2. tenancy: leased (embankment work needs owner approval) vs owned
   (feasible now)
3. plot: low (drainage + surge exposure) vs high (drainage fast)

## TAB 3: DELIVERY LADDER

Title: "ପହଞ୍ଚାଣ Delivery ladder: six rungs, one message"
Intro line: "No single channel reaches every Odisha farmer (d7, d28).
The advisory starts at the top rung and escalates DOWN when a rung
is unacknowledged. Every rung shows its latency budget."
Six vertical rungs (top to bottom), each a row with: rung number,
channel name, works-on line, latency budget, trigger line, fallback
line, and its honesty label:
1. App (offline-first PWA): smartphones, any data; <5s push; trigger
   4G/5G present; fallback: cache renders from local store, queue
   syncs later; label ROADMAP (PWA in Round 1)
2. SMS (Odia-capable, DLT): ANY phone including feature phones;
   5-30 min; trigger 2G/3G no data; fallback: unread after T,
   escalate to IVR; label SIMULATOR
3. IVR missed-call callback: ANY phone, no data; 30-60s setup;
   trigger DND, low literacy, no credit (collect call); fallback:
   unacknowledged, escalate to volunteer; label SIMULATOR
4. USSD (session-based): ANY phone, 2G; <1s round trip, 90s
   session; trigger 2G only, data dead, SMS slow; fallback: session
   expiry, SMS fallback; label SIMULATOR
5. Community radio / loudspeaker: no phone needed; broadcast
   schedule; trigger tower down, mass event; fallback: village relay
   confirms; label ROADMAP
6. Village volunteer / paper: no phone needed; hours; trigger
   everything dead; fallback: post-event debrief; label ROADMAP
Between rungs, a down-arrow with the label "unacknowledged -> next
rung down" repeated on each gap.
Side note box: "Latency budget decides the rung: a 6h action window
ships by SMS, a 1h window ships by IVR and radio (THE-PLAN rules)."
Footer line: "SIMULATOR: no live sending, no live calls. Real
gateway + DLT registration are Round 1 (BUILD-MATRIX tier 2)."

## TAB 4: RESEARCH MACHINE

Title: "ଗବେଷଣା Research machine: the 48-report base"
Subtitle: "48 reports, 6 waves, ~2.5M chars. Rows below are the
index from krishisetu/research/EVIDENCE-INDEX.md (d1-d47); refire
runs and the wave ledger live in research/run-ledger."
Search input (placeholder "search 48 reports, e.g. submergence,
tenancy, radio") + wave filter chips (All, Wave 1, Wave 2, Wave 3,
Wave 4, Wave 5, Wave 6).
List every row below. Each row: report id chip (d01-d47), wave tag,
"what it proved" text, "feeds:" text. The full 43-row index:

Wave 1 (d1-d9):
d1 cyclone science + India detection: IMD scale machine-codable,
72/48/24h lead stages, track errors, 1999 deaths despite warning |
feeds: hazard trigger
d2 flood science + CWC network: 325 stations, warning cadence,
compound chains, recession clock | feeds: flood trigger
d3 cascades + positive use (refire): waterlogging 41.9% repro loss,
salinity persistence, blast conditions, PMFBY cover | feeds: cascade
d4 Odisha crops + calendars + fragility: paddy 44% of GCA,
Swarna-Sub1, stage calendars, machinery numbers | feeds: farm profile
d5 land/elevation/soil/salinity: DEM options, soil maps, SAC Yaas
salinity mapping, CGWB recharge | feeds: soil data
d6 farmers + impact + PMFBY: 4.866M holdings, 0.95 ha avg, debt
40.5%, PMFBY intimation window | feeds: doability
d7 devices + collection: CWC sites, tide gauges, SMS/IVR tariffs,
DLT | feeds: delivery
d8 advisory prior art: GKMS cadence, KCC 22 languages, Ama Krushi
scale | feeds: prior art
d9 hazard-model math + fragility: Holland field, Bates-De Roo,
Swarna-Sub1 RCT, SDRF norms | feeds: replay

Wave 2 (d10-d14):
d10 on-device LLM: 1B Q4 = design center, 3B out, llama.cpp, Lava
Blaze target | feeds: AI layer
d11 continuous fine-tuning: three-loop model, LoRA 11-49MB, server
gated training | feeds: AI layer
d12 cheap sensor hardware: Rs 2,899 node BOM, pressure tendency, no
universal hPa/hr | feeds: hardware
d13 predictive stats: BOCPD/Kalman/iForest, no oracle claims,
thresholds must be fitted | feeds: math
d14 edge-AI agri prior art: no full loop exists anywhere, OSDMA
EWDS, Nuru | feeds: white space

Wave 3 (d15-d20):
d15 Odia + low-literacy voice: Ama Krushi 50K calls, no Odia TTS
from big vendors, IndicF5, WER 35.1 real | feeds: voice
d16 IMD/CWC/INCOIS API: CAP RSS free, IMD API gated, WRIS works,
Open-Meteo fallback | feeds: feed
d17 power + connectivity: Fani 4 districts down 9 days, rural supply
reality | feeds: offline
d18 who pays: 81.3% WTP, voice reminders 38% vs 18%, ATMA 60:40,
FPO rails | feeds: business
d19 training data: IMD gridded 1901-2024, best tracks, CWC free,
J-PAL data | feeds: replay
d20 OSDMA ecosystem: post-1999 institutions, EWDS, ODRAF, Krushak
Odisha 9.2M | feeds: institutional

Wave 4 (d25-d30):
d25 global prior art: BaKhabar Kissan 15.8M, BAMIS, no recovery
state machine anywhere | feeds: white space
d26 GitHub/forums sweep: KrishiRakshak collision (yesterday), Ama
Krushi 7.9M + 10% loss cut | feeds: honesty
d27 anticipatory action + insurance: WFP $53 pre-event, R4, ARC,
ACRE 217K failed deliveries | feeds: claims rail
d28 offline/feature-phone delivery: Ethiopia 8028 6M/60M calls,
radio 24.1M, WeFarm/iCow deaths | feeds: delivery
d29 LLM + agri worldwide: Farmer.Chat 830K/5M queries, AgroMetLLM
Pi 4B, sesame incident | feeds: AI
d30 farm data platforms: SoilGrids, WorldCover, GDACS, GloFAS,
Sen1Floods11 free | feeds: data

Wave 5 (d31-d40):
d31 farmer problem capture: symptom grammar, keypad > ASR, KCC
corpus, 65% want experts | feeds: voice
d32 crop evacuation physics: 5.76% early-harvest meta, labor
hours/ha, movable units | feeds: action
d33 frontier agri science: Swarna-Sub1 +64kg/ha/day, Saltol
seedling-stage, halopriming | feeds: science
d34 unique angle validation: QUALIFIED GO, new combination, not
first-to-harvest | feeds: honesty
d35 human disaster history: universal sequence, Koraput storage,
mangroves 409-village | feeds: wisdom
d36 science validation folk: FR13A -> Sub1 story, tiered evidence
gate | feeds: wisdom
d37 adaptation gap: tenancy 5.82%, debt, labor, relief hazard,
memory decay | feeds: THESIS
d38 farmer-as-sensor: phone as data network, DTMF, photo protocols,
zero hardware | feeds: data
d39 doability engine: feasibility-aware advisories are rare, labor
is the constraint | feeds: THESIS
d40 farmer data as asset: value loop data -> advice -> claims ->
credit | feeds: business

Wave 6 (d41-d47):
d41 global farm practices (refire): Vietnam/Japan/China/Andes/
Indus/Niger practices | feeds: wisdom
d42 storage + water engineering: stilt granaries, qanats, amunas,
bolanha, baira | feeds: wisdom
d43 institutional response + theory: CPP 76K volunteers, Japan
nosai, FCIP, Delta Programme, Sendai | feeds: institutional
d44 every cyclone agri damage: Sidr 1.4M ha, Idai 715K, Remal
498K, Mocha 327K, Yagi 286K, Michael $2B+, noise log | feeds:
global record
d45 every major flood agri: Yangtze 1998, Pakistan 2010/2022,
Kerala, Thailand 2011, Nigeria, Brazil 2024 | feeds: global record
d46 complete effects catalog: full taxonomy during/immediate/weeks/
years + positives | feeds: cascade
d47 cascade systems math: typed DAG, BN-FLEMO MAE 0.18, CVaR, MC
gates, four badges | feeds: THESIS

Row footer note: "raw reports live in krishisetu/research/raw/ and
hackathon-sota-lab/research/raw/v2/, one JSON per report
(cnc-ps07-dXX-<slug>.json). Chain: slide -> proof ledger -> index
row -> raw report."

## TAB 5: OPERATOR CONSOLE

Title: "ଅପରେଟର Operator console (minimal, SIMULATED)"
Section 1, incidents: one table row: incident INC-2026-001, source
"IMD CAP bulletin (SIMULATED FEED)", state CYCLONE_WARNING (24h),
version v3 (CAP-linked updates), started 13:40.
Section 2, per-farm ack status, table with columns farm, channel,
sent, ack, status:
- Asha | IVR callback (SIMULATOR) | 14:05 | 14:12 | ACKED
- Asha | SMS (SIMULATOR) | 13:58 | unread | ESCALATED to IVR
- High field | SMS (SIMULATOR) | 13:58 | unread | ESCALATED
- High field | Volunteer + radio (ROADMAP) | assigned 14:30 |
  pending | pending
Section 3, the evidence chain (slide -> ledger -> index -> raw):
three rows, each showing the chain for one anchor number:
- Fani 108,220 ha / Rs 1,304.58 cr: deck slide 7 (replay) -> ledger
  P1-P6 (proof ledger, deck claims) -> index row d9 -> raw report
  cnc-ps07-d09-hazard-model-math-fragility.json
- Yaas 2-4 m surge: deck slide 7 -> ledger -> index row d5 -> raw
  report cnc-ps07-d05-land-elevation-soil-salinity.json
- Swarna-Sub1 +64 kg/ha per flood day: deck slide 8 (science) ->
  ledger -> index row d33 -> raw report
  cnc-ps07-d33-frontier-agri-science.json
NOTE: verify the raw filenames by listing the directories
~/krishisetu/research/raw/ and ~/krishisetu/research/run-ledger/
before writing them. If a filename cannot be confirmed, write the
chain cell as "raw: research/raw/ (see index row dXX)" instead of
an invented filename. Never write a filename you did not see.
Section 4, delivery log (SIMULATOR), table: time, rung, event:
13:40 incident created (SIMULATED FEED)
13:58 SMS sent to Asha, SMS sent to high field (SIMULATOR)
14:05 IVR callback to Asha (SIMULATOR)
14:12 Asha ACKED via keypad press 1 (SIMULATOR)
14:30 volunteer assigned for high field (SIMULATED)
17:00 radio bulletin scheduled (ROADMAP)

## BADGE SYSTEM (used everywhere)

Four badge tags, each a colored pill:
- ODISHA-MEASURED: green (#00CE8F), "measured on Odisha ground,
  dated source"
- TRANSFER-PRIOR: blue (#4A9EFF), "from other regions or studies"
- SCENARIO-ASSUMPTION: amber (#FFB020), "demo scenario or modeled
  assumption"
- UNKNOWN: red (#FF5470), "not known yet, TODO: report dXX"
A legend block at the bottom of the FARMER VIEW tab renders all four
with their meanings.

## HONESTY STRIP (fixed, always visible, bottom of viewport)

One bar, small text, labeled "HONESTY STRIP": SIMULATED FEED (hazard
input) | SIMULATOR (SMS, IVR, USSD traces) | SIMULATED STREAM
(sensors) | ROADMAP (PWA, radio, LoRA loop, live CAP) | every number
wears a badge.

## ODIA LABELS (use verbatim, romanized fallback in parens)

କୃଷିସେତୁ (KrishiSetu), ଚାଷୀ (farmer), ଫସଲ (crop), ଧାନ (paddy),
ଜମି (land), ଝଡ଼ (cyclone), ବନ୍ୟା (flood), ଫସଲ କାଟ (harvest),
ମାଟି (soil), ବୀଜ (seed), ପାଣି (water), ପରାମର୍ଶ (advisory),
ସତର୍କତା (warning), ଜନ୍ତୁ (livestock), ଗବେଷଣା (research),
ପହଞ୍ଚାଣ (delivery), ଅପରେଟର (operator), ଅଫଲାଇନ (offline),
ଦୁଇ ଫାର୍ମ (two farms), ସାହାଯ୍ୟ (help).

## ACCEPTANCE GATES (self-check before you report done)

G1. Exactly one new file: scaffold/webapp/static/krishi.html. git
    status shows no other changes.
G2. Page opens from file:// with no console errors and no network
    requests (DevTools network tab empty). Also served by
    python3 scaffold/webapp/serve.py at /static/krishi.html with a
    200.
G3. Farmer view: farm card, 11-state stepper with CYCLONE_WARNING
    current, advisory list A1-A7 each with deadline, source,
    cost-of-waiting, doability line, badge tags, status chip.
G4. Contrast tab: both columns render; toggle switches highlight;
    same warning header; Asha shows "do not harvest" and high field
    shows "harvest now".
G5. Ladder tab: 6 rungs with latency budgets, escalation arrows with
    "unacknowledged -> next rung down", honesty labels per rung.
G6. Offline toggle: queue banner appears with "syncs when bandwidth
    returns (SIMULATED)", advisory list still renders.
G7. Badge legend + honesty strip render; every numeric claim in the
    file carries a badge class; SIMULATED FEED / SIMULATOR /
    SIMULATED STREAM / ROADMAP labels present.
G8. Research tab: 43 rows, search filters live, wave chips filter,
    no invented raw filenames.
G9. Console tab: incident table, ack table, evidence chain rows,
    delivery log.
G10. Odia script appears on key labels with romanized fallback.
G11. Only verified numbers used: Fani 108,220 ha / Rs 1,304.58 cr,
     Yaas 2-4 m surge, Swarna-Sub1 +64 kg/ha per flood day, 72h
     intimation clock, 33% threshold, 5.76% early-harvest meta,
     0.95 ha average holding, 40.5% debt, 4.866M holdings, 41.9%
     waterlogging loss, WER 35.1, 81.3% WTP, Rs 2,899 sensor BOM,
     325 CWC stations, Ama Krushi 7.9M, BaKhabar Kissan 15.8M.
     Anything not in this list carries SCENARIO-ASSUMPTION or
     UNKNOWN, or a TODO note.
G12. No em dash character (U+2014) in the file. None of the banned
     words in visible text.
G13. No fetch(), no XMLHttpRequest, no importScripts, no external
     URLs in the file.
