# Ragnarok Odyssey ACE — Đợt BD (07/11/2026)

## Tổng quan
- Tiếp tục từ checkpoint BC trên nhánh `main`.
- **14 câu NPC đã Việt hóa được hiệu đính**, không có bản dịch ID mới.
- Bản hợp nhất `translations/current.json`: **19.161 / 25.288** ID (**75,77%**), số mục chưa dịch do checkpoint cũ báo **2.488** (chưa xác minh lại bằng danh sách nguồn gốc).
- Nguồn đối chiếu: `NPC_SOURCE_5403-6138.json` chứa **733 dòng nguồn**, đã kiểm tra mã SHA-256 **733/733**.

## Các sửa đổi
- Khôi phục các tên bị lược trong thoại: `Chúa Tể Tử Thần`, `Loli Ruri`, `Thrymheim`.
- Hiệu chỉnh ngữ nghĩa: mô tả thế hệ khổng lồ/Thiazi, cách đánh phá giáp, lời báo cáo chiến trường, bảo vệ pháo đài và hướng dẫn mở rộng trang phục.
- Tinh chỉnh diễn đạt và giữ giọng nhân vật của các NPC.

**ID NPC đã sửa:** `5434, 5447, 5477, 5486, 5497, 5531, 5559, 5564, 5580, 5650, 5713, 5755, 5783, 6074`.

## QA kỹ thuật
- 14/14 mục so với source tiếng Anh theo ID và `source_sha256` trong bộ 733 mục.
- Giữ mã `{#n}`/printf, số và số dòng cũ; tối đa 38 ký tự hiển thị/dòng.
- Bản hợp nhất 19.161 mục không có giá trị rỗng, NUL/CR, sai NFC, ID trùng hoặc dòng vượt 38 ký tự theo bộ quét tĩnh.
- **Chưa thử hiển thị thực tế** trên PS3/RPCS3, **chưa chạy validator gốc** do nguồn ZIP không trích được.
- Delta: [2026-11-07-BD-semantic-revisions.json](2026-11-07-BD-semantic-revisions.json)
- QA: [2026-11-07-BD-QA.json](2026-11-07-BD-QA.json)

## Tiếp tục dịch ID mới
Tệp `RagnarokACE-BanGiaoDich-2026-11-04.zip` (29.607.145 bytes) vẫn có ở Library nhưng lệnh materialize báo không có đường cấp phép truy cập byte gốc. Những tệp nguồn nhỏ hiện có chứa 733 NPC, đều đã dịch.

**Không dịch đoán 2.488 ID còn lại.** Cần bản có thể đọc của `01_CAN_DICH/needs_translation.json` (tách khỏi ZIP gốc) rồi dùng `prepare_batch_bb.py` để chọn các ID thật sự còn trống, chạy QA và hợp nhất.

**Credit: Việt hóa bởi Votri Valley.**
