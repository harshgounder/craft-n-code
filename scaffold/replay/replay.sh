#!/usr/bin/env bash
# Craft N Code 2026 offline replay (BUILD-SPEC B6 wifi-death story).
# Serves the signed golden fixture with zero network, verifies the
# sha256 signature from replay.json, and prints the pipeline trace IDs.
# Usage: ./replay.sh   (PORT=8321 by default, override with PORT=...)
set -euo pipefail
cd "$(dirname "$0")"
ROOT="$(cd .. && pwd)"
PORT="${PORT:-8321}"

FIXTURE="$(python3 -c "import json;print(json.load(open('replay.json'))['fixture'])")"
EXPECTED="$(python3 -c "import json;print(json.load(open('replay.json'))['expected_sha256'])")"
SCREENSHOTS="$(python3 -c "import json;print(json.load(open('replay.json'))['screenshots'])")"

echo "[replay] fixture=$FIXTURE port=$PORT mode=offline (zero network)"
SERVE_LOG="$(mktemp)"
python3 "$ROOT/webapp/serve.py" --port "$PORT" --host 127.0.0.1 \
  --fixture "$FIXTURE" --offline >"$SERVE_LOG" 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true; rm -f "$SERVE_LOG"' EXIT

python3 - "$PORT" "$EXPECTED" "$SCREENSHOTS" <<'PY'
import hashlib, json, sys, time, urllib.request

port = sys.argv[1]
expected = sys.argv[2]
screenshots = sys.argv[3]
base = f"http://127.0.0.1:{port}"


def get(path):
    with urllib.request.urlopen(base + path, timeout=5) as r:
        return r.status, json.loads(r.read().decode())


ready = False
for _ in range(60):
    try:
        st, _ = get("/health")
        if st == 200:
            ready = True
            break
    except Exception:
        pass
    time.sleep(0.25)

if not ready:
    print("[replay] ABORT: server did not answer /health on time", file=sys.stderr)
    sys.exit(1)
print("[replay] /health -> 200 (offline server is up)")

st, feed = get("/api/feed")
st2, trace = get("/api/trace")
trace = trace["steps"]
print(f"[replay] /api/feed -> {st}  /api/trace -> {st2}")

payload = {
    "total": feed["total"],
    "llm": {"model": feed["llm"]["model"]},
    "items": [
        {
            "source_id": it["source_id"],
            "channel": it["channel"],
            "sender": it["sender"],
            "subject": it["subject"],
            "deadline_iso": it.get("deadline_iso"),
            "rank_score": it.get("rank_score"),
            "is_urgent": it.get("is_urgent"),
            "summary": it.get("summary"),
        }
        for it in feed["items"]
    ],
}
canon = json.dumps(payload, sort_keys=True, separators=(",", ":"))
got = hashlib.sha256(canon.encode()).hexdigest()
if got == expected:
    print(f"[replay] signature OK {got}")
else:
    print(f"[replay] signature MISMATCH expected={expected} got={got}", file=sys.stderr)

print("[replay] trace IDs:")
for step in trace:
    name = step.get("step", "?")
    ids = [it.get("source_id") for it in step.get("per_item", [])]
    ids += [it.get("source_id") for it in step.get("top3", [])]
    if ids:
        print(f"  {name}: " + ", ".join(ids))
    else:
        print(f"  {name}: (no item ids)")

print(f"[replay] screenshots go in: {screenshots}")
sys.exit(0 if got == expected else 2)
PY
