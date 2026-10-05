# Skill edit video Tabcom

Bộ skill cho Claude Code để dựng video dọc 9:16 theo đúng phong cách Tabcom: cắt cảnh theo lời thoại,
tách nền người bằng AI, dựng màn chữ có animation, chèn ảnh minh họa liên tục, caption chạy theo lời
nói, zoom punch, flash chuyển cảnh, sound effect, nối OUTRO và tạo thumbnail.

Gói này **đã kèm sẵn font, nền, card gradient, OUTRO, logo sàn và sticker** — chép vào máy là chạy
được, không phải xin thêm file.

## Dùng thế nào

**Bước 1.** Chép skill vào Claude Code:

```powershell
# Windows PowerShell, chạy trong thư mục gói này
Copy-Item ".\skills\tabcom-video-edit"      "$env:USERPROFILE\.claude\skills\" -Recurse -Force
Copy-Item ".\skills\tabcom-video-thumbnail" "$env:USERPROFILE\.claude\skills\" -Recurse -Force
```

```bash
# macOS / Linux
cp -r skills/tabcom-video-edit ~/.claude/skills/
cp -r skills/tabcom-video-thumbnail ~/.claude/skills/
```

**Bước 2.** Cài môi trường theo [cai-dat/README-cai-dat.md](cai-dat/README-cai-dat.md)
(ffmpeg, Python + thư viện, model tách nền). Làm một lần duy nhất.

**Bước 3.** Tạo thư mục cho video mới, bỏ file quay vào:

```
D:\Video\26.08.25 - Ten video\
    source.mp4          <- file quay người nói
    assets\             <- ảnh minh họa gom được cho video này
```

**Bước 4.** Mở Claude Code tại thư mục đó và nói:

> edit video giúp tôi, source là source.mp4

Claude sẽ tự gọi skill `tabcom-video-edit`, bóc timestamp lời thoại, gom thêm ảnh, dựng cảnh, render,
nối OUTRO, rồi tự chạy tiếp `tabcom-video-thumbnail` để ra ảnh bìa.

Kết quả: `26.08.25 - Ten video (draft v1).mp4` + `... (thumb).jpg` nằm cùng thư mục.
Việc còn lại của người dùng: chèn nhạc nền trong CapCut.

## Trong gói có gì

```
skills/
  tabcom-video-edit/          Skill chính
    SKILL.md                  Toàn bộ quy trình + bài học đã đúc kết
    assets/                   Font, nền, OUTRO, logo sàn, sticker  <- dùng luôn, không cần tải
    scripts/                  Pipeline Python + script gom ảnh
      tabcom_paths.py         Quản lý đường dẫn — chạy file này để kiểm tra asset
    tai-lieu/
      quy-tac-video-tabcom.md Quy tắc bắt buộc cho mọi video (màu, font, vùng an toàn, giới hạn claim)
      Phan-tich-video-mau.md  Phân tích video mẫu, 5 kiểu cảnh chuẩn
  tabcom-video-thumbnail/     Skill tạo ảnh bìa, tự chạy sau khi render xong
cai-dat/
  README-cai-dat.md           Hướng dẫn cài môi trường
  requirements.txt            Thư viện Python
  tai_model.py                Tải trước model AI tách nền
```

## Cấu hình đường dẫn (chỉ khi chạy script tay)

Script trong skill không hardcode đường dẫn. Khi cần chạy trực tiếp, set biến môi trường:

```powershell
$env:TABCOM_SRC    = "D:\Video\26.08.25 - Ten video\source.mp4"
$env:TABCOM_OUT    = "D:\Video\26.08.25 - Ten video\26.08.25 - Ten video (draft v1).mp4"
$env:TABCOM_ASSETS = "D:\Video\26.08.25 - Ten video\assets"
```

Kiểm tra asset cố định có đủ không:

```powershell
python "$env:USERPROFILE\.claude\skills\tabcom-video-edit\scripts\tabcom_paths.py"
```

## Lưu ý về máy

Bước tách nền người chạy **17–50 giây mỗi frame** tùy máy, nên mỗi giây cảnh "người tách nền" tốn
7–20 phút render. Máy yếu thì dùng ít cảnh split lại, thay bằng lớp phủ đè lên hình người nói —
rẻ hơn nhiều mà vẫn sinh động. Chi tiết trong `SKILL.md`.
