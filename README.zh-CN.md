# Pi Top 300

[English](README.md)

一个持续维护的 Pi 官方热门包分类与推荐目录，整理 [Pi 官方 Package Catalog](https://pi.dev/packages) 中按 `All types → Most downloads` 排名的前 300 个包。

## 项目用途

Pi Top 300 按“工具能做什么”帮助用户发现扩展、Skills、Prompt、Theme 和其他 Pi 包，而不只是按包名查找。

项目区分两件事：

- **热门程度**：在某个记录时间点进入 Pi 官方目录前 300；
- **推荐程度**：根据用途、维护信号、兼容性、重复功能、安全性和实际价值进行人工判断。

热门不等于质量高或安全。Pi 包可能以当前用户权限执行代码，安装前应检查源码和权限。

## 当前快照

- 来源：[`pi.dev/packages?sort=downloads`](https://pi.dev/packages?sort=downloads)
- 范围：All types、Most downloads、排名 1–300
- 快照日期：`2026-08-13`
- 结构化数据：[`data/packages-latest.json`](data/packages-latest.json)
- **完整 300 个包清单就在本 README 下方**；
- 原始数据：[`data/packages-latest.json`](data/packages-latest.json)；
- 历史快照：[`data/snapshots/`](data/snapshots/)。

## 主要类别

- Agent 编排、Subagent、Plan、Goal 和 Task
- Context、Memory、知识库和 Compaction
- Web、浏览器、科研检索和 MCP
- 代码智能、编辑和代码 Review
- 模型、Provider、模型路由、用量和缓存
- 安全、权限和 Sandbox
- UI、TUI、Session 和观测
- Skills、Prompts、Rules 和结构化提问
- 后台任务、Runtime、Worktree 和外部平台集成

代表包和选择建议见[分类指南](docs/categories.md)。本 README 下方直接列出全部 300 个包、排名、描述和安装命令。

## 更新方式

项目保存带日期的原始快照，不直接覆盖历史。后续更新应：

1. 抓取 Pi 官方目录；
2. 保存 `data/snapshots/YYYY-MM-DD.json`；
3. 更新 `data/packages-latest.json`；
4. 重新生成[`docs/packages.md`](docs/packages.md)；
5. 将人工分类和推荐意见与抓取数据分开维护；
6. 通过 Pull Request 审核后合并。

GitHub Actions 已配置为每周创建更新 Pull Request。

## 说明

下载量是 Pi 页面记录时显示的 npm 月下载量，不是独立用户数。排名会变化；包描述和仓库链接也可能过时。

## 许可证

项目代码和编辑文档采用 MIT 许可证。包名、描述、商标和上游源码归各自作者所有。
