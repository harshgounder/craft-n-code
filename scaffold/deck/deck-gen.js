// Craft N Code 2026 deck generator - ONE skeleton, 4 idea decks.
// Usage: node deck-gen.js   -> writes deck-signal.pptx, deck-pulse.pptx,
//                              deck-nightops.pptx, deck-kavach.pptx
// On the night: pick the deck that matches the problem, 0 rebuild needed.
const pptxgen = require("pptxgenjs");

const NAVY = "0B1020", PANEL = "141B33", PANEL2 = "1B2440", LINE = "263055";
const TXT = "E8ECF8", MUT = "93A0C4", VIOLET = "6C5CE7", MINT = "00CE8F",
      WARN = "FFB020", DANGER = "FF5470", WHITE = "FFFFFF";

const IDEAS = {
  signal: {
    file: "deck-signal.pptx",
    accent: VIOLET,
    title: "Signal",
    tagline: "One ranked AI feed for a student's entire day",
    problemTitle: "Your day lives in 6 channels. The one notice that matters drowns.",
    problem: [
      "Gmail, Classroom, WhatsApp, Unstop, portal notices, Instagram: 6 unread streams",
      "The ONE notice that matters (MTE dates, room shifts, fee deadline) sits under 200 memes",
      "Missed deadline = failed exam, withheld results, late fees. Nobody's fault, everybody pays",
    ],
    solutionTitle: "Signal: ingest, dedupe, summarize, rank, auto-deadline",
    solution: [
      "Pulls all 6 channels into one feed (IMAP, Google API, Unstop API, portal scrape)",
      "LLM summarizes each notice to one line, ranks by your profile + sender authority + deadline",
      "Deadlines become calendar invites with 2-day reminders",
      "Ask anything: \"when is the MTE?\" gets a sourced answer",
    ],
    demo: [
      "Open \"today\" -> 60-second digest reads out (fee + MTE on top)",
      "Ask \"when is the MTE?\" -> semantic search answers with source + date",
      "Deadline card -> calendar invite",
      "Focus mode: collapse everything but top-3 + urgent",
    ],
    impact: [
      ["6", "channels unified into one feed"],
      ["10s", "to know your whole day"],
      ["0", "missed deadlines after install"],
    ],
    roadmap: [
      ["24h", "MVP: Gmail + portal + seed data live on stage"],
      ["1 wk", "Classroom + Unstop live connectors, mobile PWA"],
      ["1 mo", "Institutional rollout: registrar office publishes through Signal"],
      ["90d", "Campus-wide: 5,000 students, placement + mess modules"],
    ],
  },
  pulse: {
    file: "deck-pulse.pptx",
    accent: MINT,
    title: "Campus Pulse",
    tagline: "Rebuild the campus notice + complaint system as one AI-native app",
    problemTitle: "Notices live in 6 places. Complaints go into a system nobody reads.",
    problem: [
      "Portal, mail, WhatsApp, Instagram, Classroom, notice boards: six copies of every notice",
      "Complaints filed into a 2010-era form, then silence for weeks",
      "Mess and canteen run on word of mouth: queues, menu surprises, no feedback loop",
    ],
    solutionTitle: "Campus Pulse: one feed, one complaint tracker, one live board",
    solution: [
      "Same engine as Signal: 6 sources -> dedupe -> summarize -> rank -> deadlines",
      "Complaint tracker with photo evidence, AI triage, SLA timer, 48h escalation",
      "Public fixed board: what got fixed, who fixed it, when",
      "Mess live board: queue load, today's menu, feedback NLP",
    ],
    demo: [
      "6 sources -> one feed -> \"today in 60 seconds\"",
      "File a complaint with a photo -> auto-triage to plumbing, SLA 48h",
      "Live status: ticket C-114 is being fixed",
      "Mess board: queue + menu + feedback",
    ],
    impact: [
      ["6->1", "sources collapse into one feed"],
      ["48h", "SLA on every complaint, auto-escalation"],
      ["100%", "visible: every fix lands on the public board"],
    ],
    roadmap: [
      ["24h", "MVP: feed + complaint tracker with seed data on stage"],
      ["1 wk", "Registrar + hostel wardens pilot, WhatsApp ingestion"],
      ["1 mo", "Full campus: mess, library, placement modules"],
      ["90d", "Template for every college in Rajasthan"],
    ],
  },
  nightops: {
    file: "deck-nightops.pptx",
    accent: WARN,
    title: "Night Ops",
    tagline: "Campus safety + night-life logistics for people who live after dark",
    problemTitle: "Campus at 2 AM: unlit routes, unwalked walks, nobody awake to help.",
    problem: [
      "Walking to the mess or gate at 2 AM: sparse security, dark stretches, no one knows you're out",
      "Night deliveries and mess runs coordinated over WhatsApp groups",
      "Women's safety on campus is a real, daily anxiety, not a feature request",
    ],
    solutionTitle: "Night Ops: trusted-circle safety + night logistics in one app",
    solution: [
      "Trusted circle: \"I'm walking back\" share with live location, auto ETA, arrival ping",
      "Lit-route heatmap: crowd-sourced safe/lit/crowded ratings -> safe path suggestions",
      "SOS: 2-second hold captures audio + video evidence, streams to circle + security with location",
      "Night mess pre-order + runners board; quiet-hours focus mode",
    ],
    demo: [
      "Start a night walk -> map shows the lit route + ETA to your circle",
      "SOS demo: 2-second hold -> circle gets live location + evidence clip",
      "Pre-order for 2 AM mess pickup",
      "Focus mode: campus-asleep pomodoro",
    ],
    impact: [
      ["2s", "hold to trigger SOS with evidence"],
      ["Live", "location + ETA shared with your circle"],
      ["24/7", "night mess + delivery coordination"],
    ],
    roadmap: [
      ["24h", "MVP: walk share + SOS + seeded route heatmap on stage"],
      ["1 wk", "Security desk dashboard, WebRTC live stream"],
      ["1 mo", "Hostel pilot: night mess pre-orders live"],
      ["90d", "Campus-wide + multi-campus rollout"],
    ],
  },
  kavach: {
    file: "deck-kavach.pptx",
    accent: DANGER,
    title: "Kavach",
    tagline: "Call-security platform: digital-arrest + voice-scam shield for Indian families",
    problemTitle: "India's biggest quantified fraud is one phone call away.",
    problem: [
      "Digital-arrest scam: fake CBI/police calls coerce victims into transferring life savings",
      "4,057 crore lost across 297,727 complaints (2022 - May 2026), losses up 20x by 2024",
      "AI-cloned voices: 30-60 seconds of harvested audio, spoofed caller ID, zero consumer defense",
    ],
    solutionTitle: "Kavach: six detection engines, one intervention loop, Hindi-first",
    solution: [
      "Real-time scam-call screening across six detection departments",
      "Family alert chain: flagged call pings trusted contacts instantly",
      "Evidence logging: full call evidence file for police complaints",
      "Already built, already tested on the IIC route",
    ],
    demo: [
      "Live scam-call simulation -> detection in seconds",
      "Family alert fires with call details + risk score",
      "Evidence file generated for a police complaint",
      "The 24h build: night-safety integration + live demo harness",
    ],
    impact: [
      ["4,057 cr", "fraud detected, one call at a time"],
      ["6", "detection engines fused in one loop"],
      ["Hindi", "first: built for the most targeted users"],
    ],
    roadmap: [
      ["24h", "Night-safety integration + live demo harness at this event"],
      ["1 mo", "IIC 3.0 R2: family network, evidence export polish"],
      ["3 mo", "Play-store launch, Telugu + Tamil voices"],
      ["1 yr", "Bank-partnered fraud interception API"],
    ],
  },
};

function iconCircle(pptx, slide, x, y, d, color, emoji) {
  slide.addShape("ellipse", { x, y, w: d, h: d, fill: { color }, line: { type: "none" } });
  slide.addText(emoji, { x, y: y + d * 0.18, w: d, h: d * 0.6, align: "center",
    fontSize: d * 0.42, fontFace: "Arial" });
}

function titleSlide(pptx, idea) {
  const s = pptx.addSlide();
  s.background = { color: NAVY };
  s.addShape("rect", { x: 0, y: 0, w: 13.33, h: 0.12, fill: { color: idea.accent } });
  s.addText("TEAM 511", { x: 0.9, y: 0.7, w: 4, h: 0.4, fontSize: 13, color: MUT, charSpacing: 2, fontFace: "Arial" });
  s.addText(idea.title, { x: 0.9, y: 1.9, w: 11.5, h: 1.3, fontSize: 64, bold: true, color: WHITE, fontFace: "Arial" });
  s.addText(idea.tagline, { x: 0.9, y: 3.25, w: 11, h: 0.7, fontSize: 22, color: idea.accent, fontFace: "Calibri" });
  s.addText("Craft N Code 2026 | Rajasthan State Qualifier | 3-minute demo", {
    x: 0.9, y: 4.9, w: 11, h: 0.4, fontSize: 14, color: MUT, fontFace: "Calibri" });
  s.addText("Harsh Gounder (lead) · Ayush Kharwar · Sujal Shukla", {
    x: 0.9, y: 5.4, w: 11, h: 0.4, fontSize: 14, color: MUT, fontFace: "Calibri" });
  iconCircle(pptx, s, 11.4, 0.55, 0.9, NAVY, "◉");
  s.addNotes("Open: \"Good morning. 3 minutes. [problem line]. This is [name].\"");
  return s;
}

function problemSlide(pptx, idea) {
  const s = pptx.addSlide();
  s.background = { color: WHITE };
  s.addText("THE PROBLEM", { x: 0.7, y: 0.55, w: 6, h: 0.4, fontSize: 13, bold: true, color: idea.accent, charSpacing: 2, fontFace: "Arial" });
  s.addText(idea.problemTitle, { x: 0.7, y: 1.0, w: 11.9, h: 1.1, fontSize: 30, bold: true, color: NAVY, fontFace: "Calibri" });
  const bullets = idea.problem.map((t) => ({ text: t, options: { bullet: true, breakLine: true, paraSpaceAfter: 10 } }));
  s.addText(bullets, { x: 0.7, y: 2.5, w: 7.2, h: 3.9, fontSize: 16, color: "333A52", fontFace: "Calibri", valign: "top" });
  // chaos visual: 6 source chips -> one feed
  const srcs = [["WhatsApp", "💬"], ["Gmail", "📧"], ["Classroom", "🎓"], ["Unstop", "⚡"], ["Portal", "🏛"], ["Insta", "📸"]];
  srcs.forEach(([name, em], i) => {
    const x = 8.3 + (i % 2) * 2.1, y = 1.9 + Math.floor(i / 2) * 1.05;
    s.addShape("roundRect", { x, y, w: 1.95, h: 0.85, rectRadius: 0.12, fill: { color: "F0F2FA" }, line: { color: LINE, width: 1 } });
    s.addText(em + "  " + name, { x, y: y + 0.22, w: 1.95, h: 0.4, align: "center", fontSize: 13, color: "333A52", fontFace: "Calibri" });
  });
  s.addShape("roundRect", { x: 8.3, y: 5.15, w: 4.25, h: 0.95, rectRadius: 0.14, fill: { color: idea.accent } });
  s.addText("ONE feed, ranked", { x: 8.3, y: 5.4, w: 4.25, h: 0.5, align: "center", fontSize: 17, bold: true, color: WHITE, fontFace: "Calibri" });
  s.addText("→", { x: 10.0, y: 4.85, w: 0.8, h: 0.5, align: "center", fontSize: 26, bold: true, color: idea.accent, fontFace: "Arial" });
  s.addNotes("Problem: [read first line]. The cost is real: missed exams, fees, safety.");
  return s;
}

function solutionSlide(pptx, idea) {
  const s = pptx.addSlide();
  s.background = { color: WHITE };
  s.addText("THE SOLUTION", { x: 0.7, y: 0.55, w: 6, h: 0.4, fontSize: 13, bold: true, color: idea.accent, charSpacing: 2, fontFace: "Arial" });
  s.addText(idea.solutionTitle, { x: 0.7, y: 1.0, w: 11.9, h: 1.1, fontSize: 28, bold: true, color: NAVY, fontFace: "Calibri" });
  const stages = [["ingest", "pull every channel"], ["dedupe", "one copy, clean"], ["summarize", "LLM one-liners"], ["rank", "what matters first"], ["deadlines", "auto calendar"]];
  stages.forEach(([name, sub], i) => {
    const x = 0.7 + i * 2.45;
    s.addShape("roundRect", { x, y: 2.45, w: 2.25, h: 1.55, rectRadius: 0.14, fill: { color: "F0F2FA" }, line: { color: LINE, width: 1 } });
    s.addText(name, { x, y: 2.72, w: 2.25, h: 0.5, align: "center", fontSize: 17, bold: true, color: idea.accent, fontFace: "Arial" });
    s.addText(sub, { x, y: 3.3, w: 2.25, h: 0.55, align: "center", fontSize: 11.5, color: MUT, fontFace: "Calibri" });
    if (i < 4) s.addText("→", { x: x + 2.28, y: 2.85, w: 0.35, h: 0.5, fontSize: 20, bold: true, color: idea.accent, fontFace: "Arial" });
  });
  const bullets = idea.solution.map((t) => ({ text: t, options: { bullet: true, breakLine: true, paraSpaceAfter: 9 } }));
  s.addText(bullets, { x: 0.7, y: 4.35, w: 11.9, h: 2.6, fontSize: 15.5, color: "333A52", fontFace: "Calibri", valign: "top" });
  s.addNotes("Solution: same engine across ideas, so the 24h build is mounting a skin.");
  return s;
}

function demoSilde(pptx, idea) {
  const s = pptx.addSlide();
  s.background = { color: NAVY };
  s.addText("LIVE DEMO · 3 MINUTES", { x: 0.9, y: 0.6, w: 8, h: 0.4, fontSize: 13, bold: true, color: idea.accent, charSpacing: 2, fontFace: "Arial" });
  const bullets = idea.demo.map((t, i) => ({ text: `${i + 1}.  ${t}`, options: { breakLine: true, paraSpaceAfter: 14 } }));
  s.addText(bullets, { x: 0.9, y: 1.5, w: 11.4, h: 4.6, fontSize: 19, color: TXT, fontFace: "Calibri", valign: "top" });
  s.addShape("roundRect", { x: 0.9, y: 6.35, w: 11.4, h: 0.75, rectRadius: 0.1, fill: { color: PANEL }, line: { color: idea.accent, width: 1 } });
  s.addText("Backup: pre-recorded demo video + offline mode. The demo cannot die.", {
    x: 0.9, y: 6.52, w: 11.4, h: 0.4, align: "center", fontSize: 13, color: MUT, fontFace: "Calibri" });
  s.addNotes("Demo script: " + idea.demo.join(" | "));
  return s;
}

function impactSlide(pptx, idea) {
  const s = pptx.addSlide();
  s.background = { color: WHITE };
  s.addText("IMPACT", { x: 0.7, y: 0.55, w: 6, h: 0.4, fontSize: 13, bold: true, color: idea.accent, charSpacing: 2, fontFace: "Arial" });
  s.addText("Why this matters now", { x: 0.7, y: 1.0, w: 11, h: 0.8, fontSize: 30, bold: true, color: NAVY, fontFace: "Calibri" });
  idea.impact.forEach(([n, l], i) => {
    const x = 0.7 + i * 4.1;
    s.addShape("roundRect", { x, y: 2.2, w: 3.8, h: 3.1, rectRadius: 0.16, fill: { color: "F0F2FA" }, line: { color: LINE, width: 1 } });
    s.addText(n, { x, y: 2.65, w: 3.8, h: 1.0, align: "center", fontSize: 40, bold: true, color: idea.accent, fontFace: "Arial" });
    s.addText(l, { x, y: 3.8, w: 3.8, h: 1.2, align: "center", fontSize: 14, color: "333A52", fontFace: "Calibri" });
  });
  s.addNotes("Impact: three numbers, no fluff.");
  return s;
}

function roadmapSlide(pptx, idea) {
  const s = pptx.addSlide();
  s.background = { color: NAVY };
  s.addText("ROADMAP", { x: 0.9, y: 0.6, w: 6, h: 0.4, fontSize: 13, bold: true, color: idea.accent, charSpacing: 2, fontFace: "Arial" });
  s.addText("Shipped in 24 hours, growing from there", { x: 0.9, y: 1.05, w: 11, h: 0.8, fontSize: 26, bold: true, color: WHITE, fontFace: "Calibri" });
  idea.roadmap.forEach(([when, what], i) => {
    const x = 0.9 + i * 2.95;
    s.addShape("roundRect", { x, y: 2.6, w: 2.7, h: 3.1, rectRadius: 0.14, fill: { color: PANEL }, line: { color: LINE, width: 1 } });
    s.addShape("ellipse", { x: x + 1.05, y: 2.95, w: 0.6, h: 0.6, fill: { color: idea.accent } });
    s.addText(when, { x: x + 0.2, y: 3.75, w: 2.3, h: 0.5, align: "center", fontSize: 17, bold: true, color: idea.accent, fontFace: "Arial" });
    s.addText(what, { x: x + 0.25, y: 4.35, w: 2.2, h: 1.2, align: "center", fontSize: 12, color: MUT, fontFace: "Calibri" });
  });
  s.addNotes("Roadmap: honest 24h scope, then 90 days.");
  return s;
}

function teamSlide(pptx, idea) {
  const s = pptx.addSlide();
  s.background = { color: WHITE };
  s.addText("THE TEAM", { x: 0.7, y: 0.55, w: 6, h: 0.4, fontSize: 13, bold: true, color: idea.accent, charSpacing: 2, fontFace: "Arial" });
  s.addText("Team 511 · E&CE, Manipal University Jaipur", { x: 0.7, y: 1.0, w: 11, h: 0.8, fontSize: 28, bold: true, color: NAVY, fontFace: "Calibri" });
  const members = [
    ["Harsh Gounder", "Lead · Systems", "Engine, ingestion, LLM layer, demo"],
    ["Ayush Kharwar", "Backend", "FastAPI, Supabase, connectors"],
    ["Sujal Shukla", "Frontend", "Next.js, Tailwind, UI kit"],
  ];
  members.forEach(([name, role, what], i) => {
    const x = 0.7 + i * 4.1;
    s.addShape("roundRect", { x, y: 2.3, w: 3.8, h: 3.0, rectRadius: 0.16, fill: { color: "F0F2FA" }, line: { color: LINE, width: 1 } });
    iconCircle(pptx, s, x + 1.55, 2.6, 0.7, idea.accent, ["👑", "⚙", "🎨"][i]);
    s.addText(name, { x, y: 3.5, w: 3.8, h: 0.5, align: "center", fontSize: 17, bold: true, color: NAVY, fontFace: "Calibri" });
    s.addText(role, { x, y: 4.0, w: 3.8, h: 0.4, align: "center", fontSize: 12.5, color: idea.accent, fontFace: "Calibri" });
    s.addText(what, { x, y: 4.45, w: 3.8, h: 0.7, align: "center", fontSize: 11.5, color: MUT, fontFace: "Calibri" });
  });
  s.addNotes("Team: three people, one engine, many skins.");
  return s;
}

function build(idea) {
  const pptx = new pptxgen();
  pptx.layout = "LAYOUT_WIDE";
  pptx.author = "Team 511";
  pptx.title = idea.title + " - Craft N Code 2026";
  titleSlide(pptx, idea);
  problemSlide(pptx, idea);
  solutionSlide(pptx, idea);
  demoSilde(pptx, idea);
  impactSlide(pptx, idea);
  roadmapSlide(pptx, idea);
  teamSlide(pptx, idea);
  pptx.writeFile({ fileName: idea.file }).then((f) => console.log("wrote", f));
}

Object.values(IDEAS).forEach(build);
