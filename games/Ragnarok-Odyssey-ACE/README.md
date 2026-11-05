# Ragnarok Odyssey ACE — Việt hóa PS3

- **Mã game:** BLUS31386 (US), APP_VER 01.00
- **Nguồn dữ liệu:** `RagnarokACE-BanGiaoDich-2026-11-04.zip`
- **Catalog đã kiểm kê:** 25.288 chuỗi / 76 bảng
- **Đã có bản dịch:** 7.805 (2.175 đã duyệt trong bàn giao + 5.630 dịch sau bàn giao)
- **Chưa dịch trong danh sách cần xử lý:** 13.844 / 19.474
- **Cập nhật gần nhất:** 06/11/2026
- **Tình trạng:** dữ liệu bản dịch; chưa được kiểm thử đóng gói patch PS3.

## Điểm bắt đầu mỗi lần dịch

1. Mở [`translations/current.json`](translations/current.json): đây là **bản hợp nhất hiện hành duy nhất**, chứa 7.805 cặp `id → target_vi`.
2. Đối chiếu với `01_CAN_DICH/needs_translation.json` từ gói bàn giao gốc, chỉ dịch mục chưa có trong `current.json`.
3. Không chỉnh ID, file, index, source, source_tagged, attributes, status hoặc source_sha256. Giữ token `{#0}`, `{#1}`, printf như `%u` và số liệu.
4. Sau mỗi đợt, viết một JSON mới trong `checkpoints/`, kiểm tra, rồi cập nhật `translations/current.json` và tiến độ này.
5. Giữ font tiếng Việt và dòng credit **“Việt hóa bởi Votri Valley.”** trong bản dựng game; kho chỉ quản lý dữ liệu dịch và quy tắc.

## Lịch sử

| Đợt | Mục mới | Nội dung |
|---|---:|---|
| 04/11 | 2.175 | Bản duyệt bàn giao |
| 05/11 — checkpoint trước | 434 | Mẹo tải màn, NPC, chế độ, giao diện |
| 05/11 — đợt mới A | 131 | Bình thuốc, mô tả, biểu cảm |
| 05/11 — đợt mới B | 123 | DLC, nhật ký trận đấu, xếp hạng |
| 05/11 — đợt mới C | 385 | Lịch sử chiến đấu, bách khoa, phòng mạng, hội thoại NPC |
| 05/11 — đợt mới D | 410 | Lời thoại NPC, mô tả và tên nhiệm vụ, địa điểm, bộ phận quái vật |
| 05/11 — đợt mới E | 347 | Lời thoại NPC, mô tả nguyên liệu, dấu ngoặc/nhãn rơi vật phẩm |
| 05/11 — đợt mới F | 367 | Lời thoại NPC 1681–1983, mô tả nguyên liệu 111–180 |
| 05/11 — đợt mới G | 342 | Thoại NPC 1984–2206, mô tả nguyên liệu 181–299 |
| 05/11 — đợt mới H | 204 | Thoại NPC 2207–2350, mô tả nguyên liệu 300–359 |
| 05/11 — đợt mới I | 221 | Hội thoại NPC 2351–2520, nguyên liệu 360–410 |
| 05/11 — đợt mới J | 244 | Thoại NPC 2521–2640; tên và mô tả ACE; tên kỹ năng bị động 0–39 |
| 05/11 — đợt mới K | 372 | Thoại Lod 2641–2730; 121 tên và 161 mô tả kỹ năng bị động |
| 05/11 — đợt mới L | 370 | Thoại Lif–Thrasir 2731–2850, 125 tên và 125 mô tả kỹ năng bị động 161–285 |
| 05/11 — đợt mới M | 350 | Thoại Thrasir 2851–2920; tên và mô tả kỹ năng 286–425 |
| 05/11 — đợt mới N | 240 | Thoại Thrasir–Yukino 2921–3000, kỹ năng 426–505 (tên và mô tả) |
| 05/11 — đợt mới O | 240 | NPC 3001–3070, tên và mô tả kỹ năng 506–590 |
| 05/11 — đợt mới P | 240 | NPC 3071–3141 (bỏ 3090 đã dịch), tên và mô tả kỹ năng 591–675 |
| 05/11 — đợt mới Q | 279 | Hội thoại 3142–3232 (bỏ 6 ID đã có), tên/mô tả kỹ năng 676–775 |
| 06/11 — đợt mới R | 331 | NPC Brokkr/Rune 3233–3315, tên và mô tả kỹ năng 776–899; QA 331/331 |
| **Tổng** | **7.805** | Không trùng ID |

## Cấu trúc

- `translations/current.json`: snapshot mới nhất để Codex/người dịch tiếp nối.
- `checkpoints/`: từng đợt dịch theo ngày, không xóa bản cũ.
- `glossary.md`: thuật ngữ và lối xưng hô.
- `apply_checkpoint.py`: gắn bản dịch từ `current.json` vào bản gốc `needs_translation.json`, chỉ sửa `target_vi`.

## Tạo `completed.json`

Tải gói bàn giao gốc 04/11, dùng Python 3:

```bash
python games/Ragnarok-Odyssey-ACE/apply_checkpoint.py \
  --input needs_translation.json --output completed.json
```

Bước này chỉ điền các mục trong danh sách cần dịch. Để chuẩn bị dữ liệu dựng game, chạy tiếp **`validate_return.py` của gói bàn giao**, kiểm tra ảnh/texture, font, bản đóng gói và thử trong RPCS3/PS3 thật. Không xuất bản patch khi chưa kiểm thử.

**Lưu ý:** 25.288 mục chỉ là kiểm kê 76 bảng TXT, chưa bảo đảm mọi chữ trong ảnh, phim, EBOOT, DLC hoặc bản cập nhật đều đã được phát hiện. Không tải ISO/PKG/CPK có bản quyền hay font thương mại lên repo.

**QA đợt L:** Bản gốc tên `Triple Jump` (kỹ năng 263), nhưng mô tả tiếng Nhật ghi nhảy hai lần. Chưa tự sửa bất đồng này; cần kiểm thử game trước khi thống nhất. Đã xác minh cấu trúc 370/370 mục mới.
