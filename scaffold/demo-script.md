# DEMO SCRIPT: KrishiSetu Round 0 walkthrough (3 minutes)

Date: 2026-08-16 (window B, T2). Total: 180 seconds. Screen: the
KrishiSetu app at /static/krishi.html (or index.html after the merge
swap). Simulated elements are labeled on screen; the script below says
the honest framing out loud before any demo value appears.

## OPENING FRAME (0:00-0:15)

Screen: farmer view, Asha profile, incident chip says CYCLONE_WARNING
24h lead, SIMULATED FEED label visible.

SAY (one breath): "KrishiSetu turns a cyclone warning into a farmer's
to-do list. One farm profile in, crop-stage-specific actions out, each
action carrying a deadline, a source, and what waiting costs. This is
a prototype: every feed and channel on screen is labeled SIMULATED,
and every number on screen wears one of four evidence badges."

CLICK: nothing, let the profile card breathe for 5 seconds.

## 1. ASHA PROFILE (0:15-0:45)

Screen: Asha farm card (0.9 ha, flowering Swarna paddy, low plot, weak
embankment, leased land, feature phone) and the 11-state stepper with
CYCLONE_WARNING pulsing.

SAY: "Asha holds 0.9 hectares on a low plot. Her paddy is flowering,
28 days from maturity. Her embankment is weak and the land is leased,
so she cannot do structural work without the owner. Her phone is a
feature phone: SMS and IVR only. The stepper shows where her incident
is: pre-cyclone watch at 72 hours, alert at 48, warning now at 24."

POINT: run the finger along the stepper left to right, stop at the
pulsing CYCLONE_WARNING.

SAY: "Every field on this card wears a badge. 0.95 hectares is the
Odisha average, a measured census figure. The rest is this farm's
scenario profile, labeled as such."

## 2. TWO-FARM CONTRAST (0:45-1:15)

CLICK: the contrast tab. Toggle Asha to high field and back.

SAY: "Same storm, different advice. Asha is told: do not harvest, the
grain is not formed, early harvest at flowering is total loss. Move
seed to high ground, shelter livestock, photograph the standing crop
for the claim. Her embankment action is blocked on tenancy, flagged on
the doability line."

SAY (toggle to high field): "The high field is mature paddy, ten days
from harvest, owned land, strong embankment, five adults. It gets:
harvest now. Early harvest costs about 5.76 percent on average, a
published meta-analysis figure, and a flooded mature crop can be a
total loss. Same compiler, same warning, different actions, because
the profile differs."

## 3. WARNING ARRIVES (1:15-1:35)

CLICK: back to farmer view. Point at the incident header (SIMULATED
FEED).

SAY: "The trigger is the IMD CAP bulletin, cached sample, labeled
SIMULATED FEED. Twenty-four hour lead, winds 175 to 185 km per hour,
surge 1.5 to 2 meters. No live claims: this is a replay-grade sample
built from Fani-scale parameters. Each advisory shows its source rule
or report id, and the cost of waiting: what the farmer loses by doing
nothing."

## 4. DELIVERY LADDER ESCALATION (1:35-1:55)

CLICK: the ladder panel.

SAY: "Six rungs: app, SMS, IVR, USSD, radio, village volunteer. Each
has a latency budget and a fallback. SMS went out at 13:58. Unread.
So the system escalates down the ladder: IVR callback at 14:05, Asha
acks with a keypad press at 14:12. The high-field farm did not ack, so
a volunteer is assigned and a radio bulletin is scheduled. The rule:
unacknowledged means the message walks down the ladder until someone
confirms. Every rung here is labeled SIMULATOR or ROADMAP."

## 5. OFFLINE TOGGLE (1:55-2:10)

CLICK: the offline toggle on the header.

SAY: "Flip offline. The advisories do not disappear: they render from
local state, and the queue banner says three actions queued, syncs
when bandwidth returns. The phone is not a dependency. A tower going
down is exactly when a farmer needs the list, so the app keeps the
last compiled advisories local."

CLICK: toggle back online.

## 6. REPLAY PANEL (2:10-2:30)

Screen: the replay panel from the engine lane (agri/replay.py, Fani
calibration). If the panel is not in the UI at merge time, open the
engine output or say the one-liner below.

SAY: "The engine validates itself against real events. Fani: 108,220
hectares of crop affected, 1,304.58 crore rupees of loss, both from
the official damage and loss assessment, badge ODISHA-MEASURED. The
replay runs the advisory engine backward over Fani and Yaas and shows
the uncertainty band. We do not claim the prototype would have
prevented it; we show the numbers it was built on."

## 7. CLAIMS PACKET (2:30-2:45)

Screen: claim card from the operator console or the claim export from
agri/claims.py.

SAY: "The claim rail: photograph the standing crop now, time stamped,
file intimation within 72 hours, state relief eligibility starts at 33
percent loss. Both thresholds are scheme rules with sources. The
packet is a structured export: photo, voice note, geo tag, the 72-hour
clock, ready for the PMFBY intimation window. The farmer does not
navigate forms; the packet assembles itself from the advisory."

## 8. RESEARCH MACHINE + CLOSE (2:45-3:00)

CLICK: the research tab. Type "Fani" in the search box, show the
filtered rows.

SAY: "The credibility layer: 48 reports across 6 waves, searchable,
every row linking to its raw report. The evidence chain is enforced:
slide claim to proof ledger to index row to raw file. Any claim
without a chain does not ship."

SAY (close, 5 seconds): "One profile, one warning, staged actions,
degraded delivery, honest labels, replay-validated numbers. KrishiSetu."

## FALLBACK LINES (if a panel is missing at merge time)

- Replay panel missing: "The replay engine is in the build; on screen
  the anchors are the Fani numbers in the evidence chain, both
  ODISHA-MEASURED." Do not fake a chart.
- Claims panel missing: "The claim packet is an engine export; the UI
  shows the 72-hour clock and the photo instruction." Do not fake an
  export.
- Search box slow: it is instant, it is client-side. Do not wait.
- Judge asks if any of this is live: "Nothing is live. Every feed,
  channel, and stream on screen is labeled SIMULATED, SIMULATOR, or
  ROADMAP. The engine is real and tested; the data is sample or
  sourced with badges."

## PITFALLS

- Do not say "AI" for the advisory engine. Say compiler over rules,
  audited. The LLM renders; the engine decides.
- Do not claim sensors. The sensor stream is SIMULATED STREAM.
- Do not say Fani numbers are predictions. They are calibration
  anchors.
- Every number mentioned in speech must also be visible on screen.
- No em dashes in any spoken line. No AI-tell words.
