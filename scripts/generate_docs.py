#!/usr/bin/env python3
"""Generate README.md (by category) and docs/packages.md (by rank) from data/packages-latest.json."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "packages-latest.json"
OVERRIDES = ROOT / "data" / "categories.yaml"
README_OUT = ROOT / "README.md"
CATALOG_OUT = ROOT / "docs" / "packages.md"

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

# Specific categories are matched before the generic "agent" bucket, so that
# generic phrases like "for Pi coding agent" do not capture everything.
RULES = [
    ("security", "permission security sandbox guard safety audit casefile credential"),
    (
        "context",
        "context memory compact condense cache knowledge wiki mentis remnic papyrus fovea lore",
    ),
    (
        "web",
        "web browser chrome mcp search fetch crawl firecrawl spider pdf youtube obsidian context7 research lookup query",
    ),
    (
        "code",
        "lsp lens ast codebase edit readseek hashline simplify review diff fff pretty compiler workbench",
    ),
    (
        "model",
        "provider router usage token litellm lmstudio llama kimi openrouter openai gemini deepseek vertex nvidia llm anthropic oauth accounts gpt ollama",
    ),
    (
        "ui",
        "ui tui footer statusline powerline cockpit atelier sidebar studio preview display insight telemetry langfuse braintrust tps usage trace tracing session conversation voice audio",
    ),
    (
        "skill",
        "skill prompt rules powers ponytail ask question interview advisor persona superpowers placeholder",
    ),
    (
        "runtime",
        "background worktree sync telegram courier atlassian tickets email channel scheduler process pwsh loop lark github-pr ssh remote desktop automation runtime linear config setting repl utility",
    ),
    (
        "agent",
        "subagent agent goal plan task workflow orchestration harness fabric crew squad autopilot teammate superagent team intercom dag runner todo",
    ),
]


def load_overrides() -> dict[str, dict[str, str]]:
    """Read the deliberately small YAML override file without requiring PyYAML.
    Format:
      packages:
        <package-name>:
          category: <category-key>
          recommendation: <status>
          note: <text>"""
    if not OVERRIDES.exists():
        return {}
    overrides: dict[str, dict[str, str]] = {}
    current: str | None = None
    for raw in OVERRIDES.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line == "packages:":
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent == 0 and line.endswith(":"):
            continue
        if indent == 2 and line.endswith(":"):
            current = line[:-1].strip().strip("\"'")
            overrides[current] = {}
        elif current and ":" in line:
            key, value = line.split(":", 1)
            overrides[current][key.strip()] = value.strip().strip("\"'")
    return overrides


TRANSLATIONS = ROOT / "data" / "translations.zh.json"


def load_translations() -> dict[str, str]:
    """Load Chinese descriptions keyed by package name (fall back to English)."""
    if not TRANSLATIONS.exists():
        return {}
    try:
        data = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def slugify(text: str) -> str:
    """GitHub-style heading anchor: lowercase, strip punctuation, spaces to dashes.
    CJK characters are kept so Chinese headings get stable anchors."""
    # github-slugger punctuation set (General Punctuation + CJK punctuation + ASCII)
    cleaned = re.sub(
        r"[\u2000-\u206F\u2E00-\u2E7F\\'!\"#$%&()*+,./:;<=>?@\[\]^`{|}~]", "",
        text.strip().lower(),
    )
    return re.sub(r"\s+", "-", cleaned)


def stem(token: str) -> str:
    """Rough English plural normalization so 'agents' matches 'agent'."""
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith("es") and len(token) > 4:
        return token[:-2]
    if token.endswith("s") and len(token) > 3:
        return token[:-1]
    return token


def matches(text: str, word: str, name_tokens: list[str]) -> bool:
    """Exact stem match on the text; substring match only inside the package
    name, so glued identifiers like 'freerouter' match 'router' without
    description words like 'editor' false-matching 'edit'."""
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    if word in [stem(tok) for tok in tokens]:
        return True
    return len(word) >= 4 and any(word in tok for tok in name_tokens)


def classify(
    package: dict, overrides: dict[str, dict[str, str]]
) -> tuple[str, str]:
    name = package["name"]
    override = overrides.get(name, {})
    if override.get("category") in CATEGORIES:
        category = override["category"]
    else:
        text = f"{name} {package.get('description', '')}".lower()
        name_tokens = re.findall(r"[a-z0-9]+", name.lower())
        category = "other"
        for candidate, words in RULES:
            if any(matches(text, word, name_tokens) for word in words.split()):
                category = candidate
                break
    note = override.get("note", "")
    return CATEGORIES[category], note


def package_type(package: dict) -> str:
    types = package.get("types") or []
    return ", ".join(types) if types else "package"


def absolute_link(url: str | None) -> str:
    if not url:
        return "—"
    if url.startswith("/"):
        return f"https://pi.dev{url}"
    return url


def describe(package: dict, note: str, translations: dict[str, str]) -> str:
    description = translations.get(package["name"]) or package.get("description", "")
    description = description.replace("|", "\\|").replace("\n", " ")
    if note:
        description += f"（{note}）"
    return description


def package_link(package: dict) -> str:
    name = package["name"]
    pkg_url = absolute_link(package.get("href"))
    return f"[{name}]({pkg_url})" if pkg_url != "—" else f"`{name}`"


def row(
    package: dict, category: str, note: str, with_category: bool, translations: dict[str, str]
) -> str:
    link = package_link(package)
    install = f"`pi install npm:{package['name']}`"
    base = (
        f"| {package['rank']} | {link} | {package['downloads']:,}/mo | "
        f"{package_type(package)} | {describe(package, note, translations)}"
    )
    if with_category:
        base += f" | {category}"
    return f"{base} | {install} |"


def grouped_packages(
    packages: list[dict], overrides: dict[str, dict[str, str]]
) -> list[tuple[str, list[dict]]]:
    buckets: dict[str, list[dict]] = {}
    for package in packages:
        category, _ = classify(package, overrides)
        buckets.setdefault(category, []).append(package)
    ordered = sorted(buckets, key=lambda c: (-len(buckets[c]), c == "其他 / 待复核"))
    return [(c, buckets[c]) for c in ordered]


def render_readme(
    packages: list[dict], overrides: dict[str, dict[str, str]], payload: dict,
    translations: dict[str, str],
) -> None:
    groups = grouped_packages(packages, overrides)
    lines = [
        "# Pi Top 300",
        "",
        "Pi 官方 Package Catalog 前 300 热门包的用途分类目录（All types · Most downloads）。",
        "",
        "[分类指南](docs/categories.md) · [按排名清单](docs/packages.md) · [原始 JSON 数据](data/packages-latest.json)",
        "",
        "> ⚠️ Pi 包可能以当前用户权限执行代码，安装前请审查源码和权限。",
        "> 下载量为 npm 月下载量，不代表质量或安全性。分类基于名称和描述的初步归类，人工意见维护在 `data/categories.yaml`。",
        "",
        f"- 快照 `{payload['retrievedAt']}`（[历史快照](data/snapshots/)）· 共 {len(packages)} 包",
        "",
        "## 分类总览",
        "",
        "| 类别 | 数量 | 占比 |",
        "| --- | ---: | ---: |",
    ]
    for category, group in groups:
        anchor = slugify(category)
        lines.append(
            f"| [{category}](#{anchor}) | {len(group)} | {len(group) / len(packages) * 100:.0f}% |"
        )
    lines.append("")
    lines.append("## 按类别清单")
    lines.append("")
    for category, group in groups:
        lines.append(f"### {category}")
        lines.append("")
        lines.append("| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 安装 |")
        lines.append("| ---: | --- | ---: | --- | --- | --- |")
        for package in sorted(group, key=lambda p: p["rank"]):
            category, note = classify(package, overrides)
            lines.append(row(package, category, note, with_category=False, translations=translations))
        lines.append("")
    README_OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(
        f"Generated {README_OUT} with {len(packages)} packages in {len(groups)} categories"
    )


def render_catalog(
    packages: list[dict], overrides: dict[str, dict[str, str]], payload: dict,
    translations: dict[str, str],
) -> None:
    lines = [
        "# Pi 官方热门包前 300",
        "",
        "> 按 Pi 官方 Package Catalog 的 `All types → Most downloads` 快照生成，下载量为 npm 月下载量，不代表质量或安全性。",
        "",
        f"- 快照 `{payload['retrievedAt']}`（[历史快照](../data/snapshots/)）· 共 {len(packages)} 包",
        "",
        "按排名顺序浏览；按用途类别浏览见 [README 分类清单](../README.md)。",
        "",
        "## 完整清单（按排名）",
        "",
        "| 排名 | 包 | 月下载量 | 类型 | 主要用途 | 初步类别 | 安装 |",
        "| ---: | --- | ---: | --- | --- | --- | --- |",
    ]
    for package in packages:
        category, note = classify(package, overrides)
        lines.append(row(package, category, note, with_category=True, translations=translations))
    CATALOG_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {CATALOG_OUT} with {len(packages)} packages")


def main() -> None:
    try:
        payload = json.loads(DATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Failed to read {DATA}: {exc}") from exc
    packages = payload["packages"]
    overrides = load_overrides()
    translations = load_translations()
    render_readme(packages, overrides, payload, translations)
    render_catalog(packages, overrides, payload, translations)


if __name__ == "__main__":
    main()
