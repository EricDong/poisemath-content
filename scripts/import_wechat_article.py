#!/usr/bin/env python3
"""
Import a WeChat public-account article into this Obsidian/Quartz content repo.

The script accepts a saved HTML file or a Markdown/plain-text file and writes a
matching article into both blog/ and publish/. Images referenced from local
paths are copied into media/ and publish/media/. Remote images are kept as-is
unless --download-images is passed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import shutil
import sys
import unicodedata
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "blog"
PUBLISH_DIR = ROOT / "publish"
MEDIA_DIR = ROOT / "media"
PUBLISH_MEDIA_DIR = PUBLISH_DIR / "media"

BLOCK_TAGS = {
    "address",
    "article",
    "aside",
    "blockquote",
    "div",
    "figure",
    "figcaption",
    "footer",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "header",
    "li",
    "main",
    "nav",
    "ol",
    "p",
    "pre",
    "section",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
}


def now_iso() -> str:
    return dt.datetime.now().replace(microsecond=0).isoformat()


def safe_slug(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    if slug:
        return slug[:80].strip("-")
    quoted = urllib.parse.quote(text, safe="")
    return quoted[:120].strip("%") or "wechat-article"


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def extract_frontmatter(markdown: str) -> tuple[dict[str, str], str]:
    if not markdown.startswith("---\n"):
        return {}, markdown
    end = markdown.find("\n---", 4)
    if end == -1:
        return {}, markdown
    raw = markdown[4:end].strip()
    body = markdown[end + 4 :].lstrip()
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def strip_frontmatter(markdown: str) -> str:
    return extract_frontmatter(markdown)[1]


def collapse_blank_lines(markdown: str) -> str:
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


class WeChatHTMLToMarkdown(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.href_stack: list[str | None] = []
        self.skip_depth = 0
        self.list_stack: list[dict[str, int | str]] = []
        self.in_pre = False
        self.title: str | None = None
        self._title_parts: list[str] = []
        self._in_title = False

    def markdown(self) -> str:
        return collapse_blank_lines("".join(self.parts))

    def append(self, text: str) -> None:
        if not text:
            return
        self.parts.append(text)

    def newline(self, count: int = 2) -> None:
        current = "".join(self.parts)
        stripped = current.rstrip(" \t")
        self.parts = [stripped]
        existing = len(current) - len(current.rstrip("\n"))
        needed = max(count - existing, 0)
        self.append("\n" * needed)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs_dict = {key.lower(): value or "" for key, value in attrs}

        if tag in {"script", "style", "svg"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return

        if tag == "title":
            self._in_title = True
            self._title_parts = []
            return

        if tag in BLOCK_TAGS:
            self.newline(2)

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1])
            self.append("#" * level + " ")
        elif tag == "br":
            self.newline(1)
        elif tag == "hr":
            self.newline(2)
            self.append("---")
            self.newline(2)
        elif tag == "blockquote":
            self.append("> ")
        elif tag == "strong" or tag == "b":
            self.append("**")
        elif tag == "em" or tag == "i":
            self.append("*")
        elif tag == "code" and not self.in_pre:
            self.append("`")
        elif tag == "pre":
            self.in_pre = True
            self.append("```")
            self.newline(1)
        elif tag == "a":
            self.href_stack.append(attrs_dict.get("href"))
            self.append("[")
        elif tag == "img":
            src = attrs_dict.get("data-src") or attrs_dict.get("src")
            alt = attrs_dict.get("alt", "")
            if src:
                self.newline(2)
                self.append(f"![{alt}]({src})")
                self.newline(2)
        elif tag in {"ul", "ol"}:
            self.list_stack.append({"tag": tag, "index": 1})
        elif tag == "li":
            indent = "  " * max(len(self.list_stack) - 1, 0)
            marker = "- "
            if self.list_stack and self.list_stack[-1]["tag"] == "ol":
                marker = f"{self.list_stack[-1]['index']}. "
                self.list_stack[-1]["index"] = int(self.list_stack[-1]["index"]) + 1
            self.append(indent + marker)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "svg"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return

        if tag == "title":
            self._in_title = False
            title = " ".join("".join(self._title_parts).split())
            self.title = title or self.title
            return

        if tag == "a":
            href = self.href_stack.pop() if self.href_stack else None
            self.append(f"]({href})" if href else "]")
        elif tag in {"strong", "b"}:
            self.append("**")
        elif tag in {"em", "i"}:
            self.append("*")
        elif tag == "code" and not self.in_pre:
            self.append("`")
        elif tag == "pre":
            self.newline(1)
            self.append("```")
            self.in_pre = False
            self.newline(2)
        elif tag in {"ul", "ol"} and self.list_stack:
            self.list_stack.pop()

        if tag in BLOCK_TAGS and tag not in {"ul", "ol"}:
            self.newline(2)

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self._in_title:
            self._title_parts.append(data)
            return
        if self.in_pre:
            self.append(data)
            return
        text = html.unescape(data)
        text = re.sub(r"\s+", " ", text)
        if text.strip():
            self.append(text)


def html_to_markdown(source: str) -> tuple[str, str | None]:
    parser = WeChatHTMLToMarkdown()
    parser.feed(source)
    return parser.markdown(), parser.title


def rewrite_and_copy_images(markdown: str, article_slug: str, source_dir: Path, download: bool) -> str:
    image_re = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    counter = 0

    def replacement(match: re.Match[str]) -> str:
        nonlocal counter
        alt, src = match.group(1), match.group(2).strip()
        parsed = urllib.parse.urlparse(src)

        if parsed.scheme in {"http", "https"} and not download:
            return match.group(0)

        suffix = Path(parsed.path).suffix
        if not suffix or len(suffix) > 8:
            suffix = ".jpg"
        counter += 1
        filename = f"{article_slug}-{counter:02d}{suffix.lower()}"
        target = MEDIA_DIR / filename
        publish_target = PUBLISH_MEDIA_DIR / filename

        try:
            if parsed.scheme in {"http", "https"}:
                request = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(request, timeout=20) as response:
                    target.write_bytes(response.read())
            else:
                local_src = Path(urllib.parse.unquote(src))
                if not local_src.is_absolute():
                    local_src = source_dir / local_src
                shutil.copy2(local_src, target)
            shutil.copy2(target, publish_target)
            return f"![{alt}](../media/{filename})"
        except Exception as exc:  # noqa: BLE001
            print(f"warning: could not import image {src}: {exc}", file=sys.stderr)
            return match.group(0)

    return image_re.sub(replacement, markdown)


def build_frontmatter(
    title: str,
    date: str,
    modified: str,
    slug: str,
    source_url: str | None,
    tags: list[str],
    draft: bool,
) -> str:
    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"date: {yaml_quote(date)}",
        f"modified: {yaml_quote(modified)}",
        f"slug: {yaml_quote(slug)}",
    ]
    if source_url:
        lines.append(f"source: {yaml_quote(source_url)}")
    if tags:
        lines.append("tags:")
        lines.extend(f"  - {yaml_quote(tag)}" for tag in tags)
    if draft:
        lines.append("draft: true")
    lines.append("---")
    return "\n".join(lines) + "\n"


def infer_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        match = re.match(r"^#\s+(.+)$", line.strip())
        if match:
            return match.group(1).strip()
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("!"):
            return stripped[:60]
    return fallback


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import a WeChat article into blog/ and publish/.")
    parser.add_argument("input", type=Path, help="Saved .html/.htm/.md/.txt article file.")
    parser.add_argument("--title", help="Article title. Defaults to HTML <title>, first H1, or filename.")
    parser.add_argument("--date", help="Article date, for example 2026-06-14 or 2026-06-14T09:30:00.")
    parser.add_argument("--slug", help="URL/file slug. Defaults to an ASCII slug from the title.")
    parser.add_argument("--source-url", help="Original WeChat article URL.")
    parser.add_argument("--tag", action="append", default=[], help="Tag to add. Can be repeated.")
    parser.add_argument("--draft", action="store_true", help="Mark the publish copy as draft.")
    parser.add_argument("--download-images", action="store_true", help="Download remote images into media/.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing target Markdown files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_path = args.input.resolve()
    if not source_path.exists():
        print(f"error: input file not found: {source_path}", file=sys.stderr)
        return 1

    raw = source_path.read_text(encoding="utf-8")
    existing_frontmatter, _ = extract_frontmatter(raw)
    html_title: str | None = None

    if source_path.suffix.lower() in {".html", ".htm"} or re.search(r"<(?:html|body|section|p|div)\b", raw, re.I):
        markdown, html_title = html_to_markdown(raw)
    else:
        markdown = collapse_blank_lines(strip_frontmatter(raw))

    title = args.title or existing_frontmatter.get("title") or html_title or infer_title(markdown, source_path.stem)
    slug = args.slug or existing_frontmatter.get("slug") or safe_slug(title)
    date = args.date or existing_frontmatter.get("date") or now_iso()
    modified = now_iso()
    tags = args.tag or ["微信公众号", "聪明的提问者"]

    BLOG_DIR.mkdir(exist_ok=True)
    PUBLISH_DIR.mkdir(exist_ok=True)
    MEDIA_DIR.mkdir(exist_ok=True)
    PUBLISH_MEDIA_DIR.mkdir(exist_ok=True)

    markdown = rewrite_and_copy_images(markdown, slug, source_path.parent, args.download_images)
    frontmatter = build_frontmatter(
        title=title,
        date=date,
        modified=modified,
        slug=slug,
        source_url=args.source_url,
        tags=tags,
        draft=args.draft,
    )
    article = frontmatter + markdown

    date_prefix = date[:10] if re.match(r"\d{4}-\d{2}-\d{2}", date) else dt.date.today().isoformat()
    filename = f"{date_prefix}-{slug}.md"
    targets = [BLOG_DIR / filename, PUBLISH_DIR / filename]
    existing = [target for target in targets if target.exists()]
    if existing and not args.overwrite:
        print("error: target file exists; pass --overwrite to replace:", file=sys.stderr)
        for target in existing:
            print(f"  {target.relative_to(ROOT)}", file=sys.stderr)
        return 1

    for target in targets:
        target.write_text(article, encoding="utf-8")

    print("Imported WeChat article:")
    for target in targets:
        print(f"  {target.relative_to(ROOT)}")
    print()
    print("Next steps:")
    print(f"  - Review publish/{filename} in Obsidian.")
    print("  - Add it to publish/index.md when you want it linked from the home page.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
