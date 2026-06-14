# poisemath.com (content)

Obsidian vault — 内容源。

构建与部署由 [`poisemath-site`](https://github.com/EricDong/poisemath-site) 仓库通过 Quartz + Cloudflare Pages 完成。

## 写作流程

1. 在 Obsidian 里写笔记
2. Obsidian Git 插件每 10 分钟自动 commit + push
3. push 触发 site repo 重新构建
4. Cloudflare Pages 部署到 poisemath.com

## 迁移微信公众号文章

公众号「聪明的提问者」里的文章可以先保存成 HTML 或 Markdown，再导入到本站。

### 单篇导入

1. 在微信公众平台打开文章预览页，另存为 HTML，或把正文复制到一个 `.md` 文件。
2. 运行导入脚本：

```bash
python3 scripts/import_wechat_article.py /path/to/article.html \
  --title "文章标题" \
  --date 2026-06-14 \
  --slug article-slug \
  --source-url "https://mp.weixin.qq.com/..."
```

脚本会生成两份内容：

- `blog/文章标题.md`：源稿备份
- `publish/文章标题.md`：网站发布稿

如果文章里引用的是本地图片，脚本会复制到 `media/` 和 `publish/media/`。如果图片仍是微信公众号远程地址，默认保留原地址；需要下载远程图片时加 `--download-images`。

导入后先在 Obsidian 里校对 `publish/` 里的文章。确认要放到首页时，再手动把链接加到 `publish/index.md`。

## 不发布

只有 `publish/` 目录会发布到网站；其他目录默认不发布。

`publish/` 里的笔记如果暂时不想发布，frontmatter 加 `draft: true` 即可。
