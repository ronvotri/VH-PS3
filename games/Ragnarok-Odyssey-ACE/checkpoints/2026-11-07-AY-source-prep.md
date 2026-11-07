# Ragnarok Odyssey ACE — AY source recovery / preparation (07/11/2026)

## Verified state

- Last translation batch **AX** remains the current checkpoint: **19,161 / 25,288** translated (75.77%). The original worklist has **2,488 entries not yet translated**.
- All **784** `msg_quest.bin` source records in the AV → AW → AX bridge have already been translated. They must not be counted again.
- An independently preserved `NPC_SOURCE_5403-6138.json` contains **733** valid source records; all **733** IDs are already in `translations/current.json`. The record source SHA-256 validation passes on all 733.
- The original `RagnarokACE-BanGiaoDich-2026-11-04.zip` is listed in Library, but its raw bytes were not available to this run. No source rows for the 2,488 remaining entries could be extracted. **AY has 0 newly translated entries.**
- Original full validator `validate_return.py` has not been run on the AY source; PS3/RPCS3 rendering still untested.

## AY source extraction tool

Run `prepare_batch_ay.py` from `games/Ragnarok-Odyssey-ACE/` against the **unmodified original source archive** and the repo's latest `translations/current.json`:

```sh
python prepare_batch_ay.py \
  --archive /path/to/RagnarokACE-BanGiaoDich-2026-11-04.zip \
  --current translations/current.json \
  --limit 500 \
  --output pending-AY.local.json \
  --report AY-source-summary.local.json
```

If `needs_translation.json` has been extracted separately, pass `--needs /path/to/needs_translation.json` instead of `--archive`.

The tool checks IDs, original SHA-256 hashes and duplicates, skips IDs already in `current.json`, groups candidates by source table, and refuses to overwrite any file. A selectable `--table` filter can focus a particular `.rmsg` or `.bin` table after inspecting the inventory. `pending-AY.local.json` contains original game strings and **must remain local**; do not upload to GitHub. Worklist preparation is not translation and must not change the reported translated total.

Unit tests: `python test_prepare_batch_ay.py -v` (4/4 PASS). The extra 733-record real-source check also passed, confirming no missing untranslated entries in that already completed NPC subset.

## Next execution steps

1. Make the original ZIP (or extracted `needs_translation.json`) readable to the translation runtime.
2. Run `prepare_batch_ay.py` with the latest `translations/current.json`, producing up to 500 actually untranslated source rows.
3. Translate the selected rows manually, retaining IDs, numeric tokens, color tags, attributes and agreed terminology.
4. Run source, layout and full original validator checks before committing a **real** AY delta and merging it with the cumulative snapshot.

Project: BLUS31386. Credit: **Việt hóa bởi Votri Valley.**