# BUILD-SPEC-4.md: MCP slide + cover badge in the deck generator

Grounding: scaffold/deck/deck-gen.js (12.3K, pptxgenjs). It has an IDEAS
config with 4 skins (agentic, creative, multimodal, kavach), each with
file/accent/title/tagline/problem/solution/demo arrays, and build(idea)
renders the slides. The MCP shape (shape 6) has no dedicated slide; the
idea lab drill (MOCK-DROP-20260815) flagged this as the only asset gap.
Goal: add ONE optional mcpSlide per idea + a cover badge, so a shape-6
problem statement maps to a deck without a rebuild.

## Part 1: config (deck-gen.js)

Add to each of the 4 IDEAS entries an `mcpSlide` object:
  mcpSlide: { title: <string>, bullets: [<string> x 4] }
Titles and bullets must be domain-appropriate per skin, drawn from:
- approval-gated MCP is the least-shipped sub-niche (~52% dead-server
  share in registries) = our wedge
- official MCP registry 9,652 servers; spec dates 2024-11-05 (HTTP+SSE
  deprecated), 2025-03-26 (Streamable HTTP), 2026-07-28 (stateless
  core, hardened auth, MRTR)
- tool poisoning is the headline attack class (Invariant Labs
  1 Apr 2025, OWASP indirect prompt injection via server responses)
- we compose gold-plated servers (filesystem, GitHub, Supabase, Slack,
  Playwright, Redis, Postgres), never rebuild them; typed allow-listed
  tools, policy gate outside the model
- human approval at every handoff, audit trace on every call
No em dashes in any new string. No banned words (see docs rules).

## Part 2: render (deck-gen.js)

- In build(idea): after the demo slide is added, if idea.mcpSlide
  exists, add ONE slide titled idea.mcpSlide.title with the 4 bullets,
  using the same layout helpers as the existing slides (matching
  accent color + panel styling).
- On slide 1 (cover): if idea.mcpSlide exists, add a small badge text
  near the bottom: "MCP-READY" in the idea accent color, plain text,
  no shapes. Do not disturb existing cover layout.
- Ideas WITHOUT mcpSlide are unaffected (the if-guard must work when
  the key is absent).

## Acceptance (numbered, run by Hermes after the build)

M1. node deck-gen.js exits 0 and regenerates all 4 .pptx files.
M2. Slide count of each deck increases by EXACTLY 1 vs the previous
    build (count slides/slideN.xml entries via unzip -l; record
    before/after).
M3. The new slide's title text exists in the pptx XML (grep the
    mcpSlide title string in the unzipped deck).
M4. The cover badge "MCP-READY" appears on slide 1 XML of each deck.
M5. grep -rl "—" on scaffold/deck returns nothing (no em dashes).
M6. No other file changed (git status shows only deck-gen.js + the 4
    .pptx). No git commit.

Boundary rules: only scaffold/deck/deck-gen.js may change (plus the 4
generated .pptx). Do NOT touch serve.py, engine/, tests/, fixtures/,
index.html, README, or docs. Do NOT git commit. Do NOT add npm
packages (pptxgenjs already present).
