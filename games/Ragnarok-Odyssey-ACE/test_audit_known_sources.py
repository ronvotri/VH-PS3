import unittest
import hashlib
from audit_known_sources import audit, compare


def row(s, key="menu.cpk::msg_field.en.pac::msg_npc_talk.bin::5"):
    return {"id":key,"file":key.rsplit("::",1)[0],"index":int(key.rsplit("::",1)[1]),
            "source":s,"source_tagged":s,"source_sha256":hashlib.sha256(s.encode()).hexdigest()}


class AuditTests(unittest.TestCase):
    def test_valid_tokens_numbers_and_lines(self):
        self.assertEqual(compare(row("Get {#0}3 apples, %d!"),"Lấy {#0}3 táo, %d!"),[])

    def test_missing_markers_and_wrong_numbers(self):
        problems=compare(row("Get {#0}3 apples!"),"Lấy 5 táo!")
        self.assertIn("color_tags_mismatch",problems)
        self.assertIn("numbers_mismatch",problems)

    def test_tampered_source_is_rejected(self):
        data=row("Hello");data["source_sha256"]="0"*64
        self.assertIn("source_sha256_mismatch",compare(data,"Xin chào"))

    def test_npc_max_three_lines_and_display_width(self):
        problems=compare(row("Hello"),"a\nb\nc\nd")
        self.assertIn("npc_more_than_3_lines",problems)
        self.assertIn("npc_line_over_38_chars",compare(row("Hi"),"á"*39))

    def test_duplicate_id_and_count(self):
        r=row("Hello");mapping={"count":1,"entries":{r["id"]:"Xin chào"}}
        report=audit([r,r],mapping)
        self.assertEqual(report["matched_with_cumulative"],2)
        self.assertIn("duplicate_source_id",[x["issue"] for x in report["source_target_issues"]])


if __name__=="__main__":
    unittest.main()