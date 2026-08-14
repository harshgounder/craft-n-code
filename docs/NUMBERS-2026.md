# NUMBERS 2026 - the proof file (the 04-NUMBERS treatment for Craft N Code)

Compiled: 2026-08-14 20:30 IST | Purpose: every number we can quote on stage,
pre-verified. Nothing here is vibes; each claim has an evidence tag.

## 1. OUR BUILD (quote in the pitch, print on the KPI card)

- 42/42 automated acceptance checks, all green, all order-independent on fresh
  databases. Breakdown: approval gate 13/13, trace viewer 12/12, provider
  adapter 9/9, multimodal 4/4, provenance + consent 4/4. VERIFIED Aug 14,
  two independent runs.
- Zero external dependencies in the runtime: plain python3 stdlib, zero pip
  packages. AFTERPACKETS rule, the 2025 national winner's exact play.
- Four execution modes with a visible badge: LIVE (real LLM), CACHED (replayed
  responses), FIXTURE (golden feed), OFFLINE (deterministic rules). A judge
  always knows what the demo is running on.
- 14 API endpoints, one-command demo (./demo.sh, 9/9 endpoints verified 200).
- 200-step trace ring buffer: every decision explainable, every step auditable.
- 4 golden fixtures: happy, ambiguous, adversarial, multimodal, each with an
  expected-results file.
- 4 sponsor-shaped decks + 4 second-by-second storyboards, schema-validated.
- LLM layer VERIFIED for real on Aug 14 21:00: chat completions with the
  OLLAMA_API_KEY returned HTTP 200 with a real completion (model
  deepseek-v4-flash:0731); a cold serve.py run made 12 live calls with zero
  failures, mode=live. Earlier probes hit an auth-less /v1/models endpoint
  and were weak proof; that is corrected. Offline fallback means the demo
  never dies.
- Known bug (fix brief written, opencode queue): the mode badge reports
  "live" even when the provider failed and offline fallback ran. The
  honesty layer is blind on failure. See docs/SCAFFOLD-FINDINGS-20260814.md.
- One engine (ingest, dedupe, summarize, rank, deadlines, propose, approve,
  audit), four skins (agentic ops, multimodal assistant, creative workflow,
  security). Skin mount target: 15-40 min (target UNVERIFIED, drill planned).

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
