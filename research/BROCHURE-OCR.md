# Brochure OCR — Craft N Code 2024 + D³ Fest 2025

Compiled: 2026-08-13 | Method: Scribd page-image extraction (r.jina.ai leaked hashes) + tesseract OCR

## Craft N Code 2024 brochure (Scribd doc 781392222, 9 pages, uploaded by jiteshauddy.06)

### Page 1 (OCR'd, full-res)
- D³ Fest branding: "D³ FEST" + "IIIT BHUBANESWAR" + "CRAFT N CODE" + "NATIONAL LEVEL HACKATHON"
- Address: IIIT Bhubaneswar, AT-GOTHAPATANA, PO-MALIPADA, BHUBANESWAR, ODISHA 751003

### Page 2 (OCR'd)
- "The Craft-N-Code Hackathon, organized by the Tech Society at IIIT Bhubaneswar, is a major competition involving colleges across India and beyond."
- "This year, the event features hackathons in different states, with top teams advancing to the final round at IIIT Bhubaneswar."
- "Open to all bachelor's degree students, teams of 2-4 members from the same state compete to showcase their innovation and technical skills."

### Pages 3-9
- NOT OCR'd: page-image hashes are per-page random; only pages 1-2 leaked via r.jina.ai. The /original/{hash}/{page} pattern serves page 1 for all pages (hash is per-document).
- The full rules text was recovered from the Unstop API details instead (see PROBLEM-BANK-SPONSOR-DNA.md).

## D³ Fest 2025 brochure (Scribd doc 917484478, uploaded by Shailendra Kumar)

### Page 1 (OCR'd)
- D³ Fest branding, IIIT Bhubaneswar address (same campus)

### Page 2 (OCR'd) — INTRODUCTION
- "Get ready to rewind the past and fast-forward the future at D3 Techno Fest!"
- "Brought to life by the Tech and Robotics Societies of IIIT Bhubaneswar."
- "D3 is not just a fest — it's a four-day symphony of retro aesthetics and futuristic innovation."
- "Dive into a world where vintage charm meets tomorrow's tech, crafted for dreamers, doers, and disrupters across tech, management, and entrepreneurship."
- "Whether you're channeling 80s arcade energy or pioneering the next big breakthrough, D3 is your stage."
- "Buckle up for a high-voltage ride packed with retro flair, modern sparks, and mind-blowing rewards!"
- "From quirky challenges to creative showdowns, D3 promises endless fun, innovation, and memories that'll stick with you like your favorite cassette jam."

### Pages 3-12
- NOT OCR'd (same hash limitation)

## Method note (reusable)
1. r.jina.ai on the Scribd URL leaks the first 2 page-image URLs (html.scribdassets.com/{doc-hash}/images/{n}-{page-hash}.jpg)
2. The imgv2 original URL (imgv2-1-f.scribdassets.com/img/document/{id}/original/{doc-hash}/{page}?v=1) serves page 1 for ANY page number — the {page} segment is ignored
3. Full OCR of all pages requires the per-page hashes, which are only in the JS-rendered reader (headless browser needed)
