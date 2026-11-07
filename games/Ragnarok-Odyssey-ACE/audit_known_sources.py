#!/usr/bin/env python3
"""Audit known Ragnarok Odyssey ACE source rows against the cumulative translations.

Requires an original-source JSON array (e.g. NPC_SOURCE_5403-6138.json) and
translations/current.json. Source text stays local; report only IDs and counts.
This does not claim a complete game QA or verify PS3 font/rendering.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import unicodedata

TAG = re.compile(r"\{#\d+\}")
PRINTF = re.compile(r"(?<![0-9])%(?:\d+\$)?[-+ #0]*(?:\d+|\*)?(?:\.(?:\d+|\*))?[hlLzjt]*[diuoxXfFeEgGaAcsp%]")
NUM = re.compile(r"\d+")


def display_line_length(line: str) -> int:
    return len(TAG.sub("", line))


def compare(row: dict, target: str) -> list[str]:
    problems: list[str] = []
    ident, file, idx = row.get("id"), row.get("file"), row.get("index")
    source = row.get("source")
    source_tagged = row.get("source_tagged")
    if not isinstance(ident, str) or ident != f"{file}::{idx}":
        return ["invalid_source_id"]
    if not isinstance(source, str) or not isinstance(source_tagged, str):
        return ["missing_source_string"]
    if hashlib.sha256(source.encode("utf-8")).hexdigest() != row.get("source_sha256"):
        problems.append("source_sha256_mismatch")
    if not isinstance(target, str) or not target.strip():
        return problems + ["missing_target"]
    if Counter(TAG.findall(source_tagged)) != Counter(TAG.findall(target)):
        problems.append("color_tags_mismatch")
    if TAG.sub("", target).find("{#") >= 0:
        problems.append("malformed_color_tag")
    if PRINTF.findall(source_tagged) != PRINTF.findall(target):
        problems.append("printf_mismatch")
    if Counter(NUM.findall(TAG.sub("", source_tagged))) != Counter(NUM.findall(TAG.sub("", target))):
        problems.append("numbers_mismatch")
    if "\r" in target or "\x00" in target:
        problems.append("invalid_control_char")
    if target != unicodedata.normalize("NFC", target):
        problems.append("not_nfc")
    if file.endswith("msg_npc_talk.bin"):
        if len(target.split("\n")) > 3:
            problems.append("npc_more_than_3_lines")
        if any(display_line_length(line) > 38 for line in target.split("\n")):
            problems.append("npc_line_over_38_chars")
    return problems


def audit(rows: list[dict], mapping: dict) -> dict:
    entries = mapping.get("entries")
    if not isinstance(entries, dict) or len(entries) != mapping.get("count"):
        raise ValueError("Invalid cumulative mapping")
    seen = set()
    issues = []
    table_counts = Counter()
    for row in rows:
        ident = row.get("id")
        if ident in seen:
            issues.append({"id": ident, "issue": "duplicate_source_id"})
            continue
        seen.add(ident)
        table_counts[str(row.get("file"))] += 1
        target = entries.get(ident)
        for problem in compare(row, target):
            issues.append({"id": ident, "issue": problem})
    whole = {"empty": 0, "malformed_color_tag": 0, "control_char": 0, "non_nfc": 0, "over_38_any_table_review_only": 0}
    by_table = Counter()
    for key, target in entries.items():
        table = key.split("::")[-2] if "::" in key else "unknown"
        by_table[table] += 1
        if not isinstance(target, str) or not target.strip():
            whole["empty"] += 1
            continue
        if "{#" in TAG.sub("", target):
            whole["malformed_color_tag"] += 1
        if "\x00" in target or "\r" in target:
            whole["control_char"] += 1
        if target != unicodedata.normalize("NFC", target):
            whole["non_nfc"] += 1
        if any(display_line_length(line) > 38 for line in target.split("\n")):
            whole["over_38_any_table_review_only"] += 1
    return {
        "kind": "KNOWN_SOURCE_QA_NOT_NEW_TRANSLATIONS",
        "known_source_records_checked": len(rows),
        "unique_source_records": len(seen),
        "matched_with_cumulative": sum(1 for row in rows if row.get("id") in entries),
        "source_target_issue_count": len(issues),
        "source_target_issues": issues,
        "known_source_tables": dict(table_counts),
        "cumulative_count": len(entries),
        "cumulative_global_checks": whole,
        "cumulative_table_counts": dict(by_table),
        "interpretation": "38-character warnings across non-NPC tables require in-game layout review. This is not a complete original-source validator or runtime rendering test."
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--current", type=Path, required=True)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--report", type=Path, required=True)
    a = p.parse_args()
    if a.report.exists():
        p.error("Report already exists; refusing overwrite")
    rows = json.loads(a.source.read_text(encoding="utf-8-sig"))
    mapping = json.loads(a.current.read_text(encoding="utf-8-sig"))
    if not isinstance(rows, list):
        p.error("Original source must be a JSON array")
    report = audit(rows, mapping)
    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Known source rows:", report["known_source_records_checked"])
    print("Matched:", report["matched_with_cumulative"])
    print("Source-target issues:", report["source_target_issue_count"])
    print("Cumulative mapping:", report["cumulative_count"])
    print("Report:", a.report)
    return 0 if report["source_target_issue_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())