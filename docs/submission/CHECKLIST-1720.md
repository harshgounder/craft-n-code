# CHECKLIST-1720.md (the 17:20 gate)

Hard polish stop at 17:20. Run this list top to bottom. Any red box means
stop and fix before 17:20; after that, only what is on this list ships.

## Deck

- [ ] KrishiSetu-Round0-20260816.pptx built from a clean node run
      (cd scaffold/deck && node build-krishi-setu.js)
- [ ] 11 slides, black/white/bold/3D style (window-d restyle)
- [ ] Zero em dashes, zero banned words (sweep script in scaffold/deck/check)
- [ ] PMFBY number decided: ledger line (88.5 lakh / Rs 2,580 cr) in, or the
      78.4 crore source added to the ledger first. FRESH-EYES-AUDIT flag 1.
- [ ] Research machine slide: 49 reports, wave count agreed (7 with d21-d24)
- [ ] Deck exported to PDF, opened once, no text overflow on any slide

## Prototype zip

- [ ] prototype.zip built from the recipe (docs/submission/PROTOTYPE-ZIP-RECIPE.md)
- [ ] Gates inside the recipe all green: 85/85, 46/46, backend 16/16, 5/5
- [ ] Boot check done: /health ok, krishi.html 200, then servers killed
- [ ] README-for-judges.md at zip root
- [ ] Zip size sane (under 30 MB)

## Proof and links

- [ ] PROOF-LEDGER-2026.md present, P1-P6 rows verified
- [ ] FRESH-EYES-AUDIT.md (window-d) attached in research-inputs/
- [ ] Both repos pushed: craft-n-code (window-d merged) and krishisetu
      (window-c merged), commit hashes recorded here:
      craft-n-code: ________   krishisetu: ________
- [ ] Deck commit hash recorded: ________

## The 18:00 upload

- [ ] Deck PDF + PPTX uploaded
- [ ] prototype.zip uploaded
- [ ] README-for-judges.md text pasted into the description field
- [ ] Submission form: team name 511, event Craft N Code 2026, PS-07
- [ ] Honesty labels visible on every demo screen (SIMULATED, SIMULATOR,
      SIMULATED STREAM, ROADMAP, four badges)

## Timebox

- 16:45 merge (window-d pushes first, conductor merges)
- 17:20 hard polish stop: no new content after this, only this list
- 17:50 buffer exhausted, upload starts
- 18:00 deadline
