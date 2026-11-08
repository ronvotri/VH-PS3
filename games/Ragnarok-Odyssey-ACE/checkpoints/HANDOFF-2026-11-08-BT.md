# Ragnarok Odyssey ACE — Đợt BT (08/11/2026)

- Dịch **449 mục mới** từ danh sách gốc `needs_translation.json` theo 8 bảng.
- Nội dung: 97 nhãn nhân vật bách khoa, 126 danh hiệu/trang trí, 88 tên địch, 53 nhãn NPC, 44 bộ phận boss, 15 tên bản đồ, 13 tên và 13 mô tả màu da.
- Tên riêng nhân vật/quái vật giữ nguyên khi cần; tên quái khớp bản dịch bách khoa đã thống nhất trong BS. Một số ID `Reserved` và số thứ tự trong nhãn NPC giữ nguyên giá trị kỹ thuật tương ứng.
- Dịch không gán các mục 194–555 bách khoa NPC vì các mục đó phần lớn là mốc ngày placeholder; cần kiểm kê riêng.
- `validate_return.py` từ ZIP gốc với `all_records.json` gốc PASS **449/449**. Kiểm tra đối chiếu token, số, NFC và mỗi dòng tối đa 38 codepoint.
- Đợt BT chỉ gồm `id → target_vi`; không thay đổi trường nguồn, hash hoặc thuộc tính.
- **Chưa đóng patch hoặc test chữ/font thực tế trên PS3/RPCS3.**
- Snapshot cơ sở GitHub: `translations/current.json` **20.606** mục (commit BS), không trùng bất kỳ ID nào trong nhóm BT.
- Hợp nhất GitHub chỉ sau khi xác nhận SHA snapshot hiện tại; thông tin commit bổ sung sau.