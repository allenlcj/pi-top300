# Pi Top 300

[中文](README.zh-CN.md) · [English](README.md)

A maintained, categorized guide to the 300 most-downloaded packages in the official [Pi package catalog](https://pi.dev/packages).

## What this project does

Pi Top 300 helps Pi users discover extensions, skills, prompts, themes, and packages by **what they do**, not only by package name. It separates:

- **Popularity** — the package appears in the official catalog's `All types → Most downloads` top 300 at a recorded snapshot;
- **Recommendation** — a separate editorial judgment based on scope, maintenance signals, compatibility, overlap, safety, and usefulness.

Popularity is not a quality or security guarantee. Pi packages can execute code with the user's permissions. Review source code and package permissions before installing anything.

## Current snapshot

- Source: [`pi.dev/packages?sort=downloads`](https://pi.dev/packages?sort=downloads)
- Scope: All types, Most downloads, ranks 1–300
- Snapshot: `2026-08-13`
- Structured data: [`data/packages-latest.json`](data/packages-latest.json)
- Full browsable list: [`docs/packages.md`](docs/packages.md)
- Historical snapshots: [`data/snapshots/`](data/snapshots/)

## Main categories

- Agent orchestration, subagents, plans, goals, and tasks
- Context, memory, knowledge, and compaction
- Web, browser, research, and MCP
- Code intelligence, editing, and review
- Models, providers, routing, usage, and cache
- Security, permissions, and sandboxing
- UI, TUI, session, and observability
- Skills, prompts, rules, and structured questions
- Background work, runtime, worktrees, and integrations

See [the category guide](docs/categories.md) for representative packages and selection advice. See [`docs/packages.md`](docs/packages.md) for all 300 package rows, descriptions, rankings, and install commands.

## Updating the catalog

The project keeps a dated raw snapshot instead of overwriting history. A future update should:

1. fetch the official catalog;
2. save a new snapshot under `data/snapshots/YYYY-MM-DD.json`;
3. update `data/packages-latest.json`;
4. regenerate [`docs/packages.md`](docs/packages.md);
5. preserve editorial classifications and notes separately from fetched data;
6. open a pull request for review.

Automated updates are configured as a weekly Pull Request workflow.

## Disclaimer

Downloads are npm monthly download figures shown by pi.dev at collection time, not unique-user counts. Rankings change. Descriptions and repository links are copied from the catalog and may become stale.

## License

The project code and editorial documents are MIT-licensed. Package names, descriptions, trademarks, and upstream source code remain the property of their respective authors.
