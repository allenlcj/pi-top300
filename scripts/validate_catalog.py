#!/usr/bin/env python3
"""Validate a Pi Top 300 snapshot before publishing it."""

from __future__ import annotations

import json
from pathlib import Path


path = Path("data/packages-latest.json")
data = json.loads(path.read_text(encoding="utf-8"))
packages = data.get("packages", [])

assert data.get("scope") == "All types; Most downloads; ranks 1-300"
assert data.get("packageCount") == 300
assert len(packages) == 300
assert [item.get("rank") for item in packages] == list(range(1, 301))
assert len({item.get("name") for item in packages}) == 300
assert all(item.get("name") and item.get("description") for item in packages)
assert all(item.get("downloads", 0) >= 0 for item in packages)

print(f"Validated {len(packages)} packages from {data['retrievedAt']}")
