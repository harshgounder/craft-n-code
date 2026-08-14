#!/usr/bin/env bash
# Serve the built atlas site on port 8900.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "Atlas site: http://localhost:8900/atlas/site/index.html"
exec python3 -m http.server 8900
