# DECK-NUMBERS-AUDIT.md (Window C audit, 2026-08-16 ~15:20 IST)

Every number on the deck (scaffold/deck/KrishiSetu-Round0-20260816.pptx)
checked against the research raws (krishisetu research/raw/ and
hackathon-sota-lab research/raw/v2/) and the proof ledger
(craft-n-code/docs/packaging/PROOF-LEDGER-2026.md).

Legend: VERIFIED, VERIFIED-CONDITIONAL (holds under a stated
definition), REFRAME (right number, wrong framing), FLAG (chain broken
or count mismatch).

## 1. THE FIVE NUMBER BLOCKS

| Number | Deck slide | Claimed source | Raw + line | Verdict |
|---|---|---|---|---|
| Dana 5,428 acres, 4 blocks | Slide 2 (problem) | YSD Odisha Cyclone Dana rapid assessment (2025) | d6 content.md line 13 [26]: "A rapid assessment in four blocks of Kendrapara and Bhadrak... reported crop loss over 5,428 acres". Ledger P1 | VERIFIED. Framing correct: deck says "rapid assessment", and d20 line 10 explicitly warns against the "seven-day assessment of 5,428 acres" phrasing, which the deck avoids |
| Yaas 5,882 ha, 5 Balasore blocks | Slide 2 (problem) | Down To Earth, post-Yaas Kharif report | d22 content.md lines 17, 88 [7]: "at least 5,882 ha in five Balasore blocks... seawater impacts" (Down To Earth, 21 June 2021); corroborated d3-refire lines 9, 154, 201; v2 ps07 [7][41]. Ledger P2 | VERIFIED |
| PMFBY 78.4 crore applications, Rs 1.83 lakh crore program | Slides 2 and 9 (rail) | PMFBY program data, dated 2024-2025 | NO raw carries these figures. Searched all content + basis files in both repos: the 78.4 hit is rainfall mm (d1 basis, Akhuapada), 1.83 hits are US$ 1.83M livestock loss and 1.83-day caste flood gap, unrelated. v2 ps07 has 2,817 but no 78.4/1.83. Ledger P3 says "Verified in wave (pmfby.gov.in + press data)" but no raw backs it | FLAG, broken chain: deck -> ledger P3 -> NO raw. Deck must either add the source raw or drop/reword the number before 18:00 |
| Digital Agriculture Mission Rs 2,817 crore | Slide 9 (rail) | Digital Agriculture Mission allocation | d18 content.md line 43 [5]: "Rs 2,817 crore total outlay; AgriStack, Krishi Decision Support System and soil-profile infrastructure are named" (PIB, Sep 2024); v2 ps07 lines 6, 34 [5][30]. Ledger P4 | VERIFIED. Deck framing "funds agri-digital public infrastructure" matches the raw |
| 85/85 suites + 46/46 eval | Slide 5 (prototype) | Fresh run 2026-08-16 07:40 | Ledger rows 2, 3, P5: 85/85 fresh run 2026-08-16 07:40 (approval 13/13, trace 12/12, providers 9/9, multimodal 4/4, provenance 4/4, feeds 8/8, honesty 12/12, stress 23/23), 46/46 lane fixtures | VERIFIED (ledger is the proof artifact for build claims; rerun before demo per ledger condition) |

## 2. RESEARCH MACHINE SLIDE

| Claim | Measured reality | Verdict |
|---|---|---|
| 48 runs | Disk has 49 raw content files (d1-d47 = 47 numbered reports + 2 refires: d3-cascades-refire, d41-global-farm-practices-refire). EVIDENCE-INDEX.md titles itself "The 48-Report Map" | FLAG-count: 48 is the index title, the disk holds 49. Recommend "49 reports (47 numbered + 2 refires)" or fix the index title. Per orchestrator guidance the correct claim is 49 reports |
| 7 waves | EVIDENCE-INDEX.md numbers 6 waves (1-6). The v2 statement-faithful mine (hackathon-sota-lab research/raw/v2, 18 channel files) is the 7th wave | VERIFIED-CONDITIONAL: 7 waves only when the v2 forensics wave is counted. The index document alone shows 6 |
| 2.5M+ chars of raw evidence | krishisetu content.md total = 2,226,960 chars (measured). v2 content.md = 992,409 chars. Combined = 3.22M chars | VERIFIED-CONDITIONAL: holds at 3.2M only when both waves count; krishisetu alone (2.23M) is under 2.5M |
| 4,000+ cited sources | krishisetu content: 2,812 unique URLs, 3,471 mentions. v2 content: 1,326 mentions. Combined ~4,800 mentions | VERIFIED-CONDITIONAL: holds at ~4,800 mentions / ~4,100 unique when both waves count; krishisetu alone = 2,812 unique, under 4,000 |
| A-D evidence grades | Badges ODISHA-MEASURED / TRANSFER-PRIOR / SCENARIO-ASSUMPTION / UNKNOWN are the four-badge honesty contract, present on every record in backend and scaffold agri code | VERIFIED (code-level, audited in AGRI-NUMBERS-AUDIT) |

Note: none of the research machine claims have a PROOF-LEDGER row (P-rows stop at P6). EVIDENCE-INDEX.md serves as the map; the ledger should gain one row for the machine claims block before submission.

## 3. OTHER DECK NUMBERS SWEPT

| Claim | Verdict |
|---|---|
| "17-statement evidence wave" (team slide) | v2 wave = 17 statement-faithful channel-mines + forensics (18 files). VERIFIED |
| "Rs 1.5 lakh crore" / other PMFBY phrasing | Not present on deck; flagged above under the 1.83 lakh crore claim |
| Rule 14 in the advisory example quote ("Source: IMD + rule 14") | R14 = controlled overflow corridor (authority rules.json); the example quote is illustrative, not a claim. No action |

## 4. VERDICT

7 of 9 number blocks verify or verify under a stated definition. One
broken chain (PMFBY 78.4 cr / Rs 1.83 lakh cr, must be sourced or
dropped before 18:00) and one count mismatch (48 runs vs 49 files,
recommend 49). Research machine claims need a ledger row and their
definitions stated (both waves counted). No em dashes in this file, by
rule.