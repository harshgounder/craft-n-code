# BUILD LOG - every session, every commit, every why

This is the complete record of the Craft N Code effort. Nothing is
summarized away: each entry names the commit, the hour, what landed,
and why it matters. Read it top to bottom to see the whole arc.

Compiled: 2026-08-14 evening | Source of truth: git history + session records

## THE SHAPE OF THE CAMPAIGN

Two nights of work:
- Night 1 (Aug 13, ~22:00 to 03:00): the recon blitz. Everything about the
  event, its history, its winners, its judges, its sponsors, its site.
- Day 2 (Aug 14, ~09:00 to now): the re-audit, the strip, the scaffold
  build, the deep-research wave, the code builds, the docs.

The one rule that shaped everything: the user rejected site-track
assumptions (Aug 14). Only verified timings survived. Everything else
was rebuilt around the sponsor-set-question reality.

---

## NIGHT 1 - AUG 13

### 22:54 - ops: judge-research launcher (d2017a4)
Built the parallel.ai launcher with key fallback chain. Fired the ultra8x
deep-research run on key#112 to build dossiers on all 6 Hackfest 2024
judges.

### 22:56 - D3 Fest 2023 brochure (12706dc)
Recovered the full 14-page D3 Fest 2023 brochure: 12 events, Tech Society
+ E-Cell, the 13-hour overnight hackathon (ancestor of the 24h format),
Cyber Hunt (CTF ancestor), Shark Tank (pitch ancestor).

### 22:58 - D3 Fest 2022, all 9 problems (60563a0)
Found d3nov.netlify.app with ALL 9 hackathon problems verbatim: code
snippet sharing, hostel management, smart campus app, bill split, mess
management, PM2.5 prediction, IRCTC automation, crypto crowdfunding,
on-chain event ticketing. Key find: D3h09 (on-chain ticketing) is the
direct ancestor of the 2025 NFT challenge. The organizers recycle problem
families every 2-3 years with new tech.

### 23:04 - JUDGE-DOSSIERS (dac8eb0)
The ultra8x run landed. All 6 judges profiled: Anjana Tudu (ACP Odisha
Police, later CID Crime Branch, NIT Rourkela BTech, Ericsson background),
Lingaraj Sethi (InfoSec Manager Mphasis, PhD, CEH), Sarthak Padhi (PhD
Scholar IIIT-B, medical imaging ML), Ayushi Parashar (Hyundai corporate
finance), Shivani Prasad (GSK data lead, unconfirmed match), Sonali
Satpathy (sociopreneur). The comparative matrix: 3 judges reward
research/security depth, 3 reward operations/impact. A winning project
must satisfy BOTH axes.

### 23:36 - event-site forensics v4 (2c430d3)
Extracted the live JS bundles of craftncode-2026.vercel.app. Found the
admin console (read-only, shows team_name/track/repo/demo/pitch/timestamp:
the pitch is the first thing judges read), the auth flow (user_roles
admin guard), the submission mechanics (plain INSERT, no upsert,
resubmit = new row, latest wins), and the night canteen (a UI mock, no
backend, bring your own snacks).

### 23:44 - RABBITT-AI-DOSSIER (8d5b86a)
Rabbitt AI: Harneet S N (IIT Delhi, Flipkart PM, TechCurators), $2.1M
seed, ChanceRAG and DRIP products, open-model advocacy (Llama/Mistral/
Gemma). The NEXORA'26 partnership with CSC MUJ was the dress rehearsal
for the exact format we face.

### 23:46 - NEXORA-FORENSICS (ca94e66)
NEXORA'26 site internals: 6 tracks, the judging stack (Jury Score,
Modify Score, Scores Redacted for Review Balance, leaderboard, timeline-
gated scoring), submission requirements (GitHub repo required, live app
build expected, PPT). Same people running Craft N Code.

### 23:48 - 2024 state qualifier format (22bb7fe)
The RVCE Bangalore 2024 round: food safety theme, 3 tracks, 4x25%
judging (completeness, design, innovation, impact), top-2 advance with
expenses covered. 5 participant solutions mapped: 4 of 5 used blockchain
(2024's differentiator).

### 23:49 - COMPETITOR-POOL (e89f18a)
The 2025 winner's workflow from commit forensics: build core first,
scope down aggressively in the final hours, rebrand for impact, clean
the repo. The 20-team threat matrix. The empty-lane strategy.

### 23:52 - RAJASTHAN-LISTING-1730314 (000d43d)
Found the live Unstop listing: 402 teams registered, Rs 50,000 prize,
qualifier has its OWN problems (separate from nationals), contacts
verified (Spandan Hota, Tirtha Desai, Abhinav Trikha). Watchdog updated
to track it directly.

### 23:55 - STATE-QUALIFIER-SCAN (b87b5e7)
Rajasthan (402 reg) = biggest confirmed 2026 state round. UP listing
fresh (1 reg). No other 2026 state listings in the probed ranges.

### 00:32 (Aug 14) - 2025 problems verbatim (3b18763)
ALL 7 Phase 1 problems + 7 Phase 2 extensions from the p-society
solutions repo, with exact MVP bullets and bonus goals: NFT ticketing,
Web3 loyalty, P2P skill swap, AI lecture generator, Collegiate Inbox
Navigator, Automated Lab Grader, Mobile Packet Hunter (what AFTERPACKETS
won with).

### 00:41 - WINNER-EXACT-DEEP-DIVE (0a11753)
AFTERPACKETS at code level: the C++ DPI parser (hand-rolled IPv4/TCP/
UDP/ICMP), VPNService capture, Room DB, WebSocket server, firewall
engine, 13 UI screens, evidence-bundle export. The commit timeline by
hour (06:56 initial commit, scope-downs at 07:17 and 08:11, rebrand at
08:01). The counterfactual: PromptBuddy's Composio/Gemini war, EduSynth's
77MB production app, both lost.

### 00:42 - 2026-TOPIC-PROBABILITY (b166437)
The 5 tracks verbatim + the evidence base per track + sponsor mapping +
probability table: PS-03 35% and most winnable, PS-04 safest escape
hatch, PS-02 dark horse, PS-05 the trap (no hardware).

### 00:44 - REJECTED-LOST-ENTRIES (5a3e94c)
How teams lose: R1 mechanics from NEXORA (score 0-100, redacted
review, 23505 duplicate block), rejection patterns (2/20 repos 404,
an 18KB repo, no deployment links), and the 8-step R1 win formula.

### 01:00-01:10 - the re-audit night (3c1138e, 98ff21f, f9d5a04, 885d50d, 6c11d19)
The big re-audit corrected the earlier dossier: 9 state rounds in 2025
(not 4-5), 2024 winners were Wizard_Oz/Fork, fee confirmed Rs 299,
2024 finals timeline resolved from Instagram + certificates + repo
commits (11 PM Nov 8 kickoff, 24h). 2025 state map: 11 rounds, 1,592
reg / 285 players. The Rs 131K D3 pool claim verified via Scribd.

### 01:20 - gap-map execution (bef04cf)
D3-2026 site fully explored (no seeded problems, resubmit is official),
p-society 67 repos harvested, 2023/2024 brochures pulled, AFTERPACKETS
formula confirmed, 20-team competitor pool.

---

## DAY 2 - AUG 14

### 09:53 - the new-window handoff (bce0ee4)
IDEA-BANK with drop-ready ideas for all 5 tracks + decision tree, README
rewrite, CONTINUATION-PROMPT, INDEX. The repo became new-window ready:
a fresh agent can read one file and know everything.

### 10:06 - the scaffold (83a3be9)
The shared engine + webapp + 4 decks pre-built: ingest/dedupe/summarize/
rank/deadlines pipeline with ollama-cloud LLM + full offline fallback,
zero-dependency webapp, deck generator, demo.sh, storyboards. Verified
11/11 ad-hoc.

### 10:57-11:13 - the company-lane wave (fcac6a2, 1bfaed4, ec821d2, 1658c20)
The Rudra protocol landed: site tracks are the CLUB's backup, the
sponsor companies set the real questions. IDEA-BANK got the company
fingerprint table, setter priors, and the lane decision tree. Two
deep-research passes on company lanes: pass 1 SURFACE, pass 2 DEEP 90.1
(sponsor authorship stays UNVERIFIED publicly, insider signal stands).

### 11:51 - THE STRIP (d00077b) - the user's directive
ALL site-track assumptions removed: PS-01..PS-05, Campus Pulse, Night
Ops, Hygiene Sentinel, hardware gate. Only timings survive. IDEA-BANK
rebuilt around the 4 sponsor-shaped lanes (BriefLens, Kavach Circle,
SignalStory, Kavach). Engine seed data made domain-agnostic. Decks
regenerated. Re-verified 13/13.

### 13:29-13:37 - the deep-research wave (c4b2eb7, c4703cd, e986520)
3 parallel runs fired (sponsor-products, winner-anatomy, problem-lanes)
+ a state-rounds run. Results: problem-lanes ADECENT 333 cites,
sponsor-products ADECENT 230 cites, winner-anatomy SURFACE 138 cites,
state-rounds ADECENT 125 cites with an honest negative (no verbatim
state-round problems are publicly retrievable). The synthesis became
WAVE-SYNTHESIS.md: 5 ranked predicted problems, the common denominator
pipeline, the 5 portable patterns, the 8.5h execution plan, the
zero-dependency rule.

### 15:07-15:12 - the re-audit + handoff refresh (073951b, 009e196)
Watchdog state refreshed. All three handoff files (CONTINUATION-PROMPT,
INDEX, README) refreshed with the full re-audit state, the scaffold
story, and the deep-research wave.

### 15:27 - the build spec (5ff76a2)
BUILD-SPEC.md: approval gate + trace viewer, grounded in the actual
serve.py routes and engine.py dataclasses, with G1-G13/T1-T6 acceptance
tests. Plan-only at that point: the user had said hold builds.

### 15:48 - the evening intel refresh (a630777)
Live Unstop API: 456 registrations, submission = PPT only (pdf/pptx,
50MB), multiple submissions allowed (latest wins), judge panel buttons
shortlist/reject/hold/noshow, score /5 weighted 100, the D3 Fest 2026
site live at d3fest.techsoc-iiitbbsr.com, Tirtha Desai as a new contact.

### 15:51 - the teaching docs (e6dd5e7)
REPO-TOUR.md (the map) and CODE-WALKTHROUGH.md (every file explained
function by function, production lessons, audit how-to).

### 15:55 - the p-society harvest (91a07dc)
Org census complete: NO 2026 solutions repo exists publicly (D3-2026 is
an empty marketing site), 2024 problems not in the site source (dead
end closed honestly), 2025 confirmed already harvested. The research
frontier is closed: everything else is time-gated to the drop.

### 15:58 - THE APPROVAL GATE (cfaf85a)
Built via opencode per BUILD-SPEC Part 1: typed tool registry (4 tools),
policy gate (read-only auto / reversible suggest / side-effecting
require), proposals + audit_events tables, 5 new API endpoints, Actions
tab in the UI. G1-G13 suite, 13/13. Two audit rounds: the
double-decision guard (no fake history) and the bash -n G13 check.

### 16:22 - THE TRACE VIEWER + FIXTURES (f131a2f)
Built via opencode per BUILD-SPEC Part 2: --fixture/--offline flags,
mode badge (live/cached/offline/fixture), /api/trace ring buffer, 3
golden fixtures with expected top-3, scam-word cap, trace drawer UI.
T1-T6 + offline regression, 12/12. The audit caught a REAL bug: --offline
set the env var after engine import, so the LLM would still fire with a
key set. Fixed with lazy env reads + a regression test.

### 16:42+ - the "build everything" directive
The user went all-in: all remaining scaffold items. BUILD-SPEC-2
specified three: the provider adapter (swap LLM backends via
SIGNAL_PROVIDER), the multimodal input adapter (text/PDF/image with
graceful fallback), provenance + consent (per-decision manifests,
consent records, consent_required flags). opencode built all three:
test_providers 9/9, test_multimodal 4/4, test_provenance 4/4, with
trace 12/12 and approval 13/13 regressions. All five suites verified
independently by Hermes: 42/42.

### 16:50+ - the reading ladder + the atlas
The user asked for the full inventory, then for a reading ladder, then
for THIS: an atlas website that renders every file in full with OPEN
FILE buttons. The atlas generator, this log, and the manifest are the
answer.

### 17:05 - THE AGGRESSIVE AUDIT (user directive)
A hostile self-review of everything. What it found and what was fixed:
1. TEST RACE (critical, my earlier claim was wrong): the four
   server-starting suites used a fixed 1.2s sleep after starting the
   server, and serve.py computed the mode at startup, which on a COLD
   database runs the whole LLM pipeline BEFORE binding the port.
   test_provenance sets a fake key (Q1 needs it), so cold-start took
   longer than 1.2s and the test crashed with connection refused. It
   only passed earlier because the shared signal.db was warm. The
   "42/42 independently verified" claim was therefore warm-state
   dependent. FIXED: wait_ready() polling helper in all four
   server-starting suites (test_providers is serverless, it tests the
   provider classes directly and never had a sleep), per-suite fresh DB
   (delete signal.db + .llm_cache.json at suite start), serve.py binds
   immediately and computes the mode in a daemon thread. Re-verified in
   two orders on fresh DBs.
2. TEST CONTAMINATION (real): suites share signal.db, so consent rows
   granted by the provenance suite changed the approval suite's
   consent_required output. Fixed by per-suite fresh DBs.
3. STALE DOC NUMBERS (real): CODE-WALKTHROUGH line counts were from
   before the builds (engine 433 vs 473, serve 193 vs 373, index 245 vs
   378, approval 256 vs 362). Fixed.
4. RULE COMPLIANCE (real): the pre-rule research corpus had 377 em
   dashes across 33 files and ~20 AI-tell words in 8 files. Swept: em
   dashes replaced with hyphens everywhere; AI-tell prose replaced
   word-level; verbatim quotes (Apple newsroom, NEXORA site) and URL
   slugs left untouched on purpose. Atlas regenerated.
5. ONE FALSE FINDING (honest note): my audit script claimed a dead
   urllib import in engine.py, but the provider refactor had already
   removed it. The finding was based on a stale file read, corrected.
6. SERVED-FILE WART (known, documented): demo.sh writes
   webapp/static/demo-feed.json that nothing reads. Documented in
   CODE-WALKTHROUGH, left as-is (harmless, gitignored).

---

## THE RULES THAT SURVIVED (hard rules)

1. All source code is written by opencode CLI. Hermes is the architect
   and reviewer: writes briefs, audits diffs, tells opencode what is
   right and wrong, runs tests, commits. Hermes never writes source
   code itself.
2. No em dashes in any output, file, doc, or comment. No AI-tell words.
3. Research waves run ONE BY ONE, never parallel fan-out.
4. The demo has zero uncontrolled dependencies. LLM, cached, or offline,
   it always works.
5. The repo reflects true state. Verified numbers only, honest negatives
   included.

## ATLAS REFRESH (Aug 15 15:40 IST, atlas v3)

The atlas site was stale: it covered 82 files and missed everything
landed since the last build. Refreshed the manifest and rebuilt:

- 82 -> 135 pages (1.02M -> 1.78M source chars).
- New section THE NIGHT (AUG 15-16): runbook, submission text kit v2,
  numbers ledger, attack sheets, backend drills, Rudra ask, playbook,
  mock drops, channels, session log, build specs 3-4, UI/UX brief,
  scaffold findings, storyboards, hardware gate (archived).
- THE EVENT + 2: site forensics (two gates), brochure OCR.
- THE BUILD + 10: 5 kit fixtures (kit1..kit5), feeds.py, test_feeds,
  test_honesty, test_stress.
- New section THE RAW RESEARCH WAVES: all 17 wave .md outputs,
  judge dossiers content, 2025 Phase-1/2 verbatim txt, 6 re-fire
  prompts.
- Verified: all 134 manifest paths exist, build exits 0, test_build
  ALL TESTS PASSED, footer count 135/1780982, spot checks (runbook
  kill criteria, cheat sheet WEDGE line, continuation LATEST STATE)
  all present.
