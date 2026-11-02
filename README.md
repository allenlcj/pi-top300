# Pi Top 300

Pi 官方 Package Catalog 前 300 热门包的用途分类目录（All types · Most downloads）。

[分类指南](docs/categories.md) · [按排名清单](docs/packages.md) · [原始 JSON 数据](data/packages-latest.json)

> ⚠️ Pi 包可能以当前用户权限执行代码，安装前请审查源码和权限。
> 下载量为 npm 月下载量，不代表质量或安全性。分类基于名称和描述的初步归类，人工意见维护在 `data/categories.yaml`。

- 快照 `2026-11-02`（[历史快照](data/snapshots/)）· 共 300 包

## 分类总览

| 类别 | 数量 | 占比 |
| --- | ---: | ---: |
| [UI / TUI / Session / 观测](#ui-tui-session-观测) | 47 | 16% |
| [Web / Browser / Research / MCP](#web-browser-research-mcp) | 45 | 15% |
| [Agent 编排 / Subagent / Plan / Goal / Task](#agent-编排-subagent-plan-goal-task) | 44 | 15% |
| [Context / Memory / Knowledge / Compaction](#context-memory-knowledge-compaction) | 39 | 13% |
| [模型 / Provider / 路由 / 用量](#模型-provider-路由-用量) | 36 | 12% |
| [Skills / Prompt / Rules / 提问](#skills-prompt-rules-提问) | 23 | 8% |
| [Runtime / 后台任务 / Worktree / 集成](#runtime-后台任务-worktree-集成) | 23 | 8% |
| [代码智能 / 编辑 / Review](#代码智能-编辑-review) | 20 | 7% |
| [安全 / 权限 / Sandbox](#安全-权限-sandbox) | 15 | 5% |
| [其他 / 待复核](#其他-待复核) | 8 | 3% |

## 按类别清单

### UI / TUI / Session / 观测

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 11 | [@juicesharp/rpiv-todo](https://pi.dev/packages/@juicesharp/rpiv-todo) | 111,844/mo | extension | Pi 扩展：为模型提供待办事项列表，以实时浮层渲染，且 /reload 与会话压缩后依然保留。 | `pi install npm:@juicesharp/rpiv-todo` |
| 12 | [@langfuse/pi-observability-plugin](https://pi.dev/packages/@langfuse/pi-observability-plugin) | 93,259/mo | extension | Langfuse observability extension for the pi coding agent — traces prompts, agent turns, model generations, and tool calls to Langfuse. | `pi install npm:@langfuse/pi-observability-plugin` |
| 22 | [pi-powerline-footer](https://pi.dev/packages/pi-powerline-footer) | 65,234/mo | extension | 面向 pi 编码代理的 Powerline 风格状态栏扩展。 | `pi install npm:pi-powerline-footer` |
| 33 | [pi-cc-extensions](https://pi.dev/packages/pi-cc-extensions) | 41,290/mo | extension | 一套 Pi 效率增强套件，提供 Claude Code 风格 UI、上下文检查以及代理/会话引用。 | `pi install npm:pi-cc-extensions` |
| 38 | [pi-btw](https://pi.dev/packages/pi-btw) | 34,201/mo | extension | 一个 pi 扩展，通过 /btw 进行并行的旁路对话 | `pi install npm:pi-btw` |
| 41 | [glimpseui](https://pi.dev/packages/glimpseui) | 32,737/mo | prompt | 面向脚本和 AI 代理的原生微 UI——提供跨平台 WebView 窗口与双向 JSON 通信。 | `pi install npm:glimpseui` |
| 73 | [@raindrop-ai/pi-agent](https://pi.dev/packages/@raindrop-ai/pi-agent?page=2) | 21,338/mo | package | 为 Pi Agent 提供 Raindrop 可观测性——通过 subscriber 或 pi-coding-agent 扩展实现自动追踪。 | `pi install npm:@raindrop-ai/pi-agent` |
| 75 | [@agimon-ai/po-config](https://pi.dev/packages/@agimon-ai/po-config?page=2) | 21,013/mo | package | Typed configuration loading, validation, and host services for composing Po sessions. | `pi install npm:@agimon-ai/po-config` |
| 76 | [@agimon-ai/po-minor-mode](https://pi.dev/packages/@agimon-ai/po-minor-mode?page=2) | 20,703/mo | extension | Minor-mode ownership, catalog, commands, and session lifecycle. | `pi install npm:@agimon-ai/po-minor-mode` |
| 79 | [@brainervirus/workit-pi](https://pi.dev/packages/@brainervirus/workit-pi?page=2) | 20,171/mo | extension | Workit native extension for Pi — tools, method skills, and session continuity | `pi install npm:@brainervirus/workit-pi` |
| 88 | [@agimon-ai/po-ui](https://pi.dev/packages/@agimon-ai/po-ui?page=2) | 16,210/mo | extension | Leader-key menus, themes, and TUI components for Po and Pi extensions. | `pi install npm:@agimon-ai/po-ui` |
| 91 | [pi-straw-boss](https://pi.dev/packages/pi-straw-boss?page=2) | 15,972/mo | extension | Straw Boss coordination for pi in Herdr: sessions join a tab's net by choice, the first joiner is its main agent, a workspace tower opens on demand with a live monitoring dashboard, and boss_broadcast reaches the rest | `pi install npm:pi-straw-boss` |
| 100 | [@agimon-ai/po-session](https://pi.dev/packages/@agimon-ai/po-session?page=2) | 14,237/mo | extension | Shared session coordination services for Po. | `pi install npm:@agimon-ai/po-session` |
| 112 | [@agimon-ai/po-notification](https://pi.dev/packages/@agimon-ai/po-notification?page=3) | 12,976/mo | extension | Desktop notifications and an animated shell-tab title for Po sessions. | `pi install npm:@agimon-ai/po-notification` |
| 116 | [@agimon-ai/po-profile](https://pi.dev/packages/@agimon-ai/po-profile?page=3) | 12,725/mo | extension | Persona and environment profile switching for Po sessions. | `pi install npm:@agimon-ai/po-profile` |
| 119 | [@agimon-ai/po-autostop](https://pi.dev/packages/@agimon-ai/po-autostop?page=3) | 12,670/mo | extension | Shuts a Po session down once the agent settles and stays idle. | `pi install npm:@agimon-ai/po-autostop` |
| 121 | [@agimon-ai/po-major-mode](https://pi.dev/packages/@agimon-ai/po-major-mode?page=3) | 12,516/mo | extension | Named major-mode selection and layer composition switching for Po sessions. | `pi install npm:@agimon-ai/po-major-mode` |
| 128 | [pi-zentui](https://pi.dev/packages/pi-zentui?page=3) | 12,061/mo | extension, theme | 灵感源自 Starship 的状态行与 Opencode 风格 TUI，适用于 Pi。 | `pi install npm:pi-zentui` |
| 133 | [@agimon-ai/po-task](https://pi.dev/packages/@agimon-ai/po-task?page=3) | 11,890/mo | package | Persistent, dependency-aware task graphs and subagent delegation for Pi coding sessions. | `pi install npm:@agimon-ai/po-task` |
| 136 | [@agimon-ai/po-style-system](https://pi.dev/packages/@agimon-ai/po-style-system?page=3) | 11,850/mo | package | Optional Po story preview integration for the style-system package. | `pi install npm:@agimon-ai/po-style-system` |
| 137 | [pi-coding-agent-test](https://pi.dev/packages/pi-coding-agent-test?page=3) | 11,831/mo | package | Deterministic end-to-end testing for Pi Coding Agent extensions, tools, sessions, and TUI output. | `pi install npm:pi-coding-agent-test` |
| 140 | [pi-ask-user](https://pi.dev/packages/pi-ask-user?page=3) | 11,816/mo | extension | 面向 pi-coding-agent 的交互式 ask_user 工具，提供可搜索的分栏选择 UI、多选与自由文本输入。 | `pi install npm:pi-ask-user` |
| 141 | [@agimon-ai/po-log](https://pi.dev/packages/@agimon-ai/po-log?page=3) | 11,812/mo | extension | Session metrics, findings, and sink status for headless agent observability. | `pi install npm:@agimon-ai/po-log` |
| 142 | [@agimon-ai/po-voice](https://pi.dev/packages/@agimon-ai/po-voice?page=3) | 11,784/mo | extension | Client audio capture, host transcription, and autonomous narration for Pi agents. | `pi install npm:@agimon-ai/po-voice` |
| 144 | [@agimon-ai/po-computer-use](https://pi.dev/packages/@agimon-ai/po-computer-use?page=3) | 11,778/mo | extension | Session scoped semantic computer control through the Po Desktop capability. | `pi install npm:@agimon-ai/po-computer-use` |
| 145 | [@agimon-ai/po-user-feedback](https://pi.dev/packages/@agimon-ai/po-user-feedback?page=3) | 11,772/mo | extension | Structured user questions with interactive and autonomous Voice handoff for Pi agents. | `pi install npm:@agimon-ai/po-user-feedback` |
| 147 | [@agimon-ai/po-git](https://pi.dev/packages/@agimon-ai/po-git?page=3) | 11,735/mo | extension | Git worktree sessions for Po: spawn an isolated worktree with its own session and manage it from the parent | `pi install npm:@agimon-ai/po-git` |
| 172 | [@agimon-ai/doompi-telemetry](https://pi.dev/packages/@agimon-ai/doompi-telemetry?page=4) | 10,788/mo | package | 面向 DoomPi 会话的宿主无关遥测、OpenTelemetry 控制与 Log Sink 适配器。 | `pi install npm:@agimon-ai/doompi-telemetry` |
| 178 | [@agimon-ai/doompi-minor-mode](https://pi.dev/packages/@agimon-ai/doompi-minor-mode?page=4) | 10,451/mo | extension | Minor-mode ownership, catalog, commands, and session lifecycle. | `pi install npm:@agimon-ai/doompi-minor-mode` |
| 179 | [@agimon-ai/po-telemetry](https://pi.dev/packages/@agimon-ai/po-telemetry?page=4) | 10,408/mo | package | Host-neutral telemetry, OpenTelemetry controls, and Log Sink adapters for Po sessions. | `pi install npm:@agimon-ai/po-telemetry` |
| 189 | [@agimon-ai/doompi-ui](https://pi.dev/packages/@agimon-ai/doompi-ui?page=4) | 9,805/mo | extension | 面向 DoomPi 与 Pi 扩展的 Leader 键菜单、主题与 TUI 组件。 | `pi install npm:@agimon-ai/doompi-ui` |
| 193 | [@agimon-ai/doompi-config](https://pi.dev/packages/@agimon-ai/doompi-config?page=4) | 9,542/mo | package | 用于编排 DoomPi 会话的类型化配置加载、校验以及宿主适配器。 | `pi install npm:@agimon-ai/doompi-config` |
| 197 | [@ravshansbox/pi-statusline](https://pi.dev/packages/@ravshansbox/pi-statusline?page=4) | 9,426/mo | extension | Statusline and prompt history extension for pi | `pi install npm:@ravshansbox/pi-statusline` |
| 206 | [@juicesharp/rpiv-btw](https://pi.dev/packages/@juicesharp/rpiv-btw?page=5) | 8,919/mo | extension | Pi 扩展。/btw 斜杠命令，用于向同一个主模型提出一次性附带问题，而不污染主对话。 | `pi install npm:@juicesharp/rpiv-btw` |
| 242 | [@agimon-ai/doompi-session](https://pi.dev/packages/@agimon-ai/doompi-session?page=5) | 6,910/mo | extension | Shared session coordination services for DoomPi. | `pi install npm:@agimon-ai/doompi-session` |
| 255 | [@agimon-ai/doompi-profile](https://pi.dev/packages/@agimon-ai/doompi-profile?page=6) | 6,464/mo | extension | Persona and environment profile switching for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-profile` |
| 261 | [@agimon-ai/doompi-autostop](https://pi.dev/packages/@agimon-ai/doompi-autostop?page=6) | 6,366/mo | extension | Shuts a DoomPi session down once the agent settles and stays idle. | `pi install npm:@agimon-ai/doompi-autostop` |
| 262 | [@agimon-ai/doompi-notification](https://pi.dev/packages/@agimon-ai/doompi-notification?page=6) | 6,353/mo | extension | Desktop notifications and an animated shell-tab title for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-notification` |
| 263 | [@agimon-ai/doompi-major-mode](https://pi.dev/packages/@agimon-ai/doompi-major-mode?page=6) | 6,347/mo | extension | Named major-mode selection and layer composition switching for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-major-mode` |
| 273 | [@agimon-ai/doompi-task](https://pi.dev/packages/@agimon-ai/doompi-task?page=6) | 6,125/mo | package | 为 Pi 编码会话提供持久化、感知依赖的任务图与子代理委派。 | `pi install npm:@agimon-ai/doompi-task` |
| 276 | [@agimon-ai/doompi-voice](https://pi.dev/packages/@agimon-ai/doompi-voice?page=6) | 6,065/mo | extension | 为 Pi 代理提供客户端音频采集、主机端转写与自主叙述功能。 | `pi install npm:@agimon-ai/doompi-voice` |
| 277 | [@agimon-ai/doompi-log](https://pi.dev/packages/@agimon-ai/doompi-log?page=6) | 6,047/mo | extension | 为代理可观测性提供 Pi 会话指标、发现（findings）、数据接收端（sink）状态与 Log Metrics 覆盖层。 | `pi install npm:@agimon-ai/doompi-log` |
| 279 | [@agimon-ai/doompi-loop](https://pi.dev/packages/@agimon-ai/doompi-loop?page=6) | 6,028/mo | extension | 为 Pi 编码代理提供会话级循环提示词调度器与循环控制。 | `pi install npm:@agimon-ai/doompi-loop` |
| 281 | [@agimon-ai/doompi-hook](https://pi.dev/packages/@agimon-ai/doompi-hook?page=6) | 5,991/mo | extension | Claude-Code-compatible repository and plugin hook runner for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-hook` |
| 292 | [@agimon-ai/doompi-git](https://pi.dev/packages/@agimon-ai/doompi-git?page=6) | 5,835/mo | extension | Git worktree sessions for DoomPi: spawn an isolated worktree with its own session and manage it from the parent | `pi install npm:@agimon-ai/doompi-git` |
| 296 | [@agimon-ai/doompi-user-feedback](https://pi.dev/packages/@agimon-ai/doompi-user-feedback?page=6) | 5,816/mo | extension | 为 Pi 代理提供结构化用户提问，并支持交互式与自主式 Voice 交接。 | `pi install npm:@agimon-ai/doompi-user-feedback` |
| 298 | [@mu-crew/mu](https://pi.dev/packages/@mu-crew/mu?page=6) | 5,785/mo | package | A persistent, observable crew of pi agents running in one tmux or herdr session per workstream, coordinated through a built-in task DAG. | `pi install npm:@mu-crew/mu` |

### Web / Browser / Research / MCP

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 3 | [pi-web-access](https://pi.dev/packages/pi-web-access) | 1,006,277/mo | extension | 为 Pi 编码代理提供网页搜索、URL 抓取、GitHub 仓库克隆、PDF 提取、YouTube 视频理解与本地视频分析。支持 OpenAI、Brave、Parallel、TinyFish、Search1API、Searchinfinity、Querit、Tavily、Firecrawl、Jina、SERPdive、Ka | `pi install npm:pi-web-access` |
| 4 | [pi-mcp-extension](https://pi.dev/packages/pi-mcp-extension) | 773,324/mo | extension | 面向 Pi 编码代理的 MCP（Model Context Protocol）客户端扩展——将 Pi 连接到任意 MCP 服务器。 | `pi install npm:pi-mcp-extension` |
| 23 | [@onkernel/browser-loop](https://pi.dev/packages/@onkernel/browser-loop) | 62,238/mo | extension | Browser tools for your agent: framework-neutral tool catalog, per-model compilation, Kernel-browser execution, and a pi binding + extension | `pi install npm:@onkernel/browser-loop` |
| 26 | [@companion-ai/feynman](https://pi.dev/packages/@companion-ai/feynman) | 50,319/mo | package | 基于 Pi 和 alphaXiv 构建的研究优先 CLI 代理 | `pi install npm:@companion-ai/feynman` |
| 39 | [@quintinshaw/pi-dynamic-workflows](https://pi.dev/packages/@quintinshaw/pi-dynamic-workflows) | 33,538/mo | package | 面向 Pi 的 Claude Code 风格动态工作流：将任务扇出至数百个子代理，具备真实模型路由、token/成本核算、断点续跑、git 工作树隔离、交互式 /workflows TUI，以及真正的 /deep-research。 | `pi install npm:@quintinshaw/pi-dynamic-workflows` |
| 46 | [@agimon-ai/log-sink-mcp](https://pi.dev/packages/@agimon-ai/log-sink-mcp) | 31,515/mo | package | 支持 HTTP 摄取与 AI 分析的日志汇聚（log sink）MCP 服务器。 | `pi install npm:@agimon-ai/log-sink-mcp` |
| 50 | [@ff-labs/pi-fff](https://pi.dev/packages/@ff-labs/pi-fff) | 29,371/mo | extension | pi 扩展：由 FFF 驱动的模糊文件与内容搜索。 | `pi install npm:@ff-labs/pi-fff` |
| 51 | [@agimon-ai/po-web-components](https://pi.dev/packages/@agimon-ai/po-web-components?page=2) | 29,307/mo | theme | Shared web components and theme tokens for the Po cockpit and its web plugins: shadcn-style primitives on Radix, tuned to the Po palette, with runtime theme configs. | `pi install npm:@agimon-ai/po-web-components` |
| 55 | [@agimon-ai/po-logsink](https://pi.dev/packages/@agimon-ai/po-logsink?page=2) | 27,183/mo | package | Log sink MCP server with HTTP ingestion and AI analysis | `pi install npm:@agimon-ai/po-logsink` |
| 59 | [@datadog/pi-plugin](https://pi.dev/packages/@datadog/pi-plugin?page=2) | 25,436/mo | package | Use Datadog directly in the Pi coding agent through a preconfigured Datadog MCP server. Query logs, metrics, traces, dashboards, and more through natural conversation. | `pi install npm:@datadog/pi-plugin` |
| 81 | [@mjasnikovs/pi-task](https://pi.dev/packages/@mjasnikovs/pi-task?page=2) | 18,752/mo | extension | 为本地模型提供确定性的任务规划与规格编排：崩溃安全的 /task 流水线，带 verify/enforce 关卡、实时远程 Web 视图，以及 web/docs/fetch/worker 子代理工具。 | `pi install npm:@mjasnikovs/pi-task` |
| 85 | [pi-agent-browser-native](https://pi.dev/packages/pi-agent-browser-native?page=2) | 17,566/mo | extension | pi 扩展，将 agent-browser 作为原生工具开放，用于浏览器自动化。 | `pi install npm:pi-agent-browser-native` |
| 93 | [@ollama/pi-web-search](https://pi.dev/packages/@ollama/pi-web-search?page=2) | 15,235/mo | extension | 面向 Pi 代理的网络搜索与抓取工具——使用 Ollama 的网络搜索与抓取 API。 | `pi install npm:@ollama/pi-web-search` |
| 98 | [pi-web-ui](https://pi.dev/packages/pi-web-ui?page=2) | 14,673/mo | package | 基于 pi SDK（@earendil-works/pi-coding-agent）的 pi 编码代理 Web 聊天界面——一条命令即可运行，支持 Docker/systemd/launchd 部署。 | `pi install npm:pi-web-ui` |
| 105 | [@agimon-ai/doompi-web-components](https://pi.dev/packages/@agimon-ai/doompi-web-components?page=3) | 13,518/mo | theme | Shared web components and theme tokens for the DoomPi cockpit and its web plugins: shadcn-style primitives on Radix, tuned to the Doom palette, with runtime theme configs. | `pi install npm:@agimon-ai/doompi-web-components` |
| 106 | [pi-shazam](https://pi.dev/packages/pi-shazam?page=3) | 13,517/mo | extension | Pi coding agent native codebase awareness toolkit — 7 structural analysis tools. Also supports MCP (Cursor, Claude Desktop, Windsurf, etc.) | `pi install npm:pi-shazam` |
| 109 | [pi-markdown-preview](https://pi.dev/packages/pi-markdown-preview?page=3) | 13,382/mo | package | 面向 pi 的渲染版 Markdown + LaTeX 预览，支持终端、浏览器和 PDF 输出。 | `pi install npm:pi-markdown-preview` |
| 111 | [@agimon-ai/po-web-dashboard](https://pi.dev/packages/@agimon-ai/po-web-dashboard?page=3) | 13,150/mo | package | Shared browser state, actions and optional views for Po dashboard templates. | `pi install npm:@agimon-ai/po-web-dashboard` |
| 113 | [@agimon-ai/po-domain](https://pi.dev/packages/@agimon-ai/po-domain?page=3) | 12,935/mo | extension, skill | Domain selection, resource staging, and MCP scoping for Po sessions. | `pi install npm:@agimon-ai/po-domain` |
| 117 | [@agimon-ai/po-skill](https://pi.dev/packages/@agimon-ai/po-skill?page=3) | 12,719/mo | extension | Session skill catalogue, deferred skill discovery, and the skill browser for Po. | `pi install npm:@agimon-ai/po-skill` |
| 118 | [@agimon-ai/po](https://pi.dev/packages/@agimon-ai/po?page=3) | 12,687/mo | package | Opinionated, composable agent harness for scoped tools, skills, MCP servers, and developer workflows. | `pi install npm:@agimon-ai/po` |
| 122 | [@agimon-ai/po-template-advanced](https://pi.dev/packages/@agimon-ai/po-template-advanced?page=3) | 12,173/mo | package | Advanced multi-panel template for the Po web client. | `pi install npm:@agimon-ai/po-template-advanced` |
| 127 | [@agntn/web](https://pi.dev/packages/@agntn/web?page=3) | 12,078/mo | extension | Unified web search and read provider for agents and CLI. | `pi install npm:@agntn/web` |
| 131 | [@agimon-ai/po-mcp](https://pi.dev/packages/@agimon-ai/po-mcp?page=3) | 11,948/mo | extension | Domain-aware MCP server selection and access boundaries for Pi sessions composed with Po. | `pi install npm:@agimon-ai/po-mcp` |
| 152 | [@agimon-ai/po-template-elegant](https://pi.dev/packages/@agimon-ai/po-template-elegant?page=4) | 11,705/mo | package | Elegant chat-first template for the Po web client. | `pi install npm:@agimon-ai/po-template-elegant` |
| 173 | [pi-claude-marketplace](https://pi.dev/packages/pi-claude-marketplace?page=4) | 10,786/mo | extension | 从 Pi Coding Agent 访问 Claude 插件市场。支持 Claude 命令、技能包、AI 代理、hooks 和 MCP 服务器。 | `pi install npm:pi-claude-marketplace` |
| 176 | [@juicesharp/rpiv-web-tools](https://pi.dev/packages/@juicesharp/rpiv-web-tools?page=4) | 10,619/mo | extension | Pi 扩展。为模型提供网络搜索与抓取能力，支持可插拔的模型提供方（Brave、Tavily、Serper、Exa、You.com、Jina、Firecrawl、Perplexity、SearXNG、Ollama）。 | `pi install npm:@juicesharp/rpiv-web-tools` |
| 182 | [@gyoungwe/research-suite](https://pi.dev/packages/@gyoungwe/research-suite?page=4) | 10,326/mo | package | Bundled Drone native Pi research suite | `pi install npm:@gyoungwe/research-suite` |
| 183 | [@firstpick/pi-package-webui](https://pi.dev/packages/@firstpick/pi-package-webui?page=4) | 10,312/mo | extension | Pi Web UI 配套包，提供本地浏览器界面 CLI，以及 /webui-start 和 /webui-status 命令。 | `pi install npm:@firstpick/pi-package-webui` |
| 185 | [@jmfederico/pi-web](https://pi.dev/packages/@jmfederico/pi-web?page=4) | 10,169/mo | package | 为真实工作区中持久化的 Pi Coding Agent 会话提供 Web UI。 | `pi install npm:@jmfederico/pi-web` |
| 196 | [donsetch](https://pi.dev/packages/donsetch?page=4) | 9,427/mo | package | 面向 AI 代理的网页抓取、搜索与爬取能力。零 API 密钥。Chrome 级真实 TLS。 | `pi install npm:donsetch` |
| 198 | [@selesai/code](https://pi.dev/packages/@selesai/code?page=4) | 9,316/mo | package | 持续维护、以扩展为先的 Pi coding agent，内置工作流、子代理、网页研究、提问、技能包以及增强的终端 UI。 | `pi install npm:@selesai/code` |
| 203 | [pi-lsp-adapter](https://pi.dev/packages/pi-lsp-adapter?page=5) | 9,134/mo | package | Pi extension that gives coding agents Language Server Protocol tools for diagnostics, hover, definitions, references, and symbol search | `pi install npm:pi-lsp-adapter` |
| 205 | [@gyoungwe/pi-research](https://pi.dev/packages/@gyoungwe/pi-research?page=5) | 8,993/mo | package | Evidence-gated research retrieval, reading, deposition and source-grounded answer tools for native Pi | `pi install npm:@gyoungwe/pi-research` |
| 215 | [@agent-sh/computer-use-linux](https://pi.dev/packages/@agent-sh/computer-use-linux?page=5) | 8,101/mo | package | Native Linux desktop control for AI agents (MCP server, Pi tools, and CLI): semantic AT-SPI accessibility trees, screenshots, compositor window targeting, Wayland/X11 input, and an on-screen activity indicator. | `pi install npm:@agent-sh/computer-use-linux` |
| 219 | [pi-webapp](https://pi.dev/packages/pi-webapp?page=5) | 7,739/mo | package | A browser interface for Pi with live chat, workspaces, models, and attachments | `pi install npm:pi-webapp` |
| 224 | [@juicesharp/rpiv-pi](https://pi.dev/packages/@juicesharp/rpiv-pi?page=5) | 7,504/mo | extension, skill | 基于技能包的 Pi Agent 开发工作流：30 个带契约的技能（discover → research → design → plan → implement → validate → code-review → commit 等）、它们派发的 15 个具名子代理，以及四个内置的 /wf 工作流串联流程 | `pi install npm:@juicesharp/rpiv-pi` |
| 230 | [opencode-codebase-index](https://pi.dev/packages/opencode-codebase-index?page=5) | 7,336/mo | package | 宿主无关的语义化代码库搜索，支持嵌入（embeddings）、符号发现与调用图工具。 | `pi install npm:opencode-codebase-index` |
| 232 | [pi-docparser](https://pi.dev/packages/pi-docparser?page=5) | 7,279/mo | extension, skill | Pi package that adds document_parse, document_search, document_screenshot, and a companion skill for local document understanding with LiteParse v2. | `pi install npm:pi-docparser` |
| 233 | [@xynogen/pix-pretty](https://pi.dev/packages/@xynogen/pix-pretty?page=5) | 7,200/mo | extension | 增强的工具输出渲染：语法高亮、文件图标、树形视图、diff 渲染和 FFF 搜索 | `pi install npm:@xynogen/pix-pretty` |
| 235 | [pi-browser-use](https://pi.dev/packages/pi-browser-use?page=5) | 7,179/mo | extension | Opinionated browser automation via chrome-devtools-mcp: native Pi extension and portable Agent Plugins 1.0 skills + MCP server. | `pi install npm:pi-browser-use` |
| 240 | [@agimon-ai/doompi-domain](https://pi.dev/packages/@agimon-ai/doompi-domain?page=5) | 6,960/mo | extension, skill | Domain selection, resource staging, and MCP scoping for DoomPi sessions. | `pi install npm:@agimon-ai/doompi-domain` |
| 247 | [@agimon-ai/doompi](https://pi.dev/packages/@agimon-ai/doompi?page=5) | 6,693/mo | package | 为受限范围的代理工具、技能包（skills）、MCP 服务器与开发者工作流提供的一套有主张、可组合的 Pi 发行版。 | `pi install npm:@agimon-ai/doompi` |
| 257 | [@agimon-ai/doompi-skill](https://pi.dev/packages/@agimon-ai/doompi-skill?page=6) | 6,423/mo | extension | Session skill catalogue, deferred skill discovery, and the skill browser for DoomPi. | `pi install npm:@agimon-ai/doompi-skill` |
| 266 | [@agimon-ai/doompi-mcp](https://pi.dev/packages/@agimon-ai/doompi-mcp?page=6) | 6,260/mo | extension | 为使用 DoomPi 组合的 Pi 会话提供领域感知（domain-aware）的 MCP 服务器选择与访问边界。 | `pi install npm:@agimon-ai/doompi-mcp` |

### Agent 编排 / Subagent / Plan / Goal / Task

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 5 | [pi-subagents](https://pi.dev/packages/pi-subagents) | 659,691/mo | extension | 用于单代理委派和脚本化多代理工作流的 Pi 扩展 | `pi install npm:pi-subagents` |
| 16 | [@langchain/langsmith-pi-extension](https://pi.dev/packages/@langchain/langsmith-pi-extension) | 90,563/mo | package | 面向 Pi Coding Agent 的 LangSmith 扩展。 | `pi install npm:@langchain/langsmith-pi-extension` |
| 29 | [pi-goal-x](https://pi.dev/packages/pi-goal-x) | 46,278/mo | extension | pi 的目标模式扩展：持久的长期目标、五个模型工具、结构化任务、独立的完成审计、西西弗斯模式、自动继续和状态浮层。 | `pi install npm:pi-goal-x` |
| 36 | [@tintinweb/pi-subagents](https://pi.dev/packages/@tintinweb/pi-subagents) | 38,168/mo | extension | 一个 pi 扩展，为 pi 带来类 Claude Code 的子代理与工作流编排：并行执行、实时组件、代理集群视图、自定义代理类型、运行中转向、动态工作流、Claude Code 兼容性以及整体外观与体验。 | `pi install npm:@tintinweb/pi-subagents` |
| 44 | [@schovest/pi-goal](https://pi.dev/packages/@schovest/pi-goal) | 32,020/mo | extension | Pi extension for autonomous single-objective /goal completion. | `pi install npm:@schovest/pi-goal` |
| 47 | [pi-intercom](https://pi.dev/packages/pi-intercom) | 31,412/mo | package | <p> <img src="banner.png" alt="pi-intercom" width="1100"> </p> | `pi install npm:pi-intercom` |
| 61 | [@getpipher/vision](https://pi.dev/packages/@getpipher/vision?page=2) | 24,486/mo | extension | Capability-aware vision + paste extension for the pi coding agent. Delegates image analysis to a vision model only when the active primary model is text-only; passes images through natively for multimodal models (zero delegation). | `pi install npm:@getpipher/vision` |
| 65 | [@narumitw/pi-plan-mode](https://pi.dev/packages/@narumitw/pi-plan-mode?page=2) | 22,869/mo | extension | Pi 扩展，新增一个类似 Codex 的只读 /plan 协作模式。 | `pi install npm:@narumitw/pi-plan-mode` |
| 66 | [@narumitw/pi-goal](https://pi.dev/packages/@narumitw/pi-goal?page=2) | 22,749/mo | extension | Pi 扩展，用于通过 /goal 自主完成单一目标。 | `pi install npm:@narumitw/pi-goal` |
| 68 | [@akagilnc/pi-workflow-roles](https://pi.dev/packages/@akagilnc/pi-workflow-roles?page=2) | 22,383/mo | package | 面向 Pi 的灵魂绑定（soul-bound）工作流角色。 | `pi install npm:@akagilnc/pi-workflow-roles` |
| 69 | [agent-simple-english](https://pi.dev/packages/agent-simple-english?page=2) | 22,360/mo | package | Technical and house-style English lint engine, CLI, and host adapters | `pi install npm:agent-simple-english` |
| 78 | [@explyt/ai-agent](https://pi.dev/packages/@explyt/ai-agent?page=2) | 20,251/mo | package | Explyt AI Agent: a terminal AI coding agent | `pi install npm:@explyt/ai-agent` |
| 90 | [@gotgenes/pi-subagents](https://pi.dev/packages/@gotgenes/pi-subagents?page=2) | 16,069/mo | extension | 面向 pi 的专注型进程内子代理核心——提供自主 AI 代理，以及供其他扩展构建的类型化 API 与生命周期事件。是 @tintinweb/pi-subagents 的友好分支（fork）。 | `pi install npm:@gotgenes/pi-subagents` |
| 97 | [@injaneity/pi-computer-use](https://pi.dev/packages/@injaneity/pi-computer-use?page=2) | 14,885/mo | extension | Pi extension that lets AI agents observe and control macOS, Windows, and Linux apps. | `pi install npm:@injaneity/pi-computer-use` |
| 125 | [pi-crew](https://pi.dev/packages/pi-crew?page=3) | 12,147/mo | package | Pi 扩展，用于协调 AI 团队、工作流、工作树以及异步任务编排 | `pi install npm:pi-crew` |
| 132 | [@agimon-ai/po-runner-rtk-linux-x64](https://pi.dev/packages/@agimon-ai/po-runner-rtk-linux-x64?page=3) | 11,923/mo | package | Prebuilt RTK v0.45.0 log processor for Po Runner on Linux x64. | `pi install npm:@agimon-ai/po-runner-rtk-linux-x64` |
| 135 | [@agimon-ai/po-workflow](https://pi.dev/packages/@agimon-ai/po-workflow?page=3) | 11,858/mo | extension | GitHub Actions-style workflow graphs, artifacts, recovery, and asynchronous runs for Po. | `pi install npm:@agimon-ai/po-workflow` |
| 138 | [@piagent/platform](https://pi.dev/packages/@piagent/platform?page=3) | 11,821/mo | extension, skill, prompt | 面向 AI coding agent 的护栏：在工具调用执行前拦截密钥读取、破坏性命令和未经批准的 MCP 服务器。附带项目配置文件、能力锁定、上下文引擎和任务验证。 | `pi install npm:@piagent/platform` |
| 139 | [@awebai/pi](https://pi.dev/packages/@awebai/pi?page=3) | 11,816/mo | extension | Lets your Pi communicate with other AI agents on an open network: send and receive messages, wake up the moment one arrives, and join agent teams. | `pi install npm:@awebai/pi` |
| 146 | [@agimon-ai/po-plan](https://pi.dev/packages/@agimon-ai/po-plan?page=3) | 11,755/mo | extension | Reviewable Pi planning mode that removes file-editing tools and persists implementation plans. | `pi install npm:@agimon-ai/po-plan` |
| 149 | [@agimon-ai/po-team](https://pi.dev/packages/@agimon-ai/po-team?page=3) | 11,726/mo | package | Asynchronous named subagents, team runs, intercom, and model policy for Pi coding agents. | `pi install npm:@agimon-ai/po-team` |
| 161 | [@kontextmind/kxm](https://pi.dev/packages/@kontextmind/kxm?page=4) | 11,608/mo | extension | KXM local-first multi-agent orchestration and operator dashboard | `pi install npm:@kontextmind/kxm` |
| 163 | [@agimon-ai/po-runner-rtk-linux-arm64](https://pi.dev/packages/@agimon-ai/po-runner-rtk-linux-arm64?page=4) | 11,427/mo | package | Prebuilt RTK v0.45.0 log processor for Po Runner on Linux arm64. | `pi install npm:@agimon-ai/po-runner-rtk-linux-arm64` |
| 164 | [@agimon-ai/po-runner-rtk-darwin-arm64](https://pi.dev/packages/@agimon-ai/po-runner-rtk-darwin-arm64?page=4) | 11,357/mo | package | Prebuilt RTK v0.45.0 log processor for Po Runner on macOS arm64. | `pi install npm:@agimon-ai/po-runner-rtk-darwin-arm64` |
| 167 | [@agimon-ai/po-runner-rtk-darwin-x64](https://pi.dev/packages/@agimon-ai/po-runner-rtk-darwin-x64?page=4) | 11,129/mo | package | Prebuilt RTK v0.45.0 log processor for Po Runner on macOS x64. | `pi install npm:@agimon-ai/po-runner-rtk-darwin-x64` |
| 170 | [pi-rtk-optimizer](https://pi.dev/packages/pi-rtk-optimizer?page=4) | 11,022/mo | extension | Pi 扩展，为编码代理优化 RTK 命令重写与工具输出压缩。 | `pi install npm:pi-rtk-optimizer` |
| 177 | [@cgh567/agent](https://pi.dev/packages/@cgh567/agent?page=4) | 10,516/mo | package | Helios 自我改进实验室。 | `pi install npm:@cgh567/agent` |
| 190 | [@henryqw/pi-subagent](https://pi.dev/packages/@henryqw/pi-subagent?page=4) | 9,785/mo | package | 将受限的单个、并行或链式任务委派给隔离的 Pi 角色。 | `pi install npm:@henryqw/pi-subagent` |
| 199 | [pi-subagent-manager](https://pi.dev/packages/pi-subagent-manager?page=4) | 9,289/mo | package | Hierarchical, steerable subagent threads for pi | `pi install npm:pi-subagent-manager` |
| 210 | [@a-t-h-i/bot-lobby](https://pi.dev/packages/@a-t-h-i/bot-lobby?page=5) | 8,342/mo | extension | Structured multi-agent software engineering orchestrator for Pi | `pi install npm:@a-t-h-i/bot-lobby` |
| 227 | [atlas-project-harness](https://pi.dev/packages/atlas-project-harness?page=5) | 7,440/mo | extension | 践行 Project Harness 的全流程 AI 编程工作流治理引擎 | `pi install npm:atlas-project-harness` |
| 228 | [pi-note](https://pi.dev/packages/pi-note?page=5) | 7,438/mo | package | Persistent pinote tasks, Markdown handoffs, and task status for Pi | `pi install npm:pi-note` |
| 229 | [pi-durable-subagents](https://pi.dev/packages/pi-durable-subagents?page=5) | 7,421/mo | package | Subagents for pi that never lose work and never do it twice. Crash-safe workflows, automatic recovery, and a live view just like the main agent. | `pi install npm:pi-durable-subagents` |
| 236 | [@henryqw/pi-task-models](https://pi.dev/packages/@henryqw/pi-task-models?page=5) | 7,047/mo | package | 面向 HenryQW Pi 扩展的共享任务模型配置与路由。 | `pi install npm:@henryqw/pi-task-models` |
| 245 | [pi-extensible-workflows](https://pi.dev/packages/pi-extensible-workflows?page=5) | 6,752/mo | package | Deterministic multi-agent workflow orchestration and codemode scripts for Pi | `pi install npm:pi-extensible-workflows` |
| 246 | [runline](https://pi.dev/packages/runline?page=5) | 6,731/mo | package | 面向 AI 代理的代码模式 —— 将任意 API 或命令变成可调用的操作 | `pi install npm:runline` |
| 249 | [pi-landstrip](https://pi.dev/packages/pi-landstrip?page=5) | 6,654/mo | extension | 面向 Pi 的沙箱化 Bash 与基于进程的 AI 代理。 | `pi install npm:pi-landstrip` |
| 265 | [pi-owed](https://pi.dev/packages/pi-owed?page=6) | 6,274/mo | package | owed — the acceptance ledger for multi-agent task graphs. No receipt, not done. | `pi install npm:pi-owed` |
| 267 | [@pi-unipi/unipi](https://pi.dev/packages/@pi-unipi/unipi?page=6) | 6,254/mo | extension | 面向 Pi 编码代理的一体化扩展套件。 | `pi install npm:@pi-unipi/unipi` |
| 274 | [@agimon-ai/doompi-team](https://pi.dev/packages/@agimon-ai/doompi-team?page=6) | 6,111/mo | package | 为 Pi 编码代理提供异步具名子代理、团队运行、对讲（intercom）与模型策略。 | `pi install npm:@agimon-ai/doompi-team` |
| 280 | [@agimon-ai/doompi-workflow](https://pi.dev/packages/@agimon-ai/doompi-workflow?page=6) | 6,001/mo | extension | 为 DoomPi 提供 GitHub Actions 风格的工作流图、产物（artifacts）、恢复与异步运行。 | `pi install npm:@agimon-ai/doompi-workflow` |
| 287 | [@agimon-ai/doompi-plan](https://pi.dev/packages/@agimon-ai/doompi-plan?page=6) | 5,892/mo | extension | 可审核的 Pi 规划模式：移除文件编辑工具并持久化实现计划。 | `pi install npm:@agimon-ai/doompi-plan` |
| 290 | [@esso0428/pi-subagents](https://pi.dev/packages/@esso0428/pi-subagents?page=6) | 5,861/mo | extension | A pi extension that brings smart Claude Code-style autonomous sub-agents to pi, with npm:pi-subagents-style JSON agent overrides. | `pi install npm:@esso0428/pi-subagents` |
| 294 | [@agntn/hashes](https://pi.dev/packages/@agntn/hashes?page=6) | 5,825/mo | package | Hash, HMAC and key derivation algorithms for agents | `pi install npm:@agntn/hashes` |

### Context / Memory / Knowledge / Compaction

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 1 | [billion-context](https://pi.dev/packages/billion-context) | 2,353,370/mo | package | A context-compression plugin — small context windows (a 100K context is enough), 5x fewer tokens, month-long single sessions (billions of tokens), and compression quality — for all agents: pi, OpenCode, Codex, Claude Code, and more. billion-context is all | `pi install npm:billion-context` |
| 2 | [pi-mcp-adapter](https://pi.dev/packages/pi-mcp-adapter) | 1,500,675/mo | extension | 面向 Pi 编码代理的 MCP（Model Context Protocol）适配器扩展 | `pi install npm:pi-mcp-adapter` |
| 8 | [openwiki](https://pi.dev/packages/openwiki) | 191,287/mo | package | A CLI that uses a DeepAgents documentation agent to generate and maintain an OpenWiki for a codebase. | `pi install npm:openwiki` |
| 13 | [context-mode](https://pi.dev/packages/context-mode) | 92,636/mo | package | 可节省 98% 上下文窗口的 MCP 插件。兼容 Claude Code、Gemini CLI、VS Code Copilot、OpenCode 与 Codex CLI。提供沙箱代码执行、FTS5 知识库和意图驱动搜索。 | `pi install npm:context-mode` |
| 19 | [pi-web-search](https://pi.dev/packages/pi-web-search) | 72,761/mo | extension | 面向 pi 的模型提供方原生网络搜索，覆盖 Google Gemini、OpenAI 和 Anthropic，并支持 Gemini URL Context。 | `pi install npm:pi-web-search` |
| 24 | [pi-memory](https://pi.dev/packages/pi-memory) | 57,043/mo | package | Pi 编码代理的记忆扩展，使用 qmd 驱动的语义搜索，跨日常日志、长期记忆和临时便笺检索。 | `pi install npm:pi-memory` |
| 27 | [@opengsd/gsd-core](https://pi.dev/packages/@opengsd/gsd-core) | 49,285/mo | package | GSD Core is a meta-prompting, context engineering, and spec-driven development system for AI coding agents. | `pi install npm:@opengsd/gsd-core` |
| 58 | [pi-hermes-memory](https://pi.dev/packages/pi-hermes-memory?page=2) | 25,511/mo | extension, skill | 🧠 为 Pi 提供持久记忆 + 🔍 会话搜索 + 🛡️ 密钥扫描。默认采用感知 token 的纯策略记忆，支持 SQLite FTS5 搜索、自动整合与程序化技能。732 个测试，移植自 Hermes 代理。 | `pi install npm:pi-hermes-memory` |
| 74 | [gentle-engram](https://pi.dev/packages/gentle-engram?page=2) | 21,107/mo | extension | Pi 代理的持久记忆——一个可本地或云端部署的大脑，跨会话、压缩和 MCP 代理共享。 | `pi install npm:gentle-engram` |
| 84 | [billion-context-pi](https://pi.dev/packages/billion-context-pi?page=2) | 17,649/mo | package | 十亿，而非一百万。面向 Pi 编码代理的模型驱动上下文管理。 | `pi install npm:billion-context-pi` |
| 102 | [@agentskit/doc-bridge](https://pi.dev/packages/@agentskit/doc-bridge?page=3) | 13,860/mo | package | 连接人类与 AI 代理的文档桥梁——确定性交接、文档站链接、记忆→文档，以及可选的 AgentsKit RAG/聊天。 | `pi install npm:@agentskit/doc-bridge` |
| 104 | [@maxiaochao/pi-toolkit](https://pi.dev/packages/@maxiaochao/pi-toolkit?page=3) | 13,659/mo | extension | Personal pi coding agent toolkit: background tasks, scheduler, /btw, /cache_export, apply_patch, browser automation, and bundled theme/skills. | `pi install npm:@maxiaochao/pi-toolkit` |
| 108 | [om-memory-system](https://pi.dev/packages/om-memory-system?page=3) | 13,453/mo | package | Opinionated modular memory system for coding agents (OpenCode + Pi) | `pi install npm:om-memory-system` |
| 110 | [@agimon-ai/po-cache](https://pi.dev/packages/@agimon-ai/po-cache?page=3) | 13,349/mo | extension | Provider prompt cache policy and deterministic routing for Po | `pi install npm:@agimon-ai/po-cache` |
| 124 | [@d3ara1n/pi-context-include](https://pi.dev/packages/@d3ara1n/pi-context-include?page=3) | 12,156/mo | extension | 为 AGENTS.md 提供 @path 语法——通过引用包含文件，并支持递归解析。 | `pi install npm:@d3ara1n/pi-context-include` |
| 126 | [pi-context-view](https://pi.dev/packages/pi-context-view?page=3) | 12,083/mo | extension | Pi 扩展，用于可视化上下文使用情况并查看隐藏部分：基础提示词、工具定义和扩展注入。 | `pi install npm:pi-context-view` |
| 130 | [@chankov/agent-fleet](https://pi.dev/packages/@chankov/agent-fleet?page=3) | 11,950/mo | extension, skill, prompt | Subagent orchestration for the pi coding agent — a thin dispatcher runs parallel subagents under a verification contract, keeping their output out of its context window. Multi-agent fleets, 15 personas, skills, herdr panes, peer coms, Hermes desktop. | `pi install npm:@chankov/agent-fleet` |
| 174 | [@awebai/oats-pi](https://pi.dev/packages/@awebai/oats-pi?page=4) | 10,781/mo | package | OATS pi runtime bridge — memory session events and pre-workspace bootstrap over the runtime-neutral @awebai/oats kernel | `pi install npm:@awebai/oats-pi` |
| 180 | [pi-blackhole](https://pi.dev/packages/pi-blackhole?page=4) | 10,344/mo | extension | Pi 的统一压缩 + 观察记忆扩展——压缩对话上下文，同时保留持久的观察与反思记录。 | `pi install npm:pi-blackhole` |
| 181 | [@remnic/plugin-pi](https://pi.dev/packages/@remnic/plugin-pi?page=4) | 10,327/mo | package | 面向 Pi 编码代理的 Remnic 记忆扩展。 | `pi install npm:@remnic/plugin-pi` |
| 187 | [@gyoungwe/pi-core](https://pi.dev/packages/@gyoungwe/pi-core?page=4) | 9,898/mo | package | Portable task, authorization, status, delivery and memory tools for native Pi | `pi install npm:@gyoungwe/pi-core` |
| 188 | [pi-open-tui](https://pi.dev/packages/pi-open-tui?page=4) | 9,813/mo | extension, theme | 面向 Pi 编码代理的精美 TUI：动态 logo 头部、Starship 风格底部栏、带模型元数据的圆角编辑器，以及提示框形式的用户消息。 | `pi install npm:pi-open-tui` |
| 191 | [pi-quiver](https://pi.dev/packages/pi-quiver?page=4) | 9,752/mo | package | Personal pack of Pi coding-agent extensions: context-safe fetch, doc_to_md PDF/DOCX/PPTX-to-Markdown conversion, session naming, a themed ASCII startup header, Opus 4.8 fast mode, and a provider-stall watchdog. | `pi install npm:pi-quiver` |
| 195 | [@gyoungwe/pi-knowledge](https://pi.dev/packages/@gyoungwe/pi-knowledge?page=4) | 9,500/mo | package | Knowledge and Vault tools for native Pi hosts | `pi install npm:@gyoungwe/pi-knowledge` |
| 202 | [pi-deferred-context-engine](https://pi.dev/packages/pi-deferred-context-engine?page=5) | 9,147/mo | extension, skill | Run-scoped deferred tools, skills, blocked deny-list, and duplicate prompt context for Pi/OMP. | `pi install npm:pi-deferred-context-engine` |
| 207 | [pi-code](https://pi.dev/packages/pi-code?page=5) | 8,638/mo | extension, skill | 为 pi 编码代理带来 Claude Code 体验：读取你的 .claude 配置（规则、命令、技能包、钩子、输出样式、MCP 服务器、代理），并新增 todo、检查点、记忆、网页和子代理功能。 | `pi install npm:pi-code` |
| 216 | [@herbertgao/pi-cc-extensions](https://pi.dev/packages/@herbertgao/pi-cc-extensions?page=5) | 8,009/mo | extension | A Pi productivity suite with Claude Code-style UI, context inspection, and agent/session references | `pi install npm:@herbertgao/pi-cc-extensions` |
| 239 | [pi-smart-compact](https://pi.dev/packages/pi-smart-compact?page=5) | 6,993/mo | extension | 面向 Pi Coding Agent、以验证为导向的智能压缩扩展——支持确定性提取、探索、综合、验证、指标统计与安全检查。 | `pi install npm:pi-smart-compact` |
| 248 | [pi-maestro-flow](https://pi.dev/packages/pi-maestro-flow?page=5) | 6,676/mo | skill | 面向 Pi 编码代理的一体化多代理编排 —— 单次安装即可获得并行队友调度、目标、计划、知识系统、MCP/LSP/浏览器与驾驶舱可视化 | `pi install npm:pi-maestro-flow` |
| 251 | [pi-subdir-context](https://pi.dev/packages/pi-subdir-context?page=6) | 6,607/mo | extension | Automatically load AGENTS.md context from subdirectories in pi coding agent | `pi install npm:pi-subdir-context` |
| 253 | [@agimon-ai/doompi-cache](https://pi.dev/packages/@agimon-ai/doompi-cache?page=6) | 6,557/mo | extension | Provider prompt cache policy and deterministic routing for DoomPi | `pi install npm:@agimon-ai/doompi-cache` |
| 270 | [openlore](https://pi.dev/packages/openlore?page=6) | 6,191/mo | package | 面向 AI 编码代理的持久化架构记忆与结构化认知。 | `pi install npm:openlore` |
| 271 | [@pi-unipi/info-screen](https://pi.dev/packages/@pi-unipi/info-screen?page=6) | 6,185/mo | extension | Unicrab startup splash and the /unipi:info dashboard — this session, context, usage, compaction savings | `pi install npm:@pi-unipi/info-screen` |
| 275 | [pi-cache-optimizer](https://pi.dev/packages/pi-cache-optimizer?page=6) | 6,108/mo | package | 通过稳定的提示词、兼容 OpenAI 的缓存键、代理兼容性警告和底部缓存统计，提升 Pi 的提示词/KV 缓存命中率。 | `pi install npm:pi-cache-optimizer` |
| 282 | [@spences10/pi-redact](https://pi.dev/packages/@spences10/pi-redact?page=6) | 5,983/mo | package | Tool-output redaction for Pi that replaces likely secrets before they reach the model context | `pi install npm:@spences10/pi-redact` |
| 284 | [@pi-unipi/utility](https://pi.dev/packages/@pi-unipi/utility?page=6) | 5,980/mo | extension | Utility commands and tools for Pi coding agent — lifecycle, diagnostics, cache, analytics, display, batch execution | `pi install npm:@pi-unipi/utility` |
| 288 | [pi-lore](https://pi.dev/packages/pi-lore?page=6) | 5,888/mo | package | `pi-lore` gives Pi agents GHC-aware tools for Haskell codebases. In large projects, ordinary code discovery often means reading whole files, chasing imports by hand, and filling the model context with definitions that are unrelated or already known. Lore | `pi install npm:pi-lore` |
| 295 | [@agimon-ai/doompi-autocompact](https://pi.dev/packages/@agimon-ai/doompi-autocompact?page=6) | 5,818/mo | extension | 为 Pi 与 DoomPi 代理会话提供迭代式上下文压缩与检查点摘要。 | `pi install npm:@agimon-ai/doompi-autocompact` |
| 299 | [@bunshin-cc/bunshin](https://pi.dev/packages/@bunshin-cc/bunshin?page=6) | 5,784/mo | package | Shared memory for company AI agents. Connect Codex, Claude Code, or Pi to Bunshin. | `pi install npm:@bunshin-cc/bunshin` |

### 模型 / Provider / 路由 / 用量

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 6 | [@postman/postman-plugin](https://pi.dev/packages/@postman/postman-plugin) | 278,885/mo | package | Postman's API engineering skills for coding agents: a Pi package, and an npx installer that sets up Claude Code, Codex, Cursor, Kimi Code, Factory Droid, OpenCode and Pi. | `pi install npm:@postman/postman-plugin` |
| 18 | [pi-harness-runtime](https://pi.dev/packages/pi-harness-runtime) | 77,128/mo | extension | [BETA] 面向 pi 的 Codex 风格 /usage 状态与自主编码 harness。尚未达到生产就绪——预计会有破坏性变更。 | `pi install npm:pi-harness-runtime` |
| 20 | [pi-claude-bridge](https://pi.dev/packages/pi-claude-bridge) | 71,900/mo | extension | Pi 扩展，将 Claude Code（通过 Agent SDK）用作模型提供方，并新增 AskClaude 工具。 | `pi install npm:pi-claude-bridge` |
| 30 | [@narumitw/pi-usage](https://pi.dev/packages/@narumitw/pi-usage) | 45,576/mo | extension | Pi 扩展，可显示受支持模型提供方的当前账户用量和 DeepSeek API 余额。 | `pi install npm:@narumitw/pi-usage` |
| 37 | [@braintrust/pi-extension](https://pi.dev/packages/@braintrust/pi-extension) | 35,387/mo | package | 面向 pi 的 Braintrust 扩展，可自动将 pi 会话、轮次、LLM 调用和工具执行追踪到 Braintrust。 | `pi install npm:@braintrust/pi-extension` |
| 53 | [@gotgenes/pi-anthropic-auth](https://pi.dev/packages/@gotgenes/pi-anthropic-auth?page=2) | 27,880/mo | package | 用于 Anthropic OAuth 兼容性的 Pi 扩展包 | `pi install npm:@gotgenes/pi-anthropic-auth` |
| 54 | [pi-fireworks](https://pi.dev/packages/pi-fireworks?page=2) | 27,308/mo | extension | Fireworks AI provider extension package for pi | `pi install npm:pi-fireworks` |
| 62 | [pi-fireworks-quota](https://pi.dev/packages/pi-fireworks-quota?page=2) | 23,926/mo | extension | Pi commands /fireworks:quota and /fireworks:test-key — Fireworks AI balance, spend, tokens, and limits | `pi install npm:pi-fireworks-quota` |
| 63 | [pi-provider-litellm](https://pi.dev/packages/pi-provider-litellm?page=2) | 23,655/mo | extension | 面向 Pi 的 LiteLLM 代理模型提供方扩展。 | `pi install npm:pi-provider-litellm` |
| 67 | [pi-coralbricks-provider](https://pi.dev/packages/pi-coralbricks-provider?page=2) | 22,572/mo | extension | CoralBricks provider extension for pi - Access DeepSeek V4.1 Flash through the Coral Inference API | `pi install npm:pi-coralbricks-provider` |
| 77 | [agent-comms](https://pi.dev/packages/agent-comms?page=2) | 20,693/mo | package | Cross-harness communication mesh for LLM agents — rooms, DMs, presence, and real-time push delivery over TCP | `pi install npm:agent-comms` |
| 89 | [@sting8k/pi-vcc](https://pi.dev/packages/@sting8k/pi-vcc?page=2) | 16,135/mo | extension | Algorithmic conversation compactor for pi - transcript-preserving structured summaries, no LLM calls | `pi install npm:@sting8k/pi-vcc` |
| 92 | [pi-antigravity](https://pi.dev/packages/pi-antigravity?page=2) | 15,867/mo | extension | 面向 Pi Coding Agent 的个人 Antigravity / Cloud Code Assist 模型提供方。 | `pi install npm:pi-antigravity` |
| 96 | [pi-otel](https://pi.dev/packages/pi-otel?page=2) | 14,997/mo | extension | OpenTelemetry traces for pi-coding-agent — per-prompt span tree (interaction → llm_request, tool.<name>) exported via OTLP. Aspire-dashboard ready. | `pi install npm:pi-otel` |
| 114 | [pi-zhipu-usage](https://pi.dev/packages/pi-zhipu-usage?page=3) | 12,868/mo | package | Pi extension: show GLM Coding Plan usage and reset countdown in the footer. Supports Zhipu domestic (open.bigmodel.cn), international (api.z.ai), local proxy / Headroom setups, and @zigai/pi-footer slot integration. | `pi install npm:pi-zhipu-usage` |
| 123 | [superpowers-zh](https://pi.dev/packages/superpowers-zh?page=3) | 12,162/mo | skill | AI 编程超能力中文增强版 — superpowers（250k+ ⭐）完整汉化 + 4 个中国原创技能包，支持 Claude Code / Copilot CLI / Hermes Agent / Cursor / Claw Code / Windsurf / Kiro / Gemini CLI / Qoder 等 23 款工具 | `pi install npm:superpowers-zh` |
| 157 | [@agimon-ai/po-goal](https://pi.dev/packages/@agimon-ai/po-goal?page=4) | 11,655/mo | extension | Pi minor mode for persistent agent goals, token budgets, and goal history. | `pi install npm:@agimon-ai/po-goal` |
| 175 | [@amaster.ai/pi-image-gen](https://pi.dev/packages/@amaster.ai/pi-image-gen?page=4) | 10,692/mo | extension | Pi 图片生成扩展，支持通过 OpenAI gpt-image、Google Nano Banana（Gemini）、阿里 Qwen-Image、OpenRouter 及自定义模型提供方生成图片。 | `pi install npm:@amaster.ai/pi-image-gen` |
| 184 | [pi-cursor-sdk](https://pi.dev/packages/pi-cursor-sdk?page=4) | 10,196/mo | extension | 由 @cursor/sdk 本地及云端 AI 代理支撑的 pi 模型提供方扩展 | `pi install npm:pi-cursor-sdk` |
| 186 | [pi-dashscope](https://pi.dev/packages/pi-dashscope?page=4) | 10,094/mo | package | Alibaba DashScope (ModelStudio) provider for oh my pi — Qwen3, GLM-5, MiniMax M2.5, Kimi K2.5 via OpenAI-compatible coding API | `pi install npm:pi-dashscope` |
| 201 | [@tmustier/pi-usage-extension](https://pi.dev/packages/@tmustier/pi-usage-extension?page=5) | 9,163/mo | package | Pi 会话的用量统计仪表盘。 | `pi install npm:@tmustier/pi-usage-extension` |
| 208 | [pi-commandcode-provider](https://pi.dev/packages/pi-commandcode-provider?page=5) | 8,523/mo | extension | pi custom provider for Command Code API (commandcode.ai) | `pi install npm:pi-commandcode-provider` |
| 209 | [pi-extension-nvidia-nim](https://pi.dev/packages/pi-extension-nvidia-nim?page=5) | 8,396/mo | package | 为 pi coding agent 提供模型感知的 NVIDIA NIM 推理兼容性 | `pi install npm:pi-extension-nvidia-nim` |
| 213 | [pi-llama-cpp](https://pi.dev/packages/pi-llama-cpp?page=5) | 8,141/mo | extension | 用于集成 llama.cpp 的 Pi 扩展。支持 router、单模型与旧版（legacy）模型，并支持多个服务器。 | `pi install npm:pi-llama-cpp` |
| 214 | [@cortexkit/pi-openai-auth](https://pi.dev/packages/@cortexkit/pi-openai-auth?page=5) | 8,124/mo | package | 为 CortexKit 提供 OpenAI Codex OAuth 支持的 Pi 包。它用基于 Pi 的 OpenAI Codex Responses 传输层和 OAuth 原语的 CortexKit 模型提供方扩展，覆盖 Pi 内置的 `openai-codex` 模型提供方。 | `pi install npm:@cortexkit/pi-openai-auth` |
| 220 | [pi-cliproxyapi-provider](https://pi.dev/packages/pi-cliproxyapi-provider?page=5) | 7,642/mo | extension | 面向 CLIProxyAPI 的 Pi 模型提供方包，支持自动发现模型并利用 models.dev 补充模型信息。 | `pi install npm:pi-cliproxyapi-provider` |
| 221 | [pi-token-speed](https://pi.dev/packages/pi-token-speed?page=5) | 7,640/mo | extension | Pi 扩展，通过滑动窗口测量每秒 token 数（tokens per second）。 | `pi install npm:pi-token-speed` |
| 222 | [pi-caveman](https://pi.dev/packages/pi-caveman?page=5) | 7,555/mo | extension | 既然少量 token 就能奏效，何必使用大量 token。pi 的穴居人模式 —— 在保持完整技术准确性的同时减少约 75% 的输出 token。 | `pi install npm:pi-caveman` |
| 226 | [pi-multi-account](https://pi.dev/packages/pi-multi-account?page=5) | 7,441/mo | extension | Automatic multi-account failover & rotation for Pi Agent across Anthropic (Claude), native OpenAI ChatGPT and legacy Codex, Kimi For Coding, Cursor, Qwen/Alibaba, and Ollama. Auto-discovers authenticated accounts, grows the rotation on login, and drops ac | `pi install npm:pi-multi-account` |
| 234 | [pi-freeflow](https://pi.dev/packages/pi-freeflow?page=5) | 7,195/mo | extension | 面向 OMP/Pi 的轻量级模型提供方 —— 模型列表 + 简易中继代理 + 日志；思考（thinking）与规范化（normalization）由宿主 pi-ai 负责。 | `pi install npm:pi-freeflow` |
| 241 | [pi-ollama-cloud](https://pi.dev/packages/pi-ollama-cloud?page=5) | 6,919/mo | package | 面向 [Pi](https://pi.dev) 编码代理的 Ollama Cloud 模型提供方插件。 | `pi install npm:pi-ollama-cloud` |
| 243 | [pi-qwen_dashscope](https://pi.dev/packages/pi-qwen_dashscope?page=5) | 6,870/mo | package | Alibaba DashScope (ModelStudio / 百炼) provider for oh my pi — Qwen3, GLM-5, Kimi K2.5, MiniMax via OpenAI-compatible API, with dynamic full-catalog model discovery | `pi install npm:pi-qwen_dashscope` |
| 244 | [thoth-agents](https://pi.dev/packages/thoth-agents?page=5) | 6,812/mo | package | Adaptive multi-harness orchestration with six roles, runtime-autonomous AI-first execution routes, and external provider boundaries. | `pi install npm:thoth-agents` |
| 256 | [pi-alibaba-models](https://pi.dev/packages/pi-alibaba-models?page=6) | 6,427/mo | package | The complete Alibaba provider for pi — Plan subscription + Cloud pay-per-token, International + China endpoints, Anthropic + OpenAI shapes, native thinking levels. Qwen 3.8 Max, Qwen 3.7/3.6, DeepSeek V4 Pro, Kimi K3, GLM-5, MiniMax M3. | `pi install npm:pi-alibaba-models` |
| 268 | [pi-dashscope-native](https://pi.dev/packages/pi-dashscope-native?page=6) | 6,220/mo | extension | Native Alibaba Cloud DashScope Qwen provider for Pi | `pi install npm:pi-dashscope-native` |
| 278 | [pi-router](https://pi.dev/packages/pi-router?page=6) | 6,043/mo | extension | Intelligent routing layer for pi coding agent with multi-level failover, circuit breaker, and comprehensive observability | `pi install npm:pi-router` |

### Skills / Prompt / Rules / 提问

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 9 | [@juicesharp/rpiv-ask-user-question](https://pi.dev/packages/@juicesharp/rpiv-ask-user-question) | 181,064/mo | extension | Pi 扩展：当模型只能靠猜测时，它可以向你提出一份结构化问卷，用带类型的选项代替自由文本回答。 | `pi install npm:@juicesharp/rpiv-ask-user-question` |
| 10 | [@dietrichgebert/ponytail](https://pi.dev/packages/@dietrichgebert/ponytail) | 117,660/mo | skill | 面向 AI 代理的『懒人资深开发』模式。最好的代码就是你从未写过的代码。 | `pi install npm:@dietrichgebert/ponytail` |
| 21 | [pi-advisor-flow](https://pi.dev/packages/pi-advisor-flow) | 67,830/mo | extension | Advanced Executor/Advisor flow for Pi, fully configurable and extendable. | `pi install npm:pi-advisor-flow` |
| 28 | [@juicesharp/rpiv-i18n](https://pi.dev/packages/@juicesharp/rpiv-i18n) | 46,474/mo | extension | Pi 扩展。rpiv-* 技能包的本地化基础：区域设置检测、/languages 命令、--locale 标志以及跨包的区域设置注册表。 | `pi install npm:@juicesharp/rpiv-i18n` |
| 49 | [@nitra/cursor](https://pi.dev/packages/@nitra/cursor) | 29,488/mo | package | 用于将 cursor 规则（前缀 n-）下载到本地仓库的 CLI。（下载 cursor 规则到本地仓库的 CLI 工具） | `pi install npm:@nitra/cursor` |
| 52 | [bigpowers](https://pi.dev/packages/bigpowers?page=2) | 28,071/mo | skill | 73 个代理技能，将 17 年的软件工程纪律凝练为一套面向独立开发者的规范性方法论。 | `pi install npm:bigpowers` |
| 57 | [@mutmutco/pi-plugin](https://pi.dev/packages/@mutmutco/pi-plugin?page=2) | 25,563/mo | package | 提供 MMI 工作流技能包与 org 门控交付。 | `pi install npm:@mutmutco/pi-plugin` |
| 60 | [pi-prompt-template-model](https://pi.dev/packages/pi-prompt-template-model?page=2) | 25,105/mo | extension, prompt | 面向 pi 编码代理的提示词模板模型选择扩展。 | `pi install npm:pi-prompt-template-model` |
| 64 | [@howaboua/pi-codex-conversion](https://pi.dev/packages/@howaboua/pi-codex-conversion?page=2) | 22,917/mo | extension | 面向 pi 编码代理的 Codex 导向工具与提示词适配器。 | `pi install npm:@howaboua/pi-codex-conversion` |
| 72 | [pi-interview](https://pi.dev/packages/pi-interview?page=2) | 21,625/mo | extension | 面向 pi 编码代理的交互式访谈表单扩展。 | `pi install npm:pi-interview` |
| 82 | [@juicesharp/rpiv-advisor](https://pi.dev/packages/@juicesharp/rpiv-advisor?page=2) | 18,642/mo | extension | Pi 扩展。模型在行动之前，可以向更强的评审模型征求第二意见。 | `pi install npm:@juicesharp/rpiv-advisor` |
| 95 | [projectops](https://pi.dev/packages/projectops?page=2) | 15,034/mo | package | ProjectOps: installer CLI for a fully automated GitHub project management template (versioning, CI/CD, release notes, agent skills) | `pi install npm:projectops` |
| 99 | [@narumitw/pi-btw](https://pi.dev/packages/@narumitw/pi-btw?page=2) | 14,241/mo | extension | Pi 扩展，新增一个 /btw 顺带提问命令。 | `pi install npm:@narumitw/pi-btw` |
| 103 | [pi-gauntlet](https://pi.dev/packages/pi-gauntlet?page=3) | 13,790/mo | skill | 为 pi 编码代理提供有主张、带门控的工作流技能包、子代理人设和运行时扩展。 | `pi install npm:pi-gauntlet` |
| 153 | [@agimon-ai/po-prompt](https://pi.dev/packages/@agimon-ai/po-prompt?page=4) | 11,700/mo | extension | Staged recent prompts and saved prompt templates for Po | `pi install npm:@agimon-ai/po-prompt` |
| 154 | [@agimon-ai/po-help](https://pi.dev/packages/@agimon-ai/po-help?page=4) | 11,698/mo | extension, skill | Activation-gated package guidance and help skills for Po and Pi extensions. | `pi install npm:@agimon-ai/po-help` |
| 160 | [@agimon-ai/po-model-guidance](https://pi.dev/packages/@agimon-ai/po-model-guidance?page=4) | 11,643/mo | extension | Per-model system prompt guidance for Pi agents, layered across global and repository scope. | `pi install npm:@agimon-ai/po-model-guidance` |
| 225 | [opencode-agent-skill](https://pi.dev/packages/opencode-agent-skill?page=5) | 7,472/mo | package | Pi-native UES coding-agent runtime with V16 deterministic correctness gates, durable evidence integrity, external-data provenance, Windows-safe cleanup, and measured cost-aware routing | `pi install npm:opencode-agent-skill` |
| 237 | [bestony-pi-preset](https://pi.dev/packages/bestony-pi-preset?page=5) | 7,001/mo | extension, skill, theme, prompt | Bestony 的个人 Pi 编码代理预设——包含技能包、扩展、提示词和主题。 | `pi install npm:bestony-pi-preset` |
| 238 | [@juicesharp/rpiv-args](https://pi.dev/packages/@juicesharp/rpiv-args?page=5) | 6,996/mo | extension, skill, prompt | Pi 扩展。支持 Shell 风格的 $1 / $ARGUMENTS 占位符与 !`cmd` / ```! shell 替换，并在调用时展开到你的 Pi 技能包中。 | `pi install npm:@juicesharp/rpiv-args` |
| 250 | [@llblab/pi-kit](https://pi.dev/packages/@llblab/pi-kit?page=5) | 6,652/mo | extension | Version-pinned distribution of LLB Lab extensions and Skills for Pi | `pi install npm:@llblab/pi-kit` |
| 259 | [@ludi-uni/ludi-agent-kit](https://pi.dev/packages/@ludi-uni/ludi-agent-kit?page=6) | 6,416/mo | package | Windows-first, backend-neutral agent kit with Pi skills and extensions | `pi install npm:@ludi-uni/ludi-agent-kit` |
| 269 | [pi-lingual](https://pi.dev/packages/pi-lingual?page=6) | 6,193/mo | extension | Bilingual developer companion & declarative Prompt Optimizer for Pi — Mode as Configuration, Dual-Core Golden Defaults, Zero-Residue First-Run Handshake, and S-Tier Prompt Architect. | `pi install npm:pi-lingual` |

### Runtime / 后台任务 / Worktree / 集成

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 31 | [pi-background-tasks](https://pi.dev/packages/pi-background-tasks) | 43,036/mo | extension | Pi 扩展：支持持久的后台 shell 任务、只读委托代理、本地认证的 Pi 运行，以及通过子 Pi 进程运行的固定用途 Fusion 工作流。 | `pi install npm:pi-background-tasks` |
| 32 | [confluence-cli](https://pi.dev/packages/confluence-cli) | 41,815/mo | package | 面向 Atlassian Confluence 的命令行界面，具备页面创建与编辑能力。 | `pi install npm:confluence-cli` |
| 40 | [pi-fabric](https://pi.dev/packages/pi-fabric) | 33,358/mo | extension | 面向 Pi 的可编程工具与代理运行时。 | `pi install npm:pi-fabric` |
| 45 | [@agimon-ai/po-core](https://pi.dev/packages/@agimon-ai/po-core) | 31,999/mo | package | Po runtime systems and reusable core services. | `pi install npm:@agimon-ai/po-core` |
| 80 | [@undefineds.co/models](https://pi.dev/packages/@undefineds.co/models?page=2) | 20,105/mo | package | `@undefineds.co/models` 是面向 LinX 应用、桌面端、CLI、边车组件及未来 worker 的共享 Solid Pod 数据模型契约。 | `pi install npm:@undefineds.co/models` |
| 94 | [@llblab/pi-telegram](https://pi.dev/packages/@llblab/pi-telegram?page=2) | 15,041/mo | extension | 面向 Pi 的 Telegram 运行时适配器。 | `pi install npm:@llblab/pi-telegram` |
| 101 | [@agimon-ai/doompi-core](https://pi.dev/packages/@agimon-ai/doompi-core?page=3) | 13,964/mo | package | Doompi runtime systems and reusable core services. | `pi install npm:@agimon-ai/doompi-core` |
| 107 | [@pi-unipi/core](https://pi.dev/packages/@pi-unipi/core?page=3) | 13,496/mo | extension | 面向 Unipi 扩展套件的共享工具、事件类型和常量 | `pi install npm:@pi-unipi/core` |
| 134 | [@agimon-ai/po-runner-rmux-linux-x64](https://pi.dev/packages/@agimon-ai/po-runner-rmux-linux-x64?page=3) | 11,864/mo | package | Prebuilt RMUX runtime for Po Runner on Linux x64. | `pi install npm:@agimon-ai/po-runner-rmux-linux-x64` |
| 148 | [@agimon-ai/po-runner](https://pi.dev/packages/@agimon-ai/po-runner?page=3) | 11,730/mo | package | Supervised shell execution, background process control, and run logs for Pi coding agents. | `pi install npm:@agimon-ai/po-runner` |
| 156 | [pi-until-loop](https://pi.dev/packages/pi-until-loop?page=4) | 11,657/mo | package | Spend your time on the engineering trade-offs that matter. Let the Until Loop make sure your agents deliver what you want, how you want it. | `pi install npm:pi-until-loop` |
| 165 | [@agimon-ai/po-runner-rmux-darwin-x64](https://pi.dev/packages/@agimon-ai/po-runner-rmux-darwin-x64?page=4) | 11,333/mo | package | Prebuilt RMUX runtime for Po Runner on macOS x64. | `pi install npm:@agimon-ai/po-runner-rmux-darwin-x64` |
| 166 | [@agimon-ai/po-runner-rmux-linux-arm64](https://pi.dev/packages/@agimon-ai/po-runner-rmux-linux-arm64?page=4) | 11,278/mo | package | Prebuilt RMUX runtime for Po Runner on Linux arm64. | `pi install npm:@agimon-ai/po-runner-rmux-linux-arm64` |
| 169 | [@agimon-ai/po-runner-rmux-darwin-arm64](https://pi.dev/packages/@agimon-ai/po-runner-rmux-darwin-arm64?page=4) | 11,106/mo | package | Prebuilt RMUX runtime for Po Runner on macOS arm64. | `pi install npm:@agimon-ai/po-runner-rmux-darwin-arm64` |
| 194 | [@relaymessenger/pi](https://pi.dev/packages/@relaymessenger/pi?page=4) | 9,504/mo | package | Relay Messenger channel for Pi over Relay v1 WebSocket delivery. | `pi install npm:@relaymessenger/pi` |
| 211 | [@xynogen/pix-runtime](https://pi.dev/packages/@xynogen/pix-runtime?page=5) | 8,279/mo | extension | Pix 共享运行时 —— 带版本号的 pix.json 配置、原子化持久化、类型化变更事件 | `pi install npm:@xynogen/pix-runtime` |
| 217 | [pi-herdsman](https://pi.dev/packages/pi-herdsman?page=5) | 7,935/mo | extension | Asynchronous Pi subagents and agent fleet orchestration for parallel coding agents with nested delegation, background work, and supervision in herdr. | `pi install npm:pi-herdsman` |
| 218 | [@pi-unipi/notify](https://pi.dev/packages/@pi-unipi/notify?page=5) | 7,844/mo | extension | Pi 的跨平台通知扩展——为代理生命周期事件提供原生操作系统、Gotify 和 Telegram 通知。 | `pi install npm:@pi-unipi/notify` |
| 252 | [pi-dev-flow](https://pi.dev/packages/pi-dev-flow?page=6) | 6,588/mo | extension | Enforced feature workflow for Pi: plan → implement → pre-release → release, gated checkpoints, self-improvement reflections, one git worktree per feature, changelog + publish as part of the release | `pi install npm:pi-dev-flow` |
| 260 | [@agimon-ai/doompi-runner](https://pi.dev/packages/@agimon-ai/doompi-runner?page=6) | 6,370/mo | package | 为 Pi 编码代理提供受监督的 shell 执行、后台进程控制与运行日志。 | `pi install npm:@agimon-ai/doompi-runner` |
| 264 | [@henryqw/pi-config-store](https://pi.dev/packages/@henryqw/pi-config-store?page=6) | 6,287/mo | package | Safe JSON configuration storage for Pi extensions. | `pi install npm:@henryqw/pi-config-store` |
| 286 | [@amaster.ai/pi-computer-use](https://pi.dev/packages/@amaster.ai/pi-computer-use?page=6) | 5,914/mo | extension | 面向 Pi 桌面自动化的跨平台 computer-use（计算机操作）工具 | `pi install npm:@amaster.ai/pi-computer-use` |
| 300 | [@fro.bot/systematic](https://pi.dev/packages/@fro.bot/systematic?page=6) | 5,777/mo | package | Compound-engineering loops for OpenCode, Pi, and Claude Code | `pi install npm:@fro.bot/systematic` |

### 代码智能 / 编辑 / Review

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 14 | [@plannotator/pi-extension](https://pi.dev/packages/@plannotator/pi-extension) | 92,600/mo | package | Plannotator Pi 扩展：支持带注释的交互式计划审查、为代理消息添加注释，以及审查代码/PR。 | `pi install npm:@plannotator/pi-extension` |
| 17 | [pi-lens](https://pi.dev/packages/pi-lens) | 82,059/mo | extension | 面向 pi 的实时代码反馈——LSP、linter、格式化工具、类型检查、结构分析与 booboo | `pi install npm:pi-lens` |
| 35 | [pi-simplify](https://pi.dev/packages/pi-simplify) | 39,054/mo | extension | 一个 Pi 扩展，用于审查最近改动的代码，以提升其清晰度、一致性和可维护性。 | `pi install npm:pi-simplify` |
| 48 | [gentle-pi](https://pi.dev/packages/gentle-pi) | 30,488/mo | package | 将 Pi 变成 el Gentleman：一个资深架构师级的开发框架，具备 SDD/OpenSpec、子代理、严格的 TDD 证据、审查护栏和技能包发现能力。 | `pi install npm:gentle-pi` |
| 71 | [@heyhuynhgiabuu/pi-pretty](https://pi.dev/packages/@heyhuynhgiabuu/pi-pretty?page=2) | 22,112/mo | extension | 让 pi 的终端输出更美观——语法高亮的文件读取、彩色 bash 输出、树状目录列表等。 | `pi install npm:@heyhuynhgiabuu/pi-pretty` |
| 83 | [pi-hashline-edit-pro](https://pi.dev/packages/pi-hashline-edit-pro?page=2) | 17,932/mo | extension | 适用于 pi-coding-agent 的哈希锚定 read/replace/insert/grep 工具：每一行都会获得唯一的 3 字符哈希（A-Za-z0-9），且跨编辑保持稳定；过期或有歧义的锚点会被拒绝，绝不模糊匹配。撤销记录在重启后依然保留。 | `pi install npm:pi-hashline-edit-pro` |
| 86 | [@agimon-ai/po-hashline](https://pi.dev/packages/@agimon-ai/po-hashline?page=2) | 17,068/mo | package | Shared snapshot-bound file tags and line anchors for Po tools. | `pi install npm:@agimon-ai/po-hashline` |
| 120 | [pi-pokepet](https://pi.dev/packages/pi-pokepet?page=3) | 12,545/mo | extension | A cute, colorful pet companion for the pi coding agent. Use classic ASCII pets or Petdex image pets that live below your editor and react to tools, tests, commits, PRs, reviews, subagents, model swaps and more. | `pi install npm:pi-pokepet` |
| 150 | [@agimon-ai/po-file-edit](https://pi.dev/packages/@agimon-ai/po-file-edit?page=3) | 11,715/mo | extension | Native Po session-scoped file-change timelines, review APIs, and cross-agent edit presence. | `pi install npm:@agimon-ai/po-file-edit` |
| 155 | [@agimon-ai/po-author](https://pi.dev/packages/@agimon-ai/po-author?page=4) | 11,692/mo | extension | Visual steering workspace for focused document review and bounded authoring | `pi install npm:@agimon-ai/po-author` |
| 158 | [@agimon-ai/po-edit](https://pi.dev/packages/@agimon-ai/po-edit?page=4) | 11,646/mo | extension | Snapshot-bound hashline edit tool for Pi and Po. | `pi install npm:@agimon-ai/po-edit` |
| 159 | [@agimon-ai/po-grep](https://pi.dev/packages/@agimon-ai/po-grep?page=4) | 11,644/mo | extension | Snapshot-bound hashline grep for Pi and Po. | `pi install npm:@agimon-ai/po-grep` |
| 162 | [@agimon-ai/po-read](https://pi.dev/packages/@agimon-ai/po-read?page=4) | 11,592/mo | extension | Snapshot-bound hashline read tool for Pi and Po. | `pi install npm:@agimon-ai/po-read` |
| 192 | [pi-pigment](https://pi.dev/packages/pi-pigment?page=4) | 9,691/mo | extension, theme | Pigment for your pi: syntax highlighting for diffs, shell, grep and listings in your theme's colors — ships the Shiki bundle, imports TextMate (.tmTheme) themes | `pi install npm:pi-pigment` |
| 200 | [@narumitw/pi-lsp](https://pi.dev/packages/@narumitw/pi-lsp?page=4) | 9,286/mo | extension | Pi 扩展，通过共享的 runner 提供可配置、语言无关的 LSP 工具。 | `pi install npm:@narumitw/pi-lsp` |
| 231 | [@agimon-ai/doompi-hashline](https://pi.dev/packages/@agimon-ai/doompi-hashline?page=5) | 7,288/mo | package | Shared snapshot-bound file tags and line anchors for DoomPi tools. | `pi install npm:@agimon-ai/doompi-hashline` |
| 272 | [pi-orchestrator-config](https://pi.dev/packages/pi-orchestrator-config?page=6) | 6,172/mo | package | Orchestrator pattern for pi: specialist subagents, enforcement, code review loop, workflow commands | `pi install npm:pi-orchestrator-config` |
| 283 | [@agimon-ai/doompi-file-edit](https://pi.dev/packages/@agimon-ai/doompi-file-edit?page=6) | 5,980/mo | extension | Pi 扩展，提供会话级文件变更时间线与外部编辑器工作流。 | `pi install npm:@agimon-ai/doompi-file-edit` |
| 289 | [@agimon-ai/doompi-grep](https://pi.dev/packages/@agimon-ai/doompi-grep?page=6) | 5,885/mo | extension | Snapshot-bound hashline grep for Pi and DoomPi. | `pi install npm:@agimon-ai/doompi-grep` |
| 297 | [@agimon-ai/doompi-edit](https://pi.dev/packages/@agimon-ai/doompi-edit?page=6) | 5,803/mo | extension | Snapshot-bound hashline edit tool for Pi and DoomPi. | `pi install npm:@agimon-ai/doompi-edit` |

### 安全 / 权限 / Sandbox

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 15 | [cc-safety-net](https://pi.dev/packages/cc-safety-net) | 90,924/mo | package | 编码代理 CLI 钩子：阻止破坏性命令与机密文件访问。 | `pi install npm:cc-safety-net` |
| 25 | [@gotgenes/pi-permission-system](https://pi.dev/packages/@gotgenes/pi-permission-system) | 55,641/mo | extension | 面向 Pi 编码代理的权限强制扩展。 | `pi install npm:@gotgenes/pi-permission-system` |
| 34 | [@vigolium/piolium](https://pi.dev/packages/@vigolium/piolium) | 39,903/mo | extension | 多阶段安全审计，由专业子代理负责执行，具备隔离的上下文窗口、受限并发与可恢复状态——以 Pi 扩展形式打包提供。 | `pi install npm:@vigolium/piolium` |
| 42 | [@agimon-ai/po-web-security](https://pi.dev/packages/@agimon-ai/po-web-security) | 32,173/mo | package | Shared security primitives for the Po web cockpit: sealed channels and signed bundle manifests for independently trusted verifiers. | `pi install npm:@agimon-ai/po-web-security` |
| 87 | [latchkey](https://pi.dev/packages/latchkey?page=2) | 16,295/mo | package | 一个 CLI 工具，可将 API 凭据注入到发往第三方服务的 curl 请求中。 | `pi install npm:latchkey` |
| 129 | [pi-deltabox](https://pi.dev/packages/pi-deltabox?page=3) | 11,992/mo | package | Pi extension: agent-native sandbox sessions with diff/commit/abort, powered by deltabox-lite | `pi install npm:pi-deltabox` |
| 143 | [pi-goal-list-loop-audit](https://pi.dev/packages/pi-goal-list-loop-audit?page=3) | 11,782/mo | extension | 自主 pi 的任务控制：访谈起草的目标、受审计的任务队列，以及可运行数小时的永久循环（metric、spec、project-audit）。一个独立的、无需扩展的审计进程会用原始证据重新验证每次完成，而不会持有 | `pi install npm:pi-goal-list-loop-audit` |
| 151 | [@agimon-ai/po-sandbox](https://pi.dev/packages/@agimon-ai/po-sandbox?page=4) | 11,712/mo | extension | Per-workspace sandbox containers for Po: the container provider, the shared image, the container lifecycle, and a host credential broker | `pi install npm:@agimon-ai/po-sandbox` |
| 168 | [@trim21/personal-pi-extensions](https://pi.dev/packages/@trim21/personal-pi-extensions?page=4) | 11,123/mo | package | 自定义 pi 编码代理扩展：bwrap 沙箱、工作区守卫、opencode 编辑，以及更多。 | `pi install npm:@trim21/personal-pi-extensions` |
| 171 | [@agimon-ai/doompi-web-security](https://pi.dev/packages/@agimon-ai/doompi-web-security?page=4) | 10,994/mo | package | Shared security primitives for the DoomPi web cockpit: sealed channels and signed bundle manifests for independently trusted verifiers. | `pi install npm:@agimon-ai/doompi-web-security` |
| 212 | [pi-better-harness](https://pi.dev/packages/pi-better-harness?page=5) | 8,141/mo | extension | Pi extension bundle for a write sandbox, subagents, background tasks, SSH, goals, and Outcome & Todo. | `pi install npm:pi-better-harness` |
| 258 | [@silmaril-security/pi-firewall-plugin](https://pi.dev/packages/@silmaril-security/pi-firewall-plugin?page=6) | 6,418/mo | package | Silmaril Firewall lifecycle protection for Pi coding agents. | `pi install npm:@silmaril-security/pi-firewall-plugin` |
| 285 | [pi-sandbox](https://pi.dev/packages/pi-sandbox?page=6) | 5,937/mo | extension | 为 pi 提供操作系统级沙箱，带交互式权限提示。 | `pi install npm:pi-sandbox` |
| 291 | [@agimon-ai/doompi-sandbox](https://pi.dev/packages/@agimon-ai/doompi-sandbox?page=6) | 5,836/mo | extension | Container sandbox for DoomPi launches: the agent, extensions, and tools run inside Docker or Podman while the terminal stays on the host | `pi install npm:@agimon-ai/doompi-sandbox` |
| 293 | [kifaru](https://pi.dev/packages/kifaru?page=6) | 5,826/mo | package | Kifaru security agent on the Pi runtime | `pi install npm:kifaru` |

### 其他 / 待复核

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 7 | [@hypabolic/pi-hypa](https://pi.dev/packages/@hypabolic/pi-hypa) | 204,470/mo | package | Pi 扩展，让嘈杂的工具输出远离你的上下文窗口。通过 Hypa 自动重写 shell 命令，实现本地确定性压缩、上下文感知的文件工具与可恢复的证据。 | `pi install npm:@hypabolic/pi-hypa` |
| 43 | [@ayulab/pi-rewind](https://pi.dev/packages/@ayulab/pi-rewind) | 32,143/mo | extension | Pi extension providing /rewind checkpoint navigation | `pi install npm:@ayulab/pi-rewind` |
| 56 | [@cratis/pi](https://pi.dev/packages/@cratis/pi?page=2) | 26,214/mo | skill | Configuration-aware Cratis AI integration for Pi | `pi install npm:@cratis/pi` |
| 70 | [@jwilger/pi-development-system](https://pi.dev/packages/@jwilger/pi-development-system?page=2) | 22,301/mo | package | A pi extension package representing a seasoned approach to software development using a full AI SDLC. | `pi install npm:@jwilger/pi-development-system` |
| 115 | [@agimon-ai/po-build](https://pi.dev/packages/@agimon-ai/po-build?page=3) | 12,846/mo | package | Folder-convention scanner and build presets for Po extensions. | `pi install npm:@agimon-ai/po-build` |
| 204 | [@gyoungwe/pi-evidence](https://pi.dev/packages/@gyoungwe/pi-evidence?page=5) | 9,042/mo | package | Portable evidence manifests, provenance, checkpoints and replay proofs for native Pi | `pi install npm:@gyoungwe/pi-evidence` |
| 223 | [pi-typesafe](https://pi.dev/packages/pi-typesafe?page=5) | 7,518/mo | extension | TypeSafe AI (Jev) decisions for Pi: batched Choice/Score/Noul evaluation tool, terminal playground, and a typed API other extensions build on. | `pi install npm:pi-typesafe` |
| 254 | [@henryqw/pi-pr](https://pi.dev/packages/@henryqw/pi-pr?page=6) | 6,494/mo | package | Run /pr to safely discover or link the current pull request, then create, update, address feedback, fix CI, or merge when ready. | `pi install npm:@henryqw/pi-pr` |
