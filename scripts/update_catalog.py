#!/usr/bin/env python3
"""Fetch the Pi catalog's top 300 packages and preserve dated snapshots."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import urllib.request
from html import unescape
from pathlib import Path

CATALOG_URL = "https://pi.dev/packages?sort=downloads&page={page}"
USER_AGENT = "pi-top300-catalog/0.1 (+https://github.com/allenlcj/pi-top300)"


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", unescape(value)).strip()


def attr(tag: str, name: str) -> str:
    match = re.search(rf'data-{re.escape(name)}="([^"]*)"', tag)
    return unescape(match.group(1)) if match else ""


def href_for(card: str, label: str) -> str | None:
    links = re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', card, re.DOTALL)
    for href, body in links:
        if re.search(rf'\b{re.escape(label)}\b', strip_tags(body)):
            return unescape(href)
    return None


def parse_page(html: str, rank_offset: int) -> list[dict]:
    cards = re.findall(r'<article[^>]*data-package-card="true".*?</article>', html, re.DOTALL)
    packages = []
    for index, card in enumerate(cards, start=1):
        name = attr(card, "package-name")
        description_match = re.search(r'<p class="packages-desc">(.*?)</p>', card, re.DOTALL)
        package_link = re.search(r'<h3 class="packages-name"><a href="([^"]+)"', card)
        types = re.findall(r'data-type="([^"]+)"', card)
        if not name or not description_match:
            raise ValueError(f"Could not parse catalog card {rank_offset + index}: {name!r}")
        packages.append(
            {
                "rank": rank_offset + index,
                "name": name,
                "description": strip_tags(description_match.group(1)),
                "downloads": int(attr(card, "package-downloads") or 0),
                "types": types,
                "href": unescape(package_link.group(1)) if package_link else None,
                "repo": href_for(card, "repo"),
                "npm": href_for(card, "npm"),
            }
        )
    return packages


def fetch(page: int) -> list[dict]:
    request = urllib.request.Request(
        CATALOG_URL.format(page=page), headers={"User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return parse_page(response.read().decode("utf-8"), (page - 1) * 50)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--output", default="data/packages-latest.json")
    args = parser.parse_args()

    packages = [package for page in range(1, 7) for package in fetch(page)]
    if len(packages) != 300 or [p["rank"] for p in packages] != list(range(1, 301)):
        raise SystemExit(f"Expected ranks 1..300, got {len(packages)} packages")

    payload = {
        "source": "https://pi.dev/packages?sort=downloads",
        "scope": "All types; Most downloads; ranks 1-300",
        "retrievedAt": args.date,
        "packageCount": len(packages),
        "packages": packages,
    }

    output = Path(args.output)
    snapshot = output.parent / "snapshots" / f"{args.date}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    output.write_text(text, encoding="utf-8")
    snapshot.write_text(text, encoding="utf-8")
    print(f"Wrote {len(packages)} packages to {output} and {snapshot}")


if __name__ == "__main__":
    main()
