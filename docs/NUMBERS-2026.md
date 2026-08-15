# NUMBERS 2026 - the proof file (the 04-NUMBERS treatment for Craft N Code)

Compiled: 2026-08-14 20:30 IST | Purpose: every number we can quote on stage,
pre-verified. Nothing here is vibes; each claim has an evidence tag.

## 1. OUR BUILD (quote in the pitch, print on the KPI card)

- 81/81 automated acceptance checks, all green, all order-independent on fresh
  databases. Breakdown: approval gate 13/13, trace viewer 12/12, provider
  adapter 9/9, multimodal 4/4, provenance + consent 4/4, honesty badge 8/8,
  real data feeds 8/8, stress bench 23/23. VERIFIED Aug 15 11:00 IST,
  independently re-run by Hermes, not just opencode's claim.
- Zero external dependencies in the runtime: plain python3 stdlib, zero pip
  packages. AFTERPACKETS rule, the 2025 national winner's exact play.
- Four execution modes with a visible badge: LIVE (real LLM), CACHED (replayed
  responses), FIXTURE (golden feed), OFFLINE (deterministic rules). A judge
  always knows what the demo is running on. The badge CANNOT lie anymore:
  provider failures and missing keys flip it to offline (provider_errors
  counter, fixed Aug 15, regression-tested H1-H6).
- 14 API endpoints, one-command demo (./demo.sh, 9/9 endpoints verified 200).
- 200-step trace ring buffer: every decision explainable, every step auditable.
- 4 golden fixtures + 5 skin-kit fixtures (agent ops, creative, privacy,
  messaging, enterprise), each a mountable template for a predicted statement
  shape. Kit mount target 15-40 min, now measured by drill (MOCK-DROPS).
- Real data kit: 3 live public feeds (Hacker News, GitHub repos, Unstop event
  API), key-free, stdlib-only fetcher, honest freshness badge (live/cached/
  offline), offline fallback pre-built. VERIFIED: 31 real records fetched in
  one refresh; feeds tests 8/8.
- LLM layer VERIFIED for real on Aug 14 21:00: chat completions with the
  OLLAMA_API_KEY returned HTTP 200 with a real completion (model
  deepseek-v4-flash:0731); a cold serve.py run made 12 live calls with zero
  failures, mode=live. Earlier probes hit an auth-less /v1/models endpoint
  and were weak proof; that is corrected. Offline fallback means the demo
  never dies.
- Failure observability FIXED Aug 15 (BUILD-SPEC-3): the badge lied when
  the provider failed. Now provider_errors is counted per pipeline run and
  current_mode() returns offline on any provider miss or missing key.
  Regression suite H1-H6 proves it. See docs/SCAFFOLD-FINDINGS-20260814.md
  for the original finding and repro.
- One engine (ingest, dedupe, summarize, rank, deadlines, propose, approve,
  audit), four skins (agentic ops, multimodal assistant, creative workflow,
  security). Skin mount target: 15-40 min (target UNVERIFIED, drill planned).
- RESEARCH COVERAGE (all Aug 15, all committed, raw files on disk):
  17 parallel.ai deep research runs (12-wave round + 4-wave prior-art round
  + wave-2), all completed, all converted, all integrated.
  PER-TOPIC-BENCHMARKS: 30 domains, ~250 named benchmarks/standards/tools.
  PER-TOPIC-STRESS: 83 categories (A-F) + 10 demo-hardness (G) across 30
  domains. IDEA-DILIGENCE: 30 domains scored (need, sponsor, judge,
  funding, adoption, idea seed, gate, risk). PRIOR-ART-MAP: the exists-map
  per shape/domain with stars, wedges, traps, the three tensions, the
  venue recipe. WAVE-SYNTHESIS: the master index. NIGHT-CHEAT-SHEET: the
  21:30 quick-mount table (5 mount cards + 25 domain rows + 6 judge
  attack answers + 3-min script). EVIDENCE CHAIN (honest): wave numbers
  are verified through each report's inline citations and URL
  reachability spot-checks, not independently re-measured.
- THE 429 WATCH (Aug 15 13:45): the LLM provider rate-limits under
  sustained cold-run load. Pre-warm in two spaced passes, keep the warm
  cache as fallback, and the honesty story as the backup demo.

## 2. THE FIELD (reg counts, live Unstop API, competition/1730314)

- 2026 Rajasthan: 402 registered at 15:10 IST Aug 14, 456 by ~17:45 IST Aug 14
  (+54 in under 3 hours, ~18/hr pace). ~96 players at last check. ₹299/team.
  VERIFIED, live API.
- 2025 Rajasthan: 1,592 registered, 285 players across 11 state rounds.
  VERIFIED from research/state-rounds.
- 2026 event: hybrid mode (Unstop listing), D3 Fest national finals Oct 30 -
  Nov 1 2026 at IIIT Bhubaneswar. VERIFIED.
- 2025 national finals: 20 teams, winner AFTERPACKETS built in lane 7, the
  single-team lane. VERIFIED (p-society solutions repo).
- Sponsor slots on the 2026 site: ALL OPEN ("Your Brand Here"). The sponsor
  companies are not yet announced on the site. VERIFIED Aug 14 (site source).

## 3. THE JUDGES (taste profile, Hackfest 2024 panel, the same ecosystem)

- 6 judges, two axes: research/security (3 of 6: police ACP + cyber SOC
  expert + ML PhD) and operations/impact (3 of 6: finance, data quality,
  sociopreneur). VERIFIED from research/JUDGE-DOSSIERS.md.
- Decisive questions per lens: measurable outcome, reliability + learning,
  data/baseline/metrics, real-user safety, threat model + test evidence,
  adoption + persistence.
- Security-flavored projects hit the panel's center of mass: 3 of 6 judges
  reward security depth. INFERRED but grounded.

## 4. THE NIGHT BUDGET (Aug 15 21:30 - Aug 16 09:00)

- 21:30 drop to 06:00 Unstop close = 8.5 hours. To 09:00 club freeze = 11.5h.
- Budget: 0.5h fingerprint + decision, 0.5-1h skin mount, 2-3h vertical slice
  + differentiator + staged failure, 1h polish + KPI card, 0.5h recording
  backup video, 0.5h rehearsal. Remaining 2-3h = buffer + sleep rotation.
- Submission gates: Unstop PPT v1 at 23:00, v2 at 03:00, FINAL 05:00 (never
  05:59). Club site: repo_url + pitch v1 before 06:00, final before 09:00.
- Kill criteria (pre-agreed): any dependency failing a 60-90 min time gate
  switches to fixture/replay mode. Never spend 6h on image quality or a
  blocked API.

## 5. WHAT WE DID NOT FIND (honest negatives, do not fake)

- Sponsor authorship of the Aug 15 statements: UNVERIFIED publicly. Rudra's
  in-person intel is the best signal; the site itself shows no sponsor names.
- 2025 Rajasthan state-round problems: NOT publicly recoverable (state-rounds
  research run returned an honest negative). The Rudra ask is the only way in.
- No public 2026 solutions repo exists (p-society org census, VERIFIED).
- 2024 national winner: never publicly named.

## 6. TEAM / CAMPAIGN NUMBERS (context for judges who ask)

- This is not our first build: Kavach (call security) has a fresh-clone
  verification 5/5, 14/14 ad-hoc checks, 24 real incidents across 4 scam
  families, and a mapped grant route (iDEX, ADITI).
- Research behind this round: 6 deep-research runs, ~376K chars, 500+ cites,
  6 prompt files re-fireable.
- Repo: ~180 tracked files, clean tree, local == remote at every check.
