# Ragnarok Odyssey ACE — Bàn giao đợt AU (07/11/2026)

## Tiến độ đã xác minh

- **500 bản dịch mới** đã ghi trên GitHub: **225** NPC 5910–6138; **237** tên BGM 0–236; **38** mô tả BGM 0–37.
- Snapshot hợp nhất: `translations/current.json` với **17.877 / 25.288** (~70,7%). Danh sách cần dịch còn **3.772** mục.
- Delta: `checkpoints/2026-11-07-batch-500-AU.json`.
- 6024 và 6025 đã dịch ở trước, **không ghi đè**. NPC 6084 và 6105 không nằm trong nguồn cần dịch.
- Dùng ZIP nguồn gốc người dùng đính kèm `RagnarokACE-BanGiaoDich-2026-11-04.zip` và chạy `validate_return.py` với `all_records.json` chính gốc: **PASS 500/500**, không đổi source, ID, thuộc tính, SHA, token, printf, chữ số; bản dịch chuẩn NFC và <=3 dòng/38 ký tự mỗi dòng.
- **Chưa dựng patch** hay kiểm tra font, chiều rộng hiển thị thực tế trong RPCS3/PS3.

## Tệp tiếp nối và đợt AV

- ZIP `RagnarokACE-Checkpoint-AU-2026-11-07.zip` đã lưu trong Library dưới `/RagnarokACE/`, chứa `completed_AU.json`, `checkpoint_AU.json`, `delta_AU.json`, `QA_AU.json`, bản builder-ready và **`SOURCE_NEXT_AV.json` với 862 mục tiếng Anh gốc**.
- Đợt **AV** có thể chọn **500 mục** trong `SOURCE_NEXT_AV.json`, bắt đầu từ mô tả nhạc BGM 38–236 (199 mục) và `msg_quest.bin` 221–900 (663 mục). Luôn lọc ID đã có trong `translations/current.json`.
- **Không commit văn bản tiếng Anh gốc** lên GitHub; chỉ commit delta tiếng Việt và thông tin bàn giao. Nguồn game trong Library/ZIP riêng.
- Credit giữ nguyên: **Việt hóa bởi Votri Valley.**

## Các commit
- Delta AU: `0fdb50d9d79b2132071f055c9d98337a60d23bd0`.
- Hợp nhất AU: `5a8b975d877d5e49b9dce6ba42f4d4f106dd5e44`.
