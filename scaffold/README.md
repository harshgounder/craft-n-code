# Signal Engine + Scaffold  -  Craft N Code 2026 (Team 511)

One engine, many skins. Whatever problem drops Aug 15 21:30, this is pre-built.

```
scaffold/
├── demo.sh                 one command: generate the feed + serve the web UI
├── engine/
│   ├── engine.py           the pipeline: ingest → dedupe → summarize → rank → deadlines
│   │                       LLM via ollama-cloud (deepseek-v4-flash:0731) + FULL offline
│   │                       fallback (regex deadlines + tf-idf ranking). Domain-agnostic:
│   │                       feed ANY JSON items, works on any problem domain.
│   └── signal.db           (generated, gitignored)
├── webapp/
│   ├── serve.py            zero-dependency HTTP server (stdlib only, python3)
│   └── static/index.html   dark UI: digest, ranked feed, search, complaint board
└── deck/
    ├── deck-gen.js         pptxgenjs: ONE skeleton, 4 decks
    ├── deck-agentic.pptx     BriefLens (agentic ops / approval gate)
    ├── deck-multimodal.pptx  Kavach Circle (multimodal assistant + escalation)
    ├── deck-creative.pptx    SignalStory (brief → asset with provenance)
    └── deck-kavach.pptx      Kavach (call-security platform, real product)
```

## Quick start

```bash
# generate the feed + serve the UI (LLM if OLLAMA_API_KEY set, offline otherwise)
./demo.sh            # -> http://localhost:8137

# stage deploy on 0.0.0.0:8137 with auth (AUTH_TOKEN env or first arg)
./deploy.sh mytoken  # -> stage mode with auth; ./demo.sh stays local-only

# or run the engine directly
cd engine
python3 engine.py --seed --digest          # offline-safe digest
OLLAMA_API_KEY=... python3 engine.py --seed --digest   # LLM mode
python3 engine.py --seed --out feed.json   # full JSON result
python3 eval/eval.py --all   # eval gate (offline-safe), --live for LLM spot checks
```

## The pipeline (domain-agnostic)

1. INGEST: any JSON items (channel, sender, subject, body, received_at, tags)
2. DEDUPE: normalized subject+body fingerprint
3. SUMMARIZE: LLM one-liner (cached per item), or extractive offline
4. RANK: sender authority + profile-tag overlap + recency + deadline pressure
5. DEADLINES: regex extraction (multiple formats) + urgency flagging
6. PERSIST: SQLite (Supabase-ready shape)

Verified: 13/13 ad-hoc checks (offline + LLM mode, webapp end to end, decks).

## On the night (Aug 15, 21:30 drop)

1. Read the drop for the company fingerprint (cue table in IDEA-BANK §5.5)
2. Pick the matching deck + storyboard (4 pre-built)
3. Swap the seed feed for the real domain (10-30 min, engine untouched)
4. ./demo.sh or play the video; submit before 06:00
