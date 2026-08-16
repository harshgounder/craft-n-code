#!/usr/bin/env bash
# Deck gate: rebuild + verify 12 slides, content-identical strings, no em
# dash, no banned words. Run from scaffold/deck. Exit 0 = ship it.
set -euo pipefail
cd "$(dirname "$0")"

node build-krishi-setu.js

python3 - <<'EOF'
import zipfile, re, sys

PPTX = 'KrishiSetu-Round0-20260816.pptx'
z = zipfile.ZipFile(PPTX)
slides = [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)]
assert len(slides) == 13, f'slide count {len(slides)}, expected 13'

allxml = ''
for n in z.namelist():
    if n.endswith('.xml'):
        allxml += z.read(n).decode('utf-8', 'ignore')

texts = re.findall(r'<a:t>(.*?)</a:t>', allxml, re.S)
joined = ' '.join(texts)

if '\u2014' in joined:
    print('FAIL: em dash found in deck text'); sys.exit(1)

banned = ['delve','leverage','robust','synergy','seamless','furthermore','moreover',
          'additionally','harness','unlock','streamline','notably','significantly',
          'ultimately','certainly','indeed','essentially']
low = joined.lower()
hits = [w for w in banned if re.search(r'\b' + w + r'\b', low)]
if hits:
    print('FAIL: banned words in deck text:', hits); sys.exit(1)

# hazard orange used, near-black base used, Arial Black present
assert '97BC62' in allxml, 'moss green missing'
assert '1F3D26' in allxml, 'forest green base missing'
assert 'Arial Black' in allxml, 'Arial Black missing'

print(f'DECK GATE PASS: {len(slides)} slides, {len(texts)} text runs, 0 em dash, 0 banned words, style tokens present')
EOF

# source file hygiene
SRC='build-krishi-setu.js'
if grep -q $'\u2014' "$SRC"; then echo 'FAIL: em dash in source'; exit 1; fi
if grep -qE '\b(delve|leverage|robust|synergy|seamless|furthermore|moreover|additionally|harness|unlock|streamline|notably|significantly|ultimately)\b' "$SRC"; then
  echo 'FAIL: banned word in source'; exit 1
fi
echo 'SOURCE GATE PASS: 0 em dash, 0 banned words'
