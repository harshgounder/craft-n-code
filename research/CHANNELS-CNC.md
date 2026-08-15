# CHANNELS-CNC.md: How to get Craft N Code 2026 winning ideas

Source: startup-idea-lab's 10 idea channels (README), remapped from "how to find a startup" to "how to predict and select the winning build for THIS event". Each channel below: what it is for Craft N Code, how to mine it, where the evidence already lives in this repo, which parallel.ai prompt fires it, evidence strength.

The master rule: a channel is worth exactly what it predicts about the 21:30 Aug 15 drop from the 5 sponsors (Google 24% / Accenture 22% / Meta 21% / Adobe 18% / Apple 15% priors). Channels that predict the STATEMENT are 5 stars. Channels that predict the WINNING BUILD are 4 stars. Channels that only suggest domains are 3 stars.

---

## 1. SPONSOR MONEY-FLOW (adapted from Money-flow) ★★★★★

What it is for startups: where capital goes (VC, gov, procurement, jobs, ads) = validated demand.
What it is for THIS event: where the 5 sponsors push capital + products in 2026. What they ship is what they ask. Google pushes Gemini + Agentspace + AI Studio; Apple pushes Apple Intelligence + on-device; Meta pushes Llama + AI Studio + WhatsApp AI; Accenture pushes enterprise agents + responsible AI; Adobe pushes Firefly + Acrobat AI + Express.

How to mine: company docs, launch blogs, I/O/WWDC/Connect/MAX keynotes, API pricing pages (free tiers = student-feasible lanes), investor letters, hiring posts (building X = asking about X).

Evidence already in repo: TOPIC-UNIVERSE S1 (company lanes), S9 (landscape pass 1). Prompts: `prompts/company-lane-scan.md`. Wave-3 run `cnc-company-lanes-2026` (2026-08-15) is the dedicated fire.

## 2. STATEMENT GRAMMAR (hackathon-native) ★★★★★

What it is: the combinatorial skeleton every statement is built from: subject + core action + constraint + channel + evaluation + twist. 19 subjects x 27 actions x 22 constraints x 15 channels x 9 evals x 12 twists = ~34M raw combinations, trimmed by setter DNA to a few hundred probable.

How to mine: keep appending closed sets from every real statement you recover (2022 set, 2025 set, wave reports). Every new shape/domain run feeds new slot values.

Evidence in repo: `research/STATEMENT-GRAMMAR.md`. This is the parse engine for the drop.

## 3. SPONSOR DNA (hackathon-native) ★★★★★

What it is: what each company actually asks in ITS hackathons and what its product lines permit. Product/API names beat every prior. Vocabulary watch-words: agent, grounding, verification, evidence, tool use (Google); creative control, generation, iteration (Adobe); privacy, on-device, offline (Apple); multimodal, messaging, open-source (Meta); enterprise, governance, escalation, audit (Accenture).

Evidence in repo: `research/COMPANY-DNA.md` (2-minute fingerprint method), TOPIC-UNIVERSE S1.

## 4. INSIDER INTEL (hackathon-native) ★★★★★

What it is: club execs, organizers, past winners. Never public, highest value per byte. Rudra (in person, Aug 14) confirmed: real statements written by sponsors, site tracks are the backup set. Setter prior table originates here.

How to mine: conversations, not research. The Rudra ask list is in craft-n-code (docs/RUDRA-ASK.md): 2025 Rajasthan state problems, judging format, winning team's build.

## 5. PRIOR EDITIONS (hackathon-native; replaces Acquisition market) ★★★★

What it is for startups: buying small products = validated demand. What it is for THIS event: organizers recycle problem families every 2-3 years re-skinned with new tech. 2022 set (9 verified problems: code snippet sharing, hostel mgmt, smart campus, bill split, mess mgmt, PM2.5, IRCTC automation, crypto crowdfunding, NFT ticketing) -> 2025 set (Rewind the Legacy, Night Ops, Signal/Noise, Open Track, Hardware Hack) -> 2026 (5 backup tracks PS-01..PS-05). Lineage documented: D3h09 -> 2025 NFT ticketing, D3h05 -> 2026 night canteen, D3h06 -> AI/ML track DNA, D3h07 -> security/automation DNA.

Evidence in repo: TOPIC-UNIVERSE S6/S7, craft-n-code `research/D3FEST-2022-PROBLEMS.md`.

## 6. WORKAROUND DETECTION (from startup-idea-lab, verbatim concept) ★★★★

What it is: the spreadsheets, Zapier chains, WhatsApp groups, manual rituals people assemble because no product exists. The statement's target IS the workaround. Judges reward "I saw this pain, here is the fix".

How to mine: complaint threads + "how do you do X today" answers + r/SomebodyMakeThis-style asks in the 5 sponsor lanes (education, healthcare admin, small shops, content ops, campus life). A workaround with a paper trail is a statement waiting to be written.

## 7. FAILED-PRODUCT AUTOPSIES (from startup-idea-lab, verbatim concept) ★★★★

What it is: dead companies with live problems. Execution failure != idea failure. For THIS event: dead AI startups in the sponsor lanes = validated pain + a story judges already know (and the product's UX mistakes are free lessons for the 24h build). Also dead hackathon projects from prior editions: why did they die, what was the demo gap.

How to mine: Failory, CB Insights autopsies, AI graveyard lists, prior-edition losers (winner forensics covers the winners; autopsy covers the field).

## 8. WINNER FORENSICS (hackathon-native) ★★★★

What it is: what won, what lost, why. Verified 2026 pattern: deepest stack + zero external deps + working demo + visible AI loop + honest failure handling. Demo matters more than the idea. Our scaffold IS the winning pattern (input -> extraction -> evidence -> rank -> propose -> approve -> audit).

Evidence in repo: TOPIC-UNIVERSE S8, craft-n-code winner forensics + COMPETITOR-POOL. Prompt: `prompts/winner-forensics.md`.

## 9. JUDGE TASTE (hackathon-native) ★★★★

What it is: who judges (sponsor reps + academics), what they reward, rubric weightings. Per-judge dossier + how-to-win matrix. Sponsor judges weight their own product lines; academic judges weight impact + completeness.

Prompt: `prompts/judge-taste-profile.md` (re-fire closer to finals with the actual judge list).

## 10. COMPELLED EVIDENCE (from startup-idea-lab, verbatim concept) ★★★★

What it is: machine-readable scars: audits, incident reports, queues, budget records, complaint databases, fraud stats. Problems with receipts. For THIS event: UPI fraud numbers, DPDPA fine records, hospital waitlists, railway complaints, campus queue data. A statement citing a number (e.g. "X% of UPI fraud goes unrecovered") is the strongest possible problem framing, and the number is citable in the demo itself.

## 11. NONCONSUMPTION (from startup-idea-lab, verbatim concept) ★★★★

What it is: people who want the outcome but use nothing. For THIS event: farmers, kirana shops, rural schools, small clinics, gig workers. Judges (esp. Google/Accenture) weight India relevance and inclusion. The empty lane has no incumbent to beat and the impact story writes itself. Kit fit: KIT-4 messaging + voice-first, Hindi-first (Kavach DNA).

## 12. GEOGRAPHIC ARBITRAGE (from startup-idea-lab, verbatim concept) ★★★★

What it is: products validated in US/EU not yet in India (or done badly). For THIS event: instant impact framing ("works in the US, India does it on paper"). US/EU AI products with no Indian equivalent: clinic intake agents, school admin copilots, small-business bookkeeping agents, landlord-tenant document automation. Same build, India skin, judges see relevance.

## 13. MOCK DROPS (hackathon-native) ★★★★

What it is: rehearsal statements generated from the grammar, parsed under the 10-minute timer, failure-injected against the scaffold (network, LLM quota, cold boot, hostile judge, 100x load, Indic input). The only channel that trains the actual skill: the parse.

Prompt: `prompts/mock-drop-stress-bench.md`. Run tonight after the 3 wave-3 reports land.

## 14. COMPLAINT MINING (from startup-idea-lab, verbatim concept) ★★★

What it is: what people hate (Reddit, reviews, forums). For THIS event: raw material, not prediction. A complaint proves pain exists; it does not prove a sponsor will ask about it. Use it to fill domain slots and to phrase the demo's problem slide with real quotes.

## 15. DEMAND FORECASTING (from startup-idea-lab, verbatim concept) ★★★

What it is: trends, patents, regulatory pipeline. For THIS event: DPDPA compliance (63M SMBs), AI for Bharat, on-device shift, MCP adoption curve. Tells you which lanes the sponsors' product teams are thinking about this quarter. Wave-3 run `cnc-shapes-expansion2` + `cnc-domains-expansion2` (2026-08-15) are the live fires.

## 16. FOUNDER FRAMEWORKS (from startup-idea-lab, verbatim concept) ★★★

What it is: PG, JTBD, Mom Test, Blue Ocean applied to problem SELECTION. For THIS event: once the drop lands and we have 5 candidate angles, these frameworks kill the fake problems fast (does the user actually do this today? what would they do without it?). Blue Ocean = pick the lane the other 628 teams won't.

## 17. PARTICIPANT FIELD (hackathon-native) ★★★

What it is: who else is competing, what they build, which lanes crowd vs empty. 629 regs (Rajasthan, watchdog 2026-08-15 10:04) and climbing vs 706 in 2025. The "easiest qualifier" line is dead; the field is near-2025 size. Empty-lane analysis: which of our kit combos would be unique in the room.

## 18. SITE FORENSICS (hackathon-native) ★★★

What it is: event site source, submission flow (Unstop round 1569450: PPT, pdf/pptx, max 50MB, resubmit allowed, latest wins), backup tracks. Read-only public recon, low signal now, high signal at the finals (Oct 30) when the site changes.

## 19. TOPIC TREND SCAN (hackathon-native) ★★★

What it is: the 2026 landscape (agentic AI, MCP ecosystems, multi-agent, on-device/edge LLMs, GenAI education, AI for Bharat, responsible AI). Confirmed live 2026-08-15 from reskilll + India hackathon calendar. Feeds shapes and domains, does not predict the setter.

---

## How channels combine at the drop (21:30)

1. Fingerprint the company: named product beats every prior (COMPANY-DNA method). If no product name: vocabulary watch-words (S1), then shape, then prior table.
2. Pin the shape: 7 known + whatever wave-3 adds (S2). The shape pins the pipeline.
3. Pin the domain: 30 known + wave-3 additions (S3). The domain pins the data and the demo story.
4. Check the constraint slots (S5): gate, channel, twist. The constraint pins the adapter (browser, WhatsApp, on-device).
5. Kit resolves (S4). Demo gate resolves (S2 per-shape gates).
6. Stress: run the mock-drop bench on the picked angle, 10 minutes.

## Channel health ledger

| Channel | Evidence strength | Status (2026-08-15 11:50 IST) |
|---|---|---|
| Sponsor money-flow | ★★★★★ | wave-3 run live: cnc-company-lanes-2026 |
| Statement grammar | ★★★★★ | S5 complete, 7 shapes / 30 domains / 27 actions / 22 constraints |
| Sponsor DNA | ★★★★★ | COMPANY-DNA.md live, fingerprint method proven |
| Insider intel | ★★★★★ | Rudra intel banked; 2025 state problems still owed (RUDRA-ASK) |
| Prior editions | ★★★★ | 2022 + 2025 + backup tracks documented |
| Workaround detection | ★★★★ | concept mapped, not yet mined as a wave |
| Failed-product autopsies | ★★★★ | concept mapped, not yet mined as a wave |
| Winner forensics | ★★★★ | 2026 pattern verified in craft-n-code |
| Judge taste | ★★★★ | profile template ready, judges unknown until closer |
| Compelled evidence | ★★★★ | concept mapped, UPI/DPDPA stats pending |
| Nonconsumption | ★★★★ | mapped to KIT-4/KIT-1 voice-first |
| Geographic arbitrage | ★★★★ | mapped, US/EU product list pending |
| Mock drops | ★★★★ | bench prompt ready, first full drill tonight |
| Complaint mining | ★★★ | concept mapped |
| Demand forecasting | ★★★ | wave-3 runs live: shapes + domains expansion |
| Founder frameworks | ★★★ | mapped, fires after the drop |
| Participant field | ★★★ | 629 regs live; empty-lane analysis pending |
| Site forensics | ★★★ | Unstop flow documented |
| Topic trend scan | ★★★ | landscape pass 1 done (S9) |
