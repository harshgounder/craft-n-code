# DECK-RESTYLE-SPEC.md (window-d lane, 2026-08-16)

Rewrite `scaffold/deck/build-krishi-setu.js` in place. This is a STYLE-ONLY rebuild
of the existing Round 0 KrishiSetu deck generator. Read the current file first, then
rewrite it so every text string is byte-identical and only the visual layer changes.

## HARD INVARIANTS (do not violate)

1. **11 slides, same order, same slide count.** Do not add, remove, merge, or reorder slides.
2. **Every text string byte-identical.** Every `addText(...)` string argument, every
   `addNotes(...)` string, every string inside the data arrays (`stats`, `cards`,
   `phases`, `steps`, `proof`, `prior`, `models`, `pilot`, `team`). Copy them from the
   current file character for character. Do not reword, re-case, re-punctuate, renumber.
   Do NOT change numbers: 85/85, 46/46, 48, 2.5M+, 4,000+, A-D, 5,428 acres, 5,882 ha,
   78.4 crore, Rs 1.83 lakh crore, Rs 2,817 crore, 5.25/5.625 etc. stay as they are.
3. **Zero em dashes (U+2014) anywhere in the file**, including comments. Also zero
   banned words: delve, leverage, robust, synergy, seamless, furthermore, moreover,
   additionally, harness, unlock, streamline, notably, significantly, ultimately,
   certainly, indeed, essentially, ultimately (scan the whole file, comments included).
4. **Build command unchanged**: `node build-krishi-setu.js` writes
   `KrishiSetu-Round0-20260816.pptx` in the same directory. Keep `require("pptxgenjs")`.
5. **No external assets**: no images, no URLs, no external fonts. fontFace strings only
   ("Arial Black", "Arial").
6. Keep speaker notes identical to current notes.

## DESIGN LANGUAGE (Canva "Black White Bold 3D Social Media Report")

Replace the green "Forest & Moss" palette and flat look with a black/white bold 3D
report language:

### Palette (constants at top of file)
- `DARK = "0A0A0A"` near-black base (dark slides, card fills)
- `WHITE = "FFFFFF"` pure white (light slides, text on dark)
- `INK = "0A0A0A"` text color on light slides
- `GRAY = "6E6E6E"` muted body text
- `GRAY2 = "B0B0B0"` faint text / back layers on dark slides
- `EDGE = "E0E0E0"` extrusion back layer on light slides
- `CARD_ALT = "161616"` slightly lighter black for cards on dark slides
- `ORANGE = "FF5A1F"` the ONE accent. HAZARD CONTENT ONLY: cyclone/damage stats,
  the alert quote on the moat slide, the limitation box on the close slide, the honesty
  strip edge. Never use orange for neutral content.

### Typography
- Headlines: `fontFace: "Arial Black"`, bold. Hero numerals: "Arial Black" bold.
- Body: `fontFace: "Arial"`.
- No font below 7.5pt.

### Extrusion (the 3D trick, no images)
- **Extruded headline**: draw the text twice. Back copy at `x + 0.045, y + 0.045`,
  color = `EDGE` on light slides, `"2A2A2A"` on dark slides, identical font/size/align.
  Front copy on top with the real color. Add `shadow: { type: "outer", color: "000000",
  blur: 0, angle: 45, offset: 3, opacity: 0.25 }` to the front copy on light slides.
  On dark slides skip the shadow (invisible on black) and rely on the back layer.
- **Extruded cards**: back rect at `x + 0.055, y + 0.055` with fill `EDGE` (light slides)
  or `"2A2A2A"` (dark slides), no line; front card on top. Optionally a thin
  parallelogram strip on the right side of the card (`fill: "555555"` or `EDGE`) as a
  depth face. Front cards may get `rotate: -2` (subtle 3D tilt) on hero/stat panels only;
  body cards stay straight.
- **Perspective accent bars**: thin rects (h ~0.05-0.07) or parallelograms in `INK` /
  `GRAY2` (or `ORANGE` only on hazard content) as dividers under headlines, on card
  corners, and as slide-edge accents. Keep them subtle.

### Slide rhythm
- DARK slides: S1 (title), S2B (research machine portal), S10 (close).
- LIGHT slides: S2, S3, S4, S5, S6, S7, S8, S9 (white background, black type).
- Footers: 8.5pt, `GRAY` on light, `GRAY2` on dark. Same strings as current.

### Per-slide style map (text = current strings, style = below)
- S1: bg `DARK`. "KrishiSetu" 58pt Arial Black `WHITE`, extruded. Subtitle 18pt Arial
  bold `WHITE`. Body line 14pt `GRAY2`. "Team 511 | Craft N Code 2026 | Round 0" 12pt
  `GRAY2`. White perspective bar under the title.
- S2: bg `WHITE`. Header 28pt Arial Black `INK` extruded. Asha story card: black card
  (`DARK` fill, white text), orange left edge bar, `rotate: -2`. Stat cards: black cards,
  numerals 32pt Arial Black `WHITE`, thin `ORANGE` top edge bar on each (hazard stats),
  caption 10pt `GRAY2`, extrusion + `rotate: -2`. "Farmers get warnings..." 17pt Arial
  Black `INK` extruded. Footer same text, `GRAY`.
- S2B: bg `DARK`. Header 32pt Arial Black `WHITE` extruded. 4 portal cards 2x2, fill
  `CARD_ALT`, 1pt line `"2A2A2A"`, `rotate: -1.5`. Inside each: numeral 44pt Arial Black
  `WHITE`; caption 9.5pt `GRAY2`; and a NEW micro source row 7.5pt `"8A8A8A"` reading
  `source: EVIDENCE-INDEX.md · freshness: 2026-08-15` on every card (portal density,
  repo-truth metadata). Bottom bold line: same string, 13pt Arial Black `WHITE`. Footer
  same string, `GRAY2`.
- S3: bg `WHITE`. Header extruded `INK`. Sub-line 16pt Arial bold `INK`. Phase cards:
  white cards, 1.5pt `INK` border, extrusion, `rotate: -1.5`. Number chips: black
  circles (`DARK` fill), white numerals. Phase title 15pt Arial Black `INK`. Body 11pt
  `INK`. Honest framing line 10.5pt italic `GRAY`. Footer same.
- S4: bg `WHITE`. Header extruded. 4 step cards: white cards, 1.5pt `INK` border,
  extrusion. Number chips: black circles, white numerals. Step title 14pt Arial Black
  `INK`. Body 10.5pt `INK`. Sub-line 9.5pt italic `GRAY`. ">" separators 20pt bold
  `GRAY2`. Bottom bold line 13.5pt Arial Black `INK`. Footer same.
- S5: bg `WHITE`. Header extruded. 4 proof cards: black cards (`DARK` fill), numeral
  20pt Arial Black `WHITE`, text 9.5pt `GRAY2`, extrusion + `rotate: -1.5`. Demo arc
  line 11.5pt `INK`. Honesty strip: black card, `ORANGE` left edge bar (warning state),
  text 10.5pt `WHITE`, extrusion. Footer same.
- S6: bg `WHITE`. Header extruded. Alert card: fill `"F2F2F2"`, quote text 17pt Arial
  Black italic `ORANGE` (the hazard alert), sub-line 11pt `GRAY`, `rotate: -2`.
  Advisory card: fill `DARK`, quote 13.5pt `WHITE`, sub-label 12pt Arial Black `WHITE`,
  `rotate: -2`. Prior art: replace the label + 4 loose text rows with ONE pptxgenjs
  table: header row (3 cols, colspan 1 each) = single cell containing the string
  "Prior art", fill `DARK`, text 12pt Arial Black `WHITE`, centered; 4 body rows with
  the current row strings (name col Arial bold `INK`, desc col 10.5pt `GRAY`, gap col
  10.5pt `GRAY2`), row fills alternating `"F7F7F7"` / `WHITE`, 0.5pt `"D9D9D9"` borders.
  Final line 15pt Arial Black `INK` extruded. Footer same.
- S7: bg `WHITE`. Header extruded. 3 buyer cards: black cards, title 16pt Arial Black
  `WHITE`, body 11.5pt `GRAY2`, italic sub 10pt `"8A8A8A"`, extrusion + `rotate: -1.5`.
  Bottom line 13pt Arial Black `INK`. Footer same.
- S8: bg `WHITE`. Header extruded. Two panels: white cards, 2pt `INK` border,
  extrusion. Panel titles 13pt Arial Black `INK`. "78.4 crore PMFBY applications,
  Rs 1.83 lakh crore program" 16pt Arial Black `INK`. Other lines 12.5pt `INK` /
  12pt `INK`. Bottom contract line 14.5pt Arial Black `INK` extruded. Sources line
  10pt italic `GRAY`. Footer same.
- S9: bg `WHITE`. Header extruded. 3 team cards: white cards, 1.5pt `INK` border,
  extrusion. Circle chips: black circles, white numerals. Name 15pt Arial Black `INK`.
  Role 11.5pt `GRAY`. Bio 9.5pt italic `GRAY`. Shipped line 13pt Arial Black `INK`.
  Footer same.
- S10: bg `DARK`. "Grade our decision quality." 40pt Arial Black `WHITE` extruded.
  Sub-line 15pt `GRAY2`. Limitation card: fill `CARD_ALT`, `ORANGE` left edge bar
  (limitation = warning), text 12pt `WHITE`, thin line `"2A2A2A"`. Bottom line 12.5pt
  `GRAY2`. Same strings.

### Code structure
Keep the same overall structure (constants, helpers `header`/`card`/`footer`, one slide
block per section, `p.writeFile` at the end). You may add helper functions for
extruded text and extruded cards. Keep comments minimal, no em dashes in comments.

### Self-check before finishing
- `node build-krishi-setu.js` runs clean and prints DECK WRITTEN.
- Grep the file for U+2014 (em dash): zero hits. Grep for banned words: zero hits.
- Diff against git HEAD: every changed line is a style/visual change, no string content changed.
