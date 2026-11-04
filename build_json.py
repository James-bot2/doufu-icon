#!/usr/bin/env python3
"""Generate the icon-library JSON from icons/*.png.

Usage:
    python3 build_json.py --base-url https://icon.example.com \
        --name "doufu头像" --description "..." --out doufu-avatar.json

Each PNG file stem becomes the icon `name`; the url is
<base-url>/icons/<filename>. Re-run after every new icon.
"""
import argparse
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True, help="Public base URL, no trailing slash")
    ap.add_argument("--name", required=True)
    ap.add_argument("--description", default="")
    ap.add_argument("--out", default="doufu-avatar.json")
    args = ap.parse_args()

    icons_dir = os.path.join(HERE, "icons")
    files = sorted(
        f for f in os.listdir(icons_dir)
        if f.lower().endswith(".png") and os.path.isfile(os.path.join(icons_dir, f))
    )
    base = args.base_url.rstrip("/")
    icons = [{"name": os.path.splitext(f)[0], "url": f"{base}/icons/{f}"} for f in files]
    data = {"name": args.name, "description": args.description, "icons": icons}
    out_path = os.path.join(HERE, args.out)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"wrote {out_path} with {len(icons)} icons")


if __name__ == "__main__":
    main()
