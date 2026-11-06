#!/usr/bin/env python3
"""Extract untranslated Batch Z source IDs from the original handoff ZIP.

This script generates a LOCAL English source worklist only; it never changes
translations/current.json, and it never invents translations.

Usage:
 python prepare_batch_z.py \
   --archive RagnarokACE-BanGiaoDich-2026-11-04.zip \
   --current translations/current.json \
   --output pending-Z.local.json --limit 500

Do not commit pending-Z.local.json: it contains original game dialogue.
"""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

GROUPS = ("npc", "weapon_name", "weapon_text", "myorder")
QUOTAS = {"npc": 100, "weapon_name": 150, "weapon_text": 150, "myorder": 100}


def classify(row, npc_start):
    table = str(row.get("file", "")).split("::")[-1]
    index = row.get("index")
    if table == "msg_npc_talk.bin" and isinstance(index, int) and index >= npc_start:
        return "npc"
    if table.startswith("it_db_name_weapon"):
        return "weapon_name"
    if table.startswith("it_db_text_weapon"):
        return "weapon_text"
    if table.startswith("it_db_name_myorder"):
        return "myorder"
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--current", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=Path("pending-Z.local.json"))
    parser.add_argument("--limit", type=int, default=500)
    parser.add_argument("--npc-start", type=int, default=3958)
    args = parser.parse_args()

    if args.limit <= 0:
        parser.error("--limit must be positive")
    if args.output.exists():
        parser.error("Refusing to overwrite: " + str(args.output))
    with ZipFile(args.archive) as archive:
        names = [n for n in archive.namelist() if n.endswith("/needs_translation.json")]
        if len(names) != 1:
            raise ValueError(f"Expected one needs_translation.json, got {names}")
        records = json.loads(archive.read(names[0]))
    if not isinstance(records, list):
        raise ValueError("needs_translation.json must contain a list")
    current = json.loads(args.current.read_text(encoding="utf-8"))
    translated = current.get("entries")
    if not isinstance(translated, dict) or len(translated) != current.get("count"):
        raise ValueError("Invalid snapshot count/entries; refusing to proceed")

    pending = {name: [] for name in GROUPS}
    source_ids = set()
    for row in records:
        key = row.get("id")
        if not isinstance(key, str) or not key:
            raise ValueError("Source has an invalid ID")
        if key in source_ids:
            raise ValueError("Duplicate source ID: " + key)
        source_ids.add(key)
        if key in translated:
            continue
        bucket = classify(row, args.npc_start)
        if bucket:
            pending[bucket].append(row)
    for name in GROUPS:
        pending[name].sort(key=lambda r: (r["file"], int(r["index"])))

    chosen, selected_ids = [], set()
    for name in GROUPS:
        for row in pending[name][:min(QUOTAS[name], args.limit - len(chosen))]:
            chosen.append(row)
            selected_ids.add(row["id"])
    for name in GROUPS:
        for row in pending[name]:
            if len(chosen) >= args.limit:
                break
            if row["id"] not in selected_ids:
                chosen.append(row)
                selected_ids.add(row["id"])
    assert len(chosen) == len(selected_ids)
    assert not (selected_ids & set(translated))

    worklist = {
        "batch": "Z",
        "kind": "local_source_worklist_NOT_TRANSLATED",
        "source_archive": args.archive.name,
        "current_count": len(translated),
        "npc_start": args.npc_start,
        "available_by_group": {name: len(pending[name]) for name in GROUPS},
        "selected_count": len(chosen),
        "warning": "Original game text for local translation only; do not commit to GitHub.",
        "rows": chosen,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(worklist, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Current translations:", len(translated))
    print("Available:", worklist["available_by_group"])
    print("New source IDs for Z:", len(chosen))
    print("Output:", args.output)


if __name__ == "__main__":
    main()
