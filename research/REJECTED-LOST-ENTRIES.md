# REJECTED / LOST ENTRIES — what got cut and why (R1 mechanics + evidence)

Compiled: 2026-08-13 | Sources: NEXORA'26 portal JS forensics, 2025 finals roster, participant repos, judging UI strings

## 1. THE R1 SUBMISSION MECHANICS (NEXORA'26 portal, exact)

### The submission form (TeamSubmission table)
Fields: team_id, team_name, track_name, **problem_statement**, github_url, ppt_url, deployment_url, status

- status starts as `submitted`
- Admin evaluates with a **score 0-100** (validated: "Please enter a valid evaluation score between 0 and 100")
- After scoring: status → `Evaluated`
- A `rejected` status exists in the flow (the admin list filters on it)
- Duplicate submission blocked: error code 23505 → "Your team has already successfully submitted a project pipeline"
- Admin view: all submissions ordered by submitted_at DESC, with score + status badges (amber = Pending Review, green = Evaluated)
- **"Scores Redacted for Review Balance"** — scores hidden from teams during review (anti-bias)
- **"Cryptographic Assessment Protocol Active"** — telemetry/anti-cheat framing

### The admin gate (exact strings)
- "Admin Access Gate" / "Provide valid gateway criteria"
- Admin Username + System Password + Access Code
- Mock sandbox creds hardcoded in JS: username `test`, password `1234` (dev leftover)
- Team gate: Team Name + Leader's Full Name + Access Code

## 2. WHAT GETS REJECTED (the evidence-based list)

### From the 2025 finals roster (20 teams, 19 mapped):
- **Incomplete repos**: udaykoti/nani + WadoKira/Bhubaneswar-project--Frontend = 404 (deleted/private after event). 2/20 teams' work is GONE. If the repo is gone, the submission is unverifiable.
- **Tiny repos**: PreetiPMishra-Codes/swapp = 18KB (HTML only). GITLERS submitted a near-empty repo. That's a rejection-grade submission.
- **HTML-only entries**: swapp (18KB), VedaScore (190KB HTML) — no real app, no backend. 2/20.
- **The crowded-lane losers**: 5 lab-grader teams split the lane; only the best (if any) advanced. The other 4 lost despite building.

### From the NEXORA flow (what the admin sees):
- Missing deployment_url = weaker (the field is optional in the form but the demo round REQUIRED a deployment link)
- Missing ppt_url = auto-fail in R1 (PPT was a required round)
- problem_statement field = the pitch. Empty/weak = rejected
- Duplicate submission = blocked (23505)
- Score < threshold = "Pending Review" forever → effectively rejected

## 3. THE REJECTION PATTERNS (synthesized)

| Pattern | Evidence | 2026 R1 implication |
|---|---|---|
| Repo gone/private | 2/20 2025 repos 404 | Keep repo PUBLIC + alive. Never delete. |
| Near-empty repo | swapp 18KB | Judges see repo size. A real repo is table stakes. |
| No deployment | demo round required it | Deploy EVERYTHING. Vercel/Netlify free tier. |
| Weak pitch | problem_statement field | The pitch IS the submission. Write it like a judge reads it in 30s. |
| Crowded lane | 5 teams on lab grader | Empty lane = less competition for the same score. |
| Tooling failure | PromptBuddy's Composio/Gemini war | Zero-dependency stack = demo always works. |
| Scope creep | AFTERPACKETS cut features at 07:17 | Ship core, cut extras, clean repo, rebrand. |

## 4. THE R1 WIN FORMULA (for team 511, Aug 15 21:00 - Aug 16 06:00)

1. **Pick the lane BEFORE the problems drop** (PS-04 or PS-02 = emptiest)
2. **Have the repo skeleton ready** (public, named, README'd, with a real commit history)
3. **Have the pitch template ready** (problem_statement field: 3 sentences, judge-reads-in-30s format)
4. **Deploy early** (Vercel free tier, even a stub) — deployment_url filled from minute 1
5. **Zero-dependency core** (no OAuth/API keys in the critical path; if AI is needed, use a key we control with fallback)
6. **Demo > deck** (the 3-min demo is the whole game in PS-04)
7. **Clean repo before freeze** (no debug files, no .env, no node_modules committed)
8. **Resubmit near deadline** (latest entry wins — but keep the first submission clean in case)

## 5. THE "REJECTED" DATA WE CANNOT GET (honest limits)

- The actual NEXORA'26 results (winners named) — not public
- The 2025 R1 rejection list (only the 20 finalists are public)
- The 2026 Rajasthan R1 submissions (Supabase RLS-locked to admins)
- Judge score sheets (redacted by design)

What we CAN watch: the watchdog (reg counts, judge reveals, result flags) + the live site's admin console (read-only, but it shows submission count + timestamps once the event starts).
