# Tabcom Video Edit

Gồm 2 skill: `tabcom-video-edit` (dựng video dọc 9:16) và `tabcom-video-thumbnail` (ảnh bìa).

## Cài qua Claude Code (plugin)

```
/plugin marketplace add Annie-246/tabcom-video-edit-skill
/plugin install tabcom-video-edit@tabcom-video-edit
```

Sau khi cài, khởi động lại Claude Code để skill được nạp.

## Yêu cầu máy

ffmpeg, Python 3 (Pillow, onnxruntime...) và model tách nền. Xem `DOC-DAU-TIEN.md` và `cai-dat/` (`requirements.txt`, `tai_model.py`) để cài.

## License

MIT
