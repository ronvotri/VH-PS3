# Ragnarok Odyssey ACE — BW catalog audit (08/11/2026)

## Result

This is a **static source catalog audit**, not a new translation batch.

- Original handoff ZIP: `RagnarokACE-BanGiaoDich-2026-11-04.zip`
- `02_TOAN_BO/all_records.json`: **25,288** original records and **25,288 distinct IDs**.
- `01_CAN_DICH/needs_translation.json`: **19,474** records, exactly those marked `needs_translation` in the original catalog.
- Previous BV checkpoint: **21,649** translation IDs (2,175 reviewed-base + 19,474 worklist records).
- **No additional translation IDs in BW**. Do not raise the translated total.

## Remaining 5,814 catalog entries outside the worklist

| Original status | Count | Action |
|---|---:|---|
| reviewed_translation | 2,175 | Already translated in the original reviewed base |
| filter_list_do_not_translate | 2,953 | **DO NOT TRANSLATE**: 2,225 banned names, 720 NG words, 8 ban strings; preserve online filtering |
| placeholder_do_not_translate | 118 | Reserved, dummy, unused and translation-not-required strings |
| symbols_numbers | 258 | Digits, punctuation, control markers |
| empty | 310 | Empty original strings |
| **Total** | **5,814** | |

## Integrity QA

- Source `id` uniqueness: **PASS 25,288/25,288**.
- Original `source_sha256` matches source text: **PASS 25,288/25,288**.
- Original worklist membership matches source status: **PASS 19,474/19,474**.
- Reviewed-base `target_vi` vs original **`source_tagged`**: **0 token mismatches, 0 printf mismatches, 0 Unicode NFC errors** in 2,175 entries.
- `source` is the stripped, display-oriented string: using it instead of `source_tagged` can falsely flag preserved formatting tokens as newly added.
- No game archive or patch has been built or tested on RPCS3/PS3.

## Next phase

Audit text beyond this catalog (textures, menus rendered as images, EBOOT, updates and DLC), patch only the user's lawful local game files and test text visibility/line wrapping/font on RPCS3/PS3. Keep the online blacklist untouched.

This audit **does not** establish that every game screen is localized. It establishes that the 5,814 non-worklist records have explicitly excluded statuses in the provided catalog.
