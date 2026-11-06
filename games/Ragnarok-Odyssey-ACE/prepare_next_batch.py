#!/usr/bin/env python3
"""Prepare 500+ consecutive, untranslated Ragnarok Odyssey ACE NPC entries.

Only uses the user's locally available original handoff archive.
Never commits original English strings or changes translations/current.json.

Example:
 python prepare_next_batch.py \
   --archive RagnarokACE-BanGiaoDich-2026-11-04.zip \
   --current translations/current.json \
   --npc-start 5403 --limit 500 --output pending-AT.local.json
"""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

NPC = "menu.cpk::msg_field.en.pac::msg_npc_talk.bin"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--archive", required=True, type=Path)
    p.add_argument("--current", required=True, type=Path)
    p.add_argument("--npc-start", type=int, default=5403)
    p.add_argument("--limit", type=int, default=500)
    p.add_argument("--batch", default="AT")
    p.add_argument("--output", type=Path, default=Path("pending-AT.local.json"))
    args = p.parse_args()
    if not (1 <= args.limit <= 2000) or args.npc_start < 0:
        p.error("limit must be 1..2000 and npc-start must be >= 0")
    if args.output.exists():
        p.error("Refusing to overwrite existing file: " + str(args.output))
    with ZipFile(args.archive) as z:
        found = [name for name in z.namelist()
                 if name.endswith("01_CAN_DICH/needs_translation.json")]
        if len(found) != 1:
            raise ValueError("Expected one needs_translation.json in handoff ZIP")
        rows = json.loads(z.read(found[0]).decode("utf-8-sig"))
    if not isinstance(rows, list):
        raise ValueError("Original worklist is not an array")
    snapshot = json.loads(args.current.read_text(encoding="utf-8-sig"))
    translations = snapshot.get("entries")
    if not isinstance(translations, dict) or (
            "count" in snapshot and snapshot["count"] != len(translations)):
        raise ValueError("Invalid current.json; no file has been changed")
    seen = set()
    pending = []
    for row in rows:
        ident = row.get("id")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise ValueError("Missing or duplicate original ID: " + str(ident))
        seen.add(ident)
        if ident in translations or row.get("status") != "needs_translation":
            continue
        if (row.get("file") != NPC or
                not isinstance(row.get("index"), int) or
                row["index"] < args.npc_start):
            continue
        if not isinstance(row.get("source_tagged"), str):
            raise ValueError("Missing original source: " + ident)
        pending.append(row)
    pending.sort(key=lambda r: r["index"])
    selected = pending[:args.limit]
    if not selected:
        raise ValueError("No untranslated NPCs found from this index")
    result = {
        "batch": args.batch,
        "kind": "LOCAL_SOURCE_ONLY_NOT_TRANSLATED",
        "source_archive": args.archive.name,
        "current_count": len(translations),
        "untranslated_npc_available": len(pending),
        "selected_count": len(selected),
        "npc_range": [selected[0]["index"], selected[-1]["index"]],
        "warning": "Local English game text: do not push this worklist to GitHub.",
        "rows": [
            {key: r.get(key) for key in
             ("id", "file", "index", "source", "source_tagged",
              "attributes", "source_sha256")}
            for r in selected
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print("Translated:", len(translations))
    print("Available NPC:", len(pending))
    print("Prepared:", len(selected), "from", *result["npc_range"])
    print("Source-only local worklist:", args.output)


if __name__ == "__main__":
    main()
