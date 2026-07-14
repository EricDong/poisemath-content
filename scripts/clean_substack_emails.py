#!/usr/bin/env python3
"""清洗 Substack 邮件存档为纯正文 Markdown。

用法:
    python3 scripts/clean_substack_emails.py [--src materials/substack] [--out materials/substack-clean]

产出:
    - materials/substack-clean/<原文件名>.md  (纯正文)
    - materials/substack-clean/MANIFEST.md    (篇目清单: 日期/标题/副标题/字数)

清洗规则:
    - 跳过非正文邮件(收据/欢迎信/促销/订阅确认)
    - 去掉邮件头: Forwarded this email / banner 图 / 重复的带链接标题 / 署名行 / 日期行 / 空链接 / READ IN APP
    - 去掉页脚: Invite friends / Like/Comment/Restack / 版权退订块
    - 解码 substack.com/redirect/2/<base64> 跳转链接为真实 URL
    - 图片路径 _assets/ 改写为 ../substack/_assets/ (清洗稿放在兄弟目录仍可显示)
"""

import argparse
import base64
import json
import re
from pathlib import Path

# 标题里含这些关键词的判定为非正文邮件
SKIP_TITLE_PATTERNS = [
    r"payment receipt",
    r"You-?'?re on the list",
    r"subscriptions for you to give away",
    r"Oops! Did you forget",
    r"Here.?s \$25",
    r"Welcome to The Learning Dispatch",
]

# 页脚起始标记: 命中任意一个即截断
FOOTER_MARKERS = [
    r"^#{1,6}\s+.*Invite your friends",
    r"^Invite your friends and earn rewards",
    r"^\[Invite Friends\]",
    r"^\[Like\]\(https://substack\.com/app-link",
    r"^You.?re currently a free subscriber",
    r"^© 20\d\d ",
    r"^\[Unsubscribe\]",
    r"^\[Upgrade to paid\]\(",
]

# 整行删除的噪音
NOISE_LINE_PATTERNS = [
    r"^Forwarded this email\?",
    r"^\[\]\(http[^)]*\)\s*$",                      # 空文本链接(点赞/评论/转发按钮)
    r"^\[?READ IN APP\]?\(",
    r"^\[Carl Hendrick\]\(https://substack\.com/@carlhendrick\)\s*$",
    r"^[A-Z][a-z]{2}\s+\d{1,2}\s*$",                 # 独立日期行 "Jun 20"
    r"^\[Share\]\(http[^)]*\)\s*$",
    r"^\[Leave a comment\]\(http[^)]*\)\s*$",
    r"^\[Subscribe now\]\(http[^)]*\)\s*$",
    r"^\[Upgrade to paid\]\(http[^)]*\)\s*$",
    r"^Thanks for reading.*[Ss]ubscribe",
]

REDIRECT2_RE = re.compile(r"https://substack\.com/redirect/2/([A-Za-z0-9_-]+={0,2})")


def decode_redirect(url_match: re.Match) -> str:
    """substack.com/redirect/2/<jwt-like base64> 的 payload 里 e 字段是真实 URL。"""
    token = url_match.group(1)
    try:
        payload = token + "=" * (-len(token) % 4)
        data = json.loads(base64.urlsafe_b64decode(payload))
        real = data.get("e", "")
        if real.startswith("http"):
            return real.split("?utm_")[0]  # 顺手去掉 utm 参数
    except Exception:
        pass
    return url_match.group(0)


def clean_body(text: str) -> tuple[str, str]:
    """返回 (正文, 副标题)。"""
    # READ IN APP 跨行块: "[\n\nREAD IN APP](url)"
    text = re.sub(r"\[\s*\n+\s*READ IN APP\]\([^)]*\)", "", text)
    # 解码 redirect/2 链接 (可能带尾随 query, 截到右括号前)
    text = re.sub(r"https://substack\.com/redirect/2/([A-Za-z0-9_.-]+)\?[^)\s]*", decode_redirect, text)
    text = REDIRECT2_RE.sub(decode_redirect, text)

    lines = text.split("\n")

    # 找到重复的带链接标题 "# [Title](...)" —— 其之前的内容全是邮件头
    body_start = 0
    subtitle = ""
    for i, line in enumerate(lines[:40]):
        if re.match(r"^#\s+\[", line):
            body_start = i + 1
            # 紧随其后的 "### 副标题"
            for j in range(i + 1, min(i + 8, len(lines))):
                if lines[j].startswith("### "):
                    subtitle = lines[j][4:].strip().strip("*").strip()
                    body_start = j + 1
                    break
                if lines[j].strip() and not lines[j].startswith("#"):
                    break
            break

    # 页脚截断
    body_end = len(lines)
    for i in range(body_start, len(lines)):
        if any(re.match(p, lines[i]) for p in FOOTER_MARKERS):
            body_end = i
            break

    kept = []
    for line in lines[body_start:body_end]:
        if any(re.match(p, line) for p in NOISE_LINE_PATTERNS):
            continue
        # 图片路径改写, 保持 Obsidian 里可预览
        line = line.replace("(_assets/", "(../substack/_assets/")
        kept.append(line)

    body = "\n".join(kept)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body, subtitle


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="materials/substack")
    ap.add_argument("--out", default="materials/substack-clean")
    args = ap.parse_args()

    src, out = Path(args.src), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    manifest, skipped = [], []
    for f in sorted(src.glob("*.md")):
        raw = f.read_text(encoding="utf-8")

        if any(re.search(p, f.name, re.IGNORECASE) for p in SKIP_TITLE_PATTERNS):
            skipped.append(f.name)
            continue

        # frontmatter
        fm = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
        title = date = ""
        if fm:
            m = re.search(r'^title:\s*"?(.*?)"?\s*$', fm.group(1), re.MULTILINE)
            title = m.group(1) if m else ""
            m = re.search(r"^date:\s*(\S+)", fm.group(1), re.MULTILINE)
            date = m.group(1) if m else ""
            raw = raw[fm.end():]

        body, subtitle = clean_body(raw)
        words = len(body.split())
        if words < 200:  # 正文过短的也标记跳过(多半是通知类邮件)
            skipped.append(f"{f.name} (仅 {words} 词)")
            continue

        header = f"---\ntitle: \"{title}\"\ndate: {date}\nsource: Carl Hendrick, The Learning Dispatch\n"
        if subtitle:
            header += f"subtitle: \"{subtitle}\"\n"
        header += "---\n\n"
        (out / f.name).write_text(header + f"# {title}\n\n" + body + "\n", encoding="utf-8")
        manifest.append((date, title, subtitle, words, f.name))

    # 清单
    lines = ["# Substack 素材篇目清单\n", f"共 {len(manifest)} 篇正文, 跳过 {len(skipped)} 封非正文邮件。\n",
             "| 日期 | 标题 | 副标题 | 英文词数 |", "|------|------|--------|------|"]
    for date, title, subtitle, words, _fname in manifest:
        lines.append(f"| {date} | {title} | {subtitle} | {words} |")
    lines.append("\n## 跳过的邮件\n")
    lines += [f"- {s}" for s in skipped]
    (out / "MANIFEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"清洗完成: {len(manifest)} 篇 → {out}/ , 跳过 {len(skipped)} 封, 清单见 {out}/MANIFEST.md")


if __name__ == "__main__":
    main()
