# BUILD-SPEC-2 - the remaining 3 scaffold items (multimodal, provider adapter, provenance/consent)

Status: SPEC for immediate build (2026-08-14 evening, user "build everything" directive).
All items below are grounded in the current code (engine.py LLM class, approval.py,
serve.py route()). Tests are plain python3 acceptance suites like the existing ones.

## A. PROVIDER ADAPTER (30 min)

Problem: LLM calls are hardwired to ollama-cloud inside engine.py LLM.chat(). If a
problem forces a different provider (Google, Meta, Adobe-flavored endpoints) the
swap is a code edit. Sponsors want provable integration points.

Solution: scaffold/engine/providers.py
- class Provider (Protocol): chat(system, user, max_tokens, temperature) -> Optional[str]
- class OllamaProvider: current behavior (env OLLAMA_API_KEY, OLLAMA_BASE_URL, SIGNAL_MODEL), lazy env reads
- class NullProvider: returns None always (pure offline)
- PROVIDERS = {"ollama": OllamaProvider, "null": NullProvider}
- PROVIDER_NAME = os.environ.get("SIGNAL_PROVIDER", "ollama") read lazily in LLM.chat()
  (same lazy pattern as the key, so serve.py can force provider at runtime)
- LLM.chat(): provider = PROVIDERS[PROVIDER_NAME](); call it; keep cache + last_mode
  semantics exactly as today. Behavior of the pipeline MUST be unchanged when
  SIGNAL_PROVIDER is unset.

Tests test_providers.py P1-P4:
- P1: default (no env) behaves as today (cache works, offline fallback works)
- P2: SIGNAL_PROVIDER=null -> every chat returns None, last_mode "offline", no network
- P3: SIGNAL_PROVIDER=null set AFTER import still works (lazy read regression)
- P4: cache replay unaffected by provider choice

## B. MULTIMODAL INPUT ADAPTER (60-90 min)

Problem: predicted shapes 2/3/4 (Adobe, Apple, Meta) expect media input: image,
PDF, file attachments. Today the engine only takes text Items.

Solution: scaffold/engine/multimodal.py
- def extract_text(attachment_path: str) -> tuple[Optional[str], dict]:
  returns (text, meta). meta = {"extractor": name|None, "reason": str|None, "size": n}
  Extractors, tried in order:
    1. text/markdown/csv/json: builtin read (any extension)
    2. PDF: if "pypdf" importable, extract; else None with reason "pypdf not installed"
    3. image: if "tesseract" binary on PATH, subprocess OCR; else None "tesseract missing"
    4. else None with reason "no extractor for this type"
  Availability is detected at runtime, never hard-fails.
- serve.py: POST /api/ingest accepts JSON: {channel, sender, subject, body,
  attachment_path} (attachment_path is a local file path, demo mode). It runs
  extract_text, builds an Item (text or body + meta), appends to the feed cache,
  re-runs the pipeline, pushes a trace step "ingest:multimodal" with the meta.
  Response: {ok, item, extraction: meta}. 200 even when extraction is None
  (graceful: item still ingested with a note).
- fixture fixtures/multimodal.json: one text attachment case, one unsupported-type
  case (e.g. .exe), one no-attachment case. expected_multimodal.json: expected
  trace meta for each.

Tests test_multimodal.py M1-M4:
- M1: text attachment extracts and the item lands in /api/feed
- M2: unsupported type -> extraction None with a reason, item still ingested (200)
- M3: /api/trace shows the ingest:multimodal step with meta
- M4: no attachment -> body-only item, no extraction entry

## C. PROVENANCE + CONSENT RECORD (20-30 min)

Problem: rank-1 shape demands auditability ("typed audit trail"). Today the audit
log exists but there is no per-decision provenance manifest and no consent record.

Solution (extend approval.py + serve.py, additive):
- provenance: proposals table gains nothing; instead build the manifest on demand:
  GET /api/provenance/{proposal_id} -> {
    proposal_id, tool, params, reason, evidence,
    prompt_sha256: hash of the reason+evidence that fed the proposal,
    model: env SIGNAL_MODEL or "offline", generated_at (created_at),
    reviewed_by: actor, decided_at, decision: status
  } sourced from the proposals + audit_events rows (no new table needed).
- consent: new sqlite table consent (id, subject, scope, granted_by, granted_at,
  revoke_at NULL, UNIQUE(subject, scope)). serve.py: POST /api/consent
  {subject, scope, granted_by} -> grants a row (upsert). GET /api/consent -> list.
- propose() integration: when a side-effecting or reversible tool is proposed and
  no consent row exists for the proposal's evidence source subject, the proposal
  response gains "consent_required": true (the proposal still gets created as
  pending; the flag is informational for the UI).

Tests test_provenance.py Q1-Q4:
- Q1: after an approve decision, /api/provenance/P-xx returns all fields incl.
  prompt_sha256 (deterministic) + actor + decided_at
- Q2: POST /api/consent grants a row; GET lists it; duplicate grant upserts
- Q3: side-effecting propose without consent -> consent_required true
- Q4: with consent granted -> consent_required false

## Build rules
- Plain python3 stdlib only (tesseract/pypdf optional at runtime, never required).
- No em dashes in comments. No git commit. Do not modify deck/, docs/, research/.
- Run ALL suites at the end: test_providers, test_multimodal, test_provenance,
  test_trace, test_approval. Report pass counts per suite.
