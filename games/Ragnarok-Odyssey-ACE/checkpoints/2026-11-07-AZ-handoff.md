# Ragnarok Odyssey ACE — Đợt AZ (07/11/2026)

## Nội dung
- Rà soát và rút gọn **39 chuỗi giao diện đã Việt hóa** ở 9 bảng: `msg_common`, `msg_savedata`, `msg_field`, `msg_shop`, `msg_dialog`, `msg_load_tips_message`, `msg_room`, `msg_yggdrasill`, `msg_history`.
- Chỉ sửa câu dịch hiện có; **không thêm nguồn ID**. Tổng bản hợp nhất vẫn là **19.161 / 25.288**, với **2.488 mục** trong danh sách gốc cần dịch.
- Delta: `checkpoints/2026-11-07-AZ-ui-revisions.json` và trạng thái QA: `checkpoints/2026-11-07-AZ-ui-QA.json`.
- Mọi câu sửa dài tối đa 38 ký tự hiển thị mỗi dòng. Không đổi thứ tự/multiplicity mã màu `{#n}`, mã printf hoặc dãy số. Không có ID trùng, giá trị rỗng, NUL/CR hoặc Unicode ngoài NFC.
- Những trường hợp giao diện cụ thể cần test trên RPCS3/PS3; chưa có patch và chưa test render thực tế.

## Nguồn
- ZIP bàn giao gốc `RagnarokACE-BanGiaoDich-2026-11-04.zip` (29,6 MB) vẫn liệt kê trong Library nhưng không cho trích xuất nội dung trong phiên hiện tại; **chưa có nguồn mới cho AY/AZ**.
- Đã có AV/AW/AX (1.517 mục nguồn QA) và NPC 5403–6138 (733 mục) đều được dịch, không tạo bản dịch đếm trùng.
- Còn **102/141 cảnh báo dài dòng** trong bản quét trước, phần nhiều thuộc mô tả kỹ năng/thẻ/cốt truyện; chưa tự rút ngắn khi chưa kiểm tra giới hạn khung giao diện từng bảng.
- Tiếp tục dịch mục mới từ `needs_translation.json` gốc khi có thể trích dữ liệu; khi đó phải đối chiếu `translations/current.json` và chạy bộ validator gốc.

**Credit: Việt hóa bởi Votri Valley.**