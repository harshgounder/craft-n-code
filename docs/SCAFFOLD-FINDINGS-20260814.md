# SCAFFOLD FINDINGS - Aug 14 21:00 (failure-injection drill results)

Purpose: the failure-injection drill (docs/NUMBERS-2026 section 1) run for
real on Aug 14 night. Two findings, one confirmed fix, one bug for opencode.

## FINDING 1 - the badge can lie (REAL BUG, fix brief below)

Scenario: LLM key present but broken (simulated by exporting a malformed key
that made the http client reject the header; every call fails). What the
scaffold did:
- Every one of the 22 pipeline calls failed and fell back to per-item offline
  rules (engine prints "[llm] ollama-cloud failed (...); using offline").
- /api/stats STILL reported: mode=live, model=deepseek-v4-flash:0731,
  cache_misses=22. Zero trace of the failure in the llm dict.
- The UI badge would have shown "live" while every output was deterministic
  fallback. On stage, with a dead LLM, we would claim a live model call that
  never happened. That breaks our own honesty story (the mode badge exists
  so "a judge always knows what is real").

Root cause: current_mode() (serve.py) only knows about flags (offline,
fixture) and the cache counters. It never learns whether provider calls
actually succeeded. The llm dict records model + cache_hits + cache_misses
but no provider outcome.

Repro (safe, in a copy): cp -r scaffold /tmp/cnc-inject; delete
engine/signal.db + engine/.llm_cache.json; export a deliberately broken
OLLAMA_API_KEY; run webapp/serve.py; curl /api/stats -> mode=live despite
all calls failing in the log.

## FINDING 2 - "LLM key verified live" was weak proof (now properly verified)

The earlier live check used curl https://ollama.com/v1/models which returns
200 WITHOUT any auth (public endpoint, useless as a probe). Confirmed today:
a garbage bearer token gets 401 on /v1/chat/completions, so auth IS
enforced. Proper verification done Aug 14 21:00:
- Chat completions with the real OLLAMA_API_KEY: HTTP 200 + real completion
  id, model deepseek-v4-flash:0731.
- Cold run of serve.py (fresh DB + fresh cache, key loaded correctly):
  12 real LLM calls succeeded (cache_misses=12, zero failures), 10 cache
  hits, mode=live, cache rebuilt. VERIFIED.
- Env lesson: the .env file has a COMMENTED placeholder line
  (# OLLAMA_API_KEY=your_ollama_key_here) and the real key on line 478.
  A naive grep that does not skip comments glues both into one broken
  header value. Load .env with a real parser or grep -v '^#'.

## FIX BRIEF FOR OPENCODE (source code, Hermes does not write code)

Bug: mode badge reports live when the provider failed and offline fallback
ran. Files: scaffold/engine/engine.py (pipeline llm metadata), maybe
scaffold/webapp/serve.py current_mode().

Desired behavior:
1. The engine counts provider failures during a pipeline run and exposes
   them in the llm dict, e.g. "provider_errors": N.
2. current_mode() returns "offline" whenever provider_errors >= 1 in the
   current run (the badge then tells the truth: outputs were offline rules).
   Optional: a 5th label "degraded" when SOME calls failed and some
   succeeded; default to offline if that is simpler.
3. Keep zero external deps. Keep the 42 existing tests green.
4. Add a regression test: run the pipeline with a guaranteed-broken key
   (or SIGNAL_PROVIDER=null) and assert /api/stats mode is NOT live.
   Test style: plain python3, fresh DB, wait_ready polling, per-suite
   isolation (see scaffold/tests/).

Acceptance: cold run with broken key -> mode=offline; cold run with valid
key -> mode=live; warm DB -> mode=cached (unchanged); --fixture -> fixture
(unchanged); --offline -> offline (unchanged). 43/43 green.
