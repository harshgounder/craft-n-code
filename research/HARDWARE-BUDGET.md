# HARDWARE-BUDGET.md — Minimum Spend, Maximum Demo

Date: 2026-08-16. Goal: least hardware, least money, honest demo.
Everything the judges see is either IN OUR HANDS or LABELED SIMULATION.

## 0. THE PRINCIPLE

We simulate the fleet, we buy ONE node. The demo shows one real sensor
node streaming live pressure/water/rain data into the advisory engine,
while the mesh of 100 nodes, the phone fleet, the satellite feeds, and
the server training loop are simulated with honest labels. Simulated
layers cost Rs 0 and cannot break on stage.

## 1. WHAT WE ALREADY OWN (Rs 0)

| Asset | Spec | Job in the demo |
|---|---|---|
| Laptop (this box) | Ryzen 5 5600H, 12 cores, 7.1 GB RAM, GTX 1650 4 GB VRAM | Runs the engine, the replay, the webapp, AND 1B QLoRA training locally (4 GB VRAM is enough for 1B QLoRA; d11's floor is 3.5 GB) |
| Team phones | Any 4-6 GB Android | The "phone hub" target: Llama 3.2 1B Q4 (0.81 GB) runs on a 6 GB handset; we demo on our own, claim "Lava Blaze 3 5G class" |
| Arduino/ESP gear (check team) | Unknown | Optional extra node if someone owns one |
| OLLAMA cloud key | Already configured | The language layer fallback |

## 2. THE ONE REAL NODE WE BUY (~Rs 1,500)

Shopping list, prices from the d12 mine (Robu/Robocraze/DNA Tech listings):

| Part | Price (Rs) | What it measures | Why |
|---|---|---|---|
| ESP32 NodeMCU (WiFi+BLE) | 370 | controller | BLE to phone, WiFi for dev, Rs 232 for C3 variant |
| BMP280 pressure + temp | 85 | pressure tendency | THE cyclone precursor signal (+/-0.12 hPa relative) |
| DHT22 temp + humidity | 120 | RH | blast-disease conditions (92-96% RH), comfort |
| Waterproof ultrasonic JSN-SR04T | 249 | water level | flood rise rate, drainage clog detection |
| DIY tipping-bucket rain gauge | 150 | rain rate | local rain intensity, 5/15/60-min rates |
| Breadboard + jumpers + power bank | 350 | - | prototype mounting, phone-bank power |

TOTAL: ~Rs 1,324. Add Rs 200 shipping/overrun -> ~Rs 1,500.

Omitted on purpose (from d12's own analysis):
- Capacitive soil moisture (Rs 49): Pipli tomato pilot showed placement
  produces false dry alarms; skip until field-tested
- UV sensor: "no demonstrated cyclone/flood decision value" (d12 verdict)
- Commercial anemometer: DIY cups + reed switch (Rs 300) or skip; the
  BMP280 trend + official IMD wind polygons cover wind
- Solar + battery: for a 30-minute demo, a power bank is the honest
  power source; solar belongs in the pilot BOM

## 3. WHAT WE SIMULATE INSTEAD OF BUY (Rs 0, labeled)

| Layer | Simulated as | Label |
|---|---|---|
| Fleet of 100 sensor nodes | Synthetic streams from the d21 replay data (real Fani/Yaas/Dana station series) | "SIMULATED FEED: replayed from IMD/NOAA station archives" |
| Phone fleet (100 farmers) | 1-2 webapp sessions + one phone if someone's handset can sideload | "PROTOTYPE CLIENTS" |
| Server training loop | 1B QLoRA on the laptop GPU (real, live) or Colab/Kaggle free tier for 3B | "LOCAL TRAINING" |
| SMS delivery | Simulator queue with delivery receipts | "SIMULATED SMS (no live sending)" |
| IVR | Simulator with Odia TTS sample | "SIMULATED IVR" |
| Satellite rainfall | IMERG Final V07 archive for the replayed event | "ARCHIVED SATELLITE DATA (NASA GPM)" |

The only "fake" things on stage are explicitly labeled. The one real
node streams real pressure and water readings in real time.

## 4. COST COMPARISON: DEMO vs REAL PILOT

| Item | Demo (we spend) | Real pilot (one village cluster) |
|---|---|---|
| Sensor node | Rs 1,324 (1 node) | Rs 2,899/node BOM + enclosure, mast, solar, installation, comms: Thailand field case showed ~Rs 80K/station all-in (d13) |
| Phone hub | Rs 0 (our phones) | Rs 10,999 (Lava Blaze 3 5G, 6 GB) per farmer hub |
| Training server | Rs 0 (GTX 1650 local, or free Colab/Kaggle) | NVIDIA L4 24 GB or cloud GPU rental, 24x7 ops (d11) |
| SMS | Rs 0 (simulator) | Rs 0.18/message at 30K volume + 18% GST + DLT registration (d7) |
| IVR | Rs 0 (simulator) | Rs 0.40-0.65/minute (d7) |
| Feeds | Rs 0 (CAP RSS public, archives) | Rs 0 (public) + partner agreements |
| TOTAL | ~Rs 1,500 | Rs 5-10 lakh for a serious pilot |

The demo costs less than a dinner. The pilot economics are the story
for the business-model slide, not a purchase.

## 5. THE STAGE PRESENTATION (what judges see)

1. One ESP32 node on the table, power-bank fed, streaming LIVE pressure
   (BMP280) + water level (ultrasonic) to the laptop via BLE/USB
2. The webapp shows the node's real time series: pressure falling,
   water rising, node health badge
3. The advisory engine fuses it with the official IMD CAP alert for the
   replayed event (Fani/Yaas/Dana) and produces the staged Odia action
4. "Simulated fleet" toggle: the replay spreads the node's behavior
   across 100 synthetic farms, each with a farm profile
5. The phone (our own) shows the offline 1B Q4 rendering the same
   advisory with no internet; kill the WiFi to prove it
6. Training loop: 1B QLoRA runs on the laptop during the demo (or a
   pre-trained adapter hot-swaps in the UI)
7. Everything labeled: REAL NODE / SIMULATED FEED / ARCHIVED DATA

## 6. ROUND SPLIT (delivery reality)

- Round 0 (today, 18:00): NO physical hardware needed. Electronics
  delivery in India is 2-5 days; the node cannot arrive. Demo runs
  fully on the laptop: replayed sensor streams + real CAP feed + engine
  + offline LLM + honest labels. The "one real node" becomes a slide.
- Round 1 (next weekend): buy the Rs 1,500 node on Monday, assemble,
  stream live on stage. That is the Round 0 -> Round 1 depth story.
- Round 2 (IIIT-B): pilot-cost table + whatever the new statement needs.

## 7. RISK TABLE

| Risk | Mitigation |
|---|---|
| Node fails on stage | Everything is simulated behind a toggle; the demo runs without it |
| GTX 1650 too small for 3B | 1B is the design center; 3B only on free Colab/Kaggle |
| No sideload-able phone in team | Webapp client suffices; phone demo optional |
| Judge asks "where are the 100 nodes" | "One real node + replayed fleet; pilot BOM is Rs 5-10L" |
| Judge asks "is the SMS real" | "Simulator, labeled; real SMS is Rs 0.18/message + DLT" |
