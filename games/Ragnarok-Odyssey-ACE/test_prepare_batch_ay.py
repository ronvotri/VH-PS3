import hashlib
import importlib.util
import json
import pathlib
import tempfile
import unittest
import zipfile

ROOT = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("prepare_batch_ay", ROOT / "prepare_batch_ay.py")
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


def source_row(tab, idx, source):
    return {
        "id": f"{tab}::{idx}", "file": tab, "index": idx,
        "status": "needs_translation", "source": source,
        "source_tagged": source, "target_vi": "", "attributes": [],
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
    }


class BatchAYTests(unittest.TestCase):
    def test_skips_existing_and_selects_largest_group(self):
        t1 = "x::message_a.bin"
        t2 = "y::message_b.bin"
        rows = [source_row(t1, 1, "One"), source_row(t1, 2, "Two"),
                source_row(t1, 3, "Three"), source_row(t2, 0, "Other")]
        work, report = p.create_batch(rows, {rows[0]["id"]: "Một"}, 2)
        self.assertEqual([x["index"] for x in work["rows"]], [2, 3])
        self.assertEqual(report["still_pending_in_original_worklist"], 3)
        self.assertEqual(report["current_snapshot_count"], 1)

    def test_sha_and_duplicate_fail(self):
        row = source_row("x::t.bin", 1, "A")
        bad = {**row, "source_sha256": "0" * 64}
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            p.create_batch([bad], {}, 500)
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            p.create_batch([row, row], {}, 500)

    def test_real_zip_path_and_filter(self):
        with tempfile.TemporaryDirectory() as td:
            fn = pathlib.Path(td) / "source.zip"
            rows = [source_row("menu.cpk::test.bin", 1, "Text")]
            with zipfile.ZipFile(fn, "w") as z:
                z.writestr("project/01_CAN_DICH/needs_translation.json", json.dumps(rows))
            loaded = p.load_worklist(fn, None)
            work, report = p.create_batch(loaded, {}, 500, "test.bin")
            self.assertEqual(len(work["rows"]), 1)
            self.assertEqual(report["selected_count"], 1)

    def test_already_translated_has_zero_selected(self):
        row = source_row("menu.cpk::test.bin", 1, "Text")
        work, report = p.create_batch([row], {row["id"]: "Văn bản"}, 500)
        self.assertEqual(report["selected_count"], 0)
        self.assertEqual(work["rows"], [])


if __name__ == "__main__":
    unittest.main()