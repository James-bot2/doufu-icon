# doufu 图标库（Emby / Forward 风格）

对标 `https://emby-icon.vercel.app/TFEL-Avatar.json` 的结构：

```json
{
  "name": "doufu头像",
  "description": "...",
  "icons": [
    { "name": "T", "url": "https://<domain>/icons/T.png" }
  ]
}
```

## 目录

- `icons/` — 透明 PNG 图标，每张一张文件，文件名即图标名
- `doufu-avatar.json` — 对外发布的图标库 JSON（由脚本生成，不要手改）
- `build_json.py` — 扫描 `icons/*.png` 生成 JSON

## 加新图标的流程（你发照片 → 我来做）

1. 你把照片发我，我会做成正方形透明 PNG（512px），以你定的名字放进 `icons/`。
2. 跑 `python3 build_json.py --base-url https://<部署域名> --name "doufu头像" --description "..."` 重新生成 JSON。
3. push 到 GitHub，Cloudflare Pages 自动重新部署，JSON 和新图即时生效。

## 部署目标（待你确认）

- 方案 A（推荐）：公开 GitHub 仓库 + Cloudflare Pages + 自定义域名，
  布局与 vercel 示例完全一致：`/doufu-avatar.json` + `/icons/*.png`。
- 方案 B：Cloudflare Worker + KV/R2，不走 GitHub。
