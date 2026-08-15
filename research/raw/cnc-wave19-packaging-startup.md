# The 24-Hour YC-Grade Startup Package

## Executive Summary

A YC-seed-level hackathon submission is not a deck with startup vocabulary around a prototype. It is a coordinated evidence system: one sharp company sentence, one working user workflow, one credible proof trail, and several surfaces that all tell the same story. YC's own pitching guidance reduces the story to seven questions - what you do, market size, progress, unique insight, business model, team, and ask - and repeatedly emphasizes clarity, concision, simple language, and a direct ask. [18] [18] [18] [18]

- **Clarity Standard**: YC says the listener should understand what the company does before the investor can evaluate it, and recommends a simple two-sentence explanation without jargon. [18] [18] -> Put the company sentence and the user path on slide 1 and in the first 15 seconds of the demo.
- **Seed Narrative**: Sequoia's template moves from purpose and pain through solution, timing, market, competition, product, business model, team, and financials. [16] -> Build the requested 10 core slides in that causal order, then compress the live presentation to the few frames that prove the story.
- **Investor Attention**: DocSend defines investor reading time and reports average pitch-deck review times of **2 minutes 30 seconds** on several 2023-2024 observations. [23] [23] -> Treat the first 60 seconds as a zero-context test: product, user pain, proof, and the reason to care must be visible before a judge asks for clarification.
- **Evidence Before Polish**: Airbnb's early deck used a five-to-seven-word tagline, a concrete Craigslist demand signal, a one-line 10% transaction fee, and a clear fundraising context. [19] [19] [19] [19] -> Prefer one quantified, traceable validation signal over ten decorative claims.
- **Video Minimum**: A current product-demo guide places homepage or landing-page demos at **90 seconds to 2 minutes**, feature demos at **2 to 3 minutes**, and recommends showing the outcome in the first **15 seconds**. [14] [14] [14] -> Record a short captioned proof video only after the live happy path works; do not use a trailer to hide a broken demo.
- **2026 Production Baseline**: Wistia's 2026 report surveyed **900+ professionals**, analyzed more than **13M videos** and **79M viewing hours**, found that almost every format performs best under **5 minutes**, and reports that **90%** of teams are taking accessibility steps. [12] [12] [12] [12] -> Use clean 1080p capture, readable captions, clear voice audio, and a short edit rather than cinematic effects.
- **Repository Diligence**: Johns Hopkins OSPO recommends a README, license, Contributing file, version, and identifiers; it describes the README as the introduction explaining purpose, operation, installation, usage, and dependencies. [17] [17] -> Make a fresh judge able to understand and run the project from the repository landing page.
- **Traction Honesty**: A seed benchmark source describes a working product, early traction, retention signals, founder-market fit, and a path to later growth, with illustrative ranges of **$5K-$50K MRR** for SaaS, **50-500 users** for consumer, and **5-15 customers** for enterprise. [20] These are benchmarks, not a universal funding threshold. -> Label every number as observed, self-reported, simulated, pipeline, or target.
- **Event Constraint**: The public indexed search did not verify a 2026 Craft-N-Code Rajasthan rule sheet or event identity. [50] -> Treat the 24-hour build, 3-minute demo, sponsor judging, and top-two progression in the brief as organizer-provided constraints and confirm them with the organizer before submission.

The practical priority order is: **working core workflow -> reliable evidence -> clear live demo -> coherent public package -> visual polish**. If a package makes a judge expect more than the product can honestly demonstrate, it is worse than a plain but truthful submission.

## 1. What a Seed-Level Package Actually Is

Seed investors do not buy a collection of files. They form a view of five linked questions: Is the problem real? Does this team understand it unusually well? Does the product produce a visible outcome? Is there evidence that someone wants it? Can this team turn the next milestone into a business?

The package should therefore have one source of truth. The same user, problem sentence, product nouns, metric definitions, team names, pricing hypothesis, and next milestone should appear everywhere. The deck is the argument, the demo is the proof, the landing page is the public explanation, the repo is the diligence surface, and the one-pager is the compressed handoff.

| Artifact | Seed-stage standard | Concrete example to include | Team estimate to produce | Transfers to a 24-hour hackathon? |
|---|---|---|---:|---|
| Core pitch deck | Clear sequence from purpose and pain to product, evidence, business, team, and ask; Sequoia's template explicitly includes purpose, problem, solution, why now, market, competition, product, business model, team, and financials. [16] | 10 core slides plus a short appendix; one claim per slide | 2-4 hours after the product story is stable | Yes, strongly |
| One-pager | One readable page that allows a new person to understand the company without a live explanation; use the same claims as the deck | One sentence, user/problem, product screenshot, proof, market, model, team, ask, links | 45-90 minutes from the deck | Yes, strongly |
| Product trailer | Short outcome-led product proof with a hook, clear voice, captions, and one CTA; current guidance places landing-page demos at 90 seconds to 2 minutes. [14] [14] | 60-120 second screen recording with captions and a failure-free path | 60-120 minutes including retakes | Yes, if the product is already stable |
| Landing page | Specific headline, value proposition, product proof, one primary CTA, real evidence, and links to demo/repo | Hero statement, 3-step workflow, screenshot or embed, observed test result, Try Demo button | 60-120 minutes using a template | Yes, strongly |
| Public repository | Reproducible setup, README, screenshots/demo, architecture, license, contribution and limitation notes; OSPO recommends README, license, Contributing, version, and identifiers. [17] [17] | One-command setup, `.env.example`, seed data, architecture diagram, live URL, test command | 60-120 minutes if code is organized | Yes, strongly |
| Metrics sheet | Definitions, numerator/denominator, date, cohort, source, and limitation for each number | `5/6 testers completed task in under 2 minutes` with test date and method | 30-60 minutes | Yes, but only with real tests |
| Data room or appendix | Detailed evidence for follow-up questions, not a place to conceal caveats | Interview notes, test logs, API cost, known issues, roadmap | 30-90 minutes | Optional; useful for nationals |

The transfer rule is simple. Anything that increases **legibility, reproducibility, or trust** transfers well. Anything that requires months of user behavior, audited financials, mature security, real customer references, or a large production budget does not transfer overnight.

**Decision:** Build the minimum package that makes the product look investable because it is understandable and testable, not because it is heavily branded.

## 2. The Seed Pitch Deck: Ten Slides and the 60-Second Scan

### The canonical 10-slide operating structure

There is no single legally canonical deck, and YC's public guidance is framed as seven pitch questions rather than a mandatory numbered template. Sequoia's public template is the cleanest reference structure: Company Purpose, Problem, Solution, Why Now, Market Size, Competition, Product, Business Model, Team, and Financials. [16] YC adds the important speaking test: explain the product simply, quantify progress, state the unique insight, own the business model, explain relevant team credibility, and ask directly. [18] [18] [18]

For this hackathon, use a title card plus the following **10 core slides**. The title card is not one of the ten; it carries company name, one-line purpose, and a QR code or short URL.

| Slide | Investor-grade content | What the judge must understand | Common failure |
|---:|---|---|---|
| 1. Problem | Specific user, painful task, current workaround, frequency, and consequence | Who is suffering, and why the current method is unacceptable | A social issue with no named user or observable workflow |
| 2. Solution | One sentence plus the three most important customer benefits | What changes for that user | Feature list instead of outcome; Airbnb's teardown specifically recommends benefits over features. [19] |
| 3. Market and why now | Initial customer, bottom-up market logic, timing change, and wedge | Why this can become a company rather than a useful project | Huge top-down TAM with no buyer, price, or distribution path |
| 4. Product | One end-to-end workflow, screenshots, architecture boundary, and current scope | What exists today and what the user actually does | Ten screens with no complete path |
| 5. Traction or validation | Observed usage, tests, pilots, revenue, retention, or clearly labeled learning | What has been proven, by whom, when, and how | Calling a page view a user or a future target current traction |
| 6. Business model and go-to-market | Who pays, what they pay for, price hypothesis, distribution channel, and acquisition loop | How the project can become a business | "We monetize with AI" or several incompatible models |
| 7. Competition and advantage | Current alternatives, direct competitors, substitute behavior, and two defensible differences | Why this team can win | Saying there is no competition; YC's unique insight question exists to prevent that. [18] |
| 8. Team | Founder roles, relevant experience, who built what, and why this team has access or insight | Why this team can execute the next milestone | Generic bios, inflated titles, or no ownership of the live demo |
| 9. Ask and use of funds | Amount or resource request, instrument if relevant, use of funds, and what it unlocks | What the team wants and what changes after it receives it | Asking for money without a measurable milestone |
| 10. Timeline and milestones | Next 30, 60, and 90-day product, user, and business milestones; risks and dependencies | What happens next and how progress will be measured | A calendar with no acceptance criteria |

Sequoia's longer product and business-model guidance is useful for the appendix. It asks founders to cover product form factor, functionality, features, architecture, intellectual property, roadmap, pricing, average account size or lifetime value, sales and distribution, and customer or pipeline evidence. [16] For a student team, do not pretend to have mature IP, a sales pipeline, or audited financials. Replace absent evidence with a clearly labeled hypothesis and a test plan.

### What YC says that changes the deck

YC's most important rule is not a slide-count rule. It is compression. The pitch should make the listener interested enough to ask follow-up questions, not attempt to explain the entire business in the first pass. YC recommends a user path as an effective explanation and warns against jargon, acronyms, marketing language, and ambiguous words such as "platform." [18] [18]

Use this two-sentence construction:

> We help **[specific user]** complete **[painful job]** by **[mechanism]**, reducing **[measurable consequence]**. Unlike **[current alternative]**, we **[specific insight or advantage]**.

Then make the demo enact that sentence. If the sentence says "reduce inspection time," the demo must show a before state, the action, and the after state with a time or accuracy measure.

### The 60-second test

The evidence does not support a universal literal 60-second investor rule. DocSend measures reviewed decks, investor time, and founder-sent decks, and reported average review times of **2 minutes 30 seconds** on February 26, 2024 and August 14, 2023, with **2 minutes 36 seconds** reported on April 3, 2023. [23] [23] [23] [23] That is still a short first pass, especially for a deck that contains ten slides.

Operationalize the first 60 seconds as five visual answers:

1. What is the company and who is the user?
2. What painful event occurs today?
3. What does the product do in one visible workflow?
4. What evidence exists now?
5. What is the next ask or milestone?

A judge should be able to answer those questions from the title slide, problem/solution slide, product frame, and validation frame even if the presenter is interrupted. Airbnb's teardown reinforces the same compression discipline: five-to-seven-word tagline, simple words, one-line statements, highlighted key phrases, fewer readable quotes, and "less is more." [19] [19] 

**Decision:** Submit a complete 10-slide PDF for diligence, but rehearse a five-frame live story: user/problem, solution, product proof, validation/business, and ask/timeline.

## 3. Case Studies: Airbnb and Coinbase Show What Seed Clarity Looks Like

### Airbnb: simple language, a real demand signal, and a one-line model

The public Airbnb teardown says the original deck used the phrase "Book rooms with local, rather than hotels," a short description that simultaneously identifies the service, audience, and alternative. [19] The deck also used Craigslist's **17K weekly listings** for San Francisco and New York as evidence that temporary hosting demand already existed. [19]

It then expressed the business model in one line: Airbnb would take a **10% commission** on each transaction. [19] The teardown places the deck in a **$600K** fundraising context and notes a projection based on an average **$25** transaction fee and **$200M** in projected revenue between 2008 and 2011. [19] [19] The last figure is a historical deck projection, not proof that the projection happened; preserve that distinction in any case study.

What transfers is not the category or the exact numbers. The transferable move is to show an existing workaround, quantify activity around it, state a simple take rate or price, and make the wedge obvious. A hackathon team should replace Craigslist listings with its own real interviews, observed task tests, or publicly available market evidence, and should label any forecast as a forecast.

### Coinbase: the ask can be as concrete as the product

Brian Armstrong's founder-published page describes the deck as the slides used for YC Demo Day and records **$320K committed already** toward a round that would close at **$1M**. It also asks, "What can I do to help you make a decision to invest in Coinbase?" [5] [5] The page does not provide a full canonical slide outline, so it should not be used as evidence for one.

The lesson is directness. A student team can say, "We are asking for access to 3 pilot colleges and a $X cloud credit grant to reach 100 observed task completions," rather than making a vague request for support. If the team asks for seed money in the narrative, it must connect the amount to a milestone, not just to more features.

### Dropbox: a video can validate demand without proving product maturity

A secondary case study reports that Dropbox used a **3-minute** screencast showing how the service would work, posted it to Hacker News, and received **75,000 signups overnight**, described as a **10x** increase from **5,000 to 75,000** signups. [29] [29] The same case study says the video was simple, technical, and included inside jokes for early adopters. [29]

This is a demand-validation story, not permission to fake a product. Hacker News commentary describes the video as a prototype at best and distinguishes it from the first version that reached users and generated revenue. [43] The hackathon translation is powerful: show the intended user outcome early, but separately state what is implemented, what is simulated, and what remains.

**Decision:** Steal Airbnb's compression, Coinbase's direct ask, and Dropbox's outcome-first validation. Do not steal their historical numbers or present a validation artifact as a mature business.

## 4. The One-Pager and Landing Page: Two Surfaces, One Story

### The one-pager format

There is no single YC-mandated one-pager sequence equivalent to the formal deck templates. The safest investor-grade approach is a genuinely readable one-page handoff that compresses the same purpose, problem, solution, market, progress, business model, team, and ask that YC and Sequoia require in a deck. [18] [16]

Use a single landscape or portrait page at normal zoom. Do not shrink a 10-slide deck into microscopic text. A judge should be able to forward the page without verbal context, click the demo, identify the team, and distinguish current evidence from future plans.

| One-page block | Exact content | Evidence or link | Hackathon implementation |
|---|---|---|---|
| Header | Name, five-to-seven-word tagline, one-sentence purpose, team contact | Website and QR code | 10 minutes |
| Problem | User, event, current workaround, cost or harm | Interview quote or source link | 15 minutes |
| Solution | One sentence and three user benefits | 30-second GIF or screenshot | 15 minutes |
| Product | One complete workflow, current scope, limitations | Live URL, video, or repo | 20 minutes |
| Market and why now | Initial customer, bottom-up sizing logic, timing change | Calculation and assumptions | 20 minutes |
| Validation | Observed tests, interviews, pilot requests, revenue, or usage | Date, sample, method, raw link | 20 minutes |
| Business | Buyer, price hypothesis, distribution, competitors, advantage | Pricing assumption and alternatives | 15 minutes |
| Team | Names, roles, relevant access or experience | Linked profiles if appropriate | 10 minutes |
| Ask and next milestone | Amount or resource, use, 30/60/90-day outcomes | Acceptance criteria | 15 minutes |
| Footer | Demo, repo, privacy note, status, last-updated date | All links tested from a new browser | 10 minutes |

The one-pager should contain **one current metric**, **one product image**, **one explicit limitation**, and **one next milestone**. It should not contain unsupported logos, a fake customer quote, a vanity download count, or a market forecast presented as revenue.

### Landing-page requirements

The landing page is not a second pitch deck. It is a public answer to "What is this, why should I care, and what can I do next?" YC's clarity rule and Airbnb's short tagline rule are good tests for the hero section. [18] [18] [19]

Recommended page sequence:

1. **Hero:** target user plus outcome, not a generic technology label.
2. **Primary CTA:** Try the live demo, watch the product proof, or request a pilot. Choose one primary action.
3. **Product proof:** embedded demo, GIF, or three annotated screenshots showing input, processing, and output.
4. **How it works:** three steps using the same nouns as the live demo.
5. **Evidence:** observed test result, interview count, pilot status, or explicit "pre-launch" label.
6. **Use cases:** two or three narrow workflows, not a list of every possible customer.
7. **Business and deployment:** who pays, price hypothesis, integrations, privacy, and limitations where relevant.
8. **Team and contact:** why this team understands the user and how to reach them.
9. **Footer:** repo, one-pager, deck, status, last-updated date, and a working contact.

A useful pattern is: **"For [user], [product] helps you [outcome] without [current pain]. Try the working demo."** Avoid "AI-powered platform for the future of..." unless the next line names a concrete task.

Vercel's official enterprise demo page illustrates a narrow public page: the headline is "Get a demo of Vercel Enterprise," the CTA is "Get a custom demo," and the page points to custom plans and pricing. [44] Demand Curve's own page uses a concrete value proposition about auditing the page an ad points to and rebuilding it around what converts. [42] These examples do not prove a conversion rate, but they demonstrate the useful principle: a page can make its audience, action, and value explicit without explaining the entire company above the fold.

**Decision:** Build the one-pager after the deck and the landing page from the one-pager. If the three surfaces use different user names, metrics, or claims, fix the source of truth before adding design.

## 5. Product Trailer and Three-Minute Demo: Production Standards You Can Reproduce

### Launch-video structure

Current product-demo guidance puts a homepage or landing-page demo at **90 seconds to 2 minutes**, a feature-specific demo at **2 to 3 minutes**, a sales follow-up at **3 to 5 minutes**, and onboarding material at **5 to 10 minutes**. [14] [14] For this contest, the live 3-minute limit is the pitch, not a reason to add a 3-minute marketing monologue.

Use this video structure:

| Time | Story beat | Screen and sound |
|---:|---|---|
| 0:00-0:15 | Outcome hook | Show the finished result first. The guide explicitly says not to open with the company name or a rhetorical question. [14] |
| 0:15-0:30 | User and pain | One sentence, one real scenario, no stock montage |
| 0:30-0:45 | Tell | State the three steps the viewer will see; the Tell-Show-Tell method gets to the point. [6] |
| 0:45-1:40 | Show | Record one end-to-end workflow with visible input, processing, and output |
| 1:40-2:00 | Proof | Show one observed test, quality measure, cost, time saved, or limitation |
| 2:00-2:15 | Tell | Summarize what happened; do not add features that were not shown. [6] |
| 2:15-2:30 | CTA | Give one action, such as Try the demo or Request a pilot; multiple choices create decision paralysis according to the guide. [14] |

For the live 3-minute demo, use a slightly different version: 0:00-0:20 problem and promise, 0:20-0:40 user setup, 0:40-2:15 product path, 2:15-2:40 proof and limitation, and 2:40-3:00 ask. Rehearse with a visible timer. The trailer can be the offline fallback, but it should not be the only proof unless the rules permit prerecorded demonstrations.

### Audio, captions, and editing

The production standard is mostly discipline, not expensive equipment. The current guide recommends a condenser or dynamic microphone, a quiet room, avoiding the built-in laptop microphone, and compressing the voice in post for consistent levels. [14] Another demo guide recommends clear audio, no background noise, no background music, and clear speech. [6]

Add closed captions to every video. [14] Wistia's 2026 report says **90%** of teams are taking accessibility steps and captions are the most common starting point. [12] Use large, high-contrast captions, keep important UI text on screen long enough to read, and do not rely on audio to explain a critical step.

Cut dead air, trim pauses longer than one second, use restrained callouts or zooms to guide the eye, keep a logo reveal to **2-3 seconds**, and end with a branded CTA card that matches the website. [14] Export a clean 1080p version. Wistia reports that Full HD 1080p remains the most common upload resolution, vertical HD uploads were up **24%** year over year, 4K uploads rose **16%**, and 720p uploads fell **8%** in its 2026 dataset. [12] For a judge-room laptop, horizontal 1080p is the safest master; create a vertical crop only if the team has time.

Wistia's 2026 report is useful context rather than a contest rule: it surveyed **900+ professionals**, analyzed more than **13M videos** and **79M viewing hours**, and says shorter video generally has higher engagement, while almost every format performs best under **5 minutes**. [12] [12] [12] The relevant hackathon conclusion is to deliver the main message before attention drops, not to imitate a commercial production budget.

**Decision:** Make one reliable 90-150 second captioned product proof video, retain the raw screen recording, and test playback offline before spending time on music, animation, or a cinematic trailer.

## 6. The GitHub Repository as a Company Artifact

A public repo is a credibility surface because it lets a technically capable judge test whether the product is real, organized, and reproducible. It is not automatically evidence of quality: a beautiful README around code that cannot install is a liability.

Johns Hopkins OSPO recommends adding a license, README, Contributing file, version, and identifiers such as DOIs, SWHIDs, or citations for research software repositories. [17] It describes the README as the introduction that explains the purpose of the code, why it was created, what it does, how it works, and how to install it, use it, and handle dependencies. [17]

### Repository structure

```text
README.md
LICENSE
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
.env.example
Dockerfile or explicit deployment instructions
/docs/architecture.md
/docs/product-decisions.md
/docs/limitations.md
/screenshots/hero.png
/demo/demo.gif
/src or /app
/tests
/data/sample or /fixtures
```

The exact folders depend on the stack. The standard is discoverability and truthfulness, not a ceremonial file list.

| Repo surface | What a judge should see | Startup-grade test | Hackathon time |
|---|---|---|---:|
| First README screen | One sentence, user outcome, status, live demo, video, and screenshot/GIF | Understand the product in 20 seconds without cloning | 20-30 min |
| Quick start | Prerequisites, clone/install/run commands, `.env.example`, seed data | A fresh teammate can run it without private credentials | 20-40 min |
| Demo proof | GIF or screenshot sequence of the same workflow used on stage | The repo does not show a different or fictional product | 10-20 min |
| Architecture | Small diagram of client, API, model, database, external services, and data flow | The team can answer where data goes and what can fail | 15-25 min |
| Tests and status | Smoke-test command, known failing areas, deployment status | The team does not claim production readiness it has not tested | 10-20 min |
| License and contribution | License choice, contribution route, code of conduct, security contact | Ownership and expected use are explicit; OSPO recommends license and Contributing material. [17] | 10-20 min |
| Limitations and roadmap | What is simulated, hard-coded, rate-limited, or not yet secure | Scope is visible before a judge discovers it | 10-20 min |
| Badges | Only truthful build, deploy, test, license, or version badges | No fake coverage, stars, users, or performance badges | 5-10 min |

Investors will not normally read every line during a short contest. The useful operational test is more demanding: a judge clicks the README, sees the demo, checks the setup command, notices whether sample data is declared, and asks one architecture or limitation question. The team should be able to answer from the repo rather than from memory.

**Decision:** Optimize the first screen and the fresh-install path. A modest but runnable repo beats a heavily badged repo with missing environment variables, private dependencies, or an unexplained data source.

## 7. Metrics and Traction: Show the Evidence You Actually Have

At seed stage, traction is not one universal number. It is evidence that users want the product, that the team can deliver it, and that a business mechanism may exist. A seed-round benchmark source lists a working product rather than a prototype, early traction, retention signals, founder-market fit, and a path to later growth; its illustrative figures are **$5K-$50K MRR** for SaaS, **50-500 users** for consumer, **5-15 customers** for enterprise, and a potential path to **$1M-$2M ARR** with strong growth. [20] Treat those as contextual benchmarks from one source, not a pass/fail rule or a number to manufacture in a hackathon.

A metric source lists ARR/MRR, revenue, monthly or daily active users, CAC, LTV, and retention as traction categories. [35] Another benchmark source frames traction as what investors invest in, while acknowledging that its definition changes by stage, industry, and time. [30]

### Recommended hackathon traction slide

| Signal type | What to show | Exact honesty label |
|---|---|---|
| Problem validation | Number of interviews, date range, user profile, repeated pain themes | `Interview evidence; not product usage` |
| Product test | Completed tasks divided by test attempts, time, error rate, or quality score | `Observed internal or external test; n = ...` |
| Usage | Unique people who used the product, active definition, cohort dates, repeat use | `Observed users; definition and source linked` |
| Pilot | Named organization only with permission, scope, start date, and status | `Pilot discussion`, `pilot agreed`, or `pilot live`; never call discussion revenue |
| Revenue | Amount, payer, period, invoice or payment record | `Recognized revenue`; do not call a forecast MRR |
| Model quality | Labeled test set, accuracy, precision/recall, latency, cost, and failure cases | `Evaluation result on declared dataset` |
| Pipeline | Requests, waitlist, letters of interest, or scheduled calls | `Pipeline or intent; not customers` |
| Future milestone | Target number and date | `Target`, not traction |

Every metric should carry five footnotes: **definition, numerator, denominator, date/cohort, and source**. For example: `5 of 6 external testers completed the target task in under 2 minutes on 15 August; test log linked; one failed because of OCR quality.` That is more credible than `83% success rate` without context.

Separate four categories in the slide:

- **Observed:** analytics or test logs generated by real events.
- **Self-reported:** interview or survey responses, with sample and wording.
- **Simulated:** synthetic records, mocked payments, seeded database rows, or generated AI outputs.
- **Target:** future milestone, forecast, or business hypothesis.

The package should show at least one limitation beside the positive metric. Airbnb's Craigslist figure was a demand signal, not proof that Airbnb already had scale. [19] Coinbase's public deck showed capital already committed and a round target, which is a fundraising signal, not a claim that every business metric was mature. [5] Dropbox's reported signup spike validated interest but did not mean the screencast was a complete production system. [29] [43]

**Decision:** Put three traceable signals on the slide, not ten vanity metrics. For a 24-hour team, a well-documented external test and a clear learning loop are more credible than invented MRR, fake logos, or a huge unverified waitlist.

## 8. What Transfers to a 24-Hour Build and What Does Not

The package should be built in dependency order. The product and evidence come first; the presentation surfaces are downstream views of those facts.

| Artifact or behavior | Full seed-company standard | Zero-budget 24-hour version | Team estimate | Transfer value |
|---|---|---|---:|---|
| Problem research | Repeated customer discovery and segment evidence | 5-10 focused interviews or credible public evidence, with notes | 60-90 min | High |
| Product | Reliable multi-user product with monitoring and security | One complete happy path, seeded fallback data, visible error state | 6-10 hours | Very high |
| Analytics | Cohort retention, revenue, CAC/LTV, experiment history | Event logging for starts, completions, failures, latency, and cost | 30-60 min | High |
| Deck | Fundraising narrative, financials, diligence appendix | 10 core slides, 5-frame live narrative, one appendix slide for limitations | 2-4 hours | Very high |
| One-pager | Forwardable investor summary and data-room links | One page generated from the deck with current status and exact evidence | 45-90 min | High |
| Trailer | Scripted, captioned product video with multiple cuts and distribution versions | One 90-150 second captioned screen recording, offline copy | 60-120 min | Medium-high |
| Landing page | Conversion-tested public site with real social proof and product education | One fast page with headline, demo, proof, CTA, repo, limitations, contact | 60-120 min | Very high |
| Repository | Reproducible codebase, CI, security, docs, releases, contribution workflow | README, setup, sample data, architecture, license, limitations, smoke test | 60-120 min | Very high |
| Customers and revenue | Paying users, retention, contracts, references, financial records | Permissioned interviews, test users, pilot interest, or explicit pre-launch status | Overnight creation is not credible | Low; do not fake |
| Brand system | Research-backed positioning, design system, campaign assets | Consistent name, two colors, readable typography, one logo treatment | 20-40 min | Medium |
| Security and compliance | Threat model, access control, privacy review, legal terms, monitoring | Data-flow note, no real sensitive data, secrets removed, known-risk disclosure | 30-60 min | Medium; disclose limits |

### Recommended 24-hour schedule

| Build window | Owner focus | Exit criterion |
|---:|---|---|
| 0:00-1:00 | Choose one user, one painful job, one success metric, and one sentence | Any teammate can repeat the problem and outcome |
| 1:00-7:00 | Build the end-to-end workflow and deployment | A new account or seeded demo completes the happy path |
| 7:00-8:00 | Add error handling, fixture data, and secrets hygiene | Demo survives the obvious invalid input and network failure |
| 8:00-9:00 | Run 5-10 tests and log results | Evidence table has actual numerator, denominator, and timestamps |
| 9:00-11:00 | Draft deck storyline and ask | Slides 1-5 explain the product without narration |
| 11:00-12:00 | Write README and architecture diagram | Teammate can run it from the README |
| 12:00-13:00 | Publish landing page and one-pager | All links work in a fresh browser |
| 13:00-15:00 | Record and caption trailer or fallback demo | Offline video shows the same workflow as the live demo |
| 15:00-18:00 | Rehearse the 3-minute presentation repeatedly | Presenter finishes under time with a controlled reset path |
| 18:00-20:00 | QA on a second device and network | No secret, broken link, missing font, or untested button remains |
| 20:00-22:00 | Polish only the highest-visibility surfaces | Product proof remains stable after edits |
| 22:00-24:00 | Freeze, back up, and rehearse the ask and limitation answers | The submitted build and offline assets are identical to the rehearsed version |

If there are four people, assign one person to core product, one to integration and testing, one to evidence and README, and one to deck, landing page, and video. All four should rehearse the product reset and the honesty labels. A packaging owner should never make a late visual change that changes the demo state.

Judges are most likely to reward a reliable visible outcome, problem specificity, sponsor relevance, evidence quality, and a credible next milestone. This is a recommendation for the stated 3-minute format, not a verified Craft-N-Code scoring rubric, because the public 2026 rule sheet was not located. [50]

**Decision:** Stop adding features when the team can complete the user path, explain the evidence, and recover from failure. Spend the remaining time on rehearsal, links, captions, and reproducibility.

## 9. Failure Modes, Trade-offs, and the Underbuilt-Product Trap

### Failure mode 1: The deck is stronger than the product

A deck can make a product sound like a category leader. That raises the judge's expectation and makes any missing button or canned response more damaging. The fix is to place a visible status label on the product slide: `working now`, `simulated`, `manual behind the scenes`, or `planned next`.

Airbnb's early deck worked because its claims were concrete enough to understand: a short tagline, a current alternative, a demand signal, and a simple transaction fee. [19] [19] [19] The team should copy that level of specificity, not the apparent completeness of the later brand.

### Failure mode 2: A demo video becomes a substitute for testing

Dropbox is the right case study and the wrong excuse. The reported 3-minute video generated interest before the complete product was ready. [29] Hacker News commentary explicitly distinguishes a prototype video from the later MVP and revenue-generating product. [43] A hackathon team can use a video to de-risk live demo failure, but it should not claim that a prerecorded path proves production readiness.

### Failure mode 3: Vanity traction

A waitlist, page view, social impression, generated record, or teammate test may be useful evidence, but it is not automatically a customer, retained user, revenue, or product-market fit. Use the exact label and show the denominator. If a sponsor asks, "Who is using this outside your team?" the answer should be immediate and precise.

### Failure mode 4: The public surface contradicts the repo

A landing page may say "secure enterprise platform" while the README reveals an exposed API key, hard-coded test data, or a one-command setup that does not work. OSPO's recommended README, license, version, and contribution materials are useful because they force the project to state how it works and how others can use it. [17] [17]

### Failure mode 5: Polishing the wrong layer

A 4K export, animated logo, ten extra features, or a complex brand system cannot compensate for a broken authentication flow. Wistia's 2026 data shows 1080p is still the common baseline and that shorter videos generally engage better. [12] [12] That supports a pragmatic choice: clean 1080p, captions, clear audio, and a reliable product path.

| Temptation | Why it looks impressive | Why judges can puncture it | Correct replacement |
|---|---|---|---|
| Huge TAM slide | Sounds venture-scale | No buyer, price, wedge, or calculation | Bottom-up first customer and pricing logic |
| Fake customer logos | Signals adoption | Permission and usage questions expose it | Named interviews or pilot status with permission |
| "AI accuracy" without dataset | Sounds technical | One question about labels or failures breaks the claim | Dataset size, method, result, and failure example |
| Multiple CTAs | Appears ambitious | Nobody knows the next action | One CTA on page, video, and final slide |
| Dense deck | Feels thorough | No readable first-pass story | One takeaway per slide; larger text |
| Decorative badges | Looks like maturity | Fake coverage, stars, or deploy status are visible | Only truthful build, test, deploy, and license badges |
| Canned live demo | Avoids risk | Follow-up input or fresh account exposes it | Seeded but declared data, plus a real error path |

**Decision:** Every polished claim must have a corresponding screen, log, file, person, or test result that a judge can inspect.

## 10. Comparative Synthesis: Choose the Smallest Credible Package

The artifacts do different jobs. Treating them as interchangeable creates either repetition or a dangerous expectation gap.

| Dimension | Deck | One-pager | Trailer/demo | Landing page | GitHub repo | Metrics sheet |
|---|---|---|---|---|---|---|
| Primary mechanism | Narrative compression | Forwardable summary | Demonstrated outcome | Public conversion and trust | Reproducibility and diligence | Quantified evidence |
| Main time horizon | Next meeting or funding decision | Handoff after first contact | Immediate understanding | Ongoing public discovery | Follow-up technical review | Current proof and future measurement |
| Best evidence | Problem, market, product, team, ask | Same claims in compact form | Working workflow and result | Screenshot, demo, real proof | Code, setup, architecture, limitations | Logs, cohorts, tests, sources |
| Main trade-off | Breadth versus readability | Completeness versus density | Production quality versus truth | Social proof versus permission | Openness versus security and setup burden | Quantification versus sample size |
| Most transferable overnight feature | Clear story | One-page coherence | Outcome-first screen recording | One CTA and live link | Runnable README | Honest numerator and denominator |
| Main failure signal | Jargon or unsupported claims | Microscopic text | Music and effects hiding a weak path | Fake logos or generic headline | Cannot install or secret leakage | Vanity metric or forecast mislabeled as fact |

The mechanism differs across the stack: the deck earns attention, the product earns belief, the metric earns confidence, the repo earns technical trust, and the landing page makes the package discoverable. The time horizon also differs. A deck can make a future company legible today, while retention, revenue, security, references, and repeat usage require time that no overnight package can manufacture.

The central tension is between **venture-scale narrative** and **hackathon-scale evidence**. A student team should still show a large problem, market logic, business model, and 90-day plan, but should ground the present tense in one working workflow and a small declared test. Airbnb's early deck and Coinbase's direct round ask show that simple, concrete claims can coexist with an ambitious company story. [19] [19] [19] [5]

The correct package is therefore not the one with the most artifacts. It is the one in which every artifact points to the same proof: the same user, same input, same output, same metric, same limitation, and same next milestone. If the team has only enough time for three surfaces, choose the working demo, a readable deck, and a public README with a landing-page URL. Add the one-pager and trailer by repurposing those facts, not by inventing new ones.

**Decision:** Optimize for the smallest credible package that a sponsor judge can understand in 60 seconds, test in 3 minutes, and inspect in 10 minutes.

## HONESTY: What Cannot Be Faked in 24 Hours

You cannot honestly create overnight:

- real retention across a meaningful cohort;
- recurring revenue or paid customers without actual payment records;
- customer references or enterprise logos without permission;
- production-grade security, privacy, compliance, and reliability;
- a defensible CAC/LTV model without acquisition and revenue history;
- a mature marketplace with supply, demand, and repeat transactions;
- a proven AI quality claim without a declared dataset, labels, method, and failures;
- a working deployment that the team has not tested from a clean account;
- product-market fit from a teammate demo or generated database;
- a real founding-team advantage merely by assigning impressive titles.

Judges see through over-packaging when the live input is fixed, the output is prewritten, the dashboard has no source, the landing page uses unapproved logos, the repo cannot run, the team cannot explain data flow, or a basic error question breaks the story. A judge also notices when a team says "users" but means page visitors, says "pilot" but means a conversation, says "MRR" but means a forecast, or says "secure" without knowing where secrets and user data go.

Use explicit labels in the product and traction slide:

```text
Observed: 5 of 6 external testers completed the task in under 2 minutes on [date].
Self-reported: 7 interviewees described the same failure mode; notes linked.
Simulated: 100 synthetic records used to demonstrate the workflow.
Pipeline: 2 organizations requested a follow-up; no paid customer yet.
Target: Reach 50 weekly active users within 60 days after the event.
Limitation: Current version uses seeded data and is not production-secure.
```

This is not weak positioning. It is the standard that makes a small result investable: clear progress, a specific insight, a direct ask, and a credible next test. YC explicitly recommends explaining progress as the ratio between work completed and time spent, and it says founders do not need to sound cool; they need to be clear. [18] [18]

**Final rule:** Never let the package imply that a prototype has evidence it does not have. Make the current product small, the proof traceable, the future plan ambitious, and the boundary between those three unmistakable.

## References

1. *Startup 1 Pager – 1 Pagers for Pitching VCs Template | Notion Marketplace*. https://www.notion.com/templates/fundraiserpro
2. *SaaS Landing Page Best Practices: A Conversion-Focused Guide | Framer Websites*. https://framerwebsites.com/blog/saas-landing-page-best-practices
3. *One moment, please...*. https://tieglobalsummit.org/rajasthan-hackathon
4. *Craft-N-Code Hackathon 2024 Details | PDF*. https://www.scribd.com/document/781392222/CraftNcode-Brochure
5. *Medium*. https://barmstrong.medium.com/the-coinbase-seed-round-pitch-deck-50c8ec91d40b
6. *SaaS Product Demo Best Practices: Complete Implementation Guide 2024*. https://goconsensus.com/blog/best-practices-for-saas-product-demos
7. *Landing Page Teardowns by Demand Curve*. https://www.demandcurve.com/teardowns
8. *4 Steps to a Successful Product Launch Video: A Guide for Video Marketers*. https://editshare.com/post/4-steps-to-a-successful-product-launch-video
9. *Setting guidelines for repository contributors*. https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
10. *Code N Craft Hackathon 2026 | PDF*. https://www.scribd.com/document/1010240086/Code-N-Craft-Hackathon-2026
11. *Traction Slide Pitch Deck Best Practices and Examples*. https://www.openvc.app/blog/traction-slide
12. *State of Video Report: Video Marketing Statistics for 2026 | Wistia*. https://wistia.com/learn/marketing/video-marketing-statistics
13. *How to build your seed round pitch deck  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck
14. *SaaS Product Demo Video Best Practices: 2026 Guide*. https://www.pixel8production.com/blog/saas-product-demo-video-best-practices
15. *Medium*. https://jaredheyman.medium.com/on-seed-stage-startup-traction-and-why-to-ignore-it-9ad662981145
16. *Sequoia Capital Pitch Deck Template | PDF*. https://www.slideshare.net/slideshow/sequoia-capital-pitchdecktemplate/46231251
17. *Public Code Repository Best Practices – Open Source Programs Office*. https://ospo.library.jhu.edu/learn-grow/public-code-repository
18. *How to Pitch Your Company  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/4b-how-to-pitch-your-company
19. *AirBnb Pitch Deck: Teardown and Redesign (FREE Download)*. https://slidebean.com/blog/airbnb-pitch-deck
20. *Seed Round: definition, 2025 benchmarks (size, valuation, dilution), and the seed-to-Series-A graveyard | Startups.com*. https://www.startups.com/lexicon/seed-round
21. *About the repository README file*. https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
22. [The Startup One Pager: How to Create One Investors Will Love [Including Templates]](https://visme.co/blog/startup-one-pager)
23. *DocSend Startup Index - 2021 Pitch Deck Metrics | DocSend*. https://www.docsend.com/pitch-deck-metrics
24. *What to Include in a 1-Page Investor Summary | Funding Blueprint*. https://fundingblueprint.io/investor-summary-one-pager-template-structure
25. *SaaS Landing Page Best Practices: 14 Proven Tips (2026)*. https://splitsense.ai/blog/guides/saas-landing-page-best-practices-14-proven-tips-2026
26. *Adding a code of conduct to your project*. https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project
27. *40 best landing page examples of 2026 (for your swipe file)*. https://unbounce.com/landing-page-examples/best-landing-page-examples
28. *Best practices for repositories*. https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
29. *Dropbox MVP Success Story: How a Simple Video Created a Billion-Dollar Company*. https://whatismvp.com/case-studies/dropbox-mvp-case-study.html
30. *Startup Funding Benchmarks & Requirements*. https://fi.co/benchmarks
31. *All Encompassing Startup Fundraising Guide - Visible.vc*. https://visible.vc/blog/fundraising-guide
32. *SaaS demo landing page best practices: 7 mistakes to fix*. https://unbounce.com/landing-pages/saas-demo-landing-page-best-practices
33. *Pitch deck Metrics report 2024-2025 - Papermark*. https://www.papermark.com/pitch-deck-metrics
34. *Product Demo Video Best Practices 2026 | ngram.com ngram.com https://www.ngram.com › blog*. https://www.ngram.com/blog/product-demo-best-practices
35. *Traction: An Investor's Lens into Your Startup's Performance*. https://www.thepitch.show/blog/traction-an-investors-lens-into-your-startups-performance
36. *Startup Fundraising Playbook - Trends, Research, Guides ...*. https://www.docsend.com/startup-fundraising
37. *GIF for GitHub README: Recording and Embedding Guide (2026 ...*. https://rekort.app/blog/gif-for-github-readme
38. *YC Startup Library - Y Combinator*. https://www.ycombinator.com/library
39. *Culture of Rajasthan Special Drawings - 3-Minute Drawings ...*. https://www.facebook.com/100076387034155/posts/culture-of-rajasthan-special-drawings/587519617137601/
40. *How to build a great Series A pitch and deck : YC Startup Library*. https://www.ycombinator.com/library/8d-how-to-build-a-great-series-a-pitch-and-deck
41. *The Code on Wages (Rajasthan)Rules, 2026 (Draft)*. https://www.praansconsultech.com/gazette-details/the-code-on-wages-rajasthanrules-2026-draft
42. *Demand Curve | The AI-Powered Growth Agency for Startups*. https://www.demandcurve.com/
43. *The Dropbox demo video was a prototype at best, and probably ...*. https://news.ycombinator.com/item?id=30836156
44. *Get a demo of Vercel Enterprise. - Talk to our Sales team*. https://vercel.com/contact/sales/demo
45. *VC 101: The Angel Investor's Guide to Startup Investing*. https://fundersclub.com/learn/guides/vc-101
46. *Visible.vc - Valuation, Funding & Investors*. http://pitchbook.com/profiles/company/99167-14
47. *GitHub Docs*. https://docs.github.com/
48. *DropBox Demo*. https://www.youtube.com/watch?v=7QmCUDHpNzE
49. *A Guide to Demo Day Presentations*. https://www.ycombinator.com/blog/guide-to-demo-day-pitches
50. *Craft n Code*. https://craftncode.com/
