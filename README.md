# Pi Top 300

Pi 官方 Package Catalog 前 300 热门包的用途分类目录（All types · Most downloads）。

[分类指南](docs/categories.md) · [按排名清单](docs/packages.md) · [原始 JSON 数据](data/packages-latest.json)

> ⚠️ Pi 包可能以当前用户权限执行代码，安装前请审查源码和权限。
> 下载量为 npm 月下载量，不代表质量或安全性。分类基于名称和描述的初步归类，人工意见维护在 `data/categories.yaml`。

- 快照 `2026-09-28`（[历史快照](data/snapshots/)）· 共 300 包

## 分类总览

| 类别 | 数量 | 占比 |
| --- | ---: | ---: |
| [Web / Browser / Research / MCP](#web-browser-research-mcp) | 44 | 15% |
| [Context / Memory / Knowledge / Compaction](#context-memory-knowledge-compaction) | 39 | 13% |
| [Agent 编排 / Subagent / Plan / Goal / Task](#agent-编排-subagent-plan-goal-task) | 39 | 13% |
| [UI / TUI / Session / 观测](#ui-tui-session-观测) | 37 | 12% |
| [模型 / Provider / 路由 / 用量](#模型-provider-路由-用量) | 36 | 12% |
| [Runtime / 后台任务 / Worktree / 集成](#runtime-后台任务-worktree-集成) | 31 | 10% |
| [Skills / Prompt / Rules / 提问](#skills-prompt-rules-提问) | 28 | 9% |
| [代码智能 / 编辑 / Review](#代码智能-编辑-review) | 21 | 7% |
| [安全 / 权限 / Sandbox](#安全-权限-sandbox) | 16 | 5% |
| [其他 / 待复核](#其他-待复核) | 9 | 3% |

## 按类别清单

### Web / Browser / Research / MCP

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 3 | [pi-web-access](https://pi.dev/packages/pi-web-access) | 443,475/mo | extension | 为 Pi 编码代理提供网页搜索、URL 抓取、GitHub 仓库克隆、PDF 提取、YouTube 视频理解与本地视频分析。支持 OpenAI、Brave、Parallel、TinyFish、Search1API、Searchinfinity、Querit、Tavily、Firecrawl、Jina、SERPdive、Ka | `pi install npm:pi-web-access` |
| 8 | [@companion-ai/feynman](https://pi.dev/packages/@companion-ai/feynman) | 160,424/mo | package | 基于 Pi 和 alphaXiv 构建的研究优先 CLI 代理 | `pi install npm:@companion-ai/feynman` |
| 30 | [@ff-labs/pi-fff](https://pi.dev/packages/@ff-labs/pi-fff) | 37,850/mo | extension | pi 扩展：由 FFF 驱动的模糊文件与内容搜索。 | `pi install npm:@ff-labs/pi-fff` |
| 35 | [@quintinshaw/pi-dynamic-workflows](https://pi.dev/packages/@quintinshaw/pi-dynamic-workflows) | 32,615/mo | package | 面向 Pi 的 Claude Code 风格动态工作流：将任务扇出至数百个子代理，具备真实模型路由、token/成本核算、断点续跑、git 工作树隔离、交互式 /workflows TUI，以及真正的 /deep-research。 | `pi install npm:@quintinshaw/pi-dynamic-workflows` |
| 39 | [@agimon-ai/log-sink-mcp](https://pi.dev/packages/@agimon-ai/log-sink-mcp) | 29,656/mo | package | 支持 HTTP 摄取与 AI 分析的日志汇聚（log sink）MCP 服务器。 | `pi install npm:@agimon-ai/log-sink-mcp` |
| 41 | [pi-web-ui](https://pi.dev/packages/pi-web-ui) | 27,129/mo | package | 基于 pi SDK（@earendil-works/pi-coding-agent）的 pi 编码代理 Web 聊天界面——一条命令即可运行，支持 Docker/systemd/launchd 部署。 | `pi install npm:pi-web-ui` |
| 61 | [pi-agent-browser-native](https://pi.dev/packages/pi-agent-browser-native?page=2) | 17,825/mo | extension | pi 扩展，将 agent-browser 作为原生工具开放，用于浏览器自动化。 | `pi install npm:pi-agent-browser-native` |
| 64 | [@mjasnikovs/pi-task](https://pi.dev/packages/@mjasnikovs/pi-task?page=2) | 17,244/mo | extension | 为本地模型提供确定性的任务规划与规格编排：崩溃安全的 /task 流水线，带 verify/enforce 关卡、实时远程 Web 视图，以及 web/docs/fetch/worker 子代理工具。 | `pi install npm:@mjasnikovs/pi-task` |
| 69 | [@onkernel/browser-loop](https://pi.dev/packages/@onkernel/browser-loop?page=2) | 16,017/mo | extension | Browser tools for your agent: framework-neutral tool catalog, per-model compilation, Kernel-browser execution, and a pi binding + extension | `pi install npm:@onkernel/browser-loop` |
| 74 | [@agimon-ai/doompi-web-components](https://pi.dev/packages/@agimon-ai/doompi-web-components?page=2) | 14,657/mo | theme | Shared web components and theme tokens for the DoomPi cockpit and its web plugins: shadcn-style primitives on Radix, tuned to the Doom palette, with runtime theme configs. | `pi install npm:@agimon-ai/doompi-web-components` |
| 82 | [@selesai/code](https://pi.dev/packages/@selesai/code?page=2) | 12,467/mo | package | 持续维护、以扩展为先的 Pi coding agent，内置工作流、子代理、网页研究、提问、技能包以及增强的终端 UI。 | `pi install npm:@selesai/code` |
| 90 | [donsetch](https://pi.dev/packages/donsetch?page=2) | 11,658/mo | package | 面向 AI 代理的网页抓取、搜索与爬取能力。零 API 密钥。Chrome 级真实 TLS。 | `pi install npm:donsetch` |
| 101 | [pi-markdown-preview](https://pi.dev/packages/pi-markdown-preview?page=3) | 10,319/mo | package | 面向 pi 的渲染版 Markdown + LaTeX 预览，支持终端、浏览器和 PDF 输出。 | `pi install npm:pi-markdown-preview` |
| 103 | [@ollama/pi-web-search](https://pi.dev/packages/@ollama/pi-web-search?page=3) | 10,190/mo | extension | 面向 Pi 代理的网络搜索与抓取工具——使用 Ollama 的网络搜索与抓取 API。 | `pi install npm:@ollama/pi-web-search` |
| 110 | [@agimon-ai/doompi](https://pi.dev/packages/@agimon-ai/doompi?page=3) | 8,954/mo | package | 为受限范围的代理工具、技能包（skills）、MCP 服务器与开发者工作流提供的一套有主张、可组合的 Pi 发行版。 | `pi install npm:@agimon-ai/doompi` |
| 116 | [@jmfederico/pi-web](https://pi.dev/packages/@jmfederico/pi-web?page=3) | 8,832/mo | package | 为真实工作区中持久化的 Pi Coding Agent 会话提供 Web UI。 | `pi install npm:@jmfederico/pi-web` |
| 120 | [@narumitw/pi-firecrawl](https://pi.dev/packages/@narumitw/pi-firecrawl?page=3) | 8,618/mo | extension | Pi 扩展，提供 Firecrawl 网页抓取与爬取工具。 | `pi install npm:@narumitw/pi-firecrawl` |
| 121 | [@juicesharp/rpiv-web-tools](https://pi.dev/packages/@juicesharp/rpiv-web-tools?page=3) | 8,591/mo | extension | Pi 扩展。为模型提供网络搜索与抓取能力，支持可插拔的模型提供方（Brave、Tavily、Serper、Exa、You.com、Jina、Firecrawl、Perplexity、SearXNG、Ollama）。 | `pi install npm:@juicesharp/rpiv-web-tools` |
| 126 | [@agimon-ai/doompi-domain](https://pi.dev/packages/@agimon-ai/doompi-domain?page=3) | 8,257/mo | extension, skill | Domain selection, resource staging, and MCP scoping for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-domain` |
| 140 | [@agimon-ai/doompi-skill](https://pi.dev/packages/@agimon-ai/doompi-skill?page=3) | 7,847/mo | extension | Session skill catalogue, deferred skill discovery, and the skill browser for DoomPi. | `pi install npm:@agimon-ai/doompi-skill` |
| 149 | [@bacnh85/pi-web](https://pi.dev/packages/@bacnh85/pi-web?page=3) | 7,641/mo | extension | Pi extension for web search, page extraction, Firecrawl scraping/crawling, Crawl4AI headless browser crawling, real-browser interaction (trusted click/type/evaluate via CDP), Gemini web-tier research, free upstream image generation (Gemini/ChatGPT web/Z.a | `pi install npm:@bacnh85/pi-web` |
| 153 | [@agimon-ai/doompi-mcp](https://pi.dev/packages/@agimon-ai/doompi-mcp?page=4) | 7,547/mo | extension | 为使用 DoomPi 组合的 Pi 会话提供领域感知（domain-aware）的 MCP 服务器选择与访问边界。 | `pi install npm:@agimon-ai/doompi-mcp` |
| 167 | [opencode-codebase-index](https://pi.dev/packages/opencode-codebase-index?page=4) | 7,135/mo | package | 宿主无关的语义化代码库搜索，支持嵌入（embeddings）、符号发现与调用图工具。 | `pi install npm:opencode-codebase-index` |
| 174 | [@agimon-ai/doompi-web-contracts](https://pi.dev/packages/@agimon-ai/doompi-web-contracts?page=4) | 6,902/mo | package | Web cockpit plugin contracts for DoomPi: plugin definitions, slot contributions, session data channels, and hub channel sources. | `pi install npm:@agimon-ai/doompi-web-contracts` |
| 185 | [awesome-pi-themes](https://pi.dev/packages/awesome-pi-themes?page=4) | 6,483/mo | theme | 精心挑选的 46 款 Pi Coding Agent 原创深色主题合集，附带实时网页预览。 | `pi install npm:awesome-pi-themes` |
| 186 | [pi2dsh](https://pi.dev/packages/pi2dsh?page=4) | 6,331/mo | package | 打通 Pi 与 DeepSeek Harness 生态系统：一种通用的 Pi Host ABI，可将未经修改的 Pi 扩展作为原生 DSH 插件运行，并支持兼容性检查以及 Pi 到 DSH 的 MCP 配置转换。 | `pi install npm:pi2dsh` |
| 195 | [dripline](https://pi.dev/packages/dripline?page=4) | 6,143/mo | package | 一次一滴地查询任何内容。 | `pi install npm:dripline` |
| 200 | [@xynogen/pix-pretty](https://pi.dev/packages/@xynogen/pix-pretty?page=4) | 6,066/mo | extension | 增强的工具输出渲染：语法高亮、文件图标、树形视图、diff 渲染和 FFF 搜索 | `pi install npm:@xynogen/pix-pretty` |
| 203 | [@magiusche/pi-webview](https://pi.dev/packages/@magiusche/pi-webview?page=5) | 5,845/mo | extension | pi 编码代理的 WebView 界面，集成到 IDE 中（优先支持 VS Code）。 | `pi install npm:@magiusche/pi-webview` |
| 215 | [@amaster.ai/pi-browser-use](https://pi.dev/packages/@amaster.ai/pi-browser-use?page=5) | 5,208/mo | extension | Pi 扩展，通过 chrome-devtools-mcp 实现浏览器自动化，提供 browser_ 前缀的工具。 | `pi install npm:@amaster.ai/pi-browser-use` |
| 229 | [pi-autoresearch](https://pi.dev/packages/pi-autoresearch?page=5) | 5,001/mo | extension | 面向 pi 的自主实验循环——运行、度量、保留或舍弃。灵感来自 karpathy/autoresearch。 | `pi install npm:pi-autoresearch` |
| 231 | [pi-docparser](https://pi.dev/packages/pi-docparser?page=5) | 4,991/mo | extension, skill | Pi package that adds document_parse, document_search, document_screenshot, and a companion skill for local document understanding with LiteParse v2. | `pi install npm:pi-docparser` |
| 236 | [pi-control-chrome](https://pi.dev/packages/pi-control-chrome?page=5) | 4,920/mo | package | Codex-aligned Chrome and Edge browser control for Pi, Codex and DSH | `pi install npm:pi-control-chrome` |
| 243 | [pi-browser-use](https://pi.dev/packages/pi-browser-use?page=5) | 4,836/mo | extension | Opinionated browser automation via chrome-devtools-mcp: native Pi extension and portable Agent Plugins 1.0 skills + MCP server. | `pi install npm:pi-browser-use` |
| 253 | [@estebanforge/pi-antigravity-bridge](https://pi.dev/packages/@estebanforge/pi-antigravity-bridge?page=6) | 4,643/mo | extension | Gemini provider for Pi on the Antigravity ACP server (official Google ACP) or the stream-json agy CLI. antigravity/* models in Pi's /model picker, no-patch MCP bridge: agy runs Pi's tools. ToS safe to use. | `pi install npm:@estebanforge/pi-antigravity-bridge` |
| 255 | [pi-cloudflare](https://pi.dev/packages/pi-cloudflare?page=6) | 4,630/mo | extension | Cloudflare Agent Plugin and native Pi extension providing official skills and cf_-prefixed MCP tools. | `pi install npm:pi-cloudflare` |
| 256 | [@amaster.ai/pi-web-access](https://pi.dev/packages/@amaster.ai/pi-web-access?page=6) | 4,618/mo | extension | Pi 扩展，提供网页搜索、URL 内容提取和图片搜索（Tavily、Kimi、DeepSeek、Mimo、Z.AI、DashScope、Unsplash 等）。 | `pi install npm:@amaster.ai/pi-web-access` |
| 259 | [pi-extension-qwen-token-plan-cn-ex](https://pi.dev/packages/pi-extension-qwen-token-plan-cn-ex?page=6) | 4,559/mo | extension | Enhanced Qwen Token Plan CN provider for pi. Speaks the OpenAI Responses API (not chat-completions) to activate the platform's server-side Harness tools — web search, code interpreter, web extraction, and image search — that the built-in qwen-token-plan-c | `pi install npm:pi-extension-qwen-token-plan-cn-ex` |
| 260 | [@fadhilp/pylon](https://pi.dev/packages/@fadhilp/pylon?page=6) | 4,540/mo | package | Pi workflow extensions and a local web interface. | `pi install npm:@fadhilp/pylon` |
| 267 | [@yefengr/remote-pi](https://pi.dev/packages/@yefengr/remote-pi?page=6) | 4,435/mo | extension | Browser PWA remote control for Pi coding agent endpoints over a Relay. | `pi install npm:@yefengr/remote-pi` |
| 273 | [@gang-of-beads/pi-web](https://pi.dev/packages/@gang-of-beads/pi-web?page=6) | 4,320/mo | package | Web UI for persistent Pi Coding Agent sessions in real workspaces. | `pi install npm:@gang-of-beads/pi-web` |
| 276 | [pi-outpost](https://pi.dev/packages/pi-outpost?page=6) | 4,209/mo | package | A web interface for the pi coding agent: a browser chat UI you run with npx — no clone, no build. | `pi install npm:pi-outpost` |
| 295 | [open-codebase-index](https://pi.dev/packages/open-codebase-index?page=6) | 4,006/mo | package | Host-neutral semantic codebase search with embeddings, symbol discovery, and call-graph tooling | `pi install npm:open-codebase-index` |
| 297 | [pi-chrome](https://pi.dev/packages/pi-chrome?page=6) | 3,993/mo | extension | Let Pi use your existing signed-in Chrome profile after explicit authorization. | `pi install npm:pi-chrome` |

### Context / Memory / Knowledge / Compaction

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 1 | [pi-mcp-adapter](https://pi.dev/packages/pi-mcp-adapter) | 1,120,235/mo | extension | 面向 Pi 编码代理的 MCP（Model Context Protocol）适配器扩展 | `pi install npm:pi-mcp-adapter` |
| 4 | [billion-context](https://pi.dev/packages/billion-context) | 241,224/mo | package | A context-compression plugin — small context windows (a 100K context is enough), 5x fewer tokens, month-long single sessions (billions of tokens), and compression quality — for all agents: pi, OpenCode, Codex, Claude Code, and more. billion-context is all | `pi install npm:billion-context` |
| 12 | [pi-mcp-extension](https://pi.dev/packages/pi-mcp-extension) | 93,959/mo | extension | 面向 Pi 编码代理的 MCP（Model Context Protocol）客户端扩展——将 Pi 连接到任意 MCP 服务器。 | `pi install npm:pi-mcp-extension` |
| 15 | [context-mode](https://pi.dev/packages/context-mode) | 75,590/mo | package | 可节省 98% 上下文窗口的 MCP 插件。兼容 Claude Code、Gemini CLI、VS Code Copilot、OpenCode 与 Codex CLI。提供沙箱代码执行、FTS5 知识库和意图驱动搜索。 | `pi install npm:context-mode` |
| 17 | [billion-context-pi](https://pi.dev/packages/billion-context-pi) | 59,250/mo | package | 十亿，而非一百万。面向 Pi 编码代理的模型驱动上下文管理。 | `pi install npm:billion-context-pi` |
| 32 | [pi-memory](https://pi.dev/packages/pi-memory) | 36,884/mo | package | Pi 编码代理的记忆扩展，使用 qmd 驱动的语义搜索，跨日常日志、长期记忆和临时便笺检索。 | `pi install npm:pi-memory` |
| 48 | [@agentskit/doc-bridge](https://pi.dev/packages/@agentskit/doc-bridge) | 24,643/mo | package | 连接人类与 AI 代理的文档桥梁——确定性交接、文档站链接、记忆→文档，以及可选的 AgentsKit RAG/聊天。 | `pi install npm:@agentskit/doc-bridge` |
| 52 | [pi-hermes-memory](https://pi.dev/packages/pi-hermes-memory?page=2) | 21,582/mo | extension, skill | 🧠 为 Pi 提供持久记忆 + 🔍 会话搜索 + 🛡️ 密钥扫描。默认采用感知 token 的纯策略记忆，支持 SQLite FTS5 搜索、自动整合与程序化技能。732 个测试，移植自 Hermes 代理。 | `pi install npm:pi-hermes-memory` |
| 53 | [@amaster.ai/pi-memory-mem0](https://pi.dev/packages/@amaster.ai/pi-memory-mem0?page=2) | 21,571/mo | extension | 为 pi 提供的 Mem0 语义记忆：自动捕获、语义召回，以及一个可供 AI 代理调用的记忆工具。支持平台版、嵌入式或自托管。 | `pi install npm:@amaster.ai/pi-memory-mem0` |
| 57 | [pi-web-search](https://pi.dev/packages/pi-web-search?page=2) | 19,122/mo | extension | 面向 pi 的模型提供方原生网络搜索，覆盖 Google Gemini、OpenAI 和 Anthropic，并支持 Gemini URL Context。 | `pi install npm:pi-web-search` |
| 60 | [pi-ollama-cloud-link](https://pi.dev/packages/pi-ollama-cloud-link?page=2) | 18,361/mo | extension | Unified pi extension for the Ollama Cloud account: live model discovery with capability/pricing metadata, web search/fetch agent tools with a disk cache, a live /ollama-setup account management TUI (quota bars, per-model spend, catalog browser), and an ol | `pi install npm:pi-ollama-cloud-link` |
| 68 | [gentle-engram](https://pi.dev/packages/gentle-engram?page=2) | 16,535/mo | extension | Pi 代理的持久记忆——一个可本地或云端部署的大脑，跨会话、压缩和 MCP 代理共享。 | `pi install npm:gentle-engram` |
| 70 | [pi-cache-optimizer](https://pi.dev/packages/pi-cache-optimizer?page=2) | 15,982/mo | package | 通过稳定的提示词、兼容 OpenAI 的缓存键、代理兼容性警告和底部缓存统计，提升 Pi 的提示词/KV 缓存命中率。 | `pi install npm:pi-cache-optimizer` |
| 88 | [pi-code](https://pi.dev/packages/pi-code?page=2) | 11,863/mo | extension, skill | 为 pi 编码代理带来 Claude Code 体验：读取你的 .claude 配置（规则、命令、技能包、钩子、输出样式、MCP 服务器、代理），并新增 todo、检查点、记忆、网页和子代理功能。 | `pi install npm:pi-code` |
| 92 | [@henryqw/pi-add-dir](https://pi.dev/packages/@henryqw/pi-add-dir?page=2) | 11,433/mo | skill | Add external directories to a Pi session with context, skills, and file search. | `pi install npm:@henryqw/pi-add-dir` |
| 106 | [@d3ara1n/pi-context-include](https://pi.dev/packages/@d3ara1n/pi-context-include?page=3) | 9,721/mo | extension | 为 AGENTS.md 提供 @path 语法——通过引用包含文件，并支持递归解析。 | `pi install npm:@d3ara1n/pi-context-include` |
| 107 | [pi-blackhole](https://pi.dev/packages/pi-blackhole?page=3) | 9,678/mo | extension | Pi 的统一压缩 + 观察记忆扩展——压缩对话上下文，同时保留持久的观察与反思记录。 | `pi install npm:pi-blackhole` |
| 119 | [@henryqw/pi-auto-compact](https://pi.dev/packages/@henryqw/pi-auto-compact?page=3) | 8,655/mo | package | Trim repeated reads and compact Pi context at a configurable threshold. | `pi install npm:@henryqw/pi-auto-compact` |
| 128 | [@chankov/agent-fleet](https://pi.dev/packages/@chankov/agent-fleet?page=3) | 8,207/mo | extension, skill, prompt | Subagent orchestration for the pi coding agent — a thin dispatcher runs parallel subagents under a verification contract, keeping their output out of its context window. Multi-agent fleets, 15 personas, skills, herdr panes, peer coms, Hermes desktop. | `pi install npm:@chankov/agent-fleet` |
| 132 | [pi-context-view](https://pi.dev/packages/pi-context-view?page=3) | 8,032/mo | extension | Pi 扩展，用于可视化上下文使用情况并查看隐藏部分：基础提示词、工具定义和扩展注入。 | `pi install npm:pi-context-view` |
| 137 | [@agimon-ai/doompi-cache](https://pi.dev/packages/@agimon-ai/doompi-cache?page=3) | 7,916/mo | extension | Provider prompt cache policy and deterministic routing for DoomPi | `pi install npm:@agimon-ai/doompi-cache` |
| 147 | [@awebai/oats-pi](https://pi.dev/packages/@awebai/oats-pi?page=3) | 7,649/mo | package | OATS pi runtime bridge — memory session events and pre-workspace bootstrap over the runtime-neutral @awebai/oats kernel | `pi install npm:@awebai/oats-pi` |
| 152 | [@llblab/pi-state-flow](https://pi.dev/packages/@llblab/pi-state-flow?page=4) | 7,585/mo | extension | Incremental scoped state/context/memory compiler for Pi, inspired by SKILL.state | `pi install npm:@llblab/pi-state-flow` |
| 154 | [@agimon-ai/doompi-autocompact](https://pi.dev/packages/@agimon-ai/doompi-autocompact?page=4) | 7,544/mo | extension | 为 Pi 与 DoomPi 代理会话提供迭代式上下文压缩与检查点摘要。 | `pi install npm:@agimon-ai/doompi-autocompact` |
| 169 | [openlore](https://pi.dev/packages/openlore?page=4) | 7,079/mo | package | 面向 AI 编码代理的持久化架构记忆与结构化认知。 | `pi install npm:openlore` |
| 176 | [@reddb-io/red-skills-brain](https://pi.dev/packages/@reddb-io/red-skills-brain?page=4) | 6,870/mo | package | reddb.io brain 插件：项目本地的 RedDB 知识库，用于自由记录与图连接。 | `pi install npm:@reddb-io/red-skills-brain` |
| 177 | [@reddb-io/red-skills-memory](https://pi.dev/packages/@reddb-io/red-skills-memory?page=4) | 6,859/mo | package | reddb.io 记忆插件：构建于 dev 之上的受治理编码代理运维记忆。支持 markdown 笔记、RedDB 图记忆、零 token 受治理召回、上下文包、声明检查、就绪状态、可选生命周期钩子，以及 MCP/HTTP 读取面 | `pi install npm:@reddb-io/red-skills-memory` |
| 178 | [pi-observational-memory](https://pi.dev/packages/pi-observational-memory?page=4) | 6,787/mo | extension | pi 的观察记忆扩展——采用缓存友好的分层压缩机制，支持观察与反思记录。 | `pi install npm:pi-observational-memory` |
| 179 | [@remnic/plugin-pi](https://pi.dev/packages/@remnic/plugin-pi?page=4) | 6,732/mo | package | 面向 Pi 编码代理的 Remnic 记忆扩展。 | `pi install npm:@remnic/plugin-pi` |
| 212 | [@henryqw/pi-memory](https://pi.dev/packages/@henryqw/pi-memory?page=5) | 5,359/mo | package | Auto-managed markdown memory for Pi: capped MEMORY.md/USER.md entry stores with frozen session snapshots. | `pi install npm:@henryqw/pi-memory` |
| 226 | [@hypabolic/pi-hypa](https://pi.dev/packages/@hypabolic/pi-hypa?page=5) | 5,065/mo | package | Pi 扩展，让嘈杂的工具输出远离你的上下文窗口。通过 Hypa 自动重写 shell 命令，实现本地确定性压缩、上下文感知的文件工具与可恢复的证据。 | `pi install npm:@hypabolic/pi-hypa` |
| 228 | [@astrosheep/pi-context](https://pi.dev/packages/@astrosheep/pi-context?page=5) | 5,017/mo | extension | Codex-style context windows for Pi: durable reset windows, session history tools, and persistent notes. | `pi install npm:@astrosheep/pi-context` |
| 232 | [@zosmaai/pi-llm-wiki](https://pi.dev/packages/@zosmaai/pi-llm-wiki?page=5) | 4,963/mo | extension, skill | 面向 Pi 的自维护 LLM Wiki——采用 Karpathy 模式的知识库，支持不可变源捕获、自动化摄取、搜索、lint 检查以及与 Obsidian 兼容的 vault。可自动更新的个人与公司 wiki。 | `pi install npm:@zosmaai/pi-llm-wiki` |
| 244 | [pi-openai-toolkit](https://pi.dev/packages/pi-openai-toolkit?page=5) | 4,812/mo | extension | OpenAI toolkit for Pi: Codex Remote Context windows, remote compaction v2, routed Web Search, image gen, auto mode. | `pi install npm:pi-openai-toolkit` |
| 246 | [@upstash/context7-pi](https://pi.dev/packages/@upstash/context7-pi?page=5) | 4,770/mo | package | pi.dev 官方 Context7 扩展——为 pi 编码代理添加 resolve-library-id 和 query-docs 工具。 | `pi install npm:@upstash/context7-pi` |
| 277 | [@amaster.ai/pi-attachments](https://pi.dev/packages/@amaster.ai/pi-attachments?page=6) | 4,199/mo | extension | Pi extension for attachment processing — classifies, parses, and renders file attachments into LLM-visible prompt context | `pi install npm:@amaster.ai/pi-attachments` |
| 279 | [pi-fovea](https://pi.dev/packages/pi-fovea?page=6) | 4,181/mo | extension | 面向 AI 代理会话的 token 预算化仓库映射：在跨语言代码图上进行中央凹热扩散，并支持渐进式披露。 | `pi install npm:pi-fovea` |
| 286 | [@amaster.ai/pi-memory](https://pi.dev/packages/@amaster.ai/pi-memory?page=6) | 4,090/mo | extension | Pi extension providing persistent curated memory (MEMORY.md + USER.md) injected into the system prompt as a frozen snapshot. | `pi install npm:@amaster.ai/pi-memory` |
| 293 | [@galvinsan/pi-mentis-knowledge](https://pi.dev/packages/@galvinsan/pi-mentis-knowledge?page=6) | 4,017/mo | extension | 独立的 Pi Mentis 知识扩展，适用于 Pi >= 0.84.0。 | `pi install npm:@galvinsan/pi-mentis-knowledge` |

### Agent 编排 / Subagent / Plan / Goal / Task

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 2 | [pi-subagents](https://pi.dev/packages/pi-subagents) | 470,277/mo | package | 用于单代理委派和脚本化多代理工作流的 Pi 扩展 | `pi install npm:pi-subagents` |
| 9 | [pi-goal-x](https://pi.dev/packages/pi-goal-x) | 101,465/mo | extension | pi 的目标模式扩展：持久的长期目标、五个模型工具、结构化任务、独立的完成审计、西西弗斯模式、自动继续和状态浮层。 | `pi install npm:pi-goal-x` |
| 21 | [@langchain/langsmith-pi-extension](https://pi.dev/packages/@langchain/langsmith-pi-extension) | 49,188/mo | package | 面向 Pi Coding Agent 的 LangSmith 扩展。 | `pi install npm:@langchain/langsmith-pi-extension` |
| 24 | [@akagilnc/pi-workflow-roles](https://pi.dev/packages/@akagilnc/pi-workflow-roles) | 45,014/mo | package | 面向 Pi 的灵魂绑定（soul-bound）工作流角色。 | `pi install npm:@akagilnc/pi-workflow-roles` |
| 28 | [@schovest/pi-goal](https://pi.dev/packages/@schovest/pi-goal) | 38,374/mo | extension | Pi extension for autonomous single-objective /goal completion. | `pi install npm:@schovest/pi-goal` |
| 33 | [@tintinweb/pi-subagents](https://pi.dev/packages/@tintinweb/pi-subagents) | 35,255/mo | extension | 一个 pi 扩展，为 pi 带来类 Claude Code 的子代理与工作流编排：并行执行、实时组件、代理集群视图、自定义代理类型、运行中转向、动态工作流、Claude Code 兼容性以及整体外观与体验。 | `pi install npm:@tintinweb/pi-subagents` |
| 37 | [@narumitw/pi-goal](https://pi.dev/packages/@narumitw/pi-goal) | 30,869/mo | extension | Pi 扩展，用于通过 /goal 自主完成单一目标。 | `pi install npm:@narumitw/pi-goal` |
| 40 | [@narumitw/pi-plan-mode](https://pi.dev/packages/@narumitw/pi-plan-mode) | 28,263/mo | extension | Pi 扩展，新增一个类似 Codex 的只读 /plan 协作模式。 | `pi install npm:@narumitw/pi-plan-mode` |
| 42 | [@henryqw/pi-subagent](https://pi.dev/packages/@henryqw/pi-subagent) | 27,114/mo | package | 将受限的单个、并行或链式任务委派给隔离的 Pi 角色。 | `pi install npm:@henryqw/pi-subagent` |
| 54 | [@cgh567/agent](https://pi.dev/packages/@cgh567/agent?page=2) | 21,380/mo | package | Helios 自我改进实验室。 | `pi install npm:@cgh567/agent` |
| 59 | [@henryqw/pi-task-models](https://pi.dev/packages/@henryqw/pi-task-models?page=2) | 18,866/mo | package | 面向 HenryQW Pi 扩展的共享任务模型配置与路由。 | `pi install npm:@henryqw/pi-task-models` |
| 62 | [pi-intercom](https://pi.dev/packages/pi-intercom?page=2) | 17,636/mo | package | <p> <img src="banner.png" alt="pi-intercom" width="1100"> </p> | `pi install npm:pi-intercom` |
| 67 | [@kontextmind/kxm](https://pi.dev/packages/@kontextmind/kxm?page=2) | 16,702/mo | extension | KXM local-first multi-agent orchestration and operator dashboard | `pi install npm:@kontextmind/kxm` |
| 83 | [pi-rtk-optimizer](https://pi.dev/packages/pi-rtk-optimizer?page=2) | 12,430/mo | extension | Pi 扩展，为编码代理优化 RTK 命令重写与工具输出压缩。 | `pi install npm:pi-rtk-optimizer` |
| 87 | [@gotgenes/pi-subagents](https://pi.dev/packages/@gotgenes/pi-subagents?page=2) | 11,872/mo | extension | 面向 pi 的专注型进程内子代理核心——提供自主 AI 代理，以及供其他扩展构建的类型化 API 与生命周期事件。是 @tintinweb/pi-subagents 的友好分支（fork）。 | `pi install npm:@gotgenes/pi-subagents` |
| 141 | [pi-subagents-j0k3r](https://pi.dev/packages/pi-subagents-j0k3r?page=3) | 7,796/mo | extension | 可安装的 Pi 包，新增 markdown 定义的子代理、委派任务工具、历史记录和模型配置文件。 | `pi install npm:pi-subagents-j0k3r` |
| 145 | [@agimon-ai/doompi-team](https://pi.dev/packages/@agimon-ai/doompi-team?page=3) | 7,727/mo | package | 为 Pi 编码代理提供异步具名子代理、团队运行、对讲（intercom）与模型策略。 | `pi install npm:@agimon-ai/doompi-team` |
| 151 | [@agimon-ai/doompi-workflow](https://pi.dev/packages/@agimon-ai/doompi-workflow?page=4) | 7,607/mo | extension | 为 DoomPi 提供 GitHub Actions 风格的工作流图、产物（artifacts）、恢复与异步运行。 | `pi install npm:@agimon-ai/doompi-workflow` |
| 158 | [@agimon-ai/doompi-plan](https://pi.dev/packages/@agimon-ai/doompi-plan?page=4) | 7,308/mo | extension | 可审核的 Pi 规划模式：移除文件编辑工具并持久化实现计划。 | `pi install npm:@agimon-ai/doompi-plan` |
| 159 | [shariq-pi-extensions](https://pi.dev/packages/shariq-pi-extensions?page=4) | 7,275/mo | extension | Pi 编码代理的跨平台扩展套件。 | `pi install npm:shariq-pi-extensions` |
| 168 | [runline](https://pi.dev/packages/runline?page=4) | 7,135/mo | package | 面向 AI 代理的代码模式 —— 将任意 API 或命令变成可调用的操作 | `pi install npm:runline` |
| 183 | [infinity-harness](https://pi.dev/packages/infinity-harness?page=4) | 6,519/mo | extension | A pi agent extension that runs a gated build pipeline unattended — enforces phases, validates with deterministic gates, and keeps working for hours or days without losing the plan. | `pi install npm:infinity-harness` |
| 191 | [@astrosheep/square](https://pi.dev/packages/@astrosheep/square?page=4) | 6,219/mo | package | 一个共享的公共广场：代理们在此加入、获取动态、发表意见，并在完成后离开。 | `pi install npm:@astrosheep/square` |
| 201 | [@astrosheep/keiyaku](https://pi.dev/packages/@astrosheep/keiyaku?page=5) | 5,894/mo | package | Keiyaku 是一个面向代理的契约工作流。 | `pi install npm:@astrosheep/keiyaku` |
| 204 | [agent-simple-english](https://pi.dev/packages/agent-simple-english?page=5) | 5,791/mo | package | Technical and house-style English lint engine, CLI, and host adapters | `pi install npm:agent-simple-english` |
| 208 | [@agimon-ai/doompi-runner-rtk-linux-x64](https://pi.dev/packages/@agimon-ai/doompi-runner-rtk-linux-x64?page=5) | 5,463/mo | package | Prebuilt RTK v0.45.0 log processor for DoomPi Runner on Linux x64. | `pi install npm:@agimon-ai/doompi-runner-rtk-linux-x64` |
| 216 | [@tintinweb/pi-tasks](https://pi.dev/packages/@tintinweb/pi-tasks?page=5) | 5,195/mo | extension | 一个 pi 扩展，为 pi 带来 Claude Code 风格的任务跟踪与协调能力。 | `pi install npm:@tintinweb/pi-tasks` |
| 221 | [@agentapprove/pi](https://pi.dev/packages/@agentapprove/pi?page=5) | 5,109/mo | extension | Agent Approve extension for Pi - approve or deny AI agent tool calls from your iPhone and Apple Watch | `pi install npm:@agentapprove/pi` |
| 240 | [@agimon-ai/doompi-runner-rtk-linux-arm64](https://pi.dev/packages/@agimon-ai/doompi-runner-rtk-linux-arm64?page=5) | 4,852/mo | package | Prebuilt RTK v0.45.0 log processor for DoomPi Runner on Linux arm64. | `pi install npm:@agimon-ai/doompi-runner-rtk-linux-arm64` |
| 241 | [@agimon-ai/doompi-runner-rtk-darwin-arm64](https://pi.dev/packages/@agimon-ai/doompi-runner-rtk-darwin-arm64?page=5) | 4,849/mo | package | Prebuilt RTK v0.45.0 log processor for DoomPi Runner on macOS arm64. | `pi install npm:@agimon-ai/doompi-runner-rtk-darwin-arm64` |
| 247 | [pi-autosuggestions](https://pi.dev/packages/pi-autosuggestions?page=5) | 4,738/mo | package | zsh-autosuggestions-style ghost completions for the pi coding agent — history-based inline suggestions, path completion in bash mode, blinking beam cursor | `pi install npm:pi-autosuggestions` |
| 248 | [@agimon-ai/doompi-runner-rtk-darwin-x64](https://pi.dev/packages/@agimon-ai/doompi-runner-rtk-darwin-x64?page=5) | 4,732/mo | package | Prebuilt RTK v0.45.0 log processor for DoomPi Runner on macOS x64. | `pi install npm:@agimon-ai/doompi-runner-rtk-darwin-x64` |
| 257 | [pi-zense](https://pi.dev/packages/pi-zense?page=6) | 4,617/mo | theme | Spec-gated, human-signed SDLC harness for pi (zense = a pun on the Thai word for sign) — sub-agents, dual eval, escalation gates — plus the Zense dark theme. | `pi install npm:pi-zense` |
| 262 | [@agwab/pi-workflow](https://pi.dev/packages/@agwab/pi-workflow?page=6) | 4,504/mo | extension | Workflow orchestration for Pi subagents. | `pi install npm:@agwab/pi-workflow` |
| 263 | [pi-extensible-workflows](https://pi.dev/packages/pi-extensible-workflows?page=6) | 4,484/mo | package | Deterministic multi-agent workflow orchestration for Pi | `pi install npm:pi-extensible-workflows` |
| 268 | [@injaneity/pi-computer-use](https://pi.dev/packages/@injaneity/pi-computer-use?page=6) | 4,421/mo | extension | Pi extension that lets AI agents observe and control macOS, Windows, and Linux apps. | `pi install npm:@injaneity/pi-computer-use` |
| 271 | [@runfusion/fusion](https://pi.dev/packages/@runfusion/fusion?page=6) | 4,370/mo | package | Fusion CLI：面向 Fusion AI coding agent 的 HTTP API 服务器、守护进程、仪表盘启动器和任务工具。 | `pi install npm:@runfusion/fusion` |
| 278 | [@narumitw/pi-subagents](https://pi.dev/packages/@narumitw/pi-subagents?page=6) | 4,189/mo | extension | 面向 Pi 的子代理任务，支持与主代理的异步消息通信。 | `pi install npm:@narumitw/pi-subagents` |
| 288 | [@pify/swarm](https://pi.dev/packages/@pify/swarm?page=6) | 4,064/mo | extension | Coordinate multiple pi agents in parallel: swarm_run fan-out with per-item auto-routing, concurrency queue, aggregated reports | `pi install npm:@pify/swarm` |

### UI / TUI / Session / 观测

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 6 | [@langfuse/pi-observability-plugin](https://pi.dev/packages/@langfuse/pi-observability-plugin) | 198,579/mo | extension | Langfuse observability extension for the pi coding agent — traces prompts, agent turns, model generations, and tool calls to Langfuse. | `pi install npm:@langfuse/pi-observability-plugin` |
| 7 | [@juicesharp/rpiv-todo](https://pi.dev/packages/@juicesharp/rpiv-todo) | 169,291/mo | extension | Pi 扩展：为模型提供待办事项列表，以实时浮层渲染，且 /reload 与会话压缩后依然保留。 | `pi install npm:@juicesharp/rpiv-todo` |
| 16 | [pi-powerline-footer](https://pi.dev/packages/pi-powerline-footer) | 60,423/mo | extension | 面向 pi 编码代理的 Powerline 风格状态栏扩展。 | `pi install npm:pi-powerline-footer` |
| 23 | [pi-cc-extensions](https://pi.dev/packages/pi-cc-extensions) | 46,279/mo | extension | 一套 Pi 效率增强套件，提供 Claude Code 风格 UI、上下文检查以及代理/会话引用。 | `pi install npm:pi-cc-extensions` |
| 26 | [@raindrop-ai/pi-agent](https://pi.dev/packages/@raindrop-ai/pi-agent) | 38,869/mo | package | 为 Pi Agent 提供 Raindrop 可观测性——通过 subscriber 或 pi-coding-agent 扩展实现自动追踪。 | `pi install npm:@raindrop-ai/pi-agent` |
| 29 | [@moyai/pi-session-hoarder](https://pi.dev/packages/@moyai/pi-session-hoarder) | 38,132/mo | package | 🐿️ 一个将会话归档到本地内容寻址存储的 Pi 扩展。 | `pi install npm:@moyai/pi-session-hoarder` |
| 46 | [pi-btw](https://pi.dev/packages/pi-btw) | 24,730/mo | extension | 一个 pi 扩展，通过 /btw 进行并行的旁路对话 | `pi install npm:pi-btw` |
| 66 | [@agimon-ai/doompi-telemetry](https://pi.dev/packages/@agimon-ai/doompi-telemetry?page=2) | 16,953/mo | package | 面向 DoomPi 会话的宿主无关遥测、OpenTelemetry 控制与 Log Sink 适配器。 | `pi install npm:@agimon-ai/doompi-telemetry` |
| 73 | [@agimon-ai/doompi-ui](https://pi.dev/packages/@agimon-ai/doompi-ui?page=2) | 14,819/mo | extension | 面向 DoomPi 与 Pi 扩展的 Leader 键菜单、主题与 TUI 组件。 | `pi install npm:@agimon-ai/doompi-ui` |
| 78 | [@agimon-ai/doompi-config](https://pi.dev/packages/@agimon-ai/doompi-config?page=2) | 13,151/mo | package | 用于编排 DoomPi 会话的类型化配置加载、校验以及宿主适配器。 | `pi install npm:@agimon-ai/doompi-config` |
| 89 | [pi-open-tui](https://pi.dev/packages/pi-open-tui?page=2) | 11,693/mo | extension, theme | 面向 Pi 编码代理的精美 TUI：动态 logo 头部、Starship 风格底部栏、带模型元数据的圆角编辑器，以及提示框形式的用户消息。 | `pi install npm:pi-open-tui` |
| 93 | [@janvitos/pi-plan-build](https://pi.dev/packages/@janvitos/pi-plan-build?page=2) | 11,419/mo | package | 安全地制定计划，明确地批准，然后在此处或在一个干净的新会话中实施。 | `pi install npm:@janvitos/pi-plan-build` |
| 96 | [glimpseui](https://pi.dev/packages/glimpseui?page=2) | 10,730/mo | prompt | 面向脚本和 AI 代理的原生微 UI——提供跨平台 WebView 窗口与双向 JSON 通信。 | `pi install npm:glimpseui` |
| 109 | [pi-ask-user](https://pi.dev/packages/pi-ask-user?page=3) | 9,291/mo | extension | 面向 pi-coding-agent 的交互式 ask_user 工具，提供可搜索的分栏选择 UI、多选与自由文本输入。 | `pi install npm:pi-ask-user` |
| 111 | [pi-zentui](https://pi.dev/packages/pi-zentui?page=3) | 8,909/mo | extension, theme | 灵感源自 Starship 的状态行与 Opencode 风格 TUI，适用于 Pi。 | `pi install npm:pi-zentui` |
| 124 | [@agimon-ai/doompi-loop](https://pi.dev/packages/@agimon-ai/doompi-loop?page=3) | 8,402/mo | extension | 为 Pi 编码代理提供会话级循环提示词调度器与循环控制。 | `pi install npm:@agimon-ai/doompi-loop` |
| 125 | [@agimon-ai/doompi-profile](https://pi.dev/packages/@agimon-ai/doompi-profile?page=3) | 8,282/mo | extension | Persona and environment profile switching for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-profile` |
| 133 | [@agimon-ai/doompi-major-mode](https://pi.dev/packages/@agimon-ai/doompi-major-mode?page=3) | 8,019/mo | extension | Named major-mode selection and layer composition switching for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-major-mode` |
| 134 | [@agimon-ai/doompi-notification](https://pi.dev/packages/@agimon-ai/doompi-notification?page=3) | 7,984/mo | extension | Desktop notifications and an animated shell-tab title for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-notification` |
| 135 | [@agimon-ai/doompi-minor-mode](https://pi.dev/packages/@agimon-ai/doompi-minor-mode?page=3) | 7,970/mo | extension | Minor-mode ownership, catalog, commands, and session lifecycle. | `pi install npm:@agimon-ai/doompi-minor-mode` |
| 139 | [@agimon-ai/doompi-log](https://pi.dev/packages/@agimon-ai/doompi-log?page=3) | 7,860/mo | extension | 为代理可观测性提供 Pi 会话指标、发现（findings）、数据接收端（sink）状态与 Log Metrics 覆盖层。 | `pi install npm:@agimon-ai/doompi-log` |
| 143 | [@agimon-ai/doompi-task](https://pi.dev/packages/@agimon-ai/doompi-task?page=3) | 7,737/mo | package | 为 Pi 编码会话提供持久化、感知依赖的任务图与子代理委派。 | `pi install npm:@agimon-ai/doompi-task` |
| 148 | [@agimon-ai/doompi-autostop](https://pi.dev/packages/@agimon-ai/doompi-autostop?page=3) | 7,646/mo | extension | Shuts a DoomPi session down once the agent settles and stays idle. | `pi install npm:@agimon-ai/doompi-autostop` |
| 150 | [@agimon-ai/doompi-voice](https://pi.dev/packages/@agimon-ai/doompi-voice?page=3) | 7,635/mo | extension | 为 Pi 代理提供客户端音频采集、主机端转写与自主叙述功能。 | `pi install npm:@agimon-ai/doompi-voice` |
| 160 | [@juicesharp/rpiv-btw](https://pi.dev/packages/@juicesharp/rpiv-btw?page=4) | 7,215/mo | extension | Pi 扩展。/btw 斜杠命令，用于向同一个主模型提出一次性附带问题，而不污染主对话。 | `pi install npm:@juicesharp/rpiv-btw` |
| 163 | [@agimon-ai/doompi-hook](https://pi.dev/packages/@agimon-ai/doompi-hook?page=4) | 7,146/mo | extension | Claude-Code-compatible repository and plugin hook runner for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-hook` |
| 172 | [@agimon-ai/doompi-user-feedback](https://pi.dev/packages/@agimon-ai/doompi-user-feedback?page=4) | 6,975/mo | extension | 为 Pi 代理提供结构化用户提问，并支持交互式与自主式 Voice 交接。 | `pi install npm:@agimon-ai/doompi-user-feedback` |
| 190 | [@narumitw/pi-statusline](https://pi.dev/packages/@narumitw/pi-statusline?page=4) | 6,245/mo | extension | Pi 扩展，将底部栏替换为信息丰富的状态行（statusline）。 | `pi install npm:@narumitw/pi-statusline` |
| 218 | [pi-interactive-shell](https://pi.dev/packages/pi-interactive-shell?page=5) | 5,146/mo | extension | 在 pi 的 TUI 覆盖层中运行 AI 编码代理，支持交互式、免手动及分派式监督。 | `pi install npm:pi-interactive-shell` |
| 225 | [pi-queue-steer-factory](https://pi.dev/packages/pi-queue-steer-factory?page=5) | 5,075/mo | extension | Visible steering, follow-up, and session-control queues for Pi and Pi Fabric. | `pi install npm:pi-queue-steer-factory` |
| 230 | [pi-phoenix](https://pi.dev/packages/pi-phoenix?page=5) | 4,998/mo | extension | 面向 pi 的 Phoenix 追踪扩展 | `pi install npm:pi-phoenix` |
| 258 | [@yaag/extension](https://pi.dev/packages/@yaag/extension?page=6) | 4,583/mo | package | The yaag pi extension: run Orchestration Programs from a pi session. | `pi install npm:@yaag/extension` |
| 270 | [@agimon-ai/doompi-computer-use](https://pi.dev/packages/@agimon-ai/doompi-computer-use?page=6) | 4,384/mo | extension | Session scoped semantic computer control through the DoomPi Desktop capability. | `pi install npm:@agimon-ai/doompi-computer-use` |
| 274 | [@groeponline/pi-wishcraft](https://pi.dev/packages/@groeponline/pi-wishcraft?page=6) | 4,294/mo | extension | 面向 Pi 的操作员驾驶舱：实时 powerline 状态、可搜索的技能包、灵感队列、可置顶 Bash、钩子（hooks）、策略控制与会话体验。 | `pi install npm:@groeponline/pi-wishcraft` |
| 291 | [@agimon-ai/doompi-git](https://pi.dev/packages/@agimon-ai/doompi-git?page=6) | 4,036/mo | extension | Git worktree sessions for DoomPi: spawn an isolated worktree with its own session and manage it from the parent | `pi install npm:@agimon-ai/doompi-git` |
| 296 | [@juanibiapina/pi-powerbar](https://pi.dev/packages/@juanibiapina/pi-powerbar?page=6) | 4,001/mo | extension | Pi extension that renders a persistent powerline status bar with left/right segments updated via events | `pi install npm:@juanibiapina/pi-powerbar` |
| 300 | [@amaster.ai/pi-video-gen](https://pi.dev/packages/@amaster.ai/pi-video-gen?page=6) | 3,950/mo | extension | Pi extension for AI video generation plus local video composition: lossless clip concat and mixed image/video timelines with overlays, TTS, soft or burned subtitles, source audio, BGM, and bundled LGPL/GPL FFmpeg runtimes. | `pi install npm:@amaster.ai/pi-video-gen` |

### 模型 / Provider / 路由 / 用量

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 19 | [@narumitw/pi-usage](https://pi.dev/packages/@narumitw/pi-usage) | 56,582/mo | extension | Pi 扩展，可显示受支持模型提供方的当前账户用量和 DeepSeek API 余额。 | `pi install npm:@narumitw/pi-usage` |
| 20 | [pi-claude-bridge](https://pi.dev/packages/pi-claude-bridge) | 55,561/mo | extension | Pi 扩展，将 Claude Code（通过 Agent SDK）用作模型提供方，并新增 AskClaude 工具。 | `pi install npm:pi-claude-bridge` |
| 31 | [pi-provider-litellm](https://pi.dev/packages/pi-provider-litellm) | 37,811/mo | extension | 面向 Pi 的 LiteLLM 代理模型提供方扩展。 | `pi install npm:pi-provider-litellm` |
| 34 | [agent-comms](https://pi.dev/packages/agent-comms) | 34,025/mo | package | Cross-harness communication mesh for LLM agents — rooms, DMs, presence, and real-time push delivery over TCP | `pi install npm:agent-comms` |
| 51 | [@braintrust/pi-extension](https://pi.dev/packages/@braintrust/pi-extension?page=2) | 21,655/mo | package | 面向 pi 的 Braintrust 扩展，可自动将 pi 会话、轮次、LLM 调用和工具执行追踪到 Braintrust。 | `pi install npm:@braintrust/pi-extension` |
| 77 | [pi-freeflow](https://pi.dev/packages/pi-freeflow?page=2) | 13,384/mo | extension | 面向 OMP/Pi 的轻量级模型提供方 —— 模型列表 + 简易中继代理 + 日志；思考（thinking）与规范化（normalization）由宿主 pi-ai 负责。 | `pi install npm:pi-freeflow` |
| 79 | [auto-model-router](https://pi.dev/packages/auto-model-router?page=2) | 13,071/mo | package | Local cost/complexity-aware model router for Oh My Pi, backed by OpenRouter | `pi install npm:auto-model-router` |
| 91 | [pi-nvidia-nim](https://pi.dev/packages/pi-nvidia-nim?page=2) | 11,595/mo | package | 面向 pi 编码代理的 NVIDIA NIM API 模型提供方扩展——可访问 build.nvidia.com 上的 100 多个模型。 | `pi install npm:pi-nvidia-nim` |
| 94 | [pi-antigravity](https://pi.dev/packages/pi-antigravity?page=2) | 11,161/mo | extension | 面向 Pi Coding Agent 的个人 Antigravity / Cloud Code Assist 模型提供方。 | `pi install npm:pi-antigravity` |
| 97 | [pi-harness-runtime](https://pi.dev/packages/pi-harness-runtime?page=2) | 10,412/mo | extension | [BETA] 面向 pi 的 Codex 风格 /usage 状态与自主编码 harness。尚未达到生产就绪——预计会有破坏性变更。 | `pi install npm:pi-harness-runtime` |
| 99 | [pi-extension-nvidia-nim](https://pi.dev/packages/pi-extension-nvidia-nim?page=2) | 10,384/mo | package | 为 pi coding agent 提供模型感知的 NVIDIA NIM 推理兼容性 | `pi install npm:pi-extension-nvidia-nim` |
| 104 | [@amaster.ai/pi-image-gen](https://pi.dev/packages/@amaster.ai/pi-image-gen?page=3) | 10,148/mo | extension | Pi 图片生成扩展，支持通过 OpenAI gpt-image、Google Nano Banana（Gemini）、阿里 Qwen-Image、OpenRouter 及自定义模型提供方生成图片。 | `pi install npm:@amaster.ai/pi-image-gen` |
| 117 | [pi-lmstudio](https://pi.dev/packages/pi-lmstudio?page=3) | 8,778/mo | package | 面向 Pi 编码代理的 LM Studio 模型提供方扩展。 | `pi install npm:pi-lmstudio` |
| 118 | [@tunnckocore/pi-gpt-fast-mode](https://pi.dev/packages/@tunnckocore/pi-gpt-fast-mode?page=3) | 8,770/mo | extension | 一个极简 Pi 扩展，仅通过 /fast（默认 'priority'）在 GPT-5.4 / GPT-5.5 / GPT-5.6 的 Fast 模式之间切换，不含其他功能——只有一个文件。 | `pi install npm:@tunnckocore/pi-gpt-fast-mode` |
| 123 | [pi-llama-cpp](https://pi.dev/packages/pi-llama-cpp?page=3) | 8,412/mo | extension | 用于集成 llama.cpp 的 Pi 扩展。支持 router、单模型与旧版（legacy）模型，并支持多个服务器。 | `pi install npm:pi-llama-cpp` |
| 127 | [pi-commandcode-provider](https://pi.dev/packages/pi-commandcode-provider?page=3) | 8,253/mo | extension | pi custom provider for Command Code API (commandcode.ai) | `pi install npm:pi-commandcode-provider` |
| 130 | [@gotgenes/pi-anthropic-auth](https://pi.dev/packages/@gotgenes/pi-anthropic-auth?page=3) | 8,183/mo | package | 用于 Anthropic OAuth 兼容性的 Pi 扩展包 | `pi install npm:@gotgenes/pi-anthropic-auth` |
| 142 | [@sreetej510/pi-usage](https://pi.dev/packages/@sreetej510/pi-usage?page=3) | 7,785/mo | extension | Pi 扩展，通过 /usage 报告模型提供方的用量/速率限制预算（Codex、Anthropic OAuth 等），并提供实时状态栏小部件。 | `pi install npm:@sreetej510/pi-usage` |
| 146 | [@agimon-ai/doompi-goal](https://pi.dev/packages/@agimon-ai/doompi-goal?page=3) | 7,710/mo | extension | Pi 的辅助模式，用于持久化代理目标、token 预算与目标历史。 | `pi install npm:@agimon-ai/doompi-goal` |
| 166 | [pi-ollama-cloud](https://pi.dev/packages/pi-ollama-cloud?page=4) | 7,138/mo | package | 面向 [Pi](https://pi.dev) 编码代理的 Ollama Cloud 模型提供方插件。 | `pi install npm:pi-ollama-cloud` |
| 171 | [pi-otel](https://pi.dev/packages/pi-otel?page=4) | 6,982/mo | extension | OpenTelemetry traces for pi-coding-agent — per-prompt span tree (interaction → llm_request, tool.<name>) exported via OTLP. Aspire-dashboard ready. | `pi install npm:pi-otel` |
| 182 | [pi-token-speed](https://pi.dev/packages/pi-token-speed?page=4) | 6,565/mo | extension | Pi 扩展，通过滑动窗口测量每秒 token 数（tokens per second）。 | `pi install npm:pi-token-speed` |
| 193 | [pi-tokenrouter](https://pi.dev/packages/pi-tokenrouter?page=4) | 6,198/mo | extension | TokenRouter provider extension for pi — dynamic model discovery with OpenRouter-compatible pricing | `pi install npm:pi-tokenrouter` |
| 194 | [@realvendex/pi-token-router](https://pi.dev/packages/@realvendex/pi-token-router?page=4) | 6,164/mo | package | TokenRouter.com unified API gateway as a native Pi provider for accessing 300+ LLM models via a single API key | `pi install npm:@realvendex/pi-token-router` |
| 199 | [pi-cursor-sdk](https://pi.dev/packages/pi-cursor-sdk?page=4) | 6,067/mo | extension | 由 @cursor/sdk 本地及云端 AI 代理支撑的 pi 模型提供方扩展 | `pi install npm:pi-cursor-sdk` |
| 205 | [pi-cliproxyapi-provider](https://pi.dev/packages/pi-cliproxyapi-provider?page=5) | 5,765/mo | extension | 面向 CLIProxyAPI 的 Pi 模型提供方包，支持自动发现模型并利用 models.dev 补充模型信息。 | `pi install npm:pi-cliproxyapi-provider` |
| 207 | [@sting8k/pi-vcc](https://pi.dev/packages/@sting8k/pi-vcc?page=5) | 5,466/mo | extension | Algorithmic conversation compactor for pi - transcript-preserving structured summaries, no LLM calls | `pi install npm:@sting8k/pi-vcc` |
| 245 | [superpowers-zh](https://pi.dev/packages/superpowers-zh?page=5) | 4,811/mo | skill | AI 编程超能力中文增强版 — superpowers（250k+ ⭐）完整汉化 + 4 个中国原创技能包，支持 Claude Code / Copilot CLI / Hermes Agent / Cursor / Claw Code / Windsurf / Kiro / Gemini CLI / Qoder 等 23 款工具 | `pi install npm:superpowers-zh` |
| 251 | [@pentect/pi](https://pi.dev/packages/@pentect/pi?page=6) | 4,667/mo | package | Pi 的 Pentect 模型提供方扩展。 | `pi install npm:@pentect/pi` |
| 265 | [pi-caveman](https://pi.dev/packages/pi-caveman?page=6) | 4,450/mo | extension | 既然少量 token 就能奏效，何必使用大量 token。pi 的穴居人模式 —— 在保持完整技术准确性的同时减少约 75% 的输出 token。 | `pi install npm:pi-caveman` |
| 266 | [@amaster.ai/pi-task-scheduler](https://pi.dev/packages/@amaster.ai/pi-task-scheduler?page=6) | 4,437/mo | extension | Pi 扩展，基于 cron 的定时任务管理，提供可由 LLM 调用的工具。 | `pi install npm:@amaster.ai/pi-task-scheduler` |
| 269 | [pi-multiprovider](https://pi.dev/packages/pi-multiprovider?page=6) | 4,405/mo | extension | Same-provider multi-account pooling, OAuth storage, and safe in-stream auth failover for Pi | `pi install npm:pi-multiprovider` |
| 272 | [pi-free](https://pi.dev/packages/pi-free?page=6) | 4,358/mo | extension | 面向 Pi 的 AI 模型提供方，支持免费模型过滤与动态模型获取。 | `pi install npm:pi-free` |
| 281 | [@henryqw/pi-footer](https://pi.dev/packages/@henryqw/pi-footer?page=6) | 4,161/mo | package | Show concise repository, branch, and usage details in the Pi footer. | `pi install npm:@henryqw/pi-footer` |
| 294 | [@monotykamary/pi-better-openai](https://pi.dev/packages/@monotykamary/pi-better-openai?page=6) | 4,009/mo | extension | Improve OpenAI in pi with fast mode, usage stats, realtime voice, image generation, and footer polish. | `pi install npm:@monotykamary/pi-better-openai` |
| 299 | [pi-codemie](https://pi.dev/packages/pi-codemie?page=6) | 3,969/mo | package | Pi extension for CodeMie (AI/Run) enterprise gateway provider | `pi install npm:pi-codemie` |

### Runtime / 后台任务 / Worktree / 集成

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 14 | [pi-background-tasks](https://pi.dev/packages/pi-background-tasks) | 84,612/mo | extension | Pi 扩展：支持持久的后台 shell 任务、只读委托代理、本地认证的 Pi 运行，以及通过子 Pi 进程运行的固定用途 Fusion 工作流。 | `pi install npm:pi-background-tasks` |
| 25 | [confluence-cli](https://pi.dev/packages/confluence-cli) | 43,280/mo | package | 面向 Atlassian Confluence 的命令行界面，具备页面创建与编辑能力。 | `pi install npm:confluence-cli` |
| 50 | [pi-fabric](https://pi.dev/packages/pi-fabric) | 22,887/mo | extension | 面向 Pi 的可编程工具与代理运行时。 | `pi install npm:pi-fabric` |
| 71 | [@llblab/pi-telegram](https://pi.dev/packages/@llblab/pi-telegram?page=2) | 15,808/mo | extension | 面向 Pi 的 Telegram 运行时适配器。 | `pi install npm:@llblab/pi-telegram` |
| 98 | [@agimon-ai/doompi-core](https://pi.dev/packages/@agimon-ai/doompi-core?page=2) | 10,388/mo | package | Doompi runtime systems and reusable core services. | `pi install npm:@agimon-ai/doompi-core` |
| 102 | [@agimon-ai/doompi-extension-contracts](https://pi.dev/packages/@agimon-ai/doompi-extension-contracts?page=3) | 10,290/mo | extension | 为独立打包的 DoomPi 扩展提供的类型化生命周期、协议与 Leader 契约。（DoomPi 生态的共享类型/契约库） | `pi install npm:@agimon-ai/doompi-extension-contracts` |
| 108 | [pi-until-loop](https://pi.dev/packages/pi-until-loop?page=3) | 9,456/mo | package | Spend your time on the engineering trade-offs that matter. Let the Until Loop make sure your agents deliver what you want, how you want it. | `pi install npm:pi-until-loop` |
| 115 | [@pi-unipi/core](https://pi.dev/packages/@pi-unipi/core?page=3) | 8,839/mo | extension | 面向 Unipi 扩展套件的共享工具、事件类型和常量 | `pi install npm:@pi-unipi/core` |
| 136 | [@agimon-ai/doompi-runner](https://pi.dev/packages/@agimon-ai/doompi-runner?page=3) | 7,964/mo | package | 为 Pi 编码代理提供受监督的 shell 执行、后台进程控制与运行日志。 | `pi install npm:@agimon-ai/doompi-runner` |
| 138 | [@xynogen/pix-runtime](https://pi.dev/packages/@xynogen/pix-runtime?page=3) | 7,873/mo | extension | Pix 共享运行时 —— 带版本号的 pix.json 配置、原子化持久化、类型化变更事件 | `pi install npm:@xynogen/pix-runtime` |
| 161 | [@amaster.ai/pi-computer-use](https://pi.dev/packages/@amaster.ai/pi-computer-use?page=4) | 7,210/mo | extension | 面向 Pi 桌面自动化的跨平台 computer-use（计算机操作）工具 | `pi install npm:@amaster.ai/pi-computer-use` |
| 165 | [@relaymessenger/pi](https://pi.dev/packages/@relaymessenger/pi?page=4) | 7,139/mo | package | Relay Messenger channel for Pi over Relay v1 WebSocket delivery. | `pi install npm:@relaymessenger/pi` |
| 175 | [@osolmaz/pi-workflows](https://pi.dev/packages/@osolmaz/pi-workflows?page=4) | 6,888/mo | package | 面向 pi 编码代理的工作流与控制器运行时，附带实时终端查看器。 | `pi install npm:@osolmaz/pi-workflows` |
| 180 | [@alasano/pi-linear](https://pi.dev/packages/@alasano/pi-linear?page=4) | 6,722/mo | package | pi 的 Linear 集成，提供 64+ 个工具、多工作区认证以及按工具配置的设置。 | `pi install npm:@alasano/pi-linear` |
| 181 | [pi-warden](https://pi.dev/packages/pi-warden?page=4) | 6,569/mo | extension | Makes the Pi agent follow your project's rules. Jev judges every write against your pi-warden.md and quotes the broken rule back to the agent, names slop, breaks stuck loops, calls out unverified done claims, compresses large tool output, and holds the ra | `pi install npm:pi-warden` |
| 192 | [pi-herdsman](https://pi.dev/packages/pi-herdsman?page=4) | 6,201/mo | extension | Asynchronous Pi subagents and agent fleet orchestration for parallel coding agents with nested delegation, background work, and supervision in herdr. | `pi install npm:pi-herdsman` |
| 197 | [jorgex-pi](https://pi.dev/packages/jorgex-pi?page=4) | 6,088/mo | package | Pi-native runtime package for the JorgeX harness. | `pi install npm:jorgex-pi` |
| 198 | [@pi-unipi/notify](https://pi.dev/packages/@pi-unipi/notify?page=4) | 6,069/mo | extension | Pi 的跨平台通知扩展——为代理生命周期事件提供原生操作系统、Gotify 和 Telegram 通知。 | `pi install npm:@pi-unipi/notify` |
| 202 | [@agimon-ai/doompi-runner-rmux-linux-x64](https://pi.dev/packages/@agimon-ai/doompi-runner-rmux-linux-x64?page=5) | 5,861/mo | package | 适用于 Linux x64 上 DoomPi Runner 的预编译 RMUX 运行时。 | `pi install npm:@agimon-ai/doompi-runner-rmux-linux-x64` |
| 206 | [pi-goal](https://pi.dev/packages/pi-goal?page=5) | 5,669/mo | package | Persistent autonomous goals for pi — /goal loops until complete, paused, or budget-limited | `pi install npm:pi-goal` |
| 211 | [specpi](https://pi.dev/packages/specpi?page=5) | 5,397/mo | package | Scope control and a human-selected harness improvement loop for Pi | `pi install npm:specpi` |
| 213 | [@ferris1225/pi-subagents](https://pi.dev/packages/@ferris1225/pi-subagents?page=5) | 5,267/mo | extension | 面向 pi 的托管子代理团队：专职角色、提交前文档同步、保留线程、自动修复链、模型回退与 Git worktree 隔离。 | `pi install npm:@ferris1225/pi-subagents` |
| 214 | [@agimon-ai/doompi-runner-rmux-darwin-arm64](https://pi.dev/packages/@agimon-ai/doompi-runner-rmux-darwin-arm64?page=5) | 5,213/mo | package | 适用于 macOS arm64 上 DoomPi Runner 的预编译 RMUX 运行时。 | `pi install npm:@agimon-ai/doompi-runner-rmux-darwin-arm64` |
| 220 | [@juanibiapina/pi-extension-settings](https://pi.dev/packages/@juanibiapina/pi-extension-settings?page=5) | 5,112/mo | extension | Pi 扩展，用于跨扩展集中管理设置。 | `pi install npm:@juanibiapina/pi-extension-settings` |
| 224 | [@agimon-ai/doompi-runner-rmux-darwin-x64](https://pi.dev/packages/@agimon-ai/doompi-runner-rmux-darwin-x64?page=5) | 5,088/mo | package | 面向 macOS x64 平台的 DoomPi Runner 预构建 RMUX 运行时。 | `pi install npm:@agimon-ai/doompi-runner-rmux-darwin-x64` |
| 227 | [@agimon-ai/doompi-runner-rmux-linux-arm64](https://pi.dev/packages/@agimon-ai/doompi-runner-rmux-linux-arm64?page=5) | 5,037/mo | package | 面向 Linux arm64 平台的 DoomPi Runner 预构建 RMUX 运行时。 | `pi install npm:@agimon-ai/doompi-runner-rmux-linux-arm64` |
| 237 | [@henryqw/pi-config-store](https://pi.dev/packages/@henryqw/pi-config-store?page=5) | 4,875/mo | package | Safe JSON configuration storage for Pi extensions. | `pi install npm:@henryqw/pi-config-store` |
| 249 | [@sreetej510/pi-hpc-tools](https://pi.dev/packages/@sreetej510/pi-hpc-tools?page=5) | 4,718/mo | extension | Pi 扩展，用于通过 plink 探索远程 HPC/SSH 主机，提供 ls/read/grep 工具，并可通过 /hpc:on 和 /hpc:off 按项目开关。 | `pi install npm:@sreetej510/pi-hpc-tools` |
| 252 | [@gonrocca/nodd](https://pi.dev/packages/@gonrocca/nodd?page=6) | 4,658/mo | extension | Non-negotiable Organic Driven Development — the ODD protocol as runtime mechanism for pi: blocking gates, observed evidence, and promotion to /forge. | `pi install npm:@gonrocca/nodd` |
| 264 | [@amaster.ai/pi-lark](https://pi.dev/packages/@amaster.ai/pi-lark?page=6) | 4,464/mo | extension | Pi extension for Lark/Feishu workspace — calendar, docs, drive, sheets, tasks, mail and more via lark-cli. | `pi install npm:@amaster.ai/pi-lark` |
| 280 | [@bdsqqq/pi](https://pi.dev/packages/@bdsqqq/pi?page=6) | 4,173/mo | package | 面向 pi-coding-agent 的扩展与核心工具 | `pi install npm:@bdsqqq/pi` |

### Skills / Prompt / Rules / 提问

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 5 | [@juicesharp/rpiv-ask-user-question](https://pi.dev/packages/@juicesharp/rpiv-ask-user-question) | 225,831/mo | extension | Pi 扩展：当模型只能靠猜测时，它可以向你提出一份结构化问卷，用带类型的选项代替自由文本回答。 | `pi install npm:@juicesharp/rpiv-ask-user-question` |
| 10 | [bigpowers](https://pi.dev/packages/bigpowers) | 95,550/mo | skill | 73 个代理技能，将 17 年的软件工程纪律凝练为一套面向独立开发者的规范性方法论。 | `pi install npm:bigpowers` |
| 18 | [@dietrichgebert/ponytail](https://pi.dev/packages/@dietrichgebert/ponytail) | 57,036/mo | skill | 面向 AI 代理的『懒人资深开发』模式。最好的代码就是你从未写过的代码。 | `pi install npm:@dietrichgebert/ponytail` |
| 36 | [@narumitw/pi-btw](https://pi.dev/packages/@narumitw/pi-btw) | 31,244/mo | extension | Pi 扩展，新增一个 /btw 顺带提问命令。 | `pi install npm:@narumitw/pi-btw` |
| 38 | [pi-advisor-flow](https://pi.dev/packages/pi-advisor-flow) | 30,333/mo | extension | Advanced Executor/Advisor flow for Pi, fully configurable and extendable. | `pi install npm:pi-advisor-flow` |
| 45 | [pi-prompt-template-model](https://pi.dev/packages/pi-prompt-template-model) | 26,418/mo | extension, prompt | 面向 pi 编码代理的提示词模板模型选择扩展。 | `pi install npm:pi-prompt-template-model` |
| 55 | [@mutmutco/pi-plugin](https://pi.dev/packages/@mutmutco/pi-plugin?page=2) | 20,681/mo | package | 提供 MMI 工作流技能包与 org 门控交付。 | `pi install npm:@mutmutco/pi-plugin` |
| 56 | [pi-interview](https://pi.dev/packages/pi-interview?page=2) | 20,018/mo | extension | 面向 pi 编码代理的交互式访谈表单扩展。 | `pi install npm:pi-interview` |
| 72 | [@7n/rules](https://pi.dev/packages/@7n/rules?page=2) | 14,925/mo | package | 规则与技能包（前缀 n-）的基准 CLI：同步到仓库、delta-lint、合规性检查。 | `pi install npm:@7n/rules` |
| 75 | [@juicesharp/rpiv-i18n](https://pi.dev/packages/@juicesharp/rpiv-i18n?page=2) | 14,499/mo | extension | Pi 扩展。rpiv-* 技能包的本地化基础：区域设置检测、/languages 命令、--locale 标志以及跨包的区域设置注册表。 | `pi install npm:@juicesharp/rpiv-i18n` |
| 84 | [@howaboua/pi-codex-conversion](https://pi.dev/packages/@howaboua/pi-codex-conversion?page=2) | 12,276/mo | extension | 面向 pi 编码代理的 Codex 导向工具与提示词适配器。 | `pi install npm:@howaboua/pi-codex-conversion` |
| 105 | [pi-gauntlet](https://pi.dev/packages/pi-gauntlet?page=3) | 10,100/mo | skill | 为 pi 编码代理提供有主张、带门控的工作流技能包、子代理人设和运行时扩展。 | `pi install npm:pi-gauntlet` |
| 112 | [@llblab/pi-kit](https://pi.dev/packages/@llblab/pi-kit?page=3) | 8,871/mo | extension | Version-pinned distribution of LLB Lab extensions and Skills for Pi | `pi install npm:@llblab/pi-kit` |
| 114 | [@juicesharp/rpiv-advisor](https://pi.dev/packages/@juicesharp/rpiv-advisor?page=3) | 8,840/mo | extension | Pi 扩展。模型在行动之前，可以向更强的评审模型征求第二意见。 | `pi install npm:@juicesharp/rpiv-advisor` |
| 155 | [@agimon-ai/doompi-help](https://pi.dev/packages/@agimon-ai/doompi-help?page=4) | 7,523/mo | extension, skill | 面向 DoomPi 和 Pi 扩展的、激活门控的包使用指南与帮助技能包。 | `pi install npm:@agimon-ai/doompi-help` |
| 184 | [@reddb-io/red-skills-internal](https://pi.dev/packages/@reddb-io/red-skills-internal?page=4) | 6,501/mo | package | reddb.io 内部插件：仅限维护者使用的技能，用于运营 red-skills 仓库。 | `pi install npm:@reddb-io/red-skills-internal` |
| 189 | [bestony-pi-preset](https://pi.dev/packages/bestony-pi-preset?page=4) | 6,271/mo | extension, skill, theme, prompt | Bestony 的个人 Pi 编码代理预设——包含技能包、扩展、提示词和主题。 | `pi install npm:bestony-pi-preset` |
| 209 | [@arhen/pi-core-subagent](https://pi.dev/packages/@arhen/pi-core-subagent?page=5) | 5,443/mo | extension | pi 扩展：提供带依赖图调度器的快速进程内子代理——'needs' 边会约束任务执行并把上游输出带入依赖任务的提示词中；此外还支持后台运行、intercom 与代理间邮箱。Leader 内联定义代理。 | `pi install npm:@arhen/pi-core-subagent` |
| 217 | [@abelxiaoxing/cadence](https://pi.dev/packages/@abelxiaoxing/cadence?page=5) | 5,183/mo | package | Four explicit Abel workflow prompts with stage-isolated design and diagnosis, durable resumable implementation, and three package-owned professional Agents. | `pi install npm:@abelxiaoxing/cadence` |
| 219 | [pi-template-kit](https://pi.dev/packages/pi-template-kit?page=5) | 5,113/mo | prompt | Shared LiquidJS prompt-template engine, filters, XML tag, and file loader for Pi packages. | `pi install npm:pi-template-kit` |
| 222 | [@astrofoundry/pi-astro](https://pi.dev/packages/@astrofoundry/pi-astro?page=5) | 5,108/mo | package | Personal pi customizations (extensions, subagents, skills, prompts, themes) for the pi coding agent. | `pi install npm:@astrofoundry/pi-astro` |
| 233 | [@agimon-ai/doompi-prompt](https://pi.dev/packages/@agimon-ai/doompi-prompt?page=5) | 4,946/mo | extension | Staged recent prompts and saved prompt templates for DoomPi | `pi install npm:@agimon-ai/doompi-prompt` |
| 238 | [@devflow-tools/claude-code-plugin](https://pi.dev/packages/@devflow-tools/claude-code-plugin?page=5) | 4,874/mo | skill | 面向 DevFlow 开发智能运行时的 Claude Code hooks 与技能包（skills）。 | `pi install npm:@devflow-tools/claude-code-plugin` |
| 239 | [@sreetej510/pi-prompt-manager](https://pi.dev/packages/@sreetej510/pi-prompt-manager?page=5) | 4,864/mo | extension, prompt | Pi 扩展，可快速保存、管理并粘贴可复用的提示词，无需重新输入。 | `pi install npm:@sreetej510/pi-prompt-manager` |
| 254 | [@gtrabanco/pi-agentic-workflow](https://pi.dev/packages/@gtrabanco/pi-agentic-workflow?page=6) | 4,638/mo | skill | Pi package: canonical agentic-workflow skills, friendly slash commands, and per-command model routing. | `pi install npm:@gtrabanco/pi-agentic-workflow` |
| 282 | [@nitra/cursor](https://pi.dev/packages/@nitra/cursor?page=6) | 4,114/mo | package | 用于将 cursor 规则（前缀 n-）下载到本地仓库的 CLI。（下载 cursor 规则到本地仓库的 CLI 工具） | `pi install npm:@nitra/cursor` |
| 285 | [@juicesharp/rpiv-args](https://pi.dev/packages/@juicesharp/rpiv-args?page=6) | 4,091/mo | extension, skill, prompt | Pi 扩展。支持 Shell 风格的 $1 / $ARGUMENTS 占位符与 !`cmd` / ```! shell 替换，并在调用时展开到你的 Pi 技能包中。 | `pi install npm:@juicesharp/rpiv-args` |
| 287 | [@agimon-ai/doompi-model-guidance](https://pi.dev/packages/@agimon-ai/doompi-model-guidance?page=6) | 4,072/mo | extension | Per-model system prompt guidance for Pi agents, layered across global and repository scope. | `pi install npm:@agimon-ai/doompi-model-guidance` |

### 代码智能 / 编辑 / Review

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 11 | [pi-lens](https://pi.dev/packages/pi-lens) | 95,452/mo | extension | 面向 pi 的实时代码反馈——LSP、linter、格式化工具、类型检查、结构分析与 booboo | `pi install npm:pi-lens` |
| 13 | [@plannotator/pi-extension](https://pi.dev/packages/@plannotator/pi-extension) | 90,945/mo | package | Plannotator Pi 扩展：支持带注释的交互式计划审查、为代理消息添加注释，以及审查代码/PR。 | `pi install npm:@plannotator/pi-extension` |
| 27 | [pi-simplify](https://pi.dev/packages/pi-simplify) | 38,679/mo | extension | 一个 Pi 扩展，用于审查最近改动的代码，以提升其清晰度、一致性和可维护性。 | `pi install npm:pi-simplify` |
| 43 | [gentle-pi](https://pi.dev/packages/gentle-pi) | 26,748/mo | package | 将 Pi 变成 el Gentleman：一个资深架构师级的开发框架，具备 SDD/OpenSpec、子代理、严格的 TDD 证据、审查护栏和技能包发现能力。 | `pi install npm:gentle-pi` |
| 58 | [pi-hashline-edit-pro](https://pi.dev/packages/pi-hashline-edit-pro?page=2) | 18,870/mo | extension | 适用于 pi-coding-agent 的哈希锚定 read/replace/insert/grep 工具：每一行都会获得唯一的 3 字符哈希（A-Za-z0-9），且跨编辑保持稳定；过期或有歧义的锚点会被拒绝，绝不模糊匹配。撤销记录在重启后依然保留。 | `pi install npm:pi-hashline-edit-pro` |
| 81 | [@agimon-ai/doompi-hashline](https://pi.dev/packages/@agimon-ai/doompi-hashline?page=2) | 12,739/mo | package | Shared snapshot-bound file tags and line anchors for DoomPi tools. | `pi install npm:@agimon-ai/doompi-hashline` |
| 95 | [@heyhuynhgiabuu/pi-pretty](https://pi.dev/packages/@heyhuynhgiabuu/pi-pretty?page=2) | 10,950/mo | extension | 让 pi 的终端输出更美观——语法高亮的文件读取、彩色 bash 输出、树状目录列表等。 | `pi install npm:@heyhuynhgiabuu/pi-pretty` |
| 113 | [pi-pigment](https://pi.dev/packages/pi-pigment?page=3) | 8,861/mo | extension, theme | Pigment for your pi: Shiki-highlighted diffs, shell commands, grep hits, and file listings — every color from your active pi theme | `pi install npm:pi-pigment` |
| 122 | [@narumitw/pi-lsp](https://pi.dev/packages/@narumitw/pi-lsp?page=3) | 8,522/mo | extension | Pi 扩展，通过共享的 runner 提供可配置、语言无关的 LSP 工具。 | `pi install npm:@narumitw/pi-lsp` |
| 144 | [@viccydev/pi-fpa](https://pi.dev/packages/@viccydev/pi-fpa?page=3) | 7,731/mo | package | Full-cycle FP&A planning, strategy, forecast, and review prompts, skills, and data tools for Pi | `pi install npm:@viccydev/pi-fpa` |
| 157 | [@agimon-ai/doompi-file-edit](https://pi.dev/packages/@agimon-ai/doompi-file-edit?page=4) | 7,400/mo | extension | Pi 扩展，提供会话级文件变更时间线与外部编辑器工作流。 | `pi install npm:@agimon-ai/doompi-file-edit` |
| 162 | [@agimon-ai/doompi-edit](https://pi.dev/packages/@agimon-ai/doompi-edit?page=4) | 7,163/mo | extension | Snapshot-bound hashline edit tool for Pi and DoomPi. | `pi install npm:@agimon-ai/doompi-edit` |
| 164 | [@agimon-ai/doompi-read](https://pi.dev/packages/@agimon-ai/doompi-read?page=4) | 7,142/mo | extension | Snapshot-bound hashline read tool for Pi and DoomPi. | `pi install npm:@agimon-ai/doompi-read` |
| 170 | [@agimon-ai/doompi-grep](https://pi.dev/packages/@agimon-ai/doompi-grep?page=4) | 7,068/mo | extension | Snapshot-bound hashline grep for Pi and DoomPi. | `pi install npm:@agimon-ai/doompi-grep` |
| 173 | [@reddb-io/red-skills-dev](https://pi.dev/packages/@reddb-io/red-skills-dev?page=4) | 6,957/mo | package | reddb.io 开发插件——为编码代理提供工程类技能（自主 /afk 循环、/go 调度、问题分类、TDD、诊断、图感知代码库理解等） | `pi install npm:@reddb-io/red-skills-dev` |
| 196 | [@specpow/framework](https://pi.dev/packages/@specpow/framework?page=4) | 6,111/mo | skill | Spec-Powered AI Development Framework - 融合 OpenSpec 规范驱动 + Superpowers 执行引擎的企业级 AI 辅助编程框架（OpenSpec 规范驱动 + Superpowers 执行引擎的 AI 编程框架） | `pi install npm:@specpow/framework` |
| 210 | [@difflab/pi](https://pi.dev/packages/@difflab/pi?page=5) | 5,425/mo | package | Tools and skills for the pi coding agent | `pi install npm:@difflab/pi` |
| 223 | [pi-pr-review](https://pi.dev/packages/pi-pr-review?page=5) | 5,090/mo | extension | 在 Pi 编码代理中为 GitHub pull request 提供并行 AI 代码审查：与模型无关的分层子代理、结构化审查意见、可选验证，以及由宿主控制的 COMMENT 或符合条件时的 APPROVE 发布。 | `pi install npm:pi-pr-review` |
| 242 | [@sreetej510/pi-shipd-checks](https://pi.dev/packages/@sreetej510/pi-shipd-checks?page=5) | 4,840/mo | extension | Pi 扩展，通过 /checks 对基准任务的 agent_prompt.md、test.patch 和 solution.patch 进行严格的多 AI 代理公平性审查，并附带行为测试缺口分析。 | `pi install npm:@sreetej510/pi-shipd-checks` |
| 284 | [codecartographer-pi](https://pi.dev/packages/codecartographer-pi?page=6) | 4,091/mo | package | Turn an unfamiliar codebase into a validated reimplementation spec, then synthesize confirmed specs and a product vision into a traceable plan. | `pi install npm:codecartographer-pi` |
| 289 | [@patimweb/pi-sentinel](https://pi.dev/packages/@patimweb/pi-sentinel?page=6) | 4,063/mo | extension | Verification harness for the pi coding agent: runs your checks when the agent edits and before it is done, sends it back when they fail, and checkpoints every run so it can be rewound. | `pi install npm:@patimweb/pi-sentinel` |

### 安全 / 权限 / Sandbox

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 22 | [@gotgenes/pi-permission-system](https://pi.dev/packages/@gotgenes/pi-permission-system) | 47,458/mo | extension | 面向 Pi 编码代理的权限强制扩展。 | `pi install npm:@gotgenes/pi-permission-system` |
| 44 | [cc-safety-net](https://pi.dev/packages/cc-safety-net) | 26,647/mo | package | 编码代理 CLI 钩子：阻止破坏性命令与机密文件访问。 | `pi install npm:cc-safety-net` |
| 47 | [@trim21/personal-pi-extensions](https://pi.dev/packages/@trim21/personal-pi-extensions) | 24,670/mo | package | 自定义 pi 编码代理扩展：bwrap 沙箱、工作区守卫、opencode 编辑，以及更多。 | `pi install npm:@trim21/personal-pi-extensions` |
| 63 | [latchkey](https://pi.dev/packages/latchkey?page=2) | 17,376/mo | package | 一个 CLI 工具，可将 API 凭据注入到发往第三方服务的 curl 请求中。 | `pi install npm:latchkey` |
| 65 | [betterwright](https://pi.dev/packages/betterwright?page=2) | 17,167/mo | package | 面向 AI 代理的持久化、受策略保护的 Playwright 浏览器，具备网络控制、可信凭据自动填充、证据截图和 CAPTCHA 辅助功能。 | `pi install npm:betterwright` |
| 76 | [pi-goal-list-loop-audit](https://pi.dev/packages/pi-goal-list-loop-audit?page=2) | 14,069/mo | extension | 自主 pi 的任务控制：访谈起草的目标、受审计的任务队列，以及可运行数小时的永久循环（metric、spec、project-audit）。一个独立的、无需扩展的审计进程会用原始证据重新验证每次完成，而不会持有 | `pi install npm:pi-goal-list-loop-audit` |
| 80 | [@agimon-ai/doompi-web-security](https://pi.dev/packages/@agimon-ai/doompi-web-security?page=2) | 12,960/mo | package | Shared security primitives for the DoomPi web cockpit: sealed channels and signed bundle manifests for independently trusted verifiers. | `pi install npm:@agimon-ai/doompi-web-security` |
| 85 | [rolebox](https://pi.dev/packages/rolebox?page=2) | 12,171/mo | extension, skill | Agent plugin — define custom AI agent roles with per-role prompts, models, skills, and permissions | `pi install npm:rolebox` |
| 100 | [kifaru](https://pi.dev/packages/kifaru?page=2) | 10,370/mo | package | Kifaru security agent on the Pi runtime | `pi install npm:kifaru` |
| 187 | [trimegisto](https://pi.dev/packages/trimegisto?page=4) | 6,310/mo | package | Pi multi-agent orchestration: tiered parallel sub-agents, @mentions, loop guard, file locks, context broker, dashboard. | `pi install npm:trimegisto` |
| 188 | [@agimon-ai/doompi-sandbox](https://pi.dev/packages/@agimon-ai/doompi-sandbox?page=4) | 6,289/mo | extension | Container sandbox for DoomPi launches: the agent, extensions, and tools run inside Docker or Podman while the terminal stays on the host | `pi install npm:@agimon-ai/doompi-sandbox` |
| 261 | [pi-better-harness](https://pi.dev/packages/pi-better-harness?page=6) | 4,524/mo | extension | Pi extension bundle for a write sandbox, subagents, background tasks, SSH, goals, and structured plans. | `pi install npm:pi-better-harness` |
| 275 | [pi-verdict](https://pi.dev/packages/pi-verdict?page=6) | 4,233/mo | extension | A minimal permission gate for Pi in the style of Claude Code's auto mode | `pi install npm:pi-verdict` |
| 283 | [@amaster.ai/pi-security](https://pi.dev/packages/@amaster.ai/pi-security?page=6) | 4,111/mo | extension | Pi extension for resource-aware security policy engine and tool authorization | `pi install npm:@amaster.ai/pi-security` |
| 292 | [@aliou/pi-guardrails](https://pi.dev/packages/@aliou/pi-guardrails?page=6) | 4,022/mo | extension | ![banner](https://assets.aliou.me/github/aliou/pi-guardrails/banner.png) | `pi install npm:@aliou/pi-guardrails` |
| 298 | [@erichll/pi-auto-review](https://pi.dev/packages/@erichll/pi-auto-review?page=6) | 3,992/mo | extension | Fail-closed, model-backed approval broker for Pi: deterministically hard-denies dangerous operations, reviews dangerous boundaries with a reviewer model, and issues one-shot expiring grants that OS sandbox adapters must consume before retrying. | `pi install npm:@erichll/pi-auto-review` |

### 其他 / 待复核

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 49 | [@goofansu/pi-stuff](https://pi.dev/packages/@goofansu/pi-stuff) | 23,441/mo | package | A collection of personal Pi extensions. | `pi install npm:@goofansu/pi-stuff` |
| 86 | [@narumitw/pi-stamp](https://pi.dev/packages/@narumitw/pi-stamp?page=2) | 12,129/mo | extension | Pi extension for transcript timestamps, assistant metadata, and tool timing. | `pi install npm:@narumitw/pi-stamp` |
| 129 | [@cratis/pi](https://pi.dev/packages/@cratis/pi?page=3) | 8,188/mo | skill | Configuration-aware Cratis AI integration for Pi | `pi install npm:@cratis/pi` |
| 131 | [@henryqw/pi-pr](https://pi.dev/packages/@henryqw/pi-pr?page=3) | 8,081/mo | package | Run /pr to safely discover or link the current pull request, then create, update, address feedback, fix CI, or merge when ready. | `pi install npm:@henryqw/pi-pr` |
| 156 | [pi-typesafe](https://pi.dev/packages/pi-typesafe?page=4) | 7,453/mo | extension | TypeSafe AI (Jev) decisions for Pi: batched Choice/Score/Noul evaluation tool, terminal playground, and a typed API other extensions build on. | `pi install npm:pi-typesafe` |
| 234 | [@czottmann/pi-automode](https://pi.dev/packages/@czottmann/pi-automode?page=5) | 4,929/mo | extension | Claude Code-style auto mode guardrail for pi. | `pi install npm:@czottmann/pi-automode` |
| 235 | [bermudis-pi-goodies](https://pi.dev/packages/bermudis-pi-goodies?page=5) | 4,921/mo | package | 一组小巧且常用的 Pi 扩展合集。 | `pi install npm:bermudis-pi-goodies` |
| 250 | [projectops](https://pi.dev/packages/projectops?page=5) | 4,704/mo | package | ProjectOps — 완전 자동화 GitHub 프로젝트 관리 템플릿 통합 CLI | `pi install npm:projectops` |
| 290 | [@jameslovespancakes/pi-plus](https://pi.dev/packages/@jameslovespancakes/pi-plus?page=6) | 4,057/mo | extension | pi and more | `pi install npm:@jameslovespancakes/pi-plus` |
