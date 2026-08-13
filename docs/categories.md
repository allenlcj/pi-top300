# Pi 包分类指南

本页是前 300 快照的人工分类入口。分类只描述主要用途；复合包可能同时覆盖多个能力，但目录中只设置一个主类别，避免统计重复。

## 1. Agent 编排、Subagent、Plan、Goal、Task

解决任务拆解、子 Agent 委托、计划批准、目标持续执行和任务进度问题。

代表：`pi-subagents`、`@tintinweb/pi-subagents`、`@plannotator/pi-extension`、`@narumitw/pi-goal`、`@mjasnikovs/pi-task`、`@juicesharp/rpiv-todo`。

选择建议：先区分“计划”“任务列表”“持续执行”和“子 Agent”，不要同时安装多个会接管同一命令或生命周期的框架。

## 2. Context、Memory、知识与 Compaction

解决长 Session、跨 Session 记忆、工具输出过多和压缩后恢复问题。

代表：`context-mode`、`pi-hermes-memory`、`pi-memory`、`pi-goosedump`、`pi-context`、`pi-condense`、`pi-observational-memory`。

选择建议：先确认需要的是长期记忆、历史搜索、工具输出压缩还是主动 checkpoint，再选择一个主系统。

## 3. Web、浏览器、Research、MCP

提供网页搜索、URL 获取、GitHub/PDF/视频处理、浏览器操作和外部 MCP 工具。

代表：`pi-mcp-adapter`、`pi-web-access`、`pi-agent-browser-native`、`pi-web-search`、`@narumitw/pi-chrome-devtools`、`@upstash/context7-pi`。

选择建议：同类 Provider 不必全部安装，优先使用一个稳定 Web 层和必要的专用 MCP。

## 4. 代码智能、编辑与 Review

提供 LSP、Lint、AST、符号搜索、哈希定位编辑、Diff 和代码审查。

代表：`pi-lens`、`@narumitw/pi-lsp`、`pi-readseek`、`pi-hashline-edit-pro`、`opencode-codebase-index`、`pi-pr-review`。

选择建议：已有 LSP/诊断工具时，不要轻易同时替换 Pi 的基础读写工具。

## 5. 模型、Provider、路由、用量与缓存

提供模型接入、本地模型、Provider 代理、自动路由、账户用量和 Prompt Cache 观察。

代表：`pi-smart-router`、`pi-lmstudio`、`pi-llama-cpp`、`pi-provider-litellm`、`pi-usage`、`pi-cache-optimizer`、`pi-prompt-template-model`。

选择建议：自动路由器需要单独验证；角色模型或 Prompt 绑定通常比多个自动路由器叠加更容易控制。

## 6. 安全、权限与 Sandbox

控制工具、Bash、MCP、路径和外部进程的权限。

代表：`@gotgenes/pi-permission-system`、`piolium`、`pi-landstrip`、`pi-sandbox`、`pi-guardrails`。

选择建议：权限系统和 Sandbox 可能作用在相同边界，先理解规则叠加方式，再启用第二套。

## 7. UI、TUI、Session 与观测

改善状态栏、Widget、侧边栏、Session 浏览、Usage 和运行观测。

代表：`pi-powerline-footer`、`@narumitw/pi-statusline`、`pi-zentui`、`pi-cc-extensions`、`pi-usage-extension`、`pi-rewind`、`pi-btw`。

选择建议：Footer、Sidebar 和状态 Widget 同时启用可能冲突，按用途各选一个。

## 8. Skills、Prompts、Rules 与结构化提问

提供编程方法、规则、Prompt 模板和结构化用户选择。

代表：`bigpowers`、`@7n/rules`、`@dietrichgebert/ponytail`、`pi-prompt-template-model`、`@juicesharp/rpiv-ask-user-question`、`gentle-pi`。

选择建议：优先安装自己能理解和解释的 Skills，不要把大型方法论套件当成已掌握知识。

## 9. 后台任务、Runtime、Worktree 与平台集成

处理后台 Shell、长任务、工作区隔离、远程入口和外部项目系统。

代表：`pi-background-tasks`、`@narumitw/pi-worktree`、`pi-courier`、`pi-telegram`、`pi-g
