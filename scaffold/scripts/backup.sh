#!/usr/bin/env bash
# Backup the storage layer (BUILD-SPEC B9): timestamped copy of the DB
# files plus the JSON feed cache into backups/. The app keeps running on
# the original DB, untouched.
#
# Usage: ./scripts/backup.sh [backup_dir]   (default: backups/)
set -euo pipefail
cd "$(dirname "$0")/.."

OUT_DIR="${1:-backups}"
STAMP="$(date +%Y%m%d-%H%M%S)"
DEST="$OUT_DIR/$STAMP"
mkdir -p "$DEST"

COPIED=0

# DB files (engine/signal.db and any other sqlite databases)
for db in engine/*.db; do
  if [ -f "$db" ]; then
    cp "$db" "$DEST/"
    COPIED=$((COPIED + 1))
  fi
done

# Feed cache: JSON feed files refreshed by engine/feeds.py
if [ -d data/feeds ]; then
  cp -r data/feeds "$DEST/feeds"
  COPIED=$((COPIED + 1))
fi

echo "[backup] wrote $DEST ($COPIED sources)"
