# Ragnarok Odyssey ACE — Bàn giao đợt AV (07/11/2026)

## Đã hoàn tất

- **500 bản dịch mới**: 199 mô tả BGM trong `it_db_text_bgm.rmsg` (ID **38–236**) và 301 chuỗi `msg_quest.bin` (ID **221–521**).
- **18.377 / 25.288** chuỗi hợp nhất (**72,67%**). Còn **3.272** mục cần dịch trong danh sách 19.474 mục ban đầu.
- Delta tiếng Việt: `checkpoints/2026-11-07-batch-500-AV.json`.
- Bản hợp nhất: `translations/current.json`; không ghi đè khóa đã dịch ở các đợt trước.
- Kiểm chứng `validate_return.py` gốc dùng `02_TOAN_BO/all_records.json`: **PASS 500/500**, 0 lỗi ID, source, SHA, attributes, mã màu, printf và chữ số.
- Tối đa **38 ký tự/dòng**, mô tả nhạc tối đa 4 dòng, nhiệm vụ tối đa 5 dòng. Khác với quy định 3 dòng đối với NPC, lời giao nhiệm vụ được giữ đủ ý nghĩa gốc.
- Nhạc bản quyền thuộc các game liên quan vẫn ghi chính xác tên game, nhà soạn/phối nhạc và mã số bản nhạc.

## Tiếp tục đợt AW

- ZIP `RagnarokACE-Checkpoint-AV-2026-11-07.zip` lưu trong Library `/RagnarokACE/` và có `SOURCE_NEXT_AW.json` chứa **784 mục gốc** `msg_quest.bin` trong khoảng ID **522–1322**; không cần người dùng nộp lại ZIP nguồn.
- Đối chiếu snapshot hiện hành, lọc ID trùng, dịch theo từng nhóm UI/nhiệm vụ; có thể ưu tiên 500 mục cho đợt AW.
- Giữ nguyên chèn màu `{#0}`, `{#1}`, printf, số lượng, tên riêng. Kiểm tra trên `all_records.json` rồi mới cập nhật GitHub.
- Không tải lời thoại tiếng Anh gốc hoặc tài nguyên ROM/ISO lên GitHub; chỉ commit bản dịch tiếng Việt và checkpoint metadata.

## Lưu ý QA

- Đã kiểm tra dữ liệu/chuỗi, chưa có bản patch PS3 và **chưa kiểm thử font/render trên RPCS3 hoặc PS3**.
- Credit: **Việt hóa bởi Votri Valley.**

## Commits

- Delta AV: `39534d1f405d379bcbd0a8e03a0df176fb50549e`
- Hợp nhất AV: `6805559908dcc2d4ed35a8ac698297f46877470d`
