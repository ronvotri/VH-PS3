# Ragnarok Odyssey ACE — Bàn giao BA (07/11/2026)

## Kết quả

- Hiệu đính **102 chuỗi tiếng Việt hiện có** ở 6 bảng: 9 hướng dẫn, 11 mô tả địa điểm, 2 nguyên liệu, 3 mô tả ACE, 56 mô tả kỹ năng và 21 thẻ bài.
- Quét so sánh bản hợp nhất GitHub trước sửa: **PASS 102/102**, không trùng ID, không đổi thứ tự mã màu, printf, chữ số, tên khóa hoặc số dòng.
- Sau sửa, **0/19.161** chuỗi có dòng vượt ngưỡng *tham khảo* 38 ký tự hiển thị. Đã giảm 102 cảnh báo độ dài; chưa kiểm chứng kích thước phông chữ hoặc tràn khung thực tế.
- Tổng bản dịch hợp nhất vẫn **19.161 / 25.288 (75,77%)**. Còn **2.488** mục trong danh sách dịch ban đầu.
- Đóng gói 102 mục trong `BA-revisions.json` và file `builder-ready/` theo từng bảng để nhập liệu; không phải bản patch PS3.
- **Chưa chạy bộ validator gốc trên toàn bộ 19.161 bản dịch**, chưa kiểm thử trên RPCS3/PS3.

## Tiếp đợt BB

- Tìm lại tệp `01_CAN_DICH/needs_translation.json` trong `RagnarokACE-BanGiaoDich-2026-11-04.zip` (Library có nhưng raw-byte materialization bị từ chối). Không tự đoán văn bản nguồn.
- Lọc ID thật sự chưa dịch từ bản hợp nhất GitHub, mới có thể tiếp tục 2.488 mục.
- Chạy validator nguồn gốc khi ZIP có thể giải nén; kiểm thử trực tiếp UI các thông báo/cảnh báo và phần mô tả kỹ năng.
- Trước khi dịch thêm, kéo `translations/current.json` mới nhất để tránh trùng hoặc ghi đè.

Credit: **Việt hóa bởi Votri Valley.**