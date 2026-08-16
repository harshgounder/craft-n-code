# GATE-AUDIT.md (merge-prep gate, window-d lane, 2026-08-16 ~16:00 IST)

Walk of CHECKLIST-1720.md against disk. Legend: GREEN = present and verified,
YELLOW = present but needs a decision or a re-run, RED = absent or failing.

## 1. Deck

| Check | Status | Path / evidence |
|---|---|---|
| pptx from clean node run | GREEN | scaffold/deck/KrishiSetu-Round0-20260816.pptx, rebuilt via check-deck.sh at 15:59 (DECK WRITTEN, 286,203 bytes) |
| 11 slides, black/white/bold/3D | GREEN | gate: "DECK GATE PASS: 11 slides, 192 text runs"; style tokens in artifact: 0A0A0A x109, FFFFFF x77, FF5A1F x13 (hazard only), Arial Black x189 runs, 20 rotations, 12 shadows, 14 parallelograms |
| Zero em dash, zero banned words | GREEN | scaffold/deck/check-deck.sh both gates pass (0/0, 0/0) |
| PMFBY number decided | GREEN | deck text: "88.5 lakh PMFBY enrollments, Rs 2,580 crore claims paid (2020-25)"; "78.4" and "1.83" absent from text runs; ledger P3 VERIFIED |
| Research machine 49/7/3.2M/4,800 | GREEN | generator line 99: "49 parallel deep-research reports across 7 waves"; notes: "49 reports, 7 waves, 3.2M chars, 4,800+ sources". Artifact text runs: 49 yes, 48 no, 3.2M yes, 4,800 yes. Numbers re-measured by window D: wave 1 = 2,225,731 chars + 3,471 mentions (research-inputs), v2 wave = 992,045 chars + 1,329 mentions (hackathon-sota-lab/research/raw/v2, 18 files), combined 3,217,776 chars and 4,800 mentions exactly. Ledger row P7 ADDED by window D this gate |
| R17 citation | GREEN | "rule R17" in source and artifact, zero "rule 14" anywhere |
| Team slide truth | GREEN | 5473776: Harsh = everything (architecture, code, research, backend, QA, devops), Ayush = deck and design, Sujal = deck design |
| Deck exported to PDF | RED | no PDF on disk; no LibreOffice on this box. Export before 17:20 via Google Slides or a machine with soffice |
| No text overflow | YELLOW | cannot render locally (no soffice); do the visual pass during the PDF export |

## 2. Prototype zip

| Check | Status | Path / evidence |
|---|---|---|
| prototype.zip per recipe | RED | recipe ready at docs/submission/PROTOTYPE-ZIP-RECIPE.md; dist/craft-n-code-submission.zip exists but is STALE (pre-drop scaffold: deck-gen.js, old index.html, deck-*.pptx). Rebuild per recipe at the gate |
| Gates green inside | YELLOW | 85/85 GREEN (window D fresh run 15:30: 13+8+12+4+4+9+23+12); 46/46 GREEN (scaffold/eval/eval-report.json + dist copy, generated 2026-08-16T07:40:32, matches deck footer); agri 21/21 GREEN (15:59, R18 tillering trigger fixed); backend 16/16 + 5/5 NOT re-run here (window C evidence: 8af5297, integration 5/5 both modes) |
| Boot check /health + krishi.html 200 | RED | not exercised in this window; do at the gate per ROUND0-RUNBOOK (backend 8100 --seed, demo.sh 8137) |
| README-for-judges at zip root | GREEN (source) | docs/submission/README-for-judges.md; must be copied into the zip at build |
| Zip under 30 MB | N/A | not built yet |

## 3. Proof and links

| Check | Status | Path / evidence |
|---|---|---|
| PROOF-LEDGER P1-P6 | GREEN | docs/packaging/PROOF-LEDGER-2026.md; P1 Dana 5,428 acres, P2 Yaas 5,882 ha, P3 PMFBY 88.5 lakh / Rs 2,580 cr, P4 DAM 2,817 cr, P5 85/85 + 46/46, P6 honesty; all trace to raws (window D verified). P7 added this gate |
| FRESH-EYES-AUDIT attached | GREEN | research-inputs/FRESH-EYES-AUDIT.md, FLAG-1 through FLAG-12, committed at 4082204 |
| craft-n-code pushed | GREEN after this push | origin/window-d was at 4082204; local HEAD f0140e1 (conductor commits 5473776 R17/R18 + 21/21 tests, f0140e1 numbers + team slide) pushed with this audit |
| krishisetu pushed (window-c merged to main) | RED | origin/main = e5e1611; numbers unification f0e2d67 and window-c 8af5297 exist only on origin/window-c. Main merge pending (runbook said 16:00, not done) |
| EVIDENCE-INDEX em dash + d21-d24 rows | RED | ~/krishisetu/research/EVIDENCE-INDEX.md line 1 still has the em dash in the title; d21-d24 rows still missing (grep count 0) while the title claims "nothing omitted, nothing hidden". research-inputs copy was fixed by window D |
| THE-PLAN banned word | RED | ~/krishisetu/research/THE-PLAN.md line 68: "the replay harness with uncertainty bands". research-inputs copy fixed by window D |
| Numbers in the three docs | PARTIAL | SUBMISSION-TEXT: "a 49-report evidence base across 7 waves" yes, no 3.2M/4,800. JUDGE-QBANK Q10: "49 research reports across 7 waves" yes, no 3.2M/4,800 (the "3.2M farmers" at line 31 is Ama Krushi, unrelated). demo-script: "49 reports across 7 waves" yes, no 3.2M/4,800. The deck carries the full set. Decision needed: add "3.2M chars, 4,800 sources" to the demo SAY line (judges hear the demo) or keep deck-only |
| Deck commit hash | GREEN | f0140e1 (numbers + team slide), 85178f7 (R17 citation), 9f3c6bd (restyle) |

## 4. The 18:00 upload

All items pending, this is the submission step itself. Deck PDF first.

## Open decisions for the conductor (priority order)

1. PDF export: no soffice on this box, needs Google Slides or a LibreOffice machine
2. krishisetu main merge + push (f0e2d67 numbers unification + 8af5297 window-c work are on origin/window-c only)
3. Research-home fixes (EVIDENCE-INDEX title em dash, d21-d24 rows, THE-PLAN harness) or an explicit waive before 17:20
4. Demo SAY line: add 3.2M chars / 4,800 sources or keep deck-only
5. Zip rebuild per recipe + boot check at the gate

## Warn: do not merge

origin/deck/krishi-v2-redesign (26f6502) is a stale pre-drop experiment based on
old main 9aa5b76; it deletes 57,944 lines including krishi.html, state_machine.py,
demo-script.md and test_agri.py. Different design concept ("editorial field
journal"). Never merge it.
