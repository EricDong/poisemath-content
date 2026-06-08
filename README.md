# poisemath.com (content)

Obsidian vault — 内容源。

构建与部署由 [`poisemath-site`](https://github.com/EricDong/poisemath-site) 仓库通过 Quartz + Cloudflare Pages 完成。

## 写作流程

1. 在 Obsidian 里写笔记
2. Obsidian Git 插件每 10 分钟自动 commit + push
3. push 触发 site repo 重新构建
4. Cloudflare Pages 部署到 poisemath.com

## 不发布

只有 `publish/` 目录会发布到网站；其他目录默认不发布。

`publish/` 里的笔记如果暂时不想发布，frontmatter 加 `draft: true` 即可。
