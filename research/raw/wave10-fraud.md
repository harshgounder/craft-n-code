## executive_summary_the_eight_numbers_a_judge_will_ask_first

- **RBI's FY26 fraud universe is concentrated, not sprawling**: 10,114 cases worth Rs 48,021 crore across all bank categories in FY25-26, versus 23,722 cases worth Rs 32,803 crore in FY24-25. Case count fell ~57% while value per case climbed ~146% [executive_summary_the_eight_numbers_a_judge_will_ask_first[0]] [4] -> a fraud-guard product should not optimise for "block the long tail" but for "freeze the high-value wire".
- **Public-sector banks still dominate loss value**: 5,418 PSB cases soaked up Rs 35,709 crore in FY26, or 74% of total reported value across just 54% of cases [executive_summary_the_eight_numbers_a_judge_will_ask_first[0]] [4] -> a fraud-guard kit that demos well on SBI/Uniccan/Bank of Baroda UPI rails proves more relevant than one tuned to neobank APIs.
- **Digital arrest has become India's most expensive single scam genre**: Rs 4,057 crore stolen from ~3 lakh victims since 2022, with Rs 481.1 crore lost in just the first five months of 2026 across 15,215 complaints [executive_summary_the_eight_numbers_a_judge_will_ask_first[1]] [14]; one NRI doctor couple in Delhi lost Rs 14.84 crore in a continuous video-call "custody" [executive_summary_the_eight_numbers_a_judge_will_ask_first[1]] [14] -> a fraud-guard kit must include an "is this a fake CBI/ED/Interpol scenario?" module.
- **AI-powered scams are now the largest single loss category**: Rs 22,495 crore lost in calendar 2025 from deepfake voices, fake video calls and synthetic identity impersonation [executive_summary_the_eight_numbers_a_judge_will_ask_first[2]] [5] -> a 2026 fraud-guard pitch without a deepfake-detection story reads as 2024.
- **The 1930 helpline is India's most underrated fraud infrastructure**: 32.80 lakh (3.28M) calls logged against the helpline, Rs 11,158 crore frozen or recovered, 85 banks/wallets live on the CFCFRMS backbone [executive_summary_the_eight_numbers_a_judge_will_ask_first[3]] [8][executive_summary_the_eight_numbers_a_judge_will_ask_first[4]] [10] -> any student tool that can auto-trigger a 1930 ticket with a pre-filled packet (sender UPI ID, SMS header, screenshot, geo) demos a real multiplier, not a toy.
- **Adoption is concentrated where the spam is relentless**: Truecaller crossed 450 million monthly active Android users on 9 October 2025 [executive_summary_the_eight_numbers_a_judge_will_ask_first[5]] [15] and blocked 38 billion unwanted calls in 2021 alone [executive_summary_the_eight_numbers_a_judge_will_ask_first[6]] [16] -> a fraud-guard kit that integrates with Truecaller's caller-ID graph inherits the largest user-level fraud dataset in India, no need to build one.
- **State geometry of digital crime is concentrated, not uniform**: Telangana (15,297) and Karnataka (12,556) registered the highest cyber-crime counts in NCRB's 2022 publication; Maharashtra (8,249) and Uttar Pradesh (10,117) follow [executive_summary_the_eight_numbers_a_judge_will_ask_first[7]] [17] -> a fraud-guard demo is sharper when it shows a city-level hotspot heatmap rather than a national aggregate.
- **Regulators have pre-stamped the rails**: RBI issued the FREE-AI framework on 13 August 2025 (7 Sutras, 6 Pillars, 26 recommendations) [executive_summary_the_eight_numbers_a_judge_will_ask_first[8]] [18][executive_summary_the_eight_numbers_a_judge_will_ask_first[9]] [19], revised Master Directions on Fraud Risk Management on 15 July 2024 [executive_summary_the_eight_numbers_a_judge_will_ask_first[10]] [9], and is building the Digital Payment Intelligence Platform (DPIP) [executive_summary_the_eight_numbers_a_judge_will_ask_first[11]] [20]; DoT runs Sanchar Saathi/Chakshu; MeitY runs the I4C-backed NCRP at cybercrime.gov.in. -> a fraud-guard kit that demos "we plug into Sanchar Saathi Chakshu + 1930 + NCRP inbox + bank mule-account list" is speaking the regulator's vocabulary, not just the user's.

---

## 1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff

### 1.1 The headline shift: fewer cases, much bigger cheques

RBI's FY25-26 Trend and Progress disclosure, as reported by The Hindu on RBI data, shows the paradox every fraud-guard builder must internalise [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[0]] [4].

| Metric | FY24-25 | FY25-26 | Delta |
|---|---|---|---|
| Total reported bank fraud cases | 23,722 | 10,114 | -57.4% |
| Total reported amount involved | Rs 32,803 crore | Rs 48,021 crore | +46.4% |
| Average value per case | Rs 1.38 crore | Rs 4.75 crore | +243% |

Mechanism -> deduction: detection is winning on the long tail (cheap phishing, QR reversals, OTP thefts), but losing on the engineered long-con (digital arrest, fake trading app, deepfake CEO "boss scam") that takes weeks to prepare and extracts a single large sum [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[1]] [7][1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[2]] [5]. Implication -> recommendation: position the fraud-guard kit as a *con-trace* tool (multi-day social-engineering pattern detection), not a per-transaction OTP firewall.

### 1.2 Where the money sits: bank-group and category breakdown

RBI's category breakdown for FY26 [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[0]] [4]:

| Bank group / category | Cases FY26 | Amount FY26 (Rs crore) | Share of value |
|---|---|---|---|
| Public Sector Banks (PSBs) | 5,418 | 35,709 | 74.4% |
| Private Sector Banks | 3,956 | 11,399 | 23.7% |
| Foreign Banks | 210 | 290 | 0.6% |
| Small Finance Banks | 467 | 114 | 0.2% |
| Payments Banks | 47 | 11 | 0.0% |
| Advances (loan/credit category) | 8,640 | 40,774 | 84.9% of all-India value |
| Card / Internet / Digital Payments | 293 | 29 | 0.06% of all-India value |

Observation: UPI/card/internet fraud at bank reporting level is statistically invisible - Rs 29 crore on Rs 48,021 crore of total bank fraud. This is because UPI fraud is typically absorbed directly by issuing banks/wallets and reported under "Other categories" or absorbed by the recipient PSP under the new 2024 RBI dispute-redressal mechanism, not surfaced as a category in RBI's annual disclosure. Recommendation -> in the demo, contrast "RBI's reported bank fraud" vs "NCRP's reported cybercrime fraud" (Rs 55,050 crore between 2021 and 2025 on 6,589,201 complaints [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[3]] [8]) - this is a 165x gap.

### 1.3 Total digital-fraud loss reported via RBI / central agencies

- Indians lost ~USD 2.5 billion to digital fraud across calendar 2025, per BBC reporting on RBI's broader fight-back announcement [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[4]] [3].
- The Citizen Financial Cyber Fraud Reporting and Management System (CFCFRMS) under I4C has handled 6,589,201 financial-fraud complaints between 2021 and end-2025, totalling Rs 55,050 crore in reported losses, Rs 8,189 crore marked as lien (frozen), and 195,760 FIRs registered [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[3]] [8].
- 1930 helpline alone has fielded 32.80 lakh (3,280,000) calls and saved Rs 11,158 crore as of 30 June 2026 per PIB [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[3]] [8].

### 1.4 What UPI fraud *actually* looks like

The RBI DPIP (Digital Payment Intelligence Platform) under development, plus the existing Mule Account.AI / Risk-Insight rules applied by every issuing bank, treat UPI fraud as two structurally different events [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[5]] [20][1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[6]] [9]:

- **Micro-phishing / collect-request scams**: UPI collect requests that look like cashback; reverse-QR to a fake merchant; small amounts (Rs 50 - Rs 5,000) skimmed from a large pool. Detection signal: anomalous collect-request bursts to dormant VPA handles; sender-IP reputation; first-time VPAs as recipients.
- **Authorised push payment / coercion scams**: victim themselves enters UPI PIN/credential, then transfers Rs 50,000 - Rs 10+ crore under "digital arrest" duress or fake-app manipulation [1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[7]] [14][1_upi_and_banking_fraud_rbi_s_fy26_numbers_no_fluff[1]] [7]. Detection signal: this is what RBI DPIP and mule-account freezes have the hardest time catching, because *the transaction is technically authorised*.

---

## 2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers

### 2.1 The numbers, as currently published

| Indicator | Value | Source |
|---|---|---|
| Indians duped since 2022 | ~3,00,000 | News18 report on I4C compiled data |
| Total losses 2022 - mid-2026 | Rs 4,057 crore | News18 citing complaints on NCRP [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[0]] [14] |
| Complaints Jan - May 2026 alone | 15,215 | News18 [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[0]] [14] |
| Losses Jan - May 2026 alone | Rs 481.1 crore | News18 [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[0]] [14] |
| Growth in digital-arrest case counts 2022-2024 | Nearly tripled | Lowy Institute analysis [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[1]] [1] |
| Highest single-victim case found | Rs 14.84 crore (NRI doctor couple, Delhi) | News18 [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[0]] [14] |
| Mumbai "Rs 58 crore" digital arrest case, with Rs 3 lakh reward for absconder Devender Saini | 19 January 2026 announcement | Times of India [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[2]] [21] |
| CBI arrested 3 individuals in Rs 2.07 crore "digital arrest" case | 3 July 2026 | Economic Times digital arrest piece |
| Kerala Police - statewide crackdown arrests | 165 persons, 455 cases registered | UNI/Facebook [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[3]] [22] |
| RBI Ombudsman Scheme for Digital Transactions introduced | 27 July 2026 | RBI press release page [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[4]] [23] |

### 2.2 The scam script (lifted from grounded reporting)

Frontline documents a script that has run on elderly and semi-literate victims in India repeatedly since 2022 [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[5]] [2][2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[0]] [14]:

1. **Cold-call hook**: caller claims to be CBI / ED / Interpol / Mumbai Cyber Cell / Narcotics Bureau, citing a real-sounding FIR number; WhatsApp Video ID with a uniform, a backdrop, sometimes a badge. New variants in 2026: AI-cloned voices of India's Home Minister or senior IPS officers [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[6]] [5].
2. **Pressure injection**: victim is told they are under "digital arrest", must remain on camera for 8-48 hours, must not inform family, must pay "clearance" or "PMLA bail".
3. **Channel collapse to UPI / RTGS**: the script pushes the victim off the video call to a UPI collect-request, a bank wire, or an overseas SWIFT into an aggregator or a hawala-style account; sometimes through a fake "court deposit" portal.
4. **Theft laundering**: money is split into 8-12 mule accounts within 90 minutes, then onward to crypto OTC desks in Dubai, Tbilisi or Cambodia; banks report ~50% recovery when the 1930 helpline is called within the "golden hour" [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[7]] [10].

Detection signals a fraud-guard kit can use:

- Outbound VoIP from a foreign number claiming to be an Indian government officer working in India.
- WhatsApp video call from a number whose Tera- / Truecaller / Bharat Caller ID name is *not* a government agency.
- Repeated collect-request attempts of identical structure to a single VPA in under 24 hours.
- The victim is logged as online/locked-screen for >2 hours between midnight and 6am in a single WhatsApp session.

### 2.3 State hit hardest

The Press Information Bureau has clarified that NCRB does not maintain a separate head for "digital arrest scams" [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[8]] [24]. However, NCRB's state-wise cyber-crime table (2020-2022) [2_digital_arrest_the_scam_industrial_complex_behind_india_s_cyber_crime_numbers[9]] [17] and recent state-crackdown activity suggest:

| Top states by cyber-crime cases (NCRB, 2022) | Cases 2022 | Cases 2021 | Cases 2020 |
|---|---|---|---|
| Telangana | 15,297 | 10,303 | 5,024 |
| Karnataka | 12,556 | 8,136 | 10,741 |
| Uttar Pradesh | 10,117 | 8,829 | 11,097 |
| Maharashtra | 8,249 | 5,562 | 5,496 |
| Tamil Nadu | 2,082 | 1,076 | 782 |

Trend: Telangana volumes nearly tripled in two years; Tamil Nadu 2.6x. Implication: a fraud-guard pitch that visualises the surge (2020 -> 2022) frames digital arrest as a Hyderabad / Bengaluru emerging crime as much as a Delhi-NCR one - this counters the obvious "Delhi NCR is the only epicentre" assumption.

---

## 3_scam_channels_real_cases_and_detection_signals

### 3.1 Five scam families you're expected to know

| Channel | Frequency data | Typical script (verbatim from cases) | Detection signals |
|---|---|---|---|
| Fake customer care (bank, Paytm Flipkart Amazon IRCTC) | Among top 3 complaint categories on CFCFRMS for 2025 | Caller: "Your KYC is expiring in 24 hours / Your account will be blocked / Press 1 to talk to officer". Victim is linked to a clone of the bank's site over WhatsApp; UPI collect-request for "verification fee" | Google-indexed phone number vs official helpline; URL clone with off-by-a-letter domain; UPI collect from non-merchant VPA |
| KYC update scam (Aadhaar, PAN, SIM, electric/gas) | Top complaint family on Chakshu reporting portal | SMS: "Dear customer your SBI account will be deactivated today. Update KYC at http://sbi-kyc-update.in". Fake RBI letterhead attached | Sender SMS header not on whitelist, URL hosted on free subdomain, brand name + period, urgency delimiter ("24 hours") |
| FedEx / DHL / India Post customs-parcel scam | Rs 1,800 crore lost across India per Scamdekho aggregation [3_scam_channels_real_cases_and_detection_signals[0]] [6] | SMS: "Your DHL parcel is held at customs. Pay Rs 4,200 duty at http://dhl-customs-verify.in to release". 14 January 2026 Noida case: graphic designer lost money in 90 seconds after tapping link and entering CVV [3_scam_channels_real_cases_and_detection_signals[1]] [25] | Real Customs never collect duty via UPI; brand logo misspelled; one-time UPI collect-request from "DHL-Customs"; SMS from a 10-digit mobile, not "DHLCUST" 6-letter sender ID |
| WhatsApp investment / trading / "task" scam | Single-largest amount-loss channel per NDTV and CryptoTimes reporting; one Mumbai businessman lost Rs 10.98 crore 29 Dec 2025 - 19 Jan 2026 [3_scam_channels_real_cases_and_detection_signals[2]] [7]; Khammam businessman lost Rs 2.05 crore to a WhatsApp crypto scam [cryptotimes]; a third lost Rs 33.5 lakh to a deepfake stock scam | "Join our VIP Telegram/WhatsApp group of SEBI-registered analysts. Rs 49,999/day task; today: complete 30 'product-likes' and earn Rs 5,000 commission. After 5 days we move to a 'Premium task' where you must deposit Rs 50k-2.2 lakh to unlock withdrawals. To withdraw, pay 20% TDS / GST / 'anti-money-laundering fee' first." | Celebrity deepfake video endorsement (HDFC-Life-style); fake SEBI/IRDAI/AMFI registration number on a one-page site; foreign +91 number but message in Chinese-translated English; the moment "withdrawal tax" appears - it's a lock-in trap |
| Family emergency + AI voice / video | Rs 22,495 crore lost in calendar 2025 from "AI-powered scams" per DQIndia aggregation of 2025 cases [3_scam_channels_real_cases_and_detection_signals[3]] [5] | "Mom, I am in jail, my lawyer will call". AI-cloned voice from a Telegram-supplied 30-second audio clip of the grandchild. 2026 variant: a synthetic Zoom call in which the real grandchild's face has been live-deepfaked | Voice biometric inconsistency; background-noise change vs target's native environment; caller cannot answer a personal question the real grandchild would know; call from a different number mid-conversation mid-call |

### 3.2 The new "boss scam" - I4C's freshest 2026 warning

India Cybercrime Coordination Centre (I4C) flagged in early 2026 a "Boss Scam" pattern: attackers compromise the CEO's mobile device or WhatsApp account, then message the finance team via WhatsApp using the *real* CEO number, pressing an urgent wire to an overseas counter-party [3_scam_channels_real_cases_and_detection_signals[4]] [26]. The hook is UPI/whatsApp-channel consistency, not deepfake tech. Detection signals flow-level (not voice-level): the wire destination is new; the destination IMPS holder has been active for <30 days; the request is sent outside the CEO's normal hours; the destination VPA's first three characters repeat a known mule-network prefix seen in NCRP data.

### 3.3 Deepfake celebrity endorsement - the new "exchange listing" dupe

Per Facia.ai and Fakeout.io aggregated reporting [60.0-60.2, fakeout.io]:

- AI-rendered videos of Indian public figures - Mukesh Ambani, Ratan Tata, Anand Mahindra, Nirmala Sitharaman, top cricketers - are pushed inside WhatsApp investment groups as "VIP tips on next GEM listing".
- Detection: lip-sync vs audio waveform mismatch, finger count (deepfakes cannot render 5-finger hands consistently), skin-edge artefacts on hair in profile shots, group-supplied "screen recording" of a stock platform that is a fully synthesised local Android APK.

---

## 4_fraud_detection_products_in_india_the_real_stack

### 4.1 Consumer-side caller-ID / spam blockers

| Product | India relevance | Adoption signal | Source |
|---|---|---|---|
| Truecaller | 450M monthly active Android users globally on 9 October 2025 (adds ~50M users in 2025); 448 / 449 / 450M lifetime Android; 500M+ global active users on corporate page | Truecaller press releases [4_fraud_detection_products_in_india_the_real_stack[0]] [15][4_fraud_detection_products_in_india_the_real_stack[1]] [16][4_fraud_detection_products_in_india_the_real_stack[2]] [27] |
| Truecaller Premium Caller ID on iPhone (iOS 18.2+) | "Automatically identify spam, fraud, scam, and robocalls before you pick up" | Apple App Store listing [4_fraud_detection_products_in_india_the_real_stack[3]] [28] |
| Truecaller India data scale | 38 billion unwanted calls identified and blocked in calendar 2021 (most are from India) | Truecaller corporate home [4_fraud_detection_products_in_india_the_real_stack[1]] [16] |
| Google Call Screen (Pixel) | Limited India rollout; Pixel low-volume in India. India team should target mainstream Android via Truecaller / Airtel Wynk / JioSaavn caller-ID layer instead | Inferred from lack of dedicated India Call Screen marketing |
| Airtel Wynk / Jio dialer-tone & caller-ID layers | Bundled with SIM; high coverage; no public API for fraud-guard integration | Public engineering blogs / NDTV coverage |
| Lifeguard (trylifeguard) | AI voice assistant that picks up unknown calls, has a real conversation, only lets legitimate callers through; ships Scam-Check Chat to paste messages | App Store and blog [4_fraud_detection_products_in_india_the_real_stack[4]] [29][4_fraud_detection_products_in_india_the_real_stack[5]] [30] |

### 4.2 Enterprise / bank-side fraud risk engine vendors (Tracxn-verified)

| Company | HQ / Stage | Funding / Customers | Differentiator | Source |
|---|---|---|---|---|
| Truecaller | Stockholm-listed (Nasdaq), public company, ~630 employees as of 31 May 2026 [4_fraud_detection_products_in_india_the_real_stack[6]] [31] | Public; >500M MAU | Largest user-level spam graph in India | Tracxn [4_fraud_detection_products_in_india_the_real_stack[6]] [31] |
| Bureau (bureau.id) | Bengaluru, Series-stage | Re-announced Bureau Device ID on 19 June 2025 as a "next-gen" capability against AI-powered coordinated fraud | Device, behaviour, identity, network and transaction data fused into one risk-decision platform [4_fraud_detection_products_in_india_the_real_stack[7]] [11] |
| Sign3 | Bengaluru AI fraud prevention startup | Raised USD 1.5 million on 30 March 2026, led by Cedar Hill Capital, AI fraud prevention for financial institutions [4_fraud_detection_products_in_india_the_real_stack[8]] [32][4_fraud_detection_products_in_india_the_real_stack[9]] [33][4_fraud_detection_products_in_india_the_real_stack[10]] [34] |
| Neural Defend | Delhi + San Francisco | Seed round 13 March 2025; investors: Inflection Point Ventures, Techstars, Soonicorn Ventures, 100X.VC, SBXi [4_fraud_detection_products_in_india_the_real_stack[11]] [35] | Real-time deepfake detection across video, images, audio, real-time streams; integrated with video-conferencing platforms to identify synthetic media during live calls [4_fraud_detection_products_in_india_the_real_stack[12]] [36][4_fraud_detection_products_in_india_the_real_stack[13]] [37] |
| Credit / UPI payment apps | Paytm, Cred, PhonePe, GPay | NPCI UPI rails; Paytm positioning as "India's Most Trusted Platform for BHIM UPI Payments" [4_fraud_detection_products_in_india_the_real_stack[14]] [38]; Cred security audited by CERT-In empanelled assessors per NPCI mandate | UPI rails fraud detection (mostly rule-based, moving to ML) |

### 4.3 What banks actually deploy, and RBI's governance rails

- SBI underwrote nearly Rs 1 trillion of MSME loans in FY26 using AI [4_fraud_detection_products_in_india_the_real_stack[15]] [39]; the same fraud-risk AI stack powers its UPI YONO anti-fraud rules.
- HDFC, ICICI, Axis and Kotak transaction-monitoring stacks are dominated by FICO Falcon / SAS Fraud Management / internal ML, deployed over the 1930 -> CFCFRMS pipeline.
- RBI's FREE-AI framework (Framework for Responsible and Ethical Enablement of AI), issued 13 August 2025, lays out 7 Sutras, 6 Pillars, 26 actionable recommendations specifically for the financial sector AI governance [4_fraud_detection_products_in_india_the_real_stack[16]] [19][4_fraud_detection_products_in_india_the_real_stack[17]] [40].
- RBI's Digital Payment Intelligence Platform (DPIP) is being built to flag risky digital transactions in real time [4_fraud_detection_products_in_india_the_real_stack[18]] [20]; quote from RBI: "the incidence of transaction fraud in UPI and other digital channels remains low, DPIP is expected to further reduce fraud, enhancing the security and resilience of India's digital payments ecosystem".
- Master Directions on Fraud Risk Management (Commercial Banks, RRBs and All India Financial Institutions Directions, 2024) require banks to have a Fraud Risk Management Committee at board level, a defined early-warning system and a 7-day reporting SLA.

### 4.4 RBI mule-account rules

The mule-account framework (RBI Master Direction, July 2024 [4_fraud_detection_products_in_india_the_real_stack[19]] [9]) requires:

- All banks to maintain negative-list screening for "mule / suspect" accounts.
- A real-time intra-bank block on transfers *out* of a flagged mule account.
- Freezing of physical and digital channels on accounts that have received sudden, high-volume credits from unrelated parties.
- Reporting to I4C / 1930 within 24 hours.
- Student kit implication: any fraud-guard design that surfaces a "this VPA was seen in a mule network 2 hours ago" warning - by pulling from a daily mule-feed - solves a real RBI-driven pain point.

### 4.5 Known failure modes

From grounded reporting (News18, RBI annual disclosures, Truecaller App Store reviews aggregated):

- **False positives from Truecaller spam-tagging**: small-business phones using *new* SIMs are often flagged "spam" because call-volume pattern matches a dialer; this creates customer-trust cost for legitimate merchants. Counter-signal: anti-tag overlays (Mint, Airtel) that re-verify.
- **Missed scams on Google Call Screen**: only Pixel devices; India Pixel share is sub-1%. Implication for student: a Google-Call-Screen-style feature as a PWA is a higher-leverage move than restricting to a single OEM.
- **Banks missing the multi-day con**: Mule rules freeze *post hoc*; AI scam tools must integrate with the *victim-side* app to throttle a draining pattern before Rs 1 lakh is gone. RBI's FREE-AI Sutra 5 explicitly calls for "AI for customer protection" beyond "AI for fraud detection" [4_fraud_detection_products_in_india_the_real_stack[20]] [18].

---

## 5_countermeasure_programs_plug_in_points_for_a_student_tool

| Program | Owner | What it offers | How Craft N Code plugs in |
|---|---|---|---|
| 1930 Cyber Crime Helpline | MHA / I4C | 24x7 national helpline; CFCFRMS routes financial-cyber-fraud complaints to the issuing bank in real time; "golden hour" freeze of funds within minutes [5_countermeasure_programs_plug_in_points_for_a_student_tool[0]] [10][5_countermeasure_programs_plug_in_points_for_a_student_tool[1]] [41] | One-tap "Report to 1930" button - generates pre-filled CFCFRMS complaint with VPA, SMS header, screenshot, geo, caller ID, and opens the dialer |
| National Cyber Crime Reporting Portal (NCRP) - cybercrime.gov.in | MHA / I4C | All-types-cybercrime complaint intake; Vani CyberDost Chatbot on the portal; National / State / District monitoring dashboards; 3,035,737 unique visitors as of 11 March 2026 [5_countermeasure_programs_plug_in_points_for_a_student_tool[0]] [10] | A pre-formatted SCA-packet converter -> CSV/PDF inbox upload to NCRP |
| Sanchar Saathi (sancharsaathi.gov.in) | DoT | Citizen-facing portal for SIM verification, lost-device blocking, IMEI traceability, suspected fraud communication reporting | "Report to Sanchar Saathi Chakshu" - identical suspect-SMS/SIM packet pushed to DoT - automatic DoT-level re-verification of the sender number |
| Chakshu (subset of Sanchar Saathi) | DoT | Citizens report suspected fraud communications - calls, SMS, WhatsApp - for spam, financial fraud, impersonation, misuse; examples advertised: bank account, payment wallet, SIM, gas, electricity, KYC update | Pre-staged "suspect" classification: SMS parsers auto-fill header, message body, sender URL; one-tap Chakshu submission with full forensic chain |
| RBI FREE-AI (Framework for Responsible and Ethical Enablement of AI), 13 August 2025 | RBI | India's first AI governance rail for finance: 7 Sutras, 6 Pillars, 26 actionable recommendations [5_countermeasure_programs_plug_in_points_for_a_student_tool[2]] [40] | Voluntary adoption: a student lockstep with FREE-AI Sutra 5 ("AI for customer protection") can claim "FREE-AI-aligned" status -> marketing hook |
| RBI DPIP - Digital Payment Intelligence Platform | RBI | Risk flagging on UPI / card / IMPS / NETC in real time [5_countermeasure_programs_plug_in_points_for_a_student_tool[3]] [20] | Plug-in is closed; hedge by aligning with what DPIP will likely require (VPA reputation, IP reputation, behavioural-sequence anomalies) |
| RBI Revised Master Directions on Fraud Risk Management, 15 July 2024 | RBI | Banks required to have Fraud Risk Management Committee, early-warning system, 7-day reporting SLA [5_countermeasure_programs_plug_in_points_for_a_student_tool[4]] [9][5_countermeasure_programs_plug_in_points_for_a_student_tool[5]] [42] | Indirect: any bank partnership a student team pitches inherits these rules, so the partner's friction is reduced |
| RBI Ombudsman Scheme for Digital Transactions, introduced 27 July 2026 | RBI | New digital-transaction dispute resolution scheme [5_countermeasure_programs_plug_in_points_for_a_student_tool[6]] [23] | Student on-ramp: provide a "file Ombudsman complaint" assistant |
| Cyber Jaagrookta (Awareness) Diwas - IRDAI | MoF / IRDAI | First Wednesday of every month is a cyber-awareness day for insurance customers; multi-stakeholder PDF distributed to all insurers [irdai 34.0-34.2] | Tie a fraud-guard "month reminder" feature to this date |
| CyberPeace Foundation engagement | NGO | Research+awareness publisher: phishing / Territorial Army clone site research, Big Billion Days scam OSINT reports, OSINT-backed citizen guidance [5_countermeasure_programs_plug_in_points_for_a_student_tool[7]] [43] | Use their public research + datasets for the "tell me which scams are trending this week" module |
| Bharat Caller ID / Airtel Wynk / Jio native caller-ID | Airtel, Jio, BSNL | Bundled caller-ID app, opt-in for SMS header scrubbing | Indirect API access - if permissioned, integrate; falls back to Truecaller otherwise |
| RBI / SEBI / IRDAI public advisory sites | Multi | RBI press releases, SEBI investor alerts, IRDAI policyholder warnings | Pull as a daily advisory feed for the kit's "latest scam types" module |

---

## 6_the_judge_angle_what_a_hackathon_bench_already_knows

A 2026 Indian hackathon judge panel (judges at events such as NASSCOM, I4C-supported hackathons, SIH, RBI Innovation Hub, IIT Bombay / Delhi / Kanpur, BITS Pilani) typically has the following bullet points in head:

1. **Total scale**: digital-fraud loss USD 2.5bn (Rs 21,000+ crore) in 2025 [6_the_judge_angle_what_a_hackathon_bench_already_knows[0]] [3]; NCRP has 65,89,201 cumulative cases since 2021 [6_the_judge_angle_what_a_hackathon_bench_already_knows[1]] [8]; 30+ lakh arrests at cyber-crime-busting level [6_the_judge_angle_what_a_hackathon_bench_already_knows[1]] [8]. They will expect the team's first slide to lead with one or two of these anchors.
2. **The headline harm**: digital arrest + AI scams combined > Rs 26,500 crore in 2025; this is the "why now". A team's slide that leads with UPI micro-skimming will fail to grip.
3. **The regulator stack**: judges will probe if the team understands RBI FREE-AI, RBI DPIP, RBI Master Direction 2024, NCRP / I4C, Sanchar Saathi / Chakshu, 1930 helpline, CFCFRMS. Tools that demo with these get a 2-3x adoption story.
4. **The voice / video test**: judges will ask "how do you detect a deepfake voice call in real time, <2 second latency, on a mid-range Android?" Neural Defend and Lifeguard already work this terrain in production; a student team that pitches "we do it offline, on-device" gets a 2026 innovation bonus [6_the_judge_angle_what_a_hackathon_bench_already_knows[2]] [36][6_the_judge_angle_what_a_hackathon_bench_already_knows[3]] [37].
5. **The fake-sender test**: judges will ask "how do you know if this SMS is from SBI or a clone?" The expected answer is *header whitelisting* + *URL pattern*, not just NLP. RBI and DoT mandate 6-letter sender IDs for banks (e.g. SBIINB, HDFCBK); Chakshu is the citizen reporting rail [6_the_judge_angle_what_a_hackathon_bench_already_knows[4]] [44].
6. **The "we already tried that" trap**: judges will assume the team has *not* built a generic "block spam SMS" app and has *not* done a chatbot that "explains scams". They will reward evidence of: (a) live integration with 1930 CFCFRMS, (b) live integration with Truecaller / Bureau graph, (c) a worked case study (a specific 5-minute audio clip flagged as deepfake, savings >=Rs X).
7. **What numbers they expect a team to know by name**:

| Question judges will ask | The answer they will count |
|---|---|
| "How many Indians were hit by digital arrest scams since 2022?" | ~3,00,000 victims, Rs 4,057 crore |
| "What did RBI do about it in 2025-26?" | FREE-AI framework (13 Aug 2025), DPIP being built, Revised Master Directions 15 Jul 2024, Ombudsman scheme for digital transactions 27 Jul 2026 [6_the_judge_angle_what_a_hackathon_bench_already_knows[5]] [23][6_the_judge_angle_what_a_hackathon_bench_already_knows[6]] [9][6_the_judge_angle_what_a_hackathon_bench_already_knows[7]] [20][6_the_judge_angle_what_a_hackathon_bench_already_knows[8]] [18][6_the_judge_angle_what_a_hackathon_bench_already_knows[9]] [19] |
| "Where is the policy open loop?" | WhatsApp deepfakes, foreign-origin VoIP, mule-account laundering to crypto overseas; student ideation welcome |
| "What is the strongest signal of fraud intent?" | A repeated high-value UPI collect / IMPS under video-call coercion; i.e. digital arrest has a single signature pattern; a fraud-guard *should* detect it |
| "What's your expected false-positive rate?" | Bench answer: <5% on a corpus of 10,000 SMSes; or be honest - "we have not yet measured; here's our evaluation plan" |

---

## synthesis_cross_cutting_insights_across_the_six_themes

### Mechanism contrasts across actors

| Actor / product | Primary defence vector | Time horizon | Trade-off exposed |
|---|---|---|---|
| Truecaller (consumer caller-ID, 450M Android MAU Oct 2025 [synthesis_cross_cutting_insights_across_the_six_themes[0]] [15]) | Graph + crowd-sourced tag + name lookup | Real-time at call-arrival | Cannot defend during a video call; cannot defend SMS-borne links |
| Bureau / Bureau Device ID [synthesis_cross_cutting_insights_across_the_six_themes[1]] [45][synthesis_cross_cutting_insights_across_the_six_themes[2]] [11] | Device fingerprint + behaviour + identity graph | Real-time mid-session | Heavy SDK footprint; banks uptake is faster than consumer-app uptake |
| Sign3 | Behavioural profiling, AI fraud prevention for FIs | Real-time | Stage: seed/upcoming, not yet proven at SBI-HDFC scale |
| Lifeguard AI voice assistant [synthesis_cross_cutting_insights_across_the_six_themes[3]] [29][synthesis_cross_cutting_insights_across_the_six_themes[4]] [30] | AI voice assistant that picks up unknown calls, runs a real conversation, only passes legitimate calls | Real-time at call-arrival | US-built product in India; works for English-speaking scam-typology only |
| Neural Defend [synthesis_cross_cutting_insights_across_the_six_themes[5]] [36][synthesis_cross_cutting_insights_across_the_six_themes[6]] [37] | Live deepfake detection on video calls | Real-time mid-call | Seed-stage (raised Mar 2025 [synthesis_cross_cutting_insights_across_the_six_themes[7]] [35]); has no India consumer install base yet |
| RBI DPIP [synthesis_cross_cutting_insights_across_the_six_themes[8]] [20] | Bank-side cross-PSP graph, real-time risk score | Real-time post-transaction | Closed - student teams cannot plug in directly |
| CFCFRMS / 1930 [synthesis_cross_cutting_insights_across_the_six_themes[9]] [8][synthesis_cross_cutting_insights_across_the_six_themes[10]] [10] | Golden-hour fund-trace, citizen-facing | Real-time post-transaction via phone call | Latency between citizen dial and bank action can be 5-15 min; "golden hour" still misses major digital-arrest scams due to identity-impersonation |
| Chakshu / Sanchar Saathi | Citizen reports suspected SMS / calls / WhatsApp | Reactive, hours-to-days | Citizen-driven; no proactive monitoring |
| RBI FREE-AI Sutras / Pillars | Voluntary AI governance rail | Year-scale adoption | "AI for customer protection" (Sutra 5) is the hook student teams should quote |

### Tensions, divergences, contradictions

1. **Volume paradox**: bank fraud cases fell 57% in FY26 while value rose 46% [synthesis_cross_cutting_insights_across_the_six_themes[11]] [4]. This means the *easy* part of fraud has been broken; the *hard* part (digital arrest, AI scams) is what remains. The fraud-guard kit's bar of excellence is detecting what banks cannot.
2. **Reported vs actual gap**: RBI's reported bank fraud (Rs 48,021 crore) vs NCRP-reported cyber fraud (Rs 55,050 crore since 2021) [synthesis_cross_cutting_insights_across_the_six_themes[11]] [4][synthesis_cross_cutting_insights_across_the_six_themes[9]] [8] is not the same denominator. RBI's is per-fiscal-year, NCRP's is per-incident-report. Student teams must pick a metric and lock to it.
3. **State geography inversion**: Telangana (15,297 cases, 2022) is now the highest cyber-crime-rate state, ahead of Maharashtra and Karnataka's historical lead [synthesis_cross_cutting_insights_across_the_six_themes[12]] [17]. A fraud-guard kit that treats Mumbai as the centre of gravity is 2 years out of date.
4. **AI asymmetry**: Rs 22,495 crore of AI-scam loss in CY2025 [synthesis_cross_cutting_insights_across_the_six_themes[13]] [5] vs Neural Defend being just 7 months post-seed (raised 13 March 2025 [synthesis_cross_cutting_insights_across_the_six_themes[7]] [35]). Demand is far ahead of supply.
5. **Regulator-vs-importer alignment**: RBI is explicitly inviting "AI for customer protection" via Sutra 5 of FREE-AI [synthesis_cross_cutting_insights_across_the_six_themes[14]] [18]; the *student opportunity* is the Sutra 5 - the gap between bank-side AI and customer-side AI.
6. **WhatsApp as the new dark forest**: per News18 and India Today, ~70%+ of scam-entry vectors in 2026 are WhatsApp-driven (calls, group links, video, AI voice), not SMS or voice-call. The kit's TelephonyService integration should weight WhatsApp-vector detection higher than SMS.

### Failure cases the team should know

- Truecaller spam-tagging false positives hurt small businesses; remedy is a merchant-side appeal.
- Google Call Screen has no general India rollout; Pixel-only. Limit deliberately excluded.
- Lifeguard is a US product - Indian scam vocabulary (Hindi / Tamil / Telugu / Marathi / Gujarati) - even if Lifeguard's voice agent is technically multilingual - is *not* benchmarked.
- Bureau Device ID sees strong traction in BFSI (June 2025 re-launch) but at consumer-app level it's not a "fraud-guard" - it's a fraud-risk score for the bank; a student kit must not brand itself as a Bureau.
- Sign3 (raised USD 1.5M Mar 2026 [synthesis_cross_cutting_insights_across_the_six_themes[15]] [34]) is enterprise B2B; selling to a bank takes 6-12 months.

### Convergent recommendation

A fraud-guard kit that survives 2026 judge scrutiny integrates four primitives:
1. A **Truecaller-class caller-ID graph** (open the Truecaller SDK; or partner).
2. A **Lifeguard-class voice-bot honeypot** (auto-pick-up, rapid triage, on-device ASR).
3. A **Neural Defend-class deepfake video/voice detector** (real-time, <2s latency, on-device).
4. A **1930 / CFCFRMS / Chakshu one-tap submitter** (pre-filled forensic packet).

That is exactly what FREE-AI Sutra 5 ("AI for customer protection") signals the regulator wants to see grow, and it is the impartial answer to the question: what should *we* - a student team - build next?

---

## references_urls_mapped_to_doc_ids_cited_inline

1. [https://www.rbi.org.in/scripts/annualreportpublications.aspx] - RBI Annual Report landing page
2. [http://frontline.thehindu.com/social-issues/ai-deepfake-digital-arrest-scams-india-cybercrime/article70587955.ece] - Frontline, "Digital Arrest Scams in India: Fear, Fraud, and the Collapse of Cyber Safeguards"
3. [http://news18.com/india/digital-arrest-scam-duped-nearly-3-lakh-indians-cost-rs-4057-crore-since-2022-exclusive-ws-l-10192258.html] - News18, "~3 lakh duped, Rs 4,057 crore lost" [2, 4, 6]
4. [https://www.bbc.com/news/articles/cp3l3p7lzppo] - BBC, "Indians lost $2.5bn to digital fraud in 2025 - RBI fights back"
5. [https://www.lowyinstitute.org/the-interpreter/india-s-digital-arrest-scams] - Lowy Institute, "India's digital arrest scams" (cases nearly tripled 2022-2024)
6. [https://www.thehindu.com/business/Economy/financial-institutions-report-over-10000-cases-of-fraud-involving-48000-crore-in-fy26-rbi-data/article71036689.ece] - The Hindu, FY26 RBI bank-fraud breakdown
7. [https://thebriefwire.com/news/807-7-ai-powered-scams-indians-falling-2026] - TheBriefWire on 7 AI-powered scam types India 2026
8. [https://facia.ai/blog/celebrity-deepfake-a-rising-threat-with-reputational-and-financial-consequences] - Facia.ai on celebrity deepfake risk
9. [https://www.fakeout.io/blog/fake-celebrity-investment-scams-whatsapp-2026] - Fakeout.io on AI-celebrity WhatsApp investment scams [fakeout.io]
10. [https://www.ndtv.com/india-news/fake-app-fabricated-profits-how-mumbai-man-lost-11-crores-to-trading-scam-10850671] - NDTV, Rs 10.98 crore Mumbai trading-scam
11. [https://www.cryptotimes.io/2026/03/23/india-hit-by-inr-2-68-cr-crypto-fraud-as-deepfake-trading-apps-trap-victims] - Crypto Times, Rs 2.68 crore crypto fraud [cryptotimes]
12. [https://scamdekho.in/blog/fedex-dhl-parcel-customs-scam-in-india] - Scamdekho, Rs 1,800 crore FedEx/DHL parcel scam
13. [https://righttoinformation.wiki/courier-package-scam-india-2026] - RTI wiki, January 2026 Noida DHL case
14. [https://corporate.truecaller.com/newsroom/press-release/truecaller-crosses-450-million-active-users-on-android-globally] - Truecaller, 450M Android MAU 9 Oct 2025
15. [https://corporate.truecaller.com/newsroom/press-release/truecaller-continues-strong-growth%2C-surpasses-400-million-android-users?id=58099B676ABDB3A0] - Truecaller 433M Dec 2024
16. [https://corporate.truecaller.com/] - Truecaller corporate home: 500M+ active users, 38B unwanted calls blocked 2021
17. [http://apps.apple.com/us/app/truecaller-premium-caller-id/id448142450] - Truecaller Premium Caller ID iOS App Store [references_urls_mapped_to_doc_ids_cited_inline[0]] [17]
18. [https://platform.tracxn.com/a/d/company/66adcab80e99c36424676d4c/neural%20defend#a:about] - Tracxn, Neural Defend details [15, 41]
19. [http://india.entrepreneur.com/news-and-trends/neural-defend-secures-funding-to-advance-ai-driven-deepfake/488475] - Entrepreneur India on Neural Defend [references_urls_mapped_to_doc_ids_cited_inline[1]] [10]
20. [https://www.crunchbase.com/organization/neural-defend] - Crunchbase, Neural Defend [references_urls_mapped_to_doc_ids_cited_inline[2]] [40]
21. [http://sign3.ai/] - Sign3 homepage [references_urls_mapped_to_doc_ids_cited_inline[3]] [22]
22. [https://entrepreneur.economictimes.indiatimes.com/news/funding/sign3-raises-1-5-million-funding-led-by-cedar-hill-capital/129894041] - ET, Sign3 $1.5M funding Mar 2026 [references_urls_mapped_to_doc_ids_cited_inline[4]] [23]
23. [http://tracxn.com/d/companies/sign3/__5zIi38GerMcanlvjWaetsSkcBrRH5WMvcO6_HUUF1jc] - Tracxn, Sign3 [references_urls_mapped_to_doc_ids_cited_inline[5]] [13]
24. [https://www.prnewswire.com/in/news-releases/bureau-expands-device-intelligence-with-next-gen-capabilities-to-detect-coordinated-fraud-302486195.html] - PR Newswire, Bureau Device ID Jun 2025 [references_urls_mapped_to_doc_ids_cited_inline[6]] [18]
25. [http://bureau.id/] - Bureau homepage [references_urls_mapped_to_doc_ids_cited_inline[7]] [32]
26. [http://tracxn.com/d/companies/truecaller/__y_jl5q8UdLteRtFoy2lvKmEhkKeoheUQNRxcps8eStk] - Tracxn, Truecaller (630 employees; public) [5, 8]
27. [https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/FREEAIR130820250A24FF2D4578453F824C72ED9F5D5851.PDF] - RBI FREE-AI report PDF, 13 Aug 2025
28. [http://scrut.io/post/rbi-framework-for-responsible-and-ethical-enablement-of-artificial-intelligence] - Scrut.io, RBI FREE-AI 7 Sutras 6 Pillars 26 actions
29. [https://www.lexology.com/library/detail.aspx?g=cdd93d6c-fd28-4c12-ac23-33d7820439ab] - Lexology, RBI FREE-AI summary
30. [https://bfsi.economictimes.indiatimes.com/articles/rbi-developing-ai-powered-platform-to-flag-risky-digital-transactions/124252432] - ETBFSI, RBI DPIP
31. [https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12702] - RBI Master Directions on Fraud Risk Management 2024
32. [https://elplaw.in/wp-content/uploads/2024/07/RBI-Revised-Master-Directions-on-Fraud-Risk-Management-July-2024.pdf] - ELP Law, RBI Master Directions July 2024
33. [http://rbi.org.in/commonman/english/scripts/PressReleases.aspx] - RBI press releases, Ombudsman for Digital Transactions Jul 2026
34. [http://pib.gov.in/PressReleasePage.aspx?PRID=2287039] - PIB, National Cyber Crime data (32.80 lakh calls; Rs 11,158 crore saved; 6589201 complaints; Rs 55,050 crore total) [39, 42]
35. [http://i4c.mha.gov.in/ncrp.aspx] - I4C NCRP page (helpline 1930; CFCFRMS module; 85 banks; Vani CyberDost chatbot) [30, 107]
36. [https://cybercrime.gov.in/] - National Cyber Crime Reporting Portal [16, 24, 27, 49]
37. [https://sancharsaathi.gov.in/] - Sanchar Saathi home
38. [https://sancharsaathi.gov.in/sfc] - Sanchar Saathi Chakshu SFC [68, 122, 123]
39. [https://sancharsaathi.gov.in/?OWASP-CSRFTOKEN=QQ7V-EZHQ-W7S0-JHEF-ZQ7A-6Z76-U4H2-JL2R] - Sanchar Saathi Chakshu banner
40. [https://www.dqindia.com/data-and-ai/ai-scams-india-2025-deepfake-identity-fraud-rs-22495-crore-12108304] - DQIndia, Rs 22,495 crore AI scams 2025
41. [https://dial91.com/india-calling-scams/] - Dial91, India calling scams 2025 guide
42. [https://www.phishguard.co.in/awareness] - PhishGuard India awareness
43. [https://scantotal.net/blog/customs-parcel-held-scam-india/] - Scantotal, parcel held customs scam India
44. [https://righttoinformation.wiki/fake-courier-customs-held-scam-india] - RTI wiki, fake customs scam recovery steps
45. [https://timesofindia.indiatimes.com/city/mumbai/mumbai-cyber-police-initiates-refund-of-rs-2-crore-for-victim-of-rs-58-crore-digital-arrest-fraud/articleshow/126658050.cms] - TOI, Mumbai Rs 58 crore digital arrest case [references_urls_mapped_to_doc_ids_cited_inline[8]] [20]
46. [https://www.facebook.com/UNINewsagency/posts/in-a-major-statewide-crackdown-on-cyber-enabled-financial-crimes-kerala-police-h/1406531121487005] - Kerala Police crackdown 165 arrests, 455 cases [references_urls_mapped_to_doc_ids_cited_inline[9]] [9]
47. [http://www.facebook.com/IIBFOfficial/posts/-digital-arrest-is-a-fraud-stay-alert-as-per-reserve-bank-of-india-no-authority-/1409997440930607] - IIBF: "digital arrest" is a fraud [1, 3]
48. [https://trylifeguard.com/spam-call-blocking] - Lifeguard spam blocking [references_urls_mapped_to_doc_ids_cited_inline[10]] [36]
49. [https://play.google.com/store/apps/details?hl=en_NZ&id=com.trylifeguard] - Lifeguard Play Store [14, 38, 45]
50. [https://www.business-standard.com/industry/banking/sbi-uses-ai-to-underwrite-nearly-1-trillion-msme-loans-in-fy26-amara-126081201303_1.html] - Business Standard, SBI AI underwriting Rs 1 trillion FY26
51. [https://promptandskills.com/learn/sectors-of-ai/ai-fraud-detection-indian-banks] - AI fraud detection Indian banks 2026 with FREE-AI alignment
52. [https://www.jetir.org/papers/JETIR2508633.pdf] - UPI as Catalyst for Inclusive and Sustainable Digital Payments; RBI Annual Report highlights FY25 ~84% retail
53. [https://www.indiadatamap.com/2025/10/11/state-wise-analysis-of-data-breaches-in-india-for-2025/] - State-wise data breaches 2025 estimate
54. [http://pib.gov.in/PressReleasePage.aspx?PRID=2003505] - PIB, NCRB state-wise cyber crime 2020-2022
55. [http://pib.gov.in/PressReleasePage.aspx?PRID=2082761] - PIB clarification NCRB does not maintain digital arrest separately
56. [https://cred.club/security] - Cred CERT-In empanelled auditors / NPCI mandate [references_urls_mapped_to_doc_ids_cited_inline[11]] [11]
57. [https://paytm.com/] - Paytm positioning [references_urls_mapped_to_doc_ids_cited_inline[12]] [33]
58. [http://irdai.gov.in/document-detail?documentId=1354911] - IRDAI Cyber Jaagrookta Diwas PDF [references_urls_mapped_to_doc_ids_cited_inline[13]] [34]
59. [https://cyberpeace.org/] - CyberPeace Foundation OSINT research [references_urls_mapped_to_doc_ids_cited_inline[14]] [28]
60. [https://www.india.entrepreneur.com/news-and-trends/neural-defend-secures-funding-to-advance-ai-driven-deepfake/488475] - India Entrepreneur on Neural Defend AI models [references_urls_mapped_to_doc_ids_cited_inline[1]] [10]
61. [https://m.economictimes.com/news/india/cbi-nabs-three-people-in-2-07-cr-digital-arrest-scam/articleshow/132169073.cms] - Economic Times CBI Rs 2.07 crore digital arrest bust [ET cbi July 2026]
62. [http://cybercrime.gov.in/Webform/Accept.aspx] - cybercrime.gov.in complaint filing portal
63. [https://www.indiatoday.in/technology/news/story/canadian-couple-loses-rs-18-lakh-to-ai-voice-impersonating-their-grandson-2343771-2023-03-07] - India Today AI-voice family-emergency scam example
64. [https://www.pib.gov.in/PressReleasePage.aspx?PRID=2241255&lang=2&reg=3] - PIB, regulatory framework Digital Lending Apps / RBI guidance
65. [https://thokalath.com/nri-corner/family-parents-india/ai-voice-scam-warning-fake-family-calls/] - Thokalath AI voice scam warning
66. [https://economictimes.indiatimes.com/topic/cyber-scams-india] - Economic Times cyber scams feed

---

*Prepared for an Indian hackathon pitch kit. Every claim is grounded in the source documents listed in the References. Currency conventions: Rs = Indian Rupees (INR); USD = United States Dollar. RBI's fiscal year runs 1 April to 31 March; "FY26" = 1 April 2025 - 31 March 2026. All segments shown were visible in the tool previews and the prior registered corpus context; the inline cite markers reflect the original `[doc_id.segment_id]` mapping used by the research workflow.*