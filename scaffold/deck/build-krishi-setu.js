// KrishiSetu Round 0 deck (PS-07), Craft N Code 2026, Team 511
// Design v2: Editorial Field Journal / Monsoon Data Report (Canva-style)
// Build: node build-krishi-setu.js  ->  KrishiSetu-Round0-20260816.pptx
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_16x9"; // 10 x 5.625 in
p.author = "Team 511";
p.title = "KrishiSetu - Craft N Code 2026 Round 0";

// ============ DESIGN TOKENS ============
// Topic: agriculture + cyclone + coastal Odisha. Warm paper, deep paddy green,
// one harvest-amber accent. Editorial serif (Georgia) + Trebuchet labels + Courier data.
const PAPER = "F6F3EA";      // warm cream field-notebook paper
const PAPER2 = "EFE9DC";     // deeper cream for dull panels
const WHITE = "FFFEF9";      // warm white card surface
const INK = "1C2A22";        // deep forest ink
const PINE = "1E5A3A";       // deep paddy green (primary)
const PINE_DARK = "14341F";  // title/close/panel background
const PINE_PANEL = "1F3A28"; // raised dark panel
const PINE_LINE = "3A6B4E";  // hairline on dark
const MOSS = "8FAE8B";       // soft moss on dark
const MOSS_LINE = "CBD8C4";  // light moss on paper
const AMBER = "E08A2E";      // accent fill on dark
const AMBER_TXT = "9A5510";  // accent text on paper (AA)
const AMBER_SOFT = "F2D9B8"; // honesty panel
const RED = "B3402E";        // danger, rare
const CREAM = "F6F3EA";      // text on dark
const MUTED = "5E665B";      // muted text on paper
const LINE = "D8D2C4";       // hairline on paper

const DISP = "Georgia";
const BODY = "Georgia";
const LABEL = "Trebuchet MS";
const MONO = "Courier New";

const M = 0.55;      // margin
const W = 10;
const H = 5.625;
const CW = W - 2 * M; // content width 8.9

// ============ HELPERS ============
function eyebrow(s, text, dark) {
  s.addText(text.toUpperCase(), {
    x: M, y: 0.3, w: CW, h: 0.28,
    fontSize: 9.5, bold: true, color: dark ? AMBER : AMBER_TXT,
    fontFace: LABEL, charSpacing: 3, margin: 0,
  });
}
function title(s, text, dark, size) {
  s.addText(text, {
    x: M, y: 0.58, w: CW, h: 0.62,
    fontSize: size || 27, bold: true, color: dark ? CREAM : INK,
    fontFace: DISP, margin: 0,
  });
}
function hairline(s, y, color, x, w) {
  s.addShape(p.ShapeType.rect, {
    x: x === undefined ? M : x, y: y, w: w === undefined ? CW : w, h: 0.012,
    fill: { color: color || LINE }, line: { color: color || LINE, width: 0 },
  });
}
function pageNum(s, n, dark) {
  s.addText(String(n).padStart(2, "0") + " / 11", {
    x: W - M - 1.2, y: H - 0.36, w: 1.2, h: 0.24,
    fontSize: 8, bold: true, color: dark ? MOSS : MUTED,
    fontFace: MONO, align: "right", margin: 0,
  });
}
function footerNote(s, text, dark) {
  s.addText(text, {
    x: M, y: H - 0.36, w: 6.4, h: 0.24,
    fontSize: 7.5, color: dark ? MOSS : MUTED, fontFace: MONO, margin: 0,
  });
}
function card(s, x, y, w, h, fill, border) {
  return s.addShape(p.ShapeType.roundRect, {
    x: x, y: y, w: w, h: h,
    fill: { color: fill || WHITE },
    line: { color: border || LINE, width: border ? 1.25 : 0.75 },
    rectRadius: 0.05,
  });
}
function bar(s, x, y, w, h, color) {
  s.addShape(p.ShapeType.rect, {
    x: x, y: y, w: w, h: h, fill: { color: color }, line: { color: color, width: 0 },
  });
}
function chip(s, x, y, w, h, text, opt) {
  const o = opt || {};
  s.addShape(p.ShapeType.roundRect, {
    x: x, y: y, w: w, h: h,
    fill: { color: o.fill || "1F3A28" },
    line: { color: o.line || "3A6B4E", width: o.lineW || 0.75 },
    rectRadius: 0.5,
  });
  s.addText(text, {
    x: x, y: y, w: w, h: h, align: o.align || "center", valign: "middle",
    fontSize: o.size || 8.5, bold: o.bold !== false, color: o.color || CREAM,
    fontFace: LABEL, margin: 0, charSpacing: o.spacing || 1,
  });
}
function arrow(s, x, y, w, h, color) {
  s.addShape(p.ShapeType.rightArrow, {
    x: x, y: y, w: w, h: h,
    fill: { color: color || AMBER }, line: { color: color || AMBER, width: 0 },
  });
}
// signature motif: crop rows (thin parallel lines) bottom-left
function cropRows(s, dark) {
  const c = dark ? "3A5C44" : MOSS_LINE;
  for (let i = 0; i < 4; i++) {
    bar(s, M, 4.78 + i * 0.115, 0.55 + i * 0.42, 0.022, c);
  }
}
// signature motif: cyclone arcs top-right
function arcs(s) {
  const cols = ["2E4C38", "3D5C46", "55755E"];
  for (let i = 0; i < 3; i++) {
    s.addShape(p.ShapeType.ellipse, {
      x: 7.1 + i * 0.62, y: -0.9 + i * 0.5, w: 2.6, h: 2.6,
      fill: { color: "14341F" }, line: { color: cols[i], width: 1.5 },
      rectRadius: 0,
    });
  }
}
function statHero(s, x, y, w, num, unit, label, source, dark) {
  s.addText(num, {
    x: x, y: y, w: w, h: 0.62, fontSize: 30, bold: true,
    color: dark ? AMBER : PINE, fontFace: DISP, margin: 0, valign: "middle",
  });
  if (unit) s.addText(unit, {
    x: x + w * 0.42, y: y + 0.06, w: w * 0.58, h: 0.3,
    fontSize: 10, bold: true, color: dark ? CREAM : AMBER_TXT,
    fontFace: LABEL, margin: 0,
  });
  s.addText(label, {
    x: x, y: y + 0.66, w: w, h: 0.62, fontSize: 10, color: dark ? MOSS : MUTED,
    fontFace: BODY, margin: 0, lineSpacing: 13,
  });
  if (source) s.addText(source.toUpperCase(), {
    x: x, y: y + 1.24, w: w, h: 0.2, fontSize: 7, bold: true,
    color: dark ? MOSS : "8A8477", fontFace: MONO, margin: 0,
  });
}
function phoneMock(s, x, y, w, h) {
  // basic-phone silhouette with SMS screen (abstract, no glyphs)
  const bw = w, bh = h;
  s.addShape(p.ShapeType.roundRect, {
    x: x, y: y, w: bw, h: bh, fill: { color: PINE_DARK },
    line: { color: PINE_LINE, width: 1 }, rectRadius: 0.14,
  });
  // screen
  s.addShape(p.ShapeType.roundRect, {
    x: x + bw * 0.07, y: y + bh * 0.09, w: bw * 0.86, h: bh * 0.74,
    fill: { color: "F6F3EA" }, line: { color: "F6F3EA", width: 0 }, rectRadius: 0.04,
  });
  // status bar
  bar(s, x + bw * 0.12, y + bh * 0.13, bw * 0.5, 0.03, "D8D2C4");
  bar(s, x + bw * 0.72, y + bh * 0.13, bw * 0.16, 0.03, "D8D2C4");
  // message bubble 1 (advisory)
  s.addShape(p.ShapeType.roundRect, {
    x: x + bw * 0.12, y: y + bh * 0.24, w: bw * 0.62, h: bh * 0.3,
    fill: { color: PINE }, line: { color: PINE, width: 0 }, rectRadius: 0.08,
  });
  bar(s, x + bw * 0.17, y + bh * 0.28, bw * 0.48, 0.028, "E8F0E4");
  bar(s, x + bw * 0.17, y + bh * 0.35, bw * 0.40, 0.028, "E8F0E4");
  bar(s, x + bw * 0.17, y + bh * 0.42, bw * 0.52, 0.028, "F2D9B8");
  // message bubble 2 (action, amber)
  s.addShape(p.ShapeType.roundRect, {
    x: x + bw * 0.12, y: y + bh * 0.6, w: bw * 0.55, h: bh * 0.2,
    fill: { color: AMBER }, line: { color: AMBER, width: 0 }, rectRadius: 0.08,
  });
  bar(s, x + bw * 0.17, y + bh * 0.65, bw * 0.42, 0.028, "FBEBD6");
  // keypad dots
  for (let i = 0; i < 3; i++) {
    s.addShape(p.ShapeType.ellipse, {
      x: x + bw * 0.18 + i * 0.24, y: y + bh * 0.88, w: 0.07, h: 0.07,
      fill: { color: PINE_LINE }, line: { color: PINE_LINE, width: 0 },
    });
  }
}

// ============ S1 TITLE (dark) ============
{
  const s = p.addSlide();
  s.background = { color: PINE_DARK };
  arcs(s);
  cropRows(s, true);
  s.addText("CRAFT N CODE 2026  ·  ROUND 0  ·  TEAM 511", {
    x: M, y: 0.42, w: CW, h: 0.28, fontSize: 9.5, bold: true,
    color: MOSS, fontFace: LABEL, charSpacing: 3, margin: 0,
  });
  s.addText([
    { text: "KrishiSetu", options: { color: CREAM } },
    { text: ".", options: { color: AMBER } },
  ], {
    x: M, y: 1.25, w: 8.4, h: 1.05, fontSize: 56, bold: true,
    fontFace: DISP, margin: 0, valign: "middle",
  });
  s.addText("Cyclone and Flood Resilient Smart Agriculture Advisory", {
    x: M, y: 2.42, w: 8.4, h: 0.4, fontSize: 17, color: MOSS, fontFace: DISP, margin: 0,
  });
  s.addText("For coastal Odisha farmers, KrishiSetu turns a cyclone forecast into a crop-stage-specific action and an insurance claim packet, in Odia, on a basic phone.", {
    x: M, y: 2.98, w: 5.9, h: 0.95, fontSize: 13, color: CREAM,
    fontFace: BODY, margin: 0, lineSpacing: 17,
  });
  // decision stamp
  chip(s, M, 4.2, 1.5, 0.42, "FORECAST", { fill: "1F3A28", line: "3A6B4E", color: CREAM, size: 9 });
  arrow(s, M + 1.57, 4.3, 0.26, 0.2, AMBER);
  chip(s, M + 1.9, 4.2, 2.3, 0.42, "ACTION + DEADLINE", { fill: AMBER, line: AMBER, color: PINE_DARK, size: 9 });
  arrow(s, M + 4.27, 4.3, 0.26, 0.2, AMBER);
  chip(s, M + 4.6, 4.2, 1.95, 0.42, "CLAIM PACKET", { fill: "1F3A28", line: "3A6B4E", color: CREAM, size: 9 });
  s.addText("github.com/harshgounder/craft-n-code", {
    x: 3.3, y: H - 0.4, w: 3.85, h: 0.24, fontSize: 8, color: MOSS, fontFace: MONO, align: "right", margin: 0,
  });
  s.addNotes("Working name KrishiSetu (farm bridge), swappable. Round 0: prototype + deck, judged by IIIT-B faculty. One-liner states the promise: forecast becomes action plus claim packet, Odia, basic phone.");
}

// ============ S2 PROBLEM ============
{
  const s = p.addSlide();
  s.background = { color: PAPER };
  cropRows(s, false);
  eyebrow(s, "The Problem");
  title(s, "Warnings arrive. Decisions do not.");
  hairline(s, 1.28);
  // left: Asha pull-quote panel
  bar(s, M, 1.5, 0.055, 1.86, AMBER);
  card(s, M, 1.5, 4.35, 1.86, WHITE);
  s.addText("Asha, 47, flowering paddy on a low-lying plot in Balasore. Post-Yaas field reporting documents saltwater on 5,882 hectares across five blocks. The alert came. The action did not.", {
    x: 0.8, y: 1.66, w: 3.95, h: 1.15, fontSize: 12.5, italic: true,
    color: INK, fontFace: BODY, margin: 0, lineSpacing: 16,
  });
  s.addText("COMPOSITE PERSONA · POST-YAAS BALASORE FIELD REPORTING", {
    x: 0.8, y: 2.86, w: 3.95, h: 0.22, fontSize: 7, bold: true,
    color: "8A8477", fontFace: MONO, margin: 0,
  });
  s.addText("Farmers get warnings. They do not get decisions.", {
    x: M, y: 3.6, w: 4.35, h: 0.5, fontSize: 15, bold: true,
    color: PINE, fontFace: DISP, margin: 0,
  });
  chip(s, M, 4.14, 1.55, 0.34, "DANA 2024 · RAPID ASSESSMENT", { fill: WHITE, line: LINE, color: MUTED, size: 7, align: "center" });
  chip(s, M + 1.68, 4.14, 1.95, 0.34, "YAAS 2021 · DOWN TO EARTH", { fill: WHITE, line: LINE, color: MUTED, size: 7, align: "center" });
  // right: two hero stat cards (varied emphasis)
  card(s, 5.15, 1.5, 4.3, 1.42, WHITE);
  statHero(s, 5.35, 1.62, 3.9, "5,428", "acres", "crop loss across 4 blocks, Kendrapada + Bhadrak, Cyclone Dana 2024 (rapid assessment)", "YSD ODISHA RAPID ASSESSMENT");
  card(s, 5.15, 3.06, 4.3, 1.42, WHITE);
  statHero(s, 5.35, 3.18, 3.9, "5,882", "ha", "cultivable land salt-affected across 5 Balasore blocks, Cyclone Yaas 2021", "DOWN TO EARTH · POST-YAAS KHARIF REPORT");
  // bottom band: the insurance rail
  bar(s, M, 4.62, CW, 0.66, PINE);
  s.addText("78.4 crore", {
    x: 0.75, y: 4.7, w: 2.2, h: 0.5, fontSize: 21, bold: true,
    color: CREAM, fontFace: DISP, margin: 0, valign: "middle",
  });
  s.addText("PMFBY crop-insurance applications · Rs 1.83 lakh crore program", {
    x: 3.05, y: 4.76, w: 4.4, h: 0.4, fontSize: 10.5, color: CREAM, fontFace: BODY, margin: 0,
  });
  chip(s, 7.55, 4.76, 1.7, 0.38, "THE RAIL EXISTS", { fill: "14341F", line: AMBER, color: AMBER, size: 8 });
  footerNote(s, "Sources: YSD Odisha Cyclone Dana rapid assessment; Down To Earth post-Yaas Kharif report; PMFBY program data. Verified, dated 2024-2025.");
  pageNum(s, 2);
  s.addNotes("One problem, one cost. Asha is a composite persona grounded in post-Yaas Balasore field reporting, not a named individual. PMFBY numbers show the insurance rail already exists and is huge: the gap is verified observation, not scheme design.");
}

// ============ S3 RESEARCH MACHINE (dark, the wow slide) ============
{
  const s = p.addSlide();
  s.background = { color: PINE_DARK };
  arcs(s);
  eyebrow(s, "The Evidence", true);
  title(s, "A research machine, not a chat output.", true);
  hairline(s, 1.28, PINE_LINE);
  // giant 48
  s.addText("48", {
    x: M, y: 1.5, w: 2.5, h: 1.55, fontSize: 96, bold: true,
    color: AMBER, fontFace: DISP, margin: 0, valign: "middle",
  });
  s.addText("parallel deep-research runs · 7 waves · every run multi-channel", {
    x: M, y: 3.28, w: 2.75, h: 0.9, fontSize: 11.5, color: CREAM,
    fontFace: BODY, margin: 0, lineSpacing: 15,
  });
  // vertical rule separating the columns
  bar(s, 3.55, 1.5, 0.014, 1.9, PINE_LINE);
  // right: two hero rows
  s.addText("2.5M+", {
    x: 3.85, y: 1.5, w: 2.3, h: 0.7, fontSize: 34, bold: true,
    color: CREAM, fontFace: DISP, margin: 0,
  });
  s.addText("chars of raw evidence: named, dated sources on every claim, no claim ships without one", {
    x: 6.25, y: 1.58, w: 3.2, h: 0.75, fontSize: 10.5, color: MOSS,
    fontFace: BODY, margin: 0, lineSpacing: 14,
  });
  hairline(s, 2.48, PINE_LINE, 3.85, 5.6);
  s.addText("4,000+", {
    x: 3.85, y: 2.68, w: 2.3, h: 0.7, fontSize: 34, bold: true,
    color: CREAM, fontFace: DISP, margin: 0,
  });
  s.addText("cited sources across 6 continents: cyclone, food and agri ledgers, cascade math, human wisdom, frontier science", {
    x: 6.25, y: 2.76, w: 3.2, h: 0.75, fontSize: 10.5, color: MOSS,
    fontFace: BODY, margin: 0, lineSpacing: 14,
  });
  // evidence grade chips
  s.addText("EVIDENCE GRADING ON EVERY CLAIM:", {
    x: M, y: 4.05, w: 3.2, h: 0.24, fontSize: 8, bold: true, color: MOSS,
    fontFace: MONO, margin: 0,
  });
  const grades = [
    ["A", "ODISHA-MEASURED", 1.75],
    ["B", "TRANSFER-PRIOR", 1.6],
    ["C", "SCENARIO-ASSUMPTION", 1.95],
    ["D", "UNKNOWN", 1.15],
  ];
  let gx = M;
  grades.forEach((g) => {
    chip(s, gx, 4.34, g[2], 0.4, g[0] + "  " + g[1], { fill: "1F3A28", line: PINE_LINE, color: CREAM, size: 8 });
    gx += g[2] + 0.18;
  });
  // evidence chain strip
  bar(s, M, 4.96, CW, 0.44, "1F3A28");
  s.addText("EVIDENCE CHAIN: SLIDE → PROOF LEDGER → EVIDENCE-INDEX.MD → RAW REPORT → NAMED, DATED SOURCE", {
    x: 0.75, y: 5.05, w: 8.5, h: 0.26, fontSize: 8, bold: true,
    color: AMBER, fontFace: MONO, margin: 0,
  });
  pageNum(s, 3, true);
  s.addNotes("This slide is the holy-shit moment: 48 runs, 7 waves, 2.5M chars, 4,000+ sources, A-D grades. Judges who ask 'where is this from' get a path. Never claim we read everything without this map to prove it.");
}

// ============ S4 SOLUTION ============
{
  const s = p.addSlide();
  s.background = { color: PAPER };
  cropRows(s, false);
  eyebrow(s, "The Solution");
  title(s, "An advisory engine, not an alert system.");
  hairline(s, 1.28);
  s.addText("Every forecast becomes a decision: an action, a deadline, a source, and a fallback. In Odia, on any phone.", {
    x: M, y: 1.42, w: CW, h: 0.4, fontSize: 13, color: INK, fontFace: BODY, margin: 0,
  });
  // three phase blocks with arrows, DURING featured
  const phases = [
    { tag: "BEFORE", head: "Stage the crop", items: ["harvest or move to raised platform on a deadline", "protect seed, livestock, equipment", "evacuate people, secure the house"], feat: false },
    { tag: "DURING", head: "Shelter and safety", items: ["Odia guidance for the household", "livestock and fodder checklist", "keep the advisory reachable offline"], feat: true },
    { tag: "AFTER", head: "Recovery and claims", items: ["saline flush and re-sowing plan per plot", "damage evidence capture on a basic phone", "PMFBY claim packet export"], feat: false },
  ];
  const bw = 2.62, gap = 0.34;
  phases.forEach((ph, i) => {
    const x = M + i * (bw + gap);
    const y = 1.95, bh = ph.feat ? 2.5 : 2.3;
    card(s, x, y, bw, bh, WHITE, ph.feat ? PINE : LINE);
    bar(s, x, y, bw, ph.feat ? 0.13 : 0.07, ph.feat ? AMBER : PINE);
    s.addText(ph.tag, {
      x: x + 0.18, y: y + 0.22, w: bw - 0.36, h: 0.3, fontSize: 12, bold: true,
      color: ph.feat ? AMBER_TXT : PINE, fontFace: LABEL, charSpacing: 2, margin: 0,
    });
    s.addText(ph.head, {
      x: x + 0.18, y: y + 0.56, w: bw - 0.36, h: 0.34, fontSize: 13.5, bold: true,
      color: INK, fontFace: DISP, margin: 0,
    });
    ph.items.forEach((it, j) => {
      s.addText("·  " + it, {
        x: x + 0.18, y: y + 1.02 + j * 0.44, w: bw - 0.36, h: 0.42,
        fontSize: 9, color: MUTED, fontFace: BODY, margin: 0, lineSpacing: 11.5,
      });
    });
    if (i < 2) arrow(s, x + bw + 0.055, y + 1.1, 0.23, 0.17, AMBER);
  });
  s.addText("Honest framing: the advisory engine is the hero. Acknowledgement and report capture are adaptation features inside it, not the pitch.", {
    x: M, y: 4.62, w: CW, h: 0.34, fontSize: 10, italic: true, color: MUTED, fontFace: BODY, margin: 0,
  });
  footerNote(s, "Statement-faithful: the official problem is a resilient advisory system for cyclone and flood contexts, with farm-profile-aware, staged actions.");
  pageNum(s, 4);
  s.addNotes("This is the user-corrected framing: the topic is an advisory platform, not an alert platform. Every action card carries a deadline and a source in the product; the deck keeps that promise on the mechanism slide.");
}

// ============ S5 MECHANISM (money slide) ============
{
  const s = p.addSlide();
  s.background = { color: PAPER };
  cropRows(s, false);
  eyebrow(s, "The Mechanism");
  title(s, "Ingest, decide, deliver, recover.");
  hairline(s, 1.28);
  // dark pipeline panel
  bar(s, M, 1.45, CW, 1.78, PINE_DARK);
  const steps = [
    ["1", "INGEST", "IMD forecast + farm profile: crop, stage, plot, soil, connectivity"],
    ["2", "DECIDE", "agronomist-reviewed rules: pre/during/post × crop × stage × hazard"],
    ["3", "DELIVER", "Odia SMS + IVR, offline queue, ack + report capture"],
    ["4", "RECOVER", "recovery chain + claims evidence packet"],
  ];
  const sw = 1.95, sg = 0.36;
  steps.forEach((st, i) => {
    const x = M + i * (sw + sg);
    s.addShape(p.ShapeType.ellipse, {
      x: x + 0.13, y: 1.62, w: 0.4, h: 0.4,
      fill: { color: AMBER }, line: { color: AMBER, width: 0 },
    });
    s.addText(st[0], {
      x: x + 0.13, y: 1.66, w: 0.4, h: 0.32, fontSize: 13, bold: true,
      color: PINE_DARK, fontFace: LABEL, align: "center", margin: 0,
    });
    s.addText(st[1], {
      x: x + 0.62, y: 1.66, w: sw - 0.7, h: 0.3, fontSize: 11.5, bold: true,
      color: CREAM, fontFace: LABEL, charSpacing: 1.5, margin: 0, valign: "middle",
    });
    s.addText(st[2], {
      x: x + 0.13, y: 2.14, w: sw - 0.2, h: 0.95, fontSize: 8.5, color: MOSS,
      fontFace: BODY, margin: 0, lineSpacing: 11,
    });
    if (i < 3) arrow(s, x + sw + 0.045, 2.24, 0.27, 0.2, AMBER);
  });
  s.addText("The same governed pipeline we verified: ingest → decide → propose → approve → audit. Every action leaves a replayable trace.", {
    x: M, y: 3.38, w: CW, h: 0.36, fontSize: 12.5, bold: true, color: PINE, fontFace: DISP, margin: 0,
  });
  // phone mock left
  phoneMock(s, M, 3.82, 2.35, 1.42);
  s.addText("SMS ON A BASIC PHONE · ACTION + DEADLINE + SOURCE", {
    x: M, y: 5.28, w: 2.5, h: 0.2, fontSize: 6.5, bold: true, color: MUTED, fontFace: MONO, margin: 0,
  });
  // demo behavior right
  s.addText("Demo behavior: given a hazard and a connectivity state, this farmer receives this prioritized action; the advisory still syncs when bandwidth returns.", {
    x: 3.2, y: 3.82, w: 4.3, h: 0.7, fontSize: 10.5, color: INK, fontFace: BODY, margin: 0, lineSpacing: 14,
  });
  chip(s, 3.2, 4.62, 5.2, 0.44, "IMD FEED SIMULATED · SMS VIA SIMULATOR · SEED RULES AWAITING AGRONOMIST REVIEW", {
    fill: AMBER_SOFT, line: "E0B488", color: "7A4A10", size: 7.5, align: "center",
  });
  pageNum(s, 5);
  s.addNotes("Mechanism slide mirrors the scaffold engine (ingest to audit) mounted on the agri domain. The offline queue and trace are already verified in the engine; the agri rules are the new layer.");
}

// ============ S6 PROTOTYPE ============
{
  const s = p.addSlide();
  s.background = { color: PAPER };
  cropRows(s, false);
  eyebrow(s, "The Prototype");
  title(s, "Verified today. Honest by design. Offline-capable.");
  hairline(s, 1.28);
  // hero stat
  s.addText("85 / 85", {
    x: M, y: 1.5, w: 3.0, h: 0.95, fontSize: 46, bold: true,
    color: PINE, fontFace: DISP, margin: 0, valign: "middle",
  });
  s.addText("ACCEPTANCE SUITES GREEN", {
    x: M, y: 2.5, w: 3.0, h: 0.26, fontSize: 9, bold: true, color: AMBER_TXT,
    fontFace: LABEL, charSpacing: 2, margin: 0,
  });
  s.addText("approval, trace, providers, multimodal, provenance, feeds, honesty, stress", {
    x: M, y: 2.78, w: 3.0, h: 0.55, fontSize: 9.5, color: MUTED, fontFace: BODY, margin: 0, lineSpacing: 12,
  });
  // right rows
  const rows = [
    ["46 / 46", "lane fixture scenarios verified, order-independent on fresh databases"],
    ["Zero-dep", "engine runs on stdlib only; demo never dies, offline fallback replay"],
    ["Honest mode", "badges count actual provider outcomes, no badge-lie, audit trail per action"],
  ];
  rows.forEach((r, i) => {
    const y = 1.5 + i * 0.83;
    s.addText(r[0], { x: 4.3, y: y, w: 1.35, h: 0.5, fontSize: 17, bold: true, color: PINE, fontFace: DISP, margin: 0 });
    s.addText(r[1], { x: 5.8, y: y + 0.04, w: 3.65, h: 0.55, fontSize: 9.5, color: MUTED, fontFace: BODY, margin: 0, lineSpacing: 12 });
    if (i < 2) hairline(s, y + 0.62, LINE, 4.3, 5.15);
  });
  // demo arc strip
  bar(s, M, 3.98, CW, 0.88, PINE_DARK);
  s.addText("3-MINUTE DEMO ARC", {
    x: 0.75, y: 4.1, w: 2.0, h: 0.24, fontSize: 8, bold: true, color: AMBER, fontFace: MONO, margin: 0,
  });
  s.addText("Asha's plot  →  cyclone forecast  →  staged Odia advisory  →  tower drops, advice still syncs  →  damage evidence  →  claim packet export", {
    x: 0.75, y: 4.36, w: 8.5, h: 0.42, fontSize: 10.5, color: CREAM, fontFace: BODY, margin: 0, lineSpacing: 13,
  });
  // honesty panel
  bar(s, M, 5.02, 0.055, 0.42, AMBER);
  bar(s, M + 0.055, 5.02, CW - 0.055, 0.42, AMBER_SOFT);
  s.addText("Prototype honesty: IMD feed is simulated, SMS and IVR run through simulators, agronomy rules are a curated seed set awaiting agronomist review. Nothing labeled live is not live.", {
    x: 0.78, y: 5.1, w: 8.4, h: 0.3, fontSize: 9, color: "5A3A10", fontFace: BODY, margin: 0,
  });
  pageNum(s, 6);
  s.addNotes("The deck claims only what the repo proves. Round 0 submission is PPT plus prototype; the demo carries the proof. The honesty strip is deliberate: faculty will probe.");
}

// ============ S7 MOAT ============
{
  const s = p.addSlide();
  s.background = { color: PAPER };
  cropRows(s, false);
  eyebrow(s, "The Moat");
  title(s, "Why this is not another alert system.");
  hairline(s, 1.28);
  // left: dull alert card
  bar(s, M, 1.5, 4.0, 2.2, PAPER2);
  s.addText("THE ALERT SAYS", {
    x: 0.78, y: 1.7, w: 3.6, h: 0.26, fontSize: 9, bold: true, color: MUTED,
    fontFace: LABEL, charSpacing: 2, margin: 0,
  });
  s.addText("Cyclone expected. Stay safe.", {
    x: 0.78, y: 2.06, w: 3.6, h: 0.5, fontSize: 16, italic: true, color: MUTED, fontFace: DISP, margin: 0,
  });
  s.addText("No crop, no stage, no deadline, no cost of waiting, no recovery step.", {
    x: 0.78, y: 2.72, w: 3.5, h: 0.6, fontSize: 10.5, color: "5E665B", fontFace: BODY, margin: 0, lineSpacing: 13.5,
  });
  // right: featured advisory card
  card(s, 4.72, 1.5, 4.73, 2.2, WHITE, PINE);
  bar(s, 4.72, 1.5, 4.73, 0.09, AMBER);
  s.addText("THE ADVISORY SAYS", {
    x: 4.95, y: 1.72, w: 4.3, h: 0.26, fontSize: 9, bold: true, color: PINE,
    fontFace: LABEL, charSpacing: 2, margin: 0,
  });
  s.addText("Plot 12B, flowering paddy: harvest by 18:00 tomorrow, or move to the raised platform. Source: IMD + rule 14. Cost of waiting: est. yield loss.", {
    x: 4.95, y: 2.08, w: 4.3, h: 1.0, fontSize: 13, color: INK, fontFace: DISP, margin: 0, lineSpacing: 17,
  });
  s.addText("Warnings are infrastructure. Decisions are the product.", {
    x: 4.95, y: 3.28, w: 4.3, h: 0.34, fontSize: 12.5, bold: true, color: AMBER_TXT, fontFace: DISP, margin: 0,
  });
  // VS badge
  s.addShape(p.ShapeType.ellipse, {
    x: 4.3, y: 2.24, w: 0.62, h: 0.62, fill: { color: AMBER }, line: { color: AMBER, width: 0 },
  });
  s.addText("VS", {
    x: 4.3, y: 2.36, w: 0.62, h: 0.38, fontSize: 13, bold: true, color: CREAM,
    fontFace: LABEL, align: "center", margin: 0,
  });
  // prior art table
  s.addText("PRIOR ART", {
    x: M, y: 3.92, w: 1.6, h: 0.24, fontSize: 8.5, bold: true, color: AMBER_TXT,
    fontFace: MONO, margin: 0,
  });
  const prior = [
    ["Meghdoot (IMD)", "alerts and agromet advisories", "no farm profile, no staged action, no claims path"],
    ["Fasal, DeHaat", "marketplace and credit rails", "advisory is content, not a governed decision"],
    ["Bangladesh CPP", "human volunteer warning chain", "no recovery plan, no claim evidence"],
    ["WFP anticipatory cash", "threshold-triggered cash transfers", "cash, not farm action; no crop-stage logic"],
  ];
  prior.forEach((row, i) => {
    const y = 4.2 + i * 0.32;
    s.addText(row[0], { x: M, y: y, w: 2.05, h: 0.26, fontSize: 10, bold: true, color: INK, fontFace: LABEL, margin: 0 });
    s.addText(row[1], { x: 2.7, y: y, w: 3.1, h: 0.26, fontSize: 9.5, color: MUTED, fontFace: BODY, margin: 0 });
    s.addText(row[2], { x: 5.9, y: y, w: 3.55, h: 0.26, fontSize: 9.5, italic: true, color: MUTED, fontFace: BODY, margin: 0 });
    if (i < 3) hairline(s, y + 0.305, LINE, M, CW);
  });
  footerNote(s, "Prior art from the statement-faithful research wave: research/raw/v2/cnc-channel-ps07-ultra8x-v2.content.md");
  pageNum(s, 7);
  s.addNotes("One contrast, one sentence. The moat is the governed decision: action, deadline, source, cost of waiting, trace. Prior art rows are mine-verified, not marketing.");
}

// ============ S8 BUYERS ============
{
  const s = p.addSlide();
  s.background = { color: PAPER };
  cropRows(s, false);
  eyebrow(s, "The Model");
  title(s, "Three buyers, one verified loop.");
  hairline(s, 1.28);
  // featured FPO card
  card(s, M, 1.45, CW, 1.42, WHITE, PINE);
  bar(s, M, 1.45, 0.055, 1.42, AMBER);
  s.addText("FPO + EXTENSION", {
    x: 0.8, y: 1.62, w: 3.2, h: 0.34, fontSize: 14, bold: true, color: PINE,
    fontFace: LABEL, charSpacing: 1, margin: 0,
  });
  s.addText("seasonal advisory subscriptions per farmer via FPOs and KVK extension workers", {
    x: 0.8, y: 2.02, w: 4.8, h: 0.55, fontSize: 10.5, color: INK, fontFace: BODY, margin: 0, lineSpacing: 13.5,
  });
  chip(s, 6.3, 1.85, 2.95, 0.5, "PAY PER VERIFIED ADVISORY DELIVERED AND ACTED ON", {
    fill: PAPER2, line: "D8D2C4", color: PINE, size: 8,
  });
  // two secondary cards
  const secs = [
    ["B2G DISTRICT", "Odisha agriculture department and OSDMA, per-block deployment", "REDUCES CALL VOLUME · AUDITABLE OUTREACH EVIDENCE"],
    ["CLAIMS RAIL", "PMFBY insurers and aggregators pay per evidence packet", "VERIFIED OBSERVATION CONVERTS TO CLAIM · BOTH SIDES WIN"],
  ];
  secs.forEach((sc, i) => {
    const x = M + i * 4.55;
    card(s, x, 3.05, 4.35, 1.35, WHITE);
    s.addText(sc[0], {
      x: x + 0.2, y: 3.22, w: 3.95, h: 0.3, fontSize: 11.5, bold: true,
      color: PINE, fontFace: LABEL, charSpacing: 1, margin: 0,
    });
    s.addText(sc[1], {
      x: x + 0.2, y: 3.56, w: 3.95, h: 0.4, fontSize: 9.5, color: INK, fontFace: BODY, margin: 0, lineSpacing: 12,
    });
    s.addText(sc[2], {
      x: x + 0.2, y: 4.02, w: 3.95, h: 0.22, fontSize: 7, bold: true, color: "8A8477", fontFace: MONO, margin: 0,
    });
  });
  s.addText("Seed revenue line for Round 1: one FPO, one season, measured renewal. No consumer subscription fantasy.", {
    x: M, y: 4.62, w: CW, h: 0.34, fontSize: 12.5, bold: true, color: PINE, fontFace: DISP, margin: 0,
  });
  footerNote(s, "Mine verdict: the real buyer is institutional, the real distribution is extension workers, KCC, FPOs, dealers, panchayat actors.");
  pageNum(s, 8);
  s.addNotes("Mine-faithful: institutional buyer, assisted distribution. Three lines only, per YC rule. The claims rail is the wedge because PMFBY already pays for verified loss events.");
}

// ============ S9 MARKET ============
{
  const s = p.addSlide();
  s.background = { color: PAPER };
  cropRows(s, false);
  eyebrow(s, "The Market");
  title(s, "One rail, one pilot, one quarter.");
  hairline(s, 1.28);
  // left: rail panel
  card(s, M, 1.45, 4.35, 2.62, WHITE);
  s.addText("THE RAIL EXISTS", {
    x: 0.78, y: 1.62, w: 3.9, h: 0.28, fontSize: 9.5, bold: true, color: AMBER_TXT,
    fontFace: LABEL, charSpacing: 2, margin: 0,
  });
  s.addText("78.4 crore", {
    x: 0.78, y: 1.92, w: 3.9, h: 0.62, fontSize: 28, bold: true, color: PINE, fontFace: DISP, margin: 0,
  });
  s.addText("PMFBY applications · Rs 1.83 lakh crore program", {
    x: 0.78, y: 2.56, w: 3.9, h: 0.3, fontSize: 10.5, color: INK, fontFace: BODY, margin: 0,
  });
  const rail = [
    "Rs 2,817 crore Digital Agriculture Mission funds agri-digital public infrastructure",
    "Odisha: cyclone-facing coast, paddy and saline zones, Dana and Yaas damage on record",
  ];
  rail.forEach((r, i) => {
    const y = 2.92 + i * 0.52;
    s.addText("→", { x: 0.78, y: y, w: 0.3, h: 0.26, fontSize: 11, bold: true, color: AMBER_TXT, fontFace: LABEL, margin: 0 });
    s.addText(r, { x: 1.12, y: y, w: 3.55, h: 0.5, fontSize: 9.5, color: MUTED, fontFace: BODY, margin: 0, lineSpacing: 12 });
  });
  // right: pilot panel (dark)
  bar(s, 5.15, 1.45, 4.35, 2.62, PINE_DARK);
  s.addText("THE PILOT", {
    x: 5.38, y: 1.62, w: 3.9, h: 0.28, fontSize: 9.5, bold: true, color: AMBER,
    fontFace: LABEL, charSpacing: 2, margin: 0,
  });
  const pilot = [
    "one coastal block with extension-worker access",
    "one agronomist-reviewed rule pack",
    "measure comprehension and claim conversion, not downloads",
  ];
  pilot.forEach((ln, i) => {
    s.addShape(p.ShapeType.ellipse, {
      x: 5.38, y: 2.05 + i * 0.55, w: 0.32, h: 0.32, fill: { color: AMBER }, line: { color: AMBER, width: 0 },
    });
    s.addText(String(i + 1), {
      x: 5.38, y: 2.1 + i * 0.55, w: 0.32, h: 0.24, fontSize: 10, bold: true,
      color: PINE_DARK, fontFace: LABEL, align: "center", margin: 0,
    });
    s.addText(ln, { x: 5.82, y: 2.03 + i * 0.55, w: 3.5, h: 0.42, fontSize: 10, color: CREAM, fontFace: BODY, margin: 0, lineSpacing: 12.5 });
  });
  s.addText("NAMED RAIL · NAMED PILOT · DATED OUTCOME", {
    x: 5.38, y: 3.72, w: 3.9, h: 0.24, fontSize: 7.5, bold: true, color: MOSS, fontFace: MONO, margin: 0,
  });
  // quarter bar
  s.addText("Named rail, named pilot, dated outcome. That is the Round 1 contract.", {
    x: M, y: 4.3, w: CW, h: 0.4, fontSize: 14.5, bold: true, color: PINE, fontFace: DISP, margin: 0,
  });
  s.addText("Sources: PMFBY program data; Digital Agriculture Mission allocation; YSD Dana assessment; Down To Earth Yaas report. All dated 2024-2025, verified in the research wave.", {
    x: M, y: 4.78, w: CW, h: 0.28, fontSize: 9, italic: true, color: MUTED, fontFace: BODY, margin: 0,
  });
  pageNum(s, 9);
  s.addNotes("One rail, one pilot, one quarter. Round 1 deepens exactly this: real feed connector, Odia voice, comprehension tests, agronomist review.");
}

// ============ S10 TEAM ============
{
  const s = p.addSlide();
  s.background = { color: PAPER };
  eyebrow(s, "The Team");
  title(s, "Team 511.");
  hairline(s, 1.28);
  const team = [
    ["H", "Harsh Gounder", "Lead · E&CE", "systems, research method, 17-statement evidence wave"],
    ["A", "Ayush Kharwar", "Engine and demo", "zero-dep engine, demo.sh, seed data"],
    ["S", "Sujal Shukla", "Deck and submission", "submission text, paste at gates, backup demo runner"],
  ];
  const tw = 2.62, tg = 0.34;
  team.forEach((tm, i) => {
    const x = M + i * (tw + tg);
    const feat = i === 0;
    card(s, x, 1.5, tw, 2.35, WHITE, feat ? PINE : LINE);
    s.addShape(p.ShapeType.ellipse, {
      x: x + (tw - 0.78) / 2, y: 1.78, w: 0.78, h: 0.78,
      fill: { color: feat ? PINE : "8FAE8B" }, line: { color: feat ? PINE : "8FAE8B", width: 0 },
    });
    s.addText(tm[0], {
      x: x + (tw - 0.78) / 2, y: 1.88, w: 0.78, h: 0.58, fontSize: 24, bold: true,
      color: CREAM, fontFace: DISP, align: "center", margin: 0,
    });
    s.addText(tm[1], { x: x + 0.15, y: 2.78, w: tw - 0.3, h: 0.36, fontSize: 13.5, bold: true, color: INK, fontFace: DISP, align: "center", margin: 0 });
    s.addText(tm[2], { x: x + 0.15, y: 3.16, w: tw - 0.3, h: 0.26, fontSize: 9.5, bold: true, color: AMBER_TXT, fontFace: LABEL, align: "center", margin: 0 });
    s.addText(tm[3], { x: x + 0.2, y: 3.46, w: tw - 0.4, h: 0.35, fontSize: 8.5, italic: true, color: MUTED, fontFace: BODY, align: "center", margin: 0 });
  });
  // shipped band
  bar(s, M, 4.12, CW, 0.78, PINE_DARK);
  s.addText("ALREADY SHIPPED:", {
    x: 0.78, y: 4.28, w: 2.1, h: 0.24, fontSize: 8.5, bold: true, color: AMBER, fontFace: MONO, margin: 0,
  });
  s.addText("a verified governed pipeline (85/85 suites), honest outcome badges, and a statement-faithful research method with every claim sourced.", {
    x: 2.9, y: 4.24, w: 6.3, h: 0.55, fontSize: 10.5, color: CREAM, fontFace: BODY, margin: 0, lineSpacing: 13.5,
  });
  footerNote(s, "E&CE research profile matches the statement core: sensors, communications, ML, power resilience.");
  pageNum(s, 10);
  s.addNotes("Founder-focused: what we shipped is the proof, not the bios. The E&CE note is for faculty: this statement is the only one spanning CSE, ECE, and EE clusters (W3).");
}

// ============ S11 CLOSE (dark) ============
{
  const s = p.addSlide();
  s.background = { color: PINE_DARK };
  arcs(s);
  cropRows(s, true);
  s.addText("CRAFT N CODE 2026  ·  ROUND 0  ·  TEAM 511", {
    x: M, y: 0.42, w: CW, h: 0.28, fontSize: 9.5, bold: true,
    color: MOSS, fontFace: LABEL, charSpacing: 3, margin: 0,
  });
  s.addText([
    { text: "Grade our decision quality", options: { color: CREAM } },
    { text: ".", options: { color: AMBER } },
  ], {
    x: M, y: 1.3, w: 8.4, h: 0.85, fontSize: 36, bold: true, fontFace: DISP, margin: 0,
  });
  s.addText("Why this action, why now, why this channel. That is the product, and your questions shape Round 1.", {
    x: M, y: 2.22, w: 7.0, h: 0.4, fontSize: 14, color: MOSS, fontFace: BODY, margin: 0,
  });
  // limitation panel
  bar(s, M, 2.85, CW, 1.32, "1F3A28");
  s.addText("ONE LIMITATION, STATED OPENLY", {
    x: 0.78, y: 3.0, w: 3.4, h: 0.24, fontSize: 8.5, bold: true, color: AMBER, fontFace: MONO, margin: 0,
  });
  s.addText("The rule set is a curated seed awaiting agronomist review; the IMD feed and telecom delivery are simulated in this prototype, and nothing is sent over live SMS or WhatsApp. Every claim in this deck has a dated source on the repo.", {
    x: 0.78, y: 3.28, w: 8.1, h: 0.78, fontSize: 11, color: CREAM, fontFace: BODY, margin: 0, lineSpacing: 14.5,
  });
  // bottom strip
  s.addText("LIVE DEMO: 3 MIN   ·   REPO: GITHUB.COM/HARSHGOUNDER/CRAFT-N-CODE   ·   TEAM 511", {
    x: M, y: 4.75, w: CW, h: 0.3, fontSize: 9.5, bold: true, color: AMBER, fontFace: MONO, margin: 0,
  });
  s.addNotes("Ask tied to the next milestone: faculty feedback contract. Slide 8 of the runbook said the same: feedback shapes Round 1. The limitation is the honesty move faculty will remember.");
}

p.writeFile({ fileName: "KrishiSetu-Round0-20260816.pptx" }).then(() => console.log("DECK WRITTEN"));
