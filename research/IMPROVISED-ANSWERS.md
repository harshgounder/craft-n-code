# IMPROVISED-ANSWERS.md: The 45 Gaps, Answered

Date: 2026-08-16. The stress audit listed 45 real gaps and parked them as
R1 backlog. Wrong move. This file designs through EVERY one. Each answer
is a concrete mechanism with the condition it needs to be true. No
deferral without a design.

## DATA-INTEGRITY (10 gaps: data vandalized + wrong crop/stage/plot/tenancy/deletion/soil/elevation/answers/transcript/photo)

D1. VANDALIZED / TAMPERED PROFILE -> the farm profile is an append-only
hash chain: every edit appends a signed event, hash-linked to the last.
Tamper = hash mismatch alarm on the operator console. Nothing rewrites
history, not even us. Condition: event store is R0 (simple SQLite with
hash column), full Merkle later.
D2. CROP ENTERED WRONG -> plausibility cross-check: crop x district x
sowing date against the regional calendar (d4). Impossible combo = the
system asks twice, differently, and labels the field "unverified until
confirmed". Plus a photo when the phone allows.
D3. STAGE STALE -> every stage has an expiry window (flowering = X days
for this variety). At advisory time the system asks "confirm stage,
press 1-4" via IVR. Stale stage = conservative default (the stage with
the WORST flood fragility), labeled.
D4. PLOT MOVED -> plot is GPS-anchored. Movement = new plot event, old
plot archived (never deleted). The advisory targets the CURRENT plot.
D5. TENANCY CHANGED -> tenancy flag expires at lease-season end
(calendar-driven). Renewal prompt at re-enrollment. Tenancy affects the
doability layer, never the crop science.
D6. PROFILE DELETED -> tombstone + purge with a 30-day undo window
(opt-out by IVR starts the clock, a call back within 30 days restores).
Deletion is a feature, not a hole.
D7. SOIL DATA MISSING -> regional default soil map (NBSS&LUP) as the
prior + farmer photo of soil + "TRANSFER-PRIOR until tested" badge.
The advisory says what changes when the real test lands.
D8. ELEVATION WRONG -> DEM lookup (30m) + farmer confirm + flood-depth
reports as live calibration. Elevation confidence feeds the CVaR
uncertainty, it never hides it.
D9. FARMER GAVE WRONG ANSWERS -> redundancy: ask the same thing twice,
differently (DTMF + voice repeat). Inconsistent = "unverified" badge +
human callback. We record what they said AND our confidence.
D10. VOICE TRANSCRIPT WRONG -> every parsed intent is echoed for DTMF
confirmation ("you said paddy flowering, press 1 yes, 2 no"). ASR is
never the sole path (WER 35.1% reality, d15). No confirmed intent, no
state change.
D11. PHOTO MISLABELED -> model confidence + a human verification queue
(volunteers/extension trainees). An unverified photo never triggers an
action; it triggers an observation request.

## SYSTEM-SECURITY (18 gaps: server down/db locked/queue overflow/trace lost/rule bug/LLM hallucination/clock skew/idempotency/PDF fail + account takeover/spoofed)

S1. SERVER DOWN -> the ladder (radio/village rungs) + offline-first
rendering: the last ingested bulletin + local rules render locally.
A down server degrades the TOP of the ladder, never the bottom.
S2. DB LOCKED -> SQLite WAL + a file-based fallback cache. Reads never
block writes; worst case is stale, never frozen.
S3. QUEUE OVERFLOW -> severity batching with a drop policy: MONITOR
level messages drop first under load, WARNING level never drops. The
drop is logged and reported in the postmortem.
S4. TRACE LOST -> append-only trace with hash chain + write-ahead
before any delivery. Farmer receipts (ack keypress) reconstruct the
trace even if server logs die.
S5. RULE ENGINE BUG -> rules are JSON DATA, not code. Versioned,
shadow-run in parallel before promotion, canary per district. A bad
rule rolls back in one config change, and the shadow comparison catches
it before farmers see it.
S6. LLM HALLUCINATION -> the LLM renders structured fields from the
audited engine through a template with a whitelist. No free text in
the critical path. If the template cannot be filled, the system sends
the deterministic fallback text, not an LLM guess.
S7. CLOCK SKEW -> advisory deadlines are RELATIVE ("by 6pm tonight"),
not absolute, with a 15% expiry tolerance. NTP where reachable, phone
time where not.
S8. IDEMPOTENCY BROKEN -> every advisory carries a delivery ID
(incident x farmer x rung). Dedupe by ID at every rung. Message design
assumes duplicates can happen: "you may receive this twice".
S9. PDF EXPORT FAILED -> the claims packet exports as structured text
+ image set + printable form. PDF is a cosmetic layer, never the only
format.
S10. OPERATOR ACCOUNT TAKEOVER -> API keys + per-operator audit + no
shared credentials + kill switch. An operator action is signed and
attributable. Farmer "accounts" are phone numbers with callback
verification, nothing to steal.
S11. MESSAGE SPOOFED -> every advisory is signed (per-farmer HMAC
fingerprint) and every message says "verify by calling this number".
CAP integrity: the system verifies IMD's public CAP feed hash, and a
fake bulletin that does not match the feed is rejected and flagged.

## INSTITUTIONAL (7 gaps)

I1. OSDMA REFUSES -> the prototype runs on IMD public CAP RSS + CWC
open data (d16: both public). A partner is growth, never a dependency.
The deck says "rails exist, pilot needs one partner".
I2. IMD API DENIED -> CAP RSS + archived IMD reports (d19) + Open-Meteo
fallback. The feed hierarchy is designed for refusal.
I3. NO AGRONOMIST REVIEW -> every rule carries its source + grade and
the "awaiting agronomist review" badge until it is signed. The KCC
escalation is the human layer meanwhile. An unreviewed rule is never
presented as reviewed.
I4. FPO WON'T PAY -> who-pays ladder: PMFBY 0.5% awareness earmark,
ATMA 60:40, panchayat development funds, CSR (delta districts have
CSR-active corporates), small farmer co-pay at 81.3% WTP (d18). The
claims-rail value (faster, verified claims) is the institutional pitch,
not the advisory fee.
I5. GOVT RELIEF CREATES DEPENDENCY -> the product positions as relief-
COMPLEMENTARY: the claims packet accelerates the relief the state
already owes. Faster verified claims is a government win, not a threat.
I6. ATMA NOT INTERESTED -> distribution alternatives: KVK, agri-clinics,
input dealers (the +50% adoption intermediary channel, d1), panchayat,
Ama Krushi-style toll-free. No single institution is load-bearing.
I7. SCHEME WINDOW CLOSED -> scheme-window awareness in the rule base:
the advisory can say "the intimation window for THIS event closes in X
hours" and "the next scheme cycle opens in Y weeks". Timing is part of
doability.

## JUDGING (4 gaps)

J1. "FANI WAS 6 YEARS AGO" -> Fani is the CALIBRATION ANCHOR, not the
story. Yaas 2021 (2-4m surge) and Dana 2024 (5,428 acres) are fresh.
The replay harness runs the same math on all three. Fresh data, live
math.
J2. "WHY ODISHA NOT NATIONWIDE" -> the statement scope is Odisha, and
that is the answer. Nationwide = the data cooperative + rule packs per
state (Round 3). One rail, one pilot, one quarter.
J3. "WHO PAYS" -> 81.3% WTP small co-pay (d18), PMFBY awareness
earmark, ATMA 60:40, FPO rails, Farmitra precedent, claims-rail value.
The answer is a ladder, not a hope.
J4. "PRIVACY" -> consent at enrollment, opt-out by IVR one press,
deletion with 30-day undo, shared-phone member separation, data-as-
asset framing: "your data, your advice, your claim". The signed event
store makes privacy provable, not promised.

## SCALE (6 gaps)

C1. 1M FARMERS -> profile capped at 10KB, Postgres partitioning by
district, batch pipelines. 1M profiles = 10GB. Nothing exotic.
C2. 10M MESSAGES/EVENT -> severity batching + per-farmer dedupe + rung
economics: only WARNING-level goes SMS-to-all (Rs 0.18 x N), lower
rungs batch to IVR/radio. Cost is a design input, not a surprise.
C3. IVR CONCURRENCY -> telephony provider concurrency is rented, not
built. Callback staggering by village + severity.
C4. THROUGHPUT -> async everywhere, delivery IDs, worker pools. The
ladder absorbs the burst by design.
C5. DLT REGISTRATION -> register as an enterprise entity with telco
headers + pre-approved template IDs per advisory type (the standard
path, documented in d7). Rejection contingency: USSD + IVR + radio
rungs carry the message (the ladder is DLT-independent).
C6. NUMBER CHURN 20%/YR -> re-verify at season start + household
profile re-linking (the household keeps the data, the number is a
pointer). Churn costs a re-link prompt, never the profile.

## WHAT THIS CHANGES IN THE PLAN
1. THE-PLAN.md PART 3: add "rules are JSON data, shadow-run, canary"
2. PART 5: add "append-only hash chain + 30-day undo deletion"
3. PART 6: add "claims packet = text + image + printable, PDF cosmetic"
4. The OPEN REGISTER shrinks from 8 to 2: comprehension tests with
   farmers, and the real Rs 1,500 node. Everything else now has a
   designed answer with a condition.
5. The two that remain are not design gaps: they are reality gaps that
   only field presence can close. The plan says so, honestly.
