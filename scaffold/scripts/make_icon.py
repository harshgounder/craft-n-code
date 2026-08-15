#!/usr/bin/env python3
"""Generate the 192x192 PWA placeholder icon with the app initial (stdlib only).

Draws a scaled 5x7 bitmap of the letter S on a solid background and writes a
valid PNG (IHDR/IDAT/IEND chunks, CRC32 via zlib) to webapp/static/icon-192.png.
No external deps, no CDN references. Re-run anytime to regenerate the asset.
"""
from __future__ import annotations

import struct
import zlib
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "webapp" / "static" / "icon-192.png"
SIZE = 192
BG = (11, 16, 32)      # matches --bg #0B1020
FG = (0, 206, 143)     # matches --accent2 #00CE8F

# 5x7 bitmap font glyph for the app initial 'S' (1 = foreground).
GLYPH = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
]

SCALE = 16  # 5*16=80 wide, 7*16=112 tall, centered on 192


def _chunk(tag: bytes, data: bytes) -> bytes:
    body = tag + data
    return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)


def _pixels() -> bytes:
    ox = (SIZE - 5 * SCALE) // 2
    oy = (SIZE - 7 * SCALE) // 2
    rows = []
    for y in range(SIZE):
        row = bytearray([0])  # filter type 0 for this scanline
        for x in range(SIZE):
            gx = (x - ox) // SCALE
            gy = (y - oy) // SCALE
            if 0 <= gx < 5 and 0 <= gy < 7 and GLYPH[gy][gx]:
                r, g, b = FG
            else:
                r, g, b = BG
            row += bytes((r, g, b))
        rows.append(bytes(row))
    return b"".join(rows)


def main() -> int:
    ihdr = struct.pack(">IIBBBBB", SIZE, SIZE, 8, 2, 0, 0, 0)  # 8-bit RGB, no interlace
    png = b"\x89PNG\r\n\x1a\n"
    png += _chunk(b"IHDR", ihdr)
    png += _chunk(b"IDAT", zlib.compress(_pixels(), 9))
    png += _chunk(b"IEND", b"")
    OUT.write_bytes(png)
    print(f"wrote {OUT} ({len(png)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
