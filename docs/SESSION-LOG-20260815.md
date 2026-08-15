# SESSION-LOG-20260815.md - competition day, morning window (10:08 - ~11:45 IST)

Full record of the Aug 15 morning prep window. Night flow starts 20:00.

## DECISIONS
1. Greenlit (user): badge fix + real data kit via opencode; full-force prep
   day: templates for predicted topics, frontier research, real AI-failure
   cases, product/UIUX taste, real data, benchmarks, stress tests.
2. No more deep research waves in parallel: research waves one at a time;
   wave-2 launched as ONE pro-fast parallel.ai task (the only network
   research allowed while opencode worked).
3. Pre-warm rule locked: never cold-boot the demo on stage (cold 31-item
   live pipeline measured at 4-5 min due to LLM rate limits).

## BUILDS (all via opencode per the hard rule; Hermes wrote the spec)
- BUILD-SPEC-3 (docs/BUILD-SPEC-3.md): 3 parts.
  Part 1: badge honesty fix. providers.py failures counter, engine.py
  provider_errors in llm dict, serve.py current_mode() treats
  model==OFFLINE and provider_errors>0 as offline. Regression H1-H6.
  Part 2: real data kit. NEW engine/feeds.py: 3 key-free sources (HN
  Algolia, GitHub repo search, Unstop event API), stdlib only, honest
  freshness meta, --refresh/--offline/--dump CLI. serve.py --feeds flag,
  GET /api/feeds, feeds_meta in /api/stats. Tests F1-F4.
  Part 3 (found by Hermes stress bench S8): static path traversal fix.
  serve.py static branch rejects ".."/"."/empty segments with 404 and
  requires resolved target inside STATIC.
- opencode run 1: 42/42 existing + honesty 8/8 + feeds 8/8 = 58/58 claimed.
- opencode fix run: traversal 404 verified (raw socket: /static/../engine
  /engine.py -> 404, /static/index.html -> 200).
- HERMES VERIFIED INDEPENDENTLY: all 8 suites = 81/81 (13+12+9+4+4+8+8+23).

## HERMES LANE (docs + data + tests only)
- research/TOPIC-UNIVERSE-2026.md: every possible statement. 8 sections:
  companies with DNA + can-ask lists, 5 shapes, 20 domains, kit mapping
  matrix, the STATEMENT GRAMMAR (subject + action + constraint + channel
  + evaluation + twist), 2025 set, 2026 backup tracks, priority matrix.
  User's idea-finder file (he builds tooling on it in another window).
- research/SKIN-KITS-2026.md: mountable templates for all 5 shapes with
  company flavor matrix, mount protocol, label patch brief for opencode.
- 5 kit fixtures: kit1_agent, kit2_creative, kit3_privacy,
  kit4_messaging (incl. digital-arrest + parcel scam), kit5_enterprise.
- scaffold/tests/test_stress.py: STRESS-BENCH S1-S10, 23/23: flood 100
  items, prompt injection (owned fields survive), 500KB bodies, empty
  feed, hostile search, malformed POST, 12 concurrent GETs, path
  traversal, provider-failure counting.
- research/BENCHMARKS-2026.md (wave 1, curl-fetched, VERIFIED quotes):
  6 benchmarks that matter in 2026 (GAIA, SWE-bench Verified, OSWorld,
  tau-squared-bench policy adherence, WebArena, METR HCAST time
  horizons), leaderboards inflated 5-15 pts by contamination/scaffolding/
  single-run, 5 reasons scores lie, SWE-bench leaders (codex-1 62.3%,
  Claude 3.5 Sonnet 55.0%, Amazon Q 52.4%). Stage line: the frontier
  measures policy adherence + task horizon; our engine was built for
  exactly those axes, and we show a trace not a number.
- docs/BACKEND-DRILLS-2026.md: 6 drills (cold boot, honesty, live data,
  skin mount, recovery, test gauntlet) + command cheat sheet with the
  anchored-key export + bracket-kill pitfalls.
- docs/UI-UX-BRIEF-2026.md: draft UI standards (badge visibility, queue
  cards with evidence, proposal pane, trace strip, failure toast);
  pattern list merges wave-2 findings when they land.
- docs/NUMBERS-2026.md updated: 81/81, feeds kit, badge fixed, 5 kits.
- docs/NIGHT-RUNBOOK.md updated: kit matrix, live-data beat, PRE-WARM
  rule, honesty moment, 81/81 KPI.

## VERIFIED LIVE CHAIN (end to end, real network)
- feeds.py --refresh: 31 records (hn 20, github 10, unstop 1).
- serve.py --feeds with real OLLAMA_API_KEY: mode=live,
  llm {model: deepseek-v4-flash:0731, cache_hits 11, cache_misses 51,
  provider_errors 0}, 51 REAL live LLM calls zero failures, /api/feeds
  mode live, feed shows real HN stories (Opus 5 thread, e-ink RSS
  newspaper, LuaCAD) with real summaries. Cold time 4-5 min for 31 items
  (rate limits) -> pre-warm rule.
- Badge honesty: H1-H6 prove offline flip on failure/missing key.

## PARALLEL POOL (user asked to check keys)
- Firecrawl (web_search/web_extract) BILLING 402 -> fell back to searxng
  web_search_plus (worked, lower quality) -> user said no low quality,
  use parallel. Probed pool fresh: 27 task-alive keys (lines 111-137,
  202 accept), lines 103-110 drained 402. status.json task_alive STALE.
- MCP keys in .env rotated to fresh lines (task=137, search=136, both
  verified 200). NOTE: task-mcp.parallel.ai/mcp blocks raw clients
  (Cloudflare 1010); use REST api.parallel.ai/v1/tasks/runs directly.
- Wave-2 deep research LAUNCHED (pro-fast, $0.10): trun_4dd3f131a592407
  cbfde93c94ca73dc5 "where AI-built software fails + human-in-the-loop
  UX patterns + policy-adherence benchmarks". Poller proc_a0bb48cf7370
  saves result to research/raw/wave2-ai-failures.json when done.

## COMMITS
- a59e710: build-spec-3 done + kits (badge fix, feeds kit, traversal,
  5 fixtures, topic universe, benchmarks, stress bench)
- 69b2750: drills + numbers 81/81
- 1454d2d: runbook kit matrix + live data + honesty moment
- (pending) runbook pre-warm + gitignore + UI brief draft

## MISTAKES / LESSONS
1. My first stress-run S2 assertion was wrong-headed (extractive offline
   summaries legitimately contain body text; injection claim is about
   owned fields). Fixed the test, not the product.
2. My first key-probe verdict "TASK-ALIVE: 0" was a false negative: the
   async accept is 202 (no run_id in sync response); probe.py treats 202
   as alive. Verified by classification logic, then by a REAL task
   launch that succeeded.
3. curl | python3 pipes trip the security scanner (auto-approved, noisy).
4. Terminal rejects foreground & -> background=true + separate checks
   (hit again, remember).
5. Cold pipeline with --feeds is 4-5 min (rate limits), NOT 40-50 s like
   the 22-item seed run. Pre-warm is mandatory. This is a real finding
   for demo timing.

## RULES IN FORCE (unchanged)
- All source code via opencode; Hermes = spec + audit + tests + commits.
- No em dashes, no AI-tell words. Research waves one by one.
- Everything committed, tree clean, local == remote.

## AFTERNOON WINDOW (13:00-14:30 IST, same day)

- Deck gap closed: BUILD-SPEC-4 via opencode (MCP slide on slide 5 +
  MCP-READY cover badge, all 4 skins), audited by Hermes, M1-M6 PASS
  independently (slide count 8 each, XML-verified, no em dashes).
- Prior-art round: waves 15-18 launched on fresh keys 145-148, all
  completed and integrated into research/PRIOR-ART-MAP-2026.md:
  shapes (stars + wedges), domains (three tensions), student builds +
  venues (demand signals, judge reality, venue recipe, evidence
  warning about the TiE/Code-N-Craft conflation), OSS stand-on map
  (compose list, traps, whitespace, vendorability matrix).
- Prewarm attempts: keyless run (my mistake, no key sourced, killed),
  keyed run hit sustained HTTP 429s (provider rate limit) and failed.
  Finding documented as the 429 WATCH in NIGHT-RUNBOOK: two-pass
  spaced pre-warm, warm cache fallback, honesty story. Cache baseline
  45 entries, not warmed.
- Honesty pass: evidence-chain legend added to both registries
  (wave numbers = source-cited, not independently re-measured),
  benchmark count corrected to ~250 named, stress canonical count
  confirmed at 83 + 10, WAVE-SYNTHESIS waves 15-18 indexed (wave-14
  header restored after a patch slip), atlas +2 files (82 total,
  1,022,706 chars, tests green), NUMBERS-2026 research coverage block.
- SUBMISSION-TEXT-KIT v2: 42 -> 81 acceptance checks fixed, evaluator
  closing line, format facts, fraud number block, honesty line.
- Commits: 7a78267, 46e32b1, 9dd1dd9, bf7ea4e, 9561959, bbe9c0b
  (pushed; plus concurrent idea-lab sync 9dd1705).
