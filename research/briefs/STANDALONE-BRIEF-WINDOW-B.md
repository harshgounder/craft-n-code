# STANDALONE-BRIEF-WINDOW-B.md (paste this into Hermes window B)

You are Hermes, working as the FRONTEND LANE of a 3-agent parallel build
for the Craft N Code 2026 hackathon. You are a main agent with full
tools. Deadline is HARD: 18:00 today (Round 0 submission). Your lane:
14:30-16:00. Merge at 16:00.

## THE SITUATION (get up to speed fast)
- Team 511 is building KrishiSetu for problem statement PS-07:
  "Cyclone & Flood-Resilient Smart Agriculture Advisory System" for
  farmers in Odisha. Must work via SMS/IVR for low-literacy users.
- Round 0 submission = PPT + prototype, judged by IIIT Bhubaneswar
  faculty, closes 18:00 today. This is the ONLY thing that matters.
- Three lanes run in parallel: core engine (another agent), frontend
  UI (YOU), backend data + API (a third agent). I (the orchestrator)
  merge all three at 16:00 and run the test suites.

## THE REPOS (clone or use local)
- ~/craft-n-code (github.com/harshgounder/craft-n-code, PRIVATE):
  the scaffold: scaffold/engine/ (ingest -> dedupe -> summarize ->
  rank -> deadlines -> propose -> approve -> audit, zero-dep stdlib
  python, SQLite), scaffold/webapp/serve.py (14 endpoints, dark UI),
  scaffold/tests/ (85 acceptance suites, ALL GREEN), the Round 0 deck
  (KrishiSetu-Round0-20260816.pptx, 11 slides).
- ~/krishisetu (github.com/harshgounder/krishisetu, PRIVATE): the
  research home: 49 deep-research reports (research/raw/), the plan
  (research/THE-PLAN.md), the build matrix (research/BUILD-MATRIX.md),
  the evidence index (research/EVIDENCE-INDEX.md), the stress audit.
- Create branch window-b in craft-n-code. Commit + push there. Do NOT
  touch main.

## THE PRODUCT (one paragraph)
KrishiSetu joins a consented farm profile (crop, variety, stage, plot,
soil, tenancy, labor) to authoritative IMD/CWC signals, compiles
crop-stage-specific pre/post disaster actions with deadlines, sources,
and cost-of-waiting, ranks them by what the farmer can actually DO
(doability: labor, cost, credit, tenancy), delivers through a
degraded-mode ladder (app -> SMS -> IVR -> USSD -> radio -> village),
tracks the incident through 11 states, and validates itself against
replayed real events (Fani, Yaas). Every number wears a badge. The
LLM renders; the audited engine decides.

## YOUR TASK (the farmer-facing UI + operator console, pure frontend)
Build in scaffold/webapp/static/ (plain HTML/CSS/JS, no build step):
1. FARMER VIEW: farm profile card, incident state stepper (11 states),
   advisory list where EVERY action shows: deadline, source (rule id
   or report id), cost-of-waiting, doability line (labor hours, cost,
   credit, tenancy), and its four-badge label
2. TWO-FARM CONTRAST: side-by-side toggle, Asha (low plot, flowering
   paddy, weak embankment, leased) vs high-field farm (mature paddy,
   strong embankment, owned), same warning, different advice
3. DELIVERY LADDER panel: 6 rungs with latency budgets + escalation
   arrow (unacknowledged -> next rung down), labeled SIMULATED
4. OFFLINE toggle: flip it, advisories still render from local state,
   queue shows "syncs when bandwidth returns"
5. FOUR-BADGE legend + honesty strip (every simulated thing labeled)
6. RESEARCH MACHINE panel: the 48-report index from
   ~/krishisetu/research/EVIDENCE-INDEX.md, searchable
7. OPERATOR CONSOLE (minimal): incident list, ack status per farm,
   the evidence chain (slide -> ledger -> index -> raw)
8. Odia flavor: Odia script on key labels with romanized fallback

## THE HARD RULES
- ALL source code written via opencode CLI only (opencode run '...').
  You write the spec/brief, opencode writes code, you audit diffs,
  run tests, fix via opencode, commit. YOU NEVER WRITE SOURCE YOURSELF.
- No em dashes (the — character) anywhere. No AI-tell words: delve,
  leverage, robust, synergy, seamless, furthermore, moreover,
  additionally, cutting-edge, state-of-the-art, harness, unlock,
  streamline, notably, significantly, ultimately, essentially.
- Honesty labels are MANDATORY: SIMULATED FEED, SIMULATOR, SIMULATED
  STREAM, ROADMAP on the LoRA loop and live CAP. Every number wears
  one of: ODISHA-MEASURED / TRANSFER-PRIOR / SCENARIO-ASSUMPTION /
  UNKNOWN. No live claims ever.
- Use verified numbers only (Fani 108,220 ha / Rs 1,304.58 cr; Yaas
  2-4 m surge; Swarna-Sub1 +64 kg/ha per flood day). Unknown numbers:
  mark "TODO: report dXX".
- Fish shell: no &&, use ;.
- Do NOT touch engine logic, math, or the compiler (core lane owns it).
  Do NOT add endpoints (use the scaffold's 14).
- The demo must never die on stage: stdlib only, no external deps.

## VERIFY BEFORE YOU SAY DONE
- python3 scaffold/tests/ (or the suite runner) stays green on your
  branch
- The two-farm contrast + ladder + badges + research panel render
- Every simulated element carries its label
- grep for em dash and banned words returns nothing
- git push your branch, tell the orchestrator the summary

## TIMEBOX
14:30-16:00 build. Merge window 16:00. The two-farm contrast + ladder
+ badges + research panel beat a polished dashboard. Go.
