# WINDOW-C-BRIEF.md: Backend + Data Lane (for the parallel Hermes window)

GOAL: build the data layer + API + adapter stubs for KrishiSetu.
Contract-first: the JSON shapes below are the contract. Implement to
them exactly. No engine logic, no UI.

## CONTEXT (read first)
- Repo: ~/krishisetu (research, THE-PLAN.md, BUILD-MATRIX.md,
  EVIDENCE-INDEX.md) and ~/craft-n-code (scaffold/ with the engine)
- The prototype runs on SQLite + stdlib python (zero-dep rule).
  Postgres/PostGIS/Timescale is the ROADMAP: you design the schema,
  implement against SQLite, and ship the migration for Postgres as a
  .sql file (not executed).
- Honesty policy: every record carries source + grade + badge fields.
  No em dashes. No AI-tell words.

## THE CONTRACT (the JSON shapes everything speaks)

### farm_profile
{"farm_id": "string", "district": "string", "block": "string",
 "phone": "string", "language": "odia|hindi|english",
 "members": [{"name": "string", "role": "farmer|household|other"}],
 "plots": [{"plot_id": "string", "lat": "float", "lon": "float",
   "elevation_m": "float", "elevation_source": "DEM|FARMER|UNKNOWN",
   "soil": "string", "soil_source": "TEST|NBSS-LUP|FARMER|UNKNOWN",
   "drainage": "good|poor|unknown", "embankment": "strong|weak|none|unknown",
   "flood_history": [{"year": "int", "depth_m": "float|unknown"}]}],
 "crops": [{"crop": "paddy|banana|coconut|vegetables|pulses|maize|other",
   "variety": "string", "stage": "seedbed|vegetative|flowering|grainfill|maturity|harvested|other",
   "stage_entered_at": "ISO-date", "sowing_date": "ISO-date|unknown",
   "stage_expires": "ISO-date"}],
 "seed_stock": {"kg": "float", "elevated": "bool", "sealed": "bool"},
 "livestock": [{"species": "cattle|buffalo|goat|poultry|other", "count": "int"}],
 "tenancy": "owned|leased|shared|unknown",
 "labor_available": "int", "credit_access": "yes|no|unknown",
 "phone_type": "smartphone|feature|shared|none",
 "consent": {"enrolled_at": "ISO-date", "opt_out": "bool", "deleted": "bool",
   "data_shared": "bool"}}

### incident (CAP-style, the 11-state machine)
{"incident_id": "string", "cap_type": "Alert|Update|Cancel|Ack|Error",
 "source": "IMD|CWC|INCOIS|LOCAL-SENSOR|SIMULATED",
 "state": "MONITOR|PRE_CYCLONE_WATCH|CYCLONE_ALERT|CYCLONE_WARNING|POST_LAND_FALL_OUTLOOK|IMPACT_SUSPECTED|IMPACT_CONFIRMED|RESPONSE|RECOVERY|NEXT_SEASON|CLOSED",
 "issued_at": "ISO-date", "valid_until": "ISO-date",
 "hazard": {"type": "cyclone|flood|surge|compound",
   "wind_kmh": "float", "rain_mm": "float", "surge_m": "float",
   "tide": "float", "river": "string"},
 "badge": "ODISHA-MEASURED|TRANSFER-PRIOR|SCENARIO-ASSUMPTION|UNKNOWN"}

### advisory_action (what the farmer gets)
{"action_id": "string", "incident_id": "string", "farm_id": "string",
 "phase": "pre|during|post|recovery|next-season",
 "action": "string", "deadline": "ISO-date|relative-string",
 "source": "rule-R1..R16|report-dXX", "grade": "A|B|C|D",
 "cost_of_waiting": "string", "badge": "string",
 "doability": {"labor_hours": "int", "cost_rs": "float",
   "credit_needed": "bool", "tenancy_ok": "bool", "feasible": "bool",
   "infeasible_reason": "string"},
 "delivery": {"rung": "app|sms|ivr|ussd|radio|village",
   "status": "queued|sent|delivered|acknowledged|escalated",
   "delivery_id": "string"},
 "obsolete_after": "ISO-date"}

### claim_packet
{"claim_id": "string", "farm_id": "string", "incident_id": "string",
 "intimation_72h": "bool", "loss_threshold_33": "bool",
 "evidence": [{"type": "photo|voice|text|geo", "path": "string"}],
 "status": "draft|ready|submitted|rejected|appealed",
 "export_formats": ["text", "images", "printable"]}

## BUILD (what this lane owns)
1. SQLite schema implementing the contract (tables: farms, plots,
   crops, incidents, actions, deliveries, claims, events) + the
   append-only events table with a hash column (the improvised-answer
   D1: tamper = hash mismatch).
2. REST API (stdlib python, extend the scaffold's serve.py pattern):
   /api/farms, /api/incidents, /api/actions, /api/claims,
   /api/deliveries, /api/events (audit), /api/research (48-report
   index from EVIDENCE-INDEX.md)
3. SMS/IVR/USSD adapter STUBS: functions that record delivery status
   and return a simulated receipt. Labeled SIMULATOR. Include the
   idempotency delivery_id and the escalation logic (unacknowledged
   -> next rung down).
4. CAP ingest STUB: parse a canned CAP-style JSON into an incident
   record. Labeled CACHED SAMPLE.
5. Seed data: two farms (Asha: low plot, flowering paddy, weak
   embankment, leased; High-field: mature paddy, strong embankment,
   owned), the Fani + Yaas incident archives (from d21/d22 raws in
   ~/krishisetu/research/raw/), the R1-R16 rule registry as JSON data
   (from the d41-refire report).
6. Postgres migration file (postgres_schema.sql) for the ROADMAP, not
   executed.

## HONESTY LABELS (hard)
- Every record has badge/source/grade where the contract says
- SIMULATOR / CACHED SAMPLE / SIMULATED labels in API responses
- No real SMS, no real telephony, no real CAP fetch

## CONTRACT VIOLATIONS TO AVOID
- No engine math (CVaR, replay, compiler): core lane owns it. You
  provide the storage + API they read/write.
- No UI work.
- No em dashes, no AI-tell words.

## DELIVERABLE
Branch window-c, committed + pushed to github.com/harshgounder/
krishisetu. One-page summary: schema, endpoints, stubs, seed data,
what is labeled, what is TODO.

## TIMEBOX
14:30-16:00. Merge window opens 16:00. Schema + API + seed data beat
polish.
