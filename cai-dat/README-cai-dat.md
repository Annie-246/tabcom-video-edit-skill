# Cài đặt môi trường

Làm một lần trên mỗi máy. Mất khoảng 15–30 phút (chủ yếu là tải model AI tách nền).

## 1. Chép skill vào Claude Code

Chép **cả hai thư mục** trong `.claude/skills/` của gói này vào thư mục skill của Claude Code:

**Windows**

```powershell
Copy-Item ".\.claude\skills\tabcom-video-edit"      "$env:USERPROFILE\.claude\skills\" -Recurse -Force
Copy-Item ".\.claude\skills\tabcom-video-thumbnail" "$env:USERPROFILE\.claude\skills\" -Recurse -Force
```

**macOS / Linux**

```bash
cp -r .claude/skills/tabcom-video-edit      ~/.claude/skills/
cp -r .claude/skills/tabcom-video-thumbnail ~/.claude/skills/
```

Mở lại Claude Code, gõ `/` sẽ thấy hai skill `tabcom-video-edit` và `tabcom-video-thumbnail`.

Muốn dùng riêng cho một dự án thì chép vào `<thư-mục-dự-án>/.claude/skills/` thay vì thư mục người dùng.

## 2. Cài phần mềm

| Phần mềm | Vì sao cần | Cách cài (Windows) |
|---|---|---|
| **ffmpeg + ffprobe** | Cắt, ghép, render video | `winget install Gyan.FFmpeg` rồi mở lại terminal |
| **Python 3.11 hoặc 3.12** | Chạy toàn bộ pipeline | `winget install Python.Python.3.12` |
| **Node.js 18+** | Script gom ảnh stock | `winget install OpenJS.NodeJS.LTS` |
| **Google Chrome** | Playwright chụp màn hình trang web | Cài bản thường |

Kiểm tra: `ffmpeg -version`, `python --version`, `node --version` đều phải ra kết quả.

macOS: `brew install ffmpeg python@3.12 node`.

## 3. Cài thư viện Python

```bash
pip install -r cai-dat/requirements.txt
```

Lưu ý đã gặp:

- **Pillow phải ≥ 10** — Pillow 9.5 segfault trên Python 3.12.
- `rembg` kéo theo `onnxruntime`, dung lượng khá lớn, cứ để nó tải xong.

## 4. Tải model tách nền (bắt buộc)

Pipeline dùng hai model của `rembg`. Lần chạy đầu nó tự tải, nhưng tải trước cho chắc:

```bash
python cai-dat/tai_model.py
```

Model nằm trong `~/.u2net/`, mỗi model 100–200 MB.

## 5. Cài Playwright (chỉ cần khi gom ảnh stock/screenshot)

```bash
pip install playwright
npm install -g playwright
```

Không cần chạy `playwright install` nếu máy đã có Chrome — script ưu tiên Chrome hệ thống.

## 6. Kiểm tra

```bash
python "%USERPROFILE%\.claude\skills\tabcom-video-edit\scripts\tabcom_paths.py"
```

Phải in ra `[OK]` cho tất cả asset và dòng `Du asset, chay duoc.`

## Máy cần cấu hình thế nào

Pipeline render từng frame bằng CPU, không cần card đồ họa rời. Nhưng bước tách nền người
(`birefnet-portrait`) chạy **~17–50 giây/frame** tùy máy — mỗi giây video split tốn 7–20 phút.
Máy yếu thì giảm số cửa sổ split, tăng dùng lớp phủ (rẻ hơn nhiều). RAM tối thiểu 8 GB;
**không chạy tách nền và render Pillow song song** — hết RAM là crash.
