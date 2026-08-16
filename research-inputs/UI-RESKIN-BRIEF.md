# UI-RESKIN-BRIEF.md (for window B, after the number audit)

The current krishi.html is functional but generic. Reskin it to match
the design language of the REAL systems in this domain. Do not invent
styles: adapt what the evidence base documents.

## THE DESIGN REFERENCES (from the research raws, read them)
- IMD cyclone warning color codes: the incident stepper and advisory
  cards must use the official palette (yellow = watch, orange = alert,
  red = warning, grey = monitor). This is domain truth, not decoration.
- Jeonnam EWS (Korea, d25): a crop x hazard matrix view with per-cell
  risk states. Add a compact matrix panel: rows = Asha crops (paddy,
  pulses), columns = flood/cyclone/surge/salinity, cells = risk chips.
- Ama Krushi / Ethiopia 8028 / mKisan (d8, d28): voice-first design
  means ONE decision per card, big type, a phone mockup panel showing
  the actual IVR prompt text + DTMF options, and the missed-call
  callback flow as a visual timeline.
- Krishi Dashboard / NIC agri portals (d8): dense but calm tables,
  district/block filter chips, source + freshness column on every row.
- Farmer.Chat (d29): chat-style advisory thread panel alongside the
  structured cards, each message showing the underlying rule id.
- OSDMA / WFP anticipatory action (d27, d20): trigger timeline visual
  (T-72h watch -> T-48h alert -> T-24h warning -> T-0 landfall) with
  the action each trigger unlocks.

## THE RESKIN RULES
1. IMD color codes everywhere risk is shown: stepper, advisory cards,
   ladder rungs, matrix cells. Legend stays.
2. Typography: big, high-contrast, Odia labels stay, but the page must
   read "this is a disaster early-warning system", not a generic SaaS
   dashboard. Dense tables + one loud status banner at top (the
   current incident + its color + its state).
3. The phone panel: a styled feature-phone mockup on the farmer view
   showing the IVR prompt + DTMF options for the current advisory.
4. The matrix panel: crop x hazard risk grid (from the seed data).
5. The trigger timeline: T-72 to T-0 strip above the stepper.
6. Cards: source + grade + badge + freshness row on every advisory,
   exactly like a government data portal row.
7. No invented metrics, no decorative charts without data behind them.
   Every visual element must map to a real field in the agri core or
   the API contract.

## VERIFY
- Render + OCR check like before (headless firefox)
- IMD colors present, phone panel present, matrix present, timeline
  present
- No em dashes, no banned words
- 85/85 suites still green
- commit + push window-b
