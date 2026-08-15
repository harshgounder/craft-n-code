# BACKEND-DRILLS-2026.md: practice until the stack is muscle memory

Purpose: every team member must be able to operate the scaffold blindfolded.
These drills are the "practice a lot of backend" program. Each drill is
timed, has a failure state, and a recovery script. Run each at least
twice before 18:00. Target times in brackets.

Setup: repo at ~/craft-n-code, python3 only, zero deps, nothing to
install. The stack: engine (pipeline) -> webapp (serve.py) -> skins
(fixtures) -> feeds (real data kit) -> tests (8 suites, 81 checks).

## DRILL 1: COLD BOOT (target 60s, the night-opener)
1. Fresh checkout state: rm -f engine/signal.db engine/.llm_cache.json
2. Export OLLAMA_API_KEY (anchored grep: grep '^OLLAMA_API_KEY=' ~/.hermes/.env | head -1 | cut -d= -f2-)
   WARNING: the .env has a COMMENTED placeholder line (# OLLAMA_API_KEY=...).
   A naive grep glues comment + real key into one broken header. Always
   anchor with ^ and strip the comment.
3. ./demo.sh 8137 in background
4. curl localhost:8137/api/stats -> expect mode=live (or offline if no key),
   llm.provider_errors present, total >= 1
5. Kill: pkill -f "[s]erve.py" (bracket trick, never bare pattern)
Pass: server up in < 20s, stats honest, no zombie processes.

## DRILL 2: THE HONESTY DRILL (target 90s, the judge's favorite moment)
1. Start serve.py cold with the real key. Confirm mode=live.
2. In a second terminal: export OLLAMA_API_KEY="" and hit
   curl localhost:PORT/api/stats (new pipeline run via POST /api/ingest).
3. Watch the badge flip to offline. That is the honesty moment: show it
   on stage if time allows. "When the model dies, the system says so and
   keeps working."
4. Restore the key, POST /api/ingest again, badge flips back.
Pass: badge always matches reality (provider_errors > 0 -> offline).

## DRILL 3: LIVE DATA (target 90s, the real problems moment)
1. python3 engine/feeds.py --refresh  (fetches HN + GitHub + Unstop, writes data/feeds/)
2. Check data/feeds/_meta.json: status per source, fetched_at.
3. Start serve.py --feeds 8138. GET /api/feeds -> mode live when fresh.
4. GET /api/feed -> real items ranked. GET /api/stats -> llm real.
5. Kill the wifi (or run feeds.py --offline) -> /api/feeds mode cached,
   feed still renders from stale files. Honest degradation.
Pass: live data in the demo, badge tells the truth on failure.

## DRILL 4: SKIN MOUNT (the measured 15-40 min claim, use MOCK-DROPS)
1. Pick a mock drop, fingerprint it (2 min), decide the kit.
2. cp fixtures/<kit>.json fixtures/current.json (or use --fixture <kit>)
3. ./demo.sh -> feed shows the kit's items, proposals fire.
4. Time the whole thing. Log it in MOCK-DROPS metrics.
Pass: mounted and demoing in under 40 min on the first try, under 20 on
the second.

## DRILL 5: RECOVERY (target 120s, what breaks at 3 AM)
Scenarios, each timed:
a. Port busy: lsof -i :8137 (or fuser) -> pick a new port, restart.
b. DB locked: stale serve.py holds signal.db. pkill -f "[s]erve.py",
   wait 2s, restart. If still locked: rm -f engine/signal.db.
c. LLM quota dead: OLLAMA_API_KEY valid but 402/429 in log -> the badge
   flips to offline by itself (provider_errors). Demo continues. No code
   change needed. This is the design.
d. Feed files missing: feeds.py --refresh fails on no wifi -> run
   feeds.py --offline, or serve without --feeds (falls back to seed).
e. Cache poisoned: weird summaries in UI -> rm -f engine/.llm_cache.json,
   restart, cold run rebuilds it.
Pass: every recovery under 2 min, no code edits.

## DRILL 6: THE FULL TEST GAUNTLET (target 3 min, the numbers moment)
cd scaffold/tests && for t in test_approval test_trace test_providers \
  test_multimodal test_provenance test_honesty test_feeds test_stress; do \
  python3 $t.py; done
Pass: 81/81. Count it out loud: 13 + 12 + 9 + 4 + 4 + 8 + 8 + 23 = 81.
Fresh DBs every run, order-independent. This is the "how do you know it
works" answer.

## COMMAND CHEAT SHEET (print this)
- serve:            python3 webapp/serve.py [--port N] [--fixture NAME] [--offline] [--feeds]
- feeds refresh:    python3 engine/feeds.py --refresh | --offline | --dump
- kill server:      pkill -f "[s]erve.py"        (bracket trick)
- key export:       export OLLAMA_API_KEY=$(grep '^OLLAMA_API_KEY=' ~/.hermes/.env | head -1 | cut -d= -f2-)
- force offline:    export SIGNAL_PROVIDER=null OLLAMA_API_KEY=""
- test gauntlet:    cd scaffold/tests && for t in test_*; do python3 $t.py; done
- demo:             ./demo.sh [port]
- trace ring:       curl localhost:PORT/api/trace
- proposals:        curl localhost:PORT/api/proposals
