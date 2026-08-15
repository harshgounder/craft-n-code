# BUILD-SPEC-3: badge honesty fix + real data kit (opencode build)

Craft N Code 2026 scaffold. Hermes wrote this spec; opencode implements it.
Both parts are small and independent. Keep every existing test green.

## GROUNDING (read these first)

- scaffold/webapp/serve.py: load_feed() lines 64-92, current_mode() lines
  95-107, /api/stats lines 239-247, main() CLI lines 345-369.
- scaffold/engine/engine.py: run_pipeline() line 315, llm dict lines
  349-350, LLM class near line 120, seed_items() line 361.
- scaffold/engine/providers.py: OllamaProvider.chat() catches all
  exceptions and returns None (prints to stderr); NullProvider returns
  None always. get_provider() resolves SIGNAL_PROVIDER.
- scaffold/demo.sh: 19 lines, DO NOT MODIFY.
- Existing tests pattern: scaffold/tests/test_*.py standalone plain
  python3, fresh DB per suite, wait_ready polling, per-suite isolation
  (delete engine/signal.db + engine/.llm_cache.json in setUp).

## PART 1: the mode badge must tell the truth (bug fix)

KNOWN LIE (reproduced Aug 14): with a broken API key, all 22 LLM calls
fail and fall back to offline rules, yet /api/stats reports
mode=live, model=deepseek-v4-flash:0731. Also: with NO key at all the
model label is "OFFLINE" but current_mode() still returns "live".
The honesty layer is blind on failure. This is the demo-critical bug.

### Changes

1. scaffold/engine/providers.py:
   - OllamaProvider.__init__ sets self.failures = 0.
   - In chat(), inside the except block: self.failures += 1.
   - NullProvider.__init__ also sets self.failures = 0 (never increments).
2. scaffold/engine/engine.py:
   - The LLM class tracks provider misses: every time
     provider.chat(...) returns None, increment a counter
     (self.provider_errors). This covers no-key, null provider, and
     failed network uniformly: if the model did not answer, that call
     is a provider miss.
   - Include it in the llm dict (line 349-350):
     "provider_errors": <count>, alongside model/cache_hits/cache_misses.
3. scaffold/webapp/serve.py current_mode() (lines 95-107), in order:
   - OFFLINE flag -> "offline" (unchanged)
   - FIXTURE -> "fixture" (unchanged)
   - llm.model == "db" -> "cached" (unchanged)
   - llm.model == "OFFLINE" -> "offline" (NEW: no-key case was lying)
   - llm.provider_errors > 0 -> "offline" (NEW: provider failed case;
     outputs were offline rules, so the badge must say offline)
   - cache_hits > 0 and cache_misses == 0 -> "cached" (unchanged)
   - else "live" (unchanged; a mix of hits and successful misses IS live)

### Acceptance (NEW file scaffold/tests/test_honesty.py, same suite pattern)

- H1: SIGNAL_PROVIDER=null, fresh DB, no fixture: /api/stats mode is
  "offline" (NOT live), llm.provider_errors >= 1. This is the regression
  for the badge lie.
- H2: OLLAMA_API_KEY removed from env (set to empty string), fresh DB:
  mode is "offline", llm.model == "OFFLINE".
- H3: seed a DB row first (use E.Item + a direct insert via sqlite3, or
  reuse E.run_pipeline once with seed_items and persist), then start the
  server: mode is "cached".
- H4: --fixture happy: mode is "fixture".
- H5: --offline flag: mode is "offline".
- H6: valid key present (read from env, skip the assertion if
  OLLAMA_API_KEY is empty): fresh DB, mode is "live" and
  provider_errors == 0. (This needs the real key at run time; the test
  skips the live assertion when the env var is absent, like H2 setup.)

## PART 2: real data kit (live feeds into the demo)

The demo should show REAL recorded problems, not just seed data. Three
public, key-free sources, stdlib-only fetcher, cached fallback, honest
freshness metadata. Same philosophy as the mode badge: the UI always
knows whether data is live, cached, or offline.

### NEW file scaffold/engine/feeds.py (stdlib only)

- SOURCES (name, url, kind, extractor):
  - "hn": https://hn.algolia.com/api/v1/search?tags=front_page (kind
    "news"). Extractor: hits[] -> {title, body: story_text or title,
    url: url or points}.
  - "github": https://api.github.com/search/repositories?q=agentic+ai&sort=stars&order=desc&per_page=10 (kind "repo"). Extractor: items[] -> {title: full_name, body: description or "", url: html_url}.
  - "unstop": https://unstop.com/api/public/competition/1730314 (kind
    "event"). Extractor: single object -> {title: name or title, body:
    short text with registrations/prize if present, url: the page url if
    present}. Keep the record small.
- fetch_source(src): urllib.request with timeout=10, User-Agent header
  (GitHub rejects no-UA). Returns (records: list[dict], error: str|None).
- refresh(outdir): fetch all sources, write outdir/<name>.json (list of
  records; empty list on error) and outdir/_meta.json:
  {"fetched_at": iso, "sources": {"hn": {"status": "ok"|"error",
  "count": N, "error": "..."}}}. ALWAYS exit 0 even when every source
  fails; the meta file is the honest record.
- to_items(records): -> list[E.Item] with channel=source name,
  source_id=record url or title slug, subject=title, body=snippet,
  received_at=fetched_at, kind=record kind.
- load_feeds(feeds_dir): -> (items: list[E.Item], meta: dict|None).
- CLI:
  - `python3 engine/feeds.py --refresh` -> network fetch, write files.
  - `python3 engine/feeds.py --offline` -> no network, write _meta.json
    with status "error" and error "offline" for every source, exit 0.
  - `python3 engine/feeds.py --dump` -> print to_items JSON to stdout.

### serve.py changes

- Import feeds (sys.path already includes engine/).
- New global FEEDS: bool = False. New CLI flag --feeds (argparse,
  store_true).
- load_feed(): when FEEDS is set and data/feeds has items:
  FEED_CACHE = E.run_pipeline(items, profile) (the REAL pipeline, so the
  LLM layer runs live when the key works); FEED_CACHE["feeds_meta"] =
  meta. If no feed files exist, fall through to existing behavior.
- New endpoint GET /api/feeds: read data/feeds/_meta.json; reply
  {"sources": [...], "mode": "live" if any source ok and fetched within
  30 minutes, "cached" if files exist but stale or all errored, "offline"
  if no files}. (This is DATA freshness, separate from the LLM mode
  badge.)
- /api/stats: when FEEDS is active, include "feeds": meta.
- demo.sh stays untouched; the night flow calls feeds.py --refresh, then
  serve.py --feeds.

### Acceptance (NEW file scaffold/tests/test_feeds.py, same suite pattern)

- F1: run `python3 engine/feeds.py --offline` from scaffold/: exit 0,
  data/feeds/_meta.json exists, every source status "error". Deterministic,
  zero network. (Clean data/feeds before and after the test.)
- F2: SIGNAL_PROVIDER=null + serve.py --feeds on a fresh port: GET
  /api/stats mode == "offline"; GET /api/feeds returns 200 with "sources"
  and a "mode" key; GET /api/feed returns 200. Zero network.
- F3: same as F2 but with OLLAMA_API_KEY set: mode is "live" and
  llm.provider_errors == 0 when the key works (skip the live assertion
  when env key is empty, same guard as H6).
- F4: DB isolation: suite deletes engine/signal.db + engine/.llm_cache.json
  in setUp, like every other suite.

## PART 3: static path traversal hygiene (found by Hermes stress bench S8)

serve.py static branch serves STATIC / parts[1] without checking "..".
/static/../engine/engine.py resolves parts[1]=".." to the webapp parent
dir: the server sends HTTP 200 then crashes reading the directory. It
cannot escape the repo, but a 200-then-crash on a traversal is bad
hygiene on a security-judged stage.

Fix in scaffold/webapp/serve.py static branch: reject the request with
404 when any segment in parts[1:] equals ".." (or "." or is empty after
strip), and also resolve the target and require it to be inside
STATIC.resolve() before serving. Keep everything else identical.

Acceptance: S8 in scaffold/tests/test_stress.py asserts 404 for
/static/../engine/engine.py and still 200 for /static/<real file>.
(Hermes updates the assertion; opencode just fixes serve.py.)

## BOUNDARY RULES (hard)

- Files open to change: scaffold/engine/providers.py,
  scaffold/engine/engine.py, scaffold/webapp/serve.py. NEW files:
  scaffold/engine/feeds.py, scaffold/tests/test_honesty.py,
  scaffold/tests/test_feeds.py.
- DO NOT modify: webapp/static/index.html, webapp/static/*, fixtures/,
  deck/, demo.sh, atlas/, tests other than the two new files, README.
- Keep zero external deps (stdlib only, urllib/json/sqlite3/threading).
- No em dashes in any comment or string ("--feeds" flag name is fine,
  it is a double hyphen by design).
- Do NOT git commit. Do NOT push. Do NOT touch the repo outside
  scaffold/.
- Use the existing test pattern (plain python3, wait_ready, fresh DBs).

## SUCCESS

- `python3 tests/test_honesty.py` and `python3 tests/test_feeds.py`
  green, run from scaffold/tests/.
- All existing suites still green (42/42: approval 13, trace 12,
  providers 9, multimodal 4, provenance 4).
- Manual check (Hermes does this after you): cold run with garbage key
  -> mode=offline; cold run with real key -> mode=live; warm DB ->
  cached; --fixture -> fixture; --offline -> offline; --feeds -> real
  items in /api/feed with feeds_meta.
- Report: list every file changed, pass counts per suite, anything you
  could not do.
