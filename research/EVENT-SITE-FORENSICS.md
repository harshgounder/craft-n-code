# Event-Site Forensics — Craft N Code 2026 (Rudra-25-12/CraftnCode-2026)

Compiled: 2026-08-13 | Method: GitHub forensics (gh CLI) on the PUBLIC event-site repo

## THE FIND: the official Craft N Code 2026 event portal source is PUBLIC on GitHub

- Repo: github.com/Rudra-25-12/CraftnCode-2026 (created 2026-08-05, TypeScript)
- Owner: RUDRA PRATAP SINGH (GitHub created 2026-03-08, 7 public repos) — CSC dev
- Built with: Lovable (vibe-coded), TanStack Router, Tailwind, Supabase backend, bun
- Theme: 8-bit arcade (Pac-Man glyphs, arcade cabinet art, neon cyan/magenta, "arcade-card" components)

## THE 5 TRACKS (VERIFIED — src/routes/problem-statements.tsx)

| ID | Title | Body | Points |
|---|---|---|---|
| PS-01 | Rewind the Legacy | Take an outdated tool your campus still depends on and rebuild it for 2026. | 100 |
| PS-02 | Night Ops | Tooling for people who work odd hours — sleep, safety, focus, logistics. | 200 |
| PS-03 | Signal / Noise | Cut through information overload with search, summarisation or ranking. | 300 |
| PS-04 | Open Track | Anything you can justify in a 3-minute demo. Surprise the judges. | 400 |
| PS-05 | Hardware Hack | Sensors, microcontrollers, ugly wiring. Physical output required. | 500 |

- "CHOOSE ONE TRACK AT CHECK-IN. SWITCHING AFTER THE CLOCK STARTS COSTS 30 MINUTES."
- Points are per-track (100-500) — likely scoring weights, not prizes.

## SPONSORS (VERIFIED — src/routes/sponsors.tsx) — NOT FINALIZED

- TITLE PARTNER: "Your Brand Here" (empty slot)
- POWERED BY: "Slot Open" x2
- COMMUNITY: "Slot Open" x3
- Contact: sponsors@craftncode.dev — "Want your logo glowing over a hall of 200 builders at 3 AM?"
- "hall of 200 builders" = expected participant count (~200)

## BACKEND (VERIFIED — supabase/migrations/*.sql)

- submissions table: team_name, track, repo_url, demo_url, pitch (1-2000 chars), created_at
- profiles table: user_id, team_name
- user_roles: admin / team (RLS-locked, admin-only update/delete on submissions)
- Anyone can submit (anon INSERT allowed with length checks)

## BUILD HISTORY (VERIFIED — .lovable/plan/*.md)

- 2026-08-09: "rename-event-to-craft-n-code" — the event was RENAMED from "Rewind and Recode" to "Craft N Code" on Aug 9
- 2026-08-10: pac-man draws the title, hero animation pacing, login overlay (arcade style)
- 2026-08-10: "shorten-header-wordmark-to-cn1"
- Food ordering menu planned for the overnight hackathon (src/routes/food.tsx)

## IMPLICATIONS FOR TEAM 511

1. The 5 tracks ARE the problem structure — sponsor companies will likely map their questions onto these tracks (or the tracks ARE the sponsor questions).
2. PS-04 Open Track = safest bet (3-min demo, anything justified). PS-05 Hardware = highest points but needs physical hardware.
3. The event site is the submission portal (Supabase) — repo_url + demo_url + pitch are the submission fields. PREPARE THESE.
4. Sponsors not finalized = the "companies behind the hackathon" (Google/Apple/FB/Accenture/Adobe per CSC post) are still being locked. Watch sponsors@craftncode.dev + the site.
5. ~200 builders expected at the overnight event.
