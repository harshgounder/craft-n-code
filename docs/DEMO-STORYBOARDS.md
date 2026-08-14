# DEMO STORYBOARDS — pre-recorded videos + live backup (scaffold §6.3)

Each skin has a 3-min storyboard. Record once today/tomorrow, screen + voiceover.
If the projector dies, network dies, or rate limits hit: the video saves us.
If the video dies: the offline mode saves us. Two layers, always.

Rule: every demo runs on PRE-IMPORTED real-ish data (the engine seed), never live accounts on stage.

---

## 1. SIGNAL (PS-03) — "one ranked feed for a student's day"

| Time | Screen | Voiceover |
|---|---|---|
| 0:00-0:20 | Title card: Signal | "A student's day lives in six channels. The one notice that matters is drowning in two hundred memes." |
| 0:20-0:50 | App opens on digest | "Signal pulls all six channels into one feed, dedupes, summarizes each notice with AI, and ranks what matters for YOU." |
| 0:50-1:20 | "Today in 60 seconds" + urgent cards | "Today: hostel fee due in six days, MTE schedule released, lab room shift. Sixty seconds and you know your whole day." |
| 1:20-1:50 | Ask box: "when is the MTE?" | "Ask anything. 'When is the MTE?' One sourced answer, with the deadline extracted." |
| 1:50-2:20 | Deadline card -> calendar invite | "The deadline is already a calendar invite with a two-day reminder. You cannot miss it." |
| 2:20-2:50 | Focus mode | "Focus mode collapses everything but what's urgent. Noise is gone." |
| 2:50-3:00 | Impact card | "Six channels, one feed, zero missed deadlines." |

## 2. CAMPUS PULSE (PS-01) — "the notice + complaint rebuild"

| Time | Screen | Voiceover |
|---|---|---|
| 0:00-0:20 | Title card | "Notices live in six places. Complaints go into a system nobody reads. We rebuilt both." |
| 0:20-0:50 | 6 source chips -> one feed | "Same engine: portal, mail, WhatsApp, Classroom, Instagram, Unstop. One ranked feed." |
| 0:50-1:30 | File a complaint with photo, auto-triage | "Water cooler broken on Hostel C, third floor. Photo in, AI triages it to plumbing, severity high, SLA 48 hours." |
| 1:30-2:10 | Ticket live status + fixed board | "Ticket C-114 goes live. Status updates like a delivery tracker. Every fix lands on the public fixed board." |
| 2:10-2:40 | Mess live board | "Mess board: queue load, today's menu, feedback NLP." |
| 2:40-3:00 | Impact card | "One feed, tracked complaints, a campus that can see itself getting fixed." |

## 3. NIGHT OPS (PS-02) — "campus after dark"

| Time | Screen | Voiceover |
|---|---|---|
| 0:00-0:20 | Title card | "Campus at 2 AM: dark stretches, sparse security, and nobody knows you're walking." |
| 0:20-0:55 | Night walk share, live map + ETA | "Start a night walk. Your trusted circle sees live location, auto ETA, and gets an arrival ping." |
| 0:55-1:30 | Lit-route heatmap | "The lit-route heatmap is crowd-sourced: safe, lit, crowded. We route you through the lit stretches." |
| 1:30-2:10 | SOS demo (2-sec hold) -> alert + evidence | "Two-second hold. Audio and video evidence captured, streamed to your circle and security with your location." |
| 2:10-2:40 | Night mess pre-order + focus mode | "Pre-order for a 2 AM pickup. And focus mode for when the campus is asleep." |
| 2:40-3:00 | Impact card | "Night on campus, without the fear." |

## 4. KAVACH (PS-04) — "the call-security platform"

| Time | Screen | Voiceover |
|---|---|---|
| 0:00-0:20 | Title card | "India's biggest quantified fraud is one phone call away. Four thousand crore lost to digital-arrest scams." |
| 0:20-0:55 | Live scam-call simulation | "Kavach screens the call in real time. Six detection engines, one intervention loop." |
| 0:55-1:30 | Family alert fires | "The family alert chain fires: trusted contacts get the call details and risk score instantly." |
| 1:30-2:10 | Evidence file export | "Every flagged call becomes an evidence file, ready for a police complaint." |
| 2:10-2:40 | The 24h build: night-safety integration | "Tonight we shipped the night-safety integration: Kavach's alert backbone now covers in-person emergencies too." |
| 2:40-3:00 | Impact card | "Real product, real demo, real families protected." |

---

## Recording checklist (per video)

- [ ] Screen recording at 1080p, voiceover in a quiet room
- [ ] Start with 1s black + title card (easy trim)
- [ ] Every screen shows REAL engine output, no fakery
- [ ] Keep under 2:50 (buffer for judge intro)
- [ ] Store: assets/demos/<skin>.mp4
- [ ] Playback test on the stage laptop BEFORE the pitch

## Live-demo fallback ladder (if going live instead of video)

1. Open http://localhost:8137 (offline mode needs nothing)
2. Pre-warm: run demo.sh 5 min before, feed cached
3. If UI breaks: fall back to the video. If video breaks: fall back to terminal digest output.
