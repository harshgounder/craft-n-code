#!/usr/bin/env bash
# Craft N Code 2026 shared scaffold - one-command demo runner
# Usage: ./demo.sh [port]
set -euo pipefail
PORT="${1:-8137}"
cd "$(dirname "$0")"

# 1. generate the feed (LLM if key present, offline otherwise)
if [ -n "${OLLAMA_API_KEY:-}" ]; then
  echo "[demo] using ollama-cloud LLM"
else
  echo "[demo] no OLLAMA_API_KEY -> offline mode (rule-based, zero network)"
  export OLLAMA_API_KEY="${OLLAMA_API_KEY:-}"
fi
python3 engine/engine.py --seed --out webapp/static/demo-feed.json >/dev/null

# 2. serve
echo "[demo] open http://localhost:${PORT}"
exec python3 webapp/serve.py --port "$PORT"
