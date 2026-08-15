# Win the Room: A 24-Hour Hackathon Video Playbook

This playbook treats the event facts in your brief as authoritative: a 24-hour build, a 3-minute sponsor-judge demo, a pre-recorded backup, a 50MB submission constraint, and only the top two teams advancing. I did not find a matching public official Craft N Code page that independently confirms every one of those details, so check the organizer's latest instructions before export day.

## Executive Summary

- **Clarity Beats Coverage**: YC's pitch guidance says to start with the problem rather than the technology, be clear, and accept that a short pitch cannot say everything [27] -> Pick one user, one failure, one workflow, and one measurable outcome.
- **Proof Must Arrive Early**: YC describes a two-minute company-plus-build window, while MLH recommends that a submitted video be a demo of the hack rather than a presentation [27][25] -> Put the real product on screen before the halfway point and keep slides to title cards.
- **Judges Reward Legible Decisions**: Devpost's judging interface rates each criterion from 1 to 5 stars, and MLH's process gives judges only a strict three-minute team slot with questions [23][25] -> Make every criterion visible in a short, labeled proof moment.
- **A $4,500 Film Can Outperform a Bigger Production**: Dollar Shave Club filmed its founder in a warehouse for about $4,500; the video crashed its server and was followed by 12,000 orders in 48 hours [26] -> Spend zero-budget effort on a sharp idea, a memorable human voice, and a clean ask, not stock footage.
- **A Demo Can Sell the Future, But It Must Be Labeled**: Dropbox's four-minute early demo used screen recordings and mockups even though the product was not fully built, and the reported waitlist rose from about 5,000 to 75,000 overnight [10] -> Use a pre-recorded path for reliability, but disclose mocks, fixtures, simulated APIs, and unfinished components when asked.
- **Audio Is a Production Multiplier**: Poor audio mix, improper pacing, out-of-sync audio, jump cuts, and tacky transitions are all listed as editing failure modes [12] -> Record narration first, mix it clearly, and only then polish color and motion.
- **The Free Stack Is Sufficient If It Is Narrow**: OBS is free and open source on Windows, Mac, and Linux and can combine window captures, text, browser windows, and cameras [8]; Kdenlive is free and open source with titles, subtitles, speech-to-text, effects, and export [29] -> Choose one editor, one recorder, and one encoder; do not learn five applications during the build.
- **A 50MB Cap Is an Engineering Constraint**: For a 90-second file, 50MB permits about 4.44 Mb/s average total bitrate; leaving 10 percent headroom gives about 4.0 Mb/s before audio. For a 3-minute file, the corresponding headroom target is about 2.0 Mb/s -> Export a readable 720p H.264 MP4, calculate bitrate before rendering, and test the actual file.
- **Live Truth Beats Cinematic Implication**: MLH says judges can ask questions for clarification [25], and its rules require code links, framework disclosure, AI disclosure, and tool credits [1] -> Prepare a one-sentence truth statement for every impressive shot before you press record.

## 1. What Startup Launch Films Compress Into 60-90 Seconds

### The structure: hook, failure, reveal, proof, ask

There is no single industry-standard duration in the evidence collected. The useful public comparison points are a YC Demo Day pitch with two minutes for the company and the build [27] and Dropbox's early product video, which ran four minutes [10]. A **60-90 second trailer** is therefore a deliberate compression target for this hackathon, not a claim that every funded startup uses that length.

Use this six-beat structure:

| Beat | Trailer time | What the viewer must understand | Visual treatment | Audio and text |
|---|---:|---|---|---|
| Cold open | 0:00-0:05 | Something is failing, urgent, or surprisingly expensive | A fast failure shot, human reaction, or alarming result | One spoken line and one short caption |
| Problem | 0:05-0:15 | Who has the problem and what the current workaround costs | Real person, real input, or a before-state screen | Voiceover states the pain; caption repeats only the key noun |
| Product reveal | 0:15-0:25 | What your product is in one sentence | Logo or title card resolves into the real interface | Say the product promise; avoid feature lists |
| Core workflow | 0:25-0:50 | The shortest path from input to useful outcome | Three to five clean UI actions, cut tightly | Narration explains why each action matters |
| Proof and differentiator | 0:50-1:10 | Why this is more than a mockup or generic chatbot | One output, one architecture detail, one user quote, or one real number | Show the evidence beside the product, not in a separate slide |
| Ask and recall | 1:10-1:30 | What the team wants the viewer to remember or do | Product end-state, team name, QR or URL | One CTA and a final sound hit; do not add a second ask |

The structure adapts YC's advice to start with the problem, make the idea legible, and avoid trying to say everything in a short pitch [27]. It also follows the YC deck sequence of one-line description, problem, solution, concrete benefits, traction, team, and ask [4]. In a trailer, traction may be a real test result rather than revenue; never replace an unavailable metric with a made-up one.

### Pacing, captions, voiceover, and editing style

Use a faster rhythm at the beginning and a slower rhythm when the audience must read or verify the product. A practical edit has **2-3 seconds** for a hook shot, **4-8 seconds** for a readable interface action, and a longer **8-12 second** hold for the final proof or number. These are production recommendations, not measured industry norms. If the screen is dense, let the shot run longer and remove words rather than speeding the viewer past the evidence.

Use **voiceover plus selective text**, not voiceover or text as mutually exclusive choices. Voiceover supplies causality: why the user is stuck, why the next action matters, and what the result changes. On-screen captions protect the demo when the room is noisy, the playback is muted, or a judge is looking at the screen rather than the speaker. Caption the problem, product promise, action labels, and final number; do not transcribe every sentence into a wall of text.

A startup-style edit is usually controlled, not effects-heavy. Use hard cuts, match cuts, short UI zooms, deliberate cursor movement, a restrained color palette, and one recurring transition motif. Avoid transitions that announce the editor. The failure list from Videomaker is a useful negative checklist: poor audio mix, improper pacing, incomplete transitions, jump cuts and match frames, ghost frames, out-of-sync audio, tacky transitions, and staggered outs [12].

### Case study: Dollar Shave Club made the constraint memorable

The Dollar Shave Club video was filmed in the original Gardena warehouse in October 2011 and cost about **$4,500**. It featured founder Michael Dubin walking through the warehouse, using off-color jokes and a direct subscription offer for razor blades priced as low as $2 per month [26]. The video was not trying to look like a luxury commercial. Its production value came from a specific voice, a physical location that made the business tangible, and a product promise that could be understood immediately.

The business result shows why the mechanism matters. The video attracted nearly 10 million views in the account captured by the source, crashed the company's server in its first hour, and was followed by **12,000 orders in the first 48 hours** [26]. The source also says the humor helped it appeal to mainstream media [26]. The lesson for a student team is not to imitate the jokes. It is to make the product's point of view unmistakable and use the real team or real environment as an asset.

### Case study: Dropbox proved the future with a controlled demo

Dropbox's early demo is a stronger model for software. The account says the team made a **four-minute** video using screen recordings and carefully constructed mockups, keeping it clear, technical, and direct around a real pain point [10]. The product shown was not fully built; the video functioned as an MVP by demonstrating what Dropbox would do rather than presenting a complete working system [10].

That approach reportedly moved the beta waitlist from around **5,000** users, with a goal of 15,000, to **75,000 signups overnight** after distribution on Hacker News and Digg in late 2007 or early 2008 [10]. It worked because the video made an invisible technical product concrete. It also creates the ethical boundary for your trailer: mockups can explain an intended flow, but the narration and README must say what is live, local, mocked, or planned.

### YC and crowdfunding-style framing

YC's Kevin Hale describes the goal of a short pitch as getting people to want a conversation, not listing every good thing about the company [27]. That is the correct trailer CTA for a hackathon: remember the team, remember the problem, and make the judge want to see the live path.

The retrieved Kickstarter Creator Handbook page was only an index linking to sections on funding, storytelling, promotion, rewards, and communication; it did not expose specific video advice [17]. Do not attribute a precise creator-presence or campaign-video rule to Kickstarter from that page. You can still borrow the crowdfunding pattern as a creative choice: show a human need, show the object or workflow, state the ask, and label any proof honestly.

**Decision:** Make the trailer a 75-second story with one problem, one real workflow, one proof moment, and one CTA. If you cannot state the proof truthfully, replace the cinematic claim with a transparent build-status card.

## 2. The Three-Minute Judge-First Demo

### What the evidence says judges actually see

MLH recommends a **2-minute submitted video** and explicitly says the video should be a demo of the hack, not a presentation [25]. Its organizer guide also describes a strict **3-minute** team slot and notes that judges can ask questions for clarification [25]. That is close to your stated format and supports a demo-first design: title cards are useful only when they move the judge into the product.

Devpost's judging workflow gives judges a criteria dashboard, a 1-5 star rating for each criterion, and no other feedback mechanism in the described interface [23]. Your organizer's rubric may differ, but the practical implication is stable: a judge must be able to map your video to criteria without reconstructing the story from scattered hints.

YC supplies the narrative discipline. It says to start with the problem rather than the technology [27], keep the idea clear [27], and accept that a short pitch cannot include everything [27]. YC's deck template adds problem, solution, concrete benefits, traction, team fit, and ask [4]. Translate those into visible demo moments rather than seven slides.

### The 3:00 beat sheet

| Time | Beat | Exact job | What to show | Narration template |
|---|---|---|---|---|
| 0:00-0:07 | Failure in seconds | Make the pain undeniable before context | The old workflow fails, a user waits, or an important result is missing | "This is what happens today when [user] tries to [job]." |
| 0:07-0:20 | User and promise | Define one audience and one change | User label, problem caption, product name | "We built [product] so [user] can [outcome] without [old pain]." |
| 0:20-0:35 | Before path | Establish a fair comparison | Two or three steps of the current or naive approach | "The failure is not theoretical; the old path loses [real cost or step]." |
| 0:35-1:25 | Real fix | Prove the core workflow works | Live or locally reliable input-to-output path | "Now we send the same input through [product]. Watch [specific state change]." |
| 1:25-1:55 | Killer feature | Show the one surprising advantage | One differentiating feature, not a tour | "The reason this is different is [mechanism], which lets us [benefit]." |
| 1:55-2:20 | Proof | Earn belief | One actual test, latency, count, accuracy result, or user action | "In our test, [number] means [plain-language interpretation]." |
| 2:20-2:40 | Build and sponsor relevance | Demonstrate technical ownership and usefulness | Architecture overlay, integrations, or deployment view | "We built [components] during the event; the next scale step is [honest limitation]." |
| 2:40-2:55 | Risk and next step | Answer the first objection before it is asked | Limitation card and mitigation | "Today it depends on [constraint]. We handle that next by [plan]." |
| 2:55-3:00 | One-number close | Leave one retrievable fact | Product end-state and a single number | "[Product] turns [before] into [after]. The number to remember is [real number]." |

The most important design choice is the ordering of **failure -> fix**. If the audience sees a polished dashboard first, it cannot tell whether the product solved anything. If it sees the failed state first, the transformation becomes evidence. The number at the end should be a real number from the build or test: seconds saved, successful runs, records processed, response time, or a measured user action. A number without a denominator or test condition is decoration.

### Judge-mapping checklist

| Likely judging dimension | Proof moment | Failure pattern | Fix |
|---|---|---|---|
| Problem and impact | 0:00-0:35 | Broad social claim with no user or failed task | Name one user and show one failure |
| Innovation | 1:25-1:55 | A generic feature list | Explain the mechanism that makes the feature different |
| Technical implementation | 0:35-1:25 and 2:20-2:40 | Architecture slide with no working path | Let the judge see the result, then briefly show ownership |
| Usability and design | Every UI shot | Tiny text, uncontrolled cursor, too many clicks | Use a clean seeded state and one action per cut |
| Impact or sponsor fit | 1:55-2:20 | Unmeasured adjectives such as "huge" | Show one real number and define what it measures |
| Presentation | Whole three minutes | Reading slides, long setup, dead air | Rehearse to 2:45, leaving 15 seconds of safety |
| Credibility | 2:40-2:55 and Q&A | Calling mock data live | Label fixtures, APIs, and limitations |

This is a preparation matrix, not a claim about the undisclosed Craft N Code rubric. Devpost's documented 1-5 rating mechanism makes the reason for the matrix clear: if a criterion is not evidenced, a judge must guess how to score it [23]. MLH's demo-not-presentation rule reinforces the same conclusion [25].

### Hackathon-winner evidence boundary

The retrieved search produced organizer guidance and a public AI hackathon workshop, but it did not expose a sufficiently detailed, named winner transcript that would support a line-by-line winner teardown. I will not invent a winning project's timing or claim that a particular winner used this exact beat sheet. Instead, use the Dropbox case as the concrete proof-over-polish software analogue and use the following teardown method on any winner video you locate: record the first visible problem time, first product time, first successful output time, number of features shown, number of proof metrics, and the last sentence. Then compare those measurements to the table above.

**Decision:** Script a 2:45 run, not a 3:00 run, and make the first successful end-to-end result land by 1:25. A judge should be able to score problem, working product, differentiation, impact, and credibility without pausing the video.

## 3. The 24-Hour Zero-Budget Production System

### Tool selection matrix

| Task | Primary choice | Fallback | Verified capability or caveat | Cost and time budget |
|---|---|---|---|---:|
| Screen capture on Windows, Mac, Linux | OBS Studio | Built-in OS recorder | OBS is free/open source, supports Windows 10/11, macOS 12+, Linux, multiple scenes, window captures, text, browser windows, webcams, and capture cards [8] | $0; 20-40 minutes to configure |
| Wayland Linux capture | wf-recorder | OBS | wf-recorder is an MIT-licensed utility for wlroots-based compositors and can record screen and audio to MP4 [22] | $0; 15-30 minutes if already on Wayland |
| Full edit, color, audio, motion | DaVinci Resolve free | Kdenlive | The official page describes Resolve as an all-in-one editor, color, VFX, motion-graphics, and audio tool; its free version supports 8-bit formats up to 60fps and up to Ultra HD 3840 x 2160 [3] | $0; 60-90 minutes to learn a narrow workflow |
| Fast open-source edit | Kdenlive | Shotcut if already installed | Kdenlive's manual identifies it as free/open source and includes effects, filters, titles, subtitles, speech-to-text, and export [29] | $0; 30-60 minutes to build a rough cut |
| Transcode and compress | FFmpeg | HandBrake if available | FFmpeg describes itself as a cross-platform solution to record, convert, and stream audio and video [18] | $0; 15-30 minutes to test one command |
| Browser/mobile fast edit | CapCut | Your chosen desktop editor | Treat plan, caption, cloud, and watermark behavior as account- and region-dependent. The captured official comparison exposed free-tier limitations, so render a five-second test before committing. | $0 if the required feature is available; otherwise abandon it |
| Local voiceover | Real team voice | Piper, if already installed | Piper is described as a fast, local neural text-to-speech system [11]. A real team voice usually sounds more credible and avoids model-license and pronunciation surprises. | $0; 30-60 minutes including retakes |
| Local captions or transcription | Editor speech-to-text | Whisper only if preinstalled and tested | Do not make a new AI install a critical dependency inside the 24-hour window. Check language, accuracy, render, and license before using generated captions. | $0; 20-45 minutes |
| Noise cleanup | Audacity | Adobe Podcast Enhance Speech if internet is reliable | Audacity is free and open source; use it for cleanup and re-recording rather than trying to rescue a badly clipped take [20] | $0; 20-40 minutes |
| Music and sound effects | YouTube Audio Library track page | Self-recorded room tone, clicks, or a simple original pad | Use a track whose current license and attribution instructions are visible, save the license text, and credit it in the README. The official Audio Library page is the safer starting point than a random "no copyright" upload [6]. | $0; 15-30 minutes |
| Motion graphics | Resolve titles and Fusion or Kdenlive titles | Simple PNG/SVG title cards | Resolve's official page includes motion graphics in the all-in-one description [3]; do not learn After Effects or a complex 3D package during the build. | $0; 30-60 minutes |

The table separates **verified capability** from **must-test behavior**. The captured official Resolve material did not state a watermark or export restriction, so do not promise that to a sponsor judge from memory; render a short test on the exact machine. Likewise, a cloud editor or AI enhancer can fail because of login, network, region, queue, or plan changes. Offline capture, local project files, and a human narration take priority.

### Realistic tool time budgets

| Stage | Time | Technique | Tool | Cost |
|---|---:|---|---|---:|
| Lock story | 0:30 | Write trailer and demo beats before opening the editor | Paper, shared document | $0 |
| Capture setup | 0:30 | Test resolution, cursor visibility, microphone, and audio channels | OBS or wf-recorder | $0 |
| Seed the product | 0:45 | Create deterministic account, sample data, and a reset button or reset script | Product code | $0 |
| Record clean UI | 1:00 | Capture three complete runs, then isolated feature shots | OBS or wf-recorder | $0 |
| Record narration | 0:45 | Record three takes in a quiet room, one sentence per take | Phone, Audacity | $0 |
| Rough demo edit | 1:30 | Place failure, fix, feature, proof, close; ignore color | Resolve or Kdenlive | $0 |
| Rough trailer edit | 2:00 | Select best shots, add title cards, music, captions, and logo | Resolve or Kdenlive | $0 |
| Audio and captions | 1:00 | Remove noise, level voice, duck music, proofread captions | Audacity plus editor | $0 |
| Compression and checks | 0:45 | Export, measure file size, test playback, upload backup | FFmpeg or HandBrake plus YouTube | $0 |
| Rehearsal | 1:30 | Five full runs, two with a deliberate failure and recovery | Live build plus video fallback | $0 |

### The 24-hour operating plan

| Hackathon clock | Build and video action | Owner | Gate to pass |
|---|---|---|---|
| 0:00-0:45 | Choose the single user, failure, promise, killer feature, and proof number | Product lead plus whole team | A five-sentence script exists |
| 0:45-2:00 | Build the stable skeleton and create seeded data; record the baseline failure immediately | Builder plus capture owner | The failure and target output are recorded |
| 2:00-10:00 | Build only the end-to-end path that the demo will show | Builders | A local or deployed path works twice in a row |
| 10:00-12:00 | Freeze the hero path; add the differentiator only if it cannot break the hero path | Technical lead | A known-good commit or build is tagged |
| 12:00-14:00 | Capture clean UI, close-ups, team shot, logo, and architecture still | Capture owner | Three full runs and isolated shots are stored locally |
| 14:00-16:00 | Record narration and assemble the 3-minute rough cut | Narrator plus editor | A silent viewer can follow the visual order |
| 16:00-18:30 | Assemble the 60-90 second trailer and add captions | Editor | Trailer tells one story without a feature dump |
| 18:30-19:30 | Audio mix, color, titles, and proofread; stop adding features | Editor plus product lead | Voice is intelligible on phone speakers |
| 19:30-20:30 | Export 50MB submission, high-quality master, and backup video | Encoder owner | Each file opens and has correct duration |
| 20:30-22:00 | Rehearse live demo, including unplugged network and failed API scenarios | Presenter plus technical lead | Presenter can finish under 2:45 |
| 22:00-23:00 | Upload unlisted backup, create deck/README links, and copy files to two devices | Release owner | A second person can open every link |
| 23:00-24:00 | Rest, final smoke test, and prepare truthful Q&A | Whole team | No unexplained claim remains on screen |

The most important scheduling rule is to record a usable hero path before polishing. If the build is late, the trailer becomes a clean explanation of the real state and the demo becomes a pre-recorded, deterministic run. Do not spend the last two hours re-rendering a title card while the product has no known-good commit.

**Decision:** Use OBS plus Resolve if one teammate already knows Resolve; otherwise use OBS plus Kdenlive. Make FFmpeg the delivery fallback, not the primary editor, and make local files the primary backup.

## 4. Screen Recording Versus Cinematic Hybrid

### Use real product footage for trust and stylized footage for emotion

A screen recording proves interaction, state change, and output. A cinematic shot proves mood, urgency, team identity, or physical context. A hybrid trailer uses both but assigns each a job: stylized footage earns attention in the first seconds and at transitions; real product footage carries the claim that judges must verify.

| Element | Indie-looking failure pattern | Produced-looking winning pattern | Fix in one sentence |
|---|---|---|---|
| Opening | Logo animation before the audience knows the problem | Failure or human consequence in the first shot | Start with the bad state, then identify the product |
| UI capture | Tiny text, browser tabs, notifications, uncontrolled cursor | Seeded data, large type, clean viewport, deliberate cursor | Design the capture frame before recording |
| Cursor | Wanders, circles, and clicks twice | Moves once to the target and stops | Use one click per edit and add a subtle highlight only when needed |
| Pacing | Long loading screens and dead air | Cut to the state change, then hold the result | Record the wait separately and remove it unless latency is the proof |
| Transitions | Every clip has a different spin, zoom, or glitch | Hard cuts and one consistent transition language | Spend motion budget on the product state, not decoration |
| Audio | Phone echo, music louder than speech, clipped words | Dry intelligible voice, low music bed, purposeful sound hits | Mix voice before music and test on a phone |
| Proof | Stock photos or an impressive dashboard with no action | Same input shown before and after the product | Use one reproducible input and one measurable output |
| Ending | Team names, social links, and several asks | Product, one number, team, one next step | End on one memory hook |

Videomaker's failure list directly supports the audio, pacing, sync, and transition checks in this comparison [12]. A product-video methods comparison also distinguishes basic screen recording from more cinematic and animated methods across speed, cost, engagement, professionalism, and ease of updates, while warning that AI-assisted production is not always the right fit [16]. For a 24-hour event, the hybrid is the rational middle: enough polish to establish attention, enough real footage to establish credibility.

### How to make a dark UI look cinematic without filming a monitor

1. Capture the interface digitally at the target resolution. Do not point a phone at a monitor unless a physical interaction is itself part of the story; camera footage introduces glare, moire, reflections, and unstable exposure.
2. Use a clean browser profile or app window. Hide bookmarks, notifications, unrelated tabs, developer tools, and personal data.
3. Increase type and contrast before recording. A dark UI needs a bright focal element, not a uniformly black canvas. Make the result card, status change, or primary button the brightest controlled accent.
4. Seed the exact data used in the script. Reset the state after every take. A deterministic demo is more cinematic than a beautiful interface that stalls.
5. Record separate clips: full workflow, input close-up, processing state, result close-up, and an optional architecture or code still. This lets the edit use a close-up without pretending the whole UI is that large.
6. Use slow, intentional cursor movement. A cursor is the actor in a screen recording; it should enter, point, click, and leave with purpose.
7. Add a restrained simulated camera move in the editor: a 2-5 percent scale or position change around the important result. Never zoom so far that text becomes soft.
8. Use a short room-tone or interface sound at the reveal, but keep the narration dominant. The product state, not the effect, is the emotional payoff.

### A shot list that can be captured in one hour

| Shot | Duration in final | Capture method | Why it exists |
|---|---:|---|---|
| Failure close-up | 2-4 seconds | Screen capture or phone on the human | Establishes the before state |
| Human problem shot | 3-5 seconds | Phone, window light, stable frame | Adds empathy and makes the team memorable |
| Product reveal | 2 seconds | Logo/title card over product | Names the solution |
| Full hero run | 20-35 seconds | Screen capture with narration added later | Proves the workflow |
| Killer-feature close-up | 5-8 seconds | Isolated screen capture | Gives the judge one differentiator |
| Proof result | 5-10 seconds | Same input and measurable output | Prevents vague claims |
| Team or build shot | 3-5 seconds | Phone or still image | Shows ownership and human effort |
| End card | 3-5 seconds | Static design | Leaves one CTA and number |

**Decision:** The live demo should be approximately 80 percent real product footage and 20 percent title, human, architecture, or transition material. The trailer can be more cinematic, but every promise in it must have a corresponding real shot or explicit status label.

## 5. Audio That Makes a Student Build Sound Real

### Phone and cheap-mic workflow

A phone in a quiet, soft room is usually a better zero-budget narration source than a cheap microphone placed in a reflective classroom. Put the phone on a stable surface, keep the speaker a consistent hand-span away, turn off fans and notifications, record three takes, and clap once at the start of each take so the editor can find the audio. Record one sentence per take rather than trying to deliver a perfect 90-second paragraph.

Use a wardrobe room, curtained corner, parked car, or room with books and fabric to reduce reflections. Do not record directly beside a laptop fan. Speak slightly off-axis to reduce breath blasts, leave a short pause before and after each sentence, and keep the same distance for every take. If the voice clips, re-record; noise reduction cannot repair distorted peaks.

Audacity is free and open source and can be used for cleanup [20]. A disciplined cleanup chain is: trim obvious silence, reduce steady noise cautiously, high-pass low rumble, apply light compression, normalize or limit, then listen on phone speakers. Adobe Podcast or another browser enhancer can be a convenience if the connection works, but it should be treated as optional because a cloud dependency can fail at the worst time.

### Music and mix

Use music as an emotional floor, not as a second narrator. Pick one track with a clear current license, download the license or attribution text, and put the credit in the README and deck notes. YouTube's Audio Library is an appropriate first place to inspect; use the track's own current instructions rather than relying on the phrase "no copyright" in a re-upload title [6]. If the exact license does not clearly cover the submission, deck, unlisted upload, and public README, choose another track or make a simple original bed.

Start with the voice completely dry and intelligible. Then bring the music up until it is felt but not parsed. As practical starting targets, keep voice peaks below clipping, place music substantially below the narration, and listen once on laptop speakers and once on a phone. Sound effects should mark only the product reveal, successful output, or final card. Silence is acceptable for a short problem beat; a silent three-minute demo with no narration or intentional sound leaves judges to infer why each click matters.

The editing failure checklist explicitly includes poor audio mix and out-of-sync audio [12]. YC's instruction that the presenter should be clear and make the idea legible gives the communication reason to prioritize voice [27].

**Decision:** Record a human voiceover, caption the key lines, use one low music bed, and reserve sound effects for three moments or fewer. If the voice is not intelligible on a phone, the mix is not finished.

## 6. Delivery Under 50MB and the Backup Chain

### Recommended deliverables

| Deliverable | Recommended spec | Purpose | Check |
|---|---|---|---|
| Submission MP4 | MP4 container, H.264 video, AAC audio, 1280x720, 24 or 30fps | Fits a strict size cap while keeping UI readable | Open on a second computer and phone |
| High-quality master | MP4 or editor archive at the native capture resolution | Re-export if the organizer changes the cap or asks for a higher-quality link | Keep on two physical devices |
| Unlisted backup | Same 3-minute demo uploaded as unlisted | Recovery if the live build, HDMI, or local file fails | Test from a logged-out or second account |
| Trailer | 60-90 seconds, separate file and URL | Startup-style impression and README/deck asset | Verify captions, end card, and music credit |
| Deck asset | Linked thumbnail or local MP4, not a fragile embedded stream | Sponsor presentation | Test with venue internet disabled |
| README asset | Thumbnail linking to YouTube plus a direct file link if permitted | Reproducibility and judge convenience | Check access permissions and mobile behavior |

FFmpeg officially presents itself as a cross-platform solution to record, convert, and stream audio and video [18]. YouTube documents that a video or playlist can be embedded in a website or blog [9]. GitHub's attachment documentation says uploaded files in public repositories can be accessed without authentication, but the page is about attaching files to issues and pull requests rather than promising a raw video player inside every README [32]. Therefore, the safest README pattern is a thumbnail image linked to an unlisted YouTube URL, plus a clear `How to run` section and a downloadable file only if repository policy and size permit.

### Bitrate math for the 50MB cap

Use headroom. A nominal 50MB file can be rejected because container metadata, audio, or rounding pushes it over the limit. Target **45MB** instead.

| Duration | 45MB total bitrate | Reserve for AAC audio | Approximate video bitrate |
|---:|---:|---:|---:|
| 60 seconds | 6.00 Mb/s | 96 kb/s | 5.90 Mb/s |
| 90 seconds | 4.00 Mb/s | 96 kb/s | 3.90 Mb/s |
| 180 seconds | 2.00 Mb/s | 96 kb/s | 1.90 Mb/s |

The calculation is `target megabytes x 8 / seconds = average megabits per second`. The values are engineering arithmetic, not a promise of visual quality. If text is unreadable at 720p, remove decorative shots and increase the UI scale before increasing bitrate. If a 3-minute file still exceeds 45MB, lower frame rate only after testing motion, then lower video bitrate, then simplify the edit. Do not make a dark UI smaller to preserve a logo animation.

A practical FFmpeg pattern for a 90-second submission is a two-pass H.264 encode near 3,900 kb/s video plus 96 kb/s AAC audio, with `+faststart` for web playback. Use `NUL` instead of `/dev/null` on Windows. The exact command should be tested on the team's machine; the important part is a target bitrate and a measured final file, not a copied preset.

Example shape:

```bash
ffmpeg -i master.mp4 -c:v libx264 -b:v 3900k -pass 1 -an -f mp4 /dev/null
ffmpeg -i master.mp4 -c:v libx264 -b:v 3900k -pass 2 -c:a aac -b:a 96k -movflags +faststart submission.mp4
```

For a 3-minute version, start near 1,900 kb/s video and test. If the organizer requires a different definition of MB, leave more headroom. Always inspect the actual file size, duration, frame size, audio presence, and first and last frames after encoding.

### Hosting and embedding chain

1. Keep `submission_720p.mp4`, `master.mp4`, captions, music license, and README in a release folder.
2. Upload the demo to YouTube as unlisted and copy the URL into the deck and README. Use the official embed mechanism when a site or deck supports it [9].
3. Make a local deck copy with a poster frame and a clickable URL. If the venue has poor internet, carry the MP4 and use the local file.
4. Put a thumbnail in the README with a plain link. Add runtime, build status, tech stack, demo credentials, known limitations, and a note distinguishing live, recorded, and mocked elements.
5. Give a teammate a second device or drive containing the local files. Test the links from an account that is not the uploader.
6. Never make the live demo depend on the unlisted URL. It is the backup, not the only copy.

**Decision:** Submit a 45MB-targeted 720p MP4, keep a higher-quality master, upload an unlisted backup, and put a thumbnail plus link in the README and deck. Verify every route offline and online before leaving the build room.

## 7. Rehearsal, Live Reliability, and Sponsor-Judge Q&A

### Five-run rehearsal protocol

| Run | Condition | What to measure | Pass condition |
|---:|---|---|---|
| 1 | Normal network and full build | Total time and unclear sentences | Finish under 2:45 |
| 2 | Presenter alone | Whether narration explains every click | No unexplained action |
| 3 | Network disabled | Local data, cached assets, and fallback | Hero path still completes or video starts immediately |
| 4 | Deliberate product failure | Recovery sentence and backup trigger | Presenter does not improvise a false claim |
| 5 | Judge interruption | One question after each beat | Presenter returns to the next beat without restarting |

MLH's organizer guidance says judges can ask questions for clarification [25]. Treat questions as part of the product experience, not an interruption. The presenter should know the actual data source, which model or API is used, what is mocked, where the code lives, and what the current limitation is.

The live runbook should have three modes:

- **Green:** Live hero path, with a second teammate watching logs and ready to reset the seeded state.
- **Yellow:** Pre-recorded demo played with live narration or a short explanation of what is being shown. Say that it is the recorded backup if asked.
- **Red:** Trailer or a short proof clip, followed by the README and a direct local run if the format permits. Never pretend a trailer proves a live system.

MLH's rules also provide a useful submission discipline: submit code as a publicly available link, list frameworks in the README, state how AI was used, credit tools, and be clear about what the team made versus what was generated [1]. Even if Craft N Code uses a different platform, adopting that standard makes sponsor questions easier.

### The 20-second answer format

When a judge asks a technical question, answer in this order:

1. **Direct answer:** "Yes, the core workflow is real in our local/deployed build."
2. **Boundary:** "The external data connector is mocked with a fixed fixture because the event environment has no stable credentials."
3. **Evidence:** "The code path is in `...`, and the README shows the test input and output."
4. **Limitation:** "It currently handles [specific scope], not [larger claim]."
5. **Next step:** "The next engineering step is [specific change]."

Do not answer a question about accuracy with a speed number. Do not answer a question about deployment with a screenshot. Do not answer a question about AI with the model name alone; explain the input, output, and guardrail.

**Decision:** Rehearse the failure and the answer to "Is this real?" as carefully as the successful path. A clean recovery is more credible than an improvised denial.

## 8. HONESTY: What a 3-Minute Video Can and Cannot Fake

### It can fake or compress

A video can compress waiting time, choose the best take, animate a title, zoom into a result, use seeded data, simulate a future workflow, or show a mockup of an incomplete product. Dropbox is a concrete example: the reported early video showed what the product would do even though the product was not fully built, and the article describes the video as a Minimum Viable Product [10]. That is a legitimate communication technique when the status is explicit.

A video can also make a small build feel larger by using a consistent visual system, a clear narrator, a close-up of the meaningful state change, and a single proof number. It cannot make an unmeasured claim measured, turn a screenshot into a deployed service, or convert a mocked API into a production integration.

### It cannot safely fake

It cannot prove that the live build works under new input, that an external API is available, that a result is accurate, that the team owns every asset, or that a backend will survive the next user. It cannot hide an event-time violation if the rules require code, framework, AI, and tool disclosure. MLH's published rules explicitly require a public code link, framework listing, AI disclosure, and tool credits [1].

It also cannot eliminate judge questions. MLH says judges can ask for clarification [25]. A sponsor judge may ask for a fresh input, disconnect the network, request the architecture, ask where the number came from, or ask what happens at ten times the load. Build the answer around the current truth, not the trailer's implication.

### The answer to "Is this real?"

Use this script and replace the brackets with facts:

> "The core path you saw is real in [local build/deployed URL]. The [specific component] is mocked or pre-recorded because [specific reason]. The input is [real test data/fixture], and the output is produced by [code, model, or service]. You can verify it in [README/code path]. Today it handles [scope]. The limitation is [limitation], and our next step is [next step]."

If the entire clip is pre-recorded, say so: "This is our pre-recorded backup of the same build path; the live version is available in the repository." If the product is only a clickable prototype, say: "This is a prototype of the intended flow; the backend is not yet live." The truthful answer may feel less cinematic, but it gives the judge a reason to trust the parts that are real.

The best ethical pattern is **show, label, verify**:

| Claim on screen | Label required | Verification artifact |
|---|---|---|
| Live feature | "Live in demo build" | Fresh run or code path |
| Recorded run | "Pre-recorded backup" | Matching commit and timestamp in README |
| Mock data | "Sample fixture" | Fixture file and input schema |
| Simulated API | "Mock connector" | Adapter code and replacement plan |
| Measured number | Test condition and denominator | Script, log, or result file |
| AI-generated asset | Tool and usage note | README credit and prompt or source where appropriate |

**Decision:** Optimize for the strongest claim you can prove, not the strongest claim you can imply. A sponsor judge who catches one undisclosed fake may discount every other claim; a sponsor judge who sees a bounded, working prototype may reward the team for engineering judgment.

## Synthesis

The central tradeoff is not cinematic versus ugly. It is **attention versus evidence**, and the winning plan assigns each medium a role.

| Dimension | Startup launch film | Three-minute live demo | Pre-recorded backup | Best hackathon choice |
|---|---|---|---|---|
| Primary job | Make the product memorable | Make the product scoreable and believable | Preserve the intended path under failure | Trailer for emotion; live demo for proof; video for recovery |
| Mechanism | Hook, human voice, compressed transformation | Failure, fix, killer feature, proof number | Deterministic best take and clear status label | Use one shared script and three outputs |
| Scope | Can imply a larger vision | Must show one working path | Can show future or incomplete flow | Keep vision in the last 10 percent, not the first 90 percent |
| Tradeoff | More polish can hide less evidence | More live detail can look less cinematic | More reliability can reduce spontaneity | Hybridize visuals, not truth |
| Time horizon | Brand impression after the event | Score in the three-minute room | Insurance against technical failure | Make the video before final polish, not instead of the build |
| Evidence base | Dollar Shave Club shows a low-budget human concept can drive response [26] | YC and MLH support clarity, problem-first framing, a demo rather than a presentation, and strict timing [27][25] | Dropbox shows a mockup-led future demo can attract users while the product is incomplete [10] | Borrow the mechanism, disclose the boundary |

The non-obvious tension is that the most persuasive trailer may be the least reliable proof. Dropbox's reported result demonstrates the power of showing a future product clearly, while the same case makes clear that a video is not a complete system [10]. Conversely, a completely raw screen recording may be honest but fail to give a judge a memorable problem, human stake, or final number. The answer is not to choose one. It is to make the trailer cinematic around real evidence, make the demo judge-first around one reliable path, and make the backup explicitly pre-recorded.

The second tension is between feature breadth and scoreability. YC says you cannot say everything in two minutes [27], and Devpost's rating interface gives a judge a separate 1-5 score for each criterion [23]. A broad demo creates many unscored impressions; a narrow demo creates a few strong, retrievable pieces of evidence. For a top-two advancement goal, the narrow strategy is safer: one painful failure, one working fix, one killer feature, one honest number, and one answer for the first objection.

The final operating principle is simple: **production grade is a system, not a filter**. It is a clear script, clean capture, intelligible audio, controlled pacing, deterministic data, tested compression, two copies, and truthful Q&A. A student team can achieve that at zero budget because the official tools already cover capture, editing, subtitles, effects, export, conversion, and local voice options [8][29][18][11].

## References

1. *Rules for Your Hackathon*. https://guide.mlh.io/general-information/judging-and-submissions/rules-for-your-hackathon
2. *Hackathon Judging Criteria & Scorecard Template | Opportunity ...*. https://www.ohack.dev/hackathon-judging-criteria
3. *DaVinci Resolve 21 Blackmagic Design https://www.blackmagicdesign.com › products › davincir...*. https://www.blackmagicdesign.com/products/davinciresolve
4. *How to build your seed round pitch deck*. https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck
5. *Dollar Shave Club's Success Story*. https://resources.latana.com/post/dollar-shave-club-marketing
6. *Use music and sound effects from the Audio Library*. https://support.google.com/youtube/answer/3376882?hl=en
7. *HandBrake: Open Source Video Transcoder*. https://handbrake.fr/
8. *OBS Studio*. https://obsproject.com/
9. *Embed videos & playlists - YouTube Help - Google Help*. https://support.google.com/youtube/answer/171780?Hl=en
10. *Dropbox's fake demo video that got 75000 signups overnight*. https://yourstory.com/2026/02/dropbox-fake-demo-video-75k-signups-mvp
11. *rhasspy/piper: A fast, local neural text to speech system GitHub https://github.com › rhasspy › piper*. https://github.com/rhasspy/piper
12. *Top 10 Editing Mistakes to Avoid - Videomaker*. https://www.videomaker.com/article/c3/15706-top-10-editing-mistakes-to-avoid
13. *Kdenlive 26.04 Manual*. https://docs.kdenlive.org/en?pubDate=20250602
14. *Loom Demo for SaaS: How to Make One Founders Watch (2026)*. https://www.flowjam.com/blog/how-to-create-a-loom-demo-the-complete-guide-for-professional-video-demos
15. *DropBox Demo*. https://www.youtube.com/watch?v=7QmCUDHpNzE
16. *Product Demo Video Production: 15 Methods Compared (2026)*. https://www.motiontheagency.com/blog/ways-to-make-a-product-demo-video
17. [
Creator Handbook — Kickstarter
](https://www.kickstarter.com/help/handbook)
18. [
FFmpeg](https://ffmpeg.org/)
19. *Embed videos & playlists - YouTube Help*. https://support.google.com/youtube/answer/171780
20. *Free Noise Reduction Tool – Remove Background Noise | Audacity*. https://www.audacityteam.org/features/noise-reduction
21. *GitHub - openai/whisper: Robust Speech Recognition via Large-Scale Weak Supervision · GitHub*. https://github.com/openai/whisper
22. *GitHub - ammen99/wf-recorder · GitHub*. https://github.com/ammen99/wf-recorder
23. *How to judge an online Hackathon - Devpost.com Help Center*. https://help.devpost.com/article/103-how-to-judge-an-online-hackathon
24. *Adobe Podcast | AI audio recording and editing, all on the web*. https://podcast.adobe.com/en
25. *Judging Plan*. https://guide.mlh.io/general-information/judging-and-submissions/judging-plan
26. *Dollar Shave Club, From Viral Video to Real Business - The New York Times*. https://www.nytimes.com/2013/04/11/business/smallbusiness/dollar-shave-club-from-viral-video-to-real-business.html
27. *How to Pitch Your Startup  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/6q-how-to-pitch-your-startup
28. *CapCut Standard vs Pro – Full Comparison Guide for Creators*. https://www.capcut.com/resource/capcut-standard-vs-pro
29. *Kdenlive Manual — Kdenlive Manual 26.04 documentation*. https://docs.kdenlive.org/en
30. *HandBrake Documentation — Welcome*. https://handbrake.fr/docs/en/latest/
31. *Change video privacy settings - Computer - YouTube Help*. https://support.google.com/youtube/answer/157177
32. *Attaching files*. https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files
