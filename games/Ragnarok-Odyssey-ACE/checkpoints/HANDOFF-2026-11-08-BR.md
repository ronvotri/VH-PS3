# Ragnarok Odyssey ACE — Bàn giao BR (08/11/2026)

- **438 chuỗi mới**, 7 bảng trang phục/tùy biến nhân vật (tên phụ kiện đầu, giọng, tóc, mặt và mô tả).
- Đối chiếu nguồn gốc theo ID và SHA256; không sửa các trường `file`, `index`, `source`, `source_tagged`, `attributes`, `source_sha256`.
- Giữ nguyên tên riêng (Odin, Valkyrie, Gacha Knights, Feena, Kat, …) và số hiệu. Tên các giọng thử nghiệm tiếng Nhật được diễn đạt theo tên nhân vật tiếng Anh ở bảng mô tả voice tương ứng; nên kiểm tra bằng game thật.
- Kiểm thử văn bản: đúng token, printf, chữ số, không mục trống, không quá 38 ký tự mỗi dòng.
- **Lưu ý quan trọng:** snapshot GitHub `translations/current.json` đã có 19.792 mục. Trong 906 mục BJ–BQ có **72 mục BJ/BK là mới**, **834 mục BL–BQ đã có sẵn trong snapshot** (cần coi là phương án hiệu đính, không cộng thêm).
- Cần bảo đảm chỉ cộng các ID thực sự mới. Chưa đóng patch hoặc thử PS3/RPCS3.

Bản dịch mới của BR ở `2026-11-08-batch-438-BR.json`, QA ở `2026-11-08-BR-QA.json`.
## Kết quả đồng bộ

- Đã merge **438/438 ID mới** của BR vào `translations/current.json`, commit `033f1f5114ba338138e9167463c140b36fab1c38`.
- Snapshot sau merge: **20.230** mục; bảng danh sách gốc còn **1.419** mục chưa dịch.
- Cập nhật README và rà lại kiểm kê, commit `840dbcd8903a14c19043425c4b1f179250ca32a4`.
- Hai checkpoint BJ/BK với 72 ID mới vẫn đang chờ rà và gộp riêng. BL–BQ có 834 ID trùng snapshot, không tự động cộng/ghi đè.
