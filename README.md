# VH-PS3 — Kho Việt hóa game PlayStation 3

Kho chung dành cho các dự án Việt hóa PS3 của Votri Valley. **Mỗi game nằm trong một thư mục riêng** để không trộn văn bản, font, công cụ hoặc checkpoint.

## Dự án

- [Ragnarok Odyssey ACE (BLUS31386)](games/Ragnarok-Odyssey-ACE/README.md) — dữ liệu dịch và tiến độ kiểm tra.

## Nguyên tắc cập nhật

1. Mỗi lần dịch có checkpoint ngày, kèm số mục mới, nguồn và danh sách mục đã sửa.
2. Giữ nguyên định danh ID, file, index, source, source_sha256 và token định dạng.
3. Chỉ đưa vào bản dịch đã biên tập. Nháp máy, debug, ảnh/asset chưa rà không tính hoàn thành.
4. Không đưa ISO, PKG/CPK game bản quyền, key, font thương mại hoặc dữ liệu game không có quyền phân phối lên kho.
5. Sau mỗi đợt: đối chiếu ID, ký hiệu chèn, ký hiệu printf và số liệu; ghi rõ **chưa kiểm thử trong game** nếu chưa có runtime test.

Bản dịch chỉ là một phần của quy trình; để tạo patch cần tài liệu/công cụ dựng và tệp nguồn hợp pháp trên máy người thực hiện.
