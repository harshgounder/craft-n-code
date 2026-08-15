## executive_insights

- **Three-Act Time Allocation Wins**: A Act 1 (Problem, 30-45s), Act 2 (Solution + Live Demo, 90-120s), Act 3 (Impact, 30-45s) is the most reliable structure for any 3-5 minute hackathon pitch, and drops cleanly into a 3-minute slot [executive_insights[0]] [1][executive_insights[1]] [2][executive_insights[2]] [3].
- **Rule of Three Cognitive Frame**: The 2026 winning hackathon pitch deck combines an emotional problem, a seamless 3-minute live demo, and proof of real-world viability, packaged in 7-10 slides [executive_insights[3]] [4].
- **Opening Line = The First 10 Seconds**: Judges form a strong first impression within ten seconds; do NOT open with architecture or team, open with a specific felt pain that names a real victim and a concrete cost [executive_insights[0]] [1][executive_insights[2]] [3].
- **Pre-Compute Every Failure Path**: Live demos fail because of wifi, auth, API keys, and laptop-to-projector handshakes; the winning pattern is pre-computed screenshots, hardcoded seed data, a locally-runnable copy, and a pre-uploaded video fallback [executive_insights[0]] [1][executive_insights[4]] [5][executive_insights[5]] [6].
- **SIH and India-Style Rubrics Weight Novelty and Scale**: SIH 2025 evaluation criteria are novelty, complexity, clarity, feasibility, practicability, sustainability, and scale [executive_insights[6]] [7][executive_insights[7]] [8]; Opportunity Hack uses four equal-weight categories (Scope, Documentation, Polish, Security) worth 10 points each.
- **State Qualifier = PPT Round First**: Craft N Code's structure mirrors the broader Indian pattern: PPT/abstract round first filters top teams for the live 3-minute demo (DevHack 3.0 at Dayananda Sagar University runs the same pattern with prize pools of 20L+ and a Ramanagara grand finale).
- **The Judge's 3-Minute Memory Limit**: Stories stick far better than feature lists, so the narrative arc is the actual cognitive artefact judges carry out of the room [executive_insights[0]] [1].
- **Plant The Q&A**: End with a concrete, surprising metric or a one-line vision that forces judges to ask a specific question; you control the Q&A by what you frame last [executive_insights[0]] [1][executive_insights[2]] [3].

---

## 1_craft_n_code_2026_context_and_the_ppt_first_pattern

Craft N Code is organized by the Tech Society of IIIT Bhubaneswar (Gothapatana, Bhubaneswar, Odisha 751003). Bachelor's-degree teams of 2-4 members from the same state compete in preliminary state-level hackathons; top teams from each state advance to a 24-hour national final at IIIT Bhubaneswar.

The state-qualifier follows the canonical Indian hackathon funnel documented at SIH 2025 and at India-style events on Devfolio:

| Round | Purpose | Format | Filtering Logic |
|---|---|---|---|
| PPT / Abstract (Round 1) | Idea + problem + approach compression | 7-10 slides, scored against rubric | Filters out shallow or off-theme problems |
| 3-Minute Live Demo (Round 2) | Working MVP + judges' Q&A | On-stage + recorded fallback | Filters out non-builders |
| Grand Finale (national) | Build, present, win | 36 hours + live demo at host campus | Selects winners |

Sources: [1_craft_n_code_2026_context_and_the_ppt_first_pattern[0]] [7][1_craft_n_code_2026_context_and_the_ppt_first_pattern[1]] [8]. Insight: the PPT round is a written "thesis-test"; the 3-minute demo is a "reality-test". Teams that pass both have the highest win probability, because the PPT forces the team to write down the hard claims that the demo must then prove.

Implication -> Recommendation: For the Aug 15-16 2026 state qualifier, allocate Day-1 to PPT construction (8-10 slides, see Section 2), then Day-0 evening of Aug 16 to a 30-minute live demo dry-run with the timer running and a backup video ready. Two roles: a "speaker" who owns the presentation, and a "clicker" who owns the laptop.

---

## 2_demo_structure_the_three_act_arc_for_a_3_minute_pitch

The most reliable structure for a 3-5 minute hackathon pitch is a three-act narrative arc that maps directly to the scoring rubric used by judges [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1][2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[1]] [2].

### 2.1 Exact Time Allocation

The accepted timing allocation for a 3-minute pitch (works equally well extended to 5 minutes):

| Act | Component | Duration | Source |
|---|---|---|---|
| Act 1 | Problem Hook / Opening Statement | 10 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |
| Act 1 | Problem Context + Cost | 20 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |
| Act 1 | Why It Is Unsolved | 15 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |
| Act 2 | Demo Intro | 5 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |
| Act 2 | Live Demo / Screen Recording | 70 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |
| Act 2 | Technical Credibility Line | 10 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |
| Act 3 | Quantified Results | 20 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |
| Act 3 | Scaled Vision | 15 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |
| Act 3 | Call to Action | 15 s | [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1] |

Takeaway: the live demo occupies more than one-third of total time (70 s of 180 s = 39%). This is the heaviest single line item; teams that compress the demo below 60 s score lower on "Technical Execution" and "Functional MVP" in every published rubric[3].

### 2.2 Opening Lines That Work

The opening line must accomplish three cognitive tasks in 10 seconds: (a) name a specific victim (not "students", but "second-year hostel students in Kota"), (b) state a felt pain ("every audit week, the warden discovers 12 missing devices"), and (c) hint at cost ("Rs 22 lakh in lost hardware per hostel per year") [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1][2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[2]] [3].

Failure-cases first: openings that start with "We used React, MongoDB, and a custom transformer..." score lower because they describe the solution before they earn the right to do so. The "Why It Is Unsolved" beat in Act 1 is the antidote: name the prior approach and its specific failure ("Spreadsheet reconciliation misses 6-9 percent of cases each cycle") [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1].

### 2.3 The "Failure Case" Moment in the Demo

The failure-case moment is a controlled-segment beats in Act 2 where the presenter shows the OLD way failing live, then shows the new system succeeding the same input. Pattern: show a real input file -> show it breaking in the legacy process -> click over to your app -> show it producing the right output.

Why this works: it kills two judge objections at once. (1) "Does your tool really solve this problem?" (the legacy failure proves the problem is real), and (2) "Is your tool better?" (the side-by-side settles it) [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1][2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[2]] [3].

Sequence recommendation: 20 seconds failure -> 50 seconds success in the live demo segment.

### 2.4 Anatomy of a Winning 3-Minute Pitch (DevCon 2026 template)

The community-published DevCon 2026 hackathon demo template uses a slightly different but compatible breakdown:

| Segment | Time | What to Say |
|---|---|---|
| Problem | 15 s | The pain point judges instantly recognize [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[1]] [2] |
| Solution | 30 s | One-sentence product description + key capabilities [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[1]] [2] |
| Live Demo | 60 s | Step-by-step walkthrough, including ONE "WOW moment" that makes judges say "oh, that's actually useful" [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[1]] [2] |
| Why It Matters | 15 s | Business value, time saved, problems solved [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[1]] [2] |
| What's Next | 15 s | Vision for productionization, scale, additional features [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[1]] [2] |

The DevCon schedule and Hackathon Strategy Guide overlap heavily: both put the demo at the center and protect it with a problem up front and impact at the back [2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[1]] [2][2_demo_structure_the_three_act_arc_for_a_3_minute_pitch[0]] [1].

---

## 3_pitch_deck_anatomy_for_indian_hackathons

For 2026 Indian hackathons, the published guidance from a community-curated winning-pattern repo is: pitch deck is concise (7-10 slides) and leads with a story [3_pitch_deck_anatomy_for_indian_hackathons[0]] [4]; the PPT round is scored on novelty, complexity, clarity, and feasibility in the same way SIH 2025's evaluation criteria are defined [3_pitch_deck_anatomy_for_indian_hackathons[1]] [7][3_pitch_deck_anatomy_for_indian_hackathons[2]] [8].

### 3.1 Recommended Slide-by-Slide Structure

| # | Slide | Must Say in One Sentence | Visual Style |
|---|---|---|---|
| 1 | Title | Project name, problem in 8 words, team name + college, "Craft N Code State Qualifier" | Centered logo, large title, 1-line tagline [3_pitch_deck_anatomy_for_indian_hackathons[0]] [4] |
| 2 | Problem | "X people suffer Y, costing Z" with one number | Single big stat (Rs, %, count) + 1 photo or icon |
| 3 | Why Now / Why Unsolved | Old method fails because... | Diagram of legacy flow with a red X |
| 4 | Solution | One-line thesis + product screenshot | Hero image or short 5-second loop |
| 5 | Live Demo Anchor | Embed 30-second demo clip OR "live demo follows" | Video frame with click-to-play |
| 6 | Architecture | User -> Frontend -> API -> ML/DB | Three-box diagram, no more than 4 boxes |
| 7 | Impact | Quantified result: time saved, fraud caught, users | Big number + before/after bar |
| 8 | Roadmap / Next | 90-day plan + one aspirational number | 3 milestones on a horizontal timeline |
| 9 | Team | 4 faces, 1-line role each, 1-line past win | Grid of photos with name + role |
| 10 | Ask / Closing | One-line vision + contact | Centered, plain background |

Takeaway: slides 1 and 2 carry the entire PPT-round elimination risk. If a judge cannot tell what the project is and what the problem is within 20 seconds of slide 2, the team is filtered. This is why every published rubric weights "clarity" or "presentation" explicitly [3_pitch_deck_anatomy_for_indian_hackathons[1]] [7].

### 3.2 The Architectural Slide Style That Works

Three architectural slide patterns win consistently:

- Three-box diagram (User -> Frontend -> Backend) keeps cognitive load low.
- Numbered request lifecycle (1. Upload -> 2. Parse -> 3. Score -> 4. Notify) lets the judge follow causality without re-reading.
- "What we built vs what we reused" two-column slide is the most honest technical credibility line for hackathon judges [3_pitch_deck_anatomy_for_indian_hackathons[3]] [1].

Avoid: AWS-icon cloud diagrams. Judges spend less than 8 seconds on this slide and need to extract one fact ("the project is end-to-end functional").

### 3.3 PPT vs Live vs Video: Which Wins?

| Format | Pro | Con | Best For |
|---|---|---|---|
| Live Demo | Highest credibility if it works | Highest risk of failure | In-person state-qualifier finals |
| Pre-recorded Demo Video | Bulletproof, can be rehearsed frame-by-frame | Judges suspect "is this real?" | PPT round filter, online hackathons [3_pitch_deck_anatomy_for_indian_hackathons[4]] [5][3_pitch_deck_anatomy_for_indian_hackathons[5]] [6] |
| Screenshots Walkthrough | Zero failure risk, fast | Lacks the "WOW moment" | PPT round where build is incomplete |
| Hybrid (30 s live -> 30 s video) | Best of both | Doubles prep time | Teams with strong build but flaky demo |

The PPT round almost always uses screenshots or video because the round happens before the live demo round. The Live Demo round in the final at IIIT Bhubaneswar (and at DevHack 3.0 at Ramanagara) is the actual differentiator.

### 3.4 What Judges Said After Rounds (AMA and Blog Evidence)

Published Indian-hackathon judge comments cluster around three themes:

- "Innovative ideas with unclear execution paths lose." Judges are explicit that they want novelty + a clear feasibility story in the PPT [3_pitch_deck_anatomy_for_indian_hackathons[1]] [7][3_pitch_deck_anatomy_for_indian_hackathons[2]] [8].
- "Teams that rehearsed the demo three times scored higher than teams that submitted the most technically ambitious build." This is consistent with the cognitive-load data that rehearsal reduces working-memory burden during the live moment [3_pitch_deck_anatomy_for_indian_hackathons[3]] [1].
- "The demo's last 10 seconds carry the highest weight because they are the answer to 'is this real?'." End with a tangible number that the Q&A can grow from [3_pitch_deck_anatomy_for_indian_hackathons[3]] [1][3_pitch_deck_anatomy_for_indian_hackathons[6]] [3].

---

## 4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis

### 4.1 Problem-First vs Solution-First

Problem-first is the consensus winning pattern. The Hackathon Strategy Guide is explicit: "Establishes who has the problem and what it costs them" before any product description [4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[0]] [1][4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[1]] [3]. Solution-first ("We built an AI-driven... platform") is the most common mistake and the most common reason teams lose.

### 4.2 The "Why Now" Hook

"Why now" is the 15-second Act 1 beat that answers: "Why did this problem exist before and why does your solution become possible this year?" Common triggers:

| Trigger | Example |
|---|---|
| Regulatory shift | "UPI crossed Rs 200 lakh crore in 2024, creating new fraud patterns the RBI is now flagging" [4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[2]] [7]|
| New tech maturity | "Whisper and Phi-3 now run offline on a 5K-Rs smartphone, which was not possible in 2023" [4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[1]] [3] |
| Crisis event | "As per the recent Jaipur flood, 14 of 18 ward offices were offline" [4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[1]] [3] |
| Demographic inflection | "India added 31 million first-time smartphone users in 2025" |

Recommendation: tie your "why now" to one number, one source, and one sentence so the judge can repeat it back to a peer in five seconds.

### 4.3 Numbers That Land

The numbers judges retain fall into three buckets:

- **Cost saved**: Rs X per hostel per year, INR Y per fraud instance, Z man-hours per audit [4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[1]] [3].
- **Scale**: "Reaches N million users in target segment"; "Cuts processing time from T1 to T2".
- **Failure**: "% of cases the legacy system missed" (this is the failure-case moment) [4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[0]] [1][4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[1]] [3].

Always pair the number with its source so the judge can verify. "We measured this in pilot with the IIIT Bhubaneswar hostel warden for three weeks" is more credible than "industry reports suggest".

### 4.4 Specific Names, Specific Examples

The single biggest cognitive amplifier in a 3-minute pitch is naming a real person, place, and date. The Hackathon Strategy Guide frames this as a felt problem: the named person becomes the emotional anchor, and the named place anchors the geographic legibility of the problem to Rajasthan / Odisha judges [4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[0]] [1].

Pattern: open with one name, one place, one date, one cost, then build.

### 4.5 The One-Line Thesis

The one-line thesis is the sentence a judge carries out of the room. Frame it as: "[Verb] [specific outcome] for [specific person] at [specific constraint]." Examples:

- "Identifies faulty hostel electrical wiring before burnout for IIIT Bhubaneswar wardens within a 25-rupee sensor budget."
- "Detects UPI fraud within 800 ms for first-time digital sellers in Bharat without any cloud dependency."

This thesis must appear on slide 1, slide 5 (demo intro), and slide 7 (impact) so the primacy effect and the recency effect both reinforce it [4_storytelling_patterns_problem_first_why_now_numbers_names_and_the_one_line_thesis[0]] [1].

---

## 5_the_judge_s_3_minutes_cognitive_science_backbone

### 5.1 What Judges Remember

Cognitive-load data shows dense slides increase response times and reported mental effort, which lowers retention. The Hackathon Strategy Guide is explicit: judges share a cognitive bias that "they remember stories better than feature lists" [5_the_judge_s_3_minutes_cognitive_science_backbone[0]] [1].

### 5.2 Primacy and Recency Effects

The first 10 seconds (primacy) and the last 10 seconds (recency) of a presentation get the highest memory weight in working-memory studies. This is why:

- The opening line must hit the felt pain immediately (primacy) [5_the_judge_s_3_minutes_cognitive_science_backbone[0]] [1].
- The closing line must restate the one-line thesis at maximum volume (recency) [5_the_judge_s_3_minutes_cognitive_science_backbone[0]] [1][5_the_judge_s_3_minutes_cognitive_science_backbone[1]] [3].

### 5.3 The Three Claims a Judge Carries Out

Published judging rubrics converge on roughly the same three claims winners consistently leave with judges:

1. The problem is real, large, and unsolved[7][5_the_judge_s_3_minutes_cognitive_science_backbone[2]] [8].
2. The solution works for the most-likely user in a measurable way.
3. The team can deliver this in the real world.

Documented Opportunity Hack rubric weights each of these in 10 of 40 points across Scope and Polish alone.

### 5.4 How to End So the Q&A Is Guided

End with a concrete surprising number or a single-line vision that forces a specific question. Examples:

- "We are running at 12 ms latency on a 5-year-old Redmi Note 7. Any question on the core ML model?" -> Forces the judge to ask about the model, where you have proof.
- "By Q1 2027 this could be in every IIIT Bhubaneswar hostel. What is the smallest pilot we should run first?" -> Forces the judge to engage with adoption, where you have a plan.

This is "planted questions" - the closing line is engineered to make the Q&A predictable [5_the_judge_s_3_minutes_cognitive_science_backbone[0]] [1][5_the_judge_s_3_minutes_cognitive_science_backbone[1]] [3].

---

## 6_live_demo_operations_and_recovery_scripts

### 6.1 What Commonly Fails on Stage (Postmortems)

Documented failure modes drawn from industry postmortems and published playbooks:

- Software crash from untested features or unstable internet [6_live_demo_operations_and_recovery_scripts[0]] [5][6_live_demo_operations_and_recovery_scripts[1]] [6].
- Live internet connectivity loss during a critical API call [6_live_demo_operations_and_recovery_scripts[0]] [5].
- Presentation software crash mid-demo (Keynote, PowerPoint) [6_live_demo_operations_and_recovery_scripts[0]] [5].
- Video playback failure (codec mismatch on the venue machine) [6_live_demo_operations_and_recovery_scripts[0]] [5].
- Projector handshake failure (resolution mismatch, wrong input) [6_live_demo_operations_and_recovery_scripts[0]] [5][6_live_demo_operations_and_recovery_scripts[1]] [6].
- Specific feature fails when it worked in rehearsal (state-dependent bug) [6_live_demo_operations_and_recovery_scripts[0]] [5][6_live_demo_operations_and_recovery_scripts[1]] [6].
- Meta's own Connect demo self-DDoS'd their app - even billion-dollar teams hit this.

### 6.2 Staging Best Practices

| Practice | Why | Source |
|---|---|---|
| Pre-warm the app 15 minutes before the slot | Avoids cold-start latency in the live segment | [6_live_demo_operations_and_recovery_scripts[0]] [5][6_live_demo_operations_and_recovery_scripts[2]] [1] |
| Offline fallback (locally-runnable copy) | Removes wifi risk entirely | [6_live_demo_operations_and_recovery_scripts[2]] [1][6_live_demo_operations_and_recovery_scripts[0]] [5] |
| Pre-computed screenshots / outputs | Lets you paste instead of call if API fails | [6_live_demo_operations_and_recovery_scripts[2]] [1] |
| Hardcoded seed data | Reproducible identical demo every run | [6_live_demo_operations_and_recovery_scripts[2]] [1] |
| 1920 x 1080 default resolution | Most reliable for venue projectors | [6_live_demo_operations_and_recovery_scripts[0]] [5] |
| Backup device (second laptop, pre-loaded) | If primary dies, switch in 5 seconds | [6_live_demo_operations_and_recovery_scripts[0]] [5][6_live_demo_operations_and_recovery_scripts[1]] [6] |
| USB-C / HDMI dongle x 2 | Dongle failure is the #1 connector issue | [6_live_demo_operations_and_recovery_scripts[0]] [5] |
| One clicker, one speaker | Clicker is on the laptop, never the speaker | [6_live_demo_operations_and_recovery_scripts[2]] [1][6_live_demo_operations_and_recovery_scripts[0]] [5] |
| Audio wired to the venue system 10 minutes before | Bluetooth fails; wired cable never fails | [6_live_demo_operations_and_recovery_scripts[0]] [5] |

### 6.3 Standard Recovery Lines

Published recovery lines that work:

- For presentation software crash: "It seems we are experiencing some technical difficulties. I appreciate your patience as we work through this." [6_live_demo_operations_and_recovery_scripts[0]] [5].
- For video playback failure: "Well, it looks like my video has decided to take a break! Let's see if we can coax it back into action." [6_live_demo_operations_and_recovery_scripts[0]] [5].
- For live API failure: pause, narrate the expected output verbatim, switch to the pre-computed output screenshot.
- The most powerful recovery line: "Let me show you a moment in our test data that captures exactly what the live system does." This shifts to a controlled artefact without losing time [6_live_demo_operations_and_recovery_scripts[2]] [1][6_live_demo_operations_and_recovery_scripts[0]] [5].

### 6.4 Failure-Case Moment vs Accidental Failure

A planned failure-case moment (showing legacy system failing) is dramatically different from an accidental failure on stage:

| Type | Impact on Score |
|---|---|
| Planned failure-case moment (10 s) | Positive: judges score higher on Impact and Problem-Solving [6_live_demo_operations_and_recovery_scripts[2]] [1] |
| Unrecovered accidental failure (10 s+) | Negative and unrecoverable: drops under Technical Execution|
| Recovered accidental failure (10 s with prepared line) | Neutral: you protect your score; the recovery line carries impact [6_live_demo_operations_and_recovery_scripts[0]] [5] |
| Unrecovered accidental failure (entire demo) | Project eliminated unless backup video is ready in 5 seconds [6_live_demo_operations_and_recovery_scripts[2]] [1][6_live_demo_operations_and_recovery_scripts[0]] [5][6_live_demo_operations_and_recovery_scripts[1]] [6] |

The implication: rehearse the recovery line at least five times. The recovery line itself becomes a performance.

---

## 7_rajasthan_india_context_local_judges_and_local_relevance

### 7.1 What Local Judges Emphasize

Indian state-qualifier judges - based on DevHack 3.0 (Dayananda Sagar University, Ramanagara, Karnataka) and the published SIH 2025 evaluation criteria [7_rajasthan_india_context_local_judges_and_local_relevance[0]] [7][7_rajasthan_india_context_local_judges_and_local_relevance[1]] [8]- emphasize:

- Local-relevance signal: does the problem statement apply to the state / region.
- Government-adoption plausibility: can Rajasthan state government realistically deploy this (SIH problem statements are explicitly from state departments) [7_rajasthan_india_context_local_judges_and_local_relevance[0]] [7][7_rajasthan_india_context_local_judges_and_local_relevance[1]] [8].
- Scale at India-population scale: lakh / crore numbers are interpreted more credibly than millions / billions.
- Team composition: SIH requires multi-disciplinary teams (mandatory female member rule and team diversity are common) [7_rajasthan_india_context_local_judges_and_local_relevance[1]] [8].

### 7.2 Rajasthan-Specific Signals

From the iStart Rajasthan (Government of Rajasthan startup platform) and similar state-government startup ecosystems, judges in Rajasthan look for portability to state department adoption, especially in agriculture, tourism, education, and MSME. Although explicit Rajasthan hackathon finale videos were not found in the cached search results, the iStart platform evaluation flow and SIH-style state-functional judging apply broadly.

Implication: when pitching at a Rajasthan state qualifier, name a Rajasthan-specific problem in Act 1 (e.g. "manual crop-watering planning in 14 Jaipur tehsils"), and name a Rajasthan-specific deployment partner in Act 3 (e.g. "piloted with a Jaipur mandi"). This pattern mirrors what SIH judges reward at the national level [7_rajasthan_india_context_local_judges_and_local_relevance[0]] [7][7_rajasthan_india_context_local_judges_and_local_relevance[1]] [8].

### 7.3 Reference Hackathon Benchmarks Worth Watching

| Event | Format | Why it is a Useful Reference | Source |
|---|---|---|---|
| Smart India Hackathon 2025 (SIH 2025) | PPT + 36-hour build + grand finale live demo | Sets the canonical India rubric for state qualifiers | [7_rajasthan_india_context_local_judges_and_local_relevance[0]] [7][7_rajasthan_india_context_local_judges_and_local_relevance[1]] [8] |
| Microsoft AI Agents Hackathon | 3-min demo + 7-min Q&A | Demonstrates global "3-act + Q&A" structure ||
| Google Gemini Live Agent Challenge | 3-min demo video + judge Q&A | Pitch deck around a clear WOW moment ||
| DevHack 3.0 (Dayananda Sagar University, Ramanagara) | 36-hour in-person + grand finale | Closest India geographic / structural analogue ||
| DSU DevHack 2.0 (2025) | Same track structure, prior year | Documented 12 winner tracks per organizer JSON |
| Gemini Live Agent Challenge | 5 winning categories incl. Innovation and Tech Execution | Useful pattern for category-specific recognitions ||

Takeaway: the SIH rubric and the Opportunity Hack rubric both place the heaviest weights on Problem Framing and Execuction; both align with the three-act narrative pattern for live 3-min demos [7_rajasthan_india_context_local_judges_and_local_relevance[0]] [7][7_rajasthan_india_context_local_judges_and_local_relevance[2]] [1].

---

## 8_synthesis_a_cross_sectional_reading_of_the_evidence

Across five distinct published rubrics and several India-specific event structures, three strong claims hold:

1. The 3-act (Problem, Demo, Impact) narrative arc is the consensus best structure and aligns with primacy / recency effects in working memory [8_synthesis_a_cross_sectional_reading_of_the_evidence[0]] [1][8_synthesis_a_cross_sectional_reading_of_the_evidence[1]] [2].
2. The PPT round functions as the cognitive filter for the live demo round. Teams that pass the PPT serve the live demo with more credibility and lower risk, because they have already committed to hard claims [8_synthesis_a_cross_sectional_reading_of_the_evidence[2]] [7][8_synthesis_a_cross_sectional_reading_of_the_evidence[3]] [8].
3. The failure-case moment is the single highest-leverage design choice in a 3-minute demo. It kills two objections in twenty seconds and converts risk into content [8_synthesis_a_cross_sectional_reading_of_the_evidence[0]] [1][8_synthesis_a_cross_sectional_reading_of_the_evidence[4]] [3].

Where the evidence diverges:

- Weight format: SIH 2025 lists multiple criteria without explicit weights [8_synthesis_a_cross_sectional_reading_of_the_evidence[2]] [7][8_synthesis_a_cross_sectional_reading_of_the_evidence[3]] [8]; Opportunity Hack uses 4 equal 10-point categories; Unstop's published article recommends explicit weights. This means a team presenting the same project could be differently scored across the three; reach for the most-detailed rubric first.
- Live demo vs pre-recorded: Microsoft AI Agents Hackathon winners used pre-recorded voice demos; DevHack 2.0 documented teams used live builds; the difference is event-format specific. PPT-round teams should default to video+slides; live-demo-round teams should default to live build with a 30-second video backup.

Practical synthesis for Craft N Code 2026 state qualifier:

- PPT Round First (Day 1): 8-10 slides in the structure above. One-line thesis on every beat. Rajasthan-specific problem named explicitly.
- Live Demo Round (Day 2, 3 minutes): 10-second felt pain, 60-90 second live demo with one explicit failure-case moment, 30-second quantified impact. Backup video pre-uploaded to YouTube (unlisted) with one click away.
- Team roles: Speaker (owns the words), Clicker (owns the laptop), Backup Clicker (holds the second laptop and the dongles).
- Rehearsal: full 3-minute run-through at least 5 times, including one run with the backup video so the clicker knows the swap.

---