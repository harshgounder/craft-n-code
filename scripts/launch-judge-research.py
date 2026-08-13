#!/usr/bin/env python3
"""launch-judge-research.py — fire the judge-dossier deep research via direct REST.
Tries TASK_ALIVE keys in order, fallback-chains on 402. Writes run_id + key to a ledger."""
import os, json, sys, time, urllib.request, urllib.error

KEYS_FILE = os.path.expanduser("~/Desktop/parallel spams")
LEDGER = os.path.expanduser("~/craft-n-code/research/raw/judge-runs.json")

PROMPT = """Deep OSINT research on 6 hackathon judges who judged Hackfest 2024 (national hackathon by Tech Society at IIIT Bhubaneswar, India, Nov 2024). For EACH of these 6 people build a detailed dossier: 1) Ayushi Parashar 2) Shivani Prasad 3) Sarthak Padhi 4) ACP Anjana Tudu (Odisha Police, Assistant Commissioner of Police) 5) Lingaraj Sethi (cybersecurity expert, Odisha) 6) Sonali Satpathy. For each: full professional identity (current role, employer, title), LinkedIn profile URL, education, career history, cybersecurity/tech expertise, public talks/posts/papers, other hackathons judged/organized, public statements about hackathons or tech evaluation, and what they likely reward when judging (technical depth vs presentation vs impact). Especially: news articles on Anjana Tudu (police officer) and Lingaraj Sethi (cyber expert). Include source URLs for every claim. Be exhaustive, cite everything, no fluff."""

def launch(key, idx):
    body = json.dumps({"input": PROMPT, "processor": "ultra8x"}).encode()
    req = urllib.request.Request(
        "https://api.parallel.ai/v1/tasks/runs",
        data=body,
        headers={"Content-Type": "application/json", "x-api-key": key},
        method="POST",
    )
    try:
        r = urllib.request.urlopen(req, timeout=60)
        data = json.loads(r.read().decode())
        return r.status, data
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:200]
    except Exception as e:
        return -1, str(e)[:200]

def main():
    keys = [l.strip() for l in open(KEYS_FILE) if l.strip()]
    # try the TASK_ALIVE block first (103-113 = idx 102-112), then full pool
    order = list(range(102, 113)) + [i for i in range(len(keys)) if i not in range(102, 113)]
    for idx in order:
        if idx >= len(keys):
            continue
        status, data = launch(keys[idx], idx)
        print(f"key#{idx+1}: HTTP {status} | {str(data)[:120]}")
        if status == 202:
            run_id = data.get("run_id") if isinstance(data, dict) else None
            if run_id:
                ledger = {"run_id": run_id, "key_idx": idx + 1, "key_tail": keys[idx][-6:],
                          "processor": "ultra8x", "launched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                          "topic": "judge-dossiers-x6"}
                with open(LEDGER, "w") as f:
                    json.dump(ledger, f, indent=2)
                print(f"LAUNCHED {run_id} with key#{idx+1} -> {LEDGER}")
                return 0
        if status == 402:
            continue  # fallback chain
        if status in (200, 201):
            # accepted but odd shape; try to extract run_id anyway
            if isinstance(data, dict) and data.get("run_id"):
                run_id = data["run_id"]
                ledger = {"run_id": run_id, "key_idx": idx + 1, "key_tail": keys[idx][-6:],
                          "processor": "ultra8x", "launched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                          "topic": "judge-dossiers-x6"}
                with open(LEDGER, "w") as f:
                    json.dump(ledger, f, indent=2)
                print(f"LAUNCHED {run_id} with key#{idx+1} -> {LEDGER}")
                return 0
    print("ALL KEYS FAILED")
    return 1

if __name__ == "__main__":
    sys.exit(main())
