# Ragnarok Odyssey ACE — Đợt BB: nguồn & kiểm tra QA (07/11/2026)

## Kiểm tra đã hoàn tất
- Snapshot `translations/current.json` trên `main`, blob `480a0c7ea4f395ab0391ed7814b0d8cab8e422e6`: **19.161/25.288** ID, đúng `count`, không có giá trị rỗng, NUL/CR, NFC sai chuẩn hay dòng vượt kiểm tra tĩnh 38 ký tự hiển thị (loại marker `{#n}`).
- Đối chiếu chính xác **733/733** bản ghi gốc NPC `msg_npc_talk.bin` ở chỉ số **5403–6138** từ `NPC_SOURCE_5403-6138.json` với bản hợp nhất GitHub. **0** lỗi mã `{#n}`/printf/thẻ, **0** sai lệch chữ số, **0** dòng vượt 38 ký tự.
- **Không có câu dịch ID mới trong BB.** Tổng giữ nguyên 19.161, không giả tăng tiến độ; danh sách cũ báo còn **2.488** cần dịch nhưng chưa được kiểm kê lại trực tiếp.
- Chi tiết: [2026-11-07-BB-source-QA.json](2026-11-07-BB-source-QA.json).

## Trở ngại cần giải quyết
Tệp `RagnarokACE-BanGiaoDich-2026-11-04.zip` (29.607.145 bytes) còn hiển thị trong Thư viện nhưng cả raw và text materialization đều trả `This Project file does not have an authorized raw-byte materialization path.` Không thể đọc `01_CAN_DICH/needs_translation.json`, vì vậy **không được tự tạo câu nguồn hoặc tiếp tục dịch 2.488 ID**.

## Cách tiếp tục khi có lại ZIP đọc được
1. Lấy `translations/current.json` mới nhất để chống dịch trùng.
2. Chạy script [prepare_batch_bb.py](../prepare_batch_bb.py) tại máy có ZIP gốc:
   
   ```bash
   python prepare_batch_bb.py --archive RagnarokACE-BanGiaoDich-2026-11-04.zip --current translations/current.json --output pending-BB.local.json --limit 500
   ```
3. Script kiểm SHA-256 nguồn, lọc ID đã có trong snapshot và xuất danh sách pending. File pending chứa nguyên văn tiếng Anh, **chỉ lưu riêng tư, không commit vào GitHub công khai**.
4. Dịch từng cụm mục mới, chạy `validate_return.py` gốc, merge `translations/current.json`, ghi checkpoint dịch mới và cập nhật tiến độ.

## QA chưa thực hiện
- Chưa đối chiếu trực tiếp toàn bộ 2.488 pending (thiếu nguồn ZIP).
- Chưa thử patch/font/giao diện trong RPCS3/PS3.

**Credit: Việt hóa bởi Votri Valley.**
