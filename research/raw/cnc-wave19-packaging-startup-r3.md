# The Seed-Stage Startup Package: Evidence, Artifacts, and Execution

## Executive Summary

A YC-level seed package is not a pile of polished files. It is a single evidence system in which the deck, one-pager, product, website, repository, metrics, and diligence room all make the same claim in different formats. YC's pitch guidance frames the first objective as creating enough interest for a follow-up rather than attempting to explain the whole business in one meeting. [19] YC's deck guidance organizes the story around the company, problem, solution, traction, insight, business model, market, team, and ask. [1] The practical implication is that founders should optimize for fast comprehension, verifiable proof, and a clear next step rather than decorative completeness.

- **Narrative coherence**: YC's canonical deck guidance moves from the company and problem through solution, traction, insight, business model, market, team, and ask, while its pitch guidance emphasizes seven plain-language questions. [1] [19] -> Make every artifact answer the same seven questions with the same nouns, customer definition, and numbers.
- **Seed evidence**: YC advises founders to raise when they understand the market and customer, have a product that matches the market, and see adoption. [17] -> Present adoption and learning as the center of the package, and do not substitute a large theoretical market for customer evidence.
- **Metric honesty**: Retention and cohort behavior are more diagnostic than a single top-line number because they show whether users continue to receive value. [8] [22] -> Show a dated cohort table, define every denominator, and label forecast, pipeline, pilot, and paid revenue separately.
- **Conversion surface**: Landing-page guidance stresses message match, clear copy, a visible action, speed, and trust. [28] -> Build the website as a proof and routing layer for the exact audience named in the deck, not as an unbounded brand exercise.
- **Engineering credibility**: GitHub treats CI as automated building and testing, protected branches as a control over merge rights, secret scanning as history-wide credential detection, and Dependabot as dependency-alert infrastructure. [20] [11] [33] [5] -> Make the public repository reveal disciplined delivery without exposing secrets or customer data.
- **Investor reality test**: Diligence commonly spans finance, tax, legal, people, assets, technology, products, and sales, while technical diligence tests architecture, code quality, security, scalability, dependencies, and IP. [46] [6] -> Prepare a permissioned evidence room before a partner asks for it, and make each claim traceable to a document or system of record.
- **Twenty-four-hour boundary**: An MVP is the version that enables maximum validated learning with least effort, whereas customer development keeps burn low until a business model is validated by paying customers. [30] [25] -> A one-day build can test one risky behavior and produce a credible demo, but it cannot honestly compress retention, legal history, production reliability, or market learning into a day.
- **Decision rule**: The best seed package is internally consistent, explicitly qualified, and easy to falsify. That follows from the contrast between YC's emphasis on simple explanations and investor diligence's demand for underlying records. [19] [7] -> Remove any claim that cannot survive a customer, code, financial, or legal cross-check.

### Executive decision matrix

| Artifact | Decision it must enable | Minimum evidence standard | Failure mode to avoid | Source URL |
|---|---|---|---|---|
| Pitch deck | Decide whether to take a serious follow-up | Plain-language company, problem, solution, proof, team, and ask in a coherent sequence. [19] | A visually polished deck that never states what the company does. [19] | https://www.ycombinator.com/library/4b-how-to-pitch-your-company [19] |
| One-pager | Decide whether to remember and route the opportunity | One or two pages with vision, product, team, location, contact, traction, market, and financing context. [17] | A brochure with no ask, no traction definition, or no contact path. [17] | https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising [17] |
| Metrics pack | Decide whether demand repeats | Dated revenue, growth, churn, retention, cohorts, and definitions that distinguish paid from pipeline. [8] | Vanity totals without cohorts or denominator. [22] | https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention [8] |
| Website | Decide whether a visitor should sign up, book, or request access | Message match, clear copy, visible action, trust signals, and acceptable performance. [28] | An attractive page that makes the visitor infer the product and next step. | https://unbounce.com/landing-page-articles/landing-page-best-practices |
| Repository | Decide whether the team can ship safely | README, tests, CI, dependency and secret controls, review controls, and understandable history. [20] [33] | A demo repository that cannot be built or whose credentials are exposed. [33] | http://docs.github.com/en/code-security/concepts/secret-security/secret-scanning [33] |
| Diligence room | Decide whether claims survive verification | Corporate, financial, tax, legal, people, customer, product, technical, and IP evidence. [46] [6] | An improvised folder with conflicting versions and missing approvals. [44] | https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital [46] |
| Twenty-four-hour build | Decide whether one risky behavior is worth testing | A narrow hypothesis, working path, instrumentation, and explicit non-goals. [30] [37] | Calling a clickable mock a validated company. [24] | https://www.gv.com/sprint [37] |

The matrix is intentionally asymmetric: the deck compresses, the data room expands, and the build isolates uncertainty. That asymmetry is a design requirement, not inconsistency, because each artifact serves a different decision while preserving the same underlying facts. [19] [7]

## 1. The Seed Pitch Deck: Canonical Order, Proof Burden, and Named Examples

### 1.1 What the deck is for

A seed deck is a decision document for earning the next conversation. YC explicitly says the purpose of the pitch is to get an investor interested enough to follow up, not to present the entire business in one sitting. [19] This changes how a founder treats detail: the main deck should establish the thesis and the evidence, while an appendix and data room hold the material needed for verification. YC also says the pitch should be clear and concise and should answer seven questions, including what the company does, what problem it solves, why now, how it makes money, how big it can become, who the team is, and what the ask is. [19]

The canonical sequence is therefore a compression algorithm. The title and one-line description establish category and identity; the problem creates urgency; the solution makes the mechanism concrete; traction establishes that someone acts; insight explains why this team sees a non-obvious path; business model and market explain the economic opportunity; team explains founder-market fit; and the ask defines the next financing step. YC's deck guide names these sections in that order. [1] A founder can combine or split slides, but changing the logic without replacing its evidence usually creates a comprehension gap.

YC's language rule is particularly important for technical founders. The pitch guide warns against jargon, acronyms, marketing language, and ambiguous words such as platform when they hide the actual product. [19] It also asks founders to describe what they do in simple language. [19] The implication is not that the product must be simple; it is that the explanation must give the listener a stable object, user, action, and outcome.

### 1.2 Slide-by-slide operating standard

**Slide 1 - Company and one-line description.** Put the company name, a short description, and the intended customer or use case on the opening slide. YC's deck guide begins with the company and a one-line description, and its pitch guide says a company should be explainable in simple language. [1] [19] The one-line description should be testable: it should allow a reader to tell whether a later customer or competitor belongs in the same category.

**Slide 2 - Problem.** Describe a costly, frequent, or strategically important problem in the customer's words. YC's deck guide treats the problem as a distinct section and says the founder should convey why the problem matters. [1] Do not turn this into a list of broad frustrations; show the current workaround, its cost, and the moment at which a buyer feels the pain.

**Slide 3 - Solution and product.** Show the minimum product path that resolves the stated problem. YC's guide separates the solution from the problem and recommends explaining how the product works rather than hiding it behind category language. [1] A screen, workflow, or before-and-after can be more useful than a feature inventory because it connects mechanism to outcome.

**Slide 4 - Traction.** Show adoption, revenue, engagement, retention, or other evidence appropriate to the business model. YC lists traction and metrics as a distinct deck component. [1] If the company is pre-revenue, replace false precision with evidence of user behavior, repeat usage, paid pilots, waitlist quality, or a measurable learning milestone and label it accurately.

**Slide 5 - Insight or why now.** Explain the non-obvious fact that makes the opportunity newly possible or makes the team unusually suited to pursue it. YC calls out insight as a separate component. [1] An insight is not a slogan; it should change the product, distribution, economics, or timing of the business.

**Slide 6 - Business model.** Explain who pays, what triggers payment, pricing logic, gross-margin drivers, and how distribution reaches the payer. YC's guide includes business model and market as separate sections. [1] DocSend's deck research similarly finds that investors spend more time on the business model and want to see how the model makes money and how it can evolve, even when every detail is not yet solved. [40]

**Slide 7 - Market.** Define a reachable initial market and the expansion path. YC includes market size, but the evidence burden is reasoning, not only a large top-down number. [1] DocSend reports that the market section usually occupies one to three pages and that investors care about the reasoning behind the numbers. [2]

**Slide 8 - Competition and differentiation.** State the alternatives, including doing nothing, and show the specific advantage that matters to the buyer. DocSend reports that competitive landscape received substantial attention and that the deck should explain why the product is unique. [40] A two-by-two chart is optional; a concrete switching reason is mandatory.

**Slide 9 - Team.** Show the founders, relevant experience, roles, and the reason this team can learn or execute faster than a generic team. YC's deck guide includes the team, and DocSend identifies the team slide as a must-have. [1] [2] DocSend also reports that investors look for context, logos or prior companies where relevant, and links or evidence that make the founders legible. [2]

**Slide 10 - Ask and use of funds.** State the amount, instrument or round context when appropriate, milestone target, and how the money changes the company's state. YC's deck guide includes the ask. [1] YC fundraising guidance says founders should raise enough to reach the next fundable milestone or profitability, with a typical 12-to-18-month milestone horizon. [17]

A founder may use a different number of slides, but each deviation should preserve the underlying decision sequence. DeckMatch's reviewed deck was described as a tight 14-slide deck, which shows that canonical logic does not require a rigid ten-slide count. [13] The correct question is whether a reader can reconstruct the company, customer, proof, economics, team, and ask without a live narrator.

### 1.3 What top seed decks teach by contrast

The named examples are useful because they show different kinds of proof rather than one universal template. The Airbnb example is a market-making narrative: a problem around renting space to travelers, a web platform, a large market ambition, a commission model, and a transaction goal. [48] [48] [48] [48] [48] Its lesson is to make the marketplace mechanism and transaction unit visible, but its limitation is that a retrospective teardown or template is not the same as a primary investor file. Any claim about exact original slide wording beyond the available analysis is therefore (UNVERIFIED).

Coinbase demonstrates a different constraint. Brian Armstrong's retrospective account says the original fundraising email said there was no deck, while the available material came from a demo-day presentation; the round had $320K committed and aimed to close at $1M. [12] [12] [12] This is evidence that a company can earn interest with a concise artifact and a strong product thesis, but it is not evidence that a deck is unnecessary for every seed company. The transferable lesson is to remove slides that do not increase belief, not to imitate the absence of a deck.

Stripe's example shows how a technical insight can be made legible. The company was framed as payments infrastructure, with a two-week integration problem and a solution that could be implemented in seven lines of code; the seed story also paired a large commerce opportunity with a closed beta waitlist of 10,000 developers. [38] [38] The mechanism is more persuasive than a broad claim about digitization because the buyer can imagine the integration, while the waitlist shows that the proposed solution has a route to users.

Notion's early deck analysis shows the value of a precise product category and adoption narrative. The company began as a tool for notes, tasks, wikis, and databases; the founders were Ivan Zhao and Simon Last; the analysis describes a small team and approximately $2M of seed funding. [26] The deck's opening language positioned the product around the future of work and put documents, tasks, notes, and projects in one shared workspace. [26] [26] The lesson is to describe the product as a repeated workflow, not as a bag of features.

Linear illustrates a timing and evidence caveat. The source describes a Series A deck, a $13M round led by Sequoia, and later metrics such as more than $400M in ARR, 2,000 teams, and an NPS of 70. [34] [34] Those later numbers are not seed-stage requirements; they are a reminder that a deck is a time-stamped argument. A seed founder should never import a later-stage proof standard or present a later outcome as though it existed at the seed date.

DeckMatch's teardown is helpful for attention economics. Its deck was described as lightly redacted, with upcoming hires and an appendix removed, and its ask was EUR 1M placed at the bottom right. [13] [13] The source also notes that VCs receive thousands of inbound decks and that DeckMatch evaluates decks and automates parts of inbound communication. [13] The tradeoff is between minimalism and discoverability: an ask can be visually quiet, but it must still be findable in seconds.

### 1.4 Pitch-deck data table

| Deck section | What belongs on it | Named example and lesson | Source URL |
|---|---|---|---|
| Company and one-line description | Name, category, customer, and plain-language description that can be repeated accurately. [1] [19] | Notion opened with a future-of-work framing and a shared workspace concept rather than a feature dump. [26] [26] | https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck [1] |
| Problem | Specific user pain, current workaround, consequence, and why the problem matters now. [1] | Stripe made integration time concrete by describing a two-week payments problem. [38] | https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck [1] |
| Solution and product | The smallest product mechanism that resolves the problem, shown through a workflow or demo. [1] | Stripe translated the solution into seven lines of code, making the mechanism legible to developers. [38] | https://www.billiondollarpitchdecks.com/decks/stripe [38] |
| Traction | Revenue, users, activation, usage, retention, waitlist quality, or other behavior with dates and definitions. [1] | Stripe paired a closed beta with a 10,000-developer waitlist. [38] | https://www.billiondollarpitchdecks.com/decks/stripe [38] |
| Insight and timing | Non-obvious fact that changes feasibility, distribution, economics, or urgency. [1] | Coinbase's retrospective story shows that a compelling product thesis can sometimes travel through a concise demo-day artifact. [12] | https://barmstrong.medium.com/the-coinbase-seed-round-pitch-deck-50c8ec91d40b [12] |
| Business model | Payer, pricing, transaction or subscription logic, gross-margin drivers, and evolution path. [1] [40] | Airbnb's analyzed deck made a 10% commission explicit. [48] | https://slidebean.com/templates/airbnb-pitch-deck [48] |
| Market | Reachable initial market, bottom-up assumptions, expansion path, and why the market can support venture scale. [2] | Airbnb's analysis connected a web platform to a large travel opportunity and a transaction goal. [48] [48] [48] | https://www.docsend.com/blog/three-pitch-deck-changes-that-make-vcs-pay-closer-attention [2] |
| Competition and differentiation | Alternatives, including status quo, and the buyer-specific reason to switch. [40] | DocSend's research says investors spend meaningful attention on competitive landscape and uniqueness. [40] | https://www.docsend.com/blog/how-your-pitch-deck-can-shine-as-vc-focus-shifts [40] |
| Team | Founder roles, relevant experience, founder-market fit, and links or context that make claims checkable. [2] [1] | Notion's analysis names Ivan Zhao and Simon Last and links the product thesis to their founding roles. [26] | https://www.docsend.com/blog/three-pitch-deck-changes-that-make-vcs-pay-closer-attention [2] |
| Ask and milestone | Amount, round context, use of funds, and the next fundable milestone or profitability target. [17] [1] | DeckMatch's reviewed deck requested EUR 1M, although the ask was visually tucked away. [13] | https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising [17] |
| Appendix and diligence handoff | Detailed cohorts, pipeline, architecture, security, customer references, and legal or financial material that supports the main claim. [7] [6] | DeckMatch's main deck removed an appendix, illustrating why supporting material should remain available even when omitted from the narrative. [13] | https://kruzeconsulting.com/blog/due-diligence-checklist [7] |

The table's key decision is not whether to copy Airbnb, Coinbase, Stripe, Notion, Linear, or DeckMatch. It is whether the deck makes the smallest number of claims necessary for a follow-up while leaving a clean evidence trail for every important claim. YC's emphasis on interest and follow-up supports brevity, while diligence requirements support an expandable appendix and room. [19] [7]

### 1.5 Recommended seed-deck build process

First write the seven-question narrative in plain text before designing slides. YC's pitch guide explicitly treats the company description, customer, problem, solution, why now, business model, market, team, and ask as the core questions. [19] Second, attach one evidence object to each answer: a customer quote, product screenshot, cohort, transaction log, experiment, cap-table record, or founder credential. The evidence object should have a date and definition so that a reviewer can reproduce the claim.

Third, build a skeptical version of the deck. Replace adjectives such as huge, viral, best, and revolutionary with a customer action, a denominator, or a measured outcome. This is consistent with YC's warning against marketing language and ambiguous platform descriptions. [19] Fourth, test the deck on someone who does not know the company and record the questions they ask before adding more slides; questions reveal missing causal links better than decoration.

Finally, create a claim ledger. For each number, list the source system, date, definition, owner, and whether it is actual, forecast, pipeline, or illustrative. This recommendation follows from the tension between a short narrative deck and a due-diligence process that asks for underlying records. [17] [46] The result is a deck that is brief without being brittle.

## 2. The One-Pager and Executive Summary: The Investor's Routing Document

### 2.1 Role, length, and format

YC's fundraising guidance says an executive summary can accompany the deck and be left behind, and it describes the summary as one or two pages, with one page better. It names the required content as vision, product, team and location, contact information, traction, market size, and minimum financial information including revenue and current and prior fundraising. [17] That is the strongest available standard for a seed executive summary in this research corpus.

The one-pager is not a miniature deck with ten tiny slides. It is a routing document: a reader should understand the company, decide whether it fits their thesis, remember the proof, and know exactly how to reach the founder. YC's one-page preference implies a strict editing constraint. [17] A two-page version is justified when the business model or technical product truly requires a second page, but extra length should carry evidence rather than prose.

A useful implementation has eight blocks: identity and one-line description; problem and customer; product and workflow; traction and retention; market and business model; team and location; financing history and current ask; contact and links. The eight-block structure is an implementation recommendation, not a separately verified YC-mandated template, so any claim that YC requires these exact block labels is (UNVERIFIED). The underlying content is supported by YC's list of vision, product, team, location, contact, traction, market size, and financial information. [17]

Format should serve scanning. Use a strong headline, short paragraphs, a compact proof row, a small chart or cohort snapshot when it adds information, and links to the full deck, demo, repository, and data room when permissioned. A one-pager should not require a live explanation to define the customer or the ask. Fundreef's summary describes the one-page document as a hook for a meeting and emphasizes value proposition, market, traction, team, and funding ask. [23] It also describes a 30-to-90-second reading window, which supports writing for rapid triage rather than exhaustive narrative. [23]

### 2.2 Content standard by element

**Identity.** Put the company name, URL, contact, location, round stage, and one-line description at the top. YC specifically names location and contact information as executive-summary content. [17] The one-line description should use the same nouns as the deck and website so that an investor never has to reconcile three categories.

**Vision and problem.** State the future the company is building, then the current problem that makes the future economically relevant. YC names vision, while its pitch guidance asks founders to explain what the company does and what problem it solves in simple language. [17] [19] Avoid using the vision as a substitute for a customer.

**Product.** Show what the user does and what the company delivers. YC names product explicitly. [17] A single screenshot, flow, or before-and-after can outperform a paragraph if it preserves enough context to explain the action and outcome.

**Traction.** Present the most decision-relevant proof with date and definition. YC names traction and revenue among minimum financial information. [17] If there is no revenue, state the actual user behavior and the missing proof rather than inventing a proxy.

**Market and model.** State the initial customer segment, reachable market logic, pricing, and expansion path. YC names market size, while its deck guidance names business model and market as separate sections. [17] [1] The one-pager should not force the reader to infer whether the market number is top-down, bottom-up, or merely adjacent.

**Team.** Name founders, roles, relevant experience, and location. YC explicitly includes team and location. [17] The detail should answer why this team can learn or execute on this problem, not merely list prestigious affiliations.

**Financing.** State prior funding, current round or ask, and what milestone the financing buys. YC says the minimum financial information includes current and prior fundraising and suggests raising to reach the next fundable milestone or profitability. [17] [17]

**Links.** Include the deck, product, demo, website, repository if public, and founder contact. A link should reduce verification time rather than create a maze. The recommendation follows from YC's description of the summary as a leave-behind and from diligence checklists that require access to underlying evidence. [17] [7]

### 2.3 One-pager case study and tradeoffs

A one-pager is strongest when it makes one causal chain visible: customer pain leads to product behavior, which leads to measured adoption, which supports a business model, which supports the ask. The one-page format forces the founder to choose a primary proof point. That constraint is beneficial because a reader can remember one strong cohort or customer outcome more easily than ten loosely related metrics. YC's one-page preference supports this compression. [17]

The tradeoff is that compression can conceal risk. A one-pager may omit the failed experiments, customer concentration, long implementation cycle, or technical limitation that a careful investor will later discover. The correct remedy is not to turn the one-pager into a risk register; it is to add a precise qualifier and link to the relevant appendix or data room. Diligence guidance expects the second layer. [7] [46]

A founder should also distinguish executive summary from teaser. A teaser optimizes for a click or meeting; an executive summary should give enough information to qualify the opportunity. Fundreef describes the summary as a hook for a meeting, but YC's list makes clear that the document still needs product, team, traction, market, contact, and financial context. [23] [17] Therefore the right design is a hook with substance, not a slogan sheet.

### 2.4 One-pager data table

| Element | Standard | Example implementation | Source URL |
|---|---|---|---|
| Header identity | Company name, one-line description, URL, contact, location, and stage. YC explicitly includes location and contact. [17] | Use the same one-line description as slide 1 and the website headline. [19] | https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising [17] |
| Vision | One sentence describing the future state the company is building. [17] | Pair the vision with a current customer problem so it does not float above the product. [19] | https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising [17] |
| Customer and problem | Identify the user, painful workflow, current workaround, and consequence. [19] | Write the problem in customer language and define who is excluded. [19] | https://www.ycombinator.com/library/4b-how-to-pitch-your-company [19] |
| Product | Explain the product action, output, and core workflow. [17] | Add one annotated screenshot or short demo link rather than a feature list. [1] | https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck [1] |
| Traction | Give dated adoption, revenue, engagement, retention, or other behavior with definitions. [17] [1] | Put the strongest cohort or repeated-use proof in a compact callout and link the full export. [8] | https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention [8] |
| Market | Define the initial segment, bottom-up opportunity, and expansion logic. [17] [2] | Explain assumptions behind the number instead of presenting a decorative TAM. [2] | https://www.docsend.com/blog/three-pitch-deck-changes-that-make-vcs-pay-closer-attention [2] |
| Business model | Identify payer, price, payment trigger, and margin logic. [1] | State what is actual, planned, or still being tested. [40] | https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck [1] |
| Team and location | Founders, roles, relevant experience, and location. [17] | Include why the team's background gives an execution or learning edge. [2] | https://www.docsend.com/blog/three-pitch-deck-changes-that-make-vcs-pay-closer-attention [2] |
| Financing history | Prior rounds, current raise, amount, instrument context, and milestone. [17] [17] | Use a compact financing line and link the detailed cap table in the room. [7] | https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising [17] |
| Contact and links | Direct founder contact plus deck, demo, website, and permitted repository or data room. [17] | Put one explicit next action: schedule, reply, or request access. [19] | https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising [17] |

The table should be treated as a content contract. If a required element is not available, write that it is not yet available rather than silently replacing it with an adjacent vanity statistic. YC's guidance supports minimum financial context, and the investor-room model supports traceable follow-up evidence. [17] [7]

### 2.5 Editing and verification workflow

Draft the one-pager after the deck narrative but before visual design. Copying slide text into a document usually produces a fragmented summary because slide headings depend on spoken context. The one-pager should instead use complete but short sentences and one clear proof artifact per major claim. YC's insistence on clear, concise pitching supports this editorial order. [19]

Run a five-question test: Can a reader state what the company does? Can they name the customer? Can they state the painful problem? Can they repeat the strongest proof and its date? Can they find the ask and contact? These questions operationalize YC's core pitch questions. [19] If a reader fails, edit the document before adding a new section.

Then run a claim reconciliation against the deck, website, metrics export, and cap table. The same revenue period, customer count, employee count, funding amount, and market definition must be identical or explicitly qualified across artifacts. This is an inference-based operating rule grounded in the fact that investors use the one-pager as a leave-behind and later request underlying documents. [17] [46]

## 3. Traction and Seed Metrics: Proving a Company Rather Than a Project

### 3.1 The seed metric principle

There is no universal seed-stage MRR, ARR, growth, or retention threshold that proves a company. YC's seed guidance says founders should raise when they understand their market and customer, have a product that matches the market, and see adoption. [17] The appropriate metric therefore depends on the product's purchase cycle, user behavior, pricing model, and stage of deployment.

The strongest seed metrics reveal repeated value. A revenue number shows that money changed hands, but retention and cohorts reveal whether the customer continues to receive value. YC's retention guidance treats cohort retention as a way to study whether users keep returning, while product-market-fit analysis often focuses on the shape of the retention curve rather than a single launch spike. [8] [22] For a transactional product, repeated transactions may matter more than monthly logins; for enterprise software, renewal, expansion, implementation completion, and usage by the buying account may matter more than free-user activity.

Metric definitions should be written beside the number. Baremetrics identifies MRR, ARR, CAC, LTV, churn, NRR, and NPS as common SaaS metrics. [14] Stripe's CAC guidance describes CAC as a customer-acquisition cost that should be interpreted relative to customer value and payback. [18] These metrics become misleading when founders change the time window, exclude failed payments, mix pilots with paying accounts, or calculate LTV from an unproven churn assumption.

### 3.2 Metric definitions and evidence

**MRR and ARR.** MRR is recurring monthly revenue; ARR is an annualized recurring revenue view. The important seed question is not merely the amount but the composition: new, expansion, contraction, reactivation, and churn. Baremetrics includes MRR and ARR in its standard metric set. [14] Show the source billing export, a period definition, and whether annual contracts are normalized.

**Growth.** Show month-over-month or quarter-over-quarter growth only when the denominator is meaningful. A small base can create a large percentage, and a one-time contract can distort the trend. YC's broader emphasis on traction and adoption supports showing the underlying customer or revenue series rather than only a percentage. [1]

**Churn.** Define logo churn, revenue churn, gross revenue retention, and net revenue retention separately. A customer can remain active while reducing spend, and a company can grow net revenue while losing smaller logos. ChartMogul's retention research discusses NRR as a measure whose level changes the growth outlook, and its cohort work emphasizes that retention is best examined by cohort. [21] [31]

**CAC and payback.** CAC should include the costs and time period used, with acquisition source separated when possible. Stripe explains that lower CAC relative to customer value enables a business to reinvest in acquisition. [18] A seed company should not state a precise payback period if implementation costs, founder time, onboarding labor, or sales commissions are excluded without disclosure.

**LTV:CAC.** LTV:CAC is a model, not a cash receipt. It depends on retention, gross margin, pricing, and acquisition cost assumptions. Use a sensitivity table with actual observed retention and a conservative scenario rather than one impressive ratio. Baremetrics and Stripe both frame these metrics as connected measures of SaaS economics rather than isolated badges. [14] [18]

**Activation and engagement.** Define the event that predicts value: first successful workflow, invited collaborator, processed transaction, or recurring use. A login count is not automatically activation. YC's product-market-fit guidance and cohort-retention approach support choosing behavior that connects to continued use. [22] [8]

**Cohorts.** Group customers or users by signup, activation, first payment, or contract start date, then show retention or revenue over time. Cohorts expose whether growth comes from new users masking decay in older cohorts. ChartMogul's cohort-oriented retention analysis supports this view. [31]

**Pipeline and pilots.** Pipeline, letters of intent, design partners, waitlists, and pilots are evidence of interest or learning, not recurring revenue. Stripe's early story distinguishes a closed beta waitlist from actual product adoption. [38] Label these states in the dashboard and keep them out of MRR and ARR.

### 3.3 How verification is presented

A good seed metrics slide has four layers. Layer one is a headline claim, such as recurring revenue or active accounts, with the period. Layer two is a small trend chart with labeled axes and no hidden denominator. Layer three is a cohort or retention view. Layer four is a footnote defining inclusion, exclusions, currency, gross versus net, and whether the number is actual or forecast. This structure is an implementation recommendation derived from YC's traction requirement and the retention literature's emphasis on cohorts. [1] [8]

The appendix should include a reconciled export. For revenue, reconcile the dashboard to the billing system and bank deposits; for customers, reconcile the customer list to contracts or account IDs; for usage, reconcile event definitions to product analytics; for churn, show cancellation date and effective period. These controls are recommendations, but they address the exact investor problem that financial and technical diligence is designed to expose. [46] [6]

Founders should also disclose uncertainty. If the company has only a few enterprise contracts, show customer concentration and contract timing. If usage is free, show conversion and repeat behavior rather than implying revenue. If churn has not stabilized, state that the estimate is immature. The absence of a universal seed threshold makes transparent uncertainty more informative than a copied benchmark. [17] [21]

### 3.4 Metrics data table

| Metric | Why it counts at seed | How top founders present it | Source URL |
|---|---|---|---|
| MRR | Shows recurring monetization when the revenue is truly recurring and reconciled. [14] | Give period, currency, new/expansion/contraction/churn bridge, and billing export link. [14] | https://baremetrics.com/blog/saas-metrics-checklist-kpis-founders-should-track [14] |
| ARR | Provides an annualized view of recurring revenue but can mislead if annualization is applied to one-off revenue. [14] | Label annualization method and separate contracted, invoiced, and collected amounts. [14] | https://baremetrics.com/blog/saas-metrics-checklist-kpis-founders-should-track [14] |
| Growth rate | Shows trajectory, but the denominator and base size determine its meaning. [1] | Display the underlying time series and customer or revenue base beside the percentage. [1] | https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck [1] |
| Logo churn | Reveals customer loss and should be separated from revenue churn. [21] | Show monthly and cohort churn with customer definition and cancellation timing. [21] | https://chartmogul.com/reports/saas-retention-the-new-normal [21] |
| Revenue churn and GRR | Shows contraction and loss before expansion masks weakness. [21] | Provide gross retention, net retention, and a bridge rather than one blended percentage. [31] | https://help.chartmogul.com/article/160-cohort-net-mrr-retention [31] |
| NRR | Shows whether an existing revenue cohort expands or contracts over time. [21] | Present cohort NRR by start month or quarter and disclose small-cohort volatility. [31] | https://help.chartmogul.com/article/160-cohort-net-mrr-retention [31] |
| CAC | Connects acquisition spend to new customers and future payback. [18] | Separate paid channels, sales labor, onboarding, and founder-led acquisition assumptions. [18] | https://stripe.com/resources/more/cac-in-saas [18] |
| CAC payback | Converts acquisition economics into a cash timing question. [15] | Show gross-margin basis, monthly cash recovery, and a conservative sensitivity case. [15] | https://stripe.com/resources/more/cac-in-saas [15] |
| LTV:CAC | Provides a directional unit-economics model, not proof by itself. [14] | Show observed retention, gross margin, and the formula so an investor can stress it. [14] | https://baremetrics.com/blog/saas-metrics-checklist-kpis-founders-should-track [14] |
| Activation | Measures the first behavior that predicts value, not a generic login. [22] | Define event, time window, denominator, and downstream retention correlation. [22] | https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention [22] |
| Cohort retention | Shows whether value persists after acquisition and whether new cohorts improve. [8] | Use signup or first-value cohorts, label incomplete cohorts, and show absolute counts. [8] | https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention [8] |
| Pipeline, pilot, or waitlist | Shows interest, learning, or future conversion potential but is not recurring revenue. [38] | Put it in a separate funnel with stage, date, owner, probability, and conversion history. [38] | https://www.billiondollarpitchdecks.com/decks/stripe [38] |
| NPS or qualitative proof | Can add customer voice and identify perceived value, but it is not a substitute for retention. [14] | Pair quotes or NPS with account behavior and specify sample and response rate. [14] | https://baremetrics.com/blog/saas-metrics-checklist-kpis-founders-should-track [14] |

The table's central control is classification. A founder can have strong seed evidence without high MRR if repeated behavior, customer urgency, or paid pilots fit the product's cycle, but the founder must name the evidence honestly. YC's adoption language supports context-specific proof, while retention analysis explains why repeated value is more diagnostic than a launch spike. [17] [8]

### 3.5 Case study: retention versus top-line theater

Suppose two companies report the same new-month revenue. Company A has a growing cohort curve, repeat use, and expansion within existing accounts; Company B has one large contract and declining use among the original cohort. The headline is identical, but the investor's risk is not. This is why cohort retention and NRR belong in the appendix even when the main deck has only one traction slide. ChartMogul's retention framing and YC's cohort guidance support looking at the shape of value over time. [21] [8]

The tradeoff is that cohorts can be noisy at seed. A few accounts can make retention look spectacular or disastrous, and enterprise contracts can have long renewal periods. The answer is not to hide the chart; it is to show absolute counts, segment by customer type, and label incomplete cohorts. That recommendation preserves the diagnostic benefit without pretending statistical stability that the evidence does not support. [31]

The practical presentation is a paired slide: one top-line chart and one cohort table. If the two disagree, explain the disagreement. A mature investor is more likely to trust a founder who surfaces the tension than one who supplies a single blended number. This is a recommendation grounded in the way cohort analysis distinguishes new-customer growth from existing-customer health. [8] [31]

## 4. The Seed-Stage Website: A Conversion and Proof Surface

### 4.1 The website's job

A seed website has three jobs: orient the right visitor, prove that the product exists and is credible, and route the visitor to one next action. Landing-page guidance emphasizes message match between the visitor's expectation and page copy, clear copy, an action visible above the fold, and speed. These are not merely design preferences; they reduce the amount of inference required before a visitor can act.

Trust is a conversion mechanism. Nielsen Norman Group's trustworthy-design guidance says trust affects willingness to risk time, money, or personal data and that losing trust can lose the sale or customer. [28] A seed company therefore needs enough evidence to be credible without pretending to have the history of a large incumbent. Clear ownership, contact paths, security explanations, customer proof with permission, and honest availability language can outperform invented social proof.

Performance is part of the product impression. web.dev's Core Web Vitals documentation defines a set of user experience signals, while its performance guidance frames speed as an engineering concern. [42] [35] A seed team need not build a complex optimization program on day one, but it should avoid a landing page whose heavy media, tracking, or animation obscures the call to action.

### 4.2 Recommended website architecture

**Hero.** State the customer, problem, product, and primary action in the first viewport. Do not write a category slogan that requires the visitor to scroll to learn what the product does. The message-match and above-the-fold guidance supports this structure.

**Proof strip.** Use a customer logo, quantified result, testimonial, waitlist count, integration, or founder credential only when it is accurate and permissioned. Trust guidance supports visible credibility, but it also implies that misleading proof damages trust. [28]

**Product path.** Show the workflow from input to outcome, ideally through a short demo, screenshots, or interactive example. YC's pitch guidance says the company should be understandable in simple language; the website can add visual detail without changing the explanation. [19]

**Use cases and audience segmentation.** Name the primary segment and the job they need done. Multiple segments should have separate paths if the product, proof, or call to action differs. This is a recommendation that follows from message match: one generic headline cannot optimize for incompatible expectations.

**How it works.** Explain the minimum steps, integrations, deployment or onboarding burden, and time to first value. This reduces uncertainty that would otherwise appear in a sales conversation. Technical products especially benefit from making implementation concrete, as Stripe's seed story did with a seven-line integration concept. [38]

**Pricing or qualification.** Show pricing when it is a self-serve product or explain why a conversation is required for enterprise pricing. A hidden price is not automatically wrong, but the visitor should know the next step and what information will be requested. The recommendation is consistent with YC's requirement to explain the business model and with trust principles. [1] [28]

**Security and reliability.** State data handling, authentication, hosting, status, and contact for security questions at the level the product warrants. Do not claim certifications or controls that are not present. Technical diligence explicitly examines security and scalability. [6]

**Resources and founder contact.** Provide docs, changelog, demo, case studies, and a direct contact path. For a developer product, the README and docs can be the highest-converting page because they let the evaluator test the product. GitHub's README guidance treats the README as a communication surface for a repository. [57]

**Single primary call to action.** Choose sign up, request access, book a demo, install, or join a waitlist based on the current product state. A page with five equal calls to action makes the visitor decide what the company wants. Landing-page guidance emphasizes a clear action.

### 4.3 Seed website tradeoffs and examples

A pre-product startup should not imitate the website of a scaled company. It should sell the next experiment. If the product is not ready, a waitlist should describe what the early user will receive and when, not imply general availability. Stripe's early narrative distinguishes a closed beta from a broader market, which is a useful model for labeling availability. [38]

A B2B product may need more proof and fewer visual effects. An investor or technical buyer may inspect documentation, integration effort, security posture, and customer evidence before converting. The engineering face and website should therefore share terms, screenshots, and claims. Technical diligence's focus on architecture, dependencies, and IP makes this cross-link important. [6]

A consumer product may need stronger emotional clarity and social proof, but the same rule applies: promise one experience and make the next action obvious. Trust guidance warns that visitors risk time, money, or data, so a seed brand should state who operates the service and how users can get help. [28]

The website should also be a claim firewall. If the deck says early access, the website should not say available to everyone; if the deck says pilots, the website should not show logos as paying customers; if the deck says encryption is planned, the website should not imply a completed security certification. These are operating recommendations derived from the need to reconcile artifacts before diligence. [46] [6]

### 4.4 Website data table

| Section | What it must contain | Seed-stage example or implementation | Source URL |
|---|---|---|---|
| Hero | Customer, problem, product outcome, and one primary action above the fold. | Use the same plain-language category as the deck and one action such as request access. [19] | https://unbounce.com/landing-page-articles/landing-page-best-practices |
| Message match | Copy that matches the ad, referral, deck, or search expectation that brought the visitor. | Create segment-specific landing pages when the customer and proof differ. | https://unbounce.com/landing-page-articles/landing-page-best-practices |
| Proof strip | Permissioned logos, quantified results, testimonials, integrations, or founder credibility. [28] | Label pilots, design partners, and customers separately so social proof remains honest. [38] | https://www.nngroup.com/reports/ecommerce-ux-trust-and-credibility [28] |
| Product demo | Visible workflow from input to outcome, with screenshots, video, or interactive example. [19] | Show the smallest successful path and link to docs or a live demo. [38] | https://www.ycombinator.com/library/4b-how-to-pitch-your-company [19] |
| Use cases | Specific jobs and audience segments rather than a generic list of industries. | Give each primary segment a proof point and next action. | https://unbounce.com/landing-page-articles/landing-page-best-practices |
| How it works | Setup, integration, onboarding, time to value, and key limitations. [38] | Make implementation effort concrete, especially for developer products. [38] | https://www.billiondollarpitchdecks.com/decks/stripe [38] |
| Pricing or qualification | Price, plan logic, or an honest explanation of why a sales conversation is needed. [1] | Do not hide the next step or collect more data than the product needs. [28] | https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck [1] |
| Security and data | Data handling, authentication, hosting, support, and accurate control statements. [6] | Link security notes and a contact; never imply an unearned certification. [6] | https://www.seedforge.com/blog/technical-due-diligence-for-startups [6] |
| Documentation | Install path, API or user docs, examples, troubleshooting, and ownership. [57] | Let a technical evaluator reach first success without a sales call when feasible. [57] | https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories [57] |
| Performance | A fast, stable page with attention to user-experience performance signals. [42] [35] | Compress media, avoid unnecessary scripts, and test the primary path. [35] | https://web.dev/articles/vitals [42] |
| Contact and CTA | One clear next action and a reliable support or founder route. | Use sign up, install, book, request access, or waitlist according to actual availability. [38] | https://unbounce.com/landing-page-articles/landing-page-best-practices |

The table is a conversion checklist, not a demand to build a large marketing site. A single well-structured page can be enough when the product path, proof, trust, and next action are clear. YC's emphasis on simple language and landing-page guidance on a visible action support a narrow, high-information page. [19]

### 4.5 Case study: the technical evaluator as website user

A developer evaluating a technical product often behaves like a customer, investor, and engineer at once. They may read the headline, open the README, try the install, inspect the API, and look for security and maintenance signals. GitHub's documentation and CI controls show why the repository is part of the public product surface, not a separate back office. [57] [20]

The tradeoff is disclosure. Public docs increase trust and reduce friction, but public repositories can expose secrets, customer identifiers, proprietary code, or unfinished experiments. GitHub's secret-scanning guidance exists precisely because hardcoded credentials can be detected across history and branches. [33] The correct pattern is selective transparency: publish the reproducible path and safe examples, keep sensitive material private, and explain the boundary.

## 5. The Public Repository and Engineering Face: What Technical Evaluators Read

### 5.1 The repository is a claim about execution

A public repository does not prove that a startup can build a company, but it can reveal whether the team has a repeatable engineering practice. A reviewer can inspect whether the project builds, whether tests run, whether documentation matches the code, whether changes are reviewed, whether dependencies are maintained, and whether credentials or customer data are handled safely. GitHub defines CI as a practice in which code is automatically built and tested, which makes a green workflow a concrete signal rather than a decorative badge. [20]

The README is the front door. GitHub's README guidance says repositories should create a README to communicate information about the project, and README best-practice material describes it as the gateway to understanding the project. [57] [59] A seed README should state what the project does, who it is for, how to run it, how to test it, configuration requirements, architecture boundaries, deployment status, and where to ask questions.

A reviewer should be able to distinguish the product repository from a throwaway prototype. That does not mean the repository must be large or production-complete. It means the team has made intentional choices visible: what is implemented, what is mocked, what is unsafe for production, which components are third-party, and what the next technical risk is.

### 5.2 README, docs, tests, and CI

**README.** Include the one-line description, status, quick start, prerequisites, commands, configuration, test command, deployment notes, license or usage boundary, and contact. The exact list is an implementation recommendation, while the need for a README as a communication layer is supported by GitHub guidance. [57]

**Documentation.** Docs should explain the product contract, not only installation. For an API, show authentication, request and response examples, errors, rate limits, versioning, and a minimal successful call. For a consumer workflow, explain the user path and known limitations. The goal is that a reviewer can test the same behavior that the deck claims.

**Tests.** A seed repository need not have exhaustive coverage, but the highest-risk behavior should be executable in tests. Include unit tests for deterministic logic, integration tests for critical boundaries, and a smoke test for the primary path. The recommendation follows from CI's purpose of automatically building and testing code. [20]

**CI.** Run formatting or lint checks, unit tests, integration or smoke tests where practical, build checks, and security checks on pull requests. GitHub describes workflows as a mechanism to build code and run tests, so a reviewer can see whether the branch is reproducible. [20]

**Dependency controls.** Dependabot alerts identify dependency issues, but GitHub notes that alert behavior has scope and limitations, including differences for archived repositories and certain Actions dependency forms. [5] Treat the alerts as a control, not proof that every vulnerability is solved. Pin or constrain dependencies thoughtfully, review updates, and record exceptions.

**Secret scanning.** GitHub says secret scanning checks repository history and branches for hardcoded credentials. [33] A public repository should contain no real secrets, should use environment variables or a secret manager, and should have a rotation procedure if exposure occurs.

**Branch protection and review.** GitHub protected branches can require reviews and status checks before merges, while required status checks can block a merge until specified checks pass. [11] [60] For a tiny team, the rule can be lightweight, but production-affecting changes should not depend entirely on memory.

**Dependency review.** Dependency review can catch insecure or undesirable dependency changes in pull requests. [36] Use it together with lockfiles, update ownership, and a documented exception process.

**Commit hygiene.** Clean history is not a vanity contest. Descriptive commits and focused pull requests allow a reviewer to understand change scope, rollback decisions, and technical ownership. The recommendation is especially useful when a reviewer is deciding whether a prototype has a path to maintainability; it should not be represented as a formal GitHub requirement.

### 5.3 Engineering signals and what they prove

A green CI badge proves only that the configured workflow passed the configured checks. It does not prove reliability, security, or product-market fit. Likewise, a large codebase does not prove technical depth, and a small codebase does not prove technical weakness. The correct evidence is fit between the risk and the control.

A public issue tracker can show prioritization and customer responsiveness, but it can also reveal private details or invite unproductive speculation. A changelog can show velocity and product learning, but it should distinguish shipped functionality from experiments. A dependency graph can show supply-chain awareness, but a large number of dependencies increases review surface. OpenSSF's Scorecard and dependency-focused work illustrate that open-source security assessment looks at concrete risk signals rather than repository size. [16] [61]

Technical diligence also cares about ownership. The technical checklist in this corpus includes architecture, code quality, security, scalability, open-source dependencies, IP ownership, and whether claims hold before money is invested. [6] The repository should therefore link to the legal owner and disclose material third-party code or generated assets where relevant.

### 5.4 Engineering-face data table

| Signal | What it proves or suggests | Seed-stage standard | Source URL |
|---|---|---|---|
| README | The team can communicate purpose, setup, and project boundaries. [57] [59] | A new evaluator can understand the project and reach first success without guessing commands. [57] | https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories [57] |
| Quick start | The claimed product path is reproducible by a new user or reviewer. [57] | Include prerequisites, configuration, install, run, and expected output. [57] | https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories [57] |
| Product docs | The public contract is more precise than the marketing headline. [19] | Document the primary workflow, errors, limits, and known gaps. [19] | https://www.ycombinator.com/library/4b-how-to-pitch-your-company [19] |
| Tests | The team has executable checks around important behavior. [20] | Cover the highest-risk logic and the primary smoke path; do not claim exhaustive coverage without evidence. [20] | https://docs.github.com/en/actions/get-started/continuous-integration [20] |
| Continuous integration | Code is automatically built and tested in a repeatable workflow. [20] | Run checks on pull requests and make failures visible before merge. [60] | https://docs.github.com/en/actions/get-started/continuous-integration [20] |
| Branch protection | Production-affecting changes have review and merge controls. [11] | Require at least an appropriate review and passing status checks for protected branches. [11] [60] | https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches [11] |
| Secret scanning | The team has a mechanism to detect credentials in history and branches. [33] | Keep real secrets out, rotate any exposure, and document safe configuration. [33] | http://docs.github.com/en/code-security/concepts/secret-security/secret-scanning [33] |
| Dependabot or dependency alerts | The team receives signals about vulnerable dependencies, subject to tool scope. [5] | Review alerts, update deliberately, and record accepted risk. [5] | https://docs.github.com/code-security/dependabot/dependabot-alerts/about-dependabot-alerts [5] |
| Dependency review | Pull requests can be checked for risky dependency changes. [36] | Combine review with lockfiles, ownership, and an exception process. [36] | https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review [36] |
| Commit and PR hygiene | A reviewer can understand scope, ownership, and rollback reasoning. | Use focused changes and explanatory descriptions; this is an operating standard rather than a GitHub requirement. [6] | https://www.seedforge.com/blog/technical-due-diligence-for-startups [6] |
| Architecture note | The team knows current boundaries, bottlenecks, and next scaling risk. [6] | Explain what is real, mocked, single-tenant, manually operated, or not production-ready. [6] | https://www.seedforge.com/blog/technical-due-diligence-for-startups [6] |
| IP and third-party inventory | The company can explain ownership and dependencies that matter to diligence. [6] | List material open-source, generated, contractor, and customer-owned components. [6] | https://www.seedforge.com/blog/technical-due-diligence-for-startups [6] |

The table makes an important distinction between evidence and interpretation. CI, branch protection, and secret scanning are concrete controls; a reviewer still needs to inspect whether the workflows cover the right code and whether the team responds to failures. GitHub's own documentation describes the controls, while technical diligence explains why architecture, security, dependencies, and IP matter. [20] [6]

### 5.5 A safe public-repository baseline

For a seed team, the minimum credible public baseline is a clean README, a reproducible local path, one automated build or test workflow, no real credentials, a protected main branch, a dependency update path, and a short architecture note. GitHub's documentation supports the underlying controls for CI, secret scanning, Dependabot, and protected branches. [20] [33] [5] [11]

Do not publish a customer database, private API keys, unreleased security findings, or code whose ownership is unclear. Secret scanning can find credentials after they are committed, but detection is not the same as preventing exposure and does not undo a leaked credential. [33] The public face should be an intentionally selected slice of the engineering system.

A 24-hour team can implement this baseline for a narrow demo repository, but it cannot prove long-term maintainability. A reviewer should be told which parts are demo-only, which parts are manually operated, and which controls are planned. This qualification is more credible than a green badge presented as a production guarantee. [6] [20]

## 6. Investor Due Diligence: Separating a Real Company from a Project

### 6.1 The investor's question

Investor diligence asks whether the company's claims are legally owned, financially real, operationally repeatable, technically defensible, and investable. Affinity's diligence framework organizes work across finance, tax, legal, HR, assets, IT, products and services, and marketing and sales. [46] A technical checklist in the corpus adds architecture, code quality, security, scalability, open-source dependencies, IP ownership, and validation of claims before investment. [6]

The phrase real company does not mean fully mature company. A real seed company may have manual processes, incomplete controls, uncertain product-market fit, and a small team. It becomes distinguishable from a project when ownership, customer evidence, financial records, product behavior, and decision rights can be traced and explained. Diligence is therefore a graph of evidence, not a maturity score.

The data room should be permissioned and staged. Early diligence needs enough information to verify the thesis without exposing personal or customer-sensitive material unnecessarily. Investor data-room guidance commonly presents an interactive checklist of items VCs request by stage. [7] A founder should maintain a canonical folder structure and a document owner rather than assembling files ad hoc after an investor asks.

### 6.2 Corporate and legal reality

Corporate records establish what entity is raising, who owns it, who can sign, and what rights have already been granted. Include incorporation documents, charter or equivalent, bylaws or operating agreement, board and stockholder approvals, cap table, prior financing documents, SAFEs or notes, option plan, grants, and material contracts. The precise list should be matched to jurisdiction and counsel; if a particular Cooley checklist item was not available in the fetched excerpt, the exact requirement is (UNVERIFIED) rather than invented.

Equity administration is a common failure point. NASPP's material identifies missing board approval for option grants and absent 409A valuation as examples of due-diligence problems. [44] The lesson is that a founder cannot repair an undocumented grant merely by placing a spreadsheet in the data room; approval history and valuation support matter.

IP ownership should be explicit. Founder invention assignment, employee and contractor agreements, open-source licenses, customer data rights, and third-party assets should map to the company entity. Technical diligence explicitly includes IP ownership and open-source dependencies. [6] A prototype built by a contractor or copied from an unlicensed source can create a financing risk even if the demo works.

### 6.3 Financial and tax reality

Financial diligence tests whether the reported numbers reconcile to bank, billing, payroll, and tax records. Prepare a historical income statement or management accounts, cash balance, burn, runway, budget, revenue recognition policy appropriate to the business, accounts receivable and payable, debt, tax filings or status, and a forecast with assumptions. Affinity's framework identifies finance and tax as separate diligence areas. [46]

The seed founder should distinguish accounting facts from operating metrics. MRR can be a useful management metric, but cash collected, booked revenue, deferred revenue, refunds, credits, and one-time services may be treated differently. Baremetrics and Stripe provide metric definitions, but the company must reconcile the definitions to its actual billing and accounting systems. [14] [18]

A forecast is not a promise. Label assumptions about hiring, pricing, conversion, churn, sales cycle, gross margin, and payment timing. YC recommends raising enough to reach a next fundable milestone or profitability, which makes the connection between the financing ask and the model important. [17] The investor should be able to see what changes if the plan is slower.

### 6.4 Customer and commercial reality

Commercial diligence verifies that customers exist, contracts are signed by the right parties, revenue is paid or collectible, usage matches the claim, and references can confirm value. For each material customer, maintain contract or order form, start date, amount, renewal or termination terms, implementation status, usage signal, and reference permission. These are operational recommendations that connect the revenue metric to evidence; the underlying need to verify products, services, marketing, and sales appears in the diligence framework. [46]

A pipeline spreadsheet is not revenue. A pilot may be highly valuable evidence, but it should be labeled pilot and shown separately from paid recurring contracts. Stripe's early story distinguishes a closed beta and waitlist from broader adoption, showing why stage labels matter. [38] Customer concentration and founder-led sales should be disclosed because they affect repeatability.

### 6.5 Technical and security reality

Technical diligence asks whether the product can support its claimed use, whether the architecture fits current demand, what breaks at the next scale, whether security risks are controlled, and whether the company owns or can use the code. The corpus checklist explicitly includes architecture, code quality, security, scalability, open-source dependencies, and IP ownership. [6]

The repository can accelerate diligence when it contains a safe demo path, tests, CI, dependency controls, architecture notes, and clear production limitations. GitHub documents the purpose of CI, secret scanning, Dependabot alerts, and protected branches. [20] [33] [5] [11] These controls do not replace an architecture review, but they reduce avoidable uncertainty.

Security claims must be exact. If the product has not completed a formal assessment, say so. If secrets were once committed, explain rotation and remediation. If data is stored by a third party, identify the boundary and relevant contract. Technical diligence rewards clarity because it can then distinguish a known risk from an undiscovered one. [6]

### 6.6 Team and operating reality

Team diligence looks at founder roles, employment or contractor arrangements, key-person dependence, hiring plan, compensation, option grants, conflicts, and the ability to execute the stated plan. Affinity includes HR and people among its diligence areas. [46] A one-person project can become a company, but the investor needs to understand which capabilities are present, outsourced, or missing.

The founder should also disclose material commitments and dependencies. A company dependent on one contractor, one customer, one cloud account, or one founder's undocumented process has concentration risk. The recommendation follows from the broad diligence categories and from the technical checklist's focus on claims that hold before investment. [46] [6]

### 6.7 Diligence data table

| Signal | How investors verify it | Evidence to prepare | Source URL |
|---|---|---|---|
| Legal entity | Check incorporation, jurisdiction, authority to sign, and entity name against financing documents. | Formation documents, charter, bylaws or operating agreement, good-standing material where applicable. [46] | https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital [46] |
| Cap table | Reconcile ownership, option pool, SAFEs, notes, warrants, and prior issuances. | Canonical cap table plus signed financing and grant documents. [7] | https://kruzeconsulting.com/blog/due-diligence-checklist [7] |
| Board and equity approvals | Inspect approval history for grants, financings, and material actions. | Board and stockholder consents, minutes, option plan, grant records. [44] | https://www.naspp.com/blog/private-company-cap-table-due-diligence [44] |
| 409A or valuation support | Check whether option pricing and valuation process were documented where applicable. | Valuation report, effective dates, board approval, and counsel or administrator records. [44] | https://www.naspp.com/blog/private-company-cap-table-due-diligence [44] |
| IP ownership | Trace code, inventions, data rights, trademarks, and contractor work to the company. | Invention assignment, employment and contractor agreements, licenses, open-source inventory. [6] | https://www.seedforge.com/blog/technical-due-diligence-for-startups [6] |
| Revenue reality | Reconcile reported recurring revenue to contracts, billing, invoices, cash, refunds, and credits. | Billing export, bank reconciliation, contracts, revenue bridge, and metric definitions. [14] [46] | https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital [46] |
| Customer quality | Confirm customer identity, payment, use, renewal, and reference permission. | Customer list, order forms, usage evidence, concentration analysis, references. [46] | https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital [46] |
| Pipeline and pilots | Separate interest, pilot, LOI, waitlist, and signed recurring revenue. | Funnel with stage definitions, dates, owners, probability, and conversion history. [38] | https://www.billiondollarpitchdecks.com/decks/stripe [38] |
| Cash and runway | Compare bank cash and burn to the financing plan and next milestone. | Bank statements, burn schedule, budget, hiring plan, and runway scenarios. [17] | https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising [17] |
| Tax and payroll | Check filings, payroll, contractor classification, sales tax or equivalent exposure, and obligations. | Tax returns or status, payroll reports, contractor records, and advisor notes. [46] | https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital [46] |
| Architecture and scalability | Review current system, bottlenecks, dependencies, reliability assumptions, and next-scale risks. | Architecture diagram, deployment notes, incident history, load assumptions, technical roadmap. [6] | https://www.seedforge.com/blog/technical-due-diligence-for-startups [6] |
| Security and secrets | Inspect controls, incidents, access, credentials, and remediation. | Security overview, access policy, secret scanning status, incident log, vendor controls. [33] [6] | http://docs.github.com/en/code-security/concepts/secret-security/secret-scanning [33] |
| Code quality and delivery | Run or inspect build, tests, CI, reviews, dependency updates, and release process. | Repository access, CI runs, test strategy, protected branches, dependency policy. [20] [11] [5] | https://docs.github.com/en/actions/get-started/continuous-integration [20] |
| Team capacity | Verify founder roles, employment, key dependencies, compensation, and hiring needs. | Team roster, agreements, org plan, and key-person risk notes. [46] | https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital [46] |
| Claims reconciliation | Compare deck, website, metrics, customer, technical, and legal statements. | Claim ledger with owner, date, source system, and qualification. [7] | https://kruzeconsulting.com/blog/due-diligence-checklist [7] |

The table is deliberately longer than a deck. A real company can have gaps, but it should know the gaps, assign owners, and explain remediation. The investor's decision is not simply yes or no on maturity; it is whether the remaining risk is understood, priced, and reducible. Affinity's broad diligence categories and the technical checklist support this multidimensional view. [46] [6]

### 6.8 Case study: the option-grant failure mode

An option grant can look complete in a founder's spreadsheet while remaining deficient in corporate records. NASPP's example of missing board approval or absent 409A support shows why diligence goes beyond a list of names and percentages. [44] The mechanism is institutional: equity rights depend on authorization, valuation, and documentation, not only on what the founders intended.

The implication for a seed package is simple: maintain an equity folder from day one, record approvals as they happen, and reconcile the cap table after each issuance. This recommendation is more valuable than adding another slide because it protects the financing process itself. The source does not establish a universal jurisdictional rule for every company, so counsel-specific requirements remain (UNVERIFIED) where not documented. [44]

### 6.9 Data-room operating model

Create folders for corporate, financing, equity, finance, tax, people, customers, product, engineering, security, IP, and fundraising. The categories reflect the finance, tax, legal, HR, assets, IT, product, and sales dimensions described by Affinity, with technical and IP categories added from the technical checklist. [46] [6]

For each document, store a canonical version, effective date, owner, sensitivity level, and a one-line explanation of what claim it proves. When a document is missing, create a placeholder that says missing, not applicable, or pending counsel. This is an operating recommendation based on the interactive checklist model and on diligence's need to verify claims. [7]

## 7. What Transfers to a 24-Hour Build, and What Does Not

### 7.1 The honest boundary

Eric Ries defines an MVP as the version of a new product that allows a team to collect the maximum amount of validated learning about customers with the least effort. [30] That definition supports a narrow 24-hour build whose purpose is to test one risky behavior. It does not support calling a shallow demo a validated business.

Steve Blank's customer-development framing keeps burn low until a business model is validated by paying customers. [25] A one-day build can reduce uncertainty about whether a user understands a workflow, can complete a task, or expresses intent to try. It cannot generate meaningful long-term retention, reliable churn, recurring revenue history, legal ownership history, production security evidence, or a mature operating system in one day.

The GV Sprint model is a useful adjacent framework: it describes a five-day process designed to shortcut learning by prototyping and testing. [37] A 24-hour build is a compressed sprint, so it must shrink scope further and make the hypothesis explicit. The correct deliverable is a tested learning artifact, not a falsely complete company package.

### 7.2 What transfers directly

**Narrative clarity transfers.** A founder can write the one-line description, problem, solution, target user, and test hypothesis in an hour. YC's pitch guidance makes plain-language explanation a core requirement. [19] The same sentence should appear in the demo, README, and landing page.

**A narrow demo transfers.** A single happy path can show the product mechanism and let a user attempt the risky action. Stripe's seed story illustrates how a concrete integration mechanism can make a technical product legible. [38]

**Landing-page structure transfers.** Message match, clear copy, a visible action, and a short form can be implemented quickly. The page should say what is real now and what early users will receive.

**Instrumentation transfers.** Add an event for signup, activation, successful workflow, error, and return visit. The exact implementation varies, but the principle of measuring the behavior that predicts value follows from cohort-retention practice. [8]

**README and reproducibility transfer.** A one-day repository can have a clear README, setup commands, an example environment file with no secrets, a smoke test, and a short known-limitations section. GitHub's README and CI guidance support these controls. [57] [20]

**A safe CI baseline transfers.** A simple workflow can build the project and run the available tests, while protected branches and secret-safe configuration can prevent obvious errors. [20] [11] [33]

**A claim ledger transfers.** Mark each statement as observed, reported by a user, planned, simulated, or unverified. This is a lightweight version of the reconciliation discipline required in diligence. [7] [46]

### 7.3 What does not transfer honestly

**Retention does not transfer.** A one-day test can show a user completed a workflow once; it cannot show a stable retention curve. YC and ChartMogul's cohort logic requires observations over time. [8] [31]

**ARR and mature unit economics do not transfer.** A forecast can be modeled in a day, but ARR requires recurring revenue and CAC or LTV assumptions require observed data and disclosed cost definitions. [14] [18] A founder may include a scenario model, but must label it forecast.

**Production reliability does not transfer.** A demo can work under controlled conditions while lacking monitoring, backup, incident response, load evidence, dependency maintenance, or security review. Technical diligence explicitly asks about scalability and security, and those are systems built over time. [6]

**Legal and cap-table completeness does not transfer.** Incorporation, invention assignment, option approvals, valuation support, and financing documents require accurate records and sometimes counsel. NASPP's examples show that missing approvals can matter even when the intended ownership is obvious. [44]

**Market validation does not transfer.** A few positive reactions do not establish a repeatable sales process or a market-size claim. YC's advice ties fundraising readiness to understanding the market and customer and seeing adoption. [17] One-day interviews can generate hypotheses, not durable evidence.

**A full investor-ready data room does not transfer.** A founder can create the folder structure and a list of missing documents, but cannot manufacture historical statements, customer contracts, approvals, or referenceable outcomes. Affinity's broad diligence categories make the time dimension visible. [46]

### 7.4 24-hour build plan

Hour 0 to 1: write the hypothesis, target user, risky behavior, success criterion, and explicit non-goals. The hypothesis should be narrow enough that a failed result changes the next action. This applies the validated-learning definition of MVP. [30]

Hour 1 to 3: write the one-line description, landing-page copy, README skeleton, and demo script. Use the same product nouns across all artifacts because YC's pitch guidance prioritizes simple language. [19]

Hour 3 to 10: build only the end-to-end path needed to test the behavior. Use mocks where they do not alter the hypothesis, and label every mock. The aim is to learn with least effort, not to hide missing infrastructure. [30]

Hour 10 to 13: add event instrumentation and an outcome log. Record user, timestamp, action, success or failure, and qualitative feedback. Cohort analysis will come later, but the event schema must preserve the information needed to analyze it. [8]

Hour 13 to 16: add README instructions, tests for the core logic, a smoke test, and a CI workflow. GitHub describes CI as building and testing code automatically, so the workflow makes the demo reproducible. [20]

Hour 16 to 18: remove secrets, configure environment variables, enable available secret scanning, and protect the main branch if the repository will be public. GitHub documents secret scanning and protected branches as concrete controls. [33] [11]

Hour 18 to 21: test with real target users or realistic evaluators, observe the behavior without coaching, and record objections. GV's sprint model treats prototype testing as the mechanism for shortening the learning loop. [37]

Hour 21 to 23: reconcile the landing page, README, demo, and deck snippet. Mark what is live, simulated, planned, or unavailable. The claim ledger is the bridge to later diligence. [7]

Hour 23 to 24: publish a results note with test count, completed actions, failure modes, qualitative findings, and next experiment. Do not call the result product-market fit, recurring revenue, retention, or production readiness unless the evidence supports those terms. [30] [8]

### 7.5 Transferability data table

| Package component | Transfers in 24 hours | Does not transfer in 24 hours | Honest evidence to publish | Source URL |
|---|---|---|---|---|
| One-line description | Yes; write and test plain-language comprehension. [19] | No; a clear sentence does not prove demand. [17] | Observed comprehension, target user, and exact non-goal. [19] | https://www.ycombinator.com/library/4b-how-to-pitch-your-company [19] |
| Landing page | Yes; build message match, copy, one action, and a lightweight form. | No; a page does not prove conversion at scale or retention. [8] | Visits, completed action, source, and qualitative objections. | https://unbounce.com/landing-page-articles/landing-page-best-practices |
| Product demo | Yes; implement one end-to-end behavior with labeled mocks. [30] | No; a happy path does not prove reliability or broad product scope. [6] | Demo recording, test conditions, known limitations, and failures. [6] | https://leanstartup.co/resources/articles/what-is-an-mvp/ [30] |
| User interviews | Yes; test comprehension, pain, and willingness to try. [37] | No; interest is not repeat purchase or a validated market. [17] | Interview selection, exact questions, observed behavior, and quotes with permission. [37] | https://www.gv.com/sprint [37] |
| Instrumentation | Yes; capture signup, activation, core action, error, and return event. [8] | No; one day cannot create a meaningful retention curve. [31] | Event definitions, timestamps, counts, and incomplete-cohort label. [8] | https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention [8] |
| README | Yes; document setup, use, tests, and boundaries. [57] | No; a README does not prove maintainability over time. [6] | Reproducible commands, expected output, and known gaps. [57] | https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories [57] |
| CI and tests | Yes; automate build and core checks. [20] | No; green CI does not prove security, scale, or product-market fit. [6] | Workflow file, test scope, and failed checks if any. [20] | https://docs.github.com/en/actions/get-started/continuous-integration [20] |
| Secret and branch controls | Yes; remove credentials, enable controls, protect main. [33] [11] | No; controls do not undo a historical leak or create a full security program. [33] | Safe configuration, scan status, rotation record if needed. [33] | http://docs.github.com/en/code-security/concepts/secret-security/secret-scanning [33] |
| Revenue model | Yes; create a clearly labeled price or payment hypothesis. [1] | No; a model is not actual MRR, ARR, CAC, or LTV. [14] [18] | Forecast versus actual labels and assumptions. [14] | https://baremetrics.com/blog/saas-metrics-checklist-kpis-founders-should-track [14] |
| Diligence room | Yes; create folders, owners, and missing-item list. [7] | No; historical legal, financial, customer, and equity evidence cannot be manufactured. [46] [44] | Canonical files, permissions, dates, and explicit missing or pending labels. [7] | https://kruzeconsulting.com/blog/due-diligence-checklist [7] |
| Retention claim | Yes; define the future measurement plan. [8] | No; one-day activity cannot prove durable retention. [31] | Hypothesis and instrumentation plan, not a fabricated curve. [31] | https://help.chartmogul.com/article/160-cohort-net-mrr-retention [31] |
| Production readiness | Yes; document current demo boundary and next risk. [6] | No; load, security, incident, backup, and dependency history require time. [6] | Architecture note, threat list, and explicit production exclusions. [6] | https://www.seedforge.com/blog/technical-due-diligence-for-startups [6] |

### 7.6 Case study: prototype debt and the credibility boundary

Rapid prototypes can accelerate time to market, but the research corpus on startup technical debt describes the corresponding risk: deferred dependencies, missing test coverage, and prototype code can become production infrastructure. [39] The mechanism is path dependence. Once customers, data, and internal processes depend on a shortcut, the cost of changing it rises and the team may stop being able to distinguish a deliberate boundary from accidental architecture.

A one-day build should therefore create a debt register at the moment it creates the prototype. List the shortcut, why it is safe for the test, what would make it unsafe, and the trigger for replacing it. This turns debt from a hidden liability into a managed experiment. The recommendation is consistent with the MVP objective of learning with least effort and with technical diligence's focus on scalability, code quality, and security. [30] [6]

The correct investor statement is: “We built a narrow prototype to test X; Y users completed Z under these conditions; the current implementation has these limitations; the next milestone is A.” The incorrect statement is: “We built the company in 24 hours.” The first statement preserves learning and credibility; the second collapses a demo, a product, a business, and a legal entity into one unsupported claim. [30] [17]

## Synthesis: One Evidence System Across Seven Artifacts

The seven artifacts differ in scope, time horizon, and proof burden. The deck is a compression layer for attention; the one-pager is a routing layer; the metric pack is a measurement layer; the website is a conversion layer; the repository is an engineering transparency layer; diligence is an ownership and verification layer; and the 24-hour build is a learning layer. YC's pitch and fundraising guidance support compression and follow-up, while investor and technical diligence sources support expansion and verification. [19] [17] [46] [6]

The first non-obvious tension is brevity versus evidence. YC says the pitch should create interest and not explain the entire business, but the investor still needs a path to underlying financial, technical, and legal material. [19] [7] The solution is not a longer main deck. It is a layered package: concise main narrative, one-page routing document, linked evidence appendix, permissioned data room, and reproducible product or repository path.

The second tension is polish versus truth. A strong website and deck can improve comprehension, while trust research warns that visitors risk time, money, and data and that lost trust can lose a customer. [28] The same claim should therefore be attractive and qualified. A founder who labels a beta as a beta, a pilot as a pilot, and a forecast as a forecast gains more credibility than one who uses mature-company language prematurely.

The third tension is speed versus durable systems. MVP theory supports least-effort validated learning, and GV's sprint model supports rapid prototyping and testing. [30] [37] Technical-debt evidence warns that deferred dependencies and missing tests can become production problems. [39] The synthesis is a two-speed architecture: move quickly at the experiment boundary, but preserve a migration path, claim ledger, event definitions, and explicit production exclusions.

The fourth tension is top-line growth versus durable value. MRR, ARR, and growth are useful, but retention and cohorts show whether the value persists. [14] [8] [31] The package should put the headline in the deck, the bridge and cohort in the appendix, and the raw export in the room. If those layers disagree, explain the disagreement rather than selecting the most flattering view.

The fifth tension is public transparency versus security. A README, docs, CI, and public examples reduce evaluator friction, while secret scanning exists because repositories can contain hardcoded credentials across history and branches. [57] [33] Publish the safe path, keep sensitive assets private, and make the boundary explicit. A public repository is an interface to engineering judgment, not a dump of the entire company.

The sixth tension is founder narrative versus institutional evidence. Founder insight can explain why a company should exist, as seen in YC's emphasis on insight and in the concrete mechanisms in Stripe's seed story. [1] [38] Diligence then asks whether the entity owns the code, whether the revenue reconciles, whether grants were approved, and whether customers can verify the claim. [6] [44] The package succeeds when the narrative points to records rather than trying to replace them.

### Comparative operating table

| Dimension | Deck | One-pager | Metrics pack | Website | Repository | Diligence room | 24-hour build |
|---|---|---|---|---|---|---|---|
| Primary decision | Follow-up interest. [19] | Fit and routing. [17] | Repeatable value. [8] | Visitor action. | Engineering credibility. [20] | Investability and ownership. [46] | Learning about one risk. [30] |
| Time horizon | Minutes to next meeting. [19] | Fast triage and leave-behind. [23] | Historical and cohort periods. [31] | Immediate conversion. | Ongoing delivery. [20] | Historical records plus future risk. [7] | One experiment cycle. [37] |
| Best proof | Clear thesis plus traction. [1] | Compact evidence and contact. [17] | Retention, cohorts, reconciled revenue. [8] | Message match, trust, product path. [28] | Build, tests, controls, docs. [20] [33] | Contracts, approvals, accounts, ownership. [46] [44] | Observed behavior under stated conditions. [30] |
| Main tradeoff | Brevity versus nuance. [19] | Compression versus risk disclosure. [17] | Top line versus durable value. [31] | Brand versus clarity and trust. [28] | Transparency versus sensitive exposure. [33] | Speed versus record completeness. [7] | Speed versus technical debt. [39] |
| Correct next action | Request a follow-up. [19] | Route to deck, demo, or room. [17] | Investigate cohort or unit economics. [8] | Sign up, install, book, or request access. | Run, review, or contribute safely. [57] | Resolve gaps and price risk. [46] | Run the next experiment. [37] |

The synthesis yields a practical rule: every artifact should be optimized for its decision, but no artifact may contradict the evidence layer beneath it. The founder should be able to move from one sentence in the deck to one row in the metrics export, one product path in the demo, one record in the data room, or one test in the repository. That traceability is the difference between a startup package and a collection of startup theater. [7] [6]

## Implementation Appendix: The 72-Hour Completion Sequence

### First 24 hours: establish the truth surface

Write the claim ledger before polishing the deck. Record company description, customer, problem, product state, revenue state, customer count, retention definition, funding history, team roles, and ask. For each claim, mark source system and status. This turns the package into a controlled set of assertions rather than a collection of copy edits. The need for underlying evidence is supported by YC's leave-behind guidance and investor data-room practice. [17] [7]

Build the narrow product path and README. Add a safe environment example, core test, CI workflow, and known-limitations section. GitHub's documentation supports README communication, automated build and test, secret scanning, and protected branches as concrete engineering controls. [57] [20] [33] [11]

Create the landing page around the same one-line description and one primary action. Message match and clear copy are the minimum conversion controls, while trust guidance requires accurate claims about the company and product. [28]

### Next 24 hours: connect proof to narrative

Write the deck in plain language, then add only the charts and screenshots that change belief. YC says the objective is follow-up interest and the pitch should answer core questions clearly. [19] [19] Put a date and definition on traction, and add a cohort or retention appendix when the product has enough history to support it. [8]

Write the one-pager as a single-page routing document. Include vision, product, team, location, contact, traction, market, and financial context because YC explicitly lists those elements. [17] Link to the deck, demo, website, and permissioned room.

### Final 24 hours: make diligence survivable

Create the data-room folders and put a missing-item list in each. Reconcile cap table, financing, customer, metrics, and technical claims. Address equity approvals and valuation support early because missing board approval or 409A material can become a diligence problem. [44]

Run a skeptical review. Ask a non-founder to state what the company does, who pays, what is real today, what the strongest proof is, what can be independently checked, and what the next financing milestone is. YC's plain-language rules and fundraising guidance make these questions decision-relevant. [19] [17]

Remove unsupported superlatives. If a number is forecast, say forecast; if a customer is a pilot, say pilot; if a control is planned, say planned; if a source cannot be verified, write (UNVERIFIED). This is the safest way to preserve trust while the company is still learning. [28] [7]

## Closing Decision Checklist

1. The deck's first slide states what the company does in simple language and the problem slide names the customer and consequence. [19] [1]
2. The traction slide separates actual revenue, usage, pilots, pipeline, and waitlist evidence and includes dates and definitions. [1] [38]
3. The one-pager includes vision, product, team, location, contact, traction, market, and financial context within one or two pages. [17]
4. The website has message match, a visible action, proof, a product path, accurate trust language, and acceptable performance. [28] [42]
5. The repository has a README, reproducible setup, core tests, CI, safe configuration, dependency controls, and branch or review controls appropriate to the risk. [57] [20] [33] [11]
6. The data room contains canonical corporate, equity, finance, customer, people, product, technical, security, and IP evidence, with missing items labeled. [46] [6] [7]
7. The 24-hour build states one hypothesis, measures one behavior, records failure, and does not claim retention, ARR, production readiness, or legal completeness without evidence. [30] [8] [6]

A seed-stage package is ready when a skeptical reader can move from narrative to proof without changing the meaning of the claim. The package does not need to look like a later-stage company; it needs to make the current state, the evidence, the uncertainty, and the next milestone legible. YC's focus on clear follow-up pitches, metric and retention guidance, and the diligence sources' focus on records all point to the same operating standard. [19] [8] [46]

## SOURCE LEDGER

The ledger below is deduplicated by URL. Corpus document IDs in parentheses identify the research records behind the inline sentence markers.

1. https://techcrunch.com/2023/08/18/sample-seed-pitch-deck-deckmatch (corpus docs: 54, 225, 277)
2. https://www.slidegmm.ai/en/blog/15-unicorn-pitch-decks-breakdown-2026 (corpus docs: 56)
3. https://techcrunch.com/tag/pitch-deck-teardown (corpus docs: 57)
4. https://bestpitchdeck.com/YC (corpus docs: 58)
5. https://www.slideshare.net/slideshow/y-combinator-pitch-deck-designed-by-zlides/228225673 (corpus docs: 55)
6. https://slidechef.net/templates/airbnb-pitch-deck-template (corpus docs: 62, 269)
7. https://upmetrics.co/pitch-deck-examples/stripe (corpus docs: 63)
8. https://www.slideshare.net/slideshow/airbnb-first-pitch-deck-editable/45768374 (corpus docs: 59, 272)
9. https://www.storydoc.com/blog/airbnb-pitch-deck-example (corpus docs: 60)
10. https://www.fundreef.com/one-pager-for-investors-template-and-examples (corpus docs: 72, 238)
11. https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising (corpus docs: 70, 246, 235)
12. https://visme.co/blog/startup-one-pager (corpus docs: 71, 237)
13. https://www.ycombinator.com/ (corpus docs: 73)
14. https://startupfundraising.com/library/pitch-deck-examples/one-pager (corpus docs: 69, 234)
15. https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention (corpus docs: 67, 249)
16. https://chartmogul.com/reports/saas-retention-the-new-normal (corpus docs: 66, 250)
17. https://www.ycombinator.com/companies?batch=Spring%202026 (corpus docs: 68)
18. https://www.thesaascfo.com/cohort-analysis-explained-for-your-saas-business (corpus docs: 64)
19. https://www.digitalapplied.com/blog/net-revenue-retention-benchmarks-2026-saas-expansion-data (corpus docs: 65)
20. https://www.getpureproof.com/blog/testimonials-for-saas-landing-pages (corpus docs: 86)
21. https://www.neweconomies.co/p/the-ultimate-guide-yc-startups (corpus docs: 84, 243)
22. https://taqwah.agency/blog/saas-landing-page-examples (corpus docs: 87)
23. https://embertribe.com/blog/the-top-10-landing-page-best-practices-to-maximize-your-conversion-rates (corpus docs: 85)
24. https://www.replo.app/blog/anatomy-of-a-landing-page (corpus docs: 88)
25. https://www.seedforge.com/blog/technical-due-diligence-for-startups (corpus docs: 81)
26. https://docs.gitscrum.com/en/best-practices/configuring-branch-protection-rules (corpus docs: 82)
27. https://ctoondemand.com/technical-due-diligence-checklist (corpus docs: 80)
28. https://odeaworks.com/blog/2026-04-05-technical-due-diligence-checklist-startup (corpus docs: 79)
29. https://github.com/memwey/startup-due-diligence (corpus docs: 83)
30. https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital (corpus docs: 75, 219)
31. https://www.moonshotnx.com/startup-data-room-for-founders (corpus docs: 76)
32. https://www.pitchwise.se/resource-list/the-startup-data-room-checklist (corpus docs: 78)
33. https://www.affinity.co/guides/venture-capital-due-diligence-best-practices (corpus docs: 77)
34. https://www.seedforge.com/blog/due-diligence-checklist-for-seed-stage-startups-the-2026-standard (corpus docs: 74, 221)
35. https://mvpmule.com/ (corpus docs: 92)
36. https://www.creolestudios.com/mvp-tech-debt (corpus docs: 90)
37. https://rapidsd.com/blog/technical-debt-mvp-development-founders-guide-2025 (corpus docs: 89)
38. https://www.buildin7.com/blog/mvp-validation-framework-us-market-research-2025 (corpus docs: 91)
39. https://railsware.com/services (corpus docs: 93)
40. https://es.scribd.com/document/382174740/DocSend-Fundraising-Research (corpus docs: 97)
41. https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck (corpus docs: 95, 248)
42. https://www.ycombinator.com/library/search?query=pitch+decks (corpus docs: 96)
43. https://slidebean.com/pitch-deck-examples (corpus docs: 98, 271, 278)
44. https://www.ycombinator.com/library/4b-how-to-pitch-your-company (corpus docs: 94, 247)
45. https://upmetrics.co/pitch-deck-examples/notion (corpus docs: 116, 224)
46. https://www.venturemage.com/coinbase-pitch-deck (corpus docs: 117)
47. https://startupfundraising.com/library/articles/coinbase-pitch-deck-teardown (corpus docs: 118)
48. https://vcmatch.ai/pitch-decks/coinbase-seed (corpus docs: 115)
49. https://barmstrong.medium.com/the-coinbase-seed-round-pitch-deck-50c8ec91d40b (corpus docs: 114, 227)
50. https://www.alexanderjarvis.com/resources/tools/venture-capital-lp-one-pager-tool (corpus docs: 104)
51. https://perfectpitchdeck.com/vc/one-pager-vc (corpus docs: 106)
52. https://onepager.vc/ (corpus docs: 108, 236)
53. https://www.slideteam.net/blog/top-20-one-page-executive-summary-for-startup-samples-with-templates-and-examples (corpus docs: 105)
54. https://thesaaslibrary.com/saas-metrics-explained (corpus docs: 119)
55. https://jrxcontabilidade.com.br/mrr-arr-cac-ltv-churn (corpus docs: 120)
56. https://baremetrics.com/blog/saas-metrics-checklist-kpis-founders-should-track (corpus docs: 123, 251)
57. https://stripe.com/resources/more/cac-in-saas (corpus docs: 122, 252)
58. https://saasmetricscalculator.com/ltv-calculator (corpus docs: 121)
59. https://www.seedforge.com/blog/startup-metrics-that-matter-to-seed-investors (corpus docs: 140)
60. https://www.lucid.now/blog/traction-metrics-startups-track-before-fundraising (corpus docs: 143)
61. https://www.stackmatix.com/blog/traction-benchmarks-by-funding-stage (corpus docs: 141)
62. https://nextgen.nen.wfglobal.org/news/2026-pitch-deck-traction-benchmarks-startup-metrics-2026-averages-283018 (corpus docs: 142)
63. https://startupfundraising.com/library/articles/how-to-think-about-startup-traction (corpus docs: 139)
64. https://www.reddit.com/r/startups/comments/1v7rst6/the_trap_of_vanity_i_will_not_promote (corpus docs: 125)
65. http://pilot.com/blog/what-happens-during-a-series-a-fundraise (corpus docs: 128)
66. https://sethlevine.com/archives/2022/05/irr-is-a-vanity-metric.html (corpus docs: 126)
67. https://deepdive.headline.com/learn/resources/what-is-cohort-analysis (corpus docs: 127)
68. https://fastercapital.com/content/Vanity-Metrics--Unlocking-the-True-Value--Moving-Beyond-Vanity-Metrics-in-Startups.html (corpus docs: 124)
69. https://sitegrade.io/en/blog/core-web-vitals-conversion-rate-correlation (corpus docs: 103)
70. https://unbounce.com/landing-page-articles/landing-page-best-practices (corpus docs: 101, 239)
71. https://www.digitalapplied.com/blog/landing-page-statistics-2026-conversion-data-points (corpus docs: 102)
72. https://markanamedia.com/blog/landing-page-speed-optimization-2026 (corpus docs: 99)
73. https://markanamedia.com/blog/landing-page-cro-2026-best-practices (corpus docs: 100)
74. https://docs.github.com/en/actions/get-started/continuous-integration (corpus docs: 150, 232)
75. https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference (corpus docs: 151)
76. https://docs.github.com/code-security/dependabot/dependabot-alerts/about-dependabot-alerts (corpus docs: 149, 230)
77. https://docs.github.com/en/code-security/reference/code-scanning/workflow-configuration-options (corpus docs: 152)
78. https://docs.github.com/articles/getting-started-with-github-actions (corpus docs: 153)
79. http://glencoyne.com/guides/deeptech-due-diligence-technical (corpus docs: 110)
80. http://kodertroop.com/services/technology-due-diligence (corpus docs: 113)
81. http://pointscienceanalytics.com/resources/technical-due-diligence-checklist (corpus docs: 112)
82. https://data-rooms.org/blog/venture-capital-due-diligence-checklist (corpus docs: 144)
83. https://www.cooleygo.com/documents/sample-vc-due-diligence-request-list (corpus docs: 145, 220)
84. https://www.peony.ink/blog/startup-data-room-checklist (corpus docs: 148)
85. https://datarooms.com.hk/blog/startup-data-room (corpus docs: 146)
86. https://www.4degrees.ai/blog/2025-venture-capital-due-diligence-checklist (corpus docs: 147)
87. https://www.tandfonline.com/doi/abs/10.1080/00472778.2026.2656168 (corpus docs: 129)
88. https://leanstartup.co/resources/articles/what-is-an-mvp/ (corpus docs: 133, 215)
89. https://www.emerald.com/jsbed/article/32/1/212/1239514/Unpacking-the-minimum-viable-product-MVP-a (corpus docs: 130)
90. https://www.atlassian.com/agile/product-management/minimum-viable-product (corpus docs: 132)
91. https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=2178&context=etm_studentprojects (corpus docs: 131)
92. https://blog.mettl.com/hackathon-judging-criteria (corpus docs: 135)
93. https://blog.progressiverobot.com/rebuilt-a-hackathon-app-into-a-production-accessibility-tool-with-github-copilot (corpus docs: 138)
94. https://newly.app/guides/vibe-coding-limitations (corpus docs: 136)
95. https://developer.nvidia.com/blog/tag/hackathon (corpus docs: 137)
96. https://cloudmatos.ai/blog/aegis-agentic-ai-hackathon-security (corpus docs: 134)
97. http://pitchdeckhunt.com/ (corpus docs: 159)
98. https://www.billiondollarpitchdecks.com/decks/linear (corpus docs: 162, 226)
99. https://www.slideshare.net/slideshow/stripe-pitch-deck-designed-by-zlides-212030290/212030290 (corpus docs: 163)
100. https://www.billiondollarpitchdecks.com/decks/stripe (corpus docs: 161, 228)
101. https://www.docsend.com/blog/tracking-investor-engagement-pitch-deck (corpus docs: 155)
102. https://www.docsend.com/blog/three-pitch-deck-changes-that-make-vcs-pay-closer-attention (corpus docs: 154, 244)
103. https://review.firstround.com/ (corpus docs: 156)
104. https://www.docsend.com/blog/how-your-pitch-deck-can-shine-as-vc-focus-shifts (corpus docs: 158, 245)
105. http://checkthat.ai/brands/firstround (corpus docs: 169)
106. https://brianbalfour.com/essays/product-market-fit (corpus docs: 171)
107. http://review.firstround.com/gongs-path-to-product-market-fit (corpus docs: 172)
108. https://www.startups.com/lexicon/seed-round (corpus docs: 173)
109. https://help.chartmogul.com/article/160-cohort-net-mrr-retention (corpus docs: 166, 253)
110. http://paddle.com/profitwell-metrics (corpus docs: 167)
111. https://www.paddle.com/resources/topic/profitwell-metrics (corpus docs: 165)
112. https://chartmogul.com/reports/saas-retention-the-ai-churn-wave (corpus docs: 168)
113. https://www.scribd.com/presentation/549660900/bessemer-benchmarks-downloadable-template-final (corpus docs: 164)
114. https://www.nngroup.com/reports/ecommerce-ux-trust-and-credibility (corpus docs: 196, 240)
115. http://nngroup.com/about (corpus docs: 197)
116. https://websitespeedy.com/blog/seo-core-web-vitals-optimization-guide (corpus docs: 198)
117. https://web.dev/ (corpus docs: 195)
118. https://www.nngroup.com/ (corpus docs: 194)
119. https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches (corpus docs: 176, 231)
120. http://docs.github.com/en/code-security/concepts/secret-security/secret-scanning (corpus docs: 177, 229)
121. https://docs.github.com/en/pull-requests/reference/status-checks (corpus docs: 174)
122. https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review (corpus docs: 178, 233)
123. https://github.com/actions/dependency-review-action (corpus docs: 175)
124. http://github.com/ossf/scorecard (corpus docs: 189)
125. http://openssf.org/projects (corpus docs: 190)
126. https://openssf.org/projects/scorecard (corpus docs: 191)
127. https://www.sonatype.com/blog/the-owasp-llm-top-10-and-sonatype-supply-chain-security (corpus docs: 192)
128. https://openssf.org/technical-initiatives/repository-security (corpus docs: 193)
129. https://carta.com/learn/startups/fundraising/convertible-securities/calculator (corpus docs: 200)
130. https://viridianlawyers.com/blog/intellectual-property-assignment (corpus docs: 201)
131. https://tactyc.app.carta.com/resources/cap-table (corpus docs: 203)
132. https://amplifypartners.com/blog-posts/safe-financing-overview-timelines-process-docs (corpus docs: 202)
133. https://startupfundraising.com/library/articles/preserving-value-mitigating-ip-transfer-risks-in-m-a-deals (corpus docs: 199)
134. https://kruzeconsulting.com/blog/due-diligence-checklist (corpus docs: 204, 222)
135. https://legalbooks.ai/resources/startup-fundraising-due-diligence-checklist (corpus docs: 206)
136. https://vcbeast.com/guides/how-to-conduct-customer-reference-calls (corpus docs: 208)
137. https://venturecapitalcareers.com/blog/venture-capital-due-diligence (corpus docs: 205)
138. https://steveblank.com/category/customer-development?params=ref-blog-openphone-review-update-and-in_blog-what-is-customer-discovery (corpus docs: 182)
139. https://steveblank.com/category/customer-development (corpus docs: 179)
140. https://steveblank.com/tag/customer-development (corpus docs: 180, 217)
141. https://www.gv.com/sprint (corpus docs: 181, 218)
142. https://steveblank.com/category/customer-development-manifesto (corpus docs: 183)
143. https://www.groenewold-it.solutions/en/blog/softwaredev/technical-debt-case-studies-and-lessons-learned (corpus docs: 209, 216)
144. https://www.researchgate.net/publication/337263748_Towards_Effective_Technical_Debt_Decision_Making_in_Software_Startups (corpus docs: 210, 214)
145. https://arxiv.org/html/2403.06484v1 (corpus docs: 212)
146. https://brainhub.eu/library/technical-debt-examples (corpus docs: 213)
147. https://arxiv.org/pdf/2403.06484 (corpus docs: 211)
148. https://www.naspp.com/blog/private-company-cap-table-due-diligence (corpus docs: 186, 223)
149. https://www.vft.wfglobal.org/articles/pitch-deck-benchmarks-venture-capital-2026-196792 (corpus docs: 187)
150. https://www.cakeequity.com/blog/investor-ready-cap-table (corpus docs: 184)
151. https://www.svb.com/startup-insights/startup-strategy/how-to-create-investor-pitch-deck-vc-angels (corpus docs: 188, 275)
152. https://web.dev/articles/vitals (corpus docs: 241)
153. https://web.dev/learn/performance (corpus docs: 242)
154. https://slidebean.com/templates/airbnb-pitch-deck (corpus docs: 270)
155. https://www.failory.com/pitch-deck/airbnb (corpus docs: 273)
156. http://slidemaster.studio/investor-pitch-deck (corpus docs: 274)
157. https://www.slideshare.net/slideshow/pitch-deck-teardown-encores-3m-preseed-seed-deck/251903456 (corpus docs: 276)
158. https://gingiris.tools/blog/2026/04/02/github-readme-template-guide (corpus docs: 279)
159. https://github.com/jehna/readme-best-practices (corpus docs: 280)
160. https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories (corpus docs: 281)
161. https://pushpen.dev/blog/github-readme-best-practices-2026 (corpus docs: 282)
162. https://github.com/levnikolaevich/claude-code-skills/blob/master/docs/standards/GITHUB_README_BEST_PRACTICES.md (corpus docs: 283)

## References

1. *How to build your seed round pitch deck : YC Startup Library*. https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck
2. *3 pitch deck changes that make VCs pay attention*. https://www.docsend.com/blog/three-pitch-deck-changes-that-make-vcs-pay-closer-attention
3. *Sample VC Due Diligence Request List*. https://www.cooleygo.com/documents/sample-vc-due-diligence-request-list
4. *Startup One-Pager — The 8-Block Executive Summary That Gets*. https://startupfundraising.com/library/pitch-deck-examples/one-pager
5. *Dependabot alerts - GitHub Docs*. https://docs.github.com/code-security/dependabot/dependabot-alerts/about-dependabot-alerts
6. *Technical Due Diligence for Startups: What Investors Check in ...*. https://www.seedforge.com/blog/technical-due-diligence-for-startups
7. *VC Due Diligence Checklist: Pre-Seed to Series B & Beyond*. https://kruzeconsulting.com/blog/due-diligence-checklist
8. *How To Improve Cohort Retention : YC Startup Library*. https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention
9. *Landing Page Best Practices To Create High-Converting Pages*. https://unbounce.com/landing-page-articles/landing-page-best-practices
10. *The Ultimate Guide: YC Startup Landing Pages*. https://www.neweconomies.co/p/the-ultimate-guide-yc-startups
11. *About protected branches - GitHub Docs*. https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
12. *The Coinbase Seed Round Pitch Deck | by Brian Armstrong*. https://barmstrong.medium.com/the-coinbase-seed-round-pitch-deck-50c8ec91d40b
13. *Pitch Deck Teardown: DeckMatch's $1M seed deck*. https://techcrunch.com/2023/08/18/sample-seed-pitch-deck-deckmatch
14. *SaaS Metrics Checklist: 15 KPIs Every Founder Should Track*. https://baremetrics.com/blog/saas-metrics-checklist-kpis-founders-should-track
15. *Startup Metrics That Matter to Seed Investors (2026)*. https://www.seedforge.com/blog/startup-metrics-that-matter-to-seed-investors
16. *OpenSSF Scorecard - Security health metrics for Open ...*. http://github.com/ossf/scorecard
17. *A guide to seed fundraising : YC Startup Library*. https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising
18. *CAC SaaS: A guide for businesses*. https://stripe.com/resources/more/cac-in-saas
19. *How to Pitch Your Company : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/4b-how-to-pitch-your-company
20. *Continuous integration*. https://docs.github.com/en/actions/get-started/continuous-integration
21. *The SaaS Retention Report: The New Normal For SaaS*. https://chartmogul.com/reports/saas-retention-the-new-normal
22. *The Never Ending Road To Product Market Fit*. https://brianbalfour.com/essays/product-market-fit
23. *One-Pager for Investors: Template and Examples - Fundreef*. https://www.fundreef.com/one-pager-for-investors-template-and-examples
24. *A guide to crafting an effective hackathon judging framework*. https://blog.mettl.com/hackathon-judging-criteria
25. *Steve Blank Customer Development*. https://steveblank.com/tag/customer-development
26. *Notion Pitch Deck: Raised $2M in Seed Round (Slide Analysis)*. https://upmetrics.co/pitch-deck-examples/notion
27. *Track investor engagement with your pitch deck*. https://www.docsend.com/blog/tracking-investor-engagement-pitch-deck
28. *Trust and Credibility: Ecommerce UX | Nielsen Norman Group ...*. https://www.nngroup.com/reports/ecommerce-ux-trust-and-credibility
29. *Technical Debt: Case Studies and Lessons Learned*. https://www.groenewold-it.solutions/en/blog/softwaredev/technical-debt-case-studies-and-lessons-learned
30. *What Is an MVP? Eric Ries Explains - Lean Startup Co.*. https://leanstartup.co/resources/articles/what-is-an-mvp/
31. *Cohort: Net MRR Retention*. https://help.chartmogul.com/article/160-cohort-net-mrr-retention
32. *Stripe Pitch Deck That Raised $4.5B (Detailed Slide Breakdown)*. https://upmetrics.co/pitch-deck-examples/stripe
33. *Secret scanning - GitHub Docs*. http://docs.github.com/en/code-security/concepts/secret-security/secret-scanning
34. *Linear Pitch Deck (2020) — $13M raised from Sequoia Capital | Billion Dollar Pitch Decks*. https://www.billiondollarpitchdecks.com/decks/linear
35. *Learn Performance  |  web.dev*. https://web.dev/learn/performance
36. *About dependency review - GitHub Docs*. https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review
37. *The Design Sprint — GV*. https://www.gv.com/sprint
38. *Stripe Pitch Deck (2010) — $2M raised from Sequoia / Peter Thiel | Billion Dollar Pitch Decks*. https://www.billiondollarpitchdecks.com/decks/stripe
39. *Towards Effective Technical Debt Decision Making in Software Startups | Request PDF*. https://www.researchgate.net/publication/337263748_Towards_Effective_Technical_Debt_Decision_Making_in_Software_Startups
40. *Here's How To Make Your Pitch Deck Investor Ready | DocSend*. https://www.docsend.com/blog/how-your-pitch-deck-can-shine-as-vc-focus-shifts
41. *Fundraising Exposure to Top VCs & Angels*. https://onepager.vc/
42. *Web Vitals  |  Articles  |  web.dev*. https://web.dev/articles/vitals
43. [The Startup One Pager: How to Create One Investors Will Love [Including Templates]](https://visme.co/blog/startup-one-pager)
44. [
	NASPP | Private Company Cap Table Due Diligence
](https://www.naspp.com/blog/private-company-cap-table-due-diligence)
45. *Due Diligence Checklist for Seed Stage Startups: The 2026 Standard | SeedForge Blog*. https://www.seedforge.com/blog/due-diligence-checklist-for-seed-stage-startups-the-2026-standard
46. *Due diligence checklist for venture capital*. https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital
47. *Airbnb Pitch Deck Template | PowerPoint & Google Slides*. https://slidechef.net/templates/airbnb-pitch-deck-template
48. [Airbnb Pitch Deck Template [Download]](https://slidebean.com/templates/airbnb-pitch-deck)
49. *Pitch Deck Examples from 35+ Killer Startups | Slidebean*. https://slidebean.com/pitch-deck-examples
50. *AirBnB Pitch Deck  | PDF*. https://www.slideshare.net/slideshow/airbnb-first-pitch-deck-editable/45768374
51. *The Pitch Deck Airbnb Used to Raise $600K*. https://www.failory.com/pitch-deck/airbnb
52. *Investor Pitch Deck Design | $20M+ Raised | slidemaster.studio*. http://slidemaster.studio/investor-pitch-deck
53. *How to create a pitch deck: Essential skills for early-stage and Series A funding*. https://www.svb.com/startup-insights/startup-strategy/how-to-create-investor-pitch-deck-vc-angels
54. *Pitch Deck Teardown: Encore's $3M Pre-seed / Seed deck | PDF*. https://www.slideshare.net/slideshow/pitch-deck-teardown-encores-3m-preseed-seed-deck/251903456
55. *GitHub README Template (2026): 12 Copy-Paste Examples*. https://gingiris.tools/blog/2026/04/02/github-readme-template-guide
56. *GitHub - jehna/readme-best-practices: Best practices for writing a README for your open source project · GitHub*. https://github.com/jehna/readme-best-practices
57. *Best practices for repositories*. https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
58. *GitHub README Best Practices in 2026: The Complete Guide*. https://pushpen.dev/blog/github-readme-best-practices-2026
59. *claude-code-skills/docs/standards/GITHUB_README_BEST_PRACTICES.md at master · levnikolaevich/claude-code-skills · GitHub*. https://github.com/levnikolaevich/claude-code-skills/blob/master/docs/standards/GITHUB_README_BEST_PRACTICES.md
60. *Status checks*. https://docs.github.com/en/pull-requests/reference/status-checks
61. *OpenSSF Scorecard – Open Source Security Foundation*. https://openssf.org/projects/scorecard
