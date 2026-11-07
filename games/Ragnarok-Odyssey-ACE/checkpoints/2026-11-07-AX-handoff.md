# Ragnarok Odyssey ACE — Bàn giao đợt AX (07/11/2026)

## Đã hoàn tất

- **284 mục** trong `msg_quest.bin` (ID 1039–1322), khép lại toàn bộ **784 mục nguồn** đã chuẩn bị từ AV cho AW+AX.
- Đã hợp nhất theo kế hoạch: **19.161 / 25.288** mục (**75,77%**). Còn **2.488** mục thuộc tập 19.474 mục ban đầu cần dịch.
- Delta cần đưa vào GitHub: `checkpoints/2026-11-07-batch-284-AX.json`; snapshot `translations/current.json`.
- 95 mục là tên riêng giữ nguyên (không tự ý dịch tên quái vật/NPC đã chuẩn hóa).
- Nhiệm vụ lặp theo cấp dùng cùng một bản dịch; 16 tên nhiệm vụ hậu tố `A` được lấy đúng tên nhiệm vụ đã dịch của bản gốc.
- QA nội bộ: SHA-256 chuỗi nguồn, ID, mã màu `{#...}`, chữ số, Unicode NFC, tối đa 38 ký tự hiển thị/dòng và tối đa 5 dòng: **PASS 284/284**.

## Chưa thực hiện

- Chưa có `02_TOAN_BO/all_records.json` nên **chưa chạy validator gốc**.
- Chưa tạo patch cho game và chưa kiểm thử font/bố cục trên RPCS3 hoặc PS3.

## Hướng tiếp tục AY

- Nguồn dành riêng cho AX trong checkpoint AW đã dịch hết: **không còn mục 1039–1322 chờ dịch**.
- Mở `RagnarokACE-BanGiaoDich-2026-11-04.zip` (hoặc dữ liệu nguồn đầy đủ đã lưu khác) để trích các mục `needs_translation` còn lại và trừ ID đã có trong `translations/current.json`.
- Giữ nguyên ID/attributes/source_sha256, mã màu, số liệu, không đè bản dịch trước và không commit chuỗi nguồn tiếng Anh từ ROM.

Credit: **Việt hóa bởi Votri Valley.**