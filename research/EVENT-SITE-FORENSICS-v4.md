# Event-Site Forensics v4 — Admin Console + Auth + Food (live JS bundle analysis)

Compiled: 2026-08-13 | Method: live-site JS bundle extraction (craftncode-2026.vercel.app/assets/*.js)

## ADMIN CONSOLE (VERIFIED — /admin + admin-D05ih_ze.js)

- Route exists (200), renders "Admin Console — Craft N Code"
- Query: `submissions` table, select `id, team_name, track, repo_url, demo_url, pitch, created_at`, order created_at DESC
- Render: article cards — team_name (neon-cyan), created_at (toLocaleString), track.toUpperCase() (neon-magenta), pitch, Repository link (repo_url), Demo link (demo_url, conditional)
- Counter: "NN ENTRIES" (padStart 2)
- Empty state: "No submissions yet."
- NO delete/update buttons in the admin UI (read-only dashboard)
- Admin guard: login flow checks `user_roles` table for role=admin; non-admin sign-in → signOut + "THIS ACCOUNT IS NOT AN ADMIN"

## AUTH FLOW (VERIFIED — index-D7FOYZhw.js)

- Signup: `auth.signUp({email, password, options: {emailRedirectTo: window.location.origin, data: {team_name}}})` → "Check your email to confirm your team account."
- Login: `auth.signInWithPassword`; if mode=admin → check user_roles for admin role → "Admin access granted." / "Player one ready."
- Session hook: reads `profiles.team_name` + `user_roles.role=admin` per user
- Team name stored in auth metadata (data.team_name) at signup; profiles row created by DB trigger (handle_new_user)

## SUBMISSION (VERIFIED — submit-DSBoB-9_.js)

- `submissions.insert({...data, demo_url: demo_url || null})` — plain INSERT, no upsert
- "One submission per team. You can resubmit until the clock hits zero — latest entry wins."
- Track select: PS-01..PS-05, defaultValue PS-01
- DEADLINE 09:00
- Zod validation: team_name (1-100), track (1-50), repo_url (valid URL, 1-500), demo_url (optional URL ≤500), pitch (1-2000)

## NIGHT CANTEEN (VERIFIED — food-BN7_vjLM.js)

- Menu (hardcoded): Midnight Maggi ₹40, Cutting Chai ₹15, Cold Brew Shot ₹60, Paneer Roll ₹80, Grilled Sandwich ₹70, Pizza Slice ₹90
- Cart: local state only (useState), NO backend — "PLACE ORDER" just shows a toast "Order placed · a runner is on the way" and clears the cart
- No localStorage persistence, no API call — the food ordering is a UI mock

## INTEL IMPLICATIONS

1. The admin console is READ-ONLY — judges see team_name/track/repo/demo/pitch + timestamp. The PITCH is the first thing they read. Pitch quality = first impression.
2. Submissions are plain INSERTs — resubmitting creates a NEW row (no upsert). "Latest entry wins" means the judges see ALL rows; the newest is what they evaluate. Old rows are NOT deleted — a sloppy early submission stays visible. Submit clean the first time, then resubmit only with a strictly better pitch.
3. The food ordering is a UI mock — no real ordering backend. Don't rely on it; bring your own snacks.
4. Admin access requires a user_roles row — the club grants it manually. No public admin signup.
5. The auth metadata carries team_name — the team name is set at signup, not editable in-app.
