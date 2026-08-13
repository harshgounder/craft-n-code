# EXACT-WINNER DEEP-DIVE — AFTERPACKETS (2025 National Winner)

Compiled: 2026-08-13 | Sources: full repo forensics (PrashamJ17/AfterPackets), FEATURE_GUIDE, commit history, C++ parser source

## 1. WHAT THEY BUILT (beyond the required MVP)

The problem (Challenge 7) required: capture module, traffic dashboard, DPI packet inspector, filtering controls.

**They shipped ALL of that PLUS:**

| Feature | Detail |
|---|---|
| App-level tracking | Per-app sent/received bytes, remote hosts, protocols, sorted by usage |
| Geo map | Real device location + remote server plotting, country/connection lines |
| Security alerts | MITM, DNS spoofing, ARP spoofing, data exfiltration, suspicious patterns, 4 severity levels |
| Custom detection rules | Metric (outbound_bytes/packet_rate/connection_count/failed_connections) + condition + threshold + time window + action (alert/log/block) + severity |
| Export | PCAP (Wireshark-compatible), JSON, Evidence Bundle (PCAP+JSON+report+timeline+threat assessment) |
| WebSocket server | Real-time streaming to companion web app |
| Firewall engine | FirewallRuleEngine.kt — block actions |
| VpnSocketProtector | Protects the VPN socket from being captured (self-awareness) |
| VpnDiagnostics + VpnVerification | Self-testing VPN setup |

## 2. THE C++ DPI CORE (packet_parser.cpp)

- Hand-rolled IPv4/TCP/UDP/ICMP parsing (no library)
- `parseIPv4`: version check, IHL, source/dest IP, total length, protocol switch
- `parseTCP`: source/dest ports, flags
- `ntohl/ntohs` byte-order handling, hex/ASCII payload view
- Native via JNI (NativePacketParser.kt) — performance + "real engineering" signal

## 3. THE ANDROID ARCHITECTURE (40+ Kotlin files)

- `PacketCaptureService : VpnService()` — MTU 1400, buffer 32767, coroutine-based
- Room database (PacketDao, FilterPresetDao) — persisted captures
- MVVM (MainViewModel, screens per feature)
- 13 UI screens: Dashboard, PacketList, PacketDetail, Filter, Alerts, Rules, Export, Map, AppDataDonut, TopTalkers, ConnectionDetails, PayloadWarning, ProtocolPie
- Theme system (Color/Theme/Type.kt) — polished dark UI

## 4. THE COMMIT TIMELINE (finals day, Nov 8 2025)

| Time (UTC) | Action |
|---|---|
| 06:56 | Initial commit (core built) |
| 07:17 | Removed geo-location features from README (scope-down) |
| 07:26 | Deleted debug APKs (cleanup) |
| 08:01 | Renamed Mobile Packet Hunter → AFTERPACKETS (rebrand) |
| 08:11 | Removed desktop web app documentation (scope-down) |
| 2026-04-07 | README update (post-event polish) |

## 5. WHY THIS WON (the full argument)

1. **Technical depth**: native C++ DPI + VPNService + Room + WebSocket + firewall = the deepest stack in the room. Judges (security experts: Anjana Tudu, Lingaraj Sethi) could verify real engineering.
2. **Zero external dependencies**: no OAuth, no API keys, no SDKs, no quota limits. It WORKED at demo time. (Compare: PromptBuddy fought Composio SDK bugs + Gemini 429s all night.)
3. **Security relevance**: MITM/DNS-spoofing/ARP-spoofing detection + evidence-bundle export = exactly what cyber judges care about.
4. **Empty lane**: only 1 team attempted Challenge 7. The 5-team lab-grader lane split attention.
5. **Demo-ability**: VPNService capture is visually impressive live (packets flowing, pie charts, map).
6. **Story**: "Mobile Wireshark for Kali NetHunter" = instantly understandable, impressive framing.

## 6. THE COUNTERFACTUAL (what the losers did)

- PromptBuddy (Challenge 5, 1 team): FULLY implemented MVP (all features, OAuth, dashboards, docs) but fought Composio SDK bugs (v0.1.55/v0.2.3 both broken), Gemini 429 quota (100 emails/request), 6 critical bugs fixed at 2am. Their own docs are a war diary.
- EduSynth (Challenge 4): 77MB production-grade FastAPI + Gemini 2.5 Pro + Prisma + MoviePy + R2. Real product. Lost to a 201MB junk-committed Android app.
- The lab-grader lane (5 teams): most crowded, most split.

**The lesson: a working demo of a hard thing beats a polished product of an easy thing. Zero-dependency wins. Empty lane wins.**
