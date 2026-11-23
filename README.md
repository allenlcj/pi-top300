# Pi Top 300

Pi 官方 Package Catalog 前 300 热门包的用途分类目录（All types · Most downloads）。

[分类指南](docs/categories.md) · [按排名清单](docs/packages.md) · [原始 JSON 数据](data/packages-latest.json)

> ⚠️ Pi 包可能以当前用户权限执行代码，安装前请审查源码和权限。
> 下载量为 npm 月下载量，不代表质量或安全性。分类基于名称和描述的初步归类，人工意见维护在 `data/categories.yaml`。

- 快照 `2026-11-23`（[历史快照](data/snapshots/)）· 共 300 包

## 分类总览

| 类别 | 数量 | 占比 |
| --- | ---: | ---: |
| [Web / Browser / Research / MCP](#web-browser-research-mcp) | 42 | 14% |
| [模型 / Provider / 路由 / 用量](#模型-provider-路由-用量) | 42 | 14% |
| [Agent 编排 / Subagent / Plan / Goal / Task](#agent-编排-subagent-plan-goal-task) | 41 | 14% |
| [Context / Memory / Knowledge / Compaction](#context-memory-knowledge-compaction) | 40 | 13% |
| [UI / TUI / Session / 观测](#ui-tui-session-观测) | 35 | 12% |
| [Skills / Prompt / Rules / 提问](#skills-prompt-rules-提问) | 23 | 8% |
| [Runtime / 后台任务 / Worktree / 集成](#runtime-后台任务-worktree-集成) | 23 | 8% |
| [代码智能 / 编辑 / Review](#代码智能-编辑-review) | 21 | 7% |
| [安全 / 权限 / Sandbox](#安全-权限-sandbox) | 19 | 6% |
| [其他 / 待复核](#其他-待复核) | 14 | 5% |

## 按类别清单

### Web / Browser / Research / MCP

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 3 | [pi-web-access](https://pi.dev/packages/pi-web-access) | 1,374,078/mo | extension | 为 Pi 编码代理提供网页搜索、URL 抓取、GitHub 仓库克隆、PDF 提取、YouTube 视频理解与本地视频分析。支持 OpenAI、Brave、Parallel、TinyFish、Search1API、Searchinfinity、Querit、Tavily、Firecrawl、Jina、SERPdive、Ka | `pi install npm:pi-web-access` |
| 5 | [pi-mcp-extension](https://pi.dev/packages/pi-mcp-extension) | 981,476/mo | extension | 面向 Pi 编码代理的 MCP（Model Context Protocol）客户端扩展——将 Pi 连接到任意 MCP 服务器。 | `pi install npm:pi-mcp-extension` |
| 11 | [@onkernel/browser-loop](https://pi.dev/packages/@onkernel/browser-loop) | 190,441/mo | extension | Browser tools for your agent: framework-neutral tool catalog, per-model compilation, Kernel-browser execution, and a pi binding + extension | `pi install npm:@onkernel/browser-loop` |
| 25 | [@agimon-ai/po-logsink](https://pi.dev/packages/@agimon-ai/po-logsink) | 88,288/mo | package | Log sink MCP server with HTTP ingestion and AI analysis | `pi install npm:@agimon-ai/po-logsink` |
| 30 | [@quintinshaw/pi-dynamic-workflows](https://pi.dev/packages/@quintinshaw/pi-dynamic-workflows) | 82,525/mo | package | 面向 Pi 的 Claude Code 风格动态工作流：将任务扇出至数百个子代理，具备真实模型路由、token/成本核算、断点续跑、git 工作树隔离、交互式 /workflows TUI，以及真正的 /deep-research。 | `pi install npm:@quintinshaw/pi-dynamic-workflows` |
| 31 | [@agimon-ai/po-web-components](https://pi.dev/packages/@agimon-ai/po-web-components) | 77,197/mo | theme | Shared web components and theme tokens for the Po cockpit and its web plugins: shadcn-style primitives on Radix, tuned to the Po palette, with runtime theme configs. | `pi install npm:@agimon-ai/po-web-components` |
| 32 | [@datadog/pi-plugin](https://pi.dev/packages/@datadog/pi-plugin) | 70,631/mo | package | Use Datadog directly in the Pi coding agent through a preconfigured Datadog MCP server. Query logs, metrics, traces, dashboards, and more through natural conversation. | `pi install npm:@datadog/pi-plugin` |
| 53 | [pi-agent-browser-native](https://pi.dev/packages/pi-agent-browser-native?page=2) | 36,690/mo | extension | pi 扩展，将 agent-browser 作为原生工具开放，用于浏览器自动化。 | `pi install npm:pi-agent-browser-native` |
| 57 | [@agimon-ai/po-web-dashboard](https://pi.dev/packages/@agimon-ai/po-web-dashboard?page=2) | 35,196/mo | package | Shared browser state, actions and optional views for Po dashboard templates. | `pi install npm:@agimon-ai/po-web-dashboard` |
| 62 | [@agimon-ai/po-domain](https://pi.dev/packages/@agimon-ai/po-domain?page=2) | 34,826/mo | extension, skill | Domain selection, resource staging, and MCP scoping for Po sessions. | `pi install npm:@agimon-ai/po-domain` |
| 65 | [@agimon-ai/po](https://pi.dev/packages/@agimon-ai/po?page=2) | 33,580/mo | package | Opinionated, composable agent harness for scoped tools, skills, MCP servers, and developer workflows. | `pi install npm:@agimon-ai/po` |
| 66 | [@agimon-ai/po-skill](https://pi.dev/packages/@agimon-ai/po-skill?page=2) | 33,502/mo | extension | Session skill catalogue, deferred skill discovery, and the skill browser for Po. | `pi install npm:@agimon-ai/po-skill` |
| 68 | [@agimon-ai/po-mcp](https://pi.dev/packages/@agimon-ai/po-mcp?page=2) | 33,011/mo | extension | Domain-aware MCP server selection and access boundaries for Pi sessions composed with Po. | `pi install npm:@agimon-ai/po-mcp` |
| 69 | [@agimon-ai/po-template-advanced](https://pi.dev/packages/@agimon-ai/po-template-advanced?page=2) | 32,663/mo | package | Advanced multi-panel template for the Po web client. | `pi install npm:@agimon-ai/po-template-advanced` |
| 70 | [@agimon-ai/po-template-elegant](https://pi.dev/packages/@agimon-ai/po-template-elegant?page=2) | 31,766/mo | package | Elegant chat-first template for the Po web client. | `pi install npm:@agimon-ai/po-template-elegant` |
| 110 | [@agimon-ai/po-identity](https://pi.dev/packages/@agimon-ai/po-identity?page=3) | 29,403/mo | package | Po account client: sign-in, device trust and Team for the phone, Desktop and web | `pi install npm:@agimon-ai/po-identity` |
| 123 | [@ff-labs/pi-fff](https://pi.dev/packages/@ff-labs/pi-fff?page=3) | 23,515/mo | extension | pi 扩展：由 FFF 驱动的模糊文件与内容搜索。 | `pi install npm:@ff-labs/pi-fff` |
| 137 | [pi-webapp](https://pi.dev/packages/pi-webapp?page=3) | 18,925/mo | package | One workspace for your Pi coding agent: live chat, files, real terminals, and Git review side by side, plus optional Excalidraw diagrams and OpenPencil UI design, in your browser or on desktop | `pi install npm:pi-webapp` |
| 138 | [@companion-ai/feynman](https://pi.dev/packages/@companion-ai/feynman?page=3) | 18,853/mo | package | 基于 Pi 和 alphaXiv 构建的研究优先 CLI 代理 | `pi install npm:@companion-ai/feynman` |
| 147 | [@agntn/web](https://pi.dev/packages/@agntn/web?page=3) | 16,844/mo | extension | Unified web search and read provider for agents and CLI. | `pi install npm:@agntn/web` |
| 151 | [pi-browser-harness](https://pi.dev/packages/pi-browser-harness?page=4) | 15,961/mo | extension | Browser control extension for pi — navigate, click, type, screenshot, and extract data from real Chrome via CDP | `pi install npm:pi-browser-harness` |
| 158 | [pi-web-ui](https://pi.dev/packages/pi-web-ui?page=4) | 15,056/mo | package | 基于 pi SDK（@earendil-works/pi-coding-agent）的 pi 编码代理 Web 聊天界面——一条命令即可运行，支持 Docker/systemd/launchd 部署。 | `pi install npm:pi-web-ui` |
| 160 | [@agent-sh/computer-use-linux](https://pi.dev/packages/@agent-sh/computer-use-linux?page=4) | 14,756/mo | package | Native Linux desktop control for AI agents (MCP server, Pi tools, and CLI): semantic AT-SPI accessibility trees, screenshots, compositor window targeting, Wayland/X11 input, and an on-screen activity indicator. | `pi install npm:@agent-sh/computer-use-linux` |
| 163 | [@selesai/code](https://pi.dev/packages/@selesai/code?page=4) | 14,522/mo | package | 持续维护、以扩展为先的 Pi coding agent，内置工作流、子代理、网页研究、提问、技能包以及增强的终端 UI。 | `pi install npm:@selesai/code` |
| 170 | [donsetch](https://pi.dev/packages/donsetch?page=4) | 13,773/mo | package | 面向 AI 代理的网页抓取、搜索与爬取能力。零 API 密钥。Chrome 级真实 TLS。 | `pi install npm:donsetch` |
| 171 | [@xynogen/pix-pretty](https://pi.dev/packages/@xynogen/pix-pretty?page=4) | 13,747/mo | extension | 增强的工具输出渲染：语法高亮、文件图标、树形视图、diff 渲染和 FFF 搜索 | `pi install npm:@xynogen/pix-pretty` |
| 174 | [@jmfederico/pi-web](https://pi.dev/packages/@jmfederico/pi-web?page=4) | 13,288/mo | package | 为真实工作区中持久化的 Pi Coding Agent 会话提供 Web UI。 | `pi install npm:@jmfederico/pi-web` |
| 179 | [@ollama/pi-web-search](https://pi.dev/packages/@ollama/pi-web-search?page=4) | 12,734/mo | extension | 面向 Pi 代理的网络搜索与抓取工具——使用 Ollama 的网络搜索与抓取 API。 | `pi install npm:@ollama/pi-web-search` |
| 189 | [@gyoungwe/research-suite](https://pi.dev/packages/@gyoungwe/research-suite?page=4) | 12,284/mo | package | Bundled Drone native Pi research suite | `pi install npm:@gyoungwe/research-suite` |
| 194 | [dripline](https://pi.dev/packages/dripline?page=4) | 11,742/mo | package | 一次一滴地查询任何内容。 | `pi install npm:dripline` |
| 197 | [@fitchmultz/pi-mcp-adapter](https://pi.dev/packages/@fitchmultz/pi-mcp-adapter?page=4) | 11,583/mo | extension | Token-efficient MCP adapter for the Pi coding agent | `pi install npm:@fitchmultz/pi-mcp-adapter` |
| 199 | [@cmo-so/skills](https://pi.dev/packages/@cmo-so/skills?page=4) | 11,506/mo | skill | Install the CMO.so marketing skills (SEO, AI search, content, social, email, ads, CRO, analytics) into Claude Code, Codex, Pi, Cursor, Gemini CLI, OpenCode, Copilot and other coding agents, for one project or for your user. Also a Pi package. | `pi install npm:@cmo-so/skills` |
| 209 | [pi-markdown-preview](https://pi.dev/packages/pi-markdown-preview?page=5) | 11,241/mo | package | 面向 pi 的渲染版 Markdown + LaTeX 预览，支持终端、浏览器和 PDF 输出。 | `pi install npm:pi-markdown-preview` |
| 220 | [@agimon-ai/po-template-desktop](https://pi.dev/packages/@agimon-ai/po-template-desktop?page=5) | 10,827/mo | package | Windowed desktop template for the Po web client. | `pi install npm:@agimon-ai/po-template-desktop` |
| 233 | [@gyoungwe/pi-research](https://pi.dev/packages/@gyoungwe/pi-research?page=5) | 10,035/mo | package | Evidence-gated research retrieval, reading, deposition and source-grounded answer tools for native Pi | `pi install npm:@gyoungwe/pi-research` |
| 239 | [@juicesharp/rpiv-web-tools](https://pi.dev/packages/@juicesharp/rpiv-web-tools?page=5) | 9,652/mo | extension | Pi 扩展。为模型提供网络搜索与抓取能力，支持可插拔的模型提供方（Brave、Tavily、Serper、Exa、You.com、Jina、Firecrawl、Perplexity、SearXNG、Ollama）。 | `pi install npm:@juicesharp/rpiv-web-tools` |
| 258 | [pi-skill-evolve](https://pi.dev/packages/pi-skill-evolve?page=6) | 8,737/mo | extension, skill | 技能进化：采集会话中的技能曝光/加载，异步复盘、生成改进提案并独立评审，附本机 Web 管理面板 | `pi install npm:pi-skill-evolve` |
| 260 | [@agimon-ai/log-sink-mcp](https://pi.dev/packages/@agimon-ai/log-sink-mcp?page=6) | 8,539/mo | package | 支持 HTTP 摄取与 AI 分析的日志汇聚（log sink）MCP 服务器。 | `pi install npm:@agimon-ai/log-sink-mcp` |
| 264 | [arcmira](https://pi.dev/packages/arcmira?page=6) | 8,437/mo | package | YouTube transcript search and monitoring for your AI: exact quotes, full transcripts and speakers. | `pi install npm:arcmira` |
| 273 | [@amaster.ai/pi-browser-use](https://pi.dev/packages/@amaster.ai/pi-browser-use?page=6) | 7,954/mo | extension | Pi 扩展，通过 chrome-devtools-mcp 实现浏览器自动化，提供 browser_ 前缀的工具。 | `pi install npm:@amaster.ai/pi-browser-use` |
| 283 | [@amaster.ai/pi-web-access](https://pi.dev/packages/@amaster.ai/pi-web-access?page=6) | 7,493/mo | extension | Pi 扩展，提供网页搜索、URL 内容提取和图片搜索（Tavily、Kimi、DeepSeek、Mimo、Z.AI、DashScope、Unsplash 等）。 | `pi install npm:@amaster.ai/pi-web-access` |
| 295 | [keyshroud](https://pi.dev/packages/keyshroud?page=6) | 7,262/mo | extension | Let AI coding agents use your secrets without ever seeing them. Encrypted local vault, self-hosted Vaultwarden/Bitwarden, or your team's HashiCorp Vault, OpenBao, Infisical, 1Password, AWS, Google Cloud or Azure secrets; masked output, MCP server, Claude | `pi install npm:keyshroud` |

### 模型 / Provider / 路由 / 用量

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 6 | [@postman/postman-plugin](https://pi.dev/packages/@postman/postman-plugin) | 508,319/mo | package | Postman's API engineering skills for coding agents: a Pi package, and an npx installer that sets up Claude Code, Codex, Cursor, Kimi Code, Factory Droid, OpenCode and Pi. | `pi install npm:@postman/postman-plugin` |
| 16 | [pi-claude-bridge](https://pi.dev/packages/pi-claude-bridge) | 129,731/mo | extension | Pi 扩展，将 Claude Code（通过 Agent SDK）用作模型提供方，并新增 AskClaude 工具。 | `pi install npm:pi-claude-bridge` |
| 35 | [pi-harness-runtime](https://pi.dev/packages/pi-harness-runtime) | 57,827/mo | extension | [BETA] 面向 pi 的 Codex 风格 /usage 状态与自主编码 harness。尚未达到生产就绪——预计会有破坏性变更。 | `pi install npm:pi-harness-runtime` |
| 40 | [@gotgenes/pi-anthropic-auth](https://pi.dev/packages/@gotgenes/pi-anthropic-auth) | 48,661/mo | package | 用于 Anthropic OAuth 兼容性的 Pi 扩展包 | `pi install npm:@gotgenes/pi-anthropic-auth` |
| 46 | [@braintrust/pi-extension](https://pi.dev/packages/@braintrust/pi-extension) | 43,338/mo | package | 面向 pi 的 Braintrust 扩展，可自动将 pi 会话、轮次、LLM 调用和工具执行追踪到 Braintrust。 | `pi install npm:@braintrust/pi-extension` |
| 88 | [@agimon-ai/po-goal](https://pi.dev/packages/@agimon-ai/po-goal?page=2) | 31,162/mo | extension | Pi mode for persistent agent goals, token budgets, and goal history. | `pi install npm:@agimon-ai/po-goal` |
| 89 | [pi-coralbricks-provider](https://pi.dev/packages/pi-coralbricks-provider?page=2) | 31,141/mo | extension | CoralBricks provider extension for pi - Access DeepSeek V4.1 Flash through the Coral Inference API | `pi install npm:pi-coralbricks-provider` |
| 98 | [@narumitw/pi-usage](https://pi.dev/packages/@narumitw/pi-usage?page=2) | 30,727/mo | extension | Pi 扩展，可显示受支持模型提供方的当前账户用量和 DeepSeek API 余额。 | `pi install npm:@narumitw/pi-usage` |
| 114 | [pi-provider-litellm](https://pi.dev/packages/pi-provider-litellm?page=3) | 26,760/mo | extension | 面向 Pi 的 LiteLLM 代理模型提供方扩展。 | `pi install npm:pi-provider-litellm` |
| 115 | [pi-otel](https://pi.dev/packages/pi-otel?page=3) | 25,875/mo | extension | OpenTelemetry traces for pi-coding-agent — per-prompt span tree (interaction → llm_request, tool.<name>) exported via OTLP. Aspire-dashboard ready. | `pi install npm:pi-otel` |
| 120 | [pi-fireworks](https://pi.dev/packages/pi-fireworks?page=3) | 24,688/mo | extension | Fireworks AI provider extension package for pi | `pi install npm:pi-fireworks` |
| 122 | [pi-fireworks-quota](https://pi.dev/packages/pi-fireworks-quota?page=3) | 23,721/mo | extension | Pi commands /fireworks:quota and /fireworks:test-key — Fireworks AI balance, spend, tokens, and limits | `pi install npm:pi-fireworks-quota` |
| 127 | [pi-cursor-sdk](https://pi.dev/packages/pi-cursor-sdk?page=3) | 21,177/mo | extension | 由 @cursor/sdk 本地及云端 AI 代理支撑的 pi 模型提供方扩展 | `pi install npm:pi-cursor-sdk` |
| 129 | [pi-antigravity](https://pi.dev/packages/pi-antigravity?page=3) | 20,873/mo | extension | 面向 Pi Coding Agent 的个人 Antigravity / Cloud Code Assist 模型提供方。 | `pi install npm:pi-antigravity` |
| 132 | [@sting8k/pi-vcc](https://pi.dev/packages/@sting8k/pi-vcc?page=3) | 19,965/mo | extension | Algorithmic conversation compactor for pi - transcript-preserving structured summaries, no LLM calls | `pi install npm:@sting8k/pi-vcc` |
| 133 | [thoth-agents](https://pi.dev/packages/thoth-agents?page=3) | 19,438/mo | package | Adaptive multi-harness orchestration with six roles, runtime-autonomous AI-first execution routes, and external provider boundaries. | `pi install npm:thoth-agents` |
| 141 | [@amaster.ai/pi-image-gen](https://pi.dev/packages/@amaster.ai/pi-image-gen?page=3) | 17,808/mo | extension | Pi 图片生成扩展，支持通过 OpenAI gpt-image、Google Nano Banana（Gemini）、阿里 Qwen-Image、OpenRouter 及自定义模型提供方生成图片。 | `pi install npm:@amaster.ai/pi-image-gen` |
| 142 | [@tmustier/pi-usage-extension](https://pi.dev/packages/@tmustier/pi-usage-extension?page=3) | 17,789/mo | package | Pi 会话的用量统计仪表盘。 | `pi install npm:@tmustier/pi-usage-extension` |
| 145 | [agent-comms](https://pi.dev/packages/agent-comms?page=3) | 17,390/mo | package | Cross-harness communication mesh for LLM agents — rooms, DMs, presence, and real-time push delivery over TCP | `pi install npm:agent-comms` |
| 164 | [@cortexkit/pi-openai-auth](https://pi.dev/packages/@cortexkit/pi-openai-auth?page=4) | 14,446/mo | package | 为 CortexKit 提供 OpenAI Codex OAuth 支持的 Pi 包。它用基于 Pi 的 OpenAI Codex Responses 传输层和 OAuth 原语的 CortexKit 模型提供方扩展，覆盖 Pi 内置的 `openai-codex` 模型提供方。 | `pi install npm:@cortexkit/pi-openai-auth` |
| 173 | [@nredd/pi-session-kit](https://pi.dev/packages/@nredd/pi-session-kit?page=4) | 13,524/mo | extension | Session-scoped pi tools and commands, offline cross-machine usage stats and a portable privacy-only stats CLI. No daemon. | `pi install npm:@nredd/pi-session-kit` |
| 176 | [@cortexkit/pi-anthropic-auth](https://pi.dev/packages/@cortexkit/pi-anthropic-auth?page=4) | 13,149/mo | package | 为 CortexKit 提供 Anthropic OAuth 支持的 Pi 包。它用由共享的 `@cortexkit/anthropic-auth-core` 包支撑的 CortexKit 模型提供方扩展，覆盖 Pi 内置的 `anthropic` 模型提供方。 | `pi install npm:@cortexkit/pi-anthropic-auth` |
| 177 | [pi-dashscope](https://pi.dev/packages/pi-dashscope?page=4) | 13,068/mo | package | Alibaba DashScope (ModelStudio) provider for oh my pi — Qwen3, GLM-5, MiniMax M2.5, Kimi K2.5 via OpenAI-compatible coding API | `pi install npm:pi-dashscope` |
| 184 | [@nredd/pi-subscription-router](https://pi.dev/packages/@nredd/pi-subscription-router?page=4) | 12,526/mo | extension | Pi virtual models that route across included subscription quota: Anthropic and ChatGPT Codex usage collectors, confirmed per-family exhaustion, and mid-run quota recovery. | `pi install npm:@nredd/pi-subscription-router` |
| 191 | [pi-llama-cpp](https://pi.dev/packages/pi-llama-cpp?page=4) | 12,079/mo | extension | 用于集成 llama.cpp 的 Pi 扩展。支持 router、单模型与旧版（legacy）模型，并支持多个服务器。 | `pi install npm:pi-llama-cpp` |
| 192 | [pi-zhipu-usage](https://pi.dev/packages/pi-zhipu-usage?page=4) | 11,804/mo | package | Pi extension: show GLM Coding Plan usage and reset countdown in the footer. Supports Zhipu domestic (open.bigmodel.cn), international (api.z.ai), local proxy / Headroom setups, and @zigai/pi-footer slot integration. | `pi install npm:pi-zhipu-usage` |
| 207 | [pi-commandcode-provider](https://pi.dev/packages/pi-commandcode-provider?page=5) | 11,264/mo | extension | pi custom provider for Command Code API (commandcode.ai) | `pi install npm:pi-commandcode-provider` |
| 210 | [pi-cliproxyapi-provider](https://pi.dev/packages/pi-cliproxyapi-provider?page=5) | 11,175/mo | extension | 面向 CLIProxyAPI 的 Pi 模型提供方包，支持自动发现模型并利用 models.dev 补充模型信息。 | `pi install npm:pi-cliproxyapi-provider` |
| 215 | [pi-caveman](https://pi.dev/packages/pi-caveman?page=5) | 10,996/mo | extension | 既然少量 token 就能奏效，何必使用大量 token。pi 的穴居人模式 —— 在保持完整技术准确性的同时减少约 75% 的输出 token。 | `pi install npm:pi-caveman` |
| 222 | [pi-ollama-cloud](https://pi.dev/packages/pi-ollama-cloud?page=5) | 10,603/mo | package | 面向 [Pi](https://pi.dev) 编码代理的 Ollama Cloud 模型提供方插件。 | `pi install npm:pi-ollama-cloud` |
| 226 | [pi-token-speed](https://pi.dev/packages/pi-token-speed?page=5) | 10,381/mo | extension | Pi 扩展，通过滑动窗口测量每秒 token 数（tokens per second）。 | `pi install npm:pi-token-speed` |
| 243 | [@router-for-me/pi-cliproxyapi-provider](https://pi.dev/packages/@router-for-me/pi-cliproxyapi-provider?page=5) | 9,428/mo | extension | Pi provider extension that auto-registers CLIProxyAPI models, plus TUI elapsed/TPS status | `pi install npm:@router-for-me/pi-cliproxyapi-provider` |
| 250 | [pi-dashscope-native](https://pi.dev/packages/pi-dashscope-native?page=5) | 9,180/mo | extension | Native Alibaba Cloud DashScope Qwen provider for Pi | `pi install npm:pi-dashscope-native` |
| 253 | [@oqtopus-team/pi-qcaleval](https://pi.dev/packages/@oqtopus-team/pi-qcaleval?page=6) | 8,972/mo | extension | pi extension that sends calibration plots to a calibration-evaluation VLM such as NVIDIA Ising-Calibration and returns a structured diagnosis | `pi install npm:@oqtopus-team/pi-qcaleval` |
| 259 | [@estebanforge/pi-antigravity-bridge](https://pi.dev/packages/@estebanforge/pi-antigravity-bridge?page=6) | 8,728/mo | extension | Gemini provider for Pi on the Antigravity ACP server (official Google ACP) or the stream-json agy CLI. Use antigravity/* models in Pi. Full /model picker support. Models runs Pi's tools. ToS safe to use. | `pi install npm:@estebanforge/pi-antigravity-bridge` |
| 261 | [@lucid-agents/pi-xgate](https://pi.dev/packages/@lucid-agents/pi-xgate?page=6) | 8,503/mo | package | Wallet-paid OpenAI and Anthropic inference through xgate for the Pi coding agent | `pi install npm:@lucid-agents/pi-xgate` |
| 262 | [@opencode/console](https://pi.dev/packages/@opencode/console?page=6) | 8,468/mo | package | Connect Claude Code, Pi, Codex, DeepSeek Harness and Hermes Agent to an OpenCode Console workspace and enforce its policies | `pi install npm:@opencode/console` |
| 270 | [omp-antigravity-acp-provider](https://pi.dev/packages/omp-antigravity-acp-provider?page=6) | 8,199/mo | extension | Google Antigravity ACP provider for Oh My Pi (OMP), with tool bridging and per-model thinking; derived from zacbemis/pi-antigravity-acp-provider | `pi install npm:omp-antigravity-acp-provider` |
| 275 | [pi-codex-token](https://pi.dev/packages/pi-codex-token?page=6) | 7,857/mo | extension | pi provider plugin: use gpt-5.5 on the OpenAI Codex backend via a personal access token (PAT), non-interactively. | `pi install npm:pi-codex-token` |
| 290 | [@nicknisi/pi-shared](https://pi.dev/packages/@nicknisi/pi-shared?page=6) | 7,376/mo | package | Shared helpers for Nick's pi extensions (one-off LLM provider access, TUI utilities) | `pi install npm:@nicknisi/pi-shared` |
| 292 | [@ravshansbox/pi-anthropic](https://pi.dev/packages/@ravshansbox/pi-anthropic?page=6) | 7,294/mo | extension | Anthropic system prompt sanitiser extension for pi | `pi install npm:@ravshansbox/pi-anthropic` |
| 300 | [not-enough-retry](https://pi.dev/packages/not-enough-retry?page=6) | 7,152/mo | extension | Make Pi's built-in retry catch every non-permanent provider error. | `pi install npm:not-enough-retry` |

### Agent 编排 / Subagent / Plan / Goal / Task

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 4 | [pi-subagents](https://pi.dev/packages/pi-subagents) | 1,015,050/mo | extension | 用于单代理委派和脚本化多代理工作流的 Pi 扩展 | `pi install npm:pi-subagents` |
| 14 | [@langchain/langsmith-pi-extension](https://pi.dev/packages/@langchain/langsmith-pi-extension) | 165,023/mo | package | 面向 Pi Coding Agent 的 LangSmith 扩展。 | `pi install npm:@langchain/langsmith-pi-extension` |
| 27 | [@tintinweb/pi-subagents](https://pi.dev/packages/@tintinweb/pi-subagents) | 86,578/mo | extension | 一个 pi 扩展，为 pi 带来类 Claude Code 的子代理与工作流编排：并行执行、实时组件、代理集群视图、自定义代理类型、运行中转向、动态工作流、Claude Code 兼容性以及整体外观与体验。 | `pi install npm:@tintinweb/pi-subagents` |
| 33 | [@getpipher/vision](https://pi.dev/packages/@getpipher/vision) | 70,413/mo | extension | Capability-aware vision + paste extension for the pi coding agent. Delegates image analysis to a vision model only when the active primary model is text-only; passes images through natively for multimodal models (zero delegation). | `pi install npm:@getpipher/vision` |
| 41 | [@explyt/ai-agent](https://pi.dev/packages/@explyt/ai-agent) | 48,271/mo | package | Explyt AI Agent: a terminal AI coding agent | `pi install npm:@explyt/ai-agent` |
| 47 | [pi-intercom](https://pi.dev/packages/pi-intercom) | 42,395/mo | package | <p> <img src="banner.png" alt="pi-intercom" width="1100"> </p> | `pi install npm:pi-intercom` |
| 49 | [@narumitw/pi-plan-mode](https://pi.dev/packages/@narumitw/pi-plan-mode) | 39,245/mo | extension | Pi 扩展，新增一个类似 Codex 的只读 /plan 协作模式。 | `pi install npm:@narumitw/pi-plan-mode` |
| 59 | [pi-goal-x](https://pi.dev/packages/pi-goal-x?page=2) | 35,124/mo | extension | pi 的目标模式扩展：持久的长期目标、五个模型工具、结构化任务、独立的完成审计、西西弗斯模式、自动继续和状态浮层。 | `pi install npm:pi-goal-x` |
| 72 | [@agimon-ai/po-workflow](https://pi.dev/packages/@agimon-ai/po-workflow?page=2) | 31,656/mo | extension | GitHub Actions-style workflow graphs, artifacts, recovery, and asynchronous runs for Po. | `pi install npm:@agimon-ai/po-workflow` |
| 74 | [@agimon-ai/po-team](https://pi.dev/packages/@agimon-ai/po-team?page=2) | 31,593/mo | package | Asynchronous named subagents, team runs, intercom, and model policy for Pi coding agents. | `pi install npm:@agimon-ai/po-team` |
| 78 | [@agimon-ai/po-plan](https://pi.dev/packages/@agimon-ai/po-plan?page=2) | 31,449/mo | extension | Reviewable Pi planning mode that removes file-editing tools and persists implementation plans. | `pi install npm:@agimon-ai/po-plan` |
| 79 | [@agimon-ai/po-runner-rtk-linux-x64](https://pi.dev/packages/@agimon-ai/po-runner-rtk-linux-x64?page=2) | 31,420/mo | package | Prebuilt RTK v0.45.0 log processor for Po Runner on Linux x64. | `pi install npm:@agimon-ai/po-runner-rtk-linux-x64` |
| 85 | [@narumitw/pi-goal](https://pi.dev/packages/@narumitw/pi-goal?page=2) | 31,294/mo | extension | Pi 扩展，用于通过 /goal 自主完成单一目标。 | `pi install npm:@narumitw/pi-goal` |
| 102 | [@agimon-ai/po-runner-rtk-linux-arm64](https://pi.dev/packages/@agimon-ai/po-runner-rtk-linux-arm64?page=3) | 30,550/mo | package | Prebuilt RTK v0.45.0 log processor for Po Runner on Linux arm64. | `pi install npm:@agimon-ai/po-runner-rtk-linux-arm64` |
| 105 | [@agimon-ai/po-runner-rtk-darwin-arm64](https://pi.dev/packages/@agimon-ai/po-runner-rtk-darwin-arm64?page=3) | 30,248/mo | package | Prebuilt RTK v0.45.0 log processor for Po Runner on macOS arm64. | `pi install npm:@agimon-ai/po-runner-rtk-darwin-arm64` |
| 107 | [@agimon-ai/po-runner-rtk-darwin-x64](https://pi.dev/packages/@agimon-ai/po-runner-rtk-darwin-x64?page=3) | 29,841/mo | package | Prebuilt RTK v0.45.0 log processor for Po Runner on macOS x64. | `pi install npm:@agimon-ai/po-runner-rtk-darwin-x64` |
| 124 | [pi-rtk-optimizer](https://pi.dev/packages/pi-rtk-optimizer?page=3) | 22,653/mo | extension | Pi 扩展，为编码代理优化 RTK 命令重写与工具输出压缩。 | `pi install npm:pi-rtk-optimizer` |
| 131 | [@akagilnc/pi-workflow-roles](https://pi.dev/packages/@akagilnc/pi-workflow-roles?page=3) | 20,292/mo | package | 面向 Pi 的灵魂绑定（soul-bound）工作流角色。 | `pi install npm:@akagilnc/pi-workflow-roles` |
| 134 | [agent-ste](https://pi.dev/packages/agent-ste?page=3) | 19,370/mo | extension | Simplified Technical English (ASD-STE100) enforcement for a coding agent. It gates a write, a commit message and a reply in pi and in Claude Code. | `pi install npm:agent-ste` |
| 136 | [@gotgenes/pi-subagents](https://pi.dev/packages/@gotgenes/pi-subagents?page=3) | 19,077/mo | extension | 面向 pi 的专注型进程内子代理核心——提供自主 AI 代理，以及供其他扩展构建的类型化 API 与生命周期事件。是 @tintinweb/pi-subagents 的友好分支（fork）。 | `pi install npm:@gotgenes/pi-subagents` |
| 144 | [pi-crew](https://pi.dev/packages/pi-crew?page=3) | 17,590/mo | package | Pi 扩展，用于协调 AI 团队、工作流、工作树以及异步任务编排 | `pi install npm:pi-crew` |
| 148 | [@injaneity/pi-computer-use](https://pi.dev/packages/@injaneity/pi-computer-use?page=3) | 16,775/mo | extension | Pi extension that lets AI agents observe and control macOS, Windows, and Linux apps. | `pi install npm:@injaneity/pi-computer-use` |
| 161 | [pi-extensible-workflows](https://pi.dev/packages/pi-extensible-workflows?page=4) | 14,728/mo | package | Deterministic multi-agent workflow orchestration and codemode scripts for Pi | `pi install npm:pi-extensible-workflows` |
| 167 | [@awebai/pi](https://pi.dev/packages/@awebai/pi?page=4) | 13,943/mo | extension | Lets your Pi communicate with other AI agents on an open network: send and receive messages, wake up the moment one arrives, and join agent teams. | `pi install npm:@awebai/pi` |
| 168 | [@piagent/platform](https://pi.dev/packages/@piagent/platform?page=4) | 13,927/mo | extension, skill, prompt | 面向 AI coding agent 的护栏：在工具调用执行前拦截密钥读取、破坏性命令和未经批准的 MCP 服务器。附带项目配置文件、能力锁定、上下文引擎和任务验证。 | `pi install npm:@piagent/platform` |
| 180 | [@nredd/pi-subagents](https://pi.dev/packages/@nredd/pi-subagents?page=4) | 12,708/mo | extension | A pi extension that brings Claude Code-like sub-agents and workflow orchestration to pi — parallel execution, live widget, fleet view, custom agent types, mid-run steering, dynamic workflows, Claude Code compatibility, look and feel. | `pi install npm:@nredd/pi-subagents` |
| 182 | [@nredd/pi-computer-use](https://pi.dev/packages/@nredd/pi-computer-use?page=4) | 12,616/mo | extension | Pi extension that lets AI agents observe and control macOS apps. | `pi install npm:@nredd/pi-computer-use` |
| 185 | [@cgh567/agent](https://pi.dev/packages/@cgh567/agent?page=4) | 12,481/mo | package | Helios 自我改进实验室。 | `pi install npm:@cgh567/agent` |
| 186 | [@nredd/pi-todo](https://pi.dev/packages/@nredd/pi-todo?page=4) | 12,397/mo | extension | Pi todo extension with a persistent overlay and plan-aware task tracking. | `pi install npm:@nredd/pi-todo` |
| 193 | [@nredd/pi-plan-mode](https://pi.dev/packages/@nredd/pi-plan-mode?page=4) | 11,780/mo | extension | Pi extension that adds a Codex-like read-only /plan collaboration mode. | `pi install npm:@nredd/pi-plan-mode` |
| 195 | [@cad0p/pi-subagents-tintinweb](https://pi.dev/packages/@cad0p/pi-subagents-tintinweb?page=4) | 11,702/mo | extension | A pi extension extension that brings smart Claude Code-style autonomous sub-agents to pi. | `pi install npm:@cad0p/pi-subagents-tintinweb` |
| 196 | [pi-herdr-agents](https://pi.dev/packages/pi-herdr-agents?page=4) | 11,630/mo | package | Asynchronous Pi subagents in Herdr, with optional isolated Git worktrees | `pi install npm:pi-herdr-agents` |
| 201 | [@kontextmind/kxm](https://pi.dev/packages/@kontextmind/kxm?page=5) | 11,455/mo | extension | KXM local-first multi-agent orchestration and operator dashboard | `pi install npm:@kontextmind/kxm` |
| 213 | [@schovest/pi-goal](https://pi.dev/packages/@schovest/pi-goal?page=5) | 11,131/mo | extension | Pi extension for autonomous single-objective /goal completion. | `pi install npm:@schovest/pi-goal` |
| 217 | [@geohar/pi-acp](https://pi.dev/packages/@geohar/pi-acp?page=5) | 10,958/mo | extension | ACP adapter for pi coding agent (fork), with a bundled pi extension for subagent→plan | `pi install npm:@geohar/pi-acp` |
| 221 | [atlas-project-harness](https://pi.dev/packages/atlas-project-harness?page=5) | 10,710/mo | extension | 践行 Project Harness 的全流程 AI 编程工作流治理引擎 | `pi install npm:atlas-project-harness` |
| 225 | [@astrosheep/square](https://pi.dev/packages/@astrosheep/square?page=5) | 10,406/mo | package | 一个共享的公共广场：代理们在此加入、获取动态、发表意见，并在完成后离开。 | `pi install npm:@astrosheep/square` |
| 245 | [pi-landstrip](https://pi.dev/packages/pi-landstrip?page=5) | 9,320/mo | extension | 面向 Pi 的沙箱化 Bash 与基于进程的 AI 代理。 | `pi install npm:pi-landstrip` |
| 248 | [@oqtopus-team/pi-qdash](https://pi.dev/packages/@oqtopus-team/pi-qdash?page=5) | 9,244/mo | extension | Pi extension for querying QDash via @oqtopus-team/qdash-client | `pi install npm:@oqtopus-team/pi-qdash` |
| 254 | [@a-t-h-i/bot-lobby](https://pi.dev/packages/@a-t-h-i/bot-lobby?page=6) | 8,927/mo | extension | Structured multi-agent software engineering orchestrator for Pi | `pi install npm:@a-t-h-i/bot-lobby` |
| 281 | [@parcha/agentrun-pi](https://pi.dev/packages/@parcha/agentrun-pi?page=6) | 7,576/mo | package | Pi extension for building, running and evaluating AgentRun workflows | `pi install npm:@parcha/agentrun-pi` |

### Context / Memory / Knowledge / Compaction

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 1 | [billion-context](https://pi.dev/packages/billion-context) | 3,965,753/mo | package | A context-compression plugin — small context windows (a 100K context is enough), 5x fewer tokens, month-long single sessions (billions of tokens), and compression quality — for all agents: pi, OpenCode, Codex, Claude Code, and more. billion-context is all | `pi install npm:billion-context` |
| 2 | [pi-mcp-adapter](https://pi.dev/packages/pi-mcp-adapter) | 2,401,610/mo | extension | 面向 Pi 编码代理的 MCP（Model Context Protocol）适配器扩展 | `pi install npm:pi-mcp-adapter` |
| 7 | [openwiki](https://pi.dev/packages/openwiki) | 329,862/mo | package | A CLI that uses a DeepAgents documentation agent to generate and maintain an OpenWiki for a codebase. | `pi install npm:openwiki` |
| 8 | [context-mode](https://pi.dev/packages/context-mode) | 226,275/mo | package | 可节省 98% 上下文窗口的 MCP 插件。兼容 Claude Code、Gemini CLI、VS Code Copilot、OpenCode 与 Codex CLI。提供沙箱代码执行、FTS5 知识库和意图驱动搜索。 | `pi install npm:context-mode` |
| 21 | [@opengsd/gsd-core](https://pi.dev/packages/@opengsd/gsd-core) | 93,554/mo | package | GSD Core is a meta-prompting, context engineering, and spec-driven development system for AI coding agents. | `pi install npm:@opengsd/gsd-core` |
| 22 | [pi-web-search](https://pi.dev/packages/pi-web-search) | 92,014/mo | extension | 面向 pi 的模型提供方原生网络搜索，覆盖 Google Gemini、OpenAI 和 Anthropic，并支持 Gemini URL Context。 | `pi install npm:pi-web-search` |
| 23 | [pi-memory](https://pi.dev/packages/pi-memory) | 91,922/mo | package | Pi 编码代理的记忆扩展，使用 qmd 驱动的语义搜索，跨日常日志、长期记忆和临时便笺检索。 | `pi install npm:pi-memory` |
| 52 | [@agentskit/doc-bridge](https://pi.dev/packages/@agentskit/doc-bridge?page=2) | 37,300/mo | package | 连接人类与 AI 代理的文档桥梁——确定性交接、文档站链接、记忆→文档，以及可选的 AgentsKit RAG/聊天。 | `pi install npm:@agentskit/doc-bridge` |
| 54 | [@agimon-ai/po-cache](https://pi.dev/packages/@agimon-ai/po-cache?page=2) | 35,702/mo | extension | Provider prompt cache policy and deterministic routing for Po | `pi install npm:@agimon-ai/po-cache` |
| 67 | [pi-deferred-context-engine](https://pi.dev/packages/pi-deferred-context-engine?page=2) | 33,399/mo | extension, skill | Run-scoped deferred tools, skills, blocked deny-list, and duplicate prompt context for Pi/OMP. | `pi install npm:pi-deferred-context-engine` |
| 104 | [pi-hermes-memory](https://pi.dev/packages/pi-hermes-memory?page=3) | 30,521/mo | extension, skill | 🧠 为 Pi 提供持久记忆 + 🔍 会话搜索 + 🛡️ 密钥扫描。默认采用感知 token 的纯策略记忆，支持 SQLite FTS5 搜索、自动整合与程序化技能。732 个测试，移植自 Hermes 代理。 | `pi install npm:pi-hermes-memory` |
| 106 | [@remnic/plugin-pi](https://pi.dev/packages/@remnic/plugin-pi?page=3) | 30,219/mo | package | 面向 Pi 编码代理的 Remnic 记忆扩展。 | `pi install npm:@remnic/plugin-pi` |
| 116 | [gentle-engram](https://pi.dev/packages/gentle-engram?page=3) | 25,518/mo | extension | Pi 代理的持久记忆——一个可本地或云端部署的大脑，跨会话、压缩和 MCP 代理共享。 | `pi install npm:gentle-engram` |
| 118 | [pi-context-view](https://pi.dev/packages/pi-context-view?page=3) | 24,987/mo | extension | Pi 扩展，用于可视化上下文使用情况并查看隐藏部分：基础提示词、工具定义和扩展注入。 | `pi install npm:pi-context-view` |
| 130 | [pi-open-tui](https://pi.dev/packages/pi-open-tui?page=3) | 20,419/mo | extension, theme | 面向 Pi 编码代理的精美 TUI：动态 logo 头部、Starship 风格底部栏、带模型元数据的圆角编辑器，以及提示框形式的用户消息。 | `pi install npm:pi-open-tui` |
| 150 | [pi-braid](https://pi.dev/packages/pi-braid?page=3) | 16,098/mo | extension, skill | 🥨 Braid - Metacognitive extension suite for pi coding agent: Adds memory, plan tracking, structured cognitive signals and completion checks on top of pi core loop, so long sessions keep their context and stop claiming unfinished work. | `pi install npm:pi-braid` |
| 153 | [pi-cache-optimizer](https://pi.dev/packages/pi-cache-optimizer?page=4) | 15,642/mo | package | 通过稳定的提示词、兼容 OpenAI 的缓存键、代理兼容性警告和底部缓存统计，提升 Pi 的提示词/KV 缓存命中率。 | `pi install npm:pi-cache-optimizer` |
| 155 | [@d3ara1n/pi-context-include](https://pi.dev/packages/@d3ara1n/pi-context-include?page=4) | 15,390/mo | extension | 为 AGENTS.md 提供 @path 语法——通过引用包含文件，并支持递归解析。 | `pi install npm:@d3ara1n/pi-context-include` |
| 165 | [pi-code](https://pi.dev/packages/pi-code?page=4) | 14,446/mo | extension, skill | 为 pi 编码代理带来 Claude Code 体验：读取你的 .claude 配置（规则、命令、技能包、钩子、输出样式、MCP 服务器、代理），并新增 todo、检查点、记忆、网页和子代理功能。 | `pi install npm:pi-code` |
| 169 | [@chankov/agent-fleet](https://pi.dev/packages/@chankov/agent-fleet?page=4) | 13,829/mo | extension, skill, prompt | Subagent orchestration for the pi coding agent — a thin dispatcher runs parallel subagents under a verification contract, keeping their output out of its context window. Multi-agent fleets, 15 personas, skills, herdr panes, peer coms, Hermes desktop. | `pi install npm:@chankov/agent-fleet` |
| 175 | [@maxiaochao/pi-toolkit](https://pi.dev/packages/@maxiaochao/pi-toolkit?page=4) | 13,261/mo | extension | Personal pi coding agent toolkit: background tasks, scheduler, /btw, /cache_export, apply_patch, browser automation, and bundled theme/skills. | `pi install npm:@maxiaochao/pi-toolkit` |
| 178 | [pi-blackhole](https://pi.dev/packages/pi-blackhole?page=4) | 12,894/mo | extension | Pi 的统一压缩 + 观察记忆扩展——压缩对话上下文，同时保留持久的观察与反思记录。 | `pi install npm:pi-blackhole` |
| 181 | [@nredd/pi-dev-tools](https://pi.dev/packages/@nredd/pi-dev-tools?page=4) | 12,670/mo | extension | Typed pi tools for git, ssh, Python (uv/ruff/ty/pytest) and Rust (cargo): compact structured results, explicit exit-code states, no-shell spawn, bounded output. | `pi install npm:@nredd/pi-dev-tools` |
| 203 | [billion-context-pi](https://pi.dev/packages/billion-context-pi?page=5) | 11,447/mo | package | 十亿，而非一百万。面向 Pi 编码代理的模型驱动上下文管理。 | `pi install npm:billion-context-pi` |
| 206 | [openlore](https://pi.dev/packages/openlore?page=5) | 11,266/mo | package | 面向 AI 编码代理的持久化架构记忆与结构化认知。 | `pi install npm:openlore` |
| 208 | [om-memory-system](https://pi.dev/packages/om-memory-system?page=5) | 11,260/mo | package | Opinionated modular memory system for coding agents (OpenCode, Pi and Claude Code) | `pi install npm:om-memory-system` |
| 214 | [@gyoungwe/pi-core](https://pi.dev/packages/@gyoungwe/pi-core?page=5) | 11,022/mo | package | Portable task, authorization, status, delivery and memory tools for native Pi | `pi install npm:@gyoungwe/pi-core` |
| 219 | [@gyoungwe/pi-knowledge](https://pi.dev/packages/@gyoungwe/pi-knowledge?page=5) | 10,848/mo | package | Knowledge and Vault tools for native Pi hosts | `pi install npm:@gyoungwe/pi-knowledge` |
| 223 | [pi-smart-compact](https://pi.dev/packages/pi-smart-compact?page=5) | 10,538/mo | extension | 面向 Pi Coding Agent、以验证为导向的智能压缩扩展——支持确定性提取、探索、综合、验证、指标统计与安全检查。 | `pi install npm:pi-smart-compact` |
| 229 | [@howaboua/pi-cache-hit-predictor](https://pi.dev/packages/@howaboua/pi-cache-hit-predictor?page=5) | 10,238/mo | extension | Predicts reusable prompt-cache prefixes when Pi switches model or reasoning lanes. | `pi install npm:@howaboua/pi-cache-hit-predictor` |
| 231 | [@spences10/pi-redact](https://pi.dev/packages/@spences10/pi-redact?page=5) | 10,087/mo | package | Tool-output redaction for Pi that replaces likely secrets before they reach the model context | `pi install npm:@spences10/pi-redact` |
| 232 | [pi-quiver](https://pi.dev/packages/pi-quiver?page=5) | 10,047/mo | package | Personal pack of Pi coding-agent extensions: context-safe fetch, doc_to_md PDF/DOCX/PPTX-to-Markdown conversion, session naming, a themed ASCII startup header, Anthropic fast mode, and a provider-stall watchdog. | `pi install npm:pi-quiver` |
| 238 | [pi-observational-memory](https://pi.dev/packages/pi-observational-memory?page=5) | 9,702/mo | extension | pi 的观察记忆扩展——采用缓存友好的分层压缩机制，支持观察与反思记录。 | `pi install npm:pi-observational-memory` |
| 242 | [pi-optchat](https://pi.dev/packages/pi-optchat?page=5) | 9,468/mo | extension | OptChat memory for Pi: persistent profiles, zoomable history, background agents, and conversation imports. | `pi install npm:pi-optchat` |
| 246 | [pi-posthorse](https://pi.dev/packages/pi-posthorse?page=5) | 9,316/mo | extension | Posthorse: fresh context, same journey. No-summary context rollover for Pi, with sparse budget reminders, handoffs, notes, and history. | `pi install npm:pi-posthorse` |
| 256 | [pi-maestro-flow](https://pi.dev/packages/pi-maestro-flow?page=6) | 8,848/mo | skill | 面向 Pi 编码代理的一体化多代理编排 —— 单次安装即可获得并行队友调度、目标、计划、知识系统、MCP/LSP/浏览器与驾驶舱可视化 | `pi install npm:pi-maestro-flow` |
| 267 | [pi-subdir-context](https://pi.dev/packages/pi-subdir-context?page=6) | 8,407/mo | extension | Automatically load AGENTS.md context from subdirectories in pi coding agent | `pi install npm:pi-subdir-context` |
| 269 | [pi-jev-compaction](https://pi.dev/packages/pi-jev-compaction?page=6) | 8,374/mo | package | Pi Coding Agent extension that replaces LLM-summary compaction with TypeSafe Jev keep/drop/truncate decisions. | `pi install npm:pi-jev-compaction` |
| 276 | [@geohar/pi-cribsheet](https://pi.dev/packages/@geohar/pi-cribsheet?page=6) | 7,834/mo | extension | Pi extension: run the crib (cribsheet) memory + code-index MCP server via sharedserver, inject the reach-for-crib directive, and ship the /crib recall command. Pairs with pi-mcp-adapter. | `pi install npm:@geohar/pi-cribsheet` |
| 294 | [agent-qa](https://pi.dev/packages/agent-qa?page=6) | 7,265/mo | skill | The self-improving Agentic QA harness with Memory | `pi install npm:agent-qa` |

### UI / TUI / Session / 观测

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 15 | [glimpseui](https://pi.dev/packages/glimpseui) | 151,684/mo | prompt | 面向脚本和 AI 代理的原生微 UI——提供跨平台 WebView 窗口与双向 JSON 通信。 | `pi install npm:glimpseui` |
| 29 | [@juicesharp/rpiv-todo](https://pi.dev/packages/@juicesharp/rpiv-todo) | 82,906/mo | extension | Pi 扩展：为模型提供待办事项列表，以实时浮层渲染，且 /reload 与会话压缩后依然保留。 | `pi install npm:@juicesharp/rpiv-todo` |
| 34 | [@agimon-ai/po-config](https://pi.dev/packages/@agimon-ai/po-config) | 58,023/mo | package | Typed configuration loading, validation, and host services for composing Po sessions. | `pi install npm:@agimon-ai/po-config` |
| 42 | [@agimon-ai/po-minor-mode](https://pi.dev/packages/@agimon-ai/po-minor-mode) | 45,654/mo | extension | Minor-mode ownership, catalog, commands, and session lifecycle. | `pi install npm:@agimon-ai/po-minor-mode` |
| 48 | [@agimon-ai/po-ui](https://pi.dev/packages/@agimon-ai/po-ui) | 42,182/mo | extension | Leader-key menus, themes, and TUI components for Po and Pi extensions. | `pi install npm:@agimon-ai/po-ui` |
| 50 | [@agimon-ai/po-session](https://pi.dev/packages/@agimon-ai/po-session) | 37,932/mo | extension | Shared session coordination services for Po. | `pi install npm:@agimon-ai/po-session` |
| 51 | [pi-btw](https://pi.dev/packages/pi-btw?page=2) | 37,449/mo | extension | 一个 pi 扩展，通过 /btw 进行并行的旁路对话 | `pi install npm:pi-btw` |
| 55 | [@agimon-ai/po-notification](https://pi.dev/packages/@agimon-ai/po-notification?page=2) | 35,438/mo | extension | Desktop notifications and an animated shell-tab title for Po sessions. | `pi install npm:@agimon-ai/po-notification` |
| 56 | [@agimon-ai/po-autostop](https://pi.dev/packages/@agimon-ai/po-autostop?page=2) | 35,287/mo | extension | Shuts a Po session down once the agent settles and stays idle. | `pi install npm:@agimon-ai/po-autostop` |
| 58 | [pi-powerline-footer](https://pi.dev/packages/pi-powerline-footer?page=2) | 35,168/mo | extension | 面向 pi 编码代理的 Powerline 风格状态栏扩展。 | `pi install npm:pi-powerline-footer` |
| 63 | [@agimon-ai/po-profile](https://pi.dev/packages/@agimon-ai/po-profile?page=2) | 34,593/mo | extension | Persona and environment profile switching for Po sessions. | `pi install npm:@agimon-ai/po-profile` |
| 73 | [@agimon-ai/po-voice](https://pi.dev/packages/@agimon-ai/po-voice?page=2) | 31,621/mo | extension | Client audio capture, host transcription, and autonomous narration for Pi agents. | `pi install npm:@agimon-ai/po-voice` |
| 76 | [@agimon-ai/po-task](https://pi.dev/packages/@agimon-ai/po-task?page=2) | 31,489/mo | package | Persistent, dependency-aware task graphs and subagent delegation for Pi coding sessions. | `pi install npm:@agimon-ai/po-task` |
| 80 | [@agimon-ai/po-computer-use](https://pi.dev/packages/@agimon-ai/po-computer-use?page=2) | 31,410/mo | extension | Session scoped semantic computer control through the Po Desktop capability. | `pi install npm:@agimon-ai/po-computer-use` |
| 81 | [@agimon-ai/po-git](https://pi.dev/packages/@agimon-ai/po-git?page=2) | 31,357/mo | extension | Git worktree sessions for Po: spawn an isolated worktree with its own session and manage it from the parent | `pi install npm:@agimon-ai/po-git` |
| 84 | [@agimon-ai/po-log](https://pi.dev/packages/@agimon-ai/po-log?page=2) | 31,309/mo | extension | Session metrics, findings, and sink status for headless agent observability. | `pi install npm:@agimon-ai/po-log` |
| 94 | [@agimon-ai/po-style-system](https://pi.dev/packages/@agimon-ai/po-style-system?page=2) | 30,989/mo | package | Optional Po story preview integration for the style-system package. | `pi install npm:@agimon-ai/po-style-system` |
| 96 | [@agimon-ai/po-user-feedback](https://pi.dev/packages/@agimon-ai/po-user-feedback?page=2) | 30,859/mo | extension | Structured user questions with interactive and autonomous Voice handoff for Pi agents. | `pi install npm:@agimon-ai/po-user-feedback` |
| 108 | [@agimon-ai/po-major-mode](https://pi.dev/packages/@agimon-ai/po-major-mode?page=3) | 29,769/mo | extension | Named major-mode selection and layer composition switching for Po sessions. | `pi install npm:@agimon-ai/po-major-mode` |
| 111 | [pi-coding-agent-test](https://pi.dev/packages/pi-coding-agent-test?page=3) | 28,975/mo | package | Deterministic end-to-end testing for Pi Coding Agent extensions, tools, sessions, and TUI output. | `pi install npm:pi-coding-agent-test` |
| 112 | [pi-cc-extensions](https://pi.dev/packages/pi-cc-extensions?page=3) | 28,822/mo | extension | 一套 Pi 效率增强套件，提供 Claude Code 风格 UI、上下文检查以及代理/会话引用。 | `pi install npm:pi-cc-extensions` |
| 117 | [pi-straw-boss](https://pi.dev/packages/pi-straw-boss?page=3) | 25,451/mo | extension | Straw Boss coordination for pi in Herdr: sessions join a tab's net by choice, the first joiner is its main agent, a workspace tower opens on demand with a live monitoring dashboard, and boss_broadcast reaches the rest | `pi install npm:pi-straw-boss` |
| 126 | [@raindrop-ai/pi-agent](https://pi.dev/packages/@raindrop-ai/pi-agent?page=3) | 21,341/mo | package | 为 Pi Agent 提供 Raindrop 可观测性——通过 subscriber 或 pi-coding-agent 扩展实现自动追踪。 | `pi install npm:@raindrop-ai/pi-agent` |
| 135 | [pi-farm](https://pi.dev/packages/pi-farm?page=3) | 19,082/mo | package | tmux session manager for pi agents — YAML config, reboot autostart, cron, todo panel, and sessions on other machines over ssh | `pi install npm:pi-farm` |
| 149 | [pi-ask-user](https://pi.dev/packages/pi-ask-user?page=3) | 16,737/mo | extension | 面向 pi-coding-agent 的交互式 ask_user 工具，提供可搜索的分栏选择 UI、多选与自由文本输入。 | `pi install npm:pi-ask-user` |
| 152 | [@abelxiaoxing/cadence](https://pi.dev/packages/@abelxiaoxing/cadence?page=4) | 15,662/mo | package | Conversation-driven Pi workspace: persistent native and WebUI workflows, explicit plan approval, checks and local delivery. | `pi install npm:@abelxiaoxing/cadence` |
| 157 | [@fitchmultz/pi-subagents](https://pi.dev/packages/@fitchmultz/pi-subagents?page=4) | 15,219/mo | package | Pi extension for subagent orchestration and local session coordination | `pi install npm:@fitchmultz/pi-subagents` |
| 159 | [@workit-dev/pi](https://pi.dev/packages/@workit-dev/pi?page=4) | 14,946/mo | extension | Workit native extension for Pi — tools, method skills, and session continuity | `pi install npm:@workit-dev/pi` |
| 183 | [@nredd/pi-preset](https://pi.dev/packages/@nredd/pi-preset?page=4) | 12,593/mo | package | Shared Pi specialist agents and workflow skills, with an optional expanded footer, themes, and public-safe settings defaults. | `pi install npm:@nredd/pi-preset` |
| 202 | [@langfuse/pi-observability-plugin](https://pi.dev/packages/@langfuse/pi-observability-plugin?page=5) | 11,454/mo | extension | Langfuse observability extension for the pi coding agent — traces prompts, agent turns, model generations, and tool calls to Langfuse. | `pi install npm:@langfuse/pi-observability-plugin` |
| 212 | [@ravshansbox/pi-statusline](https://pi.dev/packages/@ravshansbox/pi-statusline?page=5) | 11,146/mo | extension | Statusline and prompt history extension for pi | `pi install npm:@ravshansbox/pi-statusline` |
| 235 | [pi-zentui](https://pi.dev/packages/pi-zentui?page=5) | 9,917/mo | extension, theme | 灵感源自 Starship 的状态行与 Opencode 风格 TUI，适用于 Pi。 | `pi install npm:pi-zentui` |
| 252 | [pi-better-subagents](https://pi.dev/packages/pi-better-subagents?page=6) | 9,170/mo | extension | Pi extension for detached, sandboxed subagent runs that keep the foreground session free. | `pi install npm:pi-better-subagents` |
| 265 | [pi-interactive-shell](https://pi.dev/packages/pi-interactive-shell?page=6) | 8,435/mo | extension | 在 pi 的 TUI 覆盖层中运行 AI 编码代理，支持交互式、免手动及分派式监督。 | `pi install npm:pi-interactive-shell` |
| 291 | [@juicesharp/rpiv-btw](https://pi.dev/packages/@juicesharp/rpiv-btw?page=6) | 7,324/mo | extension | Pi 扩展。/btw 斜杠命令，用于向同一个主模型提出一次性附带问题，而不污染主对话。 | `pi install npm:@juicesharp/rpiv-btw` |

### Skills / Prompt / Rules / 提问

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 12 | [@juicesharp/rpiv-ask-user-question](https://pi.dev/packages/@juicesharp/rpiv-ask-user-question) | 180,645/mo | extension | Pi 扩展：当模型只能靠猜测时，它可以向你提出一份结构化问卷，用带类型的选项代替自由文本回答。 | `pi install npm:@juicesharp/rpiv-ask-user-question` |
| 13 | [@dietrichgebert/ponytail](https://pi.dev/packages/@dietrichgebert/ponytail) | 170,730/mo | skill | 面向 AI 代理的『懒人资深开发』模式。最好的代码就是你从未写过的代码。 | `pi install npm:@dietrichgebert/ponytail` |
| 18 | [@juicesharp/rpiv-i18n](https://pi.dev/packages/@juicesharp/rpiv-i18n) | 102,947/mo | extension | Pi 扩展。rpiv-* 技能包的本地化基础：区域设置检测、/languages 命令、--locale 标志以及跨包的区域设置注册表。 | `pi install npm:@juicesharp/rpiv-i18n` |
| 24 | [pi-advisor-flow](https://pi.dev/packages/pi-advisor-flow) | 89,425/mo | extension | Advanced Executor/Advisor flow for Pi, fully configurable and extendable. | `pi install npm:pi-advisor-flow` |
| 37 | [@mutmutco/pi-plugin](https://pi.dev/packages/@mutmutco/pi-plugin) | 53,019/mo | package | 提供 MMI 工作流技能包与 org 门控交付。 | `pi install npm:@mutmutco/pi-plugin` |
| 83 | [@agimon-ai/po-model-guidance](https://pi.dev/packages/@agimon-ai/po-model-guidance?page=2) | 31,321/mo | extension | Per-model system prompt guidance for Pi agents, layered across global and repository scope. | `pi install npm:@agimon-ai/po-model-guidance` |
| 86 | [@agimon-ai/po-prompt](https://pi.dev/packages/@agimon-ai/po-prompt?page=2) | 31,265/mo | extension | Staged recent prompts and saved prompt templates for Po | `pi install npm:@agimon-ai/po-prompt` |
| 91 | [@agimon-ai/po-help](https://pi.dev/packages/@agimon-ai/po-help?page=2) | 31,114/mo | extension, skill | Activation-gated package guidance and help skills for Po and Pi extensions. | `pi install npm:@agimon-ai/po-help` |
| 99 | [pi-prompt-template-model](https://pi.dev/packages/pi-prompt-template-model?page=2) | 30,657/mo | extension, prompt | 面向 pi 编码代理的提示词模板模型选择扩展。 | `pi install npm:pi-prompt-template-model` |
| 103 | [@howaboua/pi-codex-conversion](https://pi.dev/packages/@howaboua/pi-codex-conversion?page=3) | 30,530/mo | extension | 面向 pi 编码代理的 Codex 导向工具与提示词适配器。 | `pi install npm:@howaboua/pi-codex-conversion` |
| 121 | [@narumitw/pi-btw](https://pi.dev/packages/@narumitw/pi-btw?page=3) | 23,959/mo | extension | Pi 扩展，新增一个 /btw 顺带提问命令。 | `pi install npm:@narumitw/pi-btw` |
| 125 | [pi-gauntlet](https://pi.dev/packages/pi-gauntlet?page=3) | 22,498/mo | skill | 为 pi 编码代理提供有主张、带门控的工作流技能包、子代理人设和运行时扩展。 | `pi install npm:pi-gauntlet` |
| 128 | [pi-interview](https://pi.dev/packages/pi-interview?page=3) | 20,926/mo | extension | 面向 pi 编码代理的交互式访谈表单扩展。 | `pi install npm:pi-interview` |
| 139 | [@astrofoundry/pi-astro](https://pi.dev/packages/@astrofoundry/pi-astro?page=3) | 18,738/mo | package | Personal pi customizations (extensions, subagents, skills, prompts, themes) for the pi coding agent. | `pi install npm:@astrofoundry/pi-astro` |
| 140 | [bigpowers](https://pi.dev/packages/bigpowers?page=3) | 18,499/mo | skill | 73 个代理技能，将 17 年的软件工程纪律凝练为一套面向独立开发者的规范性方法论。 | `pi install npm:bigpowers` |
| 143 | [projectops](https://pi.dev/packages/projectops?page=3) | 17,662/mo | package | One npx install for GitHub release automation: semantic versioning, changelogs, release PRs, CI/CD workflows and AI agent skills | `pi install npm:projectops` |
| 204 | [@howaboua/pi-better-skills-tool](https://pi.dev/packages/@howaboua/pi-better-skills-tool?page=5) | 11,426/mo | extension, skill | Progressive skill discovery for Pi, Code Mode and Notebook Mode. | `pi install npm:@howaboua/pi-better-skills-tool` |
| 234 | [@juicesharp/rpiv-workflow](https://pi.dev/packages/@juicesharp/rpiv-workflow?page=5) | 9,996/mo | extension, skill | Pi 扩展。将技能包串联成带类型的多阶段工作流，具备可审计的 JSONL 状态、谓词路由和逐阶段输出验证。与技能包无关——可自带技能包。 | `pi install npm:@juicesharp/rpiv-workflow` |
| 241 | [@devflow-tools/claude-code-plugin](https://pi.dev/packages/@devflow-tools/claude-code-plugin?page=5) | 9,593/mo | skill | 面向 DevFlow 开发智能运行时的 Claude Code hooks 与技能包（skills）。 | `pi install npm:@devflow-tools/claude-code-plugin` |
| 255 | [@juicesharp/rpiv-advisor](https://pi.dev/packages/@juicesharp/rpiv-advisor?page=6) | 8,863/mo | extension | Pi 扩展。模型在行动之前，可以向更强的评审模型征求第二意见。 | `pi install npm:@juicesharp/rpiv-advisor` |
| 274 | [pi-schedule-prompt](https://pi.dev/packages/pi-schedule-prompt?page=6) | 7,873/mo | extension, prompt | Pi's Heartbeat - A pi extension for scheduling recurring and one-shot main agent or background prompts with cron-like functionality | `pi install npm:pi-schedule-prompt` |
| 288 | [@1aboveio/cicd-skills](https://pi.dev/packages/@1aboveio/cicd-skills?page=6) | 7,423/mo | skill | GitHub Actions and flow, Mergify, Docker and Podman, Cloud Build, Cloud Deploy and Google Cloud. | `pi install npm:@1aboveio/cicd-skills` |
| 289 | [bestony-pi-preset](https://pi.dev/packages/bestony-pi-preset?page=6) | 7,392/mo | extension, skill, theme, prompt | Bestony 的个人 Pi 编码代理预设——包含技能包、扩展、提示词和主题。 | `pi install npm:bestony-pi-preset` |

### Runtime / 后台任务 / Worktree / 集成

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 26 | [@agimon-ai/po-core](https://pi.dev/packages/@agimon-ai/po-core) | 87,223/mo | package | Po runtime systems and reusable core services. | `pi install npm:@agimon-ai/po-core` |
| 38 | [confluence-cli](https://pi.dev/packages/confluence-cli) | 52,768/mo | package | 面向 Atlassian Confluence 的命令行界面，具备页面创建与编辑能力。 | `pi install npm:confluence-cli` |
| 45 | [pi-fabric](https://pi.dev/packages/pi-fabric) | 43,989/mo | extension | 面向 Pi 的可编程工具与代理运行时。 | `pi install npm:pi-fabric` |
| 71 | [@agimon-ai/po-runner](https://pi.dev/packages/@agimon-ai/po-runner?page=2) | 31,722/mo | package | Supervised shell execution, background process control, and run logs for Pi coding agents. | `pi install npm:@agimon-ai/po-runner` |
| 75 | [@agimon-ai/po-runner-rmux-linux-x64](https://pi.dev/packages/@agimon-ai/po-runner-rmux-linux-x64?page=2) | 31,576/mo | package | Prebuilt RMUX runtime for Po Runner on Linux x64. | `pi install npm:@agimon-ai/po-runner-rmux-linux-x64` |
| 77 | [pi-background-tasks](https://pi.dev/packages/pi-background-tasks?page=2) | 31,480/mo | extension | Pi 扩展：支持持久的后台 shell 任务、只读委托代理、本地认证的 Pi 运行，以及通过子 Pi 进程运行的固定用途 Fusion 工作流。 | `pi install npm:pi-background-tasks` |
| 87 | [@undefineds.co/models](https://pi.dev/packages/@undefineds.co/models?page=2) | 31,220/mo | package | `@undefineds.co/models` 是面向 LinX 应用、桌面端、CLI、边车组件及未来 worker 的共享 Solid Pod 数据模型契约。 | `pi install npm:@undefineds.co/models` |
| 97 | [@agimon-ai/po-runner-rmux-linux-arm64](https://pi.dev/packages/@agimon-ai/po-runner-rmux-linux-arm64?page=2) | 30,786/mo | package | Prebuilt RMUX runtime for Po Runner on Linux arm64. | `pi install npm:@agimon-ai/po-runner-rmux-linux-arm64` |
| 100 | [@agimon-ai/po-runner-rmux-darwin-x64](https://pi.dev/packages/@agimon-ai/po-runner-rmux-darwin-x64?page=2) | 30,649/mo | package | Prebuilt RMUX runtime for Po Runner on macOS x64. | `pi install npm:@agimon-ai/po-runner-rmux-darwin-x64` |
| 109 | [@agimon-ai/po-runner-rmux-darwin-arm64](https://pi.dev/packages/@agimon-ai/po-runner-rmux-darwin-arm64?page=3) | 29,769/mo | package | Prebuilt RMUX runtime for Po Runner on macOS arm64. | `pi install npm:@agimon-ai/po-runner-rmux-darwin-arm64` |
| 146 | [@xynogen/pix-runtime](https://pi.dev/packages/@xynogen/pix-runtime?page=3) | 17,063/mo | extension | Pix 共享运行时 —— 带版本号的 pix.json 配置、原子化持久化、类型化变更事件 | `pi install npm:@xynogen/pix-runtime` |
| 154 | [pi-dev-flow](https://pi.dev/packages/pi-dev-flow?page=4) | 15,570/mo | extension | Enforced feature workflow for Pi: plan → implement → pre-release → release, gated checkpoints, self-improvement reflections, one git worktree per feature, changelog + publish as part of the release | `pi install npm:pi-dev-flow` |
| 162 | [@llblab/pi-telegram](https://pi.dev/packages/@llblab/pi-telegram?page=4) | 14,708/mo | extension | 面向 Pi 的 Telegram 运行时适配器。 | `pi install npm:@llblab/pi-telegram` |
| 166 | [pi-until-loop](https://pi.dev/packages/pi-until-loop?page=4) | 14,183/mo | package | Spend your time on the engineering trade-offs that matter. Let the Until Loop make sure your agents deliver what you want, how you want it. | `pi install npm:pi-until-loop` |
| 190 | [@fro.bot/systematic](https://pi.dev/packages/@fro.bot/systematic?page=4) | 12,178/mo | package | Compound-engineering loops for OpenCode, Pi, and Claude Code | `pi install npm:@fro.bot/systematic` |
| 200 | [pi-herdsman](https://pi.dev/packages/pi-herdsman?page=4) | 11,474/mo | extension | Asynchronous Pi subagents and agent fleet orchestration for parallel coding agents with nested delegation, background work, and supervision in herdr. | `pi install npm:pi-herdsman` |
| 240 | [@amaster.ai/pi-computer-use](https://pi.dev/packages/@amaster.ai/pi-computer-use?page=5) | 9,625/mo | extension | 面向 Pi 桌面自动化的跨平台 computer-use（计算机操作）工具 | `pi install npm:@amaster.ai/pi-computer-use` |
| 251 | [@trevonistrevon/pi-loop](https://pi.dev/packages/@trevonistrevon/pi-loop?page=6) | 9,177/mo | extension | Pi 扩展，支持基于 cron/事件的代理重新唤醒循环与后台进程监控。 | `pi install npm:@trevonistrevon/pi-loop` |
| 257 | [pi-warden](https://pi.dev/packages/pi-warden?page=6) | 8,821/mo | extension | Makes the Pi agent follow your project's rules. Jev judges every write against your pi-warden.md and quotes the broken rule back to the agent, names slop, breaks stuck loops, calls out unverified done claims, compresses large tool output, and holds the ra | `pi install npm:pi-warden` |
| 272 | [@tmustier/pi-ralph-wiggum](https://pi.dev/packages/@tmustier/pi-ralph-wiggum?page=6) | 8,098/mo | package | Long-running agent loops for iterative development in Pi. | `pi install npm:@tmustier/pi-ralph-wiggum` |
| 278 | [@pi-unipi/core](https://pi.dev/packages/@pi-unipi/core?page=6) | 7,790/mo | extension | 面向 Unipi 扩展套件的共享工具、事件类型和常量 | `pi install npm:@pi-unipi/core` |
| 280 | [pi-squire](https://pi.dev/packages/pi-squire?page=6) | 7,758/mo | extension | Run background Pi delegates in tmux, Herdr, Rex or Paseo, get results back, and isolate checkouts with optional managed worktrees | `pi install npm:pi-squire` |
| 298 | [@agimon-ai/po-backdrop-bamboo](https://pi.dev/packages/@agimon-ai/po-backdrop-bamboo?page=6) | 7,213/mo | package | Po's default background: Po the panda in the bamboo, painted in ink on silk, on the active theme's own surface. | `pi install npm:@agimon-ai/po-backdrop-bamboo` |

### 代码智能 / 编辑 / Review

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 17 | [pi-lens](https://pi.dev/packages/pi-lens) | 114,621/mo | extension | 面向 pi 的实时代码反馈——LSP、linter、格式化工具、类型检查、结构分析与 booboo | `pi install npm:pi-lens` |
| 19 | [pi-simplify](https://pi.dev/packages/pi-simplify) | 101,610/mo | extension | 一个 Pi 扩展，用于审查最近改动的代码，以提升其清晰度、一致性和可维护性。 | `pi install npm:pi-simplify` |
| 20 | [@plannotator/pi-extension](https://pi.dev/packages/@plannotator/pi-extension) | 98,484/mo | package | Plannotator Pi 扩展：支持带注释的交互式计划审查、为代理消息添加注释，以及审查代码/PR。 | `pi install npm:@plannotator/pi-extension` |
| 36 | [gentle-pi](https://pi.dev/packages/gentle-pi) | 55,241/mo | package | 将 Pi 变成 el Gentleman：一个资深架构师级的开发框架，具备 SDD/OpenSpec、子代理、严格的 TDD 证据、审查护栏和技能包发现能力。 | `pi install npm:gentle-pi` |
| 43 | [@heyhuynhgiabuu/pi-pretty](https://pi.dev/packages/@heyhuynhgiabuu/pi-pretty) | 44,711/mo | extension | 让 pi 的终端输出更美观——语法高亮的文件读取、彩色 bash 输出、树状目录列表等。 | `pi install npm:@heyhuynhgiabuu/pi-pretty` |
| 44 | [@agimon-ai/po-hashline](https://pi.dev/packages/@agimon-ai/po-hashline) | 44,393/mo | package | Shared snapshot-bound file tags and line anchors for Po tools. | `pi install npm:@agimon-ai/po-hashline` |
| 82 | [@agimon-ai/po-grep](https://pi.dev/packages/@agimon-ai/po-grep?page=2) | 31,329/mo | extension | Snapshot-bound hashline grep for Pi and Po. | `pi install npm:@agimon-ai/po-grep` |
| 90 | [@agimon-ai/po-author](https://pi.dev/packages/@agimon-ai/po-author?page=2) | 31,127/mo | extension | Visual steering workspace for focused document review and bounded authoring | `pi install npm:@agimon-ai/po-author` |
| 92 | [@agimon-ai/po-file-edit](https://pi.dev/packages/@agimon-ai/po-file-edit?page=2) | 31,058/mo | extension | Native Po session-scoped file-change timelines, review APIs, and cross-agent edit presence. | `pi install npm:@agimon-ai/po-file-edit` |
| 93 | [@agimon-ai/po-edit](https://pi.dev/packages/@agimon-ai/po-edit?page=2) | 30,998/mo | extension | Snapshot-bound hashline edit tool for Pi and Po. | `pi install npm:@agimon-ai/po-edit` |
| 101 | [@agimon-ai/po-read](https://pi.dev/packages/@agimon-ai/po-read?page=3) | 30,562/mo | extension | Snapshot-bound hashline read tool for Pi and Po. | `pi install npm:@agimon-ai/po-read` |
| 188 | [pi-hashline-edit-pro](https://pi.dev/packages/pi-hashline-edit-pro?page=4) | 12,323/mo | extension | 适用于 pi-coding-agent 的哈希锚定 read/replace/insert/grep 工具：每一行都会获得唯一的 3 字符哈希（A-Za-z0-9），且跨编辑保持稳定；过期或有歧义的锚点会被拒绝，绝不模糊匹配。撤销记录在重启后依然保留。 | `pi install npm:pi-hashline-edit-pro` |
| 205 | [pi-orchestrator-config](https://pi.dev/packages/pi-orchestrator-config?page=5) | 11,347/mo | package | Orchestrator pattern for pi: specialist subagents, enforcement, code review loop, workflow commands | `pi install npm:pi-orchestrator-config` |
| 224 | [@sassywares/skills](https://pi.dev/packages/@sassywares/skills?page=5) | 10,514/mo | skill | Lean, explicit-invocation Agent Skills for shipping fast: plan, work, review, validate, ship. | `pi install npm:@sassywares/skills` |
| 236 | [pi-tidy](https://pi.dev/packages/pi-tidy?page=5) | 9,828/mo | extension | Tool folding for the pi agent — a reply's tool calls collapse to one clickable line; failures, edit diffs and running jobs stay visible | `pi install npm:pi-tidy` |
| 237 | [@narumitw/pi-lsp](https://pi.dev/packages/@narumitw/pi-lsp?page=5) | 9,778/mo | extension | Pi 扩展，通过共享的 runner 提供可配置、语言无关的 LSP 工具。 | `pi install npm:@narumitw/pi-lsp` |
| 271 | [@introspection-ai/operator](https://pi.dev/packages/@introspection-ai/operator?page=6) | 8,102/mo | package | The Introspection Operator: a Recipe and skills that build an agent with its owner (brainstorm, draft and review). | `pi install npm:@introspection-ai/operator` |
| 277 | [@runkids/figlens](https://pi.dev/packages/@runkids/figlens?page=6) | 7,828/mo | package | Give your coding agent the design details to build, compare and follow changes from a saved Figma .fig: layout, text, variables, assets, reference renders, screenshot comparison and revision diffs. Offline: no Dev Mode seat, login or API quota. Pi, OpenCo | `pi install npm:@runkids/figlens` |
| 284 | [pi-claude-code-ui](https://pi.dev/packages/pi-claude-code-ui?page=6) | 7,488/mo | extension | Claude Code style UI for pi: one-line tool groups, syntax-highlighted diffs, an activity spinner, and colors from your terminal theme | `pi install npm:pi-claude-code-ui` |
| 297 | [@1aboveio/engineering-skills](https://pi.dev/packages/@1aboveio/engineering-skills?page=6) | 7,221/mo | skill | Issue-to-PR and release orchestrators, review, coverage, golden paths and test quality. | `pi install npm:@1aboveio/engineering-skills` |
| 299 | [@1aboveio/core-skills](https://pi.dev/packages/@1aboveio/core-skills?page=6) | 7,195/mo | skill | Shared writing and document foundation: house style, plain-language replies, editorial review, Chinese polish, terminology, write-doc, write-report, distill-writing, doc-to-md and reg-parser. | `pi install npm:@1aboveio/core-skills` |

### 安全 / 权限 / Sandbox

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 9 | [cc-safety-net](https://pi.dev/packages/cc-safety-net) | 200,702/mo | package | 编码代理 CLI 钩子：阻止破坏性命令与机密文件访问。 | `pi install npm:cc-safety-net` |
| 10 | [pi-deltabox](https://pi.dev/packages/pi-deltabox) | 191,452/mo | package | Pi extension: agent-native sandbox sessions with diff/commit/abort, powered by deltabox-lite | `pi install npm:pi-deltabox` |
| 28 | [@agimon-ai/po-web-security](https://pi.dev/packages/@agimon-ai/po-web-security) | 85,672/mo | package | Shared security primitives for the Po web cockpit: sealed channels and signed bundle manifests for independently trusted verifiers. | `pi install npm:@agimon-ai/po-web-security` |
| 39 | [@gotgenes/pi-permission-system](https://pi.dev/packages/@gotgenes/pi-permission-system) | 51,089/mo | extension | 面向 Pi 编码代理的权限强制扩展。 | `pi install npm:@gotgenes/pi-permission-system` |
| 61 | [@agimon-ai/po-sandbox](https://pi.dev/packages/@agimon-ai/po-sandbox?page=2) | 35,001/mo | extension | Per-workspace sandbox containers for Po: the container provider, the shared image, the container lifecycle, and a host credential broker | `pi install npm:@agimon-ai/po-sandbox` |
| 95 | [@agimon-ai/po-network](https://pi.dev/packages/@agimon-ai/po-network?page=2) | 30,919/mo | package | Host-neutral network election core and deterministic safety simulator. | `pi install npm:@agimon-ai/po-network` |
| 113 | [latchkey](https://pi.dev/packages/latchkey?page=3) | 27,207/mo | package | 一个 CLI 工具，可将 API 凭据注入到发往第三方服务的 curl 请求中。 | `pi install npm:latchkey` |
| 119 | [betterwright](https://pi.dev/packages/betterwright?page=3) | 24,901/mo | package | 面向 AI 代理的持久化、受策略保护的 Playwright 浏览器，具备网络控制、可信凭据自动填充、证据截图和 CAPTCHA 辅助功能。 | `pi install npm:betterwright` |
| 172 | [@cortexkit/pi-antigravity-auth](https://pi.dev/packages/@cortexkit/pi-antigravity-auth?page=4) | 13,547/mo | package | Google Antigravity OAuth extension for pi - access Gemini and Claude models using Google credentials | `pi install npm:@cortexkit/pi-antigravity-auth` |
| 187 | [pi-better-harness](https://pi.dev/packages/pi-better-harness?page=4) | 12,344/mo | extension | Pi extension bundle for a write sandbox, subagents, background tasks, SSH, goals, and Outcome & Todo. | `pi install npm:pi-better-harness` |
| 198 | [@capdiem/pi-todo](https://pi.dev/packages/@capdiem/pi-todo?page=4) | 11,506/mo | package | A lightweight atomic todo tool for the Pi coding agent: one-call snapshot plans, three states, stale-write guard, plus a TUI widget and a pi-agent-desktop sidebar panel | `pi install npm:@capdiem/pi-todo` |
| 216 | [pi-anchorloop](https://pi.dev/packages/pi-anchorloop?page=5) | 10,990/mo | skill | Agent workflow skills for pi: one entry skill per task type over a short anchor loop (state the check, change, show it passing), plus a close guard and a skill validator. | `pi install npm:pi-anchorloop` |
| 218 | [pi-sandbox](https://pi.dev/packages/pi-sandbox?page=5) | 10,934/mo | extension | 为 pi 提供操作系统级沙箱，带交互式权限提示。 | `pi install npm:pi-sandbox` |
| 244 | [pi-cohort](https://pi.dev/packages/pi-cohort?page=5) | 9,325/mo | package | Delegate Pi work to focused child agents: code review, scouting, implementation, parallel audits, saved chains, and background jobs. | `pi install npm:pi-cohort` |
| 249 | [@trim21/personal-pi-extensions](https://pi.dev/packages/@trim21/personal-pi-extensions?page=5) | 9,223/mo | package | 自定义 pi 编码代理扩展：bwrap 沙箱、工作区守卫、opencode 编辑，以及更多。 | `pi install npm:@trim21/personal-pi-extensions` |
| 266 | [@pi-kit/permissions](https://pi.dev/packages/@pi-kit/permissions?page=6) | 8,432/mo | extension | Allow/ask/deny guardrail extension for the Pi coding agent. No third-party runtime dependencies. | `pi install npm:@pi-kit/permissions` |
| 282 | [pi-goal-list-loop-audit](https://pi.dev/packages/pi-goal-list-loop-audit?page=6) | 7,512/mo | extension | 自主 pi 的任务控制：访谈起草的目标、受审计的任务队列，以及可运行数小时的永久循环（metric、spec、project-audit）。一个独立的、无需扩展的审计进程会用原始证据重新验证每次完成，而不会持有 | `pi install npm:pi-goal-list-loop-audit` |
| 285 | [@aliou/pi-guardrails](https://pi.dev/packages/@aliou/pi-guardrails?page=6) | 7,474/mo | extension | ![banner](https://assets.aliou.me/github/aliou/pi-guardrails/banner.png) | `pi install npm:@aliou/pi-guardrails` |
| 296 | [@1aboveio/risk-compliance-skills](https://pi.dev/packages/@1aboveio/risk-compliance-skills?page=6) | 7,224/mo | skill | Compliance audits, contract review, payment and fraud analysis. | `pi install npm:@1aboveio/risk-compliance-skills` |

### 其他 / 待复核

| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |
| ---: | --- | ---: | --- | --- | --- |
| 60 | [@cratis/pi](https://pi.dev/packages/@cratis/pi?page=2) | 35,051/mo | skill | Configuration-aware Cratis AI integration for Pi | `pi install npm:@cratis/pi` |
| 64 | [@agimon-ai/po-build](https://pi.dev/packages/@agimon-ai/po-build?page=2) | 34,327/mo | package | Folder-convention scanner and build presets for Po extensions. | `pi install npm:@agimon-ai/po-build` |
| 156 | [@bopstack/pi-codegraph](https://pi.dev/packages/@bopstack/pi-codegraph?page=4) | 15,331/mo | package | CodeGraph code understanding extension for Pi and Oh My Pi | `pi install npm:@bopstack/pi-codegraph` |
| 211 | [@howaboua/pi-unicode-charts](https://pi.dev/packages/@howaboua/pi-unicode-charts?page=5) | 11,160/mo | extension | Terminal-native Unicode charts for Pi Markdown | `pi install npm:@howaboua/pi-unicode-charts` |
| 227 | [@gyoungwe/pi-analysis](https://pi.dev/packages/@gyoungwe/pi-analysis?page=5) | 10,267/mo | package | Portable scientific analysis adapters and readiness gates for native Pi | `pi install npm:@gyoungwe/pi-analysis` |
| 228 | [@gyoungwe/pi-evidence](https://pi.dev/packages/@gyoungwe/pi-evidence?page=5) | 10,260/mo | package | Portable evidence manifests, provenance, checkpoints and replay proofs for native Pi | `pi install npm:@gyoungwe/pi-evidence` |
| 230 | [@gyoungwe/pi-connectors](https://pi.dev/packages/@gyoungwe/pi-connectors?page=5) | 10,154/mo | package | Host-neutral, read-only connector declarations and provenance receipts for native Pi | `pi install npm:@gyoungwe/pi-connectors` |
| 247 | [@lwlee2608/pi-notify](https://pi.dev/packages/@lwlee2608/pi-notify?page=5) | 9,307/mo | extension | Phone notifications when an armed Pi run finishes. | `pi install npm:@lwlee2608/pi-notify` |
| 263 | [pi-tuck](https://pi.dev/packages/pi-tuck?page=6) | 8,449/mo | extension | Deterministic compaction for Pi with no model call, plus exact recall of earlier history. | `pi install npm:pi-tuck` |
| 268 | [@amaster.ai/pi-video-gen](https://pi.dev/packages/@amaster.ai/pi-video-gen?page=6) | 8,380/mo | extension | Pi extension for direct video-model clips, recoverable mixed-shot rendering, and local concat, FFmpeg timeline or editable HyperFrames (default) / Remotion composition with subtitles and QC. | `pi install npm:@amaster.ai/pi-video-gen` |
| 279 | [@oisin-ee/pi-dogsled](https://pi.dev/packages/@oisin-ee/pi-dogsled?page=6) | 7,769/mo | extension | Pi extension for dogsled: the board, the /dogsled panel, the inbox reader, and the dogsled tools. Needs the dogsled binary of the same version. | `pi install npm:@oisin-ee/pi-dogsled` |
| 286 | [pi-tsgw](https://pi.dev/packages/pi-tsgw?page=6) | 7,453/mo | package | 面向 TOSSP AIH gateway 的 Pi 扩展：按厂商维护聊天与图片模型目录及思考策略，支持四种聊天协议、图片生成与编辑工具，以及原生 System One 分类模型。 | `pi install npm:pi-tsgw` |
| 287 | [@herbertgao/pi-extensions](https://pi.dev/packages/@herbertgao/pi-extensions?page=6) | 7,427/mo | extension | Aggregate installer for HerbertGao-maintained Pi extensions. | `pi install npm:@herbertgao/pi-extensions` |
| 293 | [pi-typesafe](https://pi.dev/packages/pi-typesafe?page=6) | 7,272/mo | extension | TypeSafe AI (Jev) decisions for Pi: batched Choice/Score/Noul evaluation tool, terminal playground, and a typed API other extensions build on. | `pi install npm:pi-typesafe` |
