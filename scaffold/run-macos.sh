#!/usr/bin/env bash
# Craft N Code 2026 shared scaffold - one-command launcher (macOS)
# Same behavior as demo.sh: generate the feed, then serve.
# Usage: ./run-macos.sh [--port PORT] [--auth TOKEN]
set -euo pipefail

PORT=8137
AUTH=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --port)
      PORT="${2:-8137}"
      if [ "$#" -ge 2 ]; then shift 2; else shift; fi
      ;;
    --auth)
      AUTH="${2:-}"
      if [ "$#" -ge 2 ]; then shift 2; else shift; fi
      ;;
    --help|-h)
      echo "Usage: $0 [--port PORT] [--auth TOKEN]"
      exit 0
      ;;
    *)
      echo "unknown arg: $1" >&2
      exit 1
      ;;
  esac
done

cd "$(dirname "$0")"

# 1. generate the feed (LLM if key present, offline otherwise)
if [ -n "${OLLAMA_API_KEY:-}" ]; then
  echo "[run] using ollama-cloud LLM"
else
  echo "[run] no OLLAMA_API_KEY -> offline mode (rule-based, zero network)"
fi
python3 engine/engine.py --seed --out webapp/static/demo-feed.json >/dev/null

# 2. serve with optional port/auth passthrough
ARGS=(--port "$PORT")
if [ -n "$AUTH" ]; then
  ARGS+=(--auth "$AUTH")
fi
echo "[run] open http://localhost:${PORT}"
exec python3 webapp/serve.py "${ARGS[@]}"
