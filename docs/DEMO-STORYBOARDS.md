# DEMO STORYBOARDS  -  pre-recorded videos + live backup

Four 3-min storyboards matching the 4 decks (agentic/multimodal/creative/kavach).
Record once today, screen + voiceover. If the projector dies, network dies, or a
demo rate-limits, the video saves us. ALSO: judges see polish.

## The one pattern (all four demos)

Every demo shows the same loop the judges reward:
source -> signal -> rank -> explanation -> owner -> action -> outcome.

## 1. BriefLens (agentic)  -  3:00

| Time | Screen | Voiceover |
|---|---|---|
| 0:00-0:05 | Title card: BriefLens, Team 511 | "Every day, inputs arrive from everywhere. The one action that matters is drowning." |
| 0:05-0:35 | The feed: 8 items from 4 channels, ranked | "This is a day's input. Email, chat, portal, tickets. The engine ingests everything, dedupes it, summarizes each to one line." |
| 0:35-1:00 | Digest: 2 urgent actions on top | "It ranks by your profile, the sender's authority, and the deadline. You see the two urgent actions in ten seconds." |
| 1:00-1:40 | Click an action -> proposal + evidence | "Here's the interesting part: it doesn't just tell you, it proposes. Pay the fee, submit the form. Evidence attached, source shown." |
| 1:40-2:10 | APPROVE -> status flips, audit log | "You approve. The action executes and the audit log records who, when, what. No blind automation, no missed actions." |
| 2:10-2:50 | Ask: "what do I need to do today?" | "Ask anything. The answer comes with the source it's grounded in." |
| 2:50-3:00 | Impact cards: 1 feed, 10s, 0 missed | "One feed. Ten seconds. Zero missed actions." |

## 2. Kavach Circle (multimodal)  -  3:00

| Time | Screen | Voiceover |
|---|---|---|
| 0:00-0:05 | Title card | "Assistants hallucinate. This one shows its sources and asks for help when unsure." |
| 0:05-0:40 | Drop a screenshot + a PDF | "Text, images, PDFs, documents. Any input format in, the system extracts the facts and shows the evidence panel with source links." |
| 0:40-1:10 | Ask a question -> answer with confidence band | "Every answer carries a confidence score and its sources. You can check the reasoning, not just trust it." |
| 1:10-1:50 | Ask something risky -> escalation to human | "When it's uncertain or high-risk, it doesn't guess. It routes to a human. That's the gate that keeps it safe." |
| 1:50-2:30 | Correct an answer -> correction applied + logged | "And when the human corrects it, the fix is applied and remembered." |
| 2:30-3:00 | Impact cards | "Any input. Evidence on every answer. Zero hallucinated high-risk answers." |

## 3. SignalStory (creative)  -  3:00

| Time | Screen | Voiceover |
|---|---|---|
| 0:00-0:05 | Title card | "Making content is slow. Making content that stays on-brand is slower." |
| 0:05-0:40 | Paste a one-paragraph brief | "A real brief in. The system extracts the brand rules, tone, and audience." |
| 0:40-1:20 | Generate an asset -> caption + alt text | "It generates the asset, captions it, and adds alt text. One brief becomes a ready asset." |
| 1:20-2:00 | Edit -> regenerate -> reviewer approves | "Human review before anything ships. Revise, regenerate, approve. The version is logged." |
| 2:00-2:40 | Provenance card: prompt, model, lineage | "And every asset carries its provenance: the prompt, the model, the lineage. You can always answer where it came from." |
| 2:40-3:00 | Impact cards | "A brief becomes an asset in minutes. Full provenance. Controlled output." |

## 4. Kavach (security)  -  3:00

| Time | Screen | Voiceover |
|---|---|---|
| 0:00-0:05 | Title card | "India's largest quantified fraud: the digital-arrest scam. 4,057 crore lost in four years." |
| 0:05-0:40 | The scam explained, one line at a time | "Fake CBI calls, AI-cloned voices, spoofed caller IDs. Banks warn you. Nobody defends the phone itself." |
| 0:40-1:20 | Simulate a digital-arrest call | "Here's the call. Kavach flags it in under a second: six detection departments, one loop." |
| 1:20-2:00 | AI proposes intervention -> user approves | "It proposes the intervention: warn, block, guide. The user approves. The loop is human-controlled." |
| 2:00-2:40 | Post-call report | "After the call: what happened, what was blocked, what the user did." |
| 2:40-3:00 | Impact cards | "Six departments. Under a second to flag. A platform defending Indian families." |

## Recording checklist

- 1080p screen capture, mic on, quiet room
- 1s black + title card at start, under 2:50 total (buffer for pitch 3-min hard cap)
- Store in assets/demos/, named demo-<skin>.mp4
- Re-record the moment a demo claim changes; stale videos lose the pitch

## Live-demo fallback ladder (on stage)

1. localhost:8137 (zero-dep server, works offline)
2. Pre-warmed browser tab (open before the pitch starts)
3. Pre-recorded video (this file's storyboards)
4. Terminal digest (python3 engine.py --seed --digest) as the absolute floor
