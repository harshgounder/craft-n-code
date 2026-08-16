# BUILD-MATRIX.md: What Ships Today, What Is Placeholder, What Is Roadmap

Date: 2026-08-16 14:15. Deadline: 18:00 (3h45m). Three lanes, one merge.
Every component of the stack is classified: BUILD (ships in the 18:00
prototype), PLACEHOLDER (labeled stub in the prototype, roadmap tag in
the deck), ROADMAP (final version only, one deck slide). Each row has
the WHY, because the why is the analysis.

## THE RULE THAT DRIVES EVERY ROW
The prototype's job is to DEMO THE THESIS, not to be the product.
Faculty judges grade: idea depth, prototype, honesty, potential.
The thesis = doability + cascade math + replay validation + honesty.
Infrastructure impresses engineers; the thesis impresses faculty.
And the honesty contract forbids presenting a stub as real. So:
everything that CARRIES THE THESIS is built real; everything that is
PRODUCTION INFRASTRUCTURE is placeholder or roadmap, visibly labeled.

## THE FULL MATRIX

### TIER 1: BUILD NOW (the thesis carriers, ~2h core)
| Component | Why build | What it is |
|---|---|---|
| Advisory compiler + rule engine | The brain. R1-R16 registry as JSON data (the improvised-answers rule: rules are data, not code), stage x hazard x lead triggers | Pure JSON + matching, runs on the scaffold engine |
| Four badges | The honesty contract is the differentiation | Label on every number: ODISHA-MEASURED / TRANSFER-PRIOR / SCENARIO-ASSUMPTION / UNKNOWN |
| Farm profile (seeded) | The personalization premise: Asha + a high-field contrast farm | JSON profiles, DTMF-confirmable fields |
| Two-farm contrast | The judging demo: same warning, different advice | Config difference, one compiler |
| CVaR harvest decision | The math is real and small: wait vs partial vs immediate | Sample-based CVaR, labor + price inputs |
| Fani replay panel | The holy-shit moment: posterior vs 108,220 ha / Rs 1,304.58 cr | Monte Carlo (small), uncertainty band, real anchors |
| Incident state machine | The evolving advisory (11 states, CAP semantics) | State model in the engine |
| Doability layer | THE thesis: labor/cost/credit/tenancy on every action | Fields on each action object |
| Claims packet export | The rail: photo/voice/geo/72h/33% | Structured text + image export |
| Research machine panel | The credibility layer: 48 reports, searchable, evidence chain | Static index + search |
| Delivery ladder diagram | The multi-channel story, 4G-below + radio | Static visualization + per-rung labels |
| SMS/IVR simulators | Shows the delivery pattern honestly | Simulator with RECEIPT labels, no live sending |

### TIER 2: PLACEHOLDER (labeled stubs in the prototype + ROADMAP tag in deck)
| Component | Why placeholder | The label |
|---|---|---|
| Real SMS gateway + DLT | Needs registration + money + can't demo live sending | "SIMULATOR: DLT registration + gateway in Round 1" |
| Real IVR telephony | Needs a provider, calls cost | "SIMULATOR: telephony in Round 1" |
| Sensor hardware stream | Delivery takes days, one real node is a Round 1 buy | "SIMULATED STREAM: one real node in Round 1" |
| LoRA fine-tune loop | The on-device LLM story, GPU + data, rendering layer not brain | "ROADMAP: server-trained adapters, gated" |
| Live CAP RSS ingest | IMD CAP feed works but live demo is flaky on a laptop | "CACHED SAMPLE: live feed in Round 1" |
| Farm photo upload + CV | Phone photo pipeline is Round 1 (permission UX) | "STUB: photo intake in Round 1" |
| Operator auth + signed messages | Local demo does not need it; the DESIGN is documented | "ROADMAP: signed + audited in Round 1" |
| Postgres/PostGIS/Timescale | SQLite serves the demo; the schema design ships in the contract | "ROADMAP: contract ready, DB in Round 1" |
| PWA service worker + IndexedDB | The webapp runs locally; offline story is SIMULATED in demo | "ROADMAP: offline-first PWA in Round 1" |

### TIER 3: ROADMAP ONLY (one deck slide, never in the prototype)
| Component | Why roadmap | The deck line |
|---|---|---|
| The full cascade DAG + dynamic BN | The prototype shows CVaR + replay (real); full graph is the Round 1 build | "typed DAG, BN, MC convergence gates: Round 1" |
| Odia TTS + real ASR | IndicF5 exists but integration is a project | "IndicF5 Odia TTS: Round 1" |
| Data cooperative rails | Needs pilots + partners | "data cooperative: pilot-gated" |
| Who-pays full ladder | The rails exist as research; live integration is Round 2 | "ATMA 60:40, PMFBY earmark: Round 2" |
| Nationwide rule packs | Round 3 scope | "one rail, one pilot, one quarter" |

## THE WHY, DEEPER (the analysis behind the tiers)
1. WHY the thesis carriers are all small: a rule compiler over JSON, a
   sample CVaR, a small MC replay: each is 30-90 min of opencode work.
   The scaffold engine already provides ingest, dedupe, rank, propose,
   approve, audit, trace: the brain's chassis exists (85/85 + 46/46).
2. WHY placeholders over half-builds: a half-real SMS gateway looks
   broken; a labeled simulator looks deliberate. Honesty is the brand.
3. WHY the deck carries the roadmap, not the prototype: the judges see
   the prototype in minutes. The deck is where the final version
   exists: one architecture slide, every node tagged. "This is the
   final shape; the prototype demonstrates the core honestly."
4. WHY no new infra in the prototype: the zero-dep rule (stdlib only)
   means the demo cannot die on stage. Postgres on a laptop is a risk
   with zero judging upside.
5. WHY Window B and C exist: the UI (Odia low-literacy flows) and the
   data layer (schema + API + adapters) are genuinely parallel to the
   engine core. Three lanes, clean seams, one merge, 30-min buffer.

## THE MERGE PROTOCOL (16:00-16:30)
1. Window B pushes to branch window-b, Window C to window-c
2. I audit both against the contract + the honesty labels
3. Merge into main, run the scaffold suites (85/85 + 46/46) + eval
4. Fix + polish + rehearse the demo arc
5. 17:30 hard stop, 17:45 submit buffer
