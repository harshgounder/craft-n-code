#!/usr/bin/env bash
# Craft N Code 2026 - one-command stage deploy (0.0.0.0 + optional auth gate)
# Usage: ./deploy.sh [AUTH_TOKEN]   or AUTH_TOKEN=... ./deploy.sh
set -euo pipefail
PORT="${PORT:-8137}"
HOST="0.0.0.0"
AUTH_TOKEN="${AUTH_TOKEN:-${1:-}}"
cd "$(dirname "$0")"

# 1. python3 must exist (the whole stack is stdlib-only)
if ! command -v python3 >/dev/null 2>&1; then
  echo "[deploy] ERROR: python3 not found. Install Python 3.10+ (e.g. apt install python3) and rerun." >&2
  exit 1
fi

# 2. var dir for runtime artifacts
mkdir -p var

# 3. same feed generation as demo.sh
if [ -n "${OLLAMA_API_KEY:-}" ]; then
  echo "[deploy] using ollama-cloud LLM"
else
  echo "[deploy] no OLLAMA_API_KEY -> offline mode (rule-based, zero network)"
fi
python3 engine/engine.py --seed --out webapp/static/demo-feed.json >/dev/null

# 4. start the server (background) with optional auth gate
ARGS=(--host "$HOST" --port "$PORT")
if [ -n "$AUTH_TOKEN" ]; then
  ARGS+=(--auth "$AUTH_TOKEN")
fi
echo "[deploy] URL: http://${HOST}:${PORT}"
if [ -n "$AUTH_TOKEN" ]; then
  echo "[deploy] token: ${AUTH_TOKEN}"
fi

python3 webapp/serve.py "${ARGS[@]}" &
SERVER_PID=$!

cleanup() {
  kill "$SERVER_PID" 2>/dev/null || true
  wait "$SERVER_PID" 2>/dev/null || true
}
trap cleanup EXIT

# 5. health probe: curl /health until ready
for _ in $(seq 1 30); do
  if curl -fsS "http://127.0.0.1:${PORT}/health" >/dev/null 2>&1; then
    echo "[deploy] server ready"
    break
  fi
  sleep 0.5
done

# 6. block until the server exits (Ctrl-C -> SIGINT -> cleanup)
wait "$SERVER_PID"
