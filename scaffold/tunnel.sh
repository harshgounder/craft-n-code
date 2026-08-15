#!/usr/bin/env bash
# Craft N Code 2026 shared scaffold - one-command public tunnel (cloudflared)
# Points a cloudflared quick tunnel at the running server and prints the URL.
# Never blocks forever: --max-wait controls how long we wait for the URL.
# Usage: ./tunnel.sh [--port PORT] [--max-wait SECONDS]
set -euo pipefail

PORT=8137
MAX_WAIT=20

while [ "$#" -gt 0 ]; do
  case "$1" in
    --port)
      PORT="${2:-8137}"
      if [ "$#" -ge 2 ]; then shift 2; else shift; fi
      ;;
    --max-wait)
      MAX_WAIT="${2:-20}"
      if [ "$#" -ge 2 ]; then shift 2; else shift; fi
      ;;
    --help|-h)
      echo "Usage: $0 [--port PORT] [--max-wait SECONDS]"
      exit 0
      ;;
    *)
      echo "unknown arg: $1" >&2
      exit 1
      ;;
  esac
done

if ! command -v cloudflared >/dev/null 2>&1; then
  echo "[tunnel] ERROR: cloudflared is not installed." >&2
  echo "[tunnel] Install it first:" >&2
  echo "  Linux:   curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o /usr/local/bin/cloudflared && chmod +x /usr/local/bin/cloudflared" >&2
  echo "  macOS:   brew install cloudflared" >&2
  echo "  Windows: choco install cloudflared" >&2
  echo "[tunnel] Then rerun: $0 [--port PORT]" >&2
  exit 1
fi

LOG="$(mktemp)"
cloudflared tunnel --url "http://127.0.0.1:${PORT}" >"$LOG" 2>&1 &
CF_PID=$!
cleanup() { rm -f "$LOG"; }
trap cleanup EXIT

URL=""
SECONDS=0
while [ "$SECONDS" -lt "$MAX_WAIT" ]; do
  URL="$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$LOG" | head -n1 || true)"
  if [ -n "$URL" ]; then
    break
  fi
  if ! kill -0 "$CF_PID" 2>/dev/null; then
    break
  fi
  sleep 0.5
done

if [ -z "$URL" ]; then
  echo "[tunnel] ERROR: no public URL after ${MAX_WAIT}s (cloudflared below):" >&2
  tail -n 3 "$LOG" >&2 2>/dev/null || true
  kill "$CF_PID" 2>/dev/null || true
  exit 1
fi

disown "$CF_PID"
echo "[tunnel] public URL: ${URL}"
echo "[tunnel] server: http://127.0.0.1:${PORT} (tunnel keeps running in the background)"
