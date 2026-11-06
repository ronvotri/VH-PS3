# Ragnarok Odyssey ACE — Việt hóa PS3

- **Mã game:** BLUS31386 (US), APP_VER 01.00
- **Nguồn dữ liệu:** `RagnarokACE-BanGiaoDich-2026-11-04.zip`
- **Catalog đã kiểm kê:** 25.288 chuỗi / 76 bảng
- **Đã có bản dịch:** 16.370 (2.175 đã duyệt trong bàn giao + 14.195 dịch sau bàn giao)
- **Chưa dịch trong danh sách cần xử lý:** 5.279 / 19.474
- **Cập nhật gần nhất:** 06/11/2026
- **Tình trạng:** dữ liệu bản dịch; chưa được kiểm thử đóng gói patch PS3.

## Điểm bắt đầu mỗi lần dịch

1. Mở [`translations/current.json`](translations/current.json): đây là **bản hợp nhất hiện hành duy nhất**, chứa 16.370 cặp `id → target_vi`.
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
| 06/11 — đợt mới X | 500 | NPC 3816–3865 (50), nhãn thẻ/kỹ năng 850–1099 (250), mô tả thẻ 440–639 (200) |
| 06/11 — đợt mới Y | 500 | NPC 3866–3957 (92); toàn bộ tên thẻ còn lại 1100–1470 (371) và mô tả thẻ 640–676 (37) |
| 06/11 — đợt mới Z | 500 | NPC 3958–4039 (80 ID, bỏ 3963/4002 đã có); 120 tên + 120 mô tả vũ khí 0–119; 180 tên đơn chế tạo 0–179 |
| 06/11 — đợt mới AA | 500 | NPC 4040–4105 (66); 100 tên + 100 mô tả vũ khí 120–219; 234 tên đơn chế tạo 180–413 |
| 06/11 — đợt mới AB | 500 | NPC 4106–4165 (60); 100 tên + 100 mô tả vũ khí 220–319; 240 đơn chế tạo 414–653 |
| 06/11 — đợt mới AC | 500 | NPC 4166–4240 (75); 100 tên + 100 mô tả vũ khí 320–419; 225 đơn chế tạo 654–878 |
| 06/11 — đợt mới AD | 500 | 80 NPC 4241–4320; 30 tên + 30 mô tả vũ khí 420–449 (hoàn tất 450/450 mỗi bảng); 360 đơn chế tạo 879–1238 |
| 06/11 — đợt mới AE | 500 | 80 NPC 4321–4400; 320 đơn chế tạo 1239–1558; 100 tên nguyên liệu 0–99 (mô tả nguyên liệu đã dịch) |
| 06/11 — đợt mới AF | 500 | 80 NPC 4401–4480; 160 tên nguyên liệu 100–259; 260 đơn chế tạo 1559–1818 |
| 06/11 — đợt mới AG | 500 | 80 NPC 4481–4560, 151 tên nguyên liệu 260–410, 269 đơn chế tạo 1819–2087 |
| 06/11 — đợt mới AH | 500 | 79 NPC 4561–4641 (giữ 4563 và 4619), 421 đơn chế tạo 2088–2508 |
| 06/11 — đợt mới AI | 500 | 81 NPC 4642–4722, 419 đơn chế tạo 2509–2927 |
| 06/11 — đợt mới AJ | 314 | 79 NPC 4723–4802, 235 đơn chế tạo 2928–3162 |
| 06/11 — đợt mới AK | 84 | 84 NPC 4803–4886 |
| **Tổng** | **16.370** | Không trùng ID |

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

**QA đợt X:** `validate_return.py` gốc PASS 500/500 với bảng tham chiếu pending tái tạo từ 500 dòng nguồn `01_CAN_DICH/needs_translation.json` trong ZIP; không có ID trùng, lỗi token/printf/chữ số. NPC dịch tối đa 3 dòng, mỗi dòng tối đa 38 ký tự. Danh mục thẻ tên 850–930 là tên **kỹ năng**, 931–1099 là tên thẻ; mô tả thẻ 440–639 dựa trên bản dịch tên thẻ đã có của đợt V–W. Tệp `all_records.json` trong ZIP lỗi local-header nên không thể xác nhận trực tiếp toàn catalog; chưa thử patch, font và độ rộng trên RPCS3/PS3.

**QA đợt Y:** `validate_return.py` nguyên bản PASS 500/500 với 500 bản ghi pending gốc trích từ `01_CAN_DICH/needs_translation.json`. Không có ID trùng, bản ghi rỗng, sai token `{#0}`, `{#1}`, mã printf hoặc chữ số. NPC tối đa 3 dòng, giới hạn mềm 38 ký tự/dòng. Hai bảng `it_db_name_card.rmsg` (0–1470) và `it_db_text_card.rmsg` (0–676) đã được điền đủ theo checkpoint U–Y. Riêng `02_TOAN_BO/all_records.json` trong ZIP bị lỗi local header, nên chưa đối chiếu trực tiếp toàn bộ catalog và chưa kiểm thử bản patch/font trong RPCS3.


## Bổ sung 06/11/2026 — QA sau checkpoint Y / chuẩn bị đợt Z
- Đã đọc lại 500 bản ghi nguồn trong ZIP checkpoint Y và sửa cách diễn đạt NPC **3881, 3953**; token, chữ số, NFC và giới hạn tối đa 3 dòng / 38 ký tự mỗi dòng đều PASS (2/2).
- Lưu delta hiệu đính riêng tại `checkpoints/2026-11-06-Y-editorial-corrections.json`, đã cập nhật `translations/current.json`. **Đây không phải bản dịch ID mới:** tổng vẫn **10.972/25.288**, còn **10.677** mục trong `needs_translation.json`.
- Thêm `prepare_batch_z.py` để chọn an toàn các mục chưa dịch: NPC **3958+**, `it_db_name_weapon`, `it_db_text_weapon`, `it_db_name_myorder`. Công cụ chỉ đọc ZIP gốc và snapshot, xuất worklist ở máy cục bộ, không tự dịch và không ghi đè. Đã kiểm thử trên source mô phỏng từ checkpoint Y: không chọn lại ID đã dịch.
- **Chưa dịch được ID mới đợt Z:** ZIP gốc `RagnarokACE-BanGiaoDich-2026-11-04.zip` đã được tìm thấy trong thư viện nhưng phiên làm việc hiện tại không lấy được bytes của file. Không bịa nội dung source, không tạo checkpoint Z rỗng, không báo tăng tiến độ.
- Khi có lại ZIP nguồn gốc đọc được, tiếp tục theo script trên rồi dịch thủ công + QA `validate_return.py` trước khi hợp nhất. Chưa build/QA patch RPCS3/PS3.


**QA đợt Z (06/11/2026):** Đã đọc thành công `02_TOAN_BO/all_records.json` gốc (12.548.481 bytes) từ ZIP bàn giao và chạy nguyên bản `validate_return.py` trên 500 dòng nguồn tương ứng: **PASS 500/500, 0 mục rỗng**. Giữ ID, file/index, `source`, `source_tagged`, `source_sha256`, `attributes`, token, printf và chữ số. Giới hạn mềm NPC và mô tả vũ khí không quá 3 dòng, 38 ký tự/dòng. GitHub xác nhận 500/500 mục hợp nhất, 0 trùng ID. Tên rune giữ nguyên, loại vũ khí và tên các nhánh Halomonas được Việt hóa. **Chưa build/test patch RPCS3/PS3**; cần QA tên hiển thị giữa bảng vũ khí và thẻ do bảng thẻ cũ giữ tên mẫu bằng tiếng Anh.

**Đợt AA kế tiếp:** NPC từ **4040**, `it_db_name_weapon` từ **120**, `it_db_text_weapon` từ **120**, `it_db_name_myorder` từ **180**. Chọn theo danh sách nguồn `needs_translation.json`, loại ID có trong `translations/current.json` trước khi dịch. Không ghi đè mục đã dịch.


**QA đợt AA (06/11/2026):** Bản nguồn `needs_translation.json` đối chiếu với `all_records.json` toàn bộ, `validate_return.py` gốc **PASS 500/500**, 0 dòng rỗng. 66 NPC, 100 tên + 100 mô tả vũ khí, 234 đơn chế tạo. Các câu NPC / mô tả vũ khí tối đa 3 dòng, 38 ký tự/dòng; kiểm tra token, chữ số, UTF-8 NFC, 0 ID trùng/ghi đè. Kiểm tra kết quả hợp nhất `current.json` sau commit; chưa kiểm thử patch/font/khung hình trên RPCS3/PS3. Giữ nguyên tên riêng Galdrabok, Domovoi, Vanir/Aesir, các tiền tố rune Wyadd/Feoh/Ullr... và mã nhánh đơn chế tạo; các tên cụ thể của vũ khí có thể cần soát đồng bộ với thẻ.

**Đợt AB kế tiếp:** NPC từ **4106**, `it_db_name_weapon` từ **220**, `it_db_text_weapon` từ **220**, `it_db_name_myorder` từ **414** (luôn lọc ID có trong `translations/current.json`).


**QA đợt AB (06/11/2026):** 500 ID mới từ nguồn `needs_translation.json`; `validate_return.py` gốc đối chiếu `all_records.json` gốc: **PASS 500/500, 0 bản ghi rỗng**. Bảo toàn ID/file/index, `source`, `source_tagged`, `source_sha256`, thuộc tính, mã token, printf, chữ số (kể cả mã nhánh/tier như `5-4`). 60 lời thoại NPC và 100 mô tả vũ khí không quá 3 dòng và 38 ký tự/dòng; kiểm tra NFC và không ghi đè dữ liệu cũ. Chưa kiểm thử bản patch, font và độ rộng hiển thị trong RPCS3/PS3. Bảng tên đơn chế tạo nhiều nhánh có mã `<Onikui>`/`<Hajin>`/`<Somezuki>`/`<Rougoku>`: giữ nguyên các nhãn này; các tên mẫu đã dịch cần soát nhất quán với bảng tên vũ khí/thẻ khi patch.

**Đợt AC tiếp theo:** NPC chưa dịch từ **4166**, `it_db_name_weapon`/`it_db_text_weapon` từ **320**, `it_db_name_myorder` từ **654**. Lấy từng ID thực tế từ nguồn và bỏ các ID đã nằm trong `current.json`.


**QA đợt AC (06/11/2026):** Dịch 500 ID trực tiếp từ `01_CAN_DICH/needs_translation.json`, kiểm lại nguyên bản trong `02_TOAN_BO/all_records.json`; chạy `validate_return.py` gốc **PASS 500/500**, không bản ghi rỗng. Các chuỗi giữ ID, token `{#0}`, printf, chữ số, mã nâng cấp `5-4`, mã tên riêng và thứ tự bảng. Kiểm tra thêm NFC tiếng Việt và tối đa 3 dòng, 38 ký tự/dòng cho NPC và mô tả vũ khí. Truyện: táo vàng là họa tiết tháo lắp trên bìa Galdrabok, dẫn tới trang ẩn; đơn chế tạo: Mince, Drill, Halomonas và Sadistic. Chưa đóng patch hoặc thử giao diện/font RPCS3/PS3.

**Đợt AD tiếp theo:** NPC chưa dịch từ **4241**, `it_db_name_weapon.rmsg`/`it_db_text_weapon.rmsg` từ **420**, `it_db_name_myorder.rmsg` từ **879**. Lọc theo ID thực tế chưa dịch; tránh ghi đè hoặc tự dịch tên riêng thần thoại.


**QA đợt AD (06/11/2026):** Đã dịch 500 ID từ `needs_translation.json` và chạy `validate_return.py` gốc với `all_records.json` nguyên bản (25.288 record): **PASS 500/500**, 0 bản ghi trống. Kiểm thêm UTF-8 NFC, token `{#0}`, mã số nâng cấp, 0 ID trùng và giới hạn 3 dòng/38 ký tự cho NPC và mô tả. Nội dung Niflheim, vợ hiệp sĩ Glast Heim, các linh hồn Helheim, vùng Sograt, bí thuật tách hồn khỏi xác, 450/450 tên và mô tả vũ khí đã hoàn tất. Cần kiểm lại tên mẫu vũ khí với tên thẻ/đơn chế tạo khi patch. Chưa build/test patch hoặc font thật trên RPCS3/PS3.

**Đợt AE tiếp theo:** NPC từ **4321**; `it_db_name_myorder.rmsg` từ **1239**. Hai bảng `it_db_name_weapon.rmsg` và `it_db_text_weapon.rmsg` đã hết ID (0–449). Có thể chuyển thêm sang bảng vật liệu, trang bị hoặc từ điển sau khi lọc ID chưa dịch. Bảo đảm giữ nguyên mọi token và trạng thái save/credit **Việt hóa bởi Votri Valley.**


**QA đợt AE (06/11/2026):** 500 bản ghi nguồn trong `needs_translation.json` đối chiếu toàn bộ `all_records.json` gốc, `validate_return.py` gốc **PASS 500/500**, không trống hoặc sai trường nguồn. Kiểm token `{#0}`, số nâng cấp 1-1/10-3 và Unicode NFC; NPC tối đa 3 dòng, 38 ký tự/dòng. Mô tả nguyên liệu 0–410 đã dịch trong những đợt cũ nên **không ghi đè**. Tên Shiranui/Jellopy/Scell và mã rune giữ nguyên; các tên mẫu chế tạo khác đã đồng bộ với danh mục. **Chưa test bản patch/font trong RPCS3/PS3.**

**Đợt AF tiếp theo:** NPC từ **4401**, đơn chế tạo từ **1559**, tên nguyên liệu từ **100** (đến 410); có thể chuyển thêm sang tên/trang bị và các bảng từ điển sau khi lọc `current.json`.


**QA đợt AF (06/11/2026):** Thêm 500 mục từ ZIP nguồn thật: NPC 4401–4480 (80), `it_db_name_material` 100–259 (160), `it_db_name_myorder` 1559–1818 (260). Chạy `validate_return.py` gốc đối chiếu `02_TOAN_BO/all_records.json` **PASS 500/500**, không có bản ghi rỗng. Kiểm thêm token `{#0}`, printf, chữ số (kể cả mã nhánh), Unicode NFC và NPC tối đa 3 dòng/38 ký tự mỗi dòng. Nội dung: Tháp Ảo Ảnh, Niflheim và màn sương của Hắc Long Nidhoggr. Tên vũ khí Hama Azusa <Misogi/Kannagi/Magami/Amaterasu>, Glanzen Kiếm và Kiếm Bóng Tối giữ mã `A1-1`, các nhánh A–E, hậu tố `: Tối Hậu`. Mô tả nguyên liệu đã dịch từ trước, không ghi đè. Chưa đóng gói hoặc kiểm thử patch/font trên RPCS3/PS3.

**Đợt AG tiếp theo:** NPC chưa dịch từ **4481**, tên nguyên liệu từ **260**, đơn chế tạo từ **1819**; ưu tiên dịch thực tế theo `needs_translation.json` và loại ID đã tồn tại trong snapshot.


**QA đợt AG (06/11/2026):** `validate_return.py` gốc với `all_records.json` gốc PASS 500/500. Không trùng ID, giữ token, số liệu và mã nhánh. NPC tối đa 3 dòng, 38 ký tự/dòng. Bảng tên nguyên liệu đã hoàn tất 411/411. Chưa thử patch hoặc font trên RPCS3/PS3.

**Đợt AH tiếp theo:** Tiếp tuyến NPC từ **4561** và đơn chế tạo từ **2088**. Lọc ID qua `translations/current.json` và `needs_translation.json`. NPC 353–354 cũng còn trong danh sách cần dịch, có thể rà theo cảnh riêng.


**QA đợt AH (06/11/2026):** `validate_return.py` gốc đối chiếu `all_records.json` gốc PASS 500/500. Giữ token, số liệu, mã nhánh và NPC tối đa 3 dòng/38 ký tự. Chưa kiểm thử patch/font trên RPCS3/PS3.

**Đợt AI tiếp theo:** NPC từ **4642** và đơn chế tạo từ **2509**, sau khi lọc ID đã dịch.


**QA đợt AI (06/11/2026):** `validate_return.py` gốc đối chiếu `all_records.json` gốc PASS 500/500. Giữ token, số liệu, mã nhánh và NPC tối đa 3 dòng/38 ký tự. Chưa kiểm thử patch/font trên RPCS3/PS3.

**Đợt AJ tiếp theo:** NPC từ **4723** và đơn chế tạo từ **2928**, sau khi lọc ID đã dịch.


**QA đợt AJ (06/11/2026):** `validate_return.py` gốc với `all_records.json` PASS 314/314. NPC 4775 là `!?`, giữ nguyên. Đã có bản dịch cho toàn bộ 3.163 tên đơn chế tạo. Chưa thử patch/font trên RPCS3/PS3.

**Đợt AK tiếp theo:** Tiếp thoại NPC từ **4803**. Có thể bắt đầu bảng `msg_quest.bin` sau khi lọc ID đã dịch.


**QA đợt AK (06/11/2026):** `validate_return.py` gốc với `all_records.json` PASS 84/84. Hội thoại về vong hồn giả dạng Pavianne và Loli Ruri. Chưa thử patch/font trên RPCS3/PS3.

**Đợt AL tiếp theo:** Tiếp thoại NPC từ **4887**, đối chiếu danh sách nguồn và bản hợp nhất.
