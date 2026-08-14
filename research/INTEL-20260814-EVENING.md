# INTEL - Evening refresh (2026-08-14, live API verified)

Source: Unstop API (id 1730314) + D3 Fest 2026 site, probed 15:45 IST. ALL VERIFIED.

## 1. Submission format (the deck IS the submission)

- Round 1 "Idea Submission": Aug 15 21:00 -> Aug 16 06:00 IST.
  "Submission round through Unstop platform."
- Submission type: PPT FILE ONLY (pdf or pptx, max 50 MB), MANDATORY.
  No description/text field in the API. Our 4 .pptx decks are exactly the
  right artifact. 50 MB cap is generous (decks are ~107K each).
- allow_multiple_submissions = 1: resubmission allowed, latest wins
  (matches forensics: plain INSERT, dup block on old row).
- Round 2 "Presentation": Aug 16 10:00 -> 17:30 IST.
  "You will be required to present your ideas to judges."
  (Our demo + pitch slot. 3-min demo, 2:30 target stays.)

## 2. Judge scoring schema (from rounds.evaluation_fields)

- Score field: 5-point (score: 5), weighted to 100 (weighted_score: 100).
- Panel buttons: shortlist / reject / hold / noshow.
- "Overall Comments" free-text field (500 char cap, optional).
- weightAutoAdjust: true. One evaluation round.

## 3. Numbers

- registerCount: 456 (was 402 at 09:30, 451 at 14:34).
- players_count: 96 (field-level).
- Round 1 players_count: 378 (participant-level count, different metric).

## 4. Event site

- Unstop web_url now points to: d3fest.techsoc-iiitbbsr.com (D3 Fest 2026,
  Next.js marketing site, LIVE, http 200).
- OLD sites DEAD: craftncode-2026.vercel.app (DEPLOYMENT_NOT_FOUND),
  craftncode.dev (DNS fail).
- Live site routes: / and /gallery only. All other routes (problem-statements,
  tracks, sponsors, judges, schedule, faq, rules) return 404.
- Site links to a Google Drive brochure PDF (28.5 MB, downloaded to /tmp,
  title check pending) + instagram.com/d3fest.iiitbh + linkedin
  (tech-society-iiitbh) + x.com/techsociiitbh.

## 5. Details text (official, worth quoting)

"The official national problem statements will be released only at the
beginning of the National Finals on 30th October 2026 at 8:00 AM IST.
The Rajasthan State Qualifier will follow its own evaluation process and
event flow, and participants need not wait for the national problem
statements to compete in the qualifier."

Reading: state qualifier = independent process, its own statements (Rudra
intel: sponsor-set questions) stay the best signal. No conflict.

## 6. Contacts (3 now)

- Spandan Hota (spandanhota2005@gmail.com) - CSC contact, GSA
- Tirtha Desai (tirthadesai29@gmail.com) - NEW (was not in prior dossiers)
- Abhinav Trikha (+91 95994 15311) - CSC chair

## 7. What this changes

- Nothing on prep: decks are the submission, deck + demo are the pitch.
- The night's submit = upload ONE pptx to Unstop (case-submissions page,
  seo_url confirmed public). Resubmit allowed if we improve later.
- No description field means the deck must carry ALL the story. 4 decks stay
  the right prep. Consider adding a "problem statement restated" slide.
