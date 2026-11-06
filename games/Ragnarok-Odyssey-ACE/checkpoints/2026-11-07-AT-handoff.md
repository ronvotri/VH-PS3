# Ragnarok Odyssey ACE — Bàn giao đợt AT (07/11/2026)

## Đã hoàn thành
- Dịch **500 NPC mới**, ID **5403–5909**, lưu `checkpoints/2026-11-07-batch-500-AT.json`.
- QA `validate_return.py` gốc với `all_records.json`: **PASS 500/500**. Mỗi câu tối đa 3 dòng, 38 ký tự Unicode/dòng; giữ nguyên ID, số và token.
- Bỏ qua **6 ID đã dịch**: 5601, 5605, 5670, 5679, 5684, 5689; ID 5901 không nằm trong danh sách cần dịch.
- `translations/current.json` cập nhật **17.377/25.288** mục (~68,7%). Danh sách cần dịch còn **4.272** mục. Không ghi đè dữ liệu cũ.
- Đã lưu gói ZIP `RagnarokACE-Checkpoint-AT-2026-11-07.zip` chứa nguồn và bản dịch có metadata (`completed_AT.json`), `delta_AT.json`, báo cáo QA, file để nhập lại và tệp nguồn NPC tiếp theo.

## Tiếp tục đợt AU
- Bắt đầu tại NPC **5910**. Trong gói checkpoint AT có `NPC_SOURCE_NEXT_5910-6138.json` gồm **227 mục nguồn** chưa dịch.
- Để làm đủ ~500 mục cho AU, sau NPC nên chọn thêm các bảng còn thiếu từ `01_CAN_DICH/needs_translation.json` trong ZIP gốc, không tự giả định ID liên tiếp.
- Dùng `translations/current.json` mới nhất trước khi dịch, kiểm trùng ID và QA token/printf/số với nguồn gốc.
- Ghi checkpoint riêng, hợp nhất GitHub và xác nhận lại SHA. Không commit ROM/ISO, văn bản tiếng Anh game gốc hoặc tệp nguồn game có bản quyền lên repo.

## Chưa xác nhận
- Chưa dựng patch hoặc kiểm thử chữ Việt và bố cục thật trong RPCS3/PS3; giới hạn 3 × 38 chỉ là kiểm tra tĩnh.
- Credit: **Việt hóa bởi Votri Valley.**

## Commits
- Checkpoint AT: `4cf8f9ed58639c0dbb6b0ef223f86b18448b2fe5`.
- Bản dịch hợp nhất AT: `cfe624a5a05ec4d4c27d7ddbaba58ace2b49df36`.
