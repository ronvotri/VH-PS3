# Ragnarok Odyssey ACE — Bàn giao BS (08/11/2026)

## Nội dung đã thực hiện

- BS: **304 mục mới**: 174 mục `dictionary.cpk::dc_db.en.pac::dc_db_text_monster.rmsg` (87 tên, 87 mô tả) và 130 mục `item.cpk::it_db.en.pac::it_db_name_equip.rmsg` (bỏ qua 16 mục đã có trong current).
- BJ/BK: **72 mục** `dictionary.cpk::dc_db.en.pac::dc_db_text_npc.rmsg` (ID 122–193) từ checkpoint cũ được phục hồi và chuẩn hóa ngắt dòng; sửa chữ số nguồn ở ID 123, 132, 140, 153, 166. Đây không phải 72 bản dịch tạo mới trong đợt BS.
- Giữ nguyên các tên riêng quái vật (Fafnir, Skoll, Hati, Nidhoggr...), nghề theo glossary và mã kỹ thuật gốc.

## Kiểm định

- Chạy bản gốc `validate_return.py` trích trực tiếp từ ZIP bàn giao cùng `02_TOAN_BO/all_records.json` gốc: **Validated 376 nonempty pending translations; 0 empty records**.
- 0 lỗi `source_sha256`, 0 thiếu/khác token, 0 printf, 0 sai chữ số, 0 trùng ID trong gói; mọi dòng tối đa 38 ký tự (kiểm tra theo codepoint, không phải pixel).
- Chưa đóng gói patch, chưa kiểm tra chữ/font thực tế trên RPCS3 hay PS3.
- Không được đếm lại checkpoint BL–BQ: 834 ID đã tồn tại trong bản hợp nhất từ trước.

## Đường dẫn

- `checkpoints/2026-11-08-batch-304-BS.json`: 304 bản dịch mới.
- `checkpoints/2026-11-08-BS-BJ-BK-72-repaired.json`: 72 bản dịch trước được QA và sửa định dạng.
- `checkpoints/2026-11-08-BS-QA.json`: kiểm tra kỹ thuật.
- `translations/current.json`: snapshot hợp nhất mới nhất; chỉ thêm ID chưa có và giữ nguyên ID cũ.

## Bước tiếp theo

- Tiếp tục bảng `dc_db_text_npc.rmsg` còn lại, mục bách khoa thuật ngữ, hướng dẫn / giao diện. Luôn kiểm tra thực tế số mục còn thiếu bằng ID từ `needs_translation.json` và `translations/current.json`.
- Credit khi đóng patch: **Việt hóa bởi Votri Valley.**
## Kết quả sau hợp nhất

- `translations/current.json` đã hợp nhất **376 ID mới đối với snapshot** (304 ID đợt BS + 72 ID đã dịch BJ/BK), không có ID va chạm, tăng **20.230 → 20.606**. Commit: `a14ef16fd62bb0c6c4a09b4dab3d01910d680b1f`.
- `README.md` đã cập nhật tiến độ, số mục còn thiếu **1.043 / 19.474**. Commit: `ac083a64536a064032940739ee4325511b4e896c`.
- Cần ưu tiên bảng bách khoa NPC, giao diện trang trí, lưu trò chơi và bảng nhiệm vụ còn thiếu. Hãy đối chiếu `needs_translation.json` với `current.json` trước khi chọn đợt tiếp theo.
