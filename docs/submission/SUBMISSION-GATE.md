# SUBMISSION-GATE.md (window-d lane, 2026-08-16 ~16:15 IST)

The two Round 0 artifacts, their verification, and the exact upload steps.

## Artifact 1: the deck (PPTX)

| Field | Value |
|---|---|
| File | scaffold/deck/KrishiSetu-Round0-20260816.pptx |
| Size | 53,358 bytes |
| SHA-256 | 4a265ff96a55c08b8c30c620695d3b36fecb2dbf04ec99069f63167a9a67fbf5 |
| Build | node build-krishi-setu.js (offline, zero deps) |

Strict-viewer verification (all green, 16:10 IST):
- unzip -t: "No errors detected in compressed data"
- [Content_Types].xml is the FIRST zip entry (rezipped for compat), 79 entries total
- python-pptx 1.0.2 opens it: 11 slides, slide 1 first text run "KrishiSetu"
- Deck gate (check-deck.sh): 11 slides, 192 text runs, 0 em dash, 0 banned words, style tokens present
- Content: 49 reports / 7 waves / 3.2M chars / 4,800 sources, 88.5 lakh PMFBY, rule R17 citation, zero "rule 14", zero "78.4"

## Artifact 2: the prototype (ZIP)

| Field | Value |
|---|---|
| File | scaffold/dist/prototype.zip |
| Size | 4,152,823 bytes (4.0 MB) |
| SHA-256 | f3fc0739ec7e18b6f032c1cc08f65e002440d25c9e29116d969e2834033059a1 |
| Build | docs/submission/PROTOTYPE-ZIP-RECIPE.md (executed 16:12 IST) |

Contents: scaffold/ (agri, webapp, engine, tests, eval, deck source, demo.sh,
demo-script.md), krishisetu-backend/ (serve.py, db.py, schema.sql, seed.py,
adapters.py, cap_ingest.py, tests.py, integration_test.py, seed/), research/
(krishisetu research home: EVIDENCE-INDEX.md + raw/ + audits), README-for-judges.md
at the zip root, docs/ (proof ledger, runbook, submission kit). Excluded: .git,
.venv, node_modules, __pycache__, *.db, *.log, *.pptx, *.zip, .env, research-inputs
raw corpus (lives in research/raw).

Gates run inside the pack dir (all green, 16:12 IST):
- 9/9 acceptance suites (85 checks), eval 46/46 (fresh eval-report.json in the zip)
- backend tests.py OK (17 tests), integration_test 5/5
- Boot check: localhost:8100/health 200, localhost:8137/static/krishi.html 200,
  both servers killed after

## Repos (git ls-remote, 16:06 IST, both live)

| Repo | URL | Branch state |
|---|---|---|
| craft-n-code | https://github.com/harshgounder/craft-n-code | main = 9aa5b76 (STALE, pre-KrishiSetu), window-d = f1ee153 (latest, will move after this commit) |
| krishisetu | https://github.com/harshgounder/krishisetu | main = e5e1611 (STALE, missing numbers unification), window-c = f0e2d67 (latest) |

CRITICAL before you paste a repo link into the form: judges open the DEFAULT
branch, which is main for both repos, and both mains are stale. Either merge the
latest branches into main first, or paste the branch URL. Commands:
- craft-n-code: git checkout main && git merge window-d && git push
- krishisetu: git checkout main && git merge window-c && git push
Then re-run git ls-remote and paste the new main hashes into this file.

## Submission steps (18:00 form)

1. Deck PDF: export KrishiSetu-Round0-20260816.pptx to PDF (Google Slides or a
   LibreOffice machine; no soffice on this box), open it once, check every slide
   for overflow, then upload the PDF with the PPTX.
2. prototype.zip: upload scaffold/dist/prototype.zip as the prototype file.
3. Repo link: craft-n-code after the main merge (or the window-d branch URL).
   Second repo krishisetu optional, same rule.
4. Description field: paste docs/submission/README-for-judges.md.
5. Team 511, Craft N Code 2026, PS-07. Honesty labels visible on every demo
   screen (SIMULATED, SIMULATOR, SIMULATED STREAM, ROADMAP, four badges).
6. Re-verify before upload, three commands:
   - cd scaffold/deck && ./check-deck.sh            (deck gate)
   - sha256sum scaffold/deck/KrishiSetu-Round0-20260816.pptx scaffold/dist/prototype.zip
     (compare to the hashes above)
   - git ls-remote https://github.com/harshgounder/craft-n-code.git main
     (must show the merged main hash)

## Still open (decide before 17:20)

- Main-branch merge for both repos (see CRITICAL above)
- Deck PDF export (no soffice on this box)
- EVIDENCE-INDEX.md em dash + d21-d24 rows + THE-PLAN "harness" in the krishisetu
  research home (flagged in GATE-AUDIT.md, still unfixed)
