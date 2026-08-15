# BENCHMARKS-2026.md: the frontier, the evals, and what we honestly claim

Wave 1 research (Aug 15, 2026). Sources: decodethefuture.org
"AI Agent Benchmarks 2026" (updated May 2026), codesota.com
"Agentic AI Benchmarks Explained" (March 2026). Both fetched raw via
curl and quoted with numbers. VERIFIED = quoted from the pages.

## THE FRONTIER IN ONE PARAGRAPH (stage line ready)

The field stopped measuring "can the model answer" and now measures
"can the agent FINISH a task safely". The six benchmarks that matter in
2026: GAIA (general assistant), SWE-bench Verified (real GitHub bug
fixes), OSWorld (computer use on a real desktop), Tau-squared-Bench
(tool-agent-user interaction with POLICY ADHERENCE), WebArena (multi-
step browser tasks), and METR HCAST / Time Horizons (the longest task
an agent can finish 50% of the time, called "the new Moore's law").
VERIFIED: top scores cluster between 74-94% on the easier suites, but
those numbers are inflated by 5-15 points by contamination, scaffolding
and single-run reporting. "Treat any leaderboard as a directional
signal, not an SLA."

Why our story wins on this axis: our engine was built for exactly the
two axes the frontier now cares about. Tau-squared-Bench measures
policy adherence; we ship a typed tool registry with a policy gate
(auto/suggest/require) and a human approval step. HCAST measures task
horizon; we ship a 200-step trace ring and an audit trail so a long
run stays readable. We do not claim a benchmark number, we show a trace
a judge can read in 10 seconds. That is the honest version of "state of
the art".

## THE SIX BENCHMARKS (what each measures, what we map to it)

1. GAIA: general assistant, real-world questions with tools.
   Our map: evidence-first answers + sources in every proposal.
   Honest claim: we answer with evidence, we do not claim GAIA scores.
2. SWE-bench Verified: coding agents on real GitHub bugs.
   Leaderboard VERIFIED: codex-1 (OpenAI) 62.3% Feb 2026, Claude 3.5
   Sonnet + SWE-agent 55.0%, Amazon Q Developer 52.4%.
   Our map: not our domain, we say so if asked.
3. OSWorld: computer use on a real desktop. Our map: not our domain.
4. Tau-squared-Bench (Sierra Research, arXiv 2506.07982): tool-agent-
   user interaction with policy adherence, dual-control environment.
   Our map: THIS IS OUR ENGINE. Typed tools, side-effect classes,
   policy gate auto/suggest/require, human approve, audit. If a judge
   asks "how do you stop the agent doing something it shouldn't", the
   answer is the approval gate + the double-decision guard + the audit
   row for every decision.
5. WebArena: multi-step browser tasks. Our map: channel adapter.
6. METR HCAST / Time Horizons: longest task finished 50% of the time.
   Our map: 200-step trace ring + replay + golden fixtures. The demo
   shows a run from ingest to approved action in one window.

## WHY LEADERBOARD SCORES LIE (VERIFIED list, 5 reasons)

1. training-data contamination (the model saw the answer)
2. LLM-as-judge noise (a model grading a model)
3. single-run reporting (best of N, not median)
4. no cost or safety in scoring (a 100% score that burns money or
   breaks policy is not a win)
5. search-time contamination (agent finds the answer online mid-run)

Our counter, all built and verifiable:
- golden fixtures with expected results files, rerun fresh every time
  (42/42, 81/81 with the new suites, order-independent, fresh DBs)
- zero LLM-as-judge: tests assert real HTTP responses and real DB rows
- no single-run cherry-picks: every suite reruns clean
- cost and safety ARE the product: approval gate, consent records,
  provenance manifest, honest mode badge (provider_errors now counted)
- no search-time contamination: offline mode is fully deterministic

## OUR OWN EVAL STACK (what we actually run, all plain python3)

- 42 baseline tests: approval 13, trace 12, providers 9, multimodal 4,
  provenance 4. Fresh DB per suite, order-independent.
- Honesty suite (8): the badge must flip to offline when the provider
  fails or the key is missing; fixture/cached/offline flags all honest.
- Feeds suite (8): real data kit fetches, offline refresh, --feeds
  server mode, zero network in tests.
- Stress bench (23): flood 100 items, prompt injection (owned fields
  survive), 500KB bodies, empty feed, hostile search queries, malformed
  POST, 12 concurrent requests, path traversal (404 after fix),
  provider-failure counting. See scaffold/tests/test_stress.py.
- Total: 81/81, all deterministic, all order-independent.

## STRESS-TEST SOURCES FOR THE NIGHT (what can kill the demo, ranked)

1. LLM key dies (network/rate limit/quota): badge now says offline,
   offline rules still produce a full ranked feed. Drill: kill key
   mid-run, watch the badge flip (the honesty moment, show it ON STAGE
   if time allows).
2. Network dies for feeds: feeds.py --offline pre-writes honest meta;
   the demo falls back to fixture data with the badge showing cached.
3. Cache poisoned (stale .llm_cache.json): delete it, cold run.
4. DB locked by a previous server: kill stale serve.py first
   (bracket trick: pkill -f "[s]erve.py").
5. Port busy: pick a fresh port (demo.sh takes one).
6. Judge asks a hostile question: attack sheets + judge dossiers
   (docs/ATTACK-SHEETS.md, research/JUDGE-DOSSIERS.md).

## FRONTIER PRODUCT LANDSCAPE (who builds what, for the "already made"
## question on stage)

VERIFIED from the leaderboard pages: OpenAI codex-1 leads coding agents
at 62.3%, Claude + SWE-agent 55.0%, Amazon Q 52.4%. The pattern: every
major lab now ships agent products with tool use and approval flows.
If a judge asks "who already does this", the honest answer: the labs
ship agents, nobody ships OUR combination (controlled pipeline +
approval + provenance + honest failure badge + zero deps + runs
anywhere). The gap is the product, not the model.

## WAVE-2 NUMBERS (parallel.ai pro-fast, Aug 15, raw in
## research/raw/wave2-ai-failures.md)

- **SWE-bench VALIDITY CAVEATS (ai-code-failure-matrix R01, VERIFIED
  Aug 15): the leaderboard itself is inflated.** 7.7% of SWE-bench
  Lite / 5.2% of Verified tasks lack unit tests that discriminate good
  from bad patches; 28.4% of "passing" Lite patches (15.7% Verified)
  actually fail when tests are augmented; 5.3% of Verified tasks pass
  WITHOUT addressing the issue at all (do-nothing agent); the ABC
  audit found 7/10 popular agentic benchmarks flawed on outcome
  validity; reward-hacking exploit rates 0% (Claude Sonnet 4.5) to
  13.9% (DeepSeek-R1-Zero) under RL. Stage line: "we report method,
  harness, run count, and code-based assertions, because even the
  famous benchmarks inflate 5-40% of their scores."
- HCAST (METR): agents succeed 70-80% on tasks under one human-hour,
  under 20% on tasks over four human-hours. The 50% time horizon
  doubles roughly every 7 months. Our line: that gap is why a human
  approves; the demo shows the division of labor.
- SWE-bench Verified: official page shows Claude 4.5 Opus high 76.80%
  (2026-02-17); a third-party tracker shows Claude Mythos 5 95.5%
  averaged over 5 runs. Same benchmark, 19 points apart: report
  version, harness, run count, source. We report our numbers exactly
  that way (81/81, fresh DBs, deterministic).
- WebArena: best GPT-4 agent in the original study 14.41% vs 78.24%
  for humans. End-to-end success is far stricter than language
  quality.
- MAST: failure rates 41% to 86.7% across seven open-source
  multi-agent systems, 14 fine-grained failure modes identified.
- Production reality: 68% of production agents execute at most 10
  steps before human intervention, 70% prompt off-the-shelf models,
  74% rely primarily on human evaluation.
- A mature production scorecard has five layers: outcome correctness,
  policy adherence, tool-call correctness, trajectory efficiency,
  failure recovery. That is our 5-layer claim set, in order:
  81/81 tests, policy gate suites, typed registry tests, trace ring
  review, provider_errors + offline fallback.
- Leaderboard hygiene: LLM-as-judge shows substantial reliability
  gaps in a 2026 study; single-run scores are unstable because
  sampling, tool latency, web state, and judge behavior are
  stochastic. Our answer: code-based assertions, fresh DBs,
  order-independent suites, no LLM judges anywhere in the 81.
