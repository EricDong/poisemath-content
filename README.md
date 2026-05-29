# poiseacademy.com (content)

Obsidian vault — 内容源。

构建与部署由 [`poiseacademy-site`](https://github.com/EricDong/poiseacademy-site) 仓库通过 Quartz + Cloudflare Pages 完成。

## 写作流程

1. 在 Obsidian 里写笔记
2. Obsidian Git 插件每 10 分钟自动 commit + push
3. push 触发 site repo 重新构建
4. Cloudflare Pages 部署到 poiseacademy.com

## 不发布

frontmatter 加 `draft: true` 即可。
