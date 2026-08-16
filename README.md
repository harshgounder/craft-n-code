# KrishiSetu

Cyclone and flood resilient smart agriculture advisory system for coastal
Odisha. Craft N Code 2026, PS-07, Team 511.

A cyclone forecast becomes a crop-stage decision: an action, a deadline, a
source, and a fallback, in Odia, on any phone.

Warnings are infrastructure. Decisions are the product.

## Where the AI is (and is not)

The decision core is deliberately deterministic: no LLM sits inside the
advice loop. Agronomy rules are a curated, cited seed set (R1-R18), and
the math is classical: CVaR, Monte Carlo with convergence gates, fragility
curves, a typed cascade graph. That is a design decision, not a gap.
LLMs hallucinate agronomy, and a farmer cannot afford a wrong answer.
Rules with citations beat vibes with confidence.

The AI layers are the delivery and sensing layer, built for Round 1, and
documented in EDGE-AI-VISION.md: on-device small LLM for conversational
Odia advisory on a phone hub, Odia ASR and TTS, photo-based damage
estimation for claim evidence, LoRA fine-tuning per district, all running
offline on the farmer's own device. The prototype proves the decision
core; Round 1 bolts on the voice.

The research base is deep: 49 reports across 7 waves with verification
gates, but the product never depends on a model to give advice. Every
number in this deck traces to a source you can open.

## The problem in one line

Farmers get warnings. They do not get decisions.

## What this is

An advisory engine, not an alert system. It takes a farm profile (crop,
stage, plot elevation, soil, tenancy, labor) and a hazard bulletin, then
issues staged actions ranked by what the farmer can actually execute:
harvest now or protect in place, move seed above the water line, brace the
banana, photograph the standing crop for the claim. Every action carries a
deadline, a source, a cost of waiting, and an evidence badge.

The cyclone and flood predictor is a backup layer that fires only when the
official warning never reaches the farm.

## Why it runs this way

Your constraints shaped it: minimize hardware, minimize API-key dependence,
work on 4G or less, self-dependent. The prototype is the honest minimum: a
decision engine plus UI that runs on any machine with Python 3.11+, no
installs, no network, no keys. All math is live on the CPU: the CVaR
harvest decision, the Fani replay band, the delivery ladder, the claim
packet.

## Run it (two commands)

```bash
cd krishisetu-backend && python3 serve.py --seed --port 8100
cd scaffold && bash ./demo.sh
```

Open http://localhost:8137. Python 3.11+ stdlib only, offline capable.

- backend on 8100: farms, incidents, actions, claims, hash-chained audit log
- UI on 8137: farmer view, operator console, two-farm contrast, research tab
- everything is simulated and labeled: SIMULATED feed, SIMULATOR delivery

## What is inside

| Folder | What it is |
|---|---|
| scaffold/agri/ | advisory core: 18-rule registry (R1-R18), compiler, CVaR, Fani replay, 11-state machine, claims, doability |
| scaffold/webapp/ | farmer UI (krishi.html), operator console, offline service worker |
| scaffold/engine/ | domain-agnostic engine: ingest, dedupe, rank, propose, approve, audit, trace |
| krishisetu-backend/ | SQLite schema, REST API, CAP ingest stub, SMS/IVR adapter stubs, hash-chained audit log |
| scaffold/deck/ | the 13-slide presentation (generator + built pptx) |
| research/ | 49 research reports, every claim traceable to a named dated source |

## The research

49 research reports across 7 waves, 3.2M chars of raw evidence, 4,800+
cited sources. Full ledgers of every cyclone and major flood with
agricultural damage (IBTrACS 1848-present, EM-DAT, Dartmouth Flood
Observatory). No phenomenon is treated as a static event: typed cascade
graphs, Monte Carlo with convergence gates, CVaR at every decision node,
fragility curves per crop and stage. Every number in the deck traces to a
source you can open: slide to proof ledger to EVIDENCE-INDEX.md to raw
report.

The counterfactual: Fani (108,220 ha, Rs 1,304.58 cr, 90h watch), Yaas
(5,882 ha salt-affected, 2-4 m surge), Dana (rapid assessment, 5,428
acres), 1999 (9,893 deaths with a 48h+ warning). The warning existed; the
decision did not.

## Honesty

- IMD feed is simulated, SMS and IVR run through simulators, agronomy rules
  are a curated seed set awaiting agronomist review
- every claim carries an evidence badge: ODISHA-MEASURED, TRANSFER-PRIOR,
  SCENARIO-ASSUMPTION, UNKNOWN
- nothing is labeled live that is not live
- no prevented-loss claims: the events are real, the engine output is what
  the product would issue, the replay validates against what happened

## Tests

```bash
cd scaffold/tests && for t in test_*.py; do python3 $t; done
cd ../krishisetu-backend 2>/dev/null; cd ../../krishisetu-backend && python3 tests.py
cd scaffold && python3 eval/eval.py --all
```

106 acceptance checks plus the backend suite and integration harness, all
green on the shipped build.

## Team 511

- Harsh Gounder: architecture, code, research method, backend, QA, devops
- Ayush Kharwar: presentation build and design
- Sujal Shukla: presentation design assistance

Craft N Code 2026, PS-07: Cyclone and flood resilient smart agriculture
advisory system.
