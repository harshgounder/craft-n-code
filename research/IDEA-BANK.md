# IDEA BANK — pre-built for all 5 tracks (drop-ready)

Compiled: 2026-08-14 | Purpose: the Rajasthan qualifier problems drop **21:30 IST Aug 15** (idea submission opens 21:00, closes Aug 16 06:00, pitch to judges Aug 16 10:00-17:30 at MUJ). We will NOT have time to brainstorm that night. Every idea below is pre-built: problem angle, MVP scope for 24h, stack that matches OUR skills, demo script, judge mapping, risk. We pick within 10 minutes of the drop.

---

## 0. THE PRE-DECISION TREE (read this first)

```
Problem drops at 21:30
│
├─ Matches PS-03 Signal/Noise ──────► IDEA 3A "Signal" (the engine, campus skin)
├─ Matches PS-01 Legacy rebuild ────► IDEA 1A "Campus Pulse" (same engine, ops skin)
├─ Matches PS-02 Night Ops ─────────► IDEA 2A "Night Ops" (safety + logistics)
├─ Matches PS-05 Hardware ──────────► IDEA 5A "Hygiene Sentinel" (ONLY if hardware sourced by 12:00 Aug 15)
├─ Open track / no match ───────────► IDEA 4A "Kavach" (existing product, 3-min demo)
│
└─ If MULTIPLE fit: priority = PS-03 > PS-01 > PS-02 > PS-04 > PS-05
```

The strategic core: **one engine, many skins**. A summarize/rank/extract-deadlines engine covers PS-01, PS-02, PS-03 with a different skin. Kavach covers PS-04 and the safety module of PS-02. So 80% of our prep is build-once.

Hardware gate: if no ESP32/RPi + sensors in hand by **Aug 15 12:00**, PS-05 is dead. Do not gamble the qualifier on it.

---

## 1. PS-01 Rewind the Legacy (100 pts) — "Take an outdated tool your campus still depends on and rebuild it for 2026."

Lineage: 2022 hostel/mess problems → 2024 food-safety round → 2025 Inbox Navigator. The family has appeared in EVERY edition. MUJ's actual outdated tools: notice/announcement chaos (WhatsApp + mail + portal), complaint system, mess, library, placement portal.

### IDEA 1A — "Campus Pulse" (PRIMARY)
Rebuild the campus notice + complaint system as ONE AI-native app.

- **Problem angle**: notices live in 6 places (portal, mail, WhatsApp groups, Instagram, Classroom, notice boards). Complaints go into a system nobody reads. Both are 2010-era workflows on 2026 campuses.
- **What we build (24h MVP)**:
  - One feed: pull from portal/mail/Classroom (IMAP + Google API), dedupe, AI-summarize each notice, rank by relevance to the user (department, year, hostel), extract deadlines → calendar invites.
  - Complaint tracker: photo evidence, AI triage (category + severity + auto-routing), status pubsub (like a delivery tracker), SLA timer, escalation after 48h, public "fixed board".
  - Mess/canteen live board: queue load, today's menu, feedback NLP.
- **Stack**: Next.js + Tailwind (Sujal), FastAPI + Supabase (Ayush), Google API + IMAP ingestion (Harsh), LLM via free tier (Gemini free / Groq / our routers — NO paid keys).
- **Demo script (3 min)**: show 6 sources → one feed → "today in 60 seconds" digest → tap a complaint → photo → auto-triage → "your ticket #C-114 is being fixed" live status. Record real MUJ notices for the demo (pre-imported, no live accounts on stage).
- **Judge mapping**: Google DNA (search/summarize), Accenture DNA (enterprise ops), practicality (the #1 rulebook criterion), direct 2025 predecessor lineage.
- **Risk**: crowded lane (it's the obvious one). Mitigate with the complaint tracker as the differentiator — 2024's winner had a complaint-ish core and won the state round.
- **Reuse**: the engine from IDEA 3A (same code, different skin).

### IDEA 1B — "Mess IQ" (ALTERNATE)
Rebuild the mess/canteen system with AI. 2024 food-safety DNA, direct.

- Menu prediction (what will be served, from past menus + festival calendar), waste prediction (from past consumption + holidays), allergy + food-safety alerts (2024's exact theme), live queue + pre-order, feedback NLP → weekly report to mess committee.
- Demo: real menu data (MUJ mess menus exist on student groups), show waste curve + "today's predicted rush" + allergy alert demo.
- Risk: mess committees are a hard sell to judges vs student impact framing. Frame it as "student health + food safety".

### IDEA 1C — Placement portal rebuild (BACKUP)
AI resume scorer against JD, job matching, deadline tracker, company prep packs. High impact, high crowd, and MUJ's placement portal is a known pain point. Only if 1A/1B feel wrong on the night.

---

## 2. PS-02 Night Ops (200 pts) — "Tooling for people who work odd hours: sleep, safety, focus, logistics."

NEW track, no direct precedent = the empty lane. 2025's winner took a 1-team lane. This is our dark-horse shot.

### IDEA 2A — "Night Ops" (PRIMARY)
Campus night safety + night-life logistics companion.

- **Problem angle**: MUJ campus + hostel life at night: walking to the mess/gate at 2 AM, night deliveries, security presence is sparse, students coordinate "who's awake" over WhatsApp. Women's safety angle is real and judge-grabbing (ACP Anjana Tudu's DNA = police/cyber safety).
- **What we build (24h MVP)**:
  - Trusted-circle live location: share "I'm walking back" with auto ETA + arrival ping.
  - Lit-route heatmap: crowd-sourced "this route felt safe/lit/crowded" ratings → safe-path suggestions. (Static demo data pre-seeded.)
  - SOS: 2-second hold → audio + video evidence clip captured → sent to circle + security with location. **Reuse Kavach's existing call-security pieces for this** — already built, already tested.
  - Night mess/delivery coordination: pre-order for 2 AM pickup, runners board (the event site itself has runners — we know the pattern).
  - Quiet-hours focus mode: "the campus is asleep" pomodoro + sleep schedule tracker (Apple Health DNA).
- **Stack**: Next.js + Tailwind, Supabase (realtime = perfect for location), WebRTC/WebSocket for SOS stream, existing Kavach backend for evidence.
- **Demo script (3 min)**: start "night walk" → map shows lit route → SOS demo (fake) → circle gets alert with live location + evidence clip → night mess pre-order screen → focus mode. Pre-record the walk portion; live-demo the SOS in the room.
- **Judge mapping**: security judges (Tudu/Sethi = cyber + police), Apple DNA (safety/health), Accenture DNA (workforce logistics), novelty (empty lane), real human problem.
- **Risk**: location permissions on stage. Mitigate: pre-record + a local mock mode.

### IDEA 2B — "Nightshift OS" (ALTERNATE)
Tooling for actual night-shift workers (delivery riders, security, hospital staff, call centers): shift handoff with recorded state, fatigue alerts (work-hour tracking), incident log with evidence export (PDF/JSON), lit-route planning. Accenture workforce DNA. Demo is harder (no real riders on stage) — use a mocked shift.

### IDEA 2C — "The All-Nighter" (BACKUP)
Self-referential: a hackathon-survival OS. Adaptive pomodoro for 2-5 AM productivity curves, caffeine schedule optimizer, noise-aware quiet hours, "survive the night" dashboard with team energy stats. The judges ARE the audience (they've run all-nighters). Fun, but thin on real-world impact — judges reward practicality. Use only as a tiebreaker.

---

## 3. PS-03 Signal / Noise (300 pts) — "Cut through information overload with search, summarisation or ranking."

The most probable AND most winnable (35% × high winnability). Direct 2025 predecessor: Challenge 5 Inbox Navigator. Google DNA. This is our home turf.

### IDEA 3A — "Signal" (PRIMARY)
One ranked AI feed for a student's entire day. The Inbox Navigator rework, upgraded.

- **Problem angle**: a student's day is 6 unread channels (Gmail, Classroom, WhatsApp groups, Unstop, portal notices, Instagram) and the ONE notice that matters (mid-sem dates, deadline changes, room shifts) drowns in 200 memes. Missed = failed.
- **What we build (24h MVP)**:
  - Ingestion: Gmail (IMAP), Classroom (Google API), Unstop (public API — we KNOW it), portal notices (scrape), WhatsApp (manual export/manual seed), Instagram (manual seed). Real accounts for demo data, pre-imported.
  - Engine: dedupe → LLM summarize (one line each) → rank by (user profile, sender authority, deadline proximity, recency) → "Today in 60 seconds" digest → deadline extraction → calendar invite with 2-day reminder.
  - "Focus mode": collapse all but the top-3 + urgent.
  - Search: semantic search over ALL channels ("when is the EM MTE?" → answer with source).
- **Stack**: Next.js + Tailwind (Sujal), FastAPI + Supabase (Ayush), ingestion + ranking pipeline (Harsh), LLM free tier (Gemini free tier / Groq Llama / our existing router infra from unorouter — we HAVE a working 189-model router, use it).
- **Demo script (3 min)**: open "today" → 60-second digest reads out → "when is the MTE?" semantic search → deadline card with calendar invite → focus mode. All pre-imported real data.
- **Judge mapping**: Google DNA (search/summarize/Workspace), 2025 predecessor (they KNOW the Inbox Navigator was a challenge), practicality, AI non-negotiable (satisfied), demo-ability (satisfied).
- **Risk**: crowded lane. Mitigation: semantic search over unified channels + deadline automation is more than the 2025 original did. We beat the template.
- **Reuse**: THE engine. Skins to PS-01 (campus ops) and PS-02 (night digest) are cosmetic.

### IDEA 3B — "PaperPilot" (ALTERNATE)
Research copilot for students: query → ranked paper list (arXiv API — free, no keys) with one-paragraph summaries, related-work generator, citation graph, "explain to a 2nd-year" mode, save-to-collection. Demo: "recommend 5 papers on RAG for my survey" → ranked list with summaries in 10 seconds. Strong for the E&CE/CS judges. Risk: academic framing vs practical framing; judges skew industry.

### IDEA 3C — "De-Fuser" (BACKUP)
News feed with bias detection, source ranking, both-sides view, echo-chamber breaker. Meta DNA. Hard to demo well in 24h (bias detection claims get poked). Last choice in this track.

---

## 4. PS-04 Open Track (400 pts) — anything you can justify in 3 minutes.

No question to guess. The escape hatch. Our READY-MADE answer exists.

### IDEA 4A — "Kavach" (PRIMARY)
Call-security platform (our existing product, IIC route). Real-time scam-call screening, family alerts, evidence logging.

- **Why this wins the state round**: it is a REAL product with a REAL demo. Judges = industry + cyber + police taste. Kavach IS the security-judge wet dream. No 24h build risk: it's built.
- **Demo script (3 min)**: live scam-call simulation → detection → family alert → evidence file. We have done this demo before (IIC).
- **Flex note**: at nationals, Kavach can ALSO be the PS-02 answer (night safety module) — it already has the evidence + alert backbone that IDEA 2A needs.
- **Risk**: (a) it's our IIC project — judges at CSC might have seen the IIC pitch; (b) "did you build this at the event?" — be honest: it's a product demo, the 24h value-add is the integration. Frame as "we're not starting from zero, we're shipping the version that matters".
- **Rule**: if we pitch Kavach, have the flex answer ready (what did you build in the 24h? → the night-safety integration + the live demo harness).

### IDEA 4B — "Market Noise Filter" (ALTERNATE)
From the crvusdt work: a live dashboard that separates signal from noise in market data (our quant pipeline, REAL data, REAL metrics). Deep tech, unique. Risk: finance framing lands flat with campus judges. Only if we read the room as technical.

### IDEA 4C — fresh on the night (BACKUP)
Do NOT bet the qualifier on a fresh idea. We have two real ones.

---

## 5. PS-05 Hardware Hack (500 pts) — sensors, microcontrollers, ugly wiring. Physical output REQUIRED.

The trap. Highest points, hardware we don't have. GATED.

### IDEA 5A — "Hygiene Sentinel" (PRIMARY, hardware gate)
Mess/canteen hygiene + air-quality monitor: ESP32 (or RPi Pico W) + MQ135 (air quality) + DHT11 (temp/humidity) + optional camera → dashboard with alert thresholds → compliance log (PDF export). 2024 food-safety DNA, 2022 PM2.5 DNA. Physical output: LED status + buzzer on threshold breach + dashboard.

- **Hardware sourcing checklist (by Aug 15 12:00)**:
  - ESP32 dev board (~₹400) or RPi Pico W (~₹500): Amazon 1-day delivery, or MUJ electronics/ECE lab (ask the E&CE lab in-charge TODAY — we're E&CE, the lab HAS these).
  - MQ135 + DHT11 sensors (~₹150 total), breadboard + jumpers (~₹100).
  - Total ~₹700-800. Ayush/Sujal can solder-free breadboard this.
  - If sourcing fails by the gate: **skip PS-05 entirely. Do not write a hardware pitch without hardware.**
- **Demo**: live sensor readings on the projector (USB or WiFi to dashboard), threshold breach → buzzer + alert, compliance log export.
- **Risk**: 24h + hardware debugging = the highest failure mode of the whole bank. The gate exists for a reason.

### IDEA 5B — Attendance/occupancy automaton (ALTERNATE)
RFID/NFC badge tap → room occupancy → auto-attendance + lab-slot tracker. Practical, boring, safe. Only if 5A hardware falls through but we still have a board.

---

## 6. THE SHARED SCAFFOLD (build ONCE before 21:30 — do not skip)

Whatever drops, these are pre-built:

1. **The engine skeleton** (IDEA 3A core): ingest → dedupe → LLM summarize → rank → deadlines. ~2h of work TODAY. All 3 skins (1A/2A/3A) mount on it.
2. **One Supabase project** + auth + a Tailwind UI kit (cards, feed, map, SOS button). Reused by every web idea.
3. **Pre-recorded demo videos** (3 min each) for: Signal, Campus Pulse, Night Ops, Kavach. Screen + voiceover. If the projector dies or the demo account rate-limits, the video saves us. ALSO: judges see polish.
4. **The deck skeleton**: title → problem (with the 6-source chaos visual) → solution → live demo → impact → roadmap → team. Per-idea swap slides (problem/solution/demo slides swap; impact/roadmap/team stay). 10 minutes to swap, not 3 hours.
5. **Free LLM keys verified TODAY**: Gemini free tier (ai.google.dev, free API key) + Groq (free tier) + our unorouter fallback chain. NO paid keys, NO quota surprises on the night. (AFTERPACKETS won partly because their demo had zero external dependencies. Same rule.)

## 7. WHAT WE SUBMIT TONIGHT IF THE PROBLEM IS OFF-MAP

The Rajasthan qualifier has its OWN problems (contact-verified) — they may not match the 5 national tracks. If the drop is off-map:
1. Map it to the closest track skin (the engine handles most things).
2. If it's a security/safety problem → Kavach + night-ops skin.
3. If it's a data/education problem → PaperPilot skin.
4. Never pitch a fresh idea we haven't thought through. The bank always wins.

---

## 8. RISK TABLE (honest)

| Risk | Likelihood | Mitigation |
|---|---|---|
| Problem doesn't match any track | Medium | Off-map protocol (sec 7) |
| Demo fails on stage (network/rate-limit/permissions) | Medium | Pre-recorded videos + local mock mode for every demo |
| Crowded lane (PS-03) | High | Differentiator = unified semantic search + deadline automation |
| Hardware not sourced | High | Gate at Aug 15 12:00, skip PS-05 |
| Judges ask "what did YOU build in the 24h" (Kavach) | Medium | Pre-scripted answer: the integration + demo harness IS the build |
| LLM quota dies at 3 AM | Medium | Verified free tiers + router fallback + offline rule-based fallback in the engine |
| Pitch overruns 3 min | High | Rehearse with a hard timer today, trim to 2:30 |

## 9. ACTION PLAN (TODAY, Aug 14)

1. [ ] Build the engine skeleton (ingest → summarize → rank → deadlines) — Harsh
2. [ ] Set up Supabase + UI kit — Ayush + Sujal
3. [ ] Pre-record 4 demo videos (Signal, Campus Pulse, Night Ops, Kavach)
4. [ ] Deck skeleton + 4 swap-slide sets
5. [ ] Verify free LLM keys (Gemini + Groq) + router fallback
6. [ ] Hardware sourcing check (lab in-charge / Amazon) — decide the PS-05 gate
7. [ ] Rehearse pitch with timer (2:30 target), record once
8. [ ] 21:00 Aug 15: watch for problem drop; 21:30: decision tree fires; submit by 06:00
9. [ ] Aug 16 10:00: pitch. 3-min demo. Kill it.
