# Research progress: seed-stage startup package

## What is now well established

### 1. Seed pitch-deck structure
The evidence converges on a concise narrative: company and one-line purpose, problem, solution, traction, insight or moat, business model, market, team, and fundraising ask. YC guidance emphasizes clarity, concision, and narrative over exhaustive detail [3]. Its template also recommends a single title slide, a concrete problem, a concise solution, meaningful traction, business model, market, founder-focused team slide, and a clear ask tied to the next milestone [3] [3] [3]. Sequoia's framework independently reaches the same core components, adding why now and competition [33].

The examples show how that structure works in practice:
- Airbnb used an 11-slide story covering problem, solution, validation, market, product, model, adoption, competition, team, and ask [1].
- Its early deck quantified validation with Couchsurfing and Craigslist activity, then connected a 10% commission to the market opportunity [10].
- Coinbase's early material illustrates that a deck can be a set of demo-day slides rather than a formal corporate presentation; the company openly framed an interim financing target and invited investor engagement [29] [29].
- Linear's seed announcement provides a useful modern example of pairing product mission, progress, lead investor, and next hiring priorities [26] [26].
- Notion's original deck is useful evidence for mission continuity: the founding vision still described the company years later [27].
- The DeckMatch teardown is a particularly useful negative example: unclear milestone timing, an overly broad market plan, an ask disconnected from use of funds, and inconsistent funnel, customer, and ARR figures [35] [35] [35].

### 2. Executive summary, one-pager, and investor materials
The research supports treating the executive summary as a one- or two-page pre-read, with one page preferred, covering vision, product, team, traction, market, financials, and fundraising [4]. A VC-style internal memo is similarly short and organized around overview, market, team, model, competition, metrics, diligence, positives, concerns, exit scenarios, and the exceptional upside case [8]. A one-pager should remain genuinely one page and include company, target market, competition, sales strategy, team, milestones, financial overview, and contact information [15] [15] [15].

The materials should be separated by sensitivity: a forwardable snapshot, an emailable deck, a more detailed meeting deck, a financial model, cap table, and data room [36] [36].

### 3. Traction and metrics
The strongest finding is that seed traction must match the company type and stage. The evidence distinguishes pre-seed problem validation from seed solution validation [19]. Advisory benchmarks include roughly $10,000-$25,000 MRR for SaaS, sustained growth, multiple paying customers rather than a single outlier, consumer engagement and cohort retention, and technical de-risking for deep tech [19] [13]. A deck should show the primary metric on a monthly timeline, ideally with cohort or retention evidence where relevant [11] [19].

The report will therefore avoid presenting any single benchmark as a law. The underlying material explicitly warns against a single gold standard and stresses that CAC payback depends on retention and gross margin [39]. Useful supporting metrics include ARR, MRR, churn, CAC, CAC payback, LTV:CAC, cash flow, gross margin, NDR, and acquisition versus expansion [34] [39] [39]. For consumer products, the Sean Ellis "very disappointed" test is a supplementary signal, not proof by itself [30].

### 4. Website and landing page
The website should communicate the value proposition within seconds, using a clear hero headline, concise supporting copy, a visible CTA, product evidence, traction or social proof, and fast mobile performance [17] [17]. The broader landing-page structure is hero, features and benefits, social proof, differentiation, and a short FAQ [48] [48]. The Dub example demonstrates the pattern with a concrete product statement, customer scale, visible conversion actions, reviews, and a trust/security position [32] [32].

### 5. Repository and engineering-readiness evidence
The technical review checklist is now well covered. A repository should make the project understandable and reproducible through a README, setup instructions, usage information, help/maintenance information, tests, configuration, and documentation [31] [31]. CI should build and test changes, including linting, security checks, coverage, and functional tests, with results visible in pull requests [14].

Investor-facing engineering diligence should address architecture and scale assumptions, test coverage, code churn, security, dependency and license risk, IP ownership, and key-person risk [16] [16] [16] [16]. The repository itself can provide useful evidence through history, issues, pull requests, and access controls [6] [6]. A clean-machine build and rollback path are especially persuasive operational signals [24] [24] [24].

### 6. Seed due diligence
The evidence supports seven proof areas: corporate/legal, team, product/IP, market/competition, traction, financials/use of funds, and references [18] [18] [18]. The most serious recurring red flag is an unclean cap table, especially undisclosed SAFEs, departed founders retaining equity, or missing ownership records [18] [18] [18] [18].

The practical data room should cover incorporation and governance, founder and employee agreements, IP assignments, open-source compliance, product/demo access, customer and revenue evidence, financial statements, taxes, contracts, liabilities, and a 12-month plan with hiring and use-of-funds assumptions [2] [9] [25]. References need preparation as well: three to five founder references, customer references, and an understanding that investors may conduct off-list calls [37] [37].

### 7. What can realistically be built and shown in 24 hours
The research supports a narrow, deployed, end-to-end MVP: one user problem, one core workflow, a public URL, basic authentication or access control where needed, graceful empty/error states, a short README, and a demonstrable proof of concept [22] [28] [38]. The 24-hour objective is evidence, not completeness: test the riskiest assumption, collect user feedback, attempt an initial monetization signal, and decide whether to continue, revise, or stop [12] [12].

Manual customer recruitment is appropriate at this stage. The research repeatedly favors direct outreach, founder-led demos, charging early, and tracking conversion rather than prematurely relying on scalable channels [44] [44] [44].

## What remains unanswered or qualified

1. **Canonical original Stripe seed deck.** I found strong secondary descriptions and official Stripe fundraising guidance, but I have not fully verified a single authoritative, complete copy of the original seed deck. The final report should label any slide-by-slide reconstruction as secondary rather than present it as canonical.

2. **Universal traction thresholds.** The reported MRR, growth, retention, and LTV:CAC figures are useful heuristics, but they vary materially by business model, geography, sales cycle, and capital intensity. The final report will identify the source and context for every benchmark and will not imply that passing one number guarantees funding.

3. **What a 24-hour build cannot prove.** A working MVP can demonstrate core functionality, feasibility, and early user reaction. It cannot honestly establish durable retention, repeatable revenue, mature unit economics, production-grade security, or completed legal diligence. That distinction is supported by the MVP, engineering, and diligence evidence [22] [28] [21].

4. **Exact URL-ledger count and hard-length requirement.** The research corpus is broad enough to support the substantive report, but I have not yet completed the final deduplicated ledger proving 120 unique URLs, nor assembled the full 40,000+ character package with every table row individually grounded. That is an assembly and verification task, not a major evidence gap.

5. **Comparability of named startup examples.** Airbnb, Coinbase, Linear, Notion, Stripe, and DeckMatch are useful artifacts, but they represent different years, stages, sectors, and disclosure norms. The final report should use them as examples of patterns and tradeoffs, not as directly comparable benchmark companies.

## Decision

There is now enough evidence for the substantive conclusions and recommendations, but I would not yet claim that the original hard-output requirements have been met. The remaining work is a final source-ledger audit, explicit labeling of primary versus secondary sources, and assembly of the long-form report and seven requested tables without inventing citations or overstating benchmarks.

This last pass should preserve the central rule emerging from the evidence: make the pitch clear and narrow, show real proof, keep the repository and cap table clean, connect the ask to measurable milestones, and be candid about what the current stage does not yet prove.

## References

1. *Airbnb Pitch Deck (2008) — $600K raised from Sequoia Capital | Billion Dollar Pitch Decks*. https://www.billiondollarpitchdecks.com/decks/airbnb
2. *Startups Due Diligence: Guide for Founders + Checklist*. https://dealroom.net/blog/startup-due-diligence
3. *How to build your seed round pitch deck  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck
4. *A guide to seed fundraising  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising
5. *How to design a better pitch deck  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/4T-how-to-design-a-better-pitch-deck
6. *About repositories*. https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
7. *The YC Startup Directory | Y Combinator*. https://www.ycombinator.com/companies
8. *The Investment Memo | NextView Ventures*. https://nextview.vc/blog/the-investment-memo
9. *Due diligence checklist for venture capital*. https://www.affinity.co/guides/due-diligence-checklist-for-venture-capital
10. *AirBnB Pitch Deck  | PDF*. https://www.slideshare.net/slideshow/airbnb-first-pitch-deck-editable/45768374
11. *Startup Traction Guide: Pre-Seed to Series A Metrics*. https://startupfundraising.com/library/articles/how-to-think-about-startup-traction
12. *MVP Hackathon: The Fast-Track Playbook for Organizing Innovation-Driven Hackathons*. https://corporate.hackathon.com/articles/mvp-hackathon-the-fast-track-playbook-for-organizing-innovation-driven-hackathons
13. *Seed Round: definition, 2025 benchmarks (size, valuation, dilution), and the seed-to-Series-A graveyard | Startups.com*. https://www.startups.com/lexicon/seed-round
14. *Continuous integration - GitHub Docs*. https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration
15. [The Startup One Pager: How to Create One Investors Will Love [Including Templates]](https://visme.co/blog/startup-one-pager)
16. *Technical Due Diligence for Startups: What Investors Check in 2026 | SeedForge Blog*. https://www.seedforge.com/blog/technical-due-diligence-for-startups
17. *How to make your startup website design investor-friendly in 2025?*. https://waveup.com/blog/how-to-make-your-startup-website-design-investor-friendly
18. *Due Diligence Checklist for Seed Stage Startups: The 2026 Standard | SeedForge Blog*. https://www.seedforge.com/blog/due-diligence-checklist-for-seed-stage-startups-the-2026-standard
19. *What Is Traction? Metrics That Matter for Pre-Seed & Seed*. https://startupfundraising.com/library/articles/what-is-traction-for-a-startup
20. *Pricing – Linear*. https://linear.app/pricing
21. *Sample VC Due Diligence Request List | Cooley GO*. https://www.cooleygo.com/documents/sample-vc-due-diligence-request-list
22. *What is a Minimum Viable Product (MVP)? How to Get Started*. https://www.atlassian.com/agile/product-management/minimum-viable-product
23. *Product market fit*. https://review.firstround.com/series/product-market-fit
24. *Continuous Integration*. https://martinfowler.com/articles/continuousIntegration.html
25. *Venture capital due diligence best practices*. https://www.affinity.co/guides/venture-capital-due-diligence-best-practices
26. *Linear’s Next Chapter: Announcing our $4.2M Seed Round*. https://linear.app/now/linear-s-next-chapter-announcing-our-usd4-2m-seed-round
27. *x.com*. https://x.com/ivanhzhao/status/1815475431052804420
28. *Hackathon Judging Criteria & Scorecard Template | Opportunity Hack*. https://www.ohack.dev/hackathon-judging-criteria
29. *Medium*. https://barmstrong.medium.com/the-coinbase-seed-round-pitch-deck-50c8ec91d40b
30. *Product/Market fit survey by Sean Ellis and GoPractice*. https://pmfsurvey.com/
31. *About the repository README file*. https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
32. *About | Dub*. https://dub.co/about
33. *Writing a Business Plan | Sequoia Capital*. https://sequoiacap.com/article/writing-a-business-plan
34. *SaaS Metrics & Benchmarks Resource Guide | OpenView Labs*. https://openviewpartners.com/blog/saas-metrics-and-resources
35. *Pitch Deck Teardown: DeckMatch's $1M seed deck | TechCrunch*. https://techcrunch.com/2023/08/18/sample-seed-pitch-deck-deckmatch
36. *Build Your Investor Pipeline Worksheet*. https://toolkit.techstars.com/build-your-investor-pipeline-worksheet
37. *How to Reference Check a Founder*. https://www.goingvc.com/post/how-to-reference-check-a-founder
38. *Hackathon judging: 6 criteria to pick winning projects - TAIKAI*. https://taikai.network/en/blog/hackathon-judging
39. *SAAS 2023 BENCHMARKS REPORT*. https://library.avpcap.com/wp-content/uploads/2023/11/OpenView-2023-SaaS-Benchmarks-report.pdf
40. *UX & Usability Articles from Nielsen Norman Group - NN/G*. https://www.nngroup.com/articles/
41. *GitHub - makeplane/plane: 🔥🔥🔥 Open-source Jira, Linear, Monday, and ClickUp alternative. Plane is a modern project management platform to manage tasks, sprints, docs, and triage. · GitHub*. https://github.com/makeplane/plane
42. *DocSend Startup Index - 2021 Pitch Deck Metrics | DocSend*. https://www.docsend.com/pitch-deck-metrics
43. *Google SRE - Defining slo: service level objective meaning*. https://sre.google/sre-book/service-level-objectives
44. *How to get your first customers  : YC Startup Library | Y Combinator*. https://www.ycombinator.com/library/Ip-how-to-get-your-first-customers
45. *About Dependabot alerts - GitHub Docs*. https://docs.github.com/code-security/dependabot/dependabot-alerts/about-dependabot-alerts
46. *Stripe Pitch Deck Template - PitchGrade*. https://pitchgrade.com/templates/stripe-pitch-deck-template
47. *Enabling secret scanning for your repository*. https://docs.github.com/en/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enable-secret-scanning
48. *The Ultimate Guide: Create SaaS Landing Pages That Convert*. https://www.leadfeeder.com/blog/conversion-optimization/saas-landing-pages-that-convert
49. *Stripe Pitch Deck That Raised $4.5B (Detailed Slide Breakdown) - Upmetrics*. https://upmetrics.co/pitch-deck-examples/stripe
