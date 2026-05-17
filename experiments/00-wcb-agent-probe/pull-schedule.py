"""Pull WCB schedule + tasks for the AI x Web3 School program.

Usage:
    set WCB_AGENT_SECRET_API_KEY=w3cb_sk_xxx
    python pull-schedule.py

Writes to ../../wcb-schedule.md and prints a today/this-week summary.
"""
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.request import Request, urlopen

# Force UTF-8 stdout on Windows so Chinese titles print correctly.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

BASE = "https://web3career.build/api/agent/call"
PROGRAM_ID = "cmnx791nl008sru0167pzp4ki"
SLUG = "AI-Web3-School"
CN_TZ = timezone(timedelta(hours=8))


def call(procedure: str, payload: dict) -> dict:
    key = os.environ.get("WCB_AGENT_SECRET_API_KEY")
    if not key:
        sys.exit("ERROR: set WCB_AGENT_SECRET_API_KEY env var first.")
    req = Request(
        BASE,
        data=json.dumps({"procedure": procedure, "input": payload}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "User-Agent": "ai-web3-school-cohort-0/0.1 (+learning-agent)",
        },
        method="POST",
    )
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fmt_cn(iso: str) -> str:
    if not iso:
        return "?"
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(CN_TZ)
    return dt.strftime("%m-%d %a %H:%M")


def main():
    now = datetime.now(timezone.utc)
    rng_start = (now - timedelta(days=1)).isoformat().replace("+00:00", "Z")
    rng_end = (now + timedelta(days=21)).isoformat().replace("+00:00", "Z")

    events = call(
        "events.listForLearner",
        {"programId": PROGRAM_ID, "rangeStart": rng_start, "rangeEnd": rng_end},
    )
    tasks = call("tasks.listForLearner", {"programId": PROGRAM_ID})

    if not events.get("ok"):
        sys.exit(f"events error: {events}")
    if not tasks.get("ok"):
        sys.exit(f"tasks error: {tasks}")

    items = events.get("result") or []
    items.sort(key=lambda e: e.get("startAt") or "")
    print(f"Events in next 3 weeks: {len(items)}")
    for e in items:
        title = e.get("title") or "?"
        loc = e.get("location") or e.get("meetingUrlPrimary") or ""
        print(f"  {fmt_cn(e.get('startAt'))}  {title}  {loc[:50]}")

    print(f"\nLearner tasks: {len(tasks.get('result') or [])}")


if __name__ == "__main__":
    main()
