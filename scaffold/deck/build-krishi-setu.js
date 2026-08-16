// KrishiSetu Round 0 deck (PS-07), Craft N Code 2026, Team 511
// Build: node build-krishi-setu.js  ->  KrishiSetu-Round0-20260816.pptx
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_16x9"; // 10 x 5.625 in

// palette: Forest & Moss
const FOREST = "2C5F2D";
const FOREST_DARK = "1F3D26";
const MOSS = "97BC62";
const PALE = "F0F5EA";
const PALE2 = "D8E8C8";
const CREAM = "F5F7F2";
const INK = "212121";
const MUTED = "5A6B5A";

const M = 0.5; // margin
const W = 10;
const H = 5.625;
const CW = (W - 2 * M - 2 * 0.35) / 3; // card width for 3-up rows

function header(s, text) {
  s.addText(text, { x: M, y: 0.32, w: W - 2 * M, h: 0.55, fontSize: 28, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
}

function card(s, x, y, w, h, fill) {
  return s.addShape(p.ShapeType.roundRect, { x, y, w, h, fill: { color: fill }, rectRadius: 0.08, line: { color: "FFFFFF", width: 0 } });
}

function footer(s, text, y) {
  s.addText(text, { x: M, y: y || H - 0.42, w: W - 2 * M, h: 0.3, fontSize: 9, color: MUTED, fontFace: "Calibri", margin: 0 });
}

// ---------- S1 TITLE (dark) ----------
let s = p.addSlide();
s.background = { color: FOREST_DARK };
s.addText("KrishiSetu", { x: 1, y: 1.0, w: 8, h: 0.9, fontSize: 52, bold: true, color: CREAM, fontFace: "Cambria", align: "center", margin: 0 });
s.addText("Cyclone and Flood Resilient Smart Agriculture Advisory", { x: 1, y: 2.0, w: 8, h: 0.4, fontSize: 17, color: MOSS, fontFace: "Cambria", align: "center", margin: 0 });
s.addText("For coastal Odisha farmers, KrishiSetu turns a cyclone forecast into a crop-stage-specific action and an insurance claim packet, in Odia, on a basic phone.", { x: 1.2, y: 2.7, w: 7.6, h: 0.9, fontSize: 14, color: CREAM, fontFace: "Calibri", align: "center", margin: 0 });
s.addText("Team 511  |  Craft N Code 2026  |  Round 0", { x: 1, y: 4.6, w: 8, h: 0.35, fontSize: 12, color: MOSS, fontFace: "Calibri", align: "center", margin: 0 });
s.addNotes("Working name KrishiSetu (farm bridge), swappable. Round 0: prototype + deck, judged by IIIT-B faculty. One-liner states the promise: forecast becomes action plus claim packet, Odia, basic phone.");

// ---------- S2 PROBLEM ----------
s = p.addSlide();
s.background = { color: "FFFFFF" };
header(s, "The problem: warnings arrive, decisions do not");
card(s, M, 1.05, 9, 1.1, PALE);
s.addText("Asha, 47, flowering paddy on a low-lying plot in Balasore district. Post-Yaas field reporting documents saltwater on 5,882 hectares of cultivable land across five blocks. The alert came. The action did not.", { x: 0.7, y: 1.18, w: 8.6, h: 0.85, fontSize: 14.5, italic: true, color: INK, fontFace: "Calibri", margin: 0 });
const stats = [
  ["5,428 acres", "crop loss across 4 blocks of Kendrapada and Bhadrak, Cyclone Dana 2024 (rapid assessment)"],
  ["5,882 ha", "cultivable land salt-affected across 5 Balasore blocks, Cyclone Yaas 2021 (Down To Earth)"],
  ["78.4 crore", "PMFBY crop-insurance applications on a Rs 1.83 lakh crore program"],
];
stats.forEach((st, i) => {
  const x = M + i * (CW + 0.35);
  card(s, x, 2.45, CW, 1.6, "F7FAF2");
  s.addText(st[0], { x: x + 0.15, y: 2.62, w: CW - 0.3, h: 0.6, fontSize: 26, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
  s.addText(st[1], { x: x + 0.15, y: 3.3, w: CW - 0.3, h: 0.65, fontSize: 10.5, color: MUTED, fontFace: "Calibri", margin: 0 });
});
s.addText("Farmers get warnings. They do not get decisions.", { x: M, y: 4.35, w: 9, h: 0.45, fontSize: 16, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
footer(s, "Sources: YSD Odisha Cyclone Dana rapid assessment (2025); Down To Earth, post-Yaas Kharif report; PMFBY program data. Numbers verified in research wave, dated 2024-2025.");
s.addNotes("One problem, one cost. Asha is a composite persona grounded in post-Yaas Balasore field reporting, not a named individual. PMFBY numbers show the insurance rail already exists and is huge: the gap is verified observation, not scheme design.");

// ---------- S2B RESEARCH MACHINE (the depth proof) ----------
{
  const s = p.addSlide();
  s.background = { color: "FFFFFF" };
  const HDR = 0.35;
  s.addText("The research machine behind this deck", { x: M, y: HDR, w: 9, h: 0.6, fontSize: 30, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
  const cards = [
    ["48", "parallel deep-research runs, 7 waves, every run multi-channel with coverage tables, noise logs, A-D evidence grades"],
    ["2.5M+", "chars of raw evidence: named, dated sources on every claim, nothing unverified ships"],
    ["4,000+", "cited sources across 6 continents: cyclone/food/agri ledgers, cascade math, human wisdom, frontier science"],
    ["A-D", "evidence grading on every claim: ODISHA-MEASURED, TRANSFER-PRIOR, SCENARIO-ASSUMPTION, UNKNOWN badges"],
  ];
  cards.forEach((c, i) => {
    const x = M + (i % 2) * 4.55;
    const y = 1.15 + Math.floor(i / 2) * 1.35;
    card(s, x, y, 4.45, 1.2, PALE2);
    s.addText(c[0], { x: x + 0.15, y: y + 0.1, w: 1.5, h: 0.5, fontSize: 26, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
    s.addText(c[1], { x: x + 1.7, y: y + 0.1, w: 2.65, h: 1.0, fontSize: 9.5, color: INK, fontFace: "Calibri", margin: 0 });
  });
  s.addText("single-pass AI summarizes. this is an orchestrated parallel research machine with verification gates: every number in this deck traces to a source you can open.", { x: M, y: 4.15, w: 9, h: 0.75, fontSize: 13, bold: true, color: FOREST, fontFace: "Calibri", margin: 0 });
  footer(s, "Evidence chain: slide -> proof ledger -> EVIDENCE-INDEX.md -> raw report -> named dated source. Nothing ships without the chain.", 5.1);
  s.addNotes("This slide is the holy-shit moment: 48 runs, 7 waves, 2.5M chars, 4,000+ sources, A-D grades. Judges who ask 'where is this from' get a path. Never claim we read everything without this map to prove it.");
}

// ---------- S3 SOLUTION ----------
s = p.addSlide();
s.background = { color: "FFFFFF" };
header(s, "The solution: an advisory engine, not an alert system");
s.addText("Every forecast becomes a decision: an action, a deadline, a source, and a fallback, in Odia, on any phone.", { x: M, y: 1.0, w: 9, h: 0.6, fontSize: 16, bold: true, color: INK, fontFace: "Cambria", margin: 0 });
const phases = [
  ["BEFORE", "stage the crop", "harvest or move to raised platform on a deadline", "protect seed, livestock, equipment", "evacuate people, secure the house"],
  ["DURING", "shelter and safety", "Odia guidance for the household", "livestock and fodder checklist", "keep the advisory reachable offline"],
  ["AFTER", "recovery and claims", "saline flush and re-sowing plan per plot", "damage evidence capture on a basic phone", "PMFBY claim packet export"],
];
phases.forEach((ph, i) => {
  const x = M + i * (CW + 0.35);
  card(s, x, 1.75, CW, 2.6, PALE);
  s.addShape(p.ShapeType.ellipse, { x: x + 0.15, y: 1.95, w: 0.42, h: 0.42, fill: { color: MOSS } });
  s.addText(String(i + 1), { x: x + 0.15, y: 2.0, w: 0.42, h: 0.32, fontSize: 14, bold: true, color: "FFFFFF", fontFace: "Calibri", align: "center", margin: 0 });
  s.addText(ph[0], { x: x + 0.68, y: 1.98, w: CW - 0.8, h: 0.35, fontSize: 15, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
  s.addText(ph.slice(1).map((t, idx) => (idx === 0 ? t.toUpperCase() : t)).join("\n"), { x: x + 0.2, y: 2.55, w: CW - 0.4, h: 1.65, fontSize: 11, color: INK, fontFace: "Calibri", lineSpacing: 22, margin: 0, breakLine: false });
});
s.addText("Honest framing: the advisory engine is the hero. Acknowledgement and report capture are adaptation features inside it, not the pitch.", { x: M, y: 4.5, w: 9, h: 0.4, fontSize: 10.5, italic: true, color: MUTED, fontFace: "Calibri", margin: 0 });
footer(s, "Statement-faithful: the official problem is a resilient advisory system for cyclone and flood contexts, with farm-profile-aware, staged actions.", 5.28);
s.addNotes("This is the user-corrected framing: the topic is an advisory platform, not an alert platform. Every action card carries a deadline and a source in the product; the deck keeps that promise on the mechanism slide.");

// ---------- S4 MECHANISM ----------
s = p.addSlide();
s.background = { color: "FFFFFF" };
header(s, "Mechanism: ingest, decide, deliver, recover");
const steps = [
  ["1", "INGEST", "IMD forecast plus farm profile: crop, stage, plot, soil, connectivity state", "one inbox, local, no external runtime deps"],
  ["2", "DECIDE", "agronomist-reviewed rule engine: pre/during/post x crop x stage x hazard", "every proposal carries deadline, source, cost of waiting"],
  ["3", "DELIVER", "Odia SMS and IVR, offline queue, ack and report capture", "works when the tower drops; syncs when it returns"],
  ["4", "RECOVER", "post-inundation recovery chain and claims evidence packet", "verified observation becomes an insurance claim"],
];
const SW = (W - 2 * M - 3 * 0.25) / 4;
steps.forEach((st, i) => {
  const x = M + i * (SW + 0.25);
  card(s, x, 1.25, SW, 2.85, PALE);
  s.addShape(p.ShapeType.ellipse, { x: x + (SW - 0.6) / 2, y: 1.45, w: 0.6, h: 0.6, fill: { color: FOREST } });
  s.addText(st[0], { x: x + (SW - 0.6) / 2, y: 1.52, w: 0.6, h: 0.45, fontSize: 18, bold: true, color: CREAM, fontFace: "Cambria", align: "center", margin: 0 });
  s.addText(st[1], { x: x + 0.1, y: 2.2, w: SW - 0.2, h: 0.35, fontSize: 14, bold: true, color: FOREST, fontFace: "Cambria", align: "center", margin: 0 });
  s.addText(st[2], { x: x + 0.15, y: 2.6, w: SW - 0.3, h: 0.85, fontSize: 10.5, color: INK, fontFace: "Calibri", align: "center", margin: 0 });
  s.addText(st[3], { x: x + 0.15, y: 3.5, w: SW - 0.3, h: 0.5, fontSize: 9.5, italic: true, color: MUTED, fontFace: "Calibri", align: "center", margin: 0 });
  if (i < 3) s.addText(">", { x: x + SW + 0.02, y: 2.3, w: 0.22, h: 0.5, fontSize: 20, bold: true, color: MOSS, fontFace: "Calibri", align: "center", margin: 0 });
});
s.addText("The same governed pipeline we verified: ingest, decide, propose, approve, audit. Every action leaves a replayable trace.", { x: M, y: 4.35, w: 9, h: 0.45, fontSize: 13.5, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
footer(s, "Demo behavior: given a hazard and a connectivity state, this farmer receives this prioritized action, and the advisory still syncs when bandwidth returns (W3 demo prescription).");
s.addNotes("Mechanism slide mirrors the scaffold engine (ingest to audit) mounted on the agri domain. The offline queue and trace are already verified in the engine; the agri rules are the new layer.");

// ---------- S5 PROTOTYPE + PROOF ----------
s = p.addSlide();
s.background = { color: "FFFFFF" };
header(s, "Prototype today: verified, honest, offline-capable");
const proof = [
  ["85 / 85", "acceptance suites green across approval, trace, providers, multimodal, provenance, feeds, honesty, stress"],
  ["46 / 46", "lane fixture scenarios verified, order-independent on fresh databases"],
  ["Zero-dep", "engine runs on stdlib only; demo never dies, offline fallback replay"],
  ["Honest mode", "badges count actual provider outcomes, no badge-lie, audit trail per action"],
];
proof.forEach((pr, i) => {
  const x = M + (i % 2) * (4.45 + 0.1);
  const y = 1.15 + Math.floor(i / 2) * 1.15;
  card(s, x, y, 4.45, 1.0, "F7FAF2");
  s.addText(pr[0], { x: x + 0.15, y: y + 0.12, w: 1.9, h: 0.5, fontSize: 18, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
  s.addText(pr[1], { x: x + 2.05, y: y + 0.12, w: 2.3, h: 0.8, fontSize: 9.5, color: MUTED, fontFace: "Calibri", margin: 0 });
});
s.addText("Demo arc (3 minutes): Asha's plot -> cyclone forecast -> staged Odia advisory -> tower drops, advice still syncs -> damage evidence -> claim packet export.", { x: 5.45, y: 3.6, w: 4.0, h: 0.9, fontSize: 11.5, color: INK, fontFace: "Calibri", margin: 0 });
card(s, M, 4.35, 9, 0.72, PALE2);
s.addText("Prototype honesty: IMD feed is simulated, SMS and IVR run through simulators, agronomy rules are a curated seed set awaiting agronomist review. Nothing is labeled live that is not live.", { x: 0.7, y: 4.44, w: 8.6, h: 0.55, fontSize: 10.5, color: INK, fontFace: "Calibri", margin: 0 });
footer(s, "Verification: fresh runs 2026-08-16 07:40 IST, scaffold eval report on repo. 46/46 eval report is engine-level; agri domain rules are the new layer for Round 1.", 5.28);
s.addNotes("The deck claims only what the repo proves. Round 0 submission is PPT plus prototype; the demo carries the proof. The honesty strip is deliberate: faculty will probe.");

// ---------- S6 MOAT ----------
s = p.addSlide();
s.background = { color: "FFFFFF" };
header(s, "Why this is not another alert system");
card(s, M, 1.05, 4.35, 1.85, PALE);
s.addText("The alert says", { x: 0.7, y: 1.2, w: 4.0, h: 0.35, fontSize: 12, bold: true, color: MUTED, fontFace: "Calibri", margin: 0 });
s.addText("\"Cyclone expected. Stay safe.\"", { x: 0.7, y: 1.6, w: 4.0, h: 0.5, fontSize: 17, italic: true, color: INK, fontFace: "Cambria", margin: 0 });
s.addText("No crop, no stage, no deadline, no cost of waiting, no recovery step.", { x: 0.7, y: 2.2, w: 4.0, h: 0.55, fontSize: 11, color: MUTED, fontFace: "Calibri", margin: 0 });
card(s, 5.15, 1.05, 4.35, 1.85, PALE);
s.addText("The advisory says", { x: 5.35, y: 1.2, w: 4.0, h: 0.35, fontSize: 12, bold: true, color: FOREST, fontFace: "Calibri", margin: 0 });
s.addText("\"Plot 12B, flowering paddy: harvest by 18:00 tomorrow, or move to the raised platform. Source: IMD + rule 14. Cost of waiting: est. yield loss.\"", { x: 5.35, y: 1.6, w: 4.0, h: 1.1, fontSize: 13.5, color: INK, fontFace: "Cambria", margin: 0 });
const prior = [
  ["Meghdoot (IMD)", "alerts and agromet advisories", "no farm profile, no staged action, no claims path"],
  ["Fasal, DeHaat", "marketplace and credit rails", "advisory is content, not a governed decision"],
  ["Bangladesh CPP", "human volunteer warning chain", "no recovery plan, no claim evidence"],
  ["WFP anticipatory cash", "threshold-triggered cash transfers", "cash, not farm action; no crop-stage logic"],
];
let ty = 3.15;
s.addText("Prior art", { x: M, y: 3.05, w: 2, h: 0.3, fontSize: 12, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
prior.forEach((row) => {
  s.addText(row[0], { x: M, y: ty, w: 2.1, h: 0.32, fontSize: 10.5, bold: true, color: INK, fontFace: "Calibri", margin: 0 });
  s.addText(row[1], { x: 2.7, y: ty, w: 3.2, h: 0.32, fontSize: 10.5, color: MUTED, fontFace: "Calibri", margin: 0 });
  s.addText(row[2], { x: 6.0, y: ty, w: 3.5, h: 0.32, fontSize: 10.5, color: MUTED, fontFace: "Calibri", margin: 0 });
  ty += 0.4;
});
s.addText("Warnings are infrastructure. Decisions are the product.", { x: M, y: 4.82, w: 9, h: 0.4, fontSize: 15, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
footer(s, "Prior art from the statement-faithful research wave: channel evidence in research/raw/v2/cnc-channel-ps07-ultra8x-v2.content.md.", 5.32);
s.addNotes("One contrast, one sentence. The moat is the governed decision: action, deadline, source, cost of waiting, trace. Prior art rows are mine-verified, not marketing.");

// ---------- S7 BUSINESS MODEL ----------
s = p.addSlide();
s.background = { color: "FFFFFF" };
header(s, "Three buyers, one verified loop");
const models = [
  ["FPO + extension", "seasonal advisory subscriptions per farmer via FPOs and KVK extension workers", "pay per verified advisory delivered and acted on"],
  ["B2G district", "Odisha agriculture department and OSDMA, per-block deployment", "reduces call volume, gives auditable outreach evidence"],
  ["Claims rail", "PMFBY insurers and aggregators pay per evidence packet", "verified observation converts to claim, both sides win"],
];
models.forEach((md, i) => {
  const x = M + i * (CW + 0.35);
  card(s, x, 1.35, CW, 2.5, PALE);
  s.addText(md[0], { x: x + 0.2, y: 1.55, w: CW - 0.4, h: 0.4, fontSize: 16, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
  s.addText(md[1], { x: x + 0.2, y: 2.1, w: CW - 0.4, h: 1.0, fontSize: 11.5, color: INK, fontFace: "Calibri", margin: 0 });
  s.addText(md[2], { x: x + 0.2, y: 3.25, w: CW - 0.4, h: 0.5, fontSize: 10, italic: true, color: MUTED, fontFace: "Calibri", margin: 0 });
});
s.addText("Seed revenue line for Round 1: one FPO, one season, measured renewal. No consumer subscription fantasy.", { x: M, y: 4.35, w: 9, h: 0.45, fontSize: 13, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
footer(s, "Mine verdict: the real buyer is institutional, and the real distribution is extension workers, KCC, FPOs, dealers, and panchayat actors. Consumer subscriptions and network effects are not evidenced.");
s.addNotes("Mine-faithful: institutional buyer, assisted distribution. Three lines only, per YC rule. The claims rail is the wedge because PMFBY already pays for verified loss events.");

// ---------- S8 MARKET ----------
s = p.addSlide();
s.background = { color: "FFFFFF" };
header(s, "One rail, one pilot, one quarter");
card(s, M, 1.15, 4.35, 2.3, PALE);
s.addText("The rail exists", { x: 0.7, y: 1.3, w: 4.0, h: 0.35, fontSize: 13, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
s.addText("78.4 crore PMFBY applications, Rs 1.83 lakh crore program", { x: 0.7, y: 1.7, w: 4.0, h: 0.6, fontSize: 15, bold: true, color: INK, fontFace: "Cambria", margin: 0 });
s.addText("Digital Agriculture Mission, Rs 2,817 crore, funds agri-digital public infrastructure", { x: 0.7, y: 2.4, w: 4.0, h: 0.6, fontSize: 12.5, color: INK, fontFace: "Cambria", margin: 0 });
s.addText("Odisha: cyclone-facing coast, paddy and saline zones, Dana and Yaas damage on record", { x: 0.7, y: 3.05, w: 4.0, h: 0.6, fontSize: 12.5, color: INK, fontFace: "Cambria", margin: 0 });
card(s, 5.15, 1.15, 4.35, 2.3, PALE);
s.addText("The pilot", { x: 5.35, y: 1.3, w: 4.0, h: 0.35, fontSize: 13, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
const pilot = ["one coastal block with extension-worker access", "one agronomist-reviewed rule pack", "measure comprehension and claim conversion, not downloads"];
pilot.forEach((ln, i) => {
  s.addText(String(i + 1) + ".  " + ln, { x: 5.35, y: 1.75 + i * 0.55, w: 4.0, h: 0.5, fontSize: 12, color: INK, fontFace: "Calibri", margin: 0 });
});
s.addText("Named rail, named pilot, dated outcome. That is the Round 1 contract.", { x: M, y: 3.75, w: 9, h: 0.45, fontSize: 14.5, bold: true, color: FOREST, fontFace: "Cambria", margin: 0 });
s.addText("Sources: PMFBY program data; Digital Agriculture Mission allocation; YSD Dana assessment; Down To Earth Yaas report. All dated 2024-2025, verified in the research wave.", { x: M, y: 4.35, w: 9, h: 0.4, fontSize: 10, italic: true, color: MUTED, fontFace: "Calibri", margin: 0 });
footer(s, "Market slide after traction in YC ordering. No TAM multiplication, no 'everyone everywhere' line.", 5.28);
s.addNotes("One rail, one pilot, one quarter. Round 1 deepens exactly this: real feed connector, Odia voice, comprehension tests, agronomist review.");

// ---------- S9 TEAM ----------
s = p.addSlide();
s.background = { color: "FFFFFF" };
header(s, "Team 511");
const team = [
  ["Harsh Gounder", "Lead, E&CE", "systems, research method, 17-statement evidence wave"],
  ["Ayush Kharwar", "Engine and demo", "zero-dep engine, demo.sh, seed data"],
  ["Sujal Shukla", "Deck and submission", "submission text, paste at gates, backup demo runner"],
];
team.forEach((tm, i) => {
  const x = M + i * (CW + 0.35);
  card(s, x, 1.2, CW, 2.0, PALE);
  s.addShape(p.ShapeType.ellipse, { x: x + (CW - 0.7) / 2, y: 1.4, w: 0.7, h: 0.7, fill: { color: MOSS } });
  s.addText(String(i + 1), { x: x + (CW - 0.7) / 2, y: 1.48, w: 0.7, h: 0.5, fontSize: 20, bold: true, color: "FFFFFF", fontFace: "Cambria", align: "center", margin: 0 });
  s.addText(tm[0], { x: x + 0.15, y: 2.25, w: CW - 0.3, h: 0.4, fontSize: 15, bold: true, color: FOREST, fontFace: "Cambria", align: "center", margin: 0 });
  s.addText(tm[1], { x: x + 0.15, y: 2.65, w: CW - 0.3, h: 0.3, fontSize: 11.5, color: MUTED, fontFace: "Calibri", align: "center", margin: 0 });
  s.addText(tm[2], { x: x + 0.15, y: 2.95, w: CW - 0.3, h: 0.35, fontSize: 9.5, italic: true, color: MUTED, fontFace: "Calibri", align: "center", margin: 0 });
});
s.addText("Already shipped: a verified governed pipeline (85/85 suites), honest outcome badges, and a statement-faithful research method with every claim sourced.", { x: M, y: 3.7, w: 9, h: 0.5, fontSize: 13, bold: true, color: INK, fontFace: "Cambria", margin: 0 });
footer(s, "E&CE research profile matches the statement core: sensors, communications, ML, power resilience.", 5.28);
s.addNotes("Founder-focused: what we shipped is the proof, not the bios. The E&CE note is for faculty: this statement is the only one spanning CSE, ECE, and EE clusters (W3).");

// ---------- S10 CLOSE (dark) ----------
s = p.addSlide();
s.background = { color: FOREST_DARK };
s.addText("Grade our decision quality.", { x: 1, y: 1.0, w: 8, h: 0.7, fontSize: 34, bold: true, color: CREAM, fontFace: "Cambria", align: "center", margin: 0 });
s.addText("Why this action, why now, why this channel. That is the product, and your questions shape Round 1.", { x: 1.2, y: 1.8, w: 7.6, h: 0.55, fontSize: 15, color: MOSS, fontFace: "Calibri", align: "center", margin: 0 });
card(s, 1.2, 2.6, 7.6, 1.5, "2A4A31");
s.addText("One limitation, stated openly: the rule set is a curated seed awaiting agronomist review; the IMD feed and telecom delivery are simulated in this prototype, and nothing is sent over live SMS or WhatsApp. Every claim in this deck has a dated source on the repo.", { x: 1.45, y: 2.78, w: 7.1, h: 1.15, fontSize: 12, color: CREAM, fontFace: "Calibri", margin: 0 });
s.addText("Live demo: 3 minutes  |  Repo: github.com/harshgounder/craft-n-code  |  Team 511", { x: 1, y: 4.5, w: 8, h: 0.4, fontSize: 12.5, color: MOSS, fontFace: "Calibri", align: "center", margin: 0 });
s.addNotes("Ask tied to the next milestone: faculty feedback contract. Slide 8 of the runbook said the same: feedback shapes Round 1. The limitation is the honesty move faculty will remember.");

p.writeFile({ fileName: "KrishiSetu-Round0-20260816.pptx" }).then(() => console.log("DECK WRITTEN"));
