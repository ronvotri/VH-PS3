# Ragnarok Odyssey ACE — AY: kiểm tra nguồn và chất lượng (07/11/2026)

> **Trạng thái:** AY chưa có câu dịch mới; **19.161 / 25.288 (75,77%)** vẫn là mốc hợp nhất. Không tăng tiến độ khi chưa đọc được câu gốc còn thiếu.

## Các phép kiểm tra đã hoàn thành

| Bộ dữ liệu | Số mục | Kết quả | Phạm vi |
|---|---:|---|---|
| `NPC_SOURCE_5403-6138.json` (chỉ nguồn lưu ngoài repo) | 733 | PASS 733/733 | SHA-256 nguồn; tất cả ID có trong bản hợp nhất; giữ mã tô màu và số; không vượt 3 dòng hoặc 38 ký tự/dòng đối với thoại NPC |
| AW + AX `completed_*.json` (chỉ dữ liệu kiểm thử cục bộ) | 784 | PASS 784/784 | ID, SHA-256, màu `{#n}`, printf, số, NFC, mã điều khiển, bản dịch không rỗng |
| `translations/current.json` (toàn bộ repo) | 19.161 | 0 lỗi cơ bản | Không có chuỗi rỗng, thẻ màu sai cú pháp, CR/NUL hoặc chuỗi chưa chuẩn NFC |

**Tổng cộng: 1.517 mục có cặp nguồn–dịch được kiểm tra**, thuộc các nhóm NPC và nhiệm vụ; không đồng nghĩa toàn bộ 19.161 mục đã qua đối chiếu nguồn. Các bản dịch AW+AX đã nằm trong repo từ các commit trước; **không cộng lại**.

### Danh sách cần kiểm tra hiển thị

Quét tĩnh trên toàn bộ bản hợp nhất phát hiện **141 chuỗi có ít nhất một dòng dài hơn 38 ký tự hiển thị**. Đây là **ứng viên cần xem lại**, không được tự động coi là lỗi, vì khung tutorial, thẻ bài và mô tả nhiều dòng có giới hạn khác NPC.

Một vài ID ưu tiên kiểm thử trên RPCS3:

- `menu.cpk::msg_common.en.pac::msg_common.bin::78` — 53 ký tự.
- `menu.cpk::msg_field.en.pac::msg_shop.bin::212` — 51 ký tự.
- `menu.cpk::msg_field.en.pac::msg_yggdrasill.bin::19` — 52 ký tự.
- `item.cpk::it_db.en.pac::it_db_text_card.rmsg::109` — 57 ký tự.

Chưa tự sửa hoặc chèn xuống dòng vì chưa xác minh giới hạn thật trên từng màn hình.

## Vì sao chưa tạo bản dịch AY?

- Đã xác nhận **784/784** mục nguồn từ cầu nối AV→AW→AX đều có bản dịch.
- Đã xác nhận **733/733** NPC trong nguồn độc lập đều có bản dịch.
- Dữ liệu chưa dịch còn lại: **2.488** mục theo bản bàn giao trước.
- Thư viện liệt kê ZIP gốc `RagnarokACE-BanGiaoDich-2026-11-04.zip` (29,6 MB), nhưng bộ truy cập tệp trả về cảnh báo không có đường dẫn đọc raw-byte được cấp quyền. Không thể trích đúng `01_CAN_DICH/needs_translation.json` từ ZIP trong phiên này.
- Không tạo nguồn English giả, không dịch từ ID đoán mò, không sửa `translations/current.json` và không ghi nguồn gốc lên GitHub.

## Công cụ QA kèm theo

- `audit_known_sources.py` đối chiếu bản gộp với các bản ghi nguồn đã có, giữ nguồn gốc cục bộ; chỉ xuất báo cáo thống kê và ID lỗi.
- `test_audit_known_sources.py`: kiểm thử tự động **5/5 PASS** bằng dữ liệu tổng hợp.
- Đã chạy công cụ trên **784** bản ghi AW+AX có nguồn và bản dịch: **PASS 784/784**.
- `prepare_batch_ay.py` (commit trước) sẵn sàng tạo tối đa 500 mục nguồn mới nếu ZIP gốc được truy cập.

### Tiếp tục AY

Khi mở được ZIP gốc hoặc `needs_translation.json`, lọc các ID chưa có trong `translations/current.json` bằng `prepare_batch_ay.py`, dịch đủ ngữ cảnh và QA theo nguồn, sau đó commit delta AY cùng README, glossary và checkpoint mới. Chỉ khi có bản dịch mới đã kiểm định mới tăng tổng 19.161.

**Chưa chạy full `validate_return.py` của bộ nguồn và chưa thử font/render trên PS3 hoặc RPCS3.**

Credit: **Việt hóa bởi Votri Valley.**