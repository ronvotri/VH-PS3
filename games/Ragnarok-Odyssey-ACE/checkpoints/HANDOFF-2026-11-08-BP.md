# Ragnarok Odyssey ACE — Bàn giao checkpoint BP (08/11/2026)

## Trạng thái
- Đã đưa đủ 7 checkpoint BJ–BP lên GitHub, tổng **770 bản dịch**.
- **Chưa** hợp nhất vào `translations/current.json`: con số này là *pending* và không được cộng vào số mục đã hợp nhất trong README cho đến khi kiểm tra xung đột.
- Không trùng ID giữa bảy checkpoint. Nội dung dịch đã đối chiếu với nguồn `RagnarokACE-BanGiaoDich-2026-11-04.zip` (field `source_tagged`).
- Chưa kiểm thử hiển thị/phông chữ và kịch bản thực tế trên PS3.

| Checkpoint | Số mục | Phạm vi | Đường dẫn |
|---|---:|---|---|
| BJ | 40 | NPC tiểu sử 122–161 | `2026-11-08-batch-40-BJ.json` |
| BK | 32 | NPC tiểu sử 162–193 | `2026-11-08-batch-32-BK.json` |
| BL | 59 | Hội thoại 5301–5360; thiếu ID 5347 trong nguồn | `2026-11-08-batch-59-BL.json` |
| BM | 60 | Hội thoại 5361–5420 | `2026-11-08-batch-60-BM.json` |
| BN | 180 | Hội thoại 5421–5600 | `2026-11-08-batch-180-BN.json` |
| BO | 200 | Hội thoại 5601–5800 | `2026-11-08-batch-200-BO.json` |
| BP | 199 | Hội thoại 5801–6000; thiếu ID 5901 trong nguồn | `2026-11-08-batch-199-BP.json` |

## Chú ý quan trọng khi hợp nhất
1. Dùng `translations/current.json` làm bản chính. Với mỗi ID: nếu chưa có, bổ sung; nếu đã có cùng target thì bỏ qua; nếu đã có khác target, tạo báo cáo xung đột, **không ghi đè**.
2. BL và BM đã lấy từ bản sửa token trong gói BN (19 mục sửa). **Không** thay bằng ZIP BL/BM ban đầu.
3. BJ và BK được ngắt dòng lại (tối đa 37 ký tự/dòng cho tiểu sử), BM tối đa 50 ký tự/dòng cho hội thoại. Các hộp thoại BL, BN, BO, BP đã kiểm tra tối đa 3 dòng / 52 ký tự/dòng.
4. Kiểm tra token `{#0}`, `{#1}`, mã printf và bảo toàn metadata nguồn trước khi dựng patch.
5. Kiểm thử giao diện PS3 và nội dung hiển thị trước khi đánh dấu hoàn tất.

## Đợt tiếp theo
- **BQ:** tiếp từ hội thoại NPC **6001**, trừ ID đã có trong `current.json` hoặc không nằm trong danh sách cần dịch.
