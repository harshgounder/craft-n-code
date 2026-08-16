# README-for-judges.md (KrishiSetu, Round 0, Team 511)

## What this is

KrishiSetu is a cyclone and flood resilient agriculture advisory system for
Odisha. A consented farm profile (crop, stage, plot, tenancy, labor) joins
official IMD signals, and a rule engine compiles crop-stage-specific actions,
each with a deadline, a source, a cost of waiting, and a doability check.
Advisories walk a degraded-mode delivery ladder (app, SMS, IVR, USSD, radio,
village volunteer), incidents track through 11 states, the engine validates
itself against replayed real events (Fani, Yaas), and a claims packet rides
the PMFBY 72-hour intimation window. Every number on screen wears one of four
evidence badges (ODISHA-MEASURED, TRANSFER-PRIOR, SCENARIO-ASSUMPTION,
UNKNOWN). The LLM renders; the audited rule engine decides.

This is a prototype. Every feed, channel and sensor stream is labeled
SIMULATED, SIMULATOR, SIMULATED STREAM or ROADMAP. Nothing is live.

## How to run it (two commands)

    cd krishisetu-backend && python3 serve.py --seed --port 8100
    cd scaffold && bash ./demo.sh

(bash runs the demo even if your unzip tool drops file permissions.)

Then open http://localhost:8137/static/krishi.html

(Optional: the generic scaffold landing page at http://localhost:8137/
is the kit's original UI. The KrishiSetu farmer UI and operator
console are the krishi.html page above.)

That is the whole demo. Python 3.11+ stdlib only, no pip installs, no venv,
no network, offline capable. The backend seeds SQLite with farms, incidents,
rules and the research index; the UI reads it on 8100 and serves on 8137.
If a port is busy, the runbook in this kit lists every fallback.

## What is in the zip

| Folder | What it is |
|---|---|
| scaffold/agri/ | advisory core: compiler, CVaR, replay, 11-state machine, claims, doability, R1-R16 rules |
| scaffold/webapp/ | farmer UI (krishi.html), operator console, offline service worker |
| krishisetu-backend/ | data layer: SQLite schema, 24-endpoint API, CAP ingest stub, SMS/IVR adapter stubs, hash-chained audit log |
| scaffold/tests/ | acceptance checks + eval, all green on this build |
| scaffold/deck/ | deck generator and build instructions |
| scaffold/demo-script.md | the 3-minute demo, beat by beat, with honesty lines |

## The evidence chain

Every claim in this deck traces: slide claim to proof ledger
(docs/packaging/PROOF-LEDGER-2026.md) to EVIDENCE-INDEX.md to the raw research
report to a named, dated source. 49 research reports back this prototype, all
in the repo. A claim without a chain does not ship. Known, stated limits: the
rule set is a curated seed awaiting agronomist review, the IMD feed and
telecom channels are simulated, and field testing is gated on a Round 1 pilot.

## Team 511

Harsh Gounder (lead, E&CE), Ayush Kharwar (engine and demo), Sujal Shukla
(deck and submission). Verified: 85/85 acceptance suites, 46/46 fixture
scenarios, replay validation against Fani (108,220 ha, Rs 1,304.58 crore of
assessed loss) and Yaas anchors.
