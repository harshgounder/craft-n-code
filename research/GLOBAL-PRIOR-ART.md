# GLOBAL-PRIOR-ART.md — What Exists in the World, and Our Honest Slot

Date: 2026-08-16. Six-wave global sweep (d25-d30, all DEEP/MINED, 226+182+127
cites in the top three). India was already covered in earlier waves; this is
the worldwide map.

## 1. THE HEADLINE: no complete duplicate exists anywhere

Six independent sweeps (agri-advisory, GitHub/forums/hackathons, money rail,
delivery channels, LLM+agriculture, farm data platforms) all converge on the
same conclusion: NO deployed system anywhere closes the full loop:
authoritative hazard ingest + farm-level profile + crop-stage actions +
pre AND post disaster phases + Odia SMS/IVR + intermittent connectivity +
offline execution. Every component exists somewhere. The integration with
the recovery state machine does not.

## 2. THE CLOSEST ANALOGUES (must-know for judges)

| System | Where | Scale | What it proves | What it lacks |
|---|---|---|---|---|
| Ama Krushi / Krushi Samruddhi Helpline | ODISHA ITSELF | 7.9M farmers, 30 districts; 10% severe-loss reduction, 21% under inadequate rainfall | Profile-based weekly voice calls + IVR + live agronomists at state scale | Weekly cadence, no real-time cyclone/flood incident engine, no post-event recovery workflow |
| BaKhabar Kissan | Pakistan | 15.8M+ users, 300+ weather stations | Profiles + disaster alerts + IVR/SMS/VMS + satellite + experts, all in one | No documented post-event agronomic workflow, no measured loss reduction |
| BAMIS | Bangladesh | 487 upazilas planned | Concrete disaster crop actions: harvest before rain, drain, repair bunds, brace bananas | No individual profiles, unclear continuity, no recovery stages |
| Ethiopia 8028 Hotline | Ethiopia | 6M+ subscribers, 60M calls | IVR for low-literacy at national scale, push + pull + surveys on ONE profile | No disaster recovery, no crop-stage hazard matrix |
| Jeonnam Farm EWS | South Korea | 30 crops, up to 11 hazards | THE rule-matrix precedent: registered farm + crop + variety -> 3-day risk texts + response guidance, 4.15/5 satisfaction | Smartphone/mobile-web dependent, no SMS/IVR disaster loop |
| PxD AI weather SMS | India | 38M farmers, 13 states (2025) | Message comprehension engineering at national scale | One-way weekly guidance, no event urgency |
| Farmer.Chat (Digital Green) | India + Africa | 830K+ users, 5M+ queries | RAG over vetted agronomy, multilingual voice/text/photo; 71% context precision, 18% low-relevance tail | General advisory, not disaster-specific; safety tails documented |
| WFP Anticipatory Action | Bangladesh + global | USD 53 to ~145,000 people up to 4 days pre-flood (July 2020) | Forecast triggers release cash BEFORE impact | Household cash, not crop actions; no agronomy |
| R4 Rural Resilience | 18 countries | 550K households, $2.1M payouts | Insurance + savings + credit + risk reduction bundle | Coarse resolution, basis risk |
| PlantVillage Nuru | Africa/Asia | Deployed offline app | Offline disease diagnosis on 2GB RAM phones, 74-88% accuracy | Visual diagnosis only, no weather trigger, no recovery |
| AgroMetLLM | India (research) | Pi 4B + quantized Qwen | Edge LLM generating irrigation advice in 1-2s | Research only, no Odia, no SMS/IVR, no hazards |
| Krushak Odisha | Odisha | 9,196,615 registered farmers | The identity/farm-data asset already exists | Data portal, not an advisory engine |

## 3. THE COLLISION (say this before anyone else does)

github.com/dontcuttrees/krishirakshak, created 2026-08-15 (yesterday), 0 stars,
17 commits: a near-verbatim implementation of THIS exact problem statement
(hyperlocal AI, Odia/Hindi SMS + IVR). Another team's build attempt. It proves
the idea is not unique, and it must never be called unique in the pitch.
Differentiation is verification, not the feature list.

## 4. THE DEATHS (funding reality)

- Gro Intelligence: ~$117M raised, closed 2024 (capital intensity, no last mile)
- aWhere: deadpooled ($16.6M raised)
- WeFarm: SMS peer Q&A reached 2.5M farmers, closed 2022 (unit economics)
- Lesson: B2G/public-extension funding path + cost-per-active-farmer target
  are product requirements, not slides.

## 5. THE MONEY RAIL (d27): orchestrate, don't reinvent

- WFP anticipatory action: pre-agreed forecast thresholds release finance +
  messages BEFORE impact. The trigger discipline is prior art.
- R4: insurance works as a bundle (risk reduction + insurance + savings +
  credit). Advisories do NOT yet demonstrably lower premiums: do not claim it.
- ARC/Africa RiskView: parametric speed trades claim inspection for basis
  risk. Coarse administrative resolution, not farm-level.
- ACRE Africa (Zambia): 587,842 messages sent, 361,539 delivered, 217,134
  FAILED = 56% success. Delivery failure is a product requirement, not an
  edge case.
- PMFBY: the right rail to INTEGRATE, not reinvent. Already requires
  farm-level loss info for localized losses, has the 72h intimation window.
- Satellite/photo claims tools (Sen4CAP, EOSDA, Agremo) assist adjudication,
  do not eliminate it. EOSDA case: 2 of 3 claims validated, one rejected:
  uncertainty is part of the workflow.

## 6. DELIVERY (d28): redundancy beats a single channel

- Multi-channel villages (SMS + voice + meetings + extension staff + clubs +
  public announcements) had higher awareness AND use.
- Radio: Farm Radio International, 24.1M listeners: the true basic-phone
  broadcast rail, already used by Ama Krushi's community-radio network.
- Feature phones are a proven financial channel (M-PESA, DigiFarm), so the
  SMS/USSD path has payment-grade precedent.
- Offline-first tools (Nuru, ODK, CommCare) prove local inference +
  store-and-forward; they are not basic-phone-first, which is our lane.

## 7. THE DATA LAYER (d30): free global assets, assembled

- SoilGrids: 250m global soil properties, CC BY 4.0, WCS/WMS/WebDAV
- ESA WorldCover: 10m global land cover, 76.7% accuracy (a prior, not truth)
- GDACS + GloFAS: free cyclone/flood event APIs + Sentinel-1 observed flood
  mapping (GloFAS = observed, not forecast)
- NASA POWER, ERA5-Land, CHIRPS: free weather/rainfall
- Sen1Floods11 (233 stars) + CropHarvest (230 stars): flood/crop datasets
- Krushak Odisha (9.2M farmers) + e-Chasa: the identity layer already exists
- Blockchain (AgriDigital, GrainChain): not the missing ingredient

## 8. THE HONEST DIFFERENTIATION (what we can claim)

NOT: "first AI farm adviser", "first voice advisory", "first hyperlocal
weather", "first offline agri AI", "first disaster alert". All taken.

CLAIM (verified by the sweep): a consented Odisha farm-and-crop profile
joined to an authoritative IMD/CWC hazard feed, a crop-stage action
compiler with deadlines and cost-of-waiting, a two-phase pre/post event
state machine with recovery + claims, delivered via SMS/IVR with offline
continuity, and validated against REAL replayed events (Fani/Yaas/Dana)
with measured comprehension and action, not message volume.

The recovery state machine is the slot no analogue occupies. BaKhabar Kissan
stops before recovery; BAMIS before personalization; WFP before agronomy;
USDA/FAO before low-tech delivery. The closed loop is the product.

## 9. PARTNER MAP (from the sweep, for Round 1+)

- Ama Krushi/Krushi Samruddhi: integrate with the existing registry + IVR
  shortcode + community radio instead of building a parallel enrollment silo
- Krushak Odisha: the 9.2M-farmer identity bridge
- Odisha Crop Contingency Plan 2025: the approved rule corpus
- KCC 22-language escalation, mKisan rails
- Farmer.Chat's RAG architecture + evaluation discipline (71% precision)
- WFP trigger discipline for the anticipatory layer
- PMFBY 0.5% awareness earmark as the funding rail
