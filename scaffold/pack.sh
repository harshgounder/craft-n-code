#!/usr/bin/env bash
# Craft N Code 2026 submission pack (BUILD-SPEC B6).
#
# One command assembles the submission kit in dist/:
#   1. gate: every suite + the offline eval must pass (no red submission)
#   2. secret scan: flag secret-like patterns in the submission tree
#   3. README-SUBMIT.md: repo url, commit, run commands, endpoint table
#   4. craft-n-code-submission.zip: the scaffold, runtime dirs excluded
#   5. printed checklist for the 06:00 upload
#
# Usage: ./pack.sh
set -euo pipefail
cd "$(dirname "$0")"

SCAFFOLD="$(pwd)"
DIST="$SCAFFOLD/dist"
ZIP="$DIST/craft-n-code-submission.zip"
mkdir -p "$DIST"

FAILED=0
SUITES=0
TOTAL_CHECKS=0
GATE_LOG="$(mktemp)"

# ── 1. gate: all acceptance suites + offline eval ────────────────
echo "== gate: acceptance suites =="
for t in tests/test_*.py; do
  SUITES=$((SUITES + 1))
  if python3 "$t" >"$GATE_LOG" 2>&1; then
    count="$(grep -Eo '[0-9]+/[0-9]+ passed' "$GATE_LOG" | tail -1 || true)"
    TOTAL_CHECKS=$((TOTAL_CHECKS + ${count%/*}))
    echo "  [PASS] $t  ($count)"
  else
    cat "$GATE_LOG" >&2
    echo "  [FAIL] $t" >&2
    FAILED=$((FAILED + 1))
  fi
done

echo "== gate: offline eval =="
if python3 eval/eval.py --all --report "$DIST/eval-report.json" >"$GATE_LOG" 2>&1; then
  echo "  [PASS] eval/eval.py --all"
else
  cat "$GATE_LOG" >&2
  echo "  [FAIL] eval/eval.py --all" >&2
  FAILED=$((FAILED + 1))
fi

if [ "$FAILED" -gt 0 ]; then
  echo "[gate] ABORT: $FAILED suite(s) failed. No red submission. Fix and rerun." >&2
  rm -f "$GATE_LOG"
  exit 1
fi
echo "[gate] OK: $SUITES suites ($TOTAL_CHECKS checks) + eval all green"
rm -f "$GATE_LOG"

# ── 2. secret scan ───────────────────────────────────────────────
echo "== secret scan =="
# Patterns: api_key=, sk-, Bearer, token= (case-sensitive so env var names
# like OLLAMA_API_KEY or AUTH_TOKEN in docs do not match). Known-good paths
# are skipped: fixtures/tests hold synthetic data, backups/var/dist are
# runtime output, and serve.py + providers.py name the auth protocol words
# by design. pack.sh and the replay bundle are new files owned by this build.
if git rev-parse --show-toplevel >/dev/null 2>&1; then
  REPO_ROOT="$(git rev-parse --show-toplevel)"
  SCAN_LIST="$(cd "$REPO_ROOT" && git ls-files -co --exclude-standard scaffold/ 2>/dev/null || true)"
else
  REPO_ROOT="$(cd "$SCAFFOLD/.." && pwd)"
  SCAN_LIST="$(cd "$REPO_ROOT" && find scaffold -type f)"
fi

FLAGGED="$(cd "$REPO_ROOT" && for f in $SCAN_LIST; do
  case "$f" in
    scaffold/fixtures/*|scaffold/tests/*|scaffold/backups/*|scaffold/var/*|scaffold/dist/*) continue ;;
    scaffold/deck/node_modules/*) continue ;;
    scaffold/webapp/serve.py|scaffold/engine/providers.py) continue ;;
    scaffold/pack.sh|scaffold/replay/*) continue ;;
  esac
  [ -f "$f" ] || continue
  if grep -nE "api_key=|sk-|Bearer|token=" "$f"; then
    printf '  %s\n' "$f"
  fi
done)"
if [ -n "$FLAGGED" ]; then
  echo "[secret] FLAGGED:" >&2
  echo "$FLAGGED" >&2
  echo "[secret] ABORT: secret-like patterns found in the file(s) above. Fix and rerun." >&2
  exit 1
fi
echo "[secret] OK: no secret-like patterns in the submission tree"

# .env must never ship with the kit
ENV_HITS="$(cd "$REPO_ROOT" && find scaffold -type f -name '.env' -o -type f -name '.env.*' 2>/dev/null || true)"
if [ -n "$ENV_HITS" ]; then
  echo "[secret] ABORT: .env file(s) found, would leak into the pack:" >&2
  echo "$ENV_HITS" >&2
  exit 1
fi

# ── 3. README-SUBMIT.md ──────────────────────────────────────────
echo "== generate README-SUBMIT.md =="
REPO_URL="$(git remote get-url origin 2>/dev/null || echo "unknown")"
COMMIT="$(git rev-parse HEAD 2>/dev/null || echo "unknown")"
EVAL_PASS="$(python3 -c "import json;print(json.load(open('$DIST/eval-report.json'))['pass'])" 2>/dev/null || echo "?")"
EVAL_TOTAL="$(python3 -c "import json;print(json.load(open('$DIST/eval-report.json'))['total'])" 2>/dev/null || echo "?")"

python3 - "$REPO_URL" "$COMMIT" "$TOTAL_CHECKS" "$EVAL_PASS" "$EVAL_TOTAL" <<'PY'
import sys
from pathlib import Path

repo_url, commit = sys.argv[1], sys.argv[2]
total_checks, eval_pass, eval_total = sys.argv[3], sys.argv[4], sys.argv[5]

doc = Path("webapp/serve.py").read_text().split('"""')[1]
rows = []
for line in doc.splitlines():
    if "Auth gate" in line:
        break
    s = line.strip()
    if s.startswith(("GET ", "POST ")):
        parts = s.split(None, 2)
        method, path = parts[0], parts[1]
        desc = parts[2] if len(parts) > 2 else ""
        rows.append((method, path, desc))

lines = []
lines.append("# Craft N Code 2026 Submission")
lines.append("")
lines.append("Team 511 - Signal Engine + shared scaffold, pre-built for the problem drop.")
lines.append("")
lines.append(f"Repo: {repo_url}")
lines.append(f"Commit: {commit}")
lines.append(f"Verified: {total_checks} acceptance checks + {eval_pass}/{eval_total} offline eval checks, all green.")
lines.append("")
lines.append("## Run")
lines.append("")
lines.append("    ./demo.sh                  one-command demo (LLM if key set, else offline)")
lines.append("    ./deploy.sh [TOKEN]        stage deploy on 0.0.0.0 with optional auth")
lines.append("    python3 eval/eval.py --all offline eval gate")
lines.append("    python3 tests/test_*.py    acceptance suites")
lines.append("    ./replay/replay.sh         offline replay bundle (wifi-death story)")
lines.append("")
lines.append("## Endpoints")
lines.append("")
lines.append("| Method | Path | Description |")
lines.append("|--------|------|-------------|")
for method, path, desc in rows:
    lines.append(f"| {method} | `{path}` | {desc} |")
lines.append("")
lines.append("## Kit contents")
lines.append("")
lines.append("- craft-n-code-submission.zip: the scaffold, runtime dirs excluded")
lines.append("- eval-report.json: offline eval evidence")
lines.append("- .env is NOT included: secrets never ship")
lines.append("")
Path("dist/README-SUBMIT.md").write_text("\n".join(lines) + "\n")
print("  [done] dist/README-SUBMIT.md")
PY

# ── 4. zip the scaffold ──────────────────────────────────────────
echo "== build zip =="
rm -f "$ZIP"
python3 - "$ZIP" <<'PY'
import os, sys, zipfile
from pathlib import Path

zpath = sys.argv[1]
root = Path(".").resolve()
skip_dirs = {"var", "backups", "dist", ".git", "node_modules", "__pycache__"}
skip_files = {"signal.db", "signal.db-journal", ".llm_cache.json",
              "stress_server.log", "demo-feed.json", "eval-report.json"}
n = 0
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for name in sorted(filenames):
            if name in skip_files or name.endswith(".pyc"):
                continue
            full = Path(dirpath) / name
            arc = full.relative_to(root).as_posix()
            z.write(full, arc)
            n += 1
print(f"  [done] {zpath} ({n} files)")
PY

# ── 5. checklist ─────────────────────────────────────────────────
echo ""
echo "== SUBMISSION CHECKLIST (06:00 upload) =="
echo "1. video URL:   PASTE THE PITCH VIDEO LINK HERE (record during rehearsal)"
echo "2. deck:        PASTE THE DECK LINK OR FILE PATH HERE"
echo "3. .env:        NOT included (verified by the secret scan above)"
echo "4. team:        Team 511 - add all member names here"
echo "5. unstop:      https://unstop.com/competitions/1730314  (event id 1730314)"
echo ""
echo "Kit is ready in $DIST"
ls -lh "$DIST"
exit 0
