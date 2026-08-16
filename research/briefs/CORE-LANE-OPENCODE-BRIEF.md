# CORE-LANE-OPENCODE-BRIEF.md (this window's lane, executed via opencode)

GOAL: build the KrishiSetu core into the scaffold: advisory compiler
(R1-R16 rule registry as JSON data + matcher), CVaR harvest decision,
Fani replay panel (small Monte Carlo), the 11-state incident machine,
doability fields, claims packet export, research machine index.
Runs on the existing scaffold engine (scaffold/ in ~/craft-n-code).
Zero-dep stdlib python + SQLite. No new infra.

## CONTEXT
- The scaffold: scaffold/engine/engine.py (Item dataclass, ingest,
  dedupe, summarize, rank, deadlines, propose, approve, audit via
  approval.py, trace ring buffer), scaffold/webapp/serve.py (14
  endpoints, static UI), tests 85/85 + eval 46/46 green.
- The rules are DATA, not code (IMPROVISED-ANSWERS S5): JSON registry,
  versioned, shadow-run capable.
- The 11 states: MONITOR, PRE_CYCLONE_WATCH, CYCLONE_ALERT,
  CYCLONE_WARNING, POST_LAND_FALL_OUTLOOK, IMPACT_SUSPECTED,
  IMPACT_CONFIRMED, RESPONSE, RECOVERY, NEXT_SEASON, CLOSED.
  CAP semantics: update, never duplicate. RECOVERY feeds NEXT_SEASON.
  Never closes on first recession.
- The R1-R16 registry (from the d41-refire report, research/raw/ in
  ~/krishisetu): R1 official-alert lock, R2 redundant last mile, R3
  flood-safe seed, R4 livestock movement plan, R5 livestock water
  safety, R6 submergence-tolerant paddy planning, R7 lodging-risk
  varietal score, R8 seasonal floating-rice pilot, R9 floating
  vegetable bed, R10 raised bed + perimeter drainage, R11 flood-
  recession sowing gate, R12 drain-pond integration, R13 community
  tank maintenance, R14 controlled overflow corridor, R15 post-flood
  damage-to-assistance, R16 evidence quarantine. Each rule: machine
  trigger, advisory action, guardrail, grade A/B/C.
- The four badges: ODISHA-MEASURED, TRANSFER-PRIOR,
  SCENARIO-ASSUMPTION, UNKNOWN. Every advisory number carries one.
- Calibration anchors: Fani 108,220 ha / Rs 1,304.58 cr, surge ~1.5 m;
  Yaas 2-4 m surge over full-moon tide, 29 cm rain at Chandbali.
- Swarna-Sub1: +64 kg/ha per flood day, ~718 kg/ha under severe
  submergence, 180 kg/ha neutral when no flood.
- Early harvest: 5.76% cost (32-study meta); harvest window 45-55 days
  after heading; delayed harvest loss 5-11.41%; tillering rice: no
  loss <4 days inundation, 80% at 6 days. Salinity: 1.9 dS/m + 9.1%
  per dS/m (TRANSFER-PRIOR). Waterlogging: 32.9% global prior.
- CVaR: a* = argmin CVaR_95(total loss|a) + cost(a) + infeasibility(a).

## BUILD (files in scaffold/, branch core-lane)
1. scaffold/agri/rules.json: the R1-R16 registry as pure JSON data,
   each rule with: id, trigger (hazard x crop x stage x lead), action
   template, deadline logic, source, grade, badge, guardrail.
2. scaffold/agri/compiler.py: matcher: farm profile + incident state
   -> ranked action list (rank by expected-loss comparator + doability
   infeasibility penalty). Pure functions, no I/O.
3. scaffold/agri/cvar.py: sample-based 95% CVaR + the harvest decision
   (wait vs partial vs immediate) with labor + price + action cost.
4. scaffold/agri/replay.py: small Monte Carlo for Fani: propagate
   hazard uncertainty -> district crop loss posterior, compare against
   the real anchors, uncertainty band. Convergence: pilot + main,
   stop on precision gate.
5. scaffold/agri/state_machine.py: the 11-state incident machine with
   CAP semantics, severity batching, never-close-on-first-recession.
6. scaffold/agri/claims.py: claim packet builder (intimation 72h,
   33% threshold, evidence list, export as text + images + printable).
7. scaffold/agri/doability.py: feasibility scoring per action
   (labor_hours, cost_rs, credit_needed, tenancy_ok, feasible,
   infeasible_reason).
8. scaffold/agri/research_index.py: the 48-report index (from
   ~/krishisetu/research/EVIDENCE-INDEX.md) as searchable JSON.
9. scaffold/agri/seed.py: Asha + high-field farm profiles, Fani/Yaas
   incident archives, sample advisories.
10. scaffold/tests/test_agri.py: acceptance tests: compiler matches
    the two-farm contrast, CVaR picks harvest under flood risk and
    wait under low risk, replay posterior covers the real anchor,
    state machine transitions correct, claims packet gates work,
    badges present on every action. Target 15+ tests, all green,
    order-independent.

## HARD RULES
- JSON rules are data: versioned, never code.
- No fabricated numbers: TRANSFER-PRIOR / UNKNOWN badges where the
  evidence is not Odisha-measured. No invented Gumbel theta, no
  flood->pest deterministic rules.
- No em dashes anywhere in code or comments. No AI-tell words.
- stdlib only. SQLite. No new deps.
- All output honest: SIMULATED labels on feeds, simulators, streams.

## VERIFY (before done)
- python3 scaffold/tests/ (or suite runner) all green incl. new test_agri
- Two-farm contrast: same incident, different actions
- Replay: posterior band contains 108,220 ha (or explains why not)
- grep -r for em dash in new files returns nothing
- git commit + push branch core-lane
