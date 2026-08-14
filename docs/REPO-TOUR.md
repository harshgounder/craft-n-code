# REPO-TOUR - where everything lives and why (read this before anything else)

Written 2026-08-14 for Team 511. The repo looks like a wall of files. This
file is the map. After this, read IDEA-BANK.md and WAVE-SYNTHESIS.md, those
two are the only files that matter for the night.

## The 30-second version

- `research/` = the intel. Why we win: we know the format, the sponsors, the
  judges, the winners, the losers, the numbers, the schedule.
- `scaffold/` = the weapon. A working product skeleton we can re-skin in
  15-40 minutes no matter what the problem statement says.
- `docs/` = the stage kit. Storyboards, build specs, tour (this file).
- `scripts/` = small automation (feed data helpers).
- Top-level files: README.md (war-room index), CONTINUATION-PROMPT.md (the
  reset file for new AI sessions), INDEX.md (file-by-file index, boring but
  complete).

## The only files you need to read (in this order, ~25 min total)

1. `research/IDEA-BANK.md` - THE playbook. Pre-built answers for each
   sponsor-shaped question, the decision tree that fires 10 minutes after
   the 21:30 problem drop. This is what we run the night on.
2. `research/WAVE-SYNTHESIS.md` - WHY one shared engine wins: the 5 most
   likely problem shapes all share one pipeline (input -> extraction ->
   evidence -> ranking -> proposal -> approval -> audit). Also the gaps we
   are filling right now and the hour-by-hour execution plan.
3. `scaffold/README.md` - how to run the engine, webapp, and decks.
4. `docs/BUILD-SPEC.md` - what we are building right now (approval gate +
   trace viewer) and how it will be tested.

## research/ - the intel (40+ files, grouped)

### Strategy (the brain, read these)
- `IDEA-BANK.md` - pre-built ideas A/B/C/D + decision tree + company-lane
  protocol + risk table + action plan. THE playbook.
- `WAVE-SYNTHESIS.md` - 5 ranked predicted problem shapes + common
  denominator + gaps table + 8.5h execution plan.
- `CHEATSHEET-BRIEF.md` - what matters most to judges, what each sponsor
  makes and looks for, hottest tech for a 24h build.
- `GAP-MAP.md` - what intel we do NOT have yet and how to get it. Source of
  truth for the research waves we are running now.

### Deep-research reports (the heavy lifting, 6 runs)
- `company-lanes/cnc-company-lanes-pass1.content.md` - 5 named skins per
  sponsor (65K chars).
- `company-lanes/cnc-company-lanes-pass2.content.md` - the honest one:
  no public proof the sponsors write the questions, but the 3 ranked
  predicted shapes (DEEP 90.1, 111 cites).
- `company-lanes/cnc-sponsor-products.content.md` - what each sponsor makes
  + looks for (68K, 230 cites).
- `company-lanes/cnc-winner-anatomy.content.md` - why winners win, the
  zero-dependency rule (62K).
- `company-lanes/cnc-problem-lanes.content.md` - the 5 ranked predicted
  problems + build cards + kill criteria (78K, 333 cites).
- `company-lanes/cnc-state-rounds.content.md` - honest negative: no
  state-round problems publicly recoverable (42K).
- `prompts/` - the prompts used for those runs, saved so we can re-fire.

### The competition (who we are up against)
- `COMPETITIVE-INTEL-DOSSIER.md` - org lineage, editions, people, sponsors.
- `MASTER-DOSSIER.md` - everything in one file (older v2 synthesis).
- `RAJASTHAN-LISTING-1730314.md` - our round's Unstop listing.
- `COMPETITOR-POOL.md` - 20-team threat matrix + empty-lane strategy.
- `PARTICIPANT-UNIVERSE.md` - 25+ past participant repos.
- `REJECTED-LOST-ENTRIES.md` - why losers lost (the anti-patterns).
- `WINNER-REVERSE-ENGINEERING.md` + `WINNER-EXACT-DEEP-DIVE.md` - AFTERPACKETS
  (2025 winners) full stack + why-it-won argument.
- `JUDGE-DOSSERIS.md` - the 6 judges' backgrounds + how-to-win matrix.

### Problem history (format forensics)
- `raw/rnr-phase1-full.txt` + `raw/rnr-phase2-full.txt` - the 2025 problems
  VERBATIM. The format template: "The Problem / Your 24-Hour Mission /
  Required MVP (bullets) / Bonus Goal".
- `2024-STATE-QUALIFIER-FORMAT.md` - RVCE round format, top-2 advance.
- `2025-FINALS-ROSTER.md`, `D3FEST-*-PROBLEMS.md` - older editions.
- `EVENT-SITE-FORENSICS.md` + `-v4.md` - the 2026 event site source code
  analysis (tracks, submission flow, admin console).

### People (who to ask / who judges)
- `PEOPLE-DOSSIER-CSC.md` - CSC MUJ full roster.
- `PEOPLE-DOSSIER-TECHSOC.md` - Tech Society IIIT-B roster.
- `RABBITT-AI-DOSSIER.md`, `NEXORA-FORENSICS.md` - partner orgs.

### State (live data, machine-written)
- `watch-state.json` - watchdog's last probe of every Unstop listing.
- `INTEL-20260814-EVENING.md` - tonight's live API findings: submission =
  PPT-only (pdf/pptx 50MB), resubmission allowed, judge buttons, site URLs.
- `RE-AUDIT-FINDINGS.md` - every correction from the Aug 14 sweep.
- `2025-STATE-SWEEP.md`, `STATE-QUALIFIER-SCAN.md` - state round maps.

## scaffold/ - the weapon (VERIFIED working)

- `engine/engine.py` - the pipeline: ingest -> dedupe -> LLM summarize ->
  rank -> deadlines. Works with a live LLM (ollama-cloud) AND fully offline
  (regex + tf-idf). The demo never dies. Domain-agnostic: feed it ANY JSON
  items, it ranks them.
- `engine/signal.db` - sqlite database the engine writes to (generated).
- `webapp/serve.py` - zero-dependency python HTTP server (stdlib only).
  Serves the feed/digest/search/complaints over HTTP so any machine with
  python3 can demo. (Approval endpoints being added now.)
- `webapp/static/index.html` - the dark UI: digest, ranked feed, search,
  requests board. Single file, no frameworks.
- `deck/deck-gen.js` - one pptxgenjs skeleton that generates 4 decks
  (agentic/multimodal/creative/kavach). Each deck is a skin of the same
  story, schema-validated.
- `demo.sh` - one command: generate feed + serve UI.
- `README.md` - how to run everything, modes, seed swap.

## docs/ - the stage kit

- `DEMO-STORYBOARDS.md` - 4x 3-min second-by-second voiceover scripts for
  the pre-recorded demo videos.
- `BUILD-SPEC.md` - the plan for the approval gate + trace viewer we are
  building right now (with acceptance tests).
- `REPO-TOUR.md` - this file.
- `HARDWARE-GATE.md` - archived what-if, NOT a track assumption.

## Why it is organized this way

- Research and build are separate: the intel should not change the code,
  the code should not pollute the intel.
- Everything is versioned (git), nothing is deleted, every claim carries a
  VERIFIED / INFERRED / UNVERIFIED tag.
- The repo is PRIVATE. Friend-facing docs strip progress detail.

## Reading order for the night (Aug 15, 20:45)

1. This tour (done).
2. IDEA-BANK.md decision tree (2 min).
3. WAVE-SYNTHESIS.md execution plan (2 min).
4. Unstop open. 21:30 drop. Cue table from IDEA-BANK §5 (2 min).
5. Decision tree fires (10 min). Pick idea + deck + storyboard.
6. Swap seed data, ./demo.sh, submit the pptx before 06:00.
