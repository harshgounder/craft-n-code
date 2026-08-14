# CODE-WALKTHROUGH - every file, every function, why it exists

Written 2026-08-14 for Harsh (Team 511 lead). Read this with the code open
next to you. This covers the CURRENT scaffold (engine, webapp, deck, demo).
The approval gate + trace viewer sections get appended when that build lands.

---

## 0. THE WHOLE SYSTEM IN ONE PARAGRAPH

You have a pipeline (engine.py): it takes raw messages from any channel,
throws away near-duplicates, writes a one-line summary for each (using a
real LLM when a key is present, using rules when it is not), ranks them by
"how much do you need to care", and extracts deadlines. That result is
saved into a tiny SQLite database (signal.db). A web server (serve.py,
stdlib only) reads that database and serves it over HTTP as JSON. A single
HTML page (index.html, no frameworks) fetches that JSON and paints it as a
dark dashboard: a "today in 60 seconds" digest, a ranked feed, a search
box, and a complaints board. The decks (deck-gen.js) are a separate story:
one Node.js script generates 4 PowerPoint decks, each a different skin of
the same idea, so on the night you pick the deck that matches the released
problem and submit it as the mandatory PPT.

Data flow: demo.sh -> engine.py -> signal.db -> serve.py -> index.html (browser).

---

## 1. demo.sh (19 lines) - the one-command runner

```bash
#!/usr/bin/env bash
set -euo pipefail
PORT="${1:-8137}"
cd "$(dirname "$0")"
```

- `set -euo pipefail`: bash safety flags. `-e` = exit on any error,
  `-u` = error on undefined variables, `-o pipefail` = a failing command
  mid-pipe fails the whole pipe. This makes the script fail loudly instead
  of half-working silently. Production habit, always put this at the top.
- `PORT="${1:-8137}"`: first argument is the port, default 8137 if none.
  The `:-` syntax means "if unset or empty, use the default".

```bash
if [ -n "${OLLAMA_API_KEY:-}" ]; then
  echo "[demo] using ollama-cloud LLM"
else
  echo "[demo] no OLLAMA_API_KEY -> offline mode (rule-based, zero network)"
  export OLLAMA_API_KEY="${OLLAMA_API_KEY:-}"
fi
python3 engine/engine.py --seed --out webapp/static/demo-feed.json >/dev/null
```

- If the LLM key env var is set, the demo uses the real LLM. If not, it
  still works: the engine falls back to offline rules. This is the
  AFTERPACKETS lesson: the demo never depends on a network.
- `python3 engine/engine.py --seed --out ...`: runs the pipeline on the
  built-in seed data and writes the JSON result. `>/dev/null` hides the
  noisy progress output.

```bash
exec python3 webapp/serve.py --port "$PORT"
```

- `exec` replaces the shell process with the server process (so Ctrl+C
  kills the server directly). The last line is the actual product: a web
  server.

NOTE (honest wart): the `--out webapp/static/demo-feed.json` file is not
actually read by serve.py. serve.py reads signal.db (which engine.py also
writes during the same run). demo-feed.json is a leftover artifact. It will
become useful when the fixture/replay mode lands (offline deterministic
replay). Nothing breaks, but know that it is currently dead weight.

## 2. engine/engine.py (433 lines) - the brain

### 2.1 The data model: Item (lines 35-59)

```python
@dataclass
class Item:
    channel: str            # where it came from: email | chat | portal | app | social | ticket
    source_id: str          # unique id within that channel (e1, p1, t1...)
    sender: str             # who sent it (Registrar Office, User (A. S.)...)
    subject: str
    body: str
    received_at: str        # ISO timestamp
    profile_tags: list      # tags describing YOU: ["2nd-year", "E&CE", "hostel"]
    kind: str = "notice"    # notice | complaint | deadline | event
    summary: str = ""       # filled by the summarize step
    rank_score: float = 0.0 # filled by the rank step
    deadline: Optional[str] = None
    deadline_iso: Optional[str] = None
    is_urgent: bool = False
```

Why a dataclass? Because every item is the SAME shape everywhere: engine,
database, JSON API, UI. One definition, no drift. This is the "schema
first" habit: define your data shape once, then everything else is
mechanical.

```python
def dedupe_key(self) -> str:
    s = re.sub(r"[^a-z0-9]+", "", (self.subject + " " + self.body).lower())[:120]
    return s
```

- `dedupe_key`: a fingerprint of the item. Lowercase, strip everything that
  is not letters/digits, take the first 120 chars of subject+body. Two
  items that say the same thing produce the same fingerprint, so the
  pipeline can drop one. This is a cheap near-duplicate detector: it is
  not perfect (a 2-char difference changes the key) but it is zero-cost.

```python
def as_dict(self):
    return asdict(self)
```

- Converts the dataclass to a plain dict so it can be JSON-serialized.

### 2.2 The LLM layer: class LLM (lines 65-122)

```python
class LLM:
    def __init__(self, cache_path=CACHE_PATH):
        ...
        self.cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
        self.hits = 0
        self.misses = 0
```

- The LLM object loads a DISK CACHE (`.llm_cache.json`) at startup. Every
  question it has already answered is stored there.

```python
def chat(self, system, user, max_tokens=400, temperature=0.2):
    key = hashlib.sha256((system + "\x00" + user).encode()).hexdigest()[:32]
    if key in self.cache:
        self.hits += 1
        return self.cache[key]
    self.misses += 1
    if not OLLAMA_KEY:
        return None
    ...
```

- The cache key is a hash of (system prompt + user prompt). Same inputs =
  same hash = cache hit = no network call, no cost, fast, deterministic.
- If there is no API key at all, `chat` returns None and the caller falls
  back to offline rules. This is the "offline mode" backbone.
- If a key exists, it POSTs to ollama-cloud (OpenAI-compatible endpoint)
  using urllib (stdlib, zero dependencies). Any exception = return None =
  offline fallback. The demo NEVER dies.

Why temperature 0.2? Low temperature = less creative, more consistent.
For summarization and deadline extraction you want consistency, not poetry.

### 2.3 The offline fallback (lines 129-247) - pure rules, deterministic

```python
MONTHS = {m: i + 1 for i, m in enumerate([...])}   # "jan" -> 1 ... "dec" -> 12
DATE_PATTERNS = [ ... 4 regexes ... ]
DEADLINE_WORDS = ["last date", "deadline", "due", "submit by", "before", "by "]
URGENT_WORDS = ["urgent", "immediate", ..., "fee", "fine", "suspend", "ragging"]
```

- 4 regexes cover the common Indian date formats: "22 Aug 2026",
  "Aug 22, 2026", "22/08/2026", and "22 Aug" (year implied = nearest
  upcoming).
- DEADLINE_WORDS: a date only counts as a deadline if a deadline-ish word
  is near it, or the item kind IS a deadline. Prevents "the party was on
  15 Aug" from being flagged.
- URGENT_WORDS: words that bump the urgency score. Includes fee/fine/exam
  because in a campus context those are the scary ones.

```python
def parse_date(text, today) -> Optional[date]: ...
def offline_summarize(item) -> str:
    first = text.split("\n")[0]  # first sentence
    ...truncate at 140 chars at a word boundary...
    return f"{item.subject} | {first}"
```

- `offline_summarize` is extractive: it takes the first line and clips it.
  No intelligence, but it never fails. The LLM summary replaces this when
  available.

```python
def offline_rank(items, profile, today) -> list[Item]:
    # TF-IDF-ish: words that appear in few documents are more distinctive
    ...
    AUTHORITY = {"registrar": 5, "dean": 5, ..., "student": 1, "bot": 1}
```

The rank score is a weighted sum of 5 signals:
1. Profile match (+2.5 max): does the item use words from YOUR tags
   ("e&ce", "hostel")? If yes, you should care.
2. Sender authority (+5 to +1): Registrar outranks a random bot. This is a
   hardcoded table, the demo's stand-in for a learned trust model.
3. Recency (+2 max): items 0-2 days old get full points, decays to 0 over
   a week. Fresh = relevant.
4. Deadline pressure (+3 max): the closer the deadline, the higher. A
   MISSED deadline is -3 (punished, should have been handled).
5. Urgency words (+1.2): "urgent", "fee", "fine"...

`is_urgent = score >= 6.0`. Then items are sorted descending. This is the
core "what should I care about" logic, and it is fully deterministic:
same input, same output, forever. That is what makes it demoable offline.

### 2.4 The pipeline (lines 254-314)

```python
SUMMARIZE_SYSTEM = ("You compress student notices to ONE line (max 140 chars)...")
DEADLINE_SYSTEM = ("Extract the single most important deadline... Today is {today}.")
```

- These are the system prompts. Notice the deadlines prompt tells the LLM
  what TODAY is, so "submit by Friday" resolves correctly. Context matters:
  an LLM without today's date cannot resolve relative dates.

```python
def llm_summarize(llm, item): 
    out = llm.chat(SUMMARIZE_SYSTEM, ...)
    return out.strip()[:160] if out else offline_summarize(item)

def llm_deadline(llm, item, today):
    out = llm.chat(...)
    m = re.search(r"\d{4}-\d{2}-\d{2}", out)   # grab the ISO date from the answer
    return m.group(0) if m else offline_extract_deadline(item, today)
```

- Pattern: TRY LLM, FALL BACK TO RULES. The regex salvages even a messy
  LLM answer ("the deadline is 2026-08-19 for sure!") by extracting the
  ISO date pattern. Never trust the model's formatting; extract structure
  from its output.

```python
def dedupe(items):
    seen = {}
    for it in items:
        k = it.dedupe_key()
        if k in seen:
            if it.received_at > seen[k].received_at:  # keep the NEWER one
                seen[k] = it
        else:
            seen[k] = it
    return list(seen.values())
```

- One dict, one pass. Duplicates resolved in favor of the newer item.

```python
def run_pipeline(items, profile, today=None) -> dict:
    today = today or date.today()
    llm = LLM()
    items = dedupe(items)
    for it in items:
        it.summary = llm_summarize(llm, it)
        it.deadline_iso = llm_deadline(llm, it, today)
    ranked = offline_rank(items, profile, today)
    return {"generated_at": ..., "today": ..., "llm": {...}, "profile": ...,
            "total": len(ranked), "items": [...]}
```

- The orchestrator: dedupe -> summarize each -> extract each deadline ->
  rank. Returns a self-describing JSON envelope: what model was used, how
  many cache hits, when it ran. That envelope is what the web layer serves.

### 2.5 Seed data (lines 321-372)

`seed_items()` returns 8 notices + 3 complaints, all shaped like real MUJ
communication (exam schedule, fee due, assignment, room change, hackathon
regs, library fines, backlog forms + 3 facility complaints). This is the
DEMO domain: on the night you replace this function's data (or the JSON
feed) with the problem statement's domain. The pipeline itself never
changes. That is the whole strategy: ONE engine, swap the seed.

### 2.6 CLI + persistence (lines 379-433)

```python
ap.add_argument("--seed", ...)  # run on demo data
ap.add_argument("--json", ...)  # dump full JSON
ap.add_argument("--digest", ...)# print the "today in 60 seconds" digest
```

- `--digest` prints the urgent items + top 5. This is the terminal version
  of the UI digest. Great for a quick live check during the demo.

```python
conn.execute("DROP TABLE IF EXISTS items")
conn.execute("""CREATE TABLE items (...)""")
for it in result["items"]:
    conn.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?,?,?,?)", (...))
conn.commit()
```

- Writes to signal.db with a hard schema. NOTE: it DROPS and recreates the
  table every run. Fine for a demo (always fresh), but in production you
  would use INSERT OR REPLACE and never drop. The comment says
  "Supabase-ready shape": same column names would map to a Postgres table
  if we ever move to Supabase for the nationals build.

## 3. webapp/serve.py (193 lines) - the zero-dependency web layer

### 3.1 load_feed (lines 41-64)

```python
FEED_CACHE = None   # module-level cache: computed ONCE per server process
def load_feed(profile=None):
    global FEED_CACHE
    if FEED_CACHE is not None: return FEED_CACHE
    if DB.exists():  # read items from signal.db
        rows = conn.execute("SELECT ... FROM items").fetchall()
        ... rebuild Item objects ...
    # no db -> run the engine fresh
    FEED_CACHE = E.run_pipeline(E.seed_items(), profile)
    return FEED_CACHE
```

- Strategy: DB first (fast, deterministic, already computed), engine fresh
  only if no DB. Result cached in memory for the server's lifetime. Every
  API call after the first is instant.
- The `global FEED_CACHE` is the simplest cache there is. In production
  you would use a proper cache layer, but for a demo this is correct and
  honest.

### 3.2 search (lines 67-78)

```python
def search(items, q, top=5):
    terms = [t for t in re.findall(r"[a-z0-9]{2,}", q.lower())]
    ...
    s = sum(hay.count(t) * (2 if t in it["subject"].lower() else 1) for t in terms)
```

- Keyword scoring: count how often each query word appears in
  subject+body+summary+sender, double-weight subject hits. Sort by score,
  return top 5. This is "semantic-ish" search: honest keyword ranking, no
  embeddings, zero deps. On the night, this is what answers "what is due
  this week?" in the demo.

### 3.3 route (lines 81-148) - the entire API in one function

```python
if parts[0] == "api":
    feed = load_feed()
    if parts[1] == "feed":     return json_reply(handler, feed)
    if parts[1] == "digest":   ... urgent + top 5 ...
    if parts[1] == "search":   ... query param q ...
    if parts[1] == "complaints": GET lists, POST adds a ticket
    if parts[1] == "stats":    ... channel counts, deadlines, skin_ready ...
```

- Every endpoint is 3-10 lines. The POST /api/complaints handler (lines
  122-134) shows the pattern for POST: parse JSON body, build a new item
  with a generated ticket id (#C-115 style), return 201 with the ticket
  number. This is the template the approval gate endpoints will follow.

### 3.4 json_reply + Handler (lines 151-181)

```python
def json_reply(handler, obj, code=200):
    data = json.dumps(obj).encode()
    handler.send_response(code)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)
```

- Every JSON response goes through one function: correct Content-Type,
  correct Content-Length, correct status code. One place to fix if
  something is wrong.

```python
class Handler(BaseHTTPRequestHandler):
    def _serve(self, method):
        parsed = urllib.parse.urlparse(self.path)
        body = None
        if method == "POST":
            length = int(self.headers.get("Content-Length") or 0)
            if length:
                body = json.loads(self.rfile.read(length).decode())
        route(self, self.path, method, body)
```

- `BaseHTTPRequestHandler` is the stdlib HTTP server. This class adapts it:
  parse the URL, read the POST body as JSON, delegate to route(). The
  `log_message` override silences the per-request logging noise.

## 4. webapp/static/index.html (245 lines) - the UI

### 4.1 The design system (lines 8-12)

```css
:root{
  --bg:#0B1020; --panel:#141B33; --panel2:#1B2440; --line:#263055;
  --txt:#E8ECF8; --mut:#93A0C4; --accent:#6C5CE7; --accent2:#00CE8F;
  --warn:#FFB020; --danger:#FF5470; --chip:#202A4E;
}
```

- CSS custom properties = one palette, used everywhere. Change one variable,
  the whole app re-themes. This is the same "define once, use everywhere"
  habit as the Item dataclass. The dark navy/purple/mint theme is the
  Signal look.

### 4.2 The page structure (lines 76-135)

- header: logo + status chips (llm mode, item count)
- digest section: "Today in 60 seconds"
- stats section: 4 stat cards
- tabs: Feed / Ask / Complaints (a fourth tab, Actions, is coming with the
  approval gate)
- three views, toggled with the `.hide` class
- footer: honest line: "Demo runs on pre-imported campus data. Zero
  external services needed."

### 4.3 The JavaScript (lines 137-243)

```js
const $ = id => document.getElementById(id);          // shorthand
let FEED = {items: []};
async function jget(u){ const r = await fetch(u); return r.json() }  // GET + parse
```

- `$` is a one-character DOM shortcut. `jget` is the fetch wrapper: every
  GET in the app goes through it.

```js
async function load(){
  const [feed, digest, stats] = await Promise.all([
    jget('/api/feed'), jget('/api/digest'), jget('/api/stats')]);
  ...
}
```

- Promise.all: fetch all three endpoints CONCURRENTLY, wait for all. The
  UI paints once, not three times.

- renderStats builds 4 stat cards from /api/stats. renderDigest paints the
  urgent items with a URGENT tag + deadline. renderFeed paints the ranked
  cards with rank number, channel icon, subject, summary, sender, deadline.

```js
const CH_ICON = {email:'📧', portal:'🏛', chat:'💬', app:'📱', social:'📸', ticket:'🛠'};
```

- Channel -> emoji map. Small touches sell the demo.

```js
async function doSearch(){ ... fetch('/api/search?q='+encodeURIComponent(q)) ... }
```

- encodeURIComponent is IMPORTANT: it escapes the query so "what's due?"
  does not break the URL. Always encode user input in URLs.

```js
const SLA = [['open',1.0], ['in-progress',.6], ['fixed',0]];
```

- Complaint status -> progress bar width. A ticket that is "open" shows a
  full bar (100% of its SLA budget used), "in-progress" 60%, "fixed" 0%.

```js
function esc(s){
  return (s||'').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
}
```

- THE most important function in the file. It HTML-escapes any text that
  came from user input or the LLM before injecting it into innerHTML.
  Without this, a notice containing `<script>` would execute in the demo.
  This is XSS prevention, the security habit that matters. NEVER inject
  unescaped user/LLM text into innerHTML.

```js
document.querySelectorAll('.tab').forEach(t => t.onclick = () => { ...toggle .hide... });
```

- Tab switching: click a tab, hide all views except the matching one.

## 5. deck/deck-gen.js (259 lines) - 4 decks from one skeleton

### 5.1 The data: IDEAS (lines 11-156)

Four objects, one per deck: agentic (BriefLens), multimodal (Kavach
Circle), creative (SignalStory), kavach. Each has: accent color, title,
tagline, problemTitle, problem[], solutionTitle, solution[], demo[],
impact[][], roadmap[][]. THE CONTENT IS THE DECK. The code below is just a
painter for this data.

### 5.2 The painter: build(idea) (lines 162-257)

```js
const p = new pptxgen();
p.defineLayout({ name: "W", width: 13.33, height: 7.5 });  // 16:9 widescreen
```

- pptxgenjs is the ONLY external dependency in the whole scaffold (a node
  package, used at build time only, not in the demo).

- S1 Title: navy background, accent stripe, big title, tagline, team line,
  speaker notes attached (s.addNotes).
- S2 Problem: white slide, "The Problem" header, problemTitle, 3 numbered
  problem lines.
- S3 Solution: navy, 4 rounded rect cards.
- S4 Live Demo: "Live Demo (3 minutes)", 4 numbered steps, plus the backup
  line: "Pre-recorded demo video ready if projector or network fails."
- S5 Impact: 3 big numbers (e.g. "1 feed replaces N channels", "10s to
  know what needs action", "0 actions missed").
- S6 Roadmap: 24h / 1 wk / 1 mo / 90d boxes.
- S7 Team: 3 member cards with emoji + role.

```js
Object.values(IDEAS).forEach(build);
```

- One loop, 4 files: deck-agentic.pptx, deck-multimodal.pptx,
  deck-creative.pptx, deck-kavach.pptx.

Why decks matter MORE now: the live API intel (INTEL-20260814-EVENING.md)
shows the submission is PPT-ONLY (pdf/pptx, 50MB). The deck IS the
submission. On the night: pick the deck matching the sponsor fingerprint,
possibly tweak the problem lines, regenerate with `node deck-gen.js`,
upload. If we need to restate the actual problem statement, add a slide.

## 6. PRODUCTION LESSONS (what changes if this becomes real)

The scaffold is deliberately simple: stdlib only, no frameworks, no auth.
That is a FEATURE for the hackathon (nothing to install, nothing to break,
judges can run it on any laptop). But you asked to learn production, so
here is the honest diff between this and a production app:

1. Server: FastAPI/Flask instead of BaseHTTPRequestHandler (routing,
   validation, OpenAPI docs for free). Still python.
2. Auth: real login (session or JWT), roles (admin vs user), and the
   audit log keyed to authenticated actors, not a "judge" string.
3. Database: Postgres instead of SQLite, migrations (Alembic), no DROP
   TABLE on startup. SQLite is fine for a single laptop demo.
4. LLM calls: async, retries with backoff, timeouts, budget tracking,
   structured output parsing (JSON schema), fallback chains across
   providers, PII redaction before sending.
5. Frontend: a framework (React/Vue) or at least build tooling; but note
   the no-dependency single-file page has real value for demos and
   offline reliability.
6. Tests: pytest suite + CI (GitHub Actions), the acceptance tests we are
   writing for the approval gate are exactly the shape of a real test
   suite. Test the pipeline with golden fixtures (deterministic inputs,
   expected outputs).
7. Observability: structured logs (JSON lines), metrics, a trace of every
   decision. The /api/trace endpoint we are building is a mini version of
   this.
8. Security: rate limiting, input validation on every POST, escaping on
   every render (esc() everywhere), no secrets in code (env vars only).
9. Deployment: container (Docker), reverse proxy (nginx/Caddy), managed
   host. For the demo, `python3 serve.py` on a laptop is the deployment.
10. The one pattern that transfers as-is: TRY LLM, FALL BACK TO RULES,
    EXTRACT STRUCTURE FROM OUTPUT. That survives in every production AI
    app.

## 7. HOW TO AUDIT THE CODE YOURSELF (verify, don't trust)

```bash
cd ~/craft-n-code/scaffold
./demo.sh &                      # starts server on :8137
curl -s localhost:8137/api/stats | python3 -m json.tool   # stats
curl -s localhost:8137/api/feed | python3 -m json.tool    # full feed
curl -s "localhost:8137/api/search?q=fee" | python3 -m json.tool  # search
curl -s localhost:8137/api/digest | python3 -m json.tool  # digest
python3 engine/engine.py --seed --digest                  # engine alone
node deck/deck-gen.js                                     # regenerate decks
```

Read order for full understanding: demo.sh (what runs) -> engine.py
(the brain) -> serve.py (the API) -> index.html (the face) -> deck-gen.js
(the deck painter). ~90 minutes at a relaxed pace, ~30 if you skim the
offline regex parts.
