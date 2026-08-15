# The YC-Grade Seed Fundraising Package

## Executive Summary

- **Compressed Attention**: YC's latest batch presents to an invite-only audience of approximately **1,500 investors and media** [1], and the event is private and oversubscribed [14] -> make the company understandable from the first sentence, then use follow-up artifacts to let serious investors verify it.
- **Narrative Before Detail**: YC's seed-deck guidance says clarity and concision matter, warns against a treatise on the market or world philosophy, and says to focus on narrative [20] -> design a short, spoken story rather than a document that requires the founder to decode it.
- **Canonical Story**: YC's public sequence covers title, problem, solution, traction, insight, business model, market, team, and the raise and milestones [20] -> make every outward artifact tell the same story in the same order.
- **Evidence Over Polish**: YC asks founders to make metrics clear and meaningful, says revenue is better when available, and accepts that a growth curve will not be smooth [20] -> show dated definitions, cohorts, denominators, and the ugly parts of the series.
- **Manual Traction Is Not Fraud**: YC founder history explicitly endorses doing things that do not scale [17], while early Stripe and Airbnb examples used manual onboarding and customer acquisition [17] -> disclose the manual work and explain the repeatable behavior it revealed.
- **Seed Is Not a Blank Check**: YC calls the team especially important at seed and asks founders to explain why the team fits the problem [20] -> pair founder-market fit with direct evidence that users, customers, and the product are moving.
- **Technical Surface Area Matters**: Technical diligence sources identify documentation debt, testing gaps, and key-person risk as material software risks [4], while GitHub documents a repository security-policy mechanism [15] -> make the evaluator path from README to running test to security contact deterministic.
- **No Fake Universal Rulebook**: The gathered primary evidence contains a public YC deck template and a Sequoia business-plan guide, but no verified official fixed deck checklist from a16z, Benchmark, Khosla, or Lightspeed -> do not attribute a generic internet template to those firms; optimize for the questions all serious investors ask and verify.

This report separates three things that founders often blur: published YC or VC guidance, historical company artifacts, and an operational standard synthesized from those sources. The last category is a recommendation, not a claim that YC or any named fund has issued a mandatory checklist.

## Executive Standard: One Company, Seven Surfaces

A YC-grade seed company is not judged by a deck in isolation. It is judged by whether a stranger can move from a one-line description to a product, from the product to evidence of repeated use, and from the evidence to ownership, economics, people, and technical reality without encountering contradictions.

Sequoia's own Airbnb example is unusually clear about the distinction: the founders used its business-plan guidance, but Sequoia says what it liked was not merely the slides; it was the ideas, clarity of thinking, and scope of ambition [19]. YC makes the same point operationally by recommending a simple deck and warning that seed companies usually do not have enough meaningful detail for a treatise [20]. The standard is therefore not maximum information. It is maximum information per unit of investor attention, followed by an easy path to verification.

| Artifact | YC-grade standard | What a serious evaluator should be able to do | Example or evidence |
|---|---|---|---|
| Live pitch | State user, pain, product, proof, insight, market, team, and ask without explanation from the audience | Repeat the company back accurately after the presentation | YC's title/problem/solution/traction/market/team/ask sequence [20] |
| Seed deck | A short narrative with one clear job per slide set | Scan opening slides and decide whether a meeting is warranted | YC says keep sets to one where possible and generally no more than three [20] |
| One-pager | The deck compressed into a forwardable page, with links to proof | Forward it without adding missing context | YC's one-line company description requirement for the title page [20] |
| Product and demo | One deterministic path from problem to outcome | Use or observe the core value, not a simulated click tour | YC asks for concrete benefits and clear explanation of what the company does [20] |
| Metrics sheet | Definitions, periods, cohorts, and source systems | Reconcile the headline number to underlying activity | YC asks for numbers to be clear and meaningful [20] |
| Website | Public version of the same proposition, with product proof and a low-friction next action | Understand and try the product without a founder present | Website guidance emphasizes informing visitors and converting them [24] |
| Repo and engineering packet | Reproducible setup, tests, CI, security reporting, and architecture explanation | Run the code or inspect the real system with limited help | Technical diligence flags documentation and testing gaps [4]; GitHub provides security-policy guidance [15] |
| Data room | Company, financial, legal, IP, customer, and ownership evidence | Verify the claims rather than accept screenshots | Diligence checklists include financials, legal records, cap table, IP, and customer contracts [5] |

The implication is practical: a founder should maintain a single source-of-truth fact sheet. The amount raised, active customers, revenue definition, launch date, team roles, product capabilities, and use of funds should be identical in the deck, one-pager, website, demo narration, and diligence folder. Any mismatch is not a cosmetic defect. It creates an avoidable question about control of the business.

## YC Demo Day: The Timed Conversion Event

### What is public and what is not

YC's current public Demo Day page says the latest batch presents to approximately **1,500 investors and media** [1]. The FAQ says that, starting with the Fall 2024 batch, Demo Day returned to an in-person format [14], is private and invitation-only [14], and does not share company information in advance, although companies launch through the Startup Directory and Launch YC [14]. The public evidence therefore supports a high-density investor event, not a public conference with a stable, universally published speaking format.

The official YC pages in the gathered evidence do not state a single current pitch duration. Do not invent a universal "YC Demo Day is exactly X seconds" rule. Ask the batch organizers for the actual slot and rehearse shorter and longer cuts: a one-sentence version, a 30-second version, the assigned stage version, and a follow-up meeting version. YC's own deck article distinguishes on-stage presentations from slightly longer decks used in follow-up investor conversations [20].

### The operating script

The following is an implementation of YC's published content requirements, not an additional YC rule:

1. **Identity and category**: company name, user, and one-line outcome.
2. **Pain**: a specific recurring problem, preferably in the user's language.
3. **Product**: the smallest understandable mechanism that changes the outcome.
4. **Proof**: one or two dated metrics, customer facts, or a compelling product behavior.
5. **Insight**: why this team sees the problem differently and why the approach can work.
6. **Business and market**: who pays, how money is made, and why the opportunity can become venture-scale.
7. **Team and ask**: founder fit, amount being raised, and what the capital buys by the next milestone.

Every item maps to YC's guidance: state the problem and real-world impact [20], explain the solution in few words and concrete benefits [20], show traction with meaningful numbers [20], explain the special insight [20], address business model [20], market and potential [20], team fit [20], and amount and milestones [20]. A live demo belongs only if it makes the product immediately clearer than a sentence or screenshot. If the demo can fail, present a reliable recorded fallback and never imply that a mock flow is production behavior.

### What YC's guidance tells founders not to do

YC's prohibitions are mostly anti-confusion rules. Do not turn the seed deck or pitch into a treatise on market size or world philosophy [20]. Do not hide weak evidence behind a mathematically perfect hockey stick: YC explicitly says a growth curve is unlikely to be smooth and that this is acceptable [20]. Do not pad the team slide with prestigious advisors; the guide says, bluntly, that investors do not care about advisors in that context [20]. Do not narrate every technical detail before the audience knows the problem and the benefit.

The live presenter should also avoid saying "we have a huge market" without explaining the buyer, price, and path to adoption. The market slide is an invitation to test the business model, not a substitute for customer evidence. Similarly, an ask without a milestone is merely a cash request; YC asks founders to say what the money gets them and why the position inside a year matters [20].

### Famous presentations and the evidence limit

Publicly verifiable famous YC Demo Day talks are harder to treat as a standard because the event is private and company information is not shared in advance [14]. The famous public artifacts available in the gathered evidence are seed decks and teardowns, not authenticated Demo Day transcripts. That distinction matters: a deck can be read at leisure, while a Demo Day pitch must work in a noisy, compressed, high-volume setting.

| Public case | What is actually verified | Why it is useful | What not to infer |
|---|---|---|---|
| Airbnb | A third-party analysis describes a 10-slide deck used to raise **$600K** from Sequoia [10], and Sequoia itself cites Airbnb as an example of clarity and ambition [19] | Shows a compact problem, solution, market, and business narrative | It is not proof of a particular YC Demo Day script |
| Coinbase | The 2012 seed artifact is labeled seed, raised seed funding, and contains **11 slides** [6]; its opening is explicitly identified as clear branding and positioning [6] | Shows that the opening can establish category and product position before detail | The later outcome is not evidence that every seed company should imitate crypto metrics |
| DeckMatch | TechCrunch's series includes a teardown of DeckMatch's **$1M seed deck** [22] | Demonstrates a modern third-party critique format | A teardown is analysis, not a VC mandate |
| Stripe | A third-party page is titled as a detailed breakdown of a deck that raised **$4.5B** [21] | Useful for studying product clarity and infrastructure narratives | That source is not evidence of Stripe's original seed deck or a YC Demo Day talk |

The preparation standard is simple: write the demo narration first, test every click on a clean account, hardcode only what is honestly a demo fixture, and retain a path that shows the real product. This is consistent with practical hackathon guidance to write the demo script before meaningful code and lock the code before submission [26]. A founder should disclose any seeded data, manual back-office work, unreleased feature, or simulated integration in the narration or follow-up materials.

## The Seed Deck: 10-12 Slides That Survive the First Minute

### What the public standards actually say

YC's public seed-deck article calls its document a template for seed decks [20]. It recommends clarity and concision, a narrative, and simple design [20]. It also says slide sets should be one slide where possible and generally no more than three [20]. This is stronger evidence than an internet claim that every seed deck must contain exactly 12 slides.

Sequoia's public business-plan guide is the second primary anchor. It uses Airbnb to emphasize ideas, clarity of thinking, and ambition rather than presentation ornament [19]. The defensible common standard is therefore a sequence that answers the investor's questions in a causal order. It is not a ritual slide count.

| Slide | Job | What belongs | Evidence anchor |
|---|---|---|---|
| 1. Cover | Make the company legible immediately | Name, one-line description, founder contact | YC says the title page has the company name and one-line description [20] |
| 2. Problem | Establish an urgent, specific pain | User, current workaround, frequency, cost or risk | YC asks for a clear problem and real-world impact [20] |
| 3. Solution | State the product's mechanism and benefit | Plain-language outcome, not a feature inventory | YC asks for few words and concrete benefits [20] |
| 4. Product or demo | Make the solution tangible | One workflow, screenshot, short clip, or live path | This is the operational implementation of YC's concrete-benefit requirement [20] |
| 5. Traction | Show behavior that validates demand | Revenue, usage, customers, retention, growth, or high-quality pilots | YC says to show traction and make numbers meaningful [20] |
| 6. More metrics | Answer the next question without clutter | Cohorts, conversion, repeat use, unit economics, or a second proof point | YC explicitly invites additional metrics and notes revenue is better when available [20] |
| 7. Insight and advantage | Explain why this can work now | Non-obvious insight, wedge, distribution, data, workflow, or technical edge | YC asks what makes the company special and what insights make it work [20] |
| 8. Business model | Explain who pays and how | Buyer, price, transaction, margin logic, sales motion | YC calls the business model important even when details are incomplete [20] |
| 9. Market and timing | Establish venture-scale potential | Initial market, expansion path, why now, and credible adoption path | YC asks whether the market is big and whether the team can make it big [20] |
| 10. Competition | Define the alternative and the durable difference | Status quo, direct competitors, switching reason, defensibility | This is the synthesis needed to make the solution and insight testable |
| 11. Team | Prove founder-market fit | Relevant experience, earned insight, role coverage, founder ownership | YC says the team is especially important at seed and should be tied to the problem [20] |
| 12. Raise and milestones | Convert interest into a next step | Amount, use of funds, runway logic, next milestone, and timing | YC asks what the money gets the company and why the one-year position matters [20] |

This 12-part order is an operating template, not a claim that every company needs 12 slides. A pre-revenue company may use a customer interview or design-partner slide instead of revenue; a deep technical company may need an architecture or validation slide; a company with no defensible competition slide should explain the status quo rather than invent a competitor matrix.

### The first 30-60 seconds

No gathered primary source establishes a universal investor reading time of exactly 30 or 60 seconds, nor does it establish a universal first-minute slide count. The honest standard is more demanding: the first screen and first two or three slides must answer **what is this, for whom, and why does the problem matter** before a reader reaches a chart. That follows directly from YC's title, problem, and solution sequence [20].

In practical terms, the first minute should contain the company name, category, user, pain, product, and one proof point. Put the most important number beside the claim it proves, with a date and definition. Do not make the reader infer the business from a logo wall, a giant market number, or a product screenshot without context. If the story only works when spoken, the deck is not a seed deck; it is a set of presenter notes.

### Firm-by-firm evidence boundary

| Investor or program | Public evidence found | What can safely be called a requirement | What cannot safely be claimed |
|---|---|---|---|
| YC | Official seed-deck template and pitch guidance [20] | Clarity, concise narrative, problem, solution, meaningful proof, model, market, team, ask | A permanent universal Demo Day time limit |
| Sequoia | Official business-plan guide and Airbnb discussion [19] | Clarity of thinking, ideas, ambition, and a coherent business plan | That a particular third-party slide template is Sequoia policy |
| a16z | No official fixed deck checklist was verified in the gathered evidence | Use the common investor questions and label the template as synthesis | A precise a16z-mandated slide order |
| Benchmark | No official fixed deck checklist was verified in the gathered evidence | Prepare for partner-level questioning and references | A precise Benchmark-mandated slide order |
| Khosla Ventures | No official fixed deck checklist was verified in the gathered evidence | Make technical risk, market, and founder edge legible when relevant | A precise Khosla-mandated slide order |
| Lightspeed | No official fixed deck checklist was verified in the gathered evidence | Make the wedge, distribution, and scale path explicit when relevant | A precise Lightspeed-mandated slide order |

The decision implication is important. A founder should not spend time reverse-engineering a supposed secret template. Make the company legible using the published YC and Sequoia anchors, then customize the proof and diligence for the partner's thesis. The absence of a verified public checklist is itself a reason to avoid false authority.

## The One-Pager and Data Room: Forwardable Truth

### The one-page standard

A one-pager is not a smaller deck with unreadable type. It is a forwarding instrument: a partner, angel, or founder should be able to send it to another investor without adding a paragraph of explanation. YC's title-page rule supplies the top: company name plus a one-line description [20]. The rest should compress the same causal story that appears in the deck.

| Block | Required content | Pass condition |
|---|---|---|
| Header | Company, one-line outcome, founder contact, link to product | A recipient knows what the company does in one glance |
| Problem | Exact user and expensive or frequent pain | The problem is concrete enough to identify a buyer or user |
| Solution | Mechanism and outcome in two or three sentences | A non-expert can explain the product back |
| Proof | One dated headline metric plus supporting customer or usage evidence | Every number has a definition, period, and source system |
| Business | Buyer, pricing or monetization hypothesis, sales or distribution motion | The reader sees how usage could become a business |
| Market and insight | Initial wedge, expansion path, why now, non-obvious insight | The opportunity is more than a generic large market |
| Team | Founders, roles, and problem-specific credibility | No advisor name-dropping in place of founder fit [20] |
| Raise | Amount, use of funds, next milestone, and contact CTA | The request is tied to a measurable change in the company [20] |
| Proof links | Product, short demo, customer references where appropriate, data room link | The recipient can verify instead of trusting prose |

Keep the page visually spare. YC says the seed deck should be intentionally simple in design [20], and the same logic applies here. A one-pager can be a PDF, a clean web page, or a plain-text memo, but it should not require a live presentation to reveal the basic facts. If the company is pre-revenue, say so and substitute the strongest honest proof: repeated usage, design partners, signed pilots, deployment, or a customer who has changed behavior.

### The handoff into diligence

The one-pager should link to a compact data room, not dump an unorganized drive folder. At seed, the minimum credible folder contains the incorporation and ownership record, cap table, founder and employee equity status, IP assignment, material contracts, bank or payment evidence for revenue, product analytics definitions, customer references, and a technical overview. Investor diligence checklists explicitly include financials, legal documents, corporate records, cap table, IP ownership, and customer contracts [5].

This is where the one-pager earns or loses trust. A headline such as "500 users" must resolve to a definition such as accounts created, activated users, weekly active users, or paying customers. If the number is a cumulative total, label it as cumulative. If a customer is a pilot, label it as a pilot. If a back-office operator manually delivers the service, explain that instead of presenting it as automation.

Airbnb and Coinbase are useful historical examples because their public seed artifacts can be studied as compact narratives: Airbnb's deck is described as a 10-slide, $600K seed fundraising artifact [10], while the Coinbase source labels its 2012 deck as seed with 11 slides [6]. Their historical success does not make their exact layouts a modern rule. The transferable lesson is that the page must expose the idea, proof, and path to scale quickly.

## Traction: Turning Early Usage Into Verifiable Proof

### What counts at seed

Seed investors do not require one universal metric. They require evidence appropriate to the business model and an explanation of how today's evidence becomes tomorrow's growth. YC's consumer metrics material explicitly separates growth rates from organic versus paid growth [9], and its search result states that **15% month-over-month growth** is good while **10%** is acceptable for a consumer company [9]. Treat those figures as a YC consumer benchmark, not a cross-sector law.

| Company type | Strong seed proof | What to show beside it | Weak substitute |
|---|---|---|---|
| Consumer | Weekly or monthly active users, activation, repeat use, retention cohorts, organic growth | Cohort definition, period, channel mix, and behavior after first use | Downloads, waitlist size, social impressions |
| B2B SaaS | Paying customers, net new MRR or ARR, expansion or renewal, usage depth, sales cycle | Contract status, invoice or payment evidence, customer segment, churn definition | Logos without contract status or a pipeline labeled as revenue |
| Marketplace | Transactions, repeat rate, liquidity, supply and demand activity, take rate or monetization evidence | Geography, cohort, buyer and seller sides, manual matching disclosed | Registered users on one side only |
| Developer or AI product | Active teams or developers, retained workflows, successful task completion, deployment, usage intensity | What counts as a successful task, model or infrastructure cost, customer permission, failure rate | A polished demo with no recurring external users |
| Pre-revenue deep tech or enterprise | Signed design partners, paid pilots, deployments, procurement progress, validation milestones | Pilot scope, conversion condition, timeline, technical validation, reference contact | Non-binding interest, anonymous quotes, or a logo wall |

The investor is testing a causal chain: acquisition creates activation; activation creates repeated value; repeated value creates payment or a credible route to payment; the economics and distribution can improve with capital. YC's deck guidance says to show traction if available and make the numbers clear and meaningful [20]. It also says revenue would be better when available, without implying that a pre-revenue company is automatically disqualified [20].

### How to present it honestly

Use a chart with a date axis, a definition, a denominator, and an annotation for any discontinuity. Show gross and net where relevant. Separate organic, paid, founder-sourced, partner-sourced, and internal traffic. Report pilots as pilots, bookings as bookings, contracted revenue as contracted revenue, and recognized cash revenue as cash revenue. Keep a metric dictionary in the data room so an investor can reproduce the deck chart.

Do not smooth the curve to tell a better story. YC explicitly says the curve is unlikely to be smooth [20]. A discontinuity is often valuable if the founder can explain it: a product launch, pricing change, channel experiment, seasonality, or a founder-led onboarding campaign. The question is not whether the first growth was scalable. Paul Graham's YC essay says one of YC's common types of advice is to do things that do not scale [17]. The question is whether the manual work uncovered a repeatable customer need and a path to reduce the marginal effort.

Stripe and Airbnb illustrate this distinction. Early Stripe manually signed users up for traditional merchant accounts behind the scenes [17]. Airbnb founders went door to door in New York to recruit users and improve listings [17]. Those actions are credible evidence of founder agency and learning, not evidence that the eventual company already had scalable distribution. Present them as experiments and service work, then show what repeated without the founders.

### Real company versus demo

A demo proves that a path can be made to work once. A company proves that external people return, pay, refer, renew, deploy, or otherwise incur a meaningful cost to continue. A seed-stage company can have small absolute numbers, but it should know exactly what each number means and who generated it.

The red flags are not low revenue alone. They are unexplained totals, no cohort view, unverified customer logos, a product that only works with the founder present, a demo account mistaken for a customer account, a chart with no denominator, and a pipeline presented as closed business. The remedy is not to hide early-stage limitations. It is to make the limitations explicit and state the next experiment that will resolve them.

## Website and Demo: The Public Conversion Layer

### The website standard

The seed website has two audiences with different jobs. A prospect asks, "Can this solve my problem?" An investor asks, "Is there a real product, a real user, and a credible path to scale?" A single page can serve both if it leads with the customer outcome and makes proof inspectable. Third-party startup-site guidance frames evaluation around clarity, velocity, proof, trust, and conversion [27], while another guide says the site should inform visitors, provide value, and convert them into subscribers, trial users, or customers [24]. Investor-oriented guidance specifically discusses hero sections and landing pages [25].

| Page layer | Standard | What the visitor should see | Seed-stage failure |
|---|---|---|---|
| Hero | One user, one painful job, one outcome | A plain-language headline, subhead, product image or short demo, and one CTA | Vague category language such as "the future of work" |
| Problem and audience | Name the user and the current workaround | A concrete before state and why the issue matters | A market-size speech with no buyer |
| Product proof | Show the core workflow | Interactive demo, short video, screenshots, sandbox, or live product | Animation that never reaches a real outcome |
| Evidence | Make adoption legible | Customer names with permission, quantified use, quotes with context, integrations, or case study | Anonymous logos or unverified claims |
| Business model | Remove the right amount of buying uncertainty | Pricing, starting price, pilot path, or clear contact route | Hiding all commercial reality while claiming traction |
| Trust and risk | Answer the obvious objection | Security, privacy, reliability, deployment, support, and founder contact as relevant | Enterprise claims without security or operating detail |
| Conversion | Give each audience a next step | Start, request access, book, install, or contact founder | Five competing CTAs and no working path |

The website should not promise more than the product and data room can support. If the demo uses seeded data, label it. If the product is invite-only, say what a visitor receives after requesting access. If pricing is still being tested, publish the pilot structure or state that pricing is custom; do not use "contact us" to conceal the absence of a business model.

### Examples and the causality limit

Airbnb's early deck offers a good copy test: its story begins with a concrete problem and a simple product proposition, which is why Sequoia cites it as an example of clarity and ambition [19]. Coinbase's early deck is explicitly described as opening with clear branding and positioning [6]. Those are useful patterns for a hero and product explanation, but the gathered evidence does not prove that a particular website converted investors or customers.

That limitation should be stated plainly. A site can be an excellent public proof surface without being the cause of a financing outcome. To produce defensible examples, record the site version, audience, traffic source, conversion event, customer cohort, and investor outcome. Without those data, call a page an example of clear communication, not a proven conversion machine. YC's public company directory can be used to assemble a live comparison set across sectors [28], but a directory listing alone is not customer or investor proof.

## Repo and Engineering Face: Technical Credibility in Public

### What a technical evaluator reads first

A public repository is not automatically a virtue. For a proprietary startup, the public artifact may appropriately be an SDK, CLI, demo application, protocol implementation, benchmark, or documentation repository rather than the production code. The standard is not "open source everything." The standard is that the visible engineering surface is honest, runnable, and coherent with the product claims.

| Engineering artifact | Minimum YC-grade standard | Evaluator test | Failure signal |
|---|---|---|---|
| README | What it is, who uses it, quickstart, prerequisites, environment variables, demo, architecture, limitations, license, and contact | A competent outsider reaches a working path quickly | README is a slogan, stale, or missing setup |
| Demo and examples | One canonical happy path with real inputs and expected outputs | Run the example from a clean environment | Screenshots replace execution or data is unexplained |
| Source layout | Clear modules, naming, interfaces, and boundaries | Find the core path without founder narration | A monolith, copied snippets, or no ownership boundaries |
| Tests | Tests for core behavior, edge cases, and failure paths | Run tests and inspect what they actually assert | Green tests that do not cover the product claim |
| CI | Automated build, test, lint, and relevant security checks on changes | Observe repeatable checks and failure visibility | Tests only run on the founder's laptop |
| Docs and operations | Architecture note, deployment, migrations, observability, rollback, and incident ownership | Ask how the system behaves when a dependency fails | No operational model beyond the demo |
| Security | No committed secrets, input validation, access control, dependency hygiene, and a vulnerability-reporting route | Try the documented security path and inspect history | Secrets in git, public sensitive data, or no response channel |
| IP and dependencies | Ownership of code, licenses, model/data rights, and third-party terms | Reconcile repository, contracts, and cap table/IP records | Unclear contractor ownership or incompatible licenses |

Technical diligence sources identify documentation debt, testing gaps, and key-person risk as risks that can affect software transactions [4]. GitHub provides a formal repository security-policy mechanism [15]. Independent judging guidance also calls for a README that explains setup, deployment, and environment variables, intuitive UX, recorded architecture decisions, and security controls [29]. These are not promises that an investor will read every line of code. They are the minimum that prevents the first technical review from becoming a credibility failure.

### The evaluator path

Make the path explicit: README -> install -> run example -> run tests -> inspect CI -> read architecture note -> report a vulnerability or question. For a private production system, provide a controlled technical diligence packet: architecture diagram, deployment topology, data flows, access model, incident history, test coverage summary, dependency and license report, and a live walkthrough with the engineering lead.

Do not optimize the repo for visual theater. A star count, a large commit graph, or a generated benchmark is weak evidence unless it translates into product use. Conversely, a small repository can be credible if it explains what is public, what is private, how the system is deployed, and which claims the evaluator can reproduce. The engineering face should reduce uncertainty, not create a second marketing narrative.

## Real Company Signals: What Investors Verify

### Observable signals

The strongest early-stage signal is not a polished artifact. It is founder-controlled movement in the real world. Paul Graham writes that startups do not simply take off by making a product available; the founders often make them take off [17]. He also describes recruiting users manually as a common unscalable founder task [17]. This explains why manual sales, onboarding, and customer support can be positive at seed when they produce learning and repeat behavior.

| Signal | Why it matters | Direct verification | False positive to avoid |
|---|---|---|---|
| Repeated external usage | Shows value beyond a one-time demo | Product analytics, cohort query, customer screen share, usage export | Total accounts or a founder's test account |
| Payment or committed budget | Shows economic value | Bank/payment processor, invoice, contract, procurement record | Letter of intent described as revenue |
| Retention or renewal | Shows value persists after novelty | Cohort table, renewal record, cancellation reasons, customer reference | Aggregate activity with no cohort definition |
| Founder agency | Shows the team can create motion before scale | Customer references, sales logs, onboarding history, experiment record | Inflated growth credited to an unrepeatable paid campaign |
| Product reality | Shows the claimed outcome happens in a real environment | Live product, deployment, logs, failure modes, support history | A scripted demo or unreleased roadmap feature |
| Founder-market fit | Explains insight and execution advantage | Specific prior work, customer knowledge, technical ownership, references | Famous resume with no connection to this problem |
| Ownership and clean company | Makes financing and future transactions possible | Incorporation, cap table, IP assignments, contracts, option records | Verbal ownership or unassigned contractor code |
| Technical control | Shows the product can survive the next stage | Repository or technical diligence, tests, CI, security, architecture review | One engineer who alone understands production |
| Learning velocity | Shows experiments change decisions | Dated experiments, metric changes, pivots, customer evidence | Constant feature shipping with no decision record |

Airbnb's door-to-door listing work and Stripe's manual merchant-account setup show the correct interpretation of early manual work [17]. The founders were not pretending the process was scalable; they were reducing the distance between a user and a useful product. That is materially different from claiming automated scale before it exists.

### What gets checked directly

A seed diligence process typically starts with the claims most likely to create legal or economic risk. The gathered checklist evidence names financials, legal documents, corporate records, cap table, IP ownership, and customer contracts [5]. In practice, investors also reconcile the deck's operating claims to product analytics, payment records, invoices, contracts, customer references, and the technical system. The founder should prepare these records before the meeting rather than assemble them after a skeptical question.

The team slide receives direct scrutiny because YC calls it especially important at seed [20]. Investors test whether the founders know the user's workflow, can explain every important metric, understand the product's failure modes, and have personally done the work that created the early signal. A founder who cannot explain a chart without a growth consultant, or a product without an engineer, creates a key-person and control concern even if the surface package looks polished.

A real company also has negative knowledge. It knows which customers churned, which experiment failed, which metric is cumulative, what is still manual, what is not yet secure, and which milestone the raise will not achieve. This is the operational meaning of validated learning: startups turn ideas into products, measure customer response, and decide whether to pivot or persevere.

## Synthesis: One Truth, Different Jobs

The artifacts differ in mechanism, scope, time horizon, and risk. The live pitch optimizes for comprehension under severe time pressure. The deck optimizes for a coherent narrative that survives asynchronous reading. The one-pager optimizes for forwarding. The website optimizes for independent customer and investor discovery. The repo optimizes for reproducibility and technical trust. The data room optimizes for legal and economic verification.

| Surface | Mechanism | Time horizon | Main trade-off | Winning evidence |
|---|---|---|---|---|
| Demo Day pitch | Attention and recall | Seconds to minutes | Compression versus nuance | Clear problem, product, proof, and ask |
| Seed deck | Causal narrative | Minutes to a follow-up meeting | Completeness versus cognitive load | Dated proof connected to insight and model |
| One-pager | Forwardability | Days of investor circulation | Brevity versus context | A stranger can forward it accurately |
| Website | Self-serve conversion | Continuous public discovery | Trust versus speed | Product path and proof work without founder help |
| Repo | Reproducibility | Hours to technical diligence | Transparency versus IP/security | Clean setup, tests, CI, architecture, security |
| Data room | Verification | Weeks of diligence | Disclosure versus confidentiality | Claims reconcile to records and references |

Three tensions should shape the final standard. First, YC asks for a concise narrative while diligence demands detail; the answer is not a longer pitch, but a short pitch with linked evidence. Second, manual founder effort can create early traction while investors still need a path to repeatability; disclose the manual process and measure what happened after it. Third, public polish can attract a first meeting while technical, customer, and ownership truth decides whether the company survives diligence.

The practical build order is: establish one-line truth; write the problem and solution; create a reliable product path; instrument the metric definitions; publish the website; package the deck and one-pager; then prepare the technical and legal evidence. Rehearse the live pitch only after the underlying claims are stable. If the package cannot survive a direct question, changing the slide design will not solve the problem.

## HONESTY: What Cannot Be Faked at Seed

Some seed-stage conditions can be small, early, or manual. They cannot safely be fictional. A company may have no revenue, but it cannot call a waitlist revenue. It may acquire users one by one, but it cannot call founder-assisted usage organic scale. It may show a prototype, but it cannot describe an unreleased integration as live production. It may have a tiny repo, but it cannot imply that a screenshot proves reliability.

Investors can verify repeated behavior through analytics and customer references; payments through processor or bank records; contracts through executed documents; ownership through corporate, cap-table, and IP records; product reality through a live environment and logs; technical control through code, architecture, tests, and deployment; and security through access controls, history, and a reporting route. The diligence checklist explicitly names financial, legal, corporate, cap-table, IP, and customer-contract evidence [5]. Technical diligence flags documentation debt, testing gaps, and key-person risk [4].

The honest seed standard is therefore:

1. **Say exactly what the number means.** Include date, denominator, cohort, channel, and whether it is cumulative, active, contracted, or paid.
2. **Separate current reality from roadmap.** Mark prototype, pilot, beta, production, and manual service distinctly.
3. **Disclose assistance.** Founder-led sales, manual onboarding, seeded data, paid acquisition, and concierge operations are acceptable experiments when labeled.
4. **Make the next verification easy.** Provide a product path, metric dictionary, reference list, contracts, ownership records, and technical packet.
5. **Keep every surface consistent.** A contradiction between the deck, website, demo, repo, and data room is more damaging than a modest metric.
6. **Know the failure cases.** Explain churn, broken experiments, security gaps, and what the raise will change.

The final test is not whether the company looks like a Series B. It is whether a skeptical investor can see a small but real company: founders creating motion, users receiving value, evidence accumulating, ownership staying clean, and a credible next experiment funded by the seed round.

## References

1. *Demo Day | Y Combinator*. https://www.ycombinator.com/demoday
2. *Continuous integration - GitHub Docs*. https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration
3. *Pitch Deck Teardown, a series from TechCrunch*. https://techcrunch.com/tag/pitch-deck-teardown
4. *Technical due diligence before acquiring a software company*. https://madewithlove.com/blog/technical-due-diligence-software-acquisition
5. *VC Due Diligence Checklist: Pre-Seed to Series B & Beyond*. https://kruzeconsulting.com/blog/due-diligence-checklist
6. *Coinbase Pitch Deck (2012) - Seed Deck That Raised Seed round | VCMatch*. https://vcmatch.ai/pitch-decks/coinbase-seed
7. *YC's essential startup advice  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice
8. *A guide to seed fundraising  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising
9. *Consumer Startup Metrics  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/KT-consumer-startup-metrics
10. *Airbnb's Pitch Deck: The Original 2009 Deck That... | VC Beast*. https://vcbeast.com/airbnb-pitch-deck-original-2009-analysis
11. *Technical Due Diligence for AI Startups | 100x Engineering*. https://100xai.engineering/blog/technical-due-diligence-ai-startup
12. *How to Pitch Your Company  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/4b-how-to-pitch-your-company
13. *Startup = Growth*. https://www.paulgraham.com/growth.html
14. *Demo Day FAQ | Y Combinator*. https://www.ycombinator.com/demoday/faq
15. *Adding a security policy to your repository - GitHub Docs*. https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository
16. *A Guide to Demo Day Presentations | Y Combinator*. https://www.ycombinator.com/blog/guide-to-demo-day-pitches
17. *Do Things that Don't Scale*. https://www.paulgraham.com/ds.html
18. *Guides · The ReadME Project · GitHub*. https://github.com/readme/guides/
19. *Writing a Business Plan | Sequoia Capital*. https://sequoiacap.com/article/writing-a-business-plan/
20. *How to build your seed round pitch deck  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck
21. *Stripe Pitch Deck That Raised $4.5B (Detailed Slide Breakdown) - Upmetrics*. https://upmetrics.co/pitch-deck-examples/stripe
22. *Pitch Deck Teardown: DeckMatch's $1M seed deck | TechCrunch*. https://techcrunch.com/2023/08/18/sample-seed-pitch-deck-deckmatch
23. *How Airbnb raised $600k at seed from Sequoia in 2009 ...*. http://suprdeck.com/case-studies/airbnb-seed-round-2009
24. *How to Structure a Startup Website that Converts*. https://startupdevkit.com/how-to-structure-a-startup-website-that-converts/
25. *Investor-Friendly Startup Website Design Tips | Waveup*. https://waveup.com/blog/how-to-make-your-startup-website-design-investor-friendly
26. *http://angelhack.com/blog/hackathon-tips-for-winners*. http://angelhack.com/blog/hackathon-tips-for-winners
27. *Best Startup Website Design Examples 2026: Stage-by-Stage ...*. https://hedrick.io/post/best-startup-website-design-examples-2026
28. *The YC Startup Directory*. https://www.ycombinator.com/companies
29. *http://ohack.dev/hackathon-judging-criteria*. http://ohack.dev/hackathon-judging-criteria
