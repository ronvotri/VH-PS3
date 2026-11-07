#!/usr/bin/env python3
"""Prepare original-source, not-yet-translated Ragnarok Odyssey ACE rows.

Requires the original handoff ZIP and the *latest* current.json from GitHub.
Outputs a local-only worklist containing original English source text:
NEVER commit pending-BB.local.json to a public repository.
"""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from zipfile import ZipFile


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--archive", required=True, type=Path)
    p.add_argument("--current", required=True, type=Path)
    p.add_argument("--output", type=Path, default=Path("pending-BB.local.json"))
    p.add_argument("--limit", type=int, default=500)
    p.add_argument("--offset", type=int, default=0)
    a = p.parse_args()
    if not 1 <= a.limit <= 10000 or a.offset < 0:
        p.error("limit must be 1..10000 and offset must be >= 0")
    if a.output.exists():
        p.error("Refusing to overwrite: " + str(a.output))
    with ZipFile(a.archive) as z:
        files = [name for name in z.namelist()
                 if name.endswith("01_CAN_DICH/needs_translation.json")]
        if len(files) != 1:
            raise ValueError("Expected one original needs_translation.json")
        rows = json.loads(z.read(files[0]).decode("utf-8-sig"))
    snap = json.loads(a.current.read_text(encoding="utf-8-sig"))
    entries = snap.get("entries")
    if not isinstance(rows, list) or not isinstance(entries, dict) or (
            snap.get("count") != len(entries)):
        raise ValueError("Invalid source or current.json count")
    seen, pending = set(), []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Nonobject record in source")
        ident, src = row.get("id"), row.get("source")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise ValueError("Duplicate/missing source ID: " + str(ident))
        seen.add(ident)
        if not isinstance(src, str) or hashlib.sha256(
                src.encode("utf-8")).hexdigest() != row.get("source_sha256"):
            raise ValueError("Source SHA-256 mismatch: " + ident)
        if row.get("status") == "needs_translation" and ident not in entries:
            pending.append(row)
    chosen = pending[a.offset:a.offset + a.limit]
    if not chosen:
        raise ValueError("No source records in requested window")
    payload = {
        "batch": "BB",
        "kind": "LOCAL_PENDING_SOURCE_NOT_YET_TRANSLATED",
        "archive": a.archive.name,
        "current_count": len(entries),
        "source_worklist_total": len(rows),
        "pending_total": len(pending),
        "offset": a.offset,
        "selected_count": len(chosen),
        "warning": "Contains English game source: DO NOT COMMIT to public GitHub.",
        "by_file": dict(sorted(Counter(r.get("file", "UNKNOWN")
                                      for r in chosen).items())),
        "records": chosen,
    }
    a.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    print("Current:", len(entries), "| Pending:", len(pending),
          "| Selected:", len(chosen), "| Output:", a.output)


if __name__ == "__main__":
    main()
