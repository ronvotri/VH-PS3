# Ragnarok Odyssey ACE — Đợt BC: hiệu đính thuật ngữ và nghĩa (07/11/2026)

## Kết quả
- **18/18 hiệu đính trên bản dịch đã tồn tại**: **17** chuỗi NPC (`msg_npc_talk.bin`) và **1** hướng dẫn (`msg_tutorial.bin::137`). **Không có ID dịch mới.**
- Tổng `translations/current.json` giữ **19.161 / 25.288 mục (75,77%)**; checkpoint BB trước đó vẫn còn hiệu lực.
- Chuẩn hóa **Proof of Expertise → Chứng Nhận Thành Thạo** theo `item.cpk::it_db.en.pac::it_db_name_material.rmsg::389` đã dịch; cập nhật `glossary.md`, 4 đoạn NPC và 1 hướng dẫn.
- Chỉnh nghĩa và văn phong ở các ID NPC: `5423, 5518, 5604, 5712, 6025, 6030, 6048, 6060, 6110, 6118, 6121, 6125, 6128`.

## QA
- Giữ nguyên ID; 18 chuỗi cũ có số dòng, marker và chữ số trùng trước/sau; chiều dài tối đa 38 ký tự hiển thị/dòng.
- Bản hợp nhất 19.161 chuỗi có 0 giá trị rỗng, 0 NUL/CR, 0 sai chuẩn NFC, 0 dòng vượt 38 ký tự ở kiểm tra tĩnh (không tính các marker `{#n}`).
- **Nguồn đối chiếu trực tiếp:** 15/18 chuỗi sửa có `source_tagged` từ `NPC_SOURCE_5403-6138.json`. Hai NPC 3174/3175 và hướng dẫn 137 chỉ đối chiếu bản dịch trước đó và tên vật phẩm, **chưa có nguyên bản tiếng Anh để kiểm tra lại**.
- Chưa chạy validator nguồn toàn bộ `validate_return.py`, chưa dựng hay thử patch RPCS3/PS3.
- Chi tiết: [2026-11-07-BC-semantic-revisions.json](2026-11-07-BC-semantic-revisions.json), [2026-11-07-BC-QA.json](2026-11-07-BC-QA.json).

## Phần đang bị chặn
- ZIP gốc `RagnarokACE-BanGiaoDich-2026-11-04.zip` 29.607.145 bytes có trong Library nhưng hiện không cho trích raw/text; chỉ còn nguồn riêng cho 733 NPC (đều đã dịch).
- **2.488 mục chưa dịch** là con số từ checkpoint trước, chưa thể đọc lại `01_CAN_DICH/needs_translation.json` để chọn ID mới.
- Không tự bịa câu nguồn. Khi ZIP nguồn được đính kèm dưới dạng file có thể đọc, dùng `prepare_batch_bb.py` với snapshot `translations/current.json` hiện tại, chọn 500 mục mới trước rồi dịch/QA.

**Credit: Việt hóa bởi Votri Valley.**
