# WINDOW-C-OPENCODE-BRIEF.md (backend + data lane, executed via opencode)

GOAL: build the KrishiSetu data layer into ~/krishisetu/backend/: SQLite
schema (stdlib sqlite3), REST API (stdlib http.server, pattern: the
scaffold serve.py), SMS/IVR/USSD adapter stubs with escalation, CAP
ingest stub, seed data (2 farms, Fani/Yaas archives, R1-R16 rules,
research index), postgres_schema.sql roadmap file. Branch: window-c.
All source code written by you (opencode). No em dashes anywhere.
stdlib only, zero new deps. Do NOT touch anything outside backend/.
Do NOT git commit, the orchestrator audits and commits.

## CONTEXT

- This repo is the research home for Team 511 KrishiSetu, Craft N Code
  2026, PS-07: cyclone and flood resilient smart agriculture advisory
  for Odisha, delivered app -> SMS -> IVR -> USSD -> radio -> village.
- The API contract shapes below are what the frontend and core lanes
  read and write. Match them EXACTLY (field names, nesting, enums).
- The events table is APPEND-ONLY with a hash chain (IMPROVISED-ANSWERS
  D1): every write appends an event whose hash chains to the previous
  event. Tamper = hash mismatch alarm via GET /api/events/verify.
- The delivery ladder rung order (THE-PLAN part 1, R2): app, sms, ivr,
  ussd, radio, village. Unacknowledged after a threshold escalates to
  the NEXT rung down (app -> sms -> ... -> village). village is
  terminal (no rung below it).
- The 11 incident states: MONITOR, PRE_CYCLONE_WATCH, CYCLONE_ALERT,
  CYCLONE_WARNING, POST_LAND_FALL_OUTLOOK, IMPACT_SUSPECTED,
  IMPACT_CONFIRMED, RESPONSE, RECOVERY, NEXT_SEASON, CLOSED.
- Honesty labels (non-negotiable): adapter stubs respond with label
  "SIMULATOR"; the CAP ingest stub responds with label "CACHED SAMPLE";
  the seeded live demo incident carries badge "SCENARIO-ASSUMPTION".
  No real SMS, no real telephony, no live CAP fetch, no real phone
  numbers (use 0000000XXX style numbers).
- Four badges: ODISHA-MEASURED, TRANSFER-PRIOR, SCENARIO-ASSUMPTION,
  UNKNOWN. Every advisory action and every incident carries a badge.
- SQLite: enable WAL mode and busy_timeout 5000 at connect (S2).
- Default API port 8100 (the scaffold webapp owns 8000, the core lane
  owns 8000 too). Flags: --port, --host, --db, --seed.

## CONTRACT SHAPES (verbatim, no deviation)

### farm_profile (POST /api/farms body, stored on farms table)
{"farm_id","district","block","phone","language":"odia|hindi|english",
 "members":[{"name","role"}],
 "plots":[{"plot_id","lat","lon","elevation_m","elevation_source":
   "DEM|FARMER|UNKNOWN","soil","soil_source":
   "TEST|NBSS-LUP|FARMER|UNKNOWN","drainage":"good|poor|unknown",
   "embankment":"strong|weak|none|unknown",
   "flood_history":[{"year","depth_m"}]}],
 "crops":[{"crop":"paddy|banana|coconut|vegetables|pulses|maize|other",
   "variety","stage":"seedbed|vegetative|flowering|grainfill|maturity|harvested|other",
   "stage_entered_at","sowing_date","stage_expires"}],
 "seed_stock":{"kg","elevated","sealed"},
 "livestock":[{"species":"cattle|buffalo|goat|poultry|other","count"}],
 "tenancy":"owned|leased|shared|unknown","labor_available","credit_access":
 "yes|no|unknown","phone_type":"smartphone|feature|shared|none",
 "consent":{"enrolled_at","opt_out","deleted","data_shared"}}

### incident (CAP-style, 11-state machine)
{"incident_id","cap_type":"Alert|Update|Cancel|Ack|Error",
 "source":"IMD|CWC|INCOIS|LOCAL-SENSOR|SIMULATED",
 "state":"MONITOR|PRE_CYCLONE_WATCH|CYCLONE_ALERT|CYCLONE_WARNING|POST_LAND_FALL_OUTLOOK|IMPACT_SUSPECTED|IMPACT_CONFIRMED|RESPONSE|RECOVERY|NEXT_SEASON|CLOSED",
 "issued_at","valid_until",
 "hazard":{"type":"cyclone|flood|surge|compound","wind_kmh","rain_mm",
   "surge_m","tide","river"},
 "badge":"ODISHA-MEASURED|TRANSFER-PRIOR|SCENARIO-ASSUMPTION|UNKNOWN"}

### advisory_action
{"action_id","incident_id","farm_id","phase":"pre|during|post|recovery|next-season",
 "action","deadline","source":"rule-R1..R16|report-dXX","grade":"A|B|C|D",
 "cost_of_waiting","badge",
 "doability":{"labor_hours","cost_rs","credit_needed","tenancy_ok",
   "feasible","infeasible_reason"},
 "delivery":{"rung":"app|sms|ivr|ussd|radio|village",
   "status":"queued|sent|delivered|acknowledged|escalated","delivery_id"},
 "obsolete_after"}

### claim_packet
{"claim_id","farm_id","incident_id","intimation_72h","loss_threshold_33",
 "evidence":[{"type":"photo|voice|text|geo","path"}],
 "status":"draft|ready|submitted|rejected|appealed",
 "export_formats":["text","images","printable"]}

## BUILD

### 1. backend/schema.sql
DDL for: farms, plots, crops, incidents, actions, deliveries, claims,
events. Normalized: farms holds scalar profile fields + JSON columns
for members, seed_stock, livestock, consent; plots and crops are child
tables with a farm_id FK; incidents carry hazard_json, impact_json,
badge; actions carry doability_json and delivery_json; deliveries carry
receipt, threshold_seconds, parent_delivery_id (escalation chain);
claims carry evidence_json. The events table:
  events(seq INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL,
    entity_type TEXT NOT NULL, entity_id TEXT NOT NULL,
    action TEXT NOT NULL, payload_json TEXT NOT NULL,
    prev_hash TEXT NOT NULL, hash TEXT NOT NULL)
hash = sha256(prev_hash + "|" + ts + "|" + entity_type + "|" +
entity_id + "|" + action + "|" + payload_json) where payload_json is
json.dumps(sort_keys=True) and the first event prev_hash = "GENESIS".
App code never UPDATEs or DELETEs events. farms table has
deleted INTEGER DEFAULT 0 and deleted_at for the tombstone (D6).

### 2. backend/db.py
connect (WAL, busy_timeout), migrate from schema.sql, event append
helper with chain hashing, chain verify helper that walks every event
and returns {ok, chain_length, broken_at (seq of first mismatch or
null)}. All helpers small, stdlib only.

### 3. backend/seed.py + backend/seed/ data files
--seed flag on serve.py calls this. Builds backend/krishisetu.db fresh
(remove old file first), runs schema.sql, loads:
- seed/farms.json: the two farms below (exact contract shapes)
- seed/incidents.json: Fani, Yaas, and the SIMULATED live demo incident
- seed/rules.json: the R1-R16 registry (content below)
- seed/actions.json: a few canned advisory actions for the demo
  incident, one per farm, showing the two-farm contrast (same
  incident, different action sets: Asha gets seed-raising + livestock
  move + no harvest order, Bikash gets harvest-now advisory), each
  with doability fields, badge, grade, source, cost_of_waiting
- seed/research_index.json: BUILT BY PARSING research/EVIDENCE-INDEX.md
  (tables: report | what it proved | feeds, wave headers) plus glob of
  research/raw/cnc-ps07-d*.content.md files joined by d-number. Each
  entry: {"id","wave","report","what","feeds","raw_paths":[...]}.
  Never hardcode a count, expose the true parsed total. Rows d21-d24
  exist as raw files but have NO index row in EVIDENCE-INDEX.md: add
  them anyway with what/feeds taken from their filenames, flagged
  "index_row":"missing-in-index".
  Seed farms/incidents/actions/claims all append their own events
  (entity_type farm/incident/action/claim, action create) so the chain
  is populated from genesis.
Seed data specifics (MERGE PROTOCOL ids, from the orchestrator: these
EXACT ids are the merge contract with the core lane, which seeds the
same two farms on its side; deviating breaks the merge silently):
- Asha: farm_id asha-001, district Kendrapara, block Mahakalapada,
  phone 0000000001, language odia, members [{"name":"Asha","role":
  "farmer"}], one plot (plot_id P1, lat 20.3561, lon 86.6348,
  elevation_m 1.2, elevation_source DEM, soil clay, soil_source
  NBSS-LUP, drainage poor, embankment weak, flood_history [{"year":
  2021,"depth_m":1.8},{"year":2019,"depth_m":1.5}]), crops paddy
  variety Swarna stage flowering, stage_entered_at 2026-08-10,
  sowing_date 2026-06-10, stage_expires 2026-08-25, seed_stock
  {"kg":25,"elevated":false,"sealed":false}, livestock cattle 2,
  tenancy leased, labor_available 1, credit_access unknown,
  phone_type feature, consent enrolled_at 2026-08-10, opt_out false,
  deleted false, data_shared false.
- Bikash: farm_id highfield-002, district Kendrapara, block
  Pattamundai, phone 0000000002, language odia, members
  [{"name":"Bikash","role":"farmer"}], one plot (plot_id P1,
  lat 20.7421, lon 86.4189, elevation_m 6.5, elevation_source DEM,
  soil loam, soil_source TEST, drainage good, embankment strong,
  flood_history []), crops paddy variety Swarna-Sub1 stage maturity,
  stage_entered_at 2026-08-01, sowing_date 2026-05-15, stage_expires
  2026-08-20, seed_stock {"kg":60,"elevated":true,"sealed":true},
  livestock cattle 4 + goat 2, tenancy owned, labor_available 3,
  credit_access yes, phone_type smartphone, consent enrolled_at
  2026-08-10, opt_out false, deleted false, data_shared false.
- Fani: incident_id fani-2019, cap_type Alert, source IMD, state
  CYCLONE_WARNING, issued_at 2019-05-03T00:00:00Z, valid_until
  2019-05-05T00:00:00Z, hazard {"type":"cyclone","wind_kmh":215,
  "rain_mm":0,"surge_m":1.5,"tide":"","river":""}, badge
  ODISHA-MEASURED, impact {"area_ha":108220,"loss_rs_cr":1304.58},
  label ARCHIVED.
- Yaas: incident_id yaas-2021, cap_type Alert, source IMD, state
  CYCLONE_WARNING, issued_at 2021-05-26T00:00:00Z, valid_until
  2021-05-28T00:00:00Z, hazard {"type":"surge","wind_kmh":140,
  "rain_mm":290,"surge_m":3.0,"tide":"full-moon","river":""}, badge
  ODISHA-MEASURED, impact {"surge_m_min":2.0,"surge_m_max":4.0,
  "rain_mm_chandbali":290,"full_moon_tide":true}, label ARCHIVED.
- Demo live: incident_id demo-2026, cap_type Alert, source
  SIMULATED, state CYCLONE_WARNING, issued_at 2026-08-16T09:00:00Z,
  valid_until 2026-08-17T09:00:00Z, hazard {"type":"compound",
  "wind_kmh":120,"rain_mm":200,"surge_m":1.0,"tide":"spring",
  "river":"Mahanadi"}, badge SCENARIO-ASSUMPTION, label SIMULATED.

### 4. backend/serve.py
stdlib ThreadingHTTPServer (pattern: scaffold/webapp/serve.py: JSON
helpers, route dispatch, Content-Type application/json, no auth for
the demo). Endpoints:
  GET  /health                          -> {"ok":true}
  GET  /api/farms                       -> {"data":[...],"total":N}
  GET  /api/farms/{farm_id}             -> {"data":{...}}
  POST /api/farms                       -> 201 {"data":{...}} (validates required fields, 400 + missing list otherwise)
  DELETE /api/farms/{farm_id}           -> tombstone (deleted true, event appended), 200 {"data":{...}}
  GET  /api/incidents                   -> {"data":[...],"total":N}
  GET  /api/incidents/{incident_id}     -> {"data":{...}}
  POST /api/incidents                   -> create (validates state enum)
  PATCH /api/incidents/{id}/state       -> body {"state":...}, validates enum, appends event
  GET  /api/actions                     -> {"data":[...],"total":N}
  GET  /api/actions/{action_id}         -> {"data":{...}}
  POST /api/actions                     -> create (validates phase, grade, badge)
  POST /api/actions/{id}/deliver        -> dispatch via adapter stub, returns receipt, label SIMULATOR
  POST /api/actions/{id}/ack            -> mark the action's current delivery acknowledged
  POST /api/actions/{id}/escalate       -> next rung down, creates new delivery, label SIMULATOR
  GET  /api/claims                      -> {"data":[...],"total":N}
  GET  /api/claims/{claim_id}           -> {"data":{...}}
  POST /api/claims                      -> create
  GET  /api/claims/{id}/export          -> {"data":{"text":...,"images":[...],"printable":...},"formats":["text","images","printable"]}
  GET  /api/deliveries                  -> {"data":[...],"total":N}
  GET  /api/deliveries/{delivery_id}    -> {"data":{...}}
  POST /api/deliveries/{id}/ack         -> acknowledged (appends event)
  POST /api/deliveries/{id}/escalate    -> next rung down (same semantics as action escalate)
  GET  /api/events?limit=50             -> latest events (append-only view)
  GET  /api/events/verify               -> {"data":{"ok":true|false,"chain_length":N,"broken_at":null|seq}}
  GET  /api/rules                       -> {"data":[...],"total":16}
  GET  /api/rules/{rule_id}             -> {"data":{...}}
  GET  /api/research?q=...              -> {"data":[...],"total":N} (case-insensitive substring across report/what/feeds/wave/id)
  GET  /api/research/{id}               -> {"data":{...}}
  POST /api/cap/ingest                  -> canned CAP-style JSON in, incident out, label "CACHED SAMPLE"
Validation errors: 400 {"error": "..."}. Unknown ids: 404 {"error":
"..."}. Every POST/PATCH appends a chained event.

### 5. backend/adapters.py (SMS/IVR/USSD stubs, label SIMULATOR)
- RUNG_ORDER = ["app","sms","ivr","ussd","radio","village"].
- send(rung, action, farm, threshold_seconds=3600): creates a
  delivery row (delivery_id like DLV-<uuid4 hex[:8]>), status sent,
  receipt = "SIMULATOR receipt: <action_id> via <rung> to
  <phone/farm_id> at <ts>", returns the delivery dict. Idempotency:
  the caller may pass delivery_id in the body; if that delivery_id
  already exists, return the existing row, append NO new row and NO
  duplicate event (S8).
- acknowledge(delivery_id): status acknowledged, acked_at, event
  appended. Escalation timer semantics: only deliveries with status
  sent (not acknowledged) can escalate.
- escalate(delivery_id): if rung is "village", return {"ok":false,
  "reason":"terminal rung"} (no rung below). Else create a new
  delivery for the same action on the next rung, parent_delivery_id
  set, the old delivery status set to escalated, events appended for
  both, return the new delivery. Thresholds are stored per delivery
  (threshold_seconds) and also exposed: GET /api/deliveries includes
  "escalation_due_at" = sent_at + threshold_seconds for non-acked.
- ack stops escalation for that delivery; escalate after ack returns
  409 {"error":"already acknowledged"}.

### 6. backend/cap_ingest.py (label CACHED SAMPLE)
- Accepts a canned CAP-style JSON: {"identifier","msgType":
  "Alert|Update|Cancel|Ack|Error","sent","expires","status",
  "info":{"event","urgency","severity","certainty","onset","expires",
  "areaDesc","parameter":[{"valueName","value"}]}}.
- Maps: msgType -> cap_type (Alert/Update/Cancel/Ack/Error), event
  text -> state (CYCLONE -> CYCLONE_WARNING when certainty Likely or
  higher, FLOOD -> POST_LAND_FALL_OUTLOOK or IMPACT_SUSPECTED by
  severity, MONITOR default), parameter wind/rain/surge -> hazard
  fields, areaDesc -> district hint, sent/expires -> issued_at/
  valid_until, badge SCENARIO-ASSUMPTION (canned sample, not a live
  feed). Creates the incident, appends the event, returns
  {"data":{...incident...},"label":"CACHED SAMPLE"}.
- Ships with one canned sample CAP JSON in backend/seed/cap_sample.json
  (a cyclone alert for coastal Odisha districts).

### 7. backend/postgres_schema.sql (ROADMAP, NOT executed, ships only)
- Full DDL mirroring the SQLite schema for Postgres 15+ with
  PostGIS (geometry(Point,4326) on plots, geography for farm
  locations) and TimescaleDB (events and sensor_series as
  hypertables). Include the farms table partitioned by district
  (C1 note). Top comment: "ROADMAP: contract ready, DB in Round 1.
  Not executed in the prototype (BUILD-MATRIX tier 2)." stdlib
  SQLite stays the demo store.

### 8. backend/tests.py (stdlib unittest, runnable: python3 backend/tests.py)
Builds a temp DB, seeds it, starts the server on an ephemeral port,
and asserts (15+ tests, order independent):
1. seed loads: 2 farms, 3 incidents, Fani carries 108220 ha and Rs
   1304.58 cr, Yaas carries 2-4 m surge and 29 cm Chandbali rain
2. farm_profile contract: POST /api/farms round-trips, GET returns
   every contract key
3. incident contract + state enum validation (bad state -> 400)
4. advisory_action contract round-trip with doability + badge
5. claim_packet round-trip + export returns text/images/printable
6. events chain verifies ok after seeding
7. tamper detection: UPDATE one event row's payload_json directly via
   sqlite3, verify now reports ok false with broken_at = that seq
8. adapter stub: deliver returns receipt + label SIMULATOR
9. idempotency: same delivery_id posted twice -> one delivery row
10. escalation: app -> sms -> ivr -> ussd -> radio -> village in
    order, each creating a delivery with parent link; village
    escalate returns ok false terminal
11. ack stops escalation (escalate after ack -> 409)
12. CAP ingest: POST canned sample -> incident created, label
    CACHED SAMPLE, cap_type mapped
13. /api/research returns >= 43 rows, q=cyclone filters, raw_paths
    non-empty
14. /api/rules returns exactly 16 rules R1..R16
15. DELETE farm -> tombstone, GET shows deleted true, event logged
16. every action in seed carries a badge from the four-badge enum
Tests must clean up (shut down the server thread, remove temp db).

## SEED RULES (R1-R16) - from research/raw/cnc-ps07-d41 report section 5.2
AUTHORITY NOTE: the core lane writes scaffold/agri/rules.json as the
compiler's source of truth (rules are data, IMPROVISED-ANSWERS S5).
This seed file is the DB mirror for the API, NOT the authority: give
seed/rules.json a top-level meta key {"authority":
"scaffold/agri/rules.json (core lane compiler input)",
"mirror": true, "note": "DB seed mirror, not the authority"} and keep
the 16 rule bodies identical to this brief.
Each entry: {"rule_id","name","source_practice","trigger","action",
"guardrail","source","grade","badge","canary_version":1}
R1 official-alert-lock (CPP): trigger "Valid IMD district or geofence
alert received", action "Repeat hazard type, location, issue time,
validity, and official action; notify village relay and extension
desk", guardrail "Never paraphrase a watch as a warning",
source "d41 [18] BDRCS CPP", grade A, badge TRANSFER-PRIOR
R2 redundant-last-mile (people-centered EWS + Ama Krushi): trigger
"Severe alert plus unacknowledged farmer message", action "Send
concise SMS; place Odia IVR call; retry; notify trusted village
contact; offer live agent", guardrail "No single channel reaches
everyone; record acknowledgment, not merely delivery", source "d41
[30] [25]", grade A, badge TRANSFER-PRIOR
R3 flood-safe-seed (Practical Action): trigger "Farm stores seed or
grain and forecast water may reach storage", action "Dry and label
seed; seal an inner container; move above predicted water; duplicate
a lot at a second safe site or community store", guardrail "Do not
claim jute sacks or earthen pots alone are floodproof", source "d41
[17]", grade A, badge TRANSFER-PRIOR
R4 livestock-movement-plan (FAO): trigger "Forecast route-cutoff time
approaching and safe shelter confirmed", action "Identify animals and
owners; move early by species order; carry fodder, medicines, and a
clean-water plan; confirm head count at destination", guardrail "No
universal fixed lead time; use route, species, daylight, handlers,
shelter capacity", source "d41 [27]", grade A, badge TRANSFER-PRIOR
R5 livestock-water-safety (post-flood guidance): trigger "Floodwater
contacted wells, troughs, manure, chemicals, or carcasses", action
"Block unsafe water; use tested or approved clean supply; monitor
animals; request veterinary help", guardrail "Floodwater can infect
animals", source "d41 [43]", grade A, badge TRANSFER-PRIOR
R6 submergence-tolerant-paddy (Swarna-Sub1): trigger "Preseason or
replanting decision; freshwater submergence risk; approved local seed
available", action "Offer Swarna-Sub1 or locally approved equivalent
with duration, seed availability, and district recommendation",
guardrail "Tolerates roughly two to three weeks of submergence; not a
salinity or wind solution", source "d41 [20] J-PAL India RCT", grade
A, badge ODISHA-MEASURED
R7 lodging-risk-varietal-score (Japan): trigger "Preseason variety
ranking for cyclone-prone block", action "Rank approved varieties by
lodging resistance, maturity, yield, and local trial performance",
guardrail "Research confirms typhoon-related lodging traits, not
automatic suitability of a Japanese variety", source "d41 [7]",
grade B, badge TRANSFER-PRIOR
R8 seasonal-floating-rice-pilot (Vietnam): trigger "Predictable slow
freshwater rise, appropriate land, long lead time, approved variety,
fish escape controls", action "Offer only as an extension-supervised
seasonal pilot", guardrail "Lower rice yield and hydrologic dependence
must be disclosed; never activate for cyclone surge", source "d41
[31]", grade B, badge TRANSFER-PRIOR
R9 floating-vegetable-bed (Bangladesh baira): trigger "Prolonged
freshwater waterlogging, safe biomass, sheltered water, household
vegetable need", action "Provide a locally tested bed recipe,
anchoring, crop list, sanitation warning", guardrail "Do not recommend
invasive or contaminated hyacinth; Nigerian evidence shows harm in
aquaculture", source "d41 [39] [26]", grade B, badge TRANSFER-PRIOR
R10 raised-bed-perimeter-drainage (chinampa/waru waru): trigger
"Recurrent shallow waterlogging; suitable soil and outlet; non-paddy
vegetable or nursery plot", action "Raise the root zone, route water
through maintained channels, stabilize edges, inspect after heavy
rain", guardrail "Dimensions require Odisha trials", source "d41
[37] [33]", grade B, badge TRANSFER-PRIOR
R11 flood-recession-sowing-gate (Cambodia/Mali): trigger "Water level
falling; field accessible; soil wet but workable; salinity and
contamination acceptable; crop can mature before next hazard", action
"Recommend approved short-duration crop and sowing window",
guardrail "Never advise solely because satellite water area shrank",
source "d41 [1] [13]", grade B, badge TRANSFER-PRIOR
R12 drain-pond-integration (China/Australia): trigger "Existing
freshwater pond and field drainage can be safely connected", action
"Capture manageable drainage, prevent fish escape, reuse only after
water-quality and overflow checks", guardrail "Agrichemical and
disease risks require local limits", source "d41 [36] [35]", grade B,
badge TRANSFER-PRIOR
R13 community-tank-maintenance (Sri Lanka/subak): trigger "Pre-monsoon
inspection or blocked community drainage detected", action "Assign
desilting, gate, bund, culvert, and outlet tasks to named water-user
groups; log completion", guardrail "Major works need engineers and
permits", source "d41 [12] [2]", grade B, badge TRANSFER-PRIOR
R14 controlled-overflow-corridor (Room for the River): trigger
"District hydrologic plan identifies safe storage or conveyance
land", action "Protect drainage corridors and designated overflow
zones from obstruction; trigger authority action, not individual
farmer action", guardrail "Requires compensation, land-use authority,
hydraulic modeling", source "d41 [32]", grade C, badge TRANSFER-PRIOR
R15 post-flood-damage-to-assistance (USDA): trigger "Alert expires and
authorities declare access safe", action "Photograph and geotag crop,
seed, livestock, pond, bund, fence, and drainage damage; triage
contamination; clear debris safely; restore drainage; route claims and
input support", guardrail "Mirrors the recovery sequence of debris,
banks, drainage, structures, reseeding", source "d41 [29]", grade A,
badge TRANSFER-PRIOR
R16 evidence-quarantine (noise log): trigger "Retrieved practice lacks
source, mechanism, hazard fit, or local approval", action "Show
research lead, no farmer advisory, to administrators; send nothing to
farmers", guardrail "Prevents unsupported labels from becoming
dangerous instructions", source "d41 noise log", grade A, badge
TRANSFER-PRIOR

## SEED ACTIONS (two-farm contrast on demo-2026, in seed/actions.json)
For Asha (asha-001, flowering paddy, weak embankment, leased, labor
1): A-ASHA-1 phase pre, action "Move seed stock above predicted water
and seal it; move cattle to high ground by 6pm", deadline
2026-08-16T18:00:00Z, source rule-R3, grade A, cost_of_waiting "Seed
and cattle loss if water reaches storage", badge TRANSFER-PRIOR,
doability {"labor_hours":2,"cost_rs":0,"credit_needed":false,
"tenancy_ok":true,"feasible":true,"infeasible_reason":null},
delivery {"rung":"sms","status":"queued","delivery_id":null},
obsolete_after 2026-08-16T20:00:00Z. A-ASHA-2 phase pre, action "Do
not harvest yet: flowering paddy loses yield if cut early; drain plot
channels", source report-d32, grade C... make grade B, cost_of_waiting
"Partial harvest loss if flood hits", badge TRANSFER-PRIOR, doability
{"labor_hours":1,"cost_rs":0,"credit_needed":false,"tenancy_ok":
true,"feasible":true,"infeasible_reason":null}.
For Bikash (highfield-002, mature Swarna-Sub1, strong embankment,
owned, labor 3): A-BIKASH-1 phase pre, action "Harvest now: crop is
at maturity, labor 3 available, 5.76% early-harvest cost is below
expected flood loss", deadline 2026-08-16T14:00:00Z, source report-d32
+ rule-R6, grade A, cost_of_waiting "Up to 100% crop loss if the
embankment is overtopped", badge TRANSFER-PRIOR, doability
{"labor_hours":24,"cost_rs":1200,"credit_needed":false,"tenancy_ok":
true,"feasible":true,"infeasible_reason":null}, delivery
{"rung":"app","status":"queued","delivery_id":null}. A-BIKASH-2 phase
pre, action "Confirm stage via IVR keypad: maturity assumed, press 1
to confirm", source report-d4, grade B, cost_of_waiting "Wrong-stage
advisory if unconfirmed", badge UNKNOWN, doability {"labor_hours":0,
"cost_rs":0,"credit_needed":false,"tenancy_ok":true,"feasible":true,
"infeasible_reason":null}.

## HARD RULES
- SCOPE LOCK: never read, write, or search anything outside
  ~/krishisetu. The scaffold repo ~/craft-n-code is OFF-LIMITS and any
  attempt to read it will be auto-rejected and KILL this run. You do
  not need it: the serve.py pattern is described here. Implement the
  HTTP server with stdlib http.server: ThreadingHTTPServer +
  BaseHTTPRequestHandler, a JSON response helper (json.dumps, Content-
  Type application/json, status codes), route dispatch by parsing
  self.path with urllib.parse. No framework, no Flask.
- All code stdlib only. No new dependencies. SQLite + http.server.
- No em dashes anywhere (use commas, periods, colons). No AI-tell
  words (delve, leverage, robust, synergy, seamless, furthermore,
  moreover, additionally, harness, unlock, streamline, notably,
  significantly, ultimately).
- Honesty labels in responses: SIMULATOR on adapter endpoints,
  CACHED SAMPLE on CAP ingest, SIMULATED on the demo incident. No
  real phone numbers, no real SMS, no live CAP fetch.
- Do NOT implement the math (CVaR, Monte Carlo replay, compiler
  matching): the core lane owns it. You provide storage and the API
  the engine reads and writes. Actions may carry doability and
  cost_of_waiting as data, but no loss math.
- Do NOT do UI work.
- Do NOT modify anything outside backend/ (the research files are
  read-only inputs). Do NOT touch other branches.

## VERIFY (before you report done)
- python3 backend/tests.py: all tests green (16 groups above)
- python3 -m py_compile on every backend python file
- grep -rn -- "-" backend/*.py for an em dash sequence returns nothing
  (the character U+2014, not hyphen); check with grep -P
- Start server with --seed on port 8100, curl /health,
  /api/farms, /api/incidents, /api/events/verify, /api/research,
  /api/rules, and one deliver + escalate, show the receipts
- Report: files created, test count, endpoint list, any deviation
  from this brief (deviations need an explicit reason comment)
