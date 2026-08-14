# Signal Engine + Scaffold — Craft N Code 2026 (Team 511)

One engine, many skins. Whatever problem drops Aug 15 21:30, this is pre-built.

```
scaffold/
├── demo.sh                 one command: generate feed + serve UI
├── engine/
│   ├── engine.py           ingest → dedupe → summarize → rank → deadlines
│   └── signal.db           (generated, gitignored)
├── webapp/
│   ├── serve.py            zero-dependency HTTP server (stdlib only)
│   └── static/index.html   the UI (dark, mobile-friendly, 3 tabs)
└── deck/
    ├── deck-gen.js         one skeleton → 4 idea decks
    ├── deck-signal.pptx    PS-03 skin
    ├── deck-pulse.pptx     PS-01 skin
    ├── deck-nightops.pptx  PS-02 skin
    └── deck-kavach.pptx    PS-04 skin
```

## Quickstart

```bash
# with the ollama-cloud key (recommended)
export OLLAMA_API_KEY=...          # from ~/.hermes/.env
./demo.sh                          # opens http://localhost:8137

# or totally offline (zero network, zero keys)
./demo.sh
```

The engine tries the LLM (summarize + deadline extraction), falls back to
rule-based offline mode if no key/network. The demo never dies.

## API (Supabase-shaped JSON)

| Route | What |
|---|---|
| GET /api/feed | ranked feed |
| GET /api/digest | "today in 60 seconds" |
| GET /api/search?q=mte | semantic-ish search over all channels |
| GET /api/complaints | complaint board |
| POST /api/complaints | file a complaint (auto-triage + SLA) |
| GET /api/stats | channel counts, deadlines found |

## Engine pipeline

1. ingest: 6 channels (Gmail IMAP, Classroom API, Unstop API, portal scrape,
   WhatsApp export, Instagram seed)
2. dedupe: normalized fingerprint, keep newest
3. summarize: LLM one-liner (ollama-cloud deepseek-v4-flash:0731), offline
   extractive fallback
4. rank: profile match + sender authority + recency + deadline pressure + urgency
5. deadlines: LLM extraction with regex fallback, ISO output

## On the night (Aug 15 21:30)

1. Problem drops -> decision tree (research/IDEA-BANK.md)
2. Pick the matching deck file, pick the skin
3. `./demo.sh` on the stage laptop, or play the pre-recorded video
4. Submit before 06:00 Aug 16

## Rules it follows

- Zero paid keys. Zero external deps in the demo. (AFTERPACKETS rule: they won
  2025 partly because their demo had no external dependencies.)
- No em dashes anywhere in this repo.
- Everything verified before claiming: run `python3 /tmp/hermes-verify-scaffold.py`.
