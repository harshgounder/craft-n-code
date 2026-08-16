# Under Rs 3,000: A Credible Cyclone-Flood Sensor Node

## 1. EXECUTIVE SUMMARY

- **Prototype is feasible, but it is not a cyclone detector.** A target bill of materials (BOM) of **Rs 2,899** can combine ESP32, pressure, humidity, soil-moisture, rain, water-level, wind, solar power, and an enclosure. Some lines are engineering allowances rather than live quotations, so this is a design target, not a purchase order. The correct claim is "IMD-gated hyperlocal risk sensing," not autonomous cyclone prediction. [5]
- **Pressure tendency is the strongest cheap local cyclone-related signal.** A BMP280 costs **Rs 85 including GST** on the cited Indian listing, while Bosch specifies typical relative pressure accuracy of **+/-0.12 hPa** under restricted conditions, typical absolute accuracy of **+/-1 hPa**, and long-term stability of **+/-1 hPa over 12 months**. Rate-of-change partly cancels a stable sensor offset, but pressure decline is not cyclone-specific. [5][9]
- **Do not publish a universal Bay of Bengal hPa/hour trigger.** IMD's Fani report documents formation on April 25-26, an estimated central pressure of **932 hPa** on May 2, and Odisha landfall on May 3, but it does not provide a colocated farm-station pressure trace from which a defensible local drop-rate threshold or lead time can be derived. [12]
- **Official warning supplies the long lead; the node supplies local confirmation.** For Fani, IMD issued the pre-cyclone watch **90 hours**, cyclone alert **66 hours**, and cyclone warning **36 hours** before landfall. IMD's current protocol describes a first-stage watch at least 72 hours ahead and a second-stage alert at least 48 hours ahead. [12][26]
- **Water and rain sensors matter more than UV or illuminance.** A calibrated tipping bucket yields rain rate and accumulation; a float or waterproof ultrasonic sensor yields inundation state and rise rate; and soil moisture indicates drainage stress. By contrast, UV and BH1750 light measurements do not directly change a cyclone/flood action in this problem and should be omitted unless another agronomy use case pays for them. [27]
- **ESP32 is the practical controller.** It supports a phone-facing Bluetooth path and low-cost Wi-Fi-class development; the cited India comparison lists an ESP32-C3 board at **Rs 232** and ESP32 NodeMCU Wi-Fi/Bluetooth boards around **Rs 370-385**. Raspberry Pi Zero 2 W needs a 5 V, 2.5 A supply and has no native analog input, while an Arduino Nano lacks native Wi-Fi/Bluetooth. [23] [34][35]
- **The Odisha field evidence warns against lab-only confidence.** In a Pipli tomato pilot, ridge-top moisture-sensor placement produced persistent dry alarms even after irrigation; moving sensors to the ridge bottom restored credible operation. Pest, wilt, and fruit-borer losses above 50% also made treatment results inconclusive, showing that sensing quality does not guarantee crop outcomes. [29]
- **Decision: GO for a tightly scoped prototype; GATED for a farm pilot.** Demo IMD replay, pressure/rain/water anomaly fusion, BLE phone synchronization, and Odia SMS/IVR generation. Do not pilot until sensors are colocated with references, enclosures survive monsoon exposure, communications and power are measured, and agronomists approve all action rules.

## 2. DATA INVENTORY

**Reliability grades:** A = primary manufacturer, IMD, or strong peer-reviewed measurement source; B = official field program or vendor page with directly testable facts; C = retailer/aggregator or incompletely validated implementation source; D = estimate, DIY allowance, or unsupported performance claim.

| Item | Named source (URL + date) | Spec/price | Feasibility for India | Grade |
|---|---|---|---|---|
| BMP280 pressure and temperature | Bosch BMP280 datasheet, https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp280/ (datasheet accessed 2026-08-16); Robu, https://robu.in/product/bmp280-barometric-pressure-and-altitude-sensor-i2c-spi-module/ (accessed 2026-08-16) | Pressure: typical +/-1 hPa absolute and +/-0.12 hPa relative in restricted ranges; stability +/-1 hPa/12 months; sleep about 0.1 uA typical. Robu price: **Rs 85 incl. GST**. [9][5] | **Best value core sensor.** Shield from direct rain and solar heating through a vented, hydrophobic pressure port. Use tendency after baseline calibration, not absolute sea-level pressure alone. | A specs / C price |
| BME280 pressure, humidity, temperature | Bosch BME280 datasheet, https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/ (accessed 2026-08-16) | Typical **+/-3% RH**, **+/-0.5 C**, and **+/-1 hPa**; humidity drift about 0.5% RH/year and pressure stability +/-1 hPa/year; combined low-power use about 3.6 uA at 1 Hz in the stated mode. [14] | Prefer when one calibrated digital package must replace BMP280 plus a budget humidity sensor. A currently displayed Indian price was not recovered, so procurement comparison remains open. | A |
| DHT22 humidity and temperature | Indian prototype BOM, source page accessed 2026-08-16 | The India BOM lists **Rs 120**. A trustworthy primary datasheet was not successfully recovered in this run, so no stronger accuracy claim is used here. [24] | Cheap demo option, but lower confidence than Sensirion/Bosch. Keep outside the sealed enclosure behind a proper radiation/rain shield. | C |
| SHT31 humidity and temperature | Sensirion SHT3x-DIS datasheet, https://sensirion.com/products/catalog/SHT31-DIS (datasheet accessed 2026-08-16) | SHT31 typical accuracy **+/-2% RH** and **+/-0.2 C**; typical long-term drift below 0.25% RH/year and below 0.03 C/year; humidity response about 8 s at 25 C and 1 m/s airflow. [7] | Better reference-grade choice than DHT22, but likely too expensive for every sub-Rs 3,000 node unless humidity materially improves advisories. | A |
| DIY cup anemometer | No qualifying India field-validation source found; engineering design dated 2026-08-16 | Target allowance **Rs 300** for cups, bearing, magnet, Hall/reed switch, and mast. Count pulses, derive speed from a fitted transfer curve, and retain short-window maxima. | Can demonstrate gust detection, but has unknown starting threshold, overspeed behavior, bearing wear, and wind-direction bias until calibrated against a reference. Do not equate its raw reading with IMD's official sustained-wind category. | D |
| Low-cost ultrasonic wind | Search of Indian retail and deployment literature, completed 2026-08-16 | No credible weatherproof unit below the node budget was found. | Reject for this cost cap. A hobby ultrasonic build is not a validated cyclone instrument. | D |
| DIY tipping-bucket rain gauge | Peer-reviewed tipping-bucket review, accessed 2026-08-16 | Calibrate statically by leveling the gauge and adjusting a known per-tip volume; calibrate dynamically at multiple flow rates because undercount grows with intensity. Wind undercatch, clogging, and loss of level are major errors. [27] | Feasible at a **Rs 250 parts allowance**. Use a debris screen, drain test, bubble level, and service log. Compute depth per tip from funnel area and measured bucket volume; do not copy an arbitrary mm/tip constant. | A method / D hardware |
| Commercial tipping bucket | IndiaMART result accessed 2026-08-16 | Search result displayed about **Rs 14,000/piece**, far above the total budget. | Exclude from the prototype BOM; use only as a temporary calibration reference if a lab can lend one. | C |
| Capacitive soil-moisture probe | Robu, https://robu.in/product/capacitive-soil-moisture-sensor-module/ (accessed 2026-08-16); India BOM accessed 2026-08-16 | Robu displayed **Rs 49 incl. GST but out of stock**, 3.3-5.5 V input, roughly 5 mA, and 0-3 V analog output. Another India BOM lists Rs 90. [4][24] | Use only after soil-specific wet/dry or volumetric calibration. Seal cable and PCB. ESP32 ADC calibration/filtering is mandatory. | C |
| Water level: float switch | No sufficiently documented current Indian listing found, search completed 2026-08-16 | Binary high-water switch; price remains a procurement gap. | Often more robust than ultrasonic for a single evacuation threshold. Install in a stilling tube with debris protection and manual test access. | D |
| Water level: waterproof ultrasonic | Robocraze waterproof ultrasonic listing, accessed 2026-08-16 | Displayed price **Rs 249**. [19] | Useful for rise rate and multiple thresholds, but blind zone, condensation, foam, angled water, wind, insects, and mounting movement require field tests. Pair with a float switch for fail-safe thresholding. | C |
| UV: VEML6075/ML8511 | Search completed 2026-08-16 | No stable current India quote and no demonstrated cyclone/flood decision value found. | **Omit.** UV does not justify power, enclosure aperture, code, or calibration in this warning node. | D |
| Light: BH1750 | India BOM accessed 2026-08-16 | Listed at **Rs 80**. [24] | Omit from storm-warning BOM; add only if a separate crop-light model is explicitly tested. | C |
| ESP32 / ESP32-C3 | India price-comparison page accessed 2026-08-16; Espressif ADC guidance accessed 2026-08-16 | ESP32-C3 **Rs 232**; ESP32 NodeMCU Wi-Fi/Bluetooth **Rs 370-385** in the cited comparison. ESP32 ADC reference voltage can vary by chip and analog readings need calibration, filtering, and local decoupling. [23] [20] | **Recommended.** BLE pairs to a farmer smartphone without a router; Wi-Fi is available at gateways; deep sleep supports solar/battery use. Prefer a board whose sleep current is measured after removing power LEDs and inefficient regulators. | A architecture / C prices |
| ESP8266 | Manufacturer/product literature search completed 2026-08-16 | Lower-cost Wi-Fi option, but no native BLE and limited analog capability relative to this sensor set; no trustworthy current price captured. | Poorer fit because phone pairing is a core requirement. Use only with an external BLE/ADC, which erodes its price advantage. | C |
| Arduino Nano | Arduino official documentation, https://docs.arduino.cc/hardware/nano (accessed 2026-08-16) | ATmega328 at 16 MHz with eight analog pins; no native Wi-Fi or Bluetooth. [35] | Electrically simple, but needs an extra phone/mesh radio. ESP32 is cheaper at system level. | A |
| Raspberry Pi Zero 2 W | Raspberry Pi official product brief, https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/ (accessed 2026-08-16) | 1 GHz quad-core 64-bit CPU, 512 MB RAM, 2.4 GHz Wi-Fi, Bluetooth 4.2/BLE, specified 5 V/2.5 A supply, and no native ADC. [34] | Overpowered and power-hungry for a sensor node. Reserve Linux-class hardware for a powered village gateway, not each field. | A |
| LoRa SX1276 option | Semtech SX1276 page, accessed 2026-08-16; E32-868T30D India listing, accessed 2026-08-16 | SX1276 family covers 137-1020 MHz; cited Indian E32 listing displayed **Rs 1,924.96**, consuming most of the node budget. [6] [21] | LoRa is a PHY, not a mesh by itself. Use a cheaper locally compliant module only after link-budget, antenna, duty-cycle, and WPC/regulatory review. Put LoRa on selected relay nodes, not automatically on every sensor. | A chip / C module price |
| GSM/SIM800-class uplink | Indian-vendor search completed 2026-08-16 | No defensible current Indian quote was recovered; many hits were foreign or stale. | Exclude per-node GSM. Use the phone's cellular connection or one maintained village gateway; confirm local 2G service before selecting SIM800-class hardware. | D |
| Solar, battery, charge electronics | Saurally 3 W/6 V India listing accessed 2026-08-16; rural-node design article dated April 1, 2026 | 3 W/6 V panel displayed **Rs 420**; 1/2 W 6 V panels were estimated at Rs 100-300, 18650 at 2.2-3.0 Ah, and IP65 box at Rs 100-300. [22] [10] | Size from measured duty-cycle energy, then derate for monsoon cloud, dirt, battery aging, conversion loss, and shade. Use protected cells, charge/load sharing suitable for solar, fuse, reverse-polarity protection, and low-voltage cutoff. | C |
| Enclosure and field mounting | Rural-node design article dated April 1, 2026; Odisha Pipli deployment 2022-23 | IP65 box planning range **Rs 100-300**; conformal coating recommended. Pipli evidence shows that correct sensor placement can matter more than electronics. [10][29] | Use a gasketed UV-resistant box, downward cable glands, drip loops, breathable pressure vent, external radiation shield, corrosion-resistant mast, and serviceable rain/soil probes. Validate ingress rather than trusting an advertised IP label. | B-C |
| Odisha/India farm deployment evidence | SIMO tomato pilot, Pipli, Odisha, 2022-23; OUAT agrometeorology program pages accessed 2026-08-16 | Pipli used 18 soil sensors at 16/31 cm and eight loggers, with 45/55/65% indications. It reported four versus two-three irrigations and yields of 35.20 versus 33.53 t/ha, but severe pest/disease loss made conclusions weak. OUAT describes 10 agrometeorological units and Tuesday/Friday advisories. [29][25] | Strong evidence for placement, maintenance, and confounding risks; weak evidence for cyclone precursor accuracy, cost, connectivity survival, or warning outcomes. | B |

### Target prototype BOM

| Line | Target Rs | Evidence status |
|---|---:|---|
| ESP32 NodeMCU with BLE/Wi-Fi | 385 | Current comparison-page anchor [23] |
| BMP280 | 85 | Current Robu anchor [5] |
| DHT22 | 120 | India BOM anchor [24] |
| Capacitive soil probe | 90 | India BOM anchor; Robu's Rs 49 unit was out of stock [4] |
| Waterproof ultrasonic level sensor | 249 | Current retailer anchor [19] |
| DIY tipping bucket parts | 250 | Engineering allowance, not quotation |
| DIY cup anemometer parts | 300 | Engineering allowance, not quotation |
| 3 W/6 V solar panel | 420 | Current listing anchor [22] |
| Protected 18650 cell and holder | 300 | Engineering allowance |
| Solar charger, regulator, protection | 150 | Engineering allowance |
| IP65 enclosure | 300 | Top of cited planning range [10] |
| Glands, PCB, connectors, cable, mast allowance | 250 | Engineering allowance |
| **Total** | **2,899** | **Excludes LoRa, GSM, freight, taxes not already included, tools, labor, calibration reference instruments, phone, server, and SMS/IVR charges** |

The arithmetic clears the cap by only Rs 101, and **Rs 1,550 of the total is allowance-based rather than a live vendor quote**. A procurement-ready version therefore remains gated. The simplest cost-risk reduction is to omit DHT22 and DIY wind from the first storm demo, because BMP280 already supplies temperature and wind is the hardest DIY channel to calibrate.

## 3. COVERAGE TABLE

| Source family | Useful hits | Noise or missing evidence | Coverage judgment |
|---|---|---|---|
| Manufacturer datasheets: Bosch, Sensirion, Espressif, Semtech, Raspberry Pi, Arduino | Pressure/RH/temperature accuracy, drift, power modes, CPU/radio and ADC constraints | Datasheets describe components, not Odisha exposure, enclosure condensation, local calibration, or full board sleep current | **A for component limits; C for system reliability** |
| IMD cyclone reports and warning protocol | Fani chronology, central pressure, wind/rain observations, official watch/alert/warning lead times | No public colocated farm-node pressure time series, no universal local hPa/hour trigger, and no sensor-node false-alarm statistics | **A for hazard truth; D for node threshold** |
| IMD warning/API pages | District/subdivision warning endpoints, dissemination channels, attribution and IP-whitelist requirements | The reviewed page did not fully specify payload schema, versioning, latency, update frequency, quotas, or offline licensing behavior [3] | **B** |
| Peer-reviewed rain-gauge literature | Static/dynamic calibration, intensity undercatch, wind, clogging, level and maintenance mechanisms | Does not price or validate this exact DIY gauge in Odisha cyclone rain | **A for method; C for build** |
| Odisha field deployments: SIMO and OUAT | Real placement failure, sensor counts/depths, advisory cadence, crop confounders | Hardware BOM, battery life, packet loss, maintenance cost, enclosure failures, and cyclone outcomes were not disclosed [29][25] | **B for operational lessons; D for total cost** |
| Indian specialist retailers: Robu, Robocraze, Engineer Store | Concrete, locally purchasable price anchors and stock status | Prices/stock change; clones may differ; pages rarely publish calibration certificates, failure rates, or environmental qualification | **C** |
| Marketplace/aggregator price pages | Broad price comparison and hard-to-find modules | Seller identity, tax, shipping, authenticity, warranty, and date stability can be unclear | **C-D** |
| DIY blogs and generic project BOMs | Parts ideas and planning ranges | Frequently omit calibration, uncertainty, ingress tests, power measurements, and failures | **D for performance; C for rough planning** |

The evidence is strong enough to select components and design a demo, but not to promise warning sensitivity, false-alarm rate, cyclone lead time, or pilot total cost. Those four claims require new measurements rather than more catalog searching.

## 4. WHAT IS MISSING

1. **A local Bay of Bengal pressure signature.** No reviewed public source provides a timestamped, quality-controlled surface-pressure trace at farm-node height in Odisha, paired with cyclone distance/intensity, that establishes a reproducible hPa/hour threshold and lead time. Fani's **932 hPa** is estimated storm-center pressure, not what a BMP280 at a village would read. [12]

2. **Discrimination statistics.** There is no public sensitivity, specificity, precision, false-alarm rate, or missed-event rate for distinguishing cyclone approach from ordinary monsoon lows, thunderstorms, diurnal tides, elevation offsets, and sensor drift using this cheap stack. Therefore, a pressure alarm must be conditional on IMD context and cross-node agreement.

3. **Odisha cyclone-season hardware failure data.** Publicly reviewed deployment material does not quantify water ingress, corrosion, cable damage, lightning/surge loss, solar starvation, battery replacement, insect blockage, sensor drift, theft, vandalism, or repair time. The Pipli paper exposes a placement failure and crop confounding, but not a cyclone-resilient node's mean time between failures. [29]

4. **A procurement-grade BOM.** Live quotations were not recovered for a float switch, protected battery, solar charge/load-share board, low-quiescent regulator, cable glands, mast, lightning protection, SIM/data plan, and SMS/IVR. Freight and fluctuating stock can erase the Rs 101 margin.

5. **Validated DIY wind and rain transfer functions.** The rain calibration method is well supported, but the proposed bucket geometry has not been built and dynamically tested. No acceptable wind-tunnel or side-by-side calibration curve was found for the proposed cup rotor. Wind should remain an experimental feature, not a pilot alarm input.

6. **Communications evidence.** No village-specific BLE range, LoRa packet-delivery ratio, cellular availability, outage duration, or energy-per-message data was found. IMD's API page indicates an IP-whitelist process, but the end-to-end behavior during network failure remains unspecified. [3]

7. **Action-to-outcome evidence.** Sources do not quantify how many kilograms or rupees of Odisha crop loss are avoided by each proposed alert. Agronomic advice must be crop-, stage-, soil-, salinity-, and district-specific, with human approval.

8. **Safe continuous-learning governance.** No public source validates unattended phone-level fine-tuning for disaster warnings. Required but missing artifacts include labeled event datasets, rollback criteria, signed model/rule packages, drift limits, audit logs, consent/retention rules, and independent agronomic review.

## 5. HOW IT FEEDS THE EDGE-AI ENGINE

| Signal or function | Tier | Derived feature | Decision powered |
|---|---|---|---|
| BMP280/BME280 pressure | Sensor node | Median-filtered pressure; 1/3/6-hour delta; robust slope; residual against time-of-day baseline; cross-node spread | Under an IMD watch, identify unusual local deepening and increase sampling/message urgency. Never declare a cyclone from pressure alone. |
| Temperature/RH | Sensor node | Dew-point/condensation risk, heat exposure, sensor-health plausibility | Protect stored inputs and harvested produce; flag enclosure condensation; refine post-event disease-risk prompts only with agronomic rules. |
| Rain tips | Sensor node | 5/15/60-minute intensity; 3/6/24-hour accumulation; inter-tip time; stuck/blocked diagnostic | Clear drains, move pumps/inputs/livestock, avoid field entry, and trigger flood watch when paired with rising water. |
| Water level/float | Sensor node | Threshold state, level derivative, time above threshold, ultrasonic/float disagreement | Escalate inundation action, choose safe route or asset elevation, and suppress unsafe post-event return until water recedes. |
| Soil moisture | Sensor node | Calibrated saturation percentile, rate of wetting/drying, stuck-value diagnostic | Stop irrigation before impact; after impact, delay machinery/field entry and tailor drainage/replant assessment. |
| Cup anemometer | Sensor node | Pulse rate, short-window maximum, rotor-stuck diagnostic | Demonstration-only local gust evidence until calibrated; it must not override IMD warnings. |
| Battery/solar/communications | Sensor node | Voltage trend, reset count, message backlog, packet-loss estimate | Distinguish "safe" from "sensor offline" and schedule maintenance before storms. |
| IMD district warning plus farm profile | Phone hub | Hazard stage, time to expected impact, crop/stage, language, assets and contact preferences | Select a pre-approved action template and its urgency. Current IMD sources distribute via website, email, SMS and social channels, while API use requires attribution and an IP-whitelist process. [3] |
| Small quantized language model | Phone hub | Retrieval-grounded Odia wording, SMS compression, IVR script, clarification dialogue | **Express**, translate, and personalize approved facts. It must not invent weather thresholds, pesticide doses, evacuation routes, or recovery instructions. |
| Event labels and fleet telemetry | Learning server | Per-sensor calibration, seasonal baseline, anomaly-model evaluation, drift/failure clustering | Improve future models only after replay tests against IMD truth and agronomist labels; sign and version every release. |

The causal chain should be **observation -> robust feature -> IMD/farm-context gate -> approved action -> delivery -> acknowledgment**. On-node code performs deterministic acquisition and health checks; the phone performs offline fusion and language generation; the server trains and validates. This partition prevents a small LLM from becoming the safety-critical detector.

A safe continuous-learning loop is deliberately asymmetric. The server may fine-tune or recalibrate on reviewed labels and push signed model/rule bundles. The phone may adapt language, farm-profile retrieval, and alert timing preferences locally, but it should not rewrite hazard thresholds from a few unlabeled experiences. Non-smartphone farmers receive SMS/IVR from the server or village gateway; the farmer phone is an optional offline hub, not the only delivery route.

## 6. REAL-vs-FILLER

| Classification | Item | Evidence-based reason |
|---|---|---|
| **Genuinely usable** | BMP280 pressure tendency | Very low cost, digital interface, low power, characterized relative accuracy, and tendency reduces dependence on absolute offset. It adds local context under an IMD alert. [9][5] |
| **Genuinely usable** | Calibrated tipping bucket | Rain accumulation/intensity directly changes drainage and inundation actions. Literature supplies a credible calibration/maintenance method, although the actual DIY unit still needs validation. [27] |
| **Genuinely usable** | Float plus ultrasonic water level | Directly measures the impact pathway. Redundant physical principles help detect a fouled or implausible reading. |
| **Genuinely usable** | ESP32 BLE phone sync | Matches the offline-phone architecture and avoids putting Linux/GSM on every field node. Current low-cost variants fit the BOM. [23] |
| **Genuinely usable** | IMD-first warning fusion | IMD already delivered Fani warnings 90/66/36 hours before landfall; a local node should refine farm actions, not compete with official forecasting. [12] |
| **Conditional** | Capacitive soil moisture | Useful only after soil- and placement-specific calibration. Pipli's ridge-top failure is direct evidence that naive placement makes an otherwise working sensor misleading. [29] |
| **Conditional** | DIY cup wind | Visually compelling and potentially useful, but no validated transfer curve or cyclone survivability evidence was found. Use in the demo UI, exclude from safety logic. |
| **Conditional** | LoRa | Can bridge villages, but the sourced module alone costs nearly Rs 2,000, and LoRa does not create routing, gateway backhaul, or regulatory compliance automatically. [6] [21] |
| **Mostly filler here** | UV and BH1750 light | Neither supplies a necessary precursor or flood-impact decision. They increase apertures, power, code paths, and calibration burden without evidence of avoided loss. |
| **Filler/unsafe claim** | "Pressure drop predicts a cyclone X hours ahead" | The reviewed Fani source lacks local hPa/hour observations; central pressure cannot be substituted for village pressure. [12] |
| **Filler/unsafe architecture** | LLM on every node | ESP32 should run deterministic statistics, not a language model. The language model belongs on the phone, where storage, memory, interaction, and update handling are more realistic. |
| **Filler/unsafe economics** | GSM and LoRa on every node under Rs 3,000 | The quoted LoRa unit consumes about two-thirds of the budget, and no reliable India GSM quote was recovered. Shared gateways and phones are the credible architecture. |
| **Filler/unsafe validation** | A successful tabletop demo proves field readiness | The Odisha pilot found placement-induced false alarms and >50% crop loss from unrelated biological causes. A functioning dashboard is not proof of agronomic benefit. [29] |

The minimum credible demo is therefore not the maximum-sensor demo. It is **ESP32 + BMP280 + rain + water level + battery health + BLE**, with soil moisture added after calibration. Every other channel must earn inclusion by changing an approved decision.

## 7. NOISE LOG

| Searched and discarded | Why discarded |
|---|---|
| US/AliExpress 433 MHz and 915 MHz LoRa boards | Import pricing was not an actual Indian-vendor cost; frequency and certification may not fit Indian deployment. |
| IndiaMART commercial tipping bucket around Rs 14,000 | Useful price reality check, but incompatible with the total Rs 3,000 cap and without sufficient calibration detail for this build. |
| Dynamic retailer/search pages with blank prices | A product title without an exposed current price cannot support the BOM. |
| Foreign SIM800L listings from Bangladesh, Turkey, Mexico and other markets | They do not answer actual India procurement cost, carrier compatibility, or local stock. |
| Generic "cyclone predictor using IoT" project pages | Most supplied architecture diagrams or marketing language but no local pressure trace, confusion matrix, field failure rate, or calibrated lead time. |
| Central-pressure histories treated as local barometer signatures | Scientifically mismatched: storm-center minimum pressure is not the time series observed at a farm. |
| Ozone, aerosol, sea-surface-temperature and satellite precursor studies | Some may be scientifically interesting, but a sub-Rs 3,000 terrestrial farm node cannot measure them credibly. The Fani study reported roughly 2 C SST warming and ozone changes, not a cheap-node pressure threshold. [8] |
| Global orchard/greenhouse WSN deployments | Useful for generic networking, but not evidence of Odisha cyclone survivability, Indian cost, or farmer warning outcomes. |
| UV/light additions | Decorative for this problem statement unless tied to a separately validated crop advisory. |
| Raspberry Pi as every node | Linux capability does not compensate for missing ADC, higher supply demand, boot/storage complexity, and unnecessary cost. [34] |
| "AI continuously learns on the phone" as a safety claim | Unlabeled local adaptation can reinforce false alarms. Only language/profile adaptation is safe without server-side validation and versioned rollback. |

## 8. VERDICT

### Prototype: **GO, with a narrow claim**

Build one to three nodes around ESP32, BMP280, DIY tipping bucket, waterproof level sensing, battery telemetry, and BLE. Add soil moisture only after a wet/dry calibration; include the DIY anemometer as an explicitly experimental visualization. Replay the official Fani timeline, inject recorded sensor traces, and demonstrate four things: IMD alert ingestion/cache, local anomaly fusion, farm-profile action selection, and Odia SMS/IVR rendering. IMD's documented 90/66/36-hour Fani messages provide a far more defensible demo clock than a fabricated pressure lead time. [12]

The **Rs 2,899** BOM is plausible but fragile. It excludes communications modules and operating costs, and more than half of the amount rests on allowances. Label it "target prototype BOM as accessed/designed on 2026-08-16," retain screenshots/quotes, and report actual landed spend after purchase. If the cap is strict, drop DHT22 and wind first rather than weakening the enclosure or power system.

### Pilot: **GATED**

A 20-50 node pilot should start only after six gates pass:

1. **Metrology:** colocate pressure, rain, wind, soil and water sensors against trusted references; publish error by rain intensity, temperature, soil type and mounting position.
2. **Reliability:** run monsoon ingress, condensation, corrosion, cable-pull, blocked-funnel, low-sun, battery-aging, brownout and recovery tests; record every service action.
3. **Decision validation:** use historical IMD events plus ordinary monsoon lows to set and freeze anomaly rules; report sensitivity, precision, false alarms and missed alerts. Pressure remains a corroborator.
4. **Communications:** survey village-specific BLE, cellular and proposed LoRa links; measure packet delivery, latency, backlog recovery and energy. Complete applicable radio/WPC review.
5. **Agronomic and language governance:** district agronomists approve pre/post-disaster templates; Odia speakers test comprehension; IVR supports repeat and acknowledgment; no LLM-generated dose or evacuation claim bypasses rules.
6. **Operations and economics:** obtain a vendor-quoted landed BOM, spares plan, installer method, ownership model, maintenance SLA, battery-replacement interval, SMS/IVR cost, data governance, signed updates and rollback.

**Overall verdict: PARTIAL.** The hardware and edge architecture are good enough for a convincing prototype, and primary sources support the key component choices. A pilot is not yet evidence-backed because the decisive public gaps are local precursor statistics, calibrated DIY wind/rain performance, Odisha cyclone-season failure rates, network availability, and action-to-crop-loss outcomes.

## References

1. *Gy Bme280 5V Temperature And Humidity Sensor*. https://robu.in/product/gy-bme280-5v-temperature-and-humidity-sensor/
2. *imdpune.gov.in*. https://imdpune.gov.in/hazardatlas/cyclone.pdf
3. *IMD APIs | India Meteorological Department*. https://mausam.imd.gov.in/responsive/apis.php
4. *Buy Capacitive Soil Moisture Sensor Online at Robu.in*. https://robu.in/product/capacitive-soil-moisture-sensor-v2-0/
5. *BMP280-5V Temperature and Barometric Pressure sensor*. https://robu.in/product/gy-bmp280-5v-temperature-and-humidity-sensor/
6. *LoRa Connect Transceiver, SX1276, 137MHz to 1020MHz  | Semtech*. https://www.semtech.com/products/wireless-rf/lora-connect/sx1276
7. *Datasheet SHT3x-DIS*. https://sensirion.com/media/documents/213E6A3B/63A5A569/Datasheet_SHT3x_DIS.pdf
8. *Impact of tropical cyclone “Fani” on land, ocean, atmospheric and meteorological parameters*. https://repository.library.noaa.gov/view/noaa/64512/noaa_64512_DS1.pdf
9. *bosch-sensortec.com*. https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf
10. *Solar Powered IoT Sensor: ESP32 Deep Sleep | Zbotic*. https://zbotic.in/solar-powered-iot-sensor-node-esp32-with-deep-sleep
11. *ESP32 Deep Sleep Battery Sensors(2026 Guide) – Esp32.co.uk*. https://esp32.co.uk/esp32-battery-powered-sensors-deep-sleep-low-power-design-guide
12. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/archive/60/60_a53fa0_fani.pdf
13. [
            A Wireless Sensor Network Deployment for Soil Moisture Monitoring in Precision Agriculture - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC8587686)
14. *BME280 Datasheet*. https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
15. *Calibration and Validation of a Low-Cost Capacitive Moisture Sensor to Integrate the Automated Soil Moisture Monitoring System*. https://www.mdpi.com/2077-0472/9/7/141
16. *Buy LoRa 868MHZ SX1276 Wireless Transmitter and Receiver RF ...*. https://robu.in/product/lora-868mhz-sx1276-wireless-transmitter-and-receiver-rf-module-e32-868t30d
17. *DHT22 AM2302 Digital Temperature and Humidity Sensor*. https://www.electronicscomp.com/dht22-am2302-digital-temperature-and-humidity-sensor
18. *ESP32-WROOM-32 38Pin Development Board WiFi+Bluetooth Ultra ...*. https://robu.in/product/esp32-38pin-development-board-wifibluetooth-ultra-low-power-consumption-dual-core
19. [
      Order Waterproof Ultrasonic Sensor for Your Next Electronics
 – Robocraze](https://robocraze.com/products/waterproof-ultrasonic-sensor)
20. *Analog to Digital Converter (ADC) - ESP32*. https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/api-reference/peripherals/adc.html
21. *Buy LoRa 868MHZ SX1276 Wireless Transmitter and Receiver RF Module E32-868T30D Online in India | The Engineer Store*. https://www.theengineerstore.in/products/lora-868mhz-sx1276-wireless-transmitter-and-receiver-rf-module-e32-868t30d
22. *Saurally Solar 3W 6V Panel with Junction Box, 3 Meter Cable DC Jack : Amazon.in: Garden & Outdoors*. https://www.amazon.in/Saurally-Solar-Panel-Junction-Meter/dp/B0C2HVRDYR
23. *Esp32 Development Board prices in India | FindMyChips*. https://findmychips.com/c/esp32-development-board
24. *Smart Plant Monitor: Soil Moisture and Light with Blynk*. https://zbotic.in/smart-plant-monitor-soil-moisture-and-light-with-blynk/
25. *OUAT*. https://ouat.ac.in/research/amfu/
26. *Four Stage Warning*. https://rsmcnewdelhi.imd.gov.in/four-stage-warning.php
27. [
            Tipping Bucket Rain Gauges in Hydrological Research: Summary on Measurement Uncertainties, Calibration, and Error Reduction Strategies - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10302425)
28. *Tipping‐bucket rain gauges: a review of the undercatch phenomenon, and methods for its reduction and correction - Dunn - 2025 - Weather - Wiley Online Library*. https://rmets.onlinelibrary.wiley.com/doi/full/10.1002/wea.7736
29. *Sensor-based Irrigation Management in Odisha (SIMO) – a pilot study on Tomato crop*. https://www.iconceptinitiatives.org/climate-change-adaptation/Notice/(SIMO)%20%E2%80%93%20A%20Pilot%20study%20on%20Tomato%20crop.pdf
30. *Digital-output relative humidity & temperature sensor/module*. https://cdn.sparkfun.com/assets/f/7/d/9/c/DHT22.pdf
31. *FAQ-TC-26April2023 - IMD*. https://rsmcnewdelhi.imd.gov.in/images/pdf/faq.pdf
32. *Terminology on Cyclonic disturbances over the North Indian ...*. https://rsmcnewdelhi.imd.gov.in/images/pdf/terminology.pdf
33. *ESP8266EX Datasheet*. https://documentation.espressif.com/0a-esp8266ex_datasheet_en.html
34. *Raspberry Pi Zero 2 W*. https://pip.raspberrypi.com/documents/RP-008359-DS-raspberry-pi-zero-2-w-product-brief.pdf
35. *localhost:8123/A000005/auabl-datasheet.html*. https://docs.arduino.cc/resources/datasheets/A000005-datasheet.pdf
36. *ESP32 Datasheet*. http://documentation.espressif.com/esp32_datasheet_en.html
