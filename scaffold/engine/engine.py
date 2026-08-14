# Signal Engine - ingest → dedupe → summarize → rank → deadlines
# Craft N Code 2026 shared scaffold (IDEA-BANK §6.1)
# One engine, many skins: Signal (PS-03), Campus Pulse (PS-01), Night Ops (PS-02).
#
# LLM layer: ollama-cloud (OpenAI-compatible, deepseek-v4-flash:0731) with
# disk cache + FULL offline fallback (regex deadlines + tf-idf ranking).
# Zero paid keys, zero external deps in the demo. AFTERPACKETS rule.

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import sys
import time
import urllib.request
from collections import Counter
from dataclasses import dataclass, field, asdict
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Optional

DB_PATH = Path(__file__).parent / "signal.db"
CACHE_PATH = Path(__file__).parent / ".llm_cache.json"
OLLAMA_KEY = os.environ.get("OLLAMA_API_KEY", "")
OLLAMA_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.com/v1").rstrip("/")
OLLAMA_MODEL = os.environ.get("SIGNAL_MODEL", "deepseek-v4-flash:0731")

# ────────────────────────────────────────────────────────────────
# 1. DATA MODEL
# ────────────────────────────────────────────────────────────────

@dataclass
class Item:
    """One raw message/notice/complaint from any channel."""
    channel: str            # gmail | classroom | unstop | portal | whatsapp | instagram | complaint
    source_id: str          # unique id within channel
    sender: str
    subject: str
    body: str
    received_at: str        # ISO
    profile_tags: list = field(default_factory=list)  # e.g. ["2nd-year", "E&CE", "hostel"]
    kind: str = "notice"    # notice | complaint | deadline | event
    summary: str = ""
    rank_score: float = 0.0
    deadline: Optional[str] = None
    deadline_iso: Optional[str] = None
    is_urgent: bool = False

    def dedupe_key(self) -> str:
        # normalized subject + first 80 chars of body = near-dup fingerprint
        s = re.sub(r"[^a-z0-9]+", "", (self.subject + " " + self.body).lower())[:120]
        return s

    def as_dict(self):
        return asdict(self)


# ────────────────────────────────────────────────────────────────
# 2. LLM LAYER (ollama-cloud + cache + offline fallback)
# ────────────────────────────────────────────────────────────────

class LLM:
    """Tiny OpenAI-compatible client. Uses ollama-cloud when key present,
    falls back to rule-based offline mode (no network at all)."""

    def __init__(self, cache_path: Path = CACHE_PATH):
        self.cache_path = cache_path
        self.cache: dict = {}
        if cache_path.exists():
            try:
                self.cache = json.loads(cache_path.read_text())
            except Exception:
                self.cache = {}
        self.hits = 0
        self.misses = 0

    def _save_cache(self):
        try:
            self.cache_path.write_text(json.dumps(self.cache, indent=1))
        except Exception:
            pass

    def chat(self, system: str, user: str, max_tokens: int = 400, temperature: float = 0.2) -> Optional[str]:
        key = hashlib.sha256((system + "\x00" + user).encode()).hexdigest()[:32]
        if key in self.cache:
            self.hits += 1
            return self.cache[key]
        self.misses += 1

        if not OLLAMA_KEY:
            return None

        payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        req = urllib.request.Request(
            f"{OLLAMA_URL}/chat/completions",
            data=json.dumps(payload).encode(),
            headers={
                "Authorization": f"Bearer {OLLAMA_KEY}",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                data = json.loads(resp.read().decode())
            out = data["choices"][0]["message"]["content"].strip()
            self.cache[key] = out
            self._save_cache()
            return out
        except Exception as e:
            print(f"  [llm] ollama-cloud failed ({e}); using offline", file=sys.stderr)
            return None


# ────────────────────────────────────────────────────────────────
# 3. OFFLINE FALLBACK (rule-based - the demo never dies)
# ────────────────────────────────────────────────────────────────

MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}

DATE_PATTERNS = [
    # "22 Aug 2026", "22 August 2026"
    re.compile(r"\b(\d{1,2})\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{4})\b", re.I),
    # "Aug 22, 2026"
    re.compile(r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{1,2}),?\s+(\d{4})\b", re.I),
    # "22/08/2026", "22-08-2026", "22.08.26"
    re.compile(r"\b(\d{1,2})[/\-.](\d{1,2})[/\-.](\d{2,4})\b"),
    # "22 Aug" (year implied = upcoming)
    re.compile(r"\b(\d{1,2})\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\b", re.I),
]

DEADLINE_WORDS = ["last date", "deadline", "due", "submit by", "before", "by "]

URGENT_WORDS = ["urgent", "immediate", "last date", "deadline", "tomorrow", "mandatory",
                "compulsory", "exam", "mte", "ete", "fee", "fine", "suspend", "ragging"]

def parse_date(text: str, today: date) -> Optional[date]:
    for pat in DATE_PATTERNS:
        m = pat.search(text)
        if not m:
            continue
        g = m.groups()
        if len(g) == 3 and g[2].isdigit():
            day, mon, year = int(g[0]), MONTHS[g[1].lower()[:3]], int(g[2])
            if year < 100:
                year += 2000
            try:
                return date(year, mon, day)
            except ValueError:
                continue
        # "22 Aug" → nearest upcoming
        if len(g) == 2:
            day, mon = int(g[0]), MONTHS[g[1].lower()[:3]]
            try:
                d = date(today.year, mon, day)
                if d < today:
                    d = date(today.year + 1, mon, day)
                return d
            except ValueError:
                continue
    return None

def offline_summarize(item: Item) -> str:
    """Extractive summary: first sentence + key numbers, no LLM needed."""
    text = item.body.strip()
    first = text.split("\n")[0] if text else item.subject
    first = re.sub(r"\s+", " ", first).strip()
    if len(first) > 140:
        first = first[:137].rsplit(" ", 1)[0] + "..."
    return f"{item.subject} | {first}"

def offline_extract_deadline(item: Item, today: date) -> Optional[str]:
    text = (item.subject + " " + item.body).lower()
    d = parse_date(text, today)
    if d is None:
        return None
    # only treat as deadline if a deadline-ish word is near, or kind=deadline
    if any(w in text for w in DEADLINE_WORDS) or item.kind == "deadline":
        return d.isoformat()
    return None

def offline_rank(items: list[Item], profile: list[str], today: date) -> list[Item]:
    """TF-IDF-ish + recency + authority + deadline pressure. Deterministic."""
    # corpus stats
    doc_terms = []
    for it in items:
        doc_terms.append(Counter(re.findall(r"[a-z]{3,}", (it.subject + " " + it.body).lower())))
    df: Counter = Counter()
    for dt in doc_terms:
        for t in set(dt):
            df[t] += 1
    n = max(len(items), 1)

    AUTHORITY = {"registrar": 5, "dean": 5, "controller": 5, "hoc": 4, "hod": 4, "faculty": 3,
                 "club": 2, "committee": 2, "student": 1, "whatsapp": 1, "bot": 1}

    scored = []
    for it, dt in zip(items, doc_terms):
        score = 0.0
        # profile match: tokens that appear in the item and the user profile
        prof_terms = [t for t in re.findall(r"[a-z]{3,}", " ".join(profile).lower())]
        if prof_terms:
            hit = sum(1 for t in set(dt) if t in prof_terms) / len(prof_terms)
            score += 2.5 * hit
        # authority
        sender_l = it.sender.lower()
        for k, v in AUTHORITY.items():
            if k in sender_l:
                score += v
                break
        # recency: 0-2 days old = full points, decays to 0 over 7 days
        try:
            age_days = (today - datetime.fromisoformat(it.received_at).date()).days
        except Exception:
            age_days = 0
        score += max(0.0, 2.0 - age_days * 0.35)
        # deadline pressure: closer = higher, deadline passed = 0
        if it.deadline_iso:
            try:
                dl = date.fromisoformat(it.deadline_iso)
                days_left = (dl - today).days
                if days_left < 0:
                    score -= 3
                else:
                    score += max(0.0, 3.0 - days_left * 0.15)
            except Exception:
                pass
        # urgency words
        if any(w in (it.subject + " " + it.body).lower() for w in URGENT_WORDS):
            score += 1.2
        it.rank_score = round(score, 3)
        it.is_urgent = score >= 6.0
        scored.append(it)

    scored.sort(key=lambda x: -x.rank_score)
    return scored


# ────────────────────────────────────────────────────────────────
# 4. PIPELINE
# ────────────────────────────────────────────────────────────────

SUMMARIZE_SYSTEM = (
    "You compress student notices to ONE line (max 140 chars). Output ONLY the summary, "
    "no prefix, no quotes. Keep numbers, dates, and room numbers."
)
DEADLINE_SYSTEM = (
    "Extract the single most important deadline from this notice. Output ONLY an ISO date "
    "YYYY-MM-DD, or the word NONE if no deadline exists. If a relative date is given, resolve "
    "it against today. Today is {today}."
)

def llm_summarize(llm: LLM, item: Item) -> str:
    out = llm.chat(SUMMARIZE_SYSTEM, f"{item.subject}\n{item.body[:1200]}")
    if not out:
        return offline_summarize(item)
    return out.strip()[:160]

def llm_deadline(llm: LLM, item: Item, today: date) -> Optional[str]:
    out = llm.chat(DEADLINE_SYSTEM.format(today=today.isoformat()),
                   f"Subject: {item.subject}\nBody: {item.body[:1200]}")
    if not out:
        return offline_extract_deadline(item, today)
    m = re.search(r"\d{4}-\d{2}-\d{2}", out)
    return m.group(0) if m else offline_extract_deadline(item, today)


def dedupe(items: list[Item]) -> list[Item]:
    seen: dict[str, Item] = {}
    for it in items:
        k = it.dedupe_key()
        if k in seen:
            # keep the newer one
            if it.received_at > seen[k].received_at:
                seen[k] = it
        else:
            seen[k] = it
    return list(seen.values())


def run_pipeline(items: list[Item], profile: list[str], today: Optional[date] = None) -> dict:
    today = today or date.today()
    llm = LLM()

    print(f"[engine] {len(items)} raw items → dedupe…")
    items = dedupe(items)
    print(f"[engine] {len(items)} after dedupe → summarize…")
    for it in items:
        it.summary = llm_summarize(llm, it)
        it.deadline_iso = llm_deadline(llm, it, today)
        if it.deadline_iso:
            it.deadline = it.deadline_iso
    print(f"[engine] ranking {len(items)} items…")
    ranked = offline_rank(items, profile, today)
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "today": today.isoformat(),
        "llm": {"model": OLLAMA_MODEL if OLLAMA_KEY else "OFFLINE",
                "cache_hits": llm.hits, "cache_misses": llm.misses},
        "profile": profile,
        "total": len(ranked),
        "items": [it.as_dict() for it in ranked],
    }


# ────────────────────────────────────────────────────────────────
# 5. SEED DATA (real MUJ-shaped notices, pre-imported for the demo)
# ────────────────────────────────────────────────────────────────

def seed_items() -> list[Item]:
    now = datetime.now()
    d = now.date()
    iso = lambda dd: datetime(dd.year, dd.month, dd.day, 9, 0).isoformat()
    base = [
        Item("portal", "n1", "Registrar Office", "MTE 2026 schedule released",
             f"Mid-Term Examinations will be held from 18 Sep to 25 Sep 2026. "
             f"Detailed timetable on the portal. Last date to apply for re-exam: 10 Sep 2026.",
             iso(d - timedelta(days=1)), ["exam"]),
        Item("gmail", "g1", "Dean Student Welfare", "Hostel fee payment reminder",
             f"Hostel fee for Semester 5 is due by 20 Aug 2026. Late payment attracts a fine of ₹500/day. "
             f"Pay via the portal or fee desk before 5 PM.",
             iso(d - timedelta(days=0)), ["hostel", "fee"]),
        Item("classroom", "c1", "Prof. Mehta (ELC2107)", "Unit 2 assignment: LTI systems",
             f"Assignment 2 uploaded. Submit by 19 Aug 2026 on Classroom. "
             f"Covers convolution and impulse response, 10 questions, 15 marks.",
             iso(d - timedelta(days=2)), ["e&ce", "assignment"]),
        Item("whatsapp", "w1", "WhatsApp: E&CE 2nd Year", "Room shift for tomorrow's Networks lab",
             f"NETWORKS LAB SHIFTED to Room 4104 (was 4102). Same slot 2-4 PM. "
             f"Share with everyone. Urgent.",
             iso(d - timedelta(hours=3)), ["e&ce", "lab"]),
        Item("unstop", "u1", "Unstop Bot", "Craft N Code 2026 registrations open",
             f"Rajasthan State Qualifier at MUJ. Idea submission opens 21 Aug 21:00, closes 22 Aug 06:00. "
             f"Register on Unstop. 131K prize pool.",
             iso(d - timedelta(days=3)), ["hackathon"]),
        Item("instagram", "i1", "Instagram: MUJ Memes", "5 memes about the canteen queue",
             f"Repost: canteen queue at 1 PM is 40 minutes. #mujproblems #mess",
             iso(d - timedelta(hours=1)), []),
        Item("gmail", "g2", "Library", "Library fine clearance deadline",
             f"All pending library fines must be cleared by 30 Aug 2026 or semester results are withheld.",
             iso(d - timedelta(days=5)), ["library"]),
        Item("portal", "n2", "Exam Cell", "Backlog exam form",
             f"Backlog exam application forms available. Last date: 5 Sep 2026. Form fee ₹300.",
             iso(d - timedelta(days=4)), ["exam"]),
    ]
    # complaints (Campus Pulse skin)
    complaints = [
        Item("complaint", "cpt1", "Student (Ananya S.)", "Hostel C water cooler broken",
             "Water cooler on Hostel C floor 3 has been broken for a week. Hot days, no drinking water. "
             "Category: plumbing. Severity: high.",
             iso(d - timedelta(days=1)), ["hostel"], kind="complaint"),
        Item("complaint", "cpt2", "Student (Rohan K.)", "Canteen food quality",
             "Found a hair in the paneer today. This is the second time this month. "
             "Category: hygiene. Severity: medium.",
             iso(d - timedelta(days=3)), ["mess"], kind="complaint"),
        Item("complaint", "cpt3", "Student (Priya M.)", "Streetlight flickering near gate 2",
             "The streetlight near Gate 2 flickers all night. Dark stretch, unsafe for late walkers. "
             "Category: electrical. Severity: high.",
             iso(d - timedelta(days=0)), ["safety"], kind="complaint"),
    ]
    return base + complaints


# ────────────────────────────────────────────────────────────────
# 6. CLI
# ────────────────────────────────────────────────────────────────

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Signal engine - one feed for a student's day")
    ap.add_argument("--seed", action="store_true", help="run on seed demo data")
    ap.add_argument("--json", action="store_true", help="dump full JSON result")
    ap.add_argument("--digest", action="store_true", help="print the 'today in 60 seconds' digest")
    ap.add_argument("--profile", default="2nd-year,e&ce,hostel", help="comma profile tags")
    ap.add_argument("--out", default="", help="write JSON result to this path")
    args = ap.parse_args()

    items = seed_items() if args.seed else []
    if not items:
        print("no items. use --seed for demo data (or extend connectors in code)")
        return 1

    result = run_pipeline(items, [t.strip() for t in args.profile.split(",") if t.strip()])

    if args.out:
        Path(args.out).write_text(json.dumps(result, indent=1))
        print(f"[engine] wrote {args.out}")

    if args.digest:
        print("\n=== TODAY IN 60 SECONDS ===")
        urgent = [i for i in result["items"] if i["is_urgent"]][:3]
        for it in urgent:
            dl = f"  ⏰ deadline {it['deadline_iso']}" if it["deadline_iso"] else ""
            print(f"  ! {it['summary']}{dl}")
        print("--- top 5 ---")
        for it in result["items"][:5]:
            print(f"  {it['rank_score']:5.2f} [{it['channel']:9s}] {it['summary']}")
        print(f"\n[{result['llm']['model']}] cache h={result['llm']['cache_hits']} m={result['llm']['cache_misses']}")
    elif args.json:
        print(json.dumps(result, indent=1))
    else:
        print(f"total={result['total']} llm={result['llm']}")

    # sqlite persistence (Supabase-ready shape)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DROP TABLE IF EXISTS items")
    conn.execute("""CREATE TABLE items (
        channel TEXT, source_id TEXT, sender TEXT, subject TEXT, body TEXT,
        received_at TEXT, summary TEXT, rank_score REAL, deadline_iso TEXT,
        is_urgent INTEGER, kind TEXT)""")
    for it in result["items"]:
        conn.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                     (it["channel"], it["source_id"], it["sender"], it["subject"], it["body"],
                      it["received_at"], it["summary"], it["rank_score"], it["deadline_iso"],
                      int(it["is_urgent"]), it["kind"]))
    conn.commit()
    print(f"[engine] persisted {len(result['items'])} rows → {DB_PATH.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
