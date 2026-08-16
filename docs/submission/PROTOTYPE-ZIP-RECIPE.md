# PROTOTYPE-ZIP-RECIPE.md (Round 0 submission kit)

Builds prototype.zip for the Round 0 upload. Two source trees, one zip.
The merge conductor runs this after the 16:45 merge; verify the gates inside.

## Inputs (must exist before packing)

| Piece | Where it lives | Branch |
|---|---|---|
| Advisory core + UI + deck + tests | ~/craft-n-code (scaffold/) | window-b merged |
| Data layer + API | ~/krishisetu/backend/ | window-c merged |

## Recipe

    # 1. stage a clean pack dir
    rm -rf /tmp/krishi-submit && mkdir -p /tmp/krishi-submit
    cd ~/craft-n-code && git archive --format=tar HEAD | tar -x -C /tmp/krishi-submit
    cp -r ~/krishisetu/backend /tmp/krishi-submit/krishisetu-backend
    rm -rf /tmp/krishi-submit/.git /tmp/krishi-submit/.venv
    find /tmp/krishi-submit -name '__pycache__' -type d -exec rm -rf {} +

    # 2. gate: every suite + eval, fresh, BEFORE the demo server starts
    cd /tmp/krishi-submit/scaffold
    for t in tests/test_*.py; do python3 "$t" || exit 1; done   # expect 85/85
    python3 eval/eval.py --all || exit 1                        # expect 46/46
    cd /tmp/krishi-submit/krishisetu-backend
    python3 tests.py || exit 1                                  # expect 16/16
    python3 integration_test.py --live || exit 1                # expect 5/5

    # 3. boot check, both servers, then kill
    cd /tmp/krishi-submit/krishisetu-backend && python3 serve.py --seed --port 8100 &
    cd /tmp/krishi-submit/scaffold && ./demo.sh &
    curl -s localhost:8100/health          # expect ok
    curl -s localhost:8137/krishi.html     # expect 200
    kill %1 %2

    # 4. zip
    cd /tmp/krishi-submit && zip -r prototype.zip . -x '*.pptx'

## Files included

- scaffold/agri/ (compiler, cvar, replay, state_machine, claims, doability,
  research_index, seed, rules.json)
- scaffold/webapp/ (serve.py, static/krishi.html, sw.js, manifest, icons,
  demo-feed.json)
- scaffold/tests/ (9 suite files, 85 checks)
- scaffold/eval/ (eval.py + eval-report.json)
- scaffold/engine/ (governed pipeline the advisory core mounts on)
- scaffold/demo-script.md, scaffold/demo.sh, scaffold/run-*.sh
- scaffold/deck/ (build-krishi-setu.js + KrishiSetu-Round0-20260816.pptx)
- krishisetu-backend/ (serve.py, db.py, schema.sql, seed.py, adapters.py,
  cap_ingest.py, tests.py, integration_test.py, seed/)
- docs/ (proof ledger, runbook, this kit)
- research-inputs/ (audits only, NOT the 98 raw files, they live in the
  krishisetu repo to keep the zip small)

## Excluded

- .git, .venv, node_modules, __pycache__, *.db, *.log, backups/, dist/,
  .env (secrets never ship), *.pptx inside the zip (deck uploads separately)

## Expected output

- prototype.zip, under ~30 MB
- README-for-judges.md at the zip root (copy from docs/submission/)
- Fresh eval-report.json inside scaffold/eval/ (regenerate, do not reuse)
