#!/usr/bin/env python3
"""Prepare the next original-source, not-yet-translated Ragnarok Odyssey ACE batch.

Offline-only; reads the owner's original handoff, never invents source text,
never edits existing translations, and refuses to overwrite output files.
The resulting *.local.json contains original English game text and must NOT
be committed to GitHub. The metadata-only report is safe to commit.

Examples (from games/Ragnarok-Odyssey-ACE/):
  python prepare_batch_ay.py \
    --archive /path/to/RagnarokACE-BanGiaoDich-2026-11-04.zip \
    --current translations/current.json \
    --output pending-AY.local.json \
    --report checkpoints/2026-11-07-AY-source-inventory.json

  python prepare_batch_ay.py \
    --needs /path/to/01_CAN_DICH/needs_translation.json \
    --current translations/current.json --limit 500 \
    --output pending-AY.local.json

A machine-readable source worklist is NOT a translation checkpoint. It must be
reviewed and translated before creating a delta or updating current.json.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
import pathlib
import sys
import zipfile
from typing import Any


def load_worklist(archive: pathlib.Path | None, needs: pathlib.Path | None) -> list[dict[str, Any]]:
    if archive is not None:
        if not archive.is_file():
            raise ValueError(f"Original archive not accessible: {archive}")
        with zipfile.ZipFile(archive) as z:
            found = [name for name in z.namelist()
                     if name.endswith("01_CAN_DICH/needs_translation.json")]
            if len(found) != 1:
                raise ValueError("Expected exactly one 01_CAN_DICH/needs_translation.json in ZIP")
            contents = z.read(found[0])
    else:
        assert needs is not None
        contents = needs.read_bytes()
    rows = json.loads(contents.decode("utf-8-sig"))
    if not isinstance(rows, list):
        raise ValueError("Original needs_translation.json must be a JSON array")
    return rows


def load_mapping(path: pathlib.Path) -> dict[str, str]:
    snapshot = json.loads(path.read_text(encoding="utf-8-sig"))
    mapping = snapshot.get("entries")
    if not isinstance(mapping, dict) or snapshot.get("count") != len(mapping):
        raise ValueError("Invalid current.json count or entries; refusing to continue")
    if any(not isinstance(k, str) or not isinstance(v, str) or not v.strip()
           for k, v in mapping.items()):
        raise ValueError("Invalid translated entry in current.json")
    return mapping


def validate_original(row: dict[str, Any]) -> None:
    if not isinstance(row, dict):
        raise ValueError("Original source contains non-object record")
    key, tab, idx = row.get("id"), row.get("file"), row.get("index")
    if not isinstance(key, str) or not isinstance(tab, str) or not isinstance(idx, int):
        raise ValueError(f"Missing ID, file, or index: {key!r}")
    if key != f"{tab}::{idx}":
        raise ValueError(f"Mismatched ID/file/index: {key}")
    if row.get("status") != "needs_translation":
        raise ValueError(f"Unexpected source status for {key}")
    if not isinstance(row.get("source"), str) or not isinstance(row.get("source_tagged"), str):
        raise ValueError(f"Missing original source strings: {key}")
    digest = hashlib.sha256(row["source"].encode("utf-8")).hexdigest()
    if digest != row.get("source_sha256"):
        raise ValueError(f"Original source SHA-256 mismatch: {key}")
    if not isinstance(row.get("attributes"), list):
        raise ValueError(f"Missing attributes list: {key}")


def create_batch(rows: list[dict[str, Any]], mapping: dict[str, str], limit: int,
                 table: str = "") -> tuple[dict[str, Any], dict[str, Any]]:
    if not 1 <= limit <= 2000:
        raise ValueError("--limit must be between 1 and 2000")
    seen: set[str] = set()
    pending: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    already = 0
    for row in rows:
        validate_original(row)
        key = row["id"]
        if key in seen:
            raise ValueError(f"Duplicate original ID: {key}")
        seen.add(key)
        if key in mapping:
            already += 1
        elif not table or table in row["file"]:
            pending[row["file"]].append(row)
    for group in pending.values():
        group.sort(key=lambda r: (r["index"], r["id"]))
    # Batch dense tables together to preserve context, instead of selecting
    # arbitrary source IDs across unrelated files. Tie-break lexicographically.
    sorted_groups = sorted(pending, key=lambda key: (-len(pending[key]), key))
    chosen: list[dict[str, Any]] = []
    for tab in sorted_groups:
        chosen.extend(pending[tab][:max(0, limit - len(chosen))])
        if len(chosen) == limit:
            break
    counts = {k: len(pending[k]) for k in sorted_groups}
    report = {
        "batch": "AY",
        "kind": "SOURCE_INVENTORY_ONLY_NOT_TRANSLATED",
        "original_worklist_count": len(rows),
        "translated_from_original_worklist": already,
        "current_snapshot_count": len(mapping),
        "still_pending_in_original_worklist": sum(counts.values()),
        "selected_count": len(chosen),
        "table_filter": table or None,
        "remaining_by_table": counts,
        "selected_by_table": dict(collections.Counter(x["file"] for x in chosen)),
        "selected_ids": [x["id"] for x in chosen],
        "note": "Only IDs/metadata. Do not report these as translations or increase the translated count."
    }
    work = {
        "batch": "AY",
        "kind": "LOCAL_ORIGINAL_SOURCE_NOT_TRANSLATED",
        "current_snapshot_count": len(mapping),
        "selected_count": len(chosen),
        "warning": "Contains original English game text; NEVER commit to repository.",
        "rows": chosen,
    }
    return work, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--archive", type=pathlib.Path, help="Unmodified original 04/11 handoff ZIP")
    source.add_argument("--needs", type=pathlib.Path, help="Extracted original needs_translation.json")
    parser.add_argument("--current", type=pathlib.Path,
                        default=pathlib.Path("translations/current.json"))
    parser.add_argument("--limit", type=int, default=500)
    parser.add_argument("--table", default="", help="Optional substring filter for source table path")
    parser.add_argument("--output", type=pathlib.Path, required=True,
                        help="Local-only output, e.g. pending-AY.local.json")
    parser.add_argument("--report", type=pathlib.Path, help="Optional metadata-only summary")
    args = parser.parse_args()
    if args.output.exists() or (args.report is not None and args.report.exists()):
        parser.error("Refusing to overwrite an existing output/report")
    if args.report is not None and args.report.resolve() == args.output.resolve():
        parser.error("Report and original-source worklist must have different paths")
    try:
        rows = load_worklist(args.archive, args.needs)
        mapping = load_mapping(args.current)
        work, report = create_batch(rows, mapping, args.limit, args.table)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, json.JSONDecodeError) as exc:
        parser.exit(2, f"FAILED: {exc}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as fh:
        json.dump(work, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    if args.report is not None:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("x", encoding="utf-8") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
    print("Current translations:", len(mapping))
    print("Missing source rows:", report["still_pending_in_original_worklist"])
    print("Selected original rows for AY:", report["selected_count"])
    print("Source worklist (local only):", args.output)
    if args.report:
        print("Metadata summary:", args.report)
    return 0


if __name__ == "__main__":
    sys.exit(main())