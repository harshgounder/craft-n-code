# STANDALONE-BRIEF-WINDOW-C.md (paste this into Hermes window C)

You are Hermes, working as the BACKEND + DATA LANE of a 3-agent parallel
build for the Craft N Code 2026 hackathon. You are a main agent with
full tools. Deadline is HARD: 18:00 today (Round 0 submission). Your
lane: 14:30-16:00. Merge at 16:00.

## THE SITUATION (get up to speed fast)
- Team 511 is building KrishiSetu for problem statement PS-07:
  "Cyclone & Flood-Resilient Smart Agriculture Advisory System" for
  farmers in Odisha. Must work via SMS/IVR for low-literacy users.
- Round 0 submission = PPT + prototype, judged by IIIT Bhubaneswar
  faculty, closes 18:00 today. This is the ONLY thing that matters.
- Three lanes run in parallel: core engine (another agent), frontend
  UI (a third agent), backend data + API (YOU). I (the orchestrator)
  merge all three at 16:00 and run the test suites.

## THE REPOS (clone or use local)
- ~/krishisetu (github.com/harshgounder/krishisetu, PRIVATE): the
  research home: 49 deep-research reports (research/raw/, files named
  cnc-ps07-d1..d47), the plan (research/THE-PLAN.md), the build matrix
  (research/BUILD-MATRIX.md), the evidence index
  (research/EVIDENCE-INDEX.md), improvised answers to 45 stress-test
  gaps (research/IMPROVISED-ANSWERS.md).
- ~/craft-n-code (github.com/harshgounder/craft-n-code, PRIVATE): the
  scaffold: scaffold/engine/ (zero-dep stdlib python, SQLite,
  ingest -> dedupe -> summarize -> rank -> deadlines -> propose ->
  approve -> audit -> trace), scaffold/webapp/serve.py (14 endpoints).
- Work in ~/krishisetu on branch window-c. Commit + push there. Do NOT
  touch main.

## THE PRODUCT (one paragraph)
KrishiSetu joins a consented farm profile (crop, variety, stage, plot,
soil, tenancy, labor) to authoritative IMD/CWC signals, compiles
crop-stage-specific pre/post disaster actions with deadlines, sources,
and cost-of-waiting, ranks them by what the farmer can actually DO
(doability: labor, cost, credit, tenancy), delivers through a
degraded-mode ladder (app -> SMS -> IVR -> USSD -> radio -> village),
tracks the incident through 11 states, and validates itself against
replayed real events (Fani, Yaas). Every number wears a badge.

## YOUR TASK (data layer + API + adapter stubs, contract-first)
Implement EXACTLY this JSON contract. These shapes are what the other
lanes read and write. No deviations without a comment.

### farm_profile
{"farm_id","district","block","phone","language":
 "odia|hindi|english","members":[{"name","role"}],
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
1. SQLite schema (stdlib sqlite3) for: farms, plots, crops, incidents,
   actions, deliveries, claims, events. The events table is
   APPEND-ONLY with a hash column chaining events (tamper = hash
   mismatch alarm, per IMPROVISED-ANSWERS D1).
2. REST API as a stdlib python server (pattern: the scaffold's
   serve.py): /api/farms, /api/incidents, /api/actions, /api/claims,
   /api/deliveries, /api/events, /api/research (the 48-report index
   from EVIDENCE-INDEX.md).
3. SMS/IVR/USSD adapter STUBS: record delivery status, return a
   simulated receipt, carry delivery_id (idempotency) and the
   escalation rule: unacknowledged after threshold -> next rung down
   the ladder (app -> sms -> ivr -> ussd -> radio -> village).
   Labeled SIMULATOR.
4. CAP ingest STUB: parse a canned CAP-style JSON into an incident.
   Labeled CACHED SAMPLE.
5. Seed data: Asha (low plot, flowering paddy, weak embankment,
   leased, labor 1) + high-field farm (mature paddy, strong
   embankment, owned, labor 3); Fani (108,220 ha, Rs 1,304.58 cr,
   surge 1.5 m) and Yaas (2-4 m surge over full-moon tide, 29 cm rain
   Chandbali) incident archives from the raws; the R1-R16 rule
   registry as JSON data from cnc-ps07-d41-global-farm-practices-
   refire.content.md (research/raw/).
6. postgres_schema.sql for the ROADMAP (Postgres + PostGIS +
   TimescaleDB migration, NOT executed, just ships).

## THE HARD RULES
- ALL source code via opencode CLI only. You write the spec, opencode
  writes code, you audit diffs, run tests, fix, commit.
- No em dashes anywhere. No AI-tell words (delve, leverage, robust,
  synergy, seamless, furthermore, moreover, additionally, harness,
  unlock, streamline, notably, significantly, ultimately).
- Honesty labels in API responses: SIMULATOR, CACHED SAMPLE,
  SIMULATED. Every record carries badge/source/grade per contract.
  No real SMS, no real telephony, no live CAP fetch.
- Do NOT implement the math (CVaR, Monte Carlo replay, compiler):
  the core lane owns it. You provide storage + API it reads/writes.
- Do NOT do UI work.
- Fish shell: no &&, use ;.

## VERIFY BEFORE YOU SAY DONE
- Your API serves the contract shapes with the seed data loaded
- The append-only events table hashes and detects a tamper
- The adapter stubs return receipts and escalate on non-ack
- grep for em dash and banned words returns nothing
- git push branch window-c, tell the orchestrator the summary

## TIMEBOX
14:30-16:00 build. Merge window 16:00. Schema + API + seed data beat
polish. Go.
