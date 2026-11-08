# Ragnarok Odyssey ACE — Bàn giao đợt BU, 08/11/2026

## Nội dung đã dịch

- 334 chuỗi chưa có trong `translations/current.json` tại mốc 21.055: 214 `dc_db_text_npc.rmsg` (ngày tháng Midgard, tên riêng, biệt danh), 102 `msg_savedata.bin` (sao lưu, khôi phục, Cross-Save), 9 `msg_room.bin` và 9 `msg_history.bin`.
- Tên riêng thần thoại như Odin, Frigg, Freyja, Thor giữ nguyên. `Unknown` thành `Chưa rõ`; ngày Midgard được viết `Năm Midgard` và giữ nguyên từng số.
- Thông báo Cross-Save giữ `PlayStation®Network`, `PlayStation®3`, `PlayStation®Vita`, số ô lưu, ID trực tuyến, số phút chờ, mọi token `{#N}`.
- Không thay 16 mục `msg_savedata.bin` đã có trên snapshot.

## Kiểm định

- Chạy `validate_return.py` nguyên bản từ ZIP nguồn với `02_TOAN_BO/all_records.json` gốc: **Validated 334 nonempty pending translations; 0 empty records**.
- 0 token / printf / chữ số / sai trường nguồn / ID trùng, tất cả Unicode NFC; độ dài dòng tối đa **46 ký tự** (kiểm tra tĩnh, không đo pixel).
- Không đóng bản vá, chưa kiểm thử thật trên RPCS3/PS3.

## Cách dùng

- `2026-11-08-batch-334-BU.json`: chỉ ánh xạ ID → bản dịch để hợp nhất vào `translations/current.json` bằng so khớp ID; không ghi đè ID cũ.
- `BU-completed.json`: 334 bản ghi nguồn đầy đủ với `target_vi`, cho kiểm tra lại bằng `validate_return.py` của ZIP nguồn.
- `2026-11-08-BU-QA.json`: báo cáo QA.
- `build_bu.py`: script tái tạo từ ZIP nguồn, gồm văn bản tiếng Việt được biên tập.
- Bảng nhiệm vụ `msg_quest.bin` còn thiếu (94 mục) được để nguyên, chưa tính hoàn thành; nên ưu tiên đợt BV.
- Sau merge dự kiến tổng **21.389**, còn **260** mục trong worklist gốc 19.474. Chỉ xác nhận khi đọc lại GitHub.