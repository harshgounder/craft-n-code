// Craft N Code 2026 deck generator - ONE skeleton, 4 sponsor-shaped decks.
// Usage: node deck-gen.js -> writes deck-agentic.pptx, deck-multimodal.pptx,
//                              deck-creative.pptx, deck-kavach.pptx
// On the night: pick the deck matching the released problem, 0 rebuild needed.
const pptxgen = require("pptxgenjs");

const NAVY = "0B1020", PANEL = "141B33", PANEL2 = "1B2440", LINE = "263055";
const TXT = "E8ECF8", MUT = "93A0C4", VIOLET = "6C5CE7", MINT = "00CE8F",
      WARN = "FFB020", DANGER = "FF5470", WHITE = "FFFFFF";

const IDEAS = {
  agentic: {
    file: "deck-agentic.pptx",
    accent: VIOLET,
    title: "BriefLens",
    tagline: "An AI agent that reads every input, ranks what matters, and proposes actions you approve",
    problemTitle: "Every workflow dumps inputs on you. The one action that matters drowns.",
    problem: [
      "Emails, tickets, documents, chat: raw inputs from many channels, no order, no priority",
      "The ONE action that matters (a deadline, an approval, a payment) hides under noise",
      "Missed action = cost. Nobody's fault, everybody pays",
    ],
    solutionTitle: "BriefLens: ingest, dedupe, summarize, rank, propose, approve",
    solution: [
      "Pulls every channel into one feed (email, chat, portal, tickets, docs)",
      "LLM summarizes each item to one line, ranks by your profile + sender authority + deadline",
      "Actionable items become PROPOSALS: the AI proposes, a human approves or rejects, audit logged",
      "Ask anything: \"what do I need to do today?\" gets a sourced answer",
    ],
    demo: [
      "Open \"today\" -> 60-second digest reads out (the 2 urgent actions on top)",
      "Click an action -> the proposal + evidence (source, deadline, amount) + APPROVE/REJECT",
      "Approve -> status flips to done, audit log written (who, when, what)",
      "Ask a question -> sourced answer with the source + confidence",
    ],
    impact: [
      ["1", "feed replaces N channels"],
      ["10s", "to know what needs action"],
      ["0", "actions missed after install"],
    ],
    roadmap: [
      ["24h", "MVP: ingest + rank + approval gate live on stage"],
      ["1 wk", "Live connectors, mobile PWA"],
      ["1 mo", "Team rollout: approval flows with audit"],
      ["90d", "Org-wide: every action tracked, every decision logged"],
    ],
    mcpSlide: {
      title: "MCP: capabilities behind a gate you approve",
      bullets: [
        "Compose gold-plated MCP servers (filesystem, GitHub, Slack, Postgres), never rebuild",
        "Typed, allow-listed tools; the policy gate sits outside the model, not in a prompt",
        "Human approval at every handoff, an audit trace on every call",
        "Tool poisoning is the headline attack (Invariant Labs, 1 Apr 2025): pin and scan descriptions",
      ],
    },
  },
  multimodal: {
    file: "deck-multimodal.pptx",
    accent: MINT,
    title: "Kavach Circle",
    tagline: "A multimodal assistant that reads text, images and documents, answers with evidence, and escalates to a human when uncertain",
    problemTitle: "Assistants hallucinate. This one shows its sources and asks for help when unsure.",
    problem: [
      "Text, images, PDFs, chat: information arrives in every format",
      "Generic assistants answer confidently even when wrong",
      "High-risk cases need a human, not a guess",
    ],
    solutionTitle: "Kavach Circle: any input, evidence-backed answers, human escalation",
    solution: [
      "Upload or camera input: text, image, PDF, document",
      "Extract + OCR, structured facts, evidence panel with source links",
      "Confidence score on every answer; uncertain or high-risk cases route to a human",
      "Correction flow: user fixes the model, the fix is remembered",
    ],
    demo: [
      "Drop a screenshot + a PDF -> both extracted, facts shown with sources",
      "Ask a question -> answer with confidence band + evidence links",
      "Ask something risky -> the system escalates to human review, visibly",
      "Correct an answer -> the correction is applied and logged",
    ],
    impact: [
      ["3", "input formats, one answer"],
      ["100%", "of answers carry a source"],
      ["0", "hallucinated high-risk answers (human gate)"],
    ],
    roadmap: [
      ["24h", "MVP: text + image + PDF in, evidence out, escalation gate"],
      ["1 wk", "More formats, correction memory"],
      ["1 mo", "Team deployment with audit trail"],
      ["90d", "Org-wide: every answer traceable"],
    ],
    mcpSlide: {
      title: "MCP: evidence in, escalation out, both gated",
      bullets: [
        "Compose gold-plated MCP servers (filesystem, GitHub, Supabase, Slack), never rebuild",
        "Typed, allow-listed tools; the policy gate sits outside the model, not in a prompt",
        "Human approval at every handoff, an audit trace on every call",
        "Tool poisoning is the headline attack (OWASP indirect prompt injection): pin and scan",
      ],
    },
  },
  creative: {
    file: "deck-creative.pptx",
    accent: WARN,
    title: "SignalStory",
    tagline: "Turn a real brief into brand-consistent media assets with generative AI, review, and provenance",
    problemTitle: "Making content is slow. Making content that stays on-brand is slower.",
    problem: [
      "Briefs live in docs and chats; assets live everywhere else",
      "Generative AI creates fast but uncontrolled: wrong brand, wrong facts",
      "Nobody can answer: where did this asset come from?",
    ],
    solutionTitle: "SignalStory: brief in, assets out, provenance all the way",
    solution: [
      "Brief intake: paste a real organizational brief, the system extracts tone, audience, brand rules",
      "Generate assets (image, caption, alt text) through a labeled generator adapter",
      "Review + revision loop: human approves before delivery",
      "Provenance record: prompt, model, lineage for every asset",
    ],
    demo: [
      "Paste a one-paragraph brief -> system extracts brand + tone + audience",
      "Generate an asset -> caption + alt text + export",
      "Edit -> regenerate -> reviewer approves, version logged",
      "Show the provenance card: prompt, model, lineage",
    ],
    impact: [
      ["1", "brief becomes an asset in minutes"],
      ["100%", "of assets carry provenance"],
      ["0", "uncontrolled brand breaks (review gate)"],
    ],
    roadmap: [
      ["24h", "MVP: brief in, asset out, provenance record"],
      ["1 wk", "More generators, revision history"],
      ["1 mo", "Team review flows"],
      ["90d", "Full asset pipeline with brand rules"],
    ],
    mcpSlide: {
      title: "MCP: provenance in, approval out, all through a gate",
      bullets: [
        "Compose gold-plated MCP servers (filesystem, GitHub, Supabase, Playwright), never rebuild",
        "Typed, allow-listed tools; the policy gate sits outside the model, not in a prompt",
        "Human approval at every handoff, an audit trace on every call",
        "Tool poisoning is the headline attack (Invariant Labs, 1 Apr 2025): pin and scan",
      ],
    },
  },
  kavach: {
    file: "deck-kavach.pptx",
    accent: DANGER,
    title: "Kavach",
    tagline: "The call-security platform that fuses six detection departments into one intervention loop",
    problemTitle: "India's largest quantified fraud: the digital-arrest scam. No consumer app defends the phone itself.",
    problem: [
      "₹4,057.7 crore lost across 297,727 complaints (2022-May 2026), losses grew 20x by 2024",
      "Scammers pair coercion scripts with AI-cloned voices (30-60s of harvested audio)",
      "Every bank warns customers. No consumer app defends the phone itself, in Hindi",
    ],
    solutionTitle: "Kavach: six detection departments, one intervention loop",
    solution: [
      "Six departments: caller ID analysis, voice-clone detection, coercion-script detection, UPI-request analysis, live-call guidance, post-call report",
      "AI detects scam signals -> proposes intervention -> user approves, audit logged",
      "Works offline-first, zero external dependencies in the demo",
      "Hindi-first interface for Indian families",
    ],
    demo: [
      "Simulate a digital-arrest call -> Kavach flags it in real time",
      "AI proposes intervention: warn, block, guide",
      "User approves -> action executes, audit logged",
      "Post-call report: what happened, what was blocked",
    ],
    impact: [
      ["6", "detection departments, one loop"],
      ["<1s", "to flag a scam pattern"],
      ["₹4,057 Cr", "the fraud pool we defend against"],
    ],
    roadmap: [
      ["24h", "Integration + demo harness for this round"],
      ["1 wk", "Live call interception on Android"],
      ["1 mo", "Hindi voice guidance v1"],
      ["90d", "Family rollout with banks as distribution"],
    ],
    mcpSlide: {
      title: "MCP: six departments, one gated intervention loop",
      bullets: [
        "Compose gold-plated MCP servers (Redis, Postgres, Slack), never rebuild",
        "Typed, allow-listed tools; the policy gate sits outside the model, not in a prompt",
        "Human approval at every handoff, an audit trace on every call",
        "Tool poisoning is the headline attack (OWASP indirect prompt injection): pin and scan",
      ],
    },
  },
};

function slideNum(s, i, n) {
  s.addText(String(i), { x: 13.1, y: 7.25, w: 0.5, h: 0.3, fontSize: 10, color: MUT, align: "right" });
}

function build(idea) {
  const p = new pptxgen();
  p.defineLayout({ name: "W", width: 13.33, height: 7.5 });
  p.layout = "W";
  p.author = "Team 511";
  p.company = "Craft N Code 2026";

  const a = idea.accent;

  // S1: Title
  let s = p.addSlide();
  s.background = { color: NAVY };
  s.addShape("rect", { x: 0, y: 0, w: 13.33, h: 0.12, fill: { color: a } });
  s.addText(idea.title, { x: 0.9, y: 2.3, w: 11.5, h: 1.4, fontSize: 54, bold: true, color: WHITE, fontFace: "Arial" });
  s.addText(idea.tagline, { x: 0.9, y: 3.75, w: 11.3, h: 0.9, fontSize: 20, color: MUT });
  s.addText("Team 511  |  Harsh Gounder (lead)  |  Ayush Kharwar  |  Sujal Shukla", { x: 0.9, y: 6.4, w: 11.5, h: 0.4, fontSize: 13, color: MUT });
  if (idea.mcpSlide) {
    s.addText("MCP-READY", { x: 10.6, y: 7.05, w: 2.0, h: 0.3, fontSize: 12, bold: true, color: a, align: "right" });
  }
  s.addNotes("Opening line: " + idea.problem[0]);

  // S2: Problem
  s = p.addSlide();
  s.background = { color: WHITE };
  s.addShape("rect", { x: 0, y: 0, w: 13.33, h: 0.08, fill: { color: a } });
  s.addText("The Problem", { x: 0.9, y: 0.5, w: 6, h: 0.6, fontSize: 30, bold: true, color: NAVY });
  s.addText(idea.problemTitle, { x: 0.9, y: 1.2, w: 11.5, h: 0.9, fontSize: 20, color: MUT });
  idea.problem.forEach((line, i) => {
    s.addText(`${i + 1}.  ${line}`, { x: 1.1, y: 2.4 + i * 1.15, w: 11, h: 1.0, fontSize: 17, color: NAVY });
  });
  s.addNotes("Problem framing: " + idea.problem[1]);

  // S3: Solution
  s = p.addSlide();
  s.background = { color: NAVY };
  s.addText("The Solution", { x: 0.9, y: 0.5, w: 6, h: 0.6, fontSize: 30, bold: true, color: WHITE });
  s.addText(idea.solutionTitle, { x: 0.9, y: 1.2, w: 11.5, h: 0.8, fontSize: 18, color: a });
  idea.solution.forEach((line, i) => {
    s.addShape("roundRect", { x: 0.9, y: 2.3 + i * 1.02, w: 11.5, h: 0.82, rectRadius: 0.08, fill: { color: PANEL }, line: { color: LINE, width: 1 } });
    s.addText(line, { x: 1.3, y: 2.48 + i * 1.02, w: 10.7, h: 0.5, fontSize: 15, color: TXT });
  });
  s.addNotes("Solution: " + idea.solution[0]);

  // S4: Live demo
  s = p.addSlide();
  s.background = { color: WHITE };
  s.addShape("rect", { x: 0, y: 0, w: 13.33, h: 0.08, fill: { color: a } });
  s.addText("Live Demo (3 minutes)", { x: 0.9, y: 0.5, w: 8, h: 0.6, fontSize: 30, bold: true, color: NAVY });
  idea.demo.forEach((line, i) => {
    s.addText(`STEP ${i + 1}`, { x: 1.1, y: 1.6 + i * 1.15, w: 2, h: 0.5, fontSize: 14, bold: true, color: a });
    s.addText(line, { x: 3.2, y: 1.6 + i * 1.15, w: 9, h: 0.7, fontSize: 16, color: NAVY });
  });
  s.addText("Backup: pre-recorded demo video ready if projector or network fails.", { x: 1.1, y: 6.6, w: 11, h: 0.5, fontSize: 12, italic: true, color: MUT });
  s.addNotes("Demo beats deck. Show the loop, not the slides.");

  // S5: MCP (optional, only if the idea declares it)
  if (idea.mcpSlide) {
    s = p.addSlide();
    s.background = { color: NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 13.33, h: 0.08, fill: { color: a } });
    s.addText(idea.mcpSlide.title, { x: 0.9, y: 0.5, w: 11.5, h: 0.7, fontSize: 26, bold: true, color: WHITE });
    idea.mcpSlide.bullets.forEach((line, i) => {
      s.addShape("roundRect", { x: 0.9, y: 1.7 + i * 1.25, w: 11.5, h: 1.05, rectRadius: 0.08, fill: { color: PANEL }, line: { color: LINE, width: 1 } });
      s.addText(line, { x: 1.3, y: 1.85 + i * 1.25, w: 10.7, h: 0.75, fontSize: 15, color: TXT });
    });
    s.addNotes("MCP is the wedge: approval-gated compose beats rebuild, gate outside the model.");
  }

  // S6: Impact
  s = p.addSlide();
  s.background = { color: NAVY };
  s.addText("Impact", { x: 0.9, y: 0.5, w: 6, h: 0.6, fontSize: 30, bold: true, color: WHITE });
  idea.impact.forEach((stat, i) => {
    const x = 1.0 + i * 4.0;
    s.addText(stat[0], { x, y: 2.3, w: 3.4, h: 1.2, fontSize: 44, bold: true, color: a, align: "center" });
    s.addText(stat[1], { x, y: 3.7, w: 3.4, h: 1.2, fontSize: 14, color: MUT, align: "center" });
  });
  s.addNotes("Numbers are the hook: " + idea.impact.map(x => x[0] + " " + x[1]).join("; "));

  // S6: Roadmap
  s = p.addSlide();
  s.background = { color: WHITE };
  s.addText("Roadmap", { x: 0.9, y: 0.5, w: 6, h: 0.6, fontSize: 30, bold: true, color: NAVY });
  idea.roadmap.forEach((step, i) => {
    const y = 1.7 + i * 1.25;
    s.addShape("roundRect", { x: 0.9, y, w: 2.2, h: 0.8, rectRadius: 0.08, fill: { color: a } });
    s.addText(step[0], { x: 0.9, y: y + 0.18, w: 2.2, h: 0.5, fontSize: 15, bold: true, color: WHITE, align: "center" });
    s.addText(step[1], { x: 3.4, y: y + 0.1, w: 9, h: 0.7, fontSize: 15, color: NAVY });
  });
  s.addNotes("24h build tonight, roadmap after.");

  // S7: Team
  s = p.addSlide();
  s.background = { color: NAVY };
  s.addText("Team 511", { x: 0.9, y: 0.5, w: 6, h: 0.6, fontSize: 30, bold: true, color: WHITE });
  const members = [
    ["Harsh Gounder", "Lead / Engine + AI", "🧠"],
    ["Ayush Kharwar", "Backend + Integrations", "⚙️"],
    ["Sujal Shukla", "Frontend + Demo", "🎨"],
  ];
  members.forEach((m, i) => {
    const x = 0.9 + i * 4.05;
    s.addShape("roundRect", { x, y: 1.8, w: 3.7, h: 3.6, rectRadius: 0.1, fill: { color: PANEL }, line: { color: LINE, width: 1 } });
    s.addText(m[2], { x, y: 2.2, w: 3.7, h: 1.0, fontSize: 40, align: "center" });
    s.addText(m[0], { x, y: 3.3, w: 3.7, h: 0.6, fontSize: 18, bold: true, color: WHITE, align: "center" });
    s.addText(m[1], { x, y: 3.95, w: 3.7, h: 0.6, fontSize: 13, color: MUT, align: "center" });
  });
  s.addText("Built in 24 hours for Craft N Code 2026", { x: 0.9, y: 6.2, w: 11.5, h: 0.5, fontSize: 12, color: MUT, align: "center" });
  s.addNotes("Keep it 20 seconds: names + roles + one line each.");

  p.writeFile({ fileName: idea.file }).then(() => console.log("wrote " + idea.file));
}

Object.values(IDEAS).forEach(build);
