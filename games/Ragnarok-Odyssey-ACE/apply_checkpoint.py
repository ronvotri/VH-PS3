#!/usr/bin/env python3
# Merge the latest Ragnarok Odyssey ACE translations into a handoff JSON.
# Python 3.8+. Does not write to the game, rebuild assets, or distribute files.
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parent
TOKENS = re.compile(r"\{#\d+\}")
PRINTF = re.compile(
    r"(?<![0-9])%(?:\d+\$)?[-+ #0]*(?:\d+|\*)?"
    r"(?:\.(?:\d+|\*))?[hlLzjt]*[diuoxXfFeEgGaAcsp%]"
)


def check_value(row, new):
    src = row.get("source_tagged", "")
    if Counter(TOKENS.findall(src)) != Counter(TOKENS.findall(new)):
        return "attribute token mismatch"
    if re.search(r"\{#[^}]*\}", TOKENS.sub("", new)):
        return "malformed attribute token"
    if PRINTF.findall(src) != PRINTF.findall(new):
        return "printf mismatch"
    before = Counter(re.findall(r"\d+", TOKENS.sub("", src)))
    after = Counter(re.findall(r"\d+", TOKENS.sub("", new)))
    if before != after:
        return "number mismatch"
    if "\x00" in new or "\r" in new:
        return "invalid control character"
    return None


def main():
    parser = argparse.ArgumentParser(description="Apply a translation checkpoint safely.")
    parser.add_argument("--input", required=True, type=Path,
                        help="Original needs_translation.json from 04/11 handoff")
    parser.add_argument("--output", required=True, type=Path,
                        help="New output path; never overwrite source")
    parser.add_argument("--mapping", type=Path,
                        default=ROOT / "translations" / "current.json")
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error("--output must differ from --input")
    if args.output.exists():
        parser.error("Output exists; choose a new file to avoid overwriting it")

    mapping = json.loads(args.mapping.read_text(encoding="utf-8-sig"))
    entries = mapping["entries"]
    rows = json.loads(args.input.read_text(encoding="utf-8-sig"))
    if not isinstance(rows, list):
        parser.error("Input must be an array of translation records")
    seen, problems, applied, unchanged = set(), [], 0, 0
    for row in rows:
        ident = row.get("id")
        if ident in seen:
            problems.append(f"Duplicate ID: {ident}")
            continue
        seen.add(ident)
        if ident not in entries:
            continue
        if row.get("status") != "needs_translation":
            # Already-reviewed records are retained as supplied by the source.
            continue
        new = entries[ident]
        if not isinstance(new, str) or not new.strip():
            problems.append(f"Empty or non-string target: {ident}")
            continue
        new = unicodedata.normalize("NFC", new)
        error = check_value(row, new)
        if error:
            problems.append(f"{error}: {ident}")
            continue
        old = row.get("target_vi", "")
        if old:
            if old != new:
                problems.append(f"Conflicting translation, not overwritten: {ident}")
            else:
                unchanged += 1
        else:
            row["target_vi"] = new
            applied += 1

    if problems:
        print("\n".join(problems[:40]), file=sys.stderr)
        raise SystemExit(f"FAILED: {len(problems)} validation problems")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
    not_in_input = len(set(entries) - seen)
    print(f"PASS: {applied} new; {unchanged} already present; "
          f"{not_in_input} map IDs absent from input (normal for reviewed records).")
    print(f"Saved: {args.output}")
    print("Next: run the handoff's validate_return.py and test game runtime.")


if __name__ == "__main__":
    main()
