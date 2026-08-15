# PACKAGING-SYNTHESIS-2026 — the YC-seed-level packaging layer for Craft N Code

Written 2026-08-15 ~19:50 IST, pre-drop. Folds the full packaging research wave (15 parallel.ai runs, 2 DEEP, 13 ADECENT/MINED, 1,159 unique sources in the union). This is the evidence base for the startup-universe hackathon edition plan. Honest tags: VERIFIED (source-cited), INFERRED (cross-run convergence, no direct cite), WILDCARD (my reasoning, no evidence).

## 1. What this layer is

The judges see a complete seed-stage startup, not a hackathon project. The bar is YC level or above: the research targets were the best companies in the world (Apple, Stripe, Linear, Notion, Figma, Dropbox, Dollar Shave Club, YC guidance, Sequoia frameworks), not hackathon lore. The hackathon is only the deployment stage.

## 2. Honest run ledger (15 runs, scored by report-supervisor)

| Run | Verdict | Score | cite_d | chars |
|---|---|---|---|---|
| wave21-packaging-trailer-r2 | DEEP | 92.3 | 2.03 | 84,312 |
| wave24-product-story (v1) | DEEP | 89.2 | 1.07 | 46,896 |
| wave23-seed-presentation-r3 | MINED | 86.0 | 0.77 | 45,708 |
| wave23-seed-presentation-r5 | ADECENT | 79.4 | 0.50 | 74,076 |
| wave23-seed-presentation-final | ADECENT | 76.6 | 0.35 | 90,314 |
| wave19a-deck-materials-r5 | ADECENT | 74.9 | 0.52 | 69,207 |
| wave19-packaging-startup-r3 | ADECENT | 74.4 | 0.35 | 120,070 |
| wave19b-traction-diligence-r5 | ADECENT | 70.5 | 0.23 | 74,545 |
| wave19-packaging-startup-r4 | ADECENT | 61.2 | 2.38 | 15,153 |
| wave19-packaging-startup-r2 | ADECENT | 81.0 | 2.46 | 15,441 |
| wave19-packaging-startup (v1) | ADECENT | 73.3 | 0.36 | 50,230 |
| wave21-packaging-trailer (v1) | ADECENT | 81.2 | 0.44 | 48,197 |
| wave23-seed-presentation (v1) | ADECENT | 72.3 | 0.44 | 44,955 |
| wave23-seed-presentation-r2 | ADECENT | 80.0 | 0.41 | 92,075 |
| wave23-seed-presentation-r4 | ADECENT | 74.1 | 0.43 | 87,033 |

Two topics never cleared DEEP despite 6 attempts each (wave19, wave23): the pipeline delivers either dense-short or long-thin. The union of versions covers the ground; per-run stamps are honest as labeled above.

Evidence union: 1,159 unique URLs across the 15 reports (source ledger at /tmp/pkg-sources.json, raw reports in research/raw/).

## 3. The artifact map (startup-universe layers -> judge-facing artifacts)

- 00-founder -> TEAM page: who we are, what we already shipped (81/81 checks, verified trace, honest badges). Founder credibility = the first minute. VERIFIED.
- 01-problem -> PROBLEM page: one victim story, one number block, one sentence. "Every [user] loses [moment] when [old way]." (wave24 hook line). VERIFIED.
- 02-market -> MARKET page: TAM via rails, one rail one pilot one quarter. VERIFIED (r2 skeleton: market slide belongs after traction in YC's ordering; Sequoia adds why now + competition).
- 03-customer -> PILOT page: who adopts first, adoption language not literalism. INFERRED (SIH/prior-wave lesson, not in this wave's sources).
- 05-product -> PRODUCT page: the scaffold demo, one continuous workflow, zero-dep story. The repo IS evidence: README, CI, tests, clean-machine build, rollback path. VERIFIED (wave19b/r2: engineering diligence list).
- 12-ops-metrics -> TRACTION page: primary metric on a monthly timeline, cohort or retention where possible, honest 24h line (what a 24h build can and cannot prove). VERIFIED (r2 skeleton).
- 06-business-model -> MODEL page: one line per model (per seat, per event, per verified packet). VERIFIED (deck structure: business model slide).
- 13-research-loop -> MOAT page: the 7-stage approval queue, evidence panel, audit trace, prior-art map. VERIFIED (r2: insight or moat slide; Sequoia adds why now).
- ask -> seed framing: ask tied to next milestone, use of funds, clear. VERIFIED (DeckMatch negative example: ask disconnected from use of funds = fail).

## 4. Locked findings from the two DEEP reports

### 4.1 Why viewers believe a product is real (wave24, reality signals table)

| Signal | What it tells the viewer | Strong implementation |
|---|---|---|
| Continuous product state | The result follows from the action | Input, transition, output in one shot |
| Specific proof | The claim has boundaries | State period, cohort, denominator, status |
| Human source | Someone owns the claim | Founder speaks concretely |
| Visible limitation | The team knows the edge | Say what is manual, staged, beta |
| Third-party support | The claim can be checked | Link a customer, report, artifact |
| Consistent UI | The product is coherent | Match footage to current build, date the demo |

Counterweight: UGC outcredits agency polish in some studies; AI-generated ads show weaker memory activation. The rule: cinematic control for the promise, documentary continuity for the proof. Do not use synthetic media to impersonate customer evidence. VERIFIED.

### 4.2 The 90-second trailer script (wave24)

| Beat | Draft line | Visual evidence |
|---|---|---|
| Hook | Every [user] loses [moment] when [old way] | Real before state |
| Reframe | We built [product] for [job], not [feature] | Product in context |
| Mechanism | Here is the three-step path | Continuous screen capture |
| Proof | In [context], [specific result] | Source, number, live artifact |
| Difference | Instead of [old way], [product] keeps [benefit] visible | One contrast |
| Close | Try it at [URL], start with [one action] | Product and CTA |

The proof line must survive a skeptical screenshot. A cinematic teaser with zero product claims produces desire, not comprehension; Dropbox's jump (5,000 to 75,000 waitlist) came from an explanatory video. VERIFIED.

### 4.3 The three-minute live demo arc (wave24)

1. Hook: user, moment, cost in one breath. 2. Problem: show the old artifact. 3. Reveal: promise before opening the product. 4. Proof: one meaningful workflow input to result. 5. Differentiation: one thing the old way cannot do. 6. Close: current status, next action, one limitation. YC clear-and-concise is the governing constraint. VERIFIED.

### 4.4 Zero-budget production stack (wave24, verified against official sources)

OBS (screen), Descript (transcript editing, watermark-free exports claimed), DaVinci Resolve free / Kdenlive (edit), Audacity (audio), whisper.cpp + Subtitle Edit (offline captions), founder voice first (local OpenVoice only with consent), YouTube Audio Library (licensed music). Local path avoids upload latency and keeps customer data private. VERIFIED.

Six-hour production schedule anchor: message lock 30m, capture plan 30m, screen recording 45m, founder voice 30m, rough edit 90m, captions 30m, music 20m, motion graphics 40m, proof pass 20m, QC 30m, upload 25m. VERIFIED.

Minimum viable sequence (wave21): pain/product-shift/proof/CTA before recording; one clean workflow; edit pauses preserving labels; narration only where screen cannot carry it; human-checked captions; licensed music logged; export cutdowns. VERIFIED.

### 4.5 Launch film case studies (wave21, VERIFIED)

Dropbox: show the invisible mechanism. Dollar Shave Club: entertainment carries proof, founder becomes part of the story. Blendtec: repeatable test = evidence. Pebble/Flow Hive: participation = evidence. Apple: live proof + metaphor risk. The two-layer launch: story (audience, enemy, promise, future, identity) + proof packet (live URL, dated recording, working path, evidence, constraints, next action).

## 5. Seed package standards (wave19 runs, best evidence = r2/r4 dense skeletons)

- Deck: company + one-line purpose, problem, solution, traction, moat, business model, market, team, ask. YC: single title slide, concrete problem, concise solution, meaningful traction, founder-focused team, ask tied to next milestone. Sequoia adds why now + competition. 11-slide Airbnb arc as the canonical example. VERIFIED.
- One-pager: one page, vision/product/team/traction/market/financials/ask. Materials separated by sensitivity: forwardable snapshot, emailable deck, meeting deck, model, cap table, data room. VERIFIED.
- Traction: match company type and stage. SaaS seed heuristics ~$10K-25K MRR, sustained growth, multiple paying customers, cohort retention for consumer, technical de-risking for deep tech. No single gold standard. VERIFIED.
- Diligence: corporate/legal, team, product/IP, market, traction, financials, references. Red flag #1: unclean cap table. Repo evidence: history, issues, PRs, access controls, CI, Dependabot, license risk, key-person risk. VERIFIED.
- The honest 24h line: a 24h build proves core functionality, feasibility, early reaction. It cannot prove retention, repeatable revenue, unit economics, production security, completed legal. State that line yourself before anyone asks. VERIFIED.

## 6. What this means for tonight (artifact list + budget, input to the plan)

Artifacts, in priority order (evidence-backed):
1. The repo face: README-as-pitch, CI badge, tests, clean tree, dated demo. Free points per winner formula, engineering evidence per diligence section. ~60-90 min.
2. The 90-second trailer: message lock first (30m), OBS capture of the real scaffold, founder voice, captions, licensed music, proof pass. Local stack. ~3-4h if full, 90-min cut possible.
3. The 3-minute live demo: the 6-beat arc mapped to our scaffold flow (input -> approval -> audit), rehearsal with the 2:30 timer. ~60 min.
4. One-pager + deck: 10-11 slides per YC structure, numbers from NUMBERS-2026, ask tied to the next milestone (nationals). ~90 min pre-drop skeleton, fill after kit mount.
5. Proof ledger: claim | evidence | condition | status for every number in every artifact. ~20 min, this is the honesty spine.

Tension to manage (VERIFIED): polish vs authenticity. Judges reward working demo + real numbers; packaging wins ties and first impressions. The trailer shows the real scaffold, not a fake UI animation. Label anything staged as concept.

## 7. Source pointer

All raw reports + basis files: craft-n-code/research/raw/cnc-wave{19,21,23,24}*. Deduplicated 1,159-URL ledger: /tmp/pkg-sources.json. DEEP anchors: cnc-wave21-packaging-trailer-r2.md, cnc-wave24-product-story.md. Dense seed skeletons: cnc-wave19-packaging-startup-r2.md (+r4). Long forms: cnc-wave19-packaging-startup-r3.md, cnc-wave23-seed-presentation-r5.md, cnc-wave23-seed-presentation-final.md.
