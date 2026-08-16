# WINDOW-B-BRIEF.md: Frontend + Offline UX Lane (for the parallel Hermes window)

GOAL: build the farmer-facing UI + operator console for the KrishiSetu
prototype. Pure frontend. Zero engine logic. Build against the scaffold's
existing endpoints only. Everything labeled per the honesty policy.

## CONTEXT (read first)
- Repo: ~/craft-n-code (scaffold/ has the zero-dep engine + webapp)
  and ~/krishisetu (research docs, raws, THE-PLAN.md, BUILD-MATRIX.md)
- The scaffold webapp: scaffold/webapp/serve.py + static/index.html,
  14 endpoints, dark UI. This is the chassis.
- Product: KrishiSetu, cyclone/flood agriculture advisory for Odisha.
  Low-literacy Odia farmers on ANY phone, degraded-mode delivery
  ladder (app -> SMS -> IVR -> USSD -> radio -> village).
- Honesty policy (hard): every number wears one of four badges
  (ODISHA-MEASURED / TRANSFER-PRIOR / SCENARIO-ASSUMPTION / UNKNOWN).
  Every placeholder is labeled. No em dashes anywhere. No AI-tell
  words (delve, leverage, robust, synergy, seamless, etc).
- The demo arc: Asha (flowering paddy, low plot) vs a high-field farm.
  Same cyclone warning, different advice. Odia text, DTMF-style
  confirmations, offline fallback, claims packet.

## BUILD (what this lane owns)
1. FARMER VIEW (the Asha screen): farm profile card (crop, stage,
   plot, soil, phone type), current incident state (the 11-state
   machine as a visual stepper), the advisory list: each action with
   deadline, source, cost-of-waiting, doability line (labor hours,
   cost, credit, tenancy flag), and its four-badge label.
2. THE TWO-FARM CONTRAST: a side-by-side toggle: Asha (low plot,
   flowering paddy, weak embankment) vs high-field farm (mature paddy)
   under the same warning. Different actions, visible in one click.
3. THE DELIVERY LADDER panel: the 6-rung ladder (app -> SMS -> IVR ->
   USSD -> radio -> village) as a visualization, with per-rung latency
   budgets and the escalation arrow ("unacknowledged -> escalates
   down"). Label: SIMULATED in this prototype.
4. OFFLINE MODE toggle: flip it, the advisory list still renders from
   local state, the queue shows "syncs when bandwidth returns".
5. THE FOUR-BADGE legend + the honesty strip: every simulated thing is
   labeled (feed, SMS, IVR, sensor stream, LoRA loop).
6. RESEARCH MACHINE panel: the 48-report index, searchable list (titles
   from EVIDENCE-INDEX.md), each row links to the raw path. This is
   the credibility layer for judges.
7. OPERATOR CONSOLE (minimal): incident list, per-farmer ack status,
   the evidence chain (slide -> ledger -> index -> raw) visible.
8. Odia flavor: Odia script on key labels (harvest, flood, cyclone,
   seed, water), romanized fallback. No full translation needed, the
   VOICE is the Odia story.

## HONESTY LABELS (hard requirements)
- "SIMULATED FEED" on the hazard input
- "SIMULATOR" on SMS and IVR traces
- "SIMULATED STREAM" on sensor data
- "ROADMAP" on the LoRA loop and the live CAP feed
- Every number carries one of the four badges
- No claim of live sending, live calls, or real sensors

## CONTRACT (what you may NOT do)
- No changes to engine logic, rules, or math: the compiler, CVaR,
  replay, state machine are THIS window's (the core lane) work
- No new backend endpoints: use the scaffold's 14
- No build tooling beyond what the scaffold uses (stdlib python, no
  npm build step required: plain HTML/CSS/JS in static/)
- No em dashes, no AI-tell words, no invented numbers: pull numbers
  from the research docs (Fani 108,220 ha / Rs 1,304.58 cr, Yaas
  2-4 m surge, Swarna-Sub1 +64 kg/ha per flood day, etc) or leave a
  "TODO: number from report dXX" marker

## DELIVERABLE
A branch window-b with the UI files, committed, pushed to
github.com/harshgounder/craft-n-code. One-page summary at the end:
what you built, what you labeled, what you left TODO.

## TIMEBOX
14:30-16:00. Merge window opens 16:00. Do not gold-plate: the two-farm
contrast + ladder + badges + research panel beat a polished dashboard.
