#!/usr/bin/env python3
"""Prepare batch BV from the original Ragnarok Odyssey ACE handoff archive.

Only selects original pending records missing from current.json.
The output contains copyrighted English source and MUST remain local.
Example:
  python prepare_batch_bv.py --archive RagnarokACE-BanGiaoDich-2026-11-04.zip \
    --current translations/current.json --output pending-BV.local.json
"""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

PRIORITY = {
    "msg_quest.bin": 0,
    "dc_db_text_word.rmsg": 1,
    "dc_db_text_reward.rmsg": 2,
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--current", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("pending-BV.local.json"))
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Refusing to overwrite " + str(args.output))
    with ZipFile(args.archive) as archive:
        matches = [n for n in archive.namelist()
                   if n.endswith("01_CAN_DICH/needs_translation.json")]
        if len(matches) != 1:
            raise ValueError("Expected exactly one original needs_translation.json")
        records = json.loads(archive.read(matches[0]).decode("utf-8-sig"))
    snap = json.loads(args.current.read_text(encoding="utf-8-sig"))
    entries = snap.get("entries")
    if not isinstance(records, list) or not isinstance(entries, dict):
        raise ValueError("Invalid source list or current.json entries")
    if snap.get("count") != len(entries):
        raise ValueError("current.json count does not match entries")
    seen = set()
    pending = []
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Invalid source record")
        ident = record.get("id")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise ValueError("Missing or duplicate source ID: " + str(ident))
        seen.add(ident)
        source = record.get("source")
        if not isinstance(source, str) or hashlib.sha256(
                source.encode("utf-8")).hexdigest() != record.get("source_sha256"):
            raise ValueError("Source SHA-256 mismatch: " + ident)
        if record.get("status") == "needs_translation" and ident not in entries:
            pending.append(record)
    def order(record):
        name = str(record.get("file", "")).split("::")[-1]
        return (PRIORITY.get(name, 3), str(record.get("file", "")),
                int(record.get("index") or 0), record["id"])
    pending.sort(key=order)
    by_file = Counter(str(r.get("file", "")).split("::")[-1] for r in pending)
    result = {
        "batch": "BV",
        "kind": "LOCAL_SOURCE_PENDING_NOT_TRANSLATED",
        "archive": args.archive.name,
        "translated_count": len(entries),
        "pending_count": len(pending),
        "priority_counts": {name: by_file.get(name, 0) for name in PRIORITY},
        "by_file": dict(sorted(by_file.items())),
        "warning": "Original English game text. Never commit this output to public GitHub.",
        "records": pending,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
    print("Current:", len(entries), "| Pending:", len(pending))
    print("Priority:", result["priority_counts"])
    print("Saved local source worklist:", args.output)

if __name__ == "__main__":
    main()
