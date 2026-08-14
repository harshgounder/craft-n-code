# CONTINUATION-PROMPT — Craft N Code (read this FIRST in a new window)

> Drop this file's contents (or this path) as the first message in a new Hermes window. It fully resets context. Written 2026-08-14 09:55 IST.

---

## WHO / WHAT

Team 511 (Harsh Gounder = lead, Ayush Kharwar, Sujal Shukla) is competing in the **Craft N Code Rajasthan State Qualifier** (Cyber Space Club MUJ, Unstop 1730314), gateway to the **Craft N Code National Finals at IIIT Bhubaneswar (Oct 30 – Nov 1 2026)**. This repo (`~/craft-n-code`, PRIVATE, remote github.com/harshgounder/craft-n-code) is the war-room: 30+ research files, all live-verified.

**We are already registered and paid (₹299/team, live API confirmed).**

## THE IMMEDIATE MISSION (the deadline is the whole game)

| When (IST) | What |
|---|---|
| Aug 15 12:00 | Hardware gate: decide PS-05 (needs ESP32/Pico + sensors in hand by then) |
| **Aug 15 21:00** | Idea submission OPENS (Unstop) |
| **Aug 15 21:30** | ★ PROBLEM STATEMENTS DROP ★ — our pre-built decision tree fires within 10 min |
| Aug 16 06:00 | Idea submission CLOSES (submit before this) |
| Aug 16 10:00–17:30 | Pitch to judges at MUJ (3-min demo, 2:30 target) |

**The idea bank is already written**: `research/IDEA-BANK.md` — pre-built answers for all 5 tracks (PS-01 Campus Pulse, PS-02 Night Ops, PS-03 Signal, PS-04 Kavach, PS-05 Hygiene Sentinel), decision tree, risk table, action plan. The strategic core: ONE engine (ingest → summarize → rank → deadlines) with skins, + Kavach for open/safety lanes.

## WHAT'S DONE (verified, committed, pushed)

- Full competitive intel: editions 2022/2023/2024/2025/2026, organizers (CSC MUJ + Tech Society IIIT-B rosters), judges (6, with taste profile), winners (2025 AFTERPACKETS codebase reverse-engineered; 2024 Wizard_Oz + Fork), losers (PromptBuddy, EduSynth war diaries), 2025 state map (11 rounds, 1,592 reg / 285 players), 2026 field (402 reg Rajasthan, down from 706).
- 2025 problem statements: FULL verbatim (7 Phase-1 + 7 Phase-2) in `research/raw/`.
- 2026 tracks: 5 verbatim bodies + overnight timeline + submission flow + canteen menu, from the official event site source (public repo Rudra-25-12/CraftnCode-2026).
- Re-audit sweep (Aug 14): every claim re-checked, corrections in `research/RE-AUDIT-FINDINGS.md` (2025 = 11 rounds not 4-5; 2024 winners found; fee ₹299; timeline Nov 8 23:00; ₹131K pool verified).
- IDEA-BANK.md + fresh README + INDEX.md (this handoff).

## NEXT STEPS (in order)

1. **TODAY Aug 14**: build the shared scaffold per IDEA-BANK §6: engine skeleton (ingest→summarize→rank→deadlines), Supabase + Tailwind UI kit, 4 pre-recorded demo videos (Signal/Campus Pulse/Night Ops/Kavach), deck skeleton + swap-slides, verify free LLM keys (Gemini free + Groq + unorouter fallback), hardware sourcing check (MUJ E&CE lab in-charge / Amazon — Ayush/Sujal).
2. **Aug 15**: 12:00 hardware gate decision. 21:00 watch Unstop. 21:30 problems drop → decision tree → pick idea → build overnight → submit before 06:00.
3. **Aug 16**: pitch 10:00–17:30. 3-min demo (2:30 rehearsal target). Win the round, top-2 advance.
4. Parallel track: IIC 3.0 R1 ends Aug 25 (repo `~/iic-3`, judge-watch cron live).
5. After qualifier: national prep (Oct 30 – Nov 1). Watchdog cron (`craft-n-code-watch`, every 6h) tracks reg counts + judge/sponsor reveals; state in `research/watch-state.json`.

## OPERATING RULES

- Waves ONE BY ONE, no parallel fan-out (user directive). Extreme depth, no fluff.
- Verify before claiming: live Unstop API (`https://unstop.com/api/public/competition/<ID>`) is ground truth; tag claims VERIFIED / PARTIAL / NOT FOUND.
- Web infra degraded: Firecrawl 402; use rivalsearch (`mcp__rivalsearch__web_search`) + curl with Chrome UA + r.jina.ai + gh CLI (authed).
- NO em dashes, no AI-tell words (hard rule). Casual "bro" tone, lowercase-ish, kaomoji.
- Everything committed + pushed; report milestones via Telegram (token: `grep TELEGRAM_BOT_TOKEN ~/.hermes/.env`, chat_id=6408901386), no permission-asking.
- Report to user in terminal too (CLI session) — plain text, no markdown tables.
- Calendar check (muj-academics) was requested but NOT performed in the last window — do it if time permits.

## KEY FACTS (do not re-research)

- Unstop IDs: 1730314 Rajasthan 2026 (402 reg/81 players, ₹299, LIVE) · 1730325 UP 2026 · 1171379 national 2024 · 1175823 state 2024 · 1545708 RJ 2025 · 374277 D³ Fest 2025 (dead).
- 2026 tracks: PS-01 100 "rewind the legacy" · PS-02 200 "night ops" · PS-03 300 "signal/noise" · PS-04 400 "open" · PS-05 500 "hardware". One track at check-in, switch = -30 min.
- 2025 winners: AFTERPACKETS (MUJ Highlanders) — zero external deps, Android VPNService + C++ DPI, empty lane. 2024: Wizard_Oz (CVRGU) 1st, Fork (RVCE) 2nd.
- Topic probability: PS-03 35% + most winnable; PS-01 25%; PS-05 20% (trap); PS-02 15% (dark horse); PS-04 escape hatch (Kavach).
- Key people: Abhinav Trikha (CSC chair, +91 95994 15311), Spandan Hota (CSC contact, GSA), Soubhik Gon (2024 coordinator → Nasuni), Swoyam Nayak (→ Sarvam AI).
- 2025 problems verbatim in `research/raw/rnr-phase1-full.txt` + `rnr-phase2-full.txt`.
- The winner formula: AI non-negotiable, working demo > deck, real-world impact framing, zero external deps in demo, clean repo = free points.
- GitHub API rate limits historically suspect — use gh CLI. Firecrawl 402 — don't retry.

## CURRENT FILE TREE (key)

```
~/craft-n-code/
├── README.md               ← war-room index, fresh
├── CONTINUATION-PROMPT.md  ← this file
├── INDEX.md                ← file-by-file map
└── research/               ← 30+ files (see INDEX.md)
    ├── IDEA-BANK.md        ← ★ THE playbook for Aug 15 21:30
    ├── 2026-TOPIC-PROBABILITY.md
    ├── RE-AUDIT-FINDINGS.md
    └── raw/                ← 2025 verbatim problems
```

Related repos: `~/iic-3` (IIC 3.0, R1 ends Aug 25), `~/muj-academics` (planner + drive sync crons alive), `~/parallel-key-tracker` (123 keys), `~/.hermes/scripts/craft-n-code-watch.py` (watchdog).

---

**Resume command**: read this file, then `research/IDEA-BANK.md`, then continue the action plan. Do not re-harvest what's already verified.
