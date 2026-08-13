#!/usr/bin/env python3
"""Generate a browsable full catalog from data/packages-latest.json."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "packages-latest.json"
OVERRIDES = ROOT / "data" / "categories.yaml"
OUTPUT = ROOT / "docs" / "packages.md"

CATEGORIES = {
    "agent": "Agent 编排 / Subagent / Plan / Goal / Task",
    "context": "Context / Memory / Knowledge / Compaction",
    "web": "Web / Browser / Research / MCP",
    "code": "代码智能 / 编辑 / Review",
    "model": "模型 / Provider / 路由 / 用量",
    "security": "安全 / 权限 / Sandbox",
    "ui": "UI / TUI / Session / 观测",
    "skill": "Skills / Prompt / Rules / 提问",
    "runtime": "Runtime / 后台任务 / Worktree / 集成",
    "other": "其他 / 待复核",
}

RULES = [
    ("security", "permission security sandbox guard safety audit casefile"),
    ("agent", "subagent agent goal task plan workflow orchestration harness fabric crew squad autopilot teammate superagent"),
    ("context", "context memory compact condense cache knowledge wiki mentis remnic papyrus fovea lore"),
    ("web", "web browser chrome mcp search fetch crawl firecrawl spider pdf youtube obsidian context7 research lookup"),
    ("code", "lsp lens ast codebase edit readseek hashline simplify review diff fff pretty compiler"),
    ("model", "model provider router usage token litellm lmstudio llama kimi cursor openrouter fast mode accounts cache"),
    ("ui", "ui tui footer statusline powerline cockpit atelier sidebar studio preview display insight telemetry langfuse braintrust tps usage"),
    ("skill", "skill prompt rules powers ponytail ask question interview advisor persona superpowers"),
    ("runtime", "background worktree sync telegram courier atlassian tickets email channel scheduler process pwsh loop lark github-pr"),
]


def load_overrides() -> dict[str, dict[str, str]]:
    """Read the deliberately small YAML override file without requiring PyYAML."""
    if not OVERRIDES.exists():
        return {}
    overrides: dict[str, dict[str, str]] = {}
    current: str | None = None
    for raw in OVERRIDES.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line in {"packages:", "packages: {}"}:
            continue
        if not raw.startswith(" ") and line.endswith(":"):
            current = line[:-1].strip().strip('"\'')
            overrides[current] = {}
        elif current and ":" in line:
            key, value = line.split(":", 1)
            overrides[current][key.strip()] = value.strip().strip('"\'')
    return overrides


def classify(package: dict, overrides: dict[str, dict[str, str]]) -> tuple[str, str, str]:
    name = package["name"]
    override = overrides.get(name, {})
    if override.get("category") in CATEGORIES:
        category = override["category"]
    else:
        text = f"{name} {package.get('description', '')}".lower()
        category = "other"
        for candidate, words in RULES:
            if any(re.search(rf"(?<![a-z0-9]){re.escape(word)}(?![a-z0-9])", text) for word in words.split()):
                category = candidate
                break
    status = override.get("recommendation", "待人工评估")
    note = override.get("note", "")
    return CATEGORIES[category], status, note


def package_type(package: dict) -> str:
    types = package.get("types") or []
    return ", ".join(types) if types else "package"


def absolute_link(url: str | None) -> str:
    if not url:
        return "—"
    if url.startswith("/"):
        return f"https://pi.dev{url}"
    return url


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    packages = payload["packages"]
    overrides = load_overrides()
    lines = [
        "# Pi 官方热门包前 300",
        "",
        "> 本页按 Pi 官方 Package Catalog 的 `All types → Most downloads` 快照生成。",
        "> 下载量是采集时页面显示的 npm 月下载量，不是独立用户数，也不代表质量或安全性。",
        "> 分类是基于名称和描述的初步分类；推荐状态默认为“待人工评估”，人工意见维护在 `data/categories.yaml`。",
        "",
        f"- 快照日期：`{payload['retrievedAt']}`",
        f"- 数据范围：`{payload['scope']}`",
        f"- 包数量：`{len(packages)}`",
        "- 原始数据：[`data/packages-latest.json`](../data/packages-latest.json)",
        "- 历史快照：[`data/snapshots/`](../data/snapshots/)",
        "",
        "## 使用方法",
        "",
        "按浏览器查找：`Ctrl+F` 搜索包名、类别或关键词。每行包含排名、包名、月下载量、用途描述、初步类别和安装命令。",
        "",
        "## 完整清单",
        "",
        "| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 初步类别 | 推荐状态 | 安装 |",
        "| ---: | --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for package in packages:
        category, status, note = classify(package, overrides)
        description = package.get("description", "").replace("|", "\\|").replace("\n", " ")
        if note:
            description += f"（{note}）"
        name = package["name"]
        pkg_url = absolute_link(package.get("href"))
        npm = package.get("npm") or f"https://www.npmjs.com/package/{name}"
        package_link = f"[{name}]({pkg_url})" if pkg_url != "—" else f"`{name}`"
        install = f"`pi install npm:{name}`"
        lines.append(
            f"| {package['rank']} | {package_link} | {package['downloads']:,}/mo | "
            f"{package_type(package)} | {description} | {category} | {status} | {install} |"
        )
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT} with {len(packages)} packages")


if __name__ == "__main__":
    main()
