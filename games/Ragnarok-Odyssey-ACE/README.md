# Ragnarok Odyssey ACE — Việt hóa PS3

- **Mã game:** BLUS31386 (US), APP_VER 01.00
- **Nguồn dữ liệu:** `RagnarokACE-BanGiaoDich-2026-11-04.zip`
- **Catalog đã kiểm kê:** 25.288 chuỗi / 76 bảng
- **Đã có bản dịch:** 9.972 (2.175 đã duyệt trong bàn giao + 7.797 dịch sau bàn giao)
- **Chưa dịch trong danh sách cần xử lý:** 11.677 / 19.474
- **Cập nhật gần nhất:** 06/11/2026
- **Tình trạng:** dữ liệu bản dịch; chưa được kiểm thử đóng gói patch PS3.

## Điểm bắt đầu mỗi lần dịch

1. Mở [`translations/current.json`](translations/current.json): đây là **bản hợp nhất hiện hành duy nhất**, chứa 9.972 cặp `id → target_vi`.
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
| 06/11 — đợt mới S | 334 | NPC 3316–3429 (Rune, Linde, Lif, Thrasir, Lod, Brokkr), tên/mô tả kỹ năng 900–1009 |
| 06/11 — đợt mới T | 338 | NPC 3430–3610 (176 ID mới); tên và mô tả kỹ năng 1010–1090 (81 cặp) |
| 06/11 — đợt mới U | 495 | NPC 3611–3705 (95), tên thẻ quái 0–299 (300), mô tả thẻ 0–99 (100) |
| 06/11 — đợt mới V | 500 | NPC 3706–3765 (60), tên thẻ 300–599 (300), mô tả thẻ 100–239 (140) |
| 06/11 — đợt mới W | 500 | NPC 3766–3815 (50), tên thẻ/trang bị/kỹ năng 600–849 (250), mô tả thẻ 240–439 (200) |
| **Tổng** | **9.972** | Không trùng ID |

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

**QA đợt S:** 334 ID chưa dịch từ `needs_translation.json`, bộ `validate_return.py` chuẩn PASS 334/334 với bản tham chiếu pending khôi phục từ cùng gói. Bản sao `02_TOAN_BO/all_records.json` trong ZIP không giải nén được (bad file header); chưa chạy được đối chiếu trực tiếp với toàn bộ `all_records.json`. Dữ liệu nguồn, token, số và placeholder được đối chiếu với `needs_translation.json`; không có va chạm với `current.json`.

**QA đợt T:** `validate_return.py` nguyên bản PASS 338/338 khi dùng danh sách tham chiếu tái tạo từ `01_CAN_DICH/needs_translation.json` (19.474 mục), do `all_records.json` trong ZIP báo BadZipFile header. Các ID 3448/3452/3454/3469 đã có ở bản tổng hợp được bỏ qua, 3522 vắng trong danh sách cần dịch. 0 va chạm và 0 lỗi token/printf/chữ số. Chưa thử patch/độ rộng font trên RPCS3/PS3. Bảng kỹ năng bị động kết thúc tại ID 1090; đợt tiếp theo ưu tiên NPC 3611+ và các bảng khác chưa dịch, không giả định có kỹ năng 1091.

**QA đợt U:** Dịch 495 ID trực tiếp từ ZIP nguồn và qua `validate_return.py` nguyên bản với bảng tham chiếu là các bản ghi pending trích nguyên dạng từ `needs_translation.json`: PASS 495/495. Đã so khớp token `{#0}`, printf, mọi chữ số, loại bỏ ID trùng, giữ số dòng NPC tối đa 3 và đoạn dài nhất 38 ký tự/dòng. Tệp `02_TOAN_BO/all_records.json` trong ZIP vẫn báo lỗi local-header; không báo đã kiểm tra trực tiếp catalog đầy đủ. Thử font/patch trên RPCS3/PS3 vẫn chưa thực hiện.

**QA đợt V:** 500 bản dịch nguồn từ ZIP 04/11; `validate_return.py` gốc PASS 500/500, 0 trống (tham chiếu là 500 bản ghi pending nguyên trạng trích từ `01_CAN_DICH/needs_translation.json`). Giữ token nhân vật `{#0}`, số, mã `[Card No.xxx-C/U/R]`, định dạng printf và ID; 0 va chạm trong `current.json`. Mỗi dòng NPC tối đa 38 ký tự, tối đa 3 dòng. Tệp `02_TOAN_BO/all_records.json` của ZIP lỗi local-header nên chưa xác nhận trực tiếp toàn bộ catalog. Chưa test game/patch/font trên RPCS3/PS3.

**QA đợt W:** 500 bản dịch gốc từ ZIP bàn giao; `validate_return.py` nguyên bản PASS 500/500 với bảng tham chiếu tái tạo từ 500 bản ghi `needs_translation.json` nguyên gốc. Bảo toàn ID, token màu/nhân vật `{#0}`, printf và chữ số; NPC không quá 3 dòng hoặc 38 ký tự/dòng; 0 va chạm với `current.json`. Tệp `02_TOAN_BO/all_records.json` bên trong ZIP lỗi `BadZipFile: Bad magic number for file header`, nên không được tuyên bố đã kiểm tra trực tiếp toàn bộ catalog. `it_db_name_card` ID 780–792 và 829–849 thực chất là tên kỹ năng (không tự thêm chữ Thẻ). Chưa thử bản patch/font trên RPCS3/PS3.
