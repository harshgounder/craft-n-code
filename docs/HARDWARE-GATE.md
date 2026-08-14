# PS-05 HARDWARE GATE — sourcing checklist (deadline: Aug 15 12:00)

The gate: if no board + sensors in hand by Aug 15 12:00 IST, PS-05 is DEAD.
Do not write a hardware pitch without hardware. The gate exists for a reason.

## What we need (minimum viable rig, ~₹700-800 total)

| Part | Est price | Where | Status |
|---|---|---|---|
| ESP32 dev board (or RPi Pico W) | ₹400-500 | Amazon 1-day / MUJ E&CE lab | [ ] |
| MQ135 air-quality sensor | ~₹100 | Amazon / lab | [ ] |
| DHT11 temp+humidity sensor | ~₹60 | Amazon / lab | [ ] |
| Breadboard + jumper wires | ~₹100 | Amazon / lab / any electronics shop | [ ] |
| USB cable (data, not charge-only!) | ~₹100 | Anywhere | [ ] |

## Actions for TODAY (Aug 14)

1. **Ayush + Sujal**: go ask the MUJ E&CE lab in-charge. We are E&CE 2nd year, the lab HAS
   ESP32/Pico boards and sensors. Ask: can we borrow for Aug 15-16?
   Say it's for the Craft N Code hackathon, hardware track, we return everything.
   Lab in-charge office: E&CE department block (ask the dept reception).
2. **Harsh (backup)**: check Amazon 1-day delivery tonight, order if lab says no.
   Prime delivery to MUJ campus or hostel address. Need it in hand by Sat morning.
3. Decision call: **Aug 15 12:00 sharp**. Text group chat. 3 votes, majority.
   If lab says yes + hardware physically in hand -> green light PS-05 as an option.
   If not -> PS-05 is OFF the table, no debate.

## The demo if we get hardware (IDEA 5A Hygiene Sentinel)

- ESP32 reads MQ135 + DHT11 -> sends over WiFi/USB to the dashboard (reuse the webapp skin!)
- Threshold breach (e.g. CO2/AQI > X) -> LED + buzzer on the board + alert on dashboard
- Compliance log: sensor history, export as PDF (the mess committee sells itself)
- On stage: live readings on the projector, trigger the buzzer by waving something smoky

## The trap to remember

- 24h + hardware debugging = highest failure mode of the whole idea bank
- If hardware is 80% working at 5 AM, we still have to submit at 6 AM
- The fallback: even with hardware, PS-03/01/02 are safer. The decision tree picks.
