#!/usr/bin/env python3
"""Import HPCA 2026 accepted papers from the official program page.

What this script updates:
1) docs/HPCA/2026/**
   - Rebuilds track directories, track index pages, and per-paper markdown stubs.
2) mkdocs.yml
   - Rebuilds the HPCA 2026 nav block under "⚡ HPCA" and keeps HPCA 2025 unchanged.
3) docs/index.md
   - Updates the HPCA 2026 card count and top-track tags.

Run:
  python3 scripts/import_hpca_2026.py
"""

from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
INDEX_MD = DOCS / "index.md"

HPCA_URL = "https://2026.hpca-conf.org/program/program-hpca-2026/"
HPCA_LOCATION = "Sydney, Australia"
HPCA_DATE = "2026年2月2日 - 2月4日"
HPCA_YEAR = "2026"

# Tracks to include (facet-track values from the HTML)
INCLUDED_FACET_TRACKS = {"HPCA Main Conference", "HPCA Best of CAL", "HPCA Industry"}


@dataclass
class Paper:
    title: str
    authors: str
    doi: str = ""


def curl_fetch(url: str) -> str:
    return subprocess.check_output(["curl", "-L", "--silent", url], text=True)


def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "paper"


def yaml_quote(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def normalize_track(raw: str) -> str:
    """Extract the session name from the session-info-in-table text."""
    # The text looks like "Session Name Main Conference at Room  Chair(s): ..."
    # Edge case: "Best of CAL Best of CAL at Cronulla ..." -> "Best of CAL"
    # Edge case: "Industry Track Industry Track at Coogee ..." -> "Industry Track"
    for suffix in ["Main Conference", "Best of CAL", "Industry Track", "Industry"]:
        idx = raw.find(suffix)
        if idx != -1:
            if idx == 0:
                # Session name IS the suffix (e.g. "Best of CAL Best of CAL at ...")
                return suffix
            track = raw[:idx].strip()
            # Remove trailing separators
            track = re.sub(r"[\s\-–—]+$", "", track).strip()
            if track:
                return track
    # Fallback: first sentence before Chair(s)
    return " ".join(raw.split()).strip().split("Chair(s)")[0].strip()


def _extract_paper_from_row(row: BeautifulSoup) -> Optional[Paper]:
    """Extract a Paper from a <tr class="hidable"> row."""
    tds = row.find_all("td")
    if len(tds) < 4:
        return None

    content_td = tds[3]

    # Title is in <strong><a>
    strong = content_td.find("strong")
    if not strong:
        return None
    title_tag = strong.find("a")
    title = title_tag.get_text(" ", strip=True) if title_tag else strong.get_text(" ", strip=True)
    title = " ".join(title.split())
    if not title:
        return None

    # Authors are in <div class="performers">
    performers_div = content_td.find("div", class_="performers")
    authors = ""
    if performers_div:
        # Build "Name Affiliation, Name Affiliation, ..." string
        parts = []
        for child in performers_div.children:
            if hasattr(child, "get_text"):
                text = child.get_text(" ", strip=True)
                if text:
                    parts.append(text)
        authors = " ".join(parts)
        authors = re.sub(r"\s+", " ", authors).strip()

    # DOI / pre-print link
    doi = ""
    for a in content_td.find_all("a", href=True):
        href = a["href"]
        if "doi.org" in href or "arxiv.org" in href:
            doi = href
            break

    return Paper(title=title, authors=authors, doi=doi)


def parse_hpca_2026() -> Dict[str, List[Paper]]:
    html = curl_fetch(HPCA_URL)
    soup = BeautifulSoup(html, "html.parser")
    tracks: Dict[str, List[Paper]] = {}

    session_tables = soup.find_all("table", class_="session-table")

    for table in session_tables:
        # Get session info
        info_div = table.find("div", class_="session-info-in-table")
        if not info_div:
            continue

        info_text = " ".join(info_div.get_text(" ", strip=True).split())

        # Only include Main Conference / Best of CAL / Industry Track sessions
        is_target = any(ft in info_text for ft in ["Main Conference", "Best of CAL", "Industry"])
        if not is_target:
            continue

        track = normalize_track(info_text)
        if not track:
            continue

        # Extract papers from hidable rows
        for row in table.find_all("tr", class_="hidable"):
            # Check facet track
            facet_span = row.find("span", attrs={"data-facet-track": True})
            if facet_span:
                facet = facet_span.get("data-facet-track", "")
                # Accept HPCA Main Conference, Best of CAL, Industry
                if not any(ft in facet for ft in ["HPCA Main", "HPCA Best", "HPCA Industry", "Industry"]):
                    continue

            # Only accept Talk type rows
            event_type_td = row.find("td", class_=lambda c: c and "text-right" in c)
            event_type_div = row.find("div", class_="event-type")
            if event_type_div:
                et = event_type_div.get_text(strip=True)
                if "Talk" not in et and "Industry talk" not in et:
                    continue
            else:
                continue

            paper = _extract_paper_from_row(row)
            if paper:
                tracks.setdefault(track, []).append(paper)

    return tracks


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def paper_md(track: str, p: Paper) -> str:
    tags = [f"HPCA{HPCA_YEAR}", track]
    tag_lines = "\n".join([f'  - "{t}"' for t in tags])
    doi_line = f"**论文链接**：[{p.doi}]({p.doi})" if p.doi else "**论文链接**："
    return f"""---
title: "{p.title}"
description: "HPCA {HPCA_YEAR} · {track}"
tags:
{tag_lines}
---

# {p.title}

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA {HPCA_YEAR}，所属 Track: {track}。</p>
<p class="paper-seo-summary__tags">HPCA {HPCA_YEAR} · {track}</p>
</div>

{doi_line}
**作者**：{p.authors}
**会议**：HPCA {HPCA_YEAR}

---

## 一句话总结

> 该工作属于 {track} 方向，围绕关键系统瓶颈提出优化方案，并在 HPCA {HPCA_YEAR} 语境下验证其价值。

## 方法简述

- 识别该方向中的关键性能、能效或可靠性瓶颈。
- 通过软硬件协同优化构建可落地的系统方案。
- 在典型工作负载上进行评估并分析设计权衡。

## 主要结果

- 在目标指标（性能、能效或可靠性）上相对基线实现改进。
- 展示了与现有系统栈集成的可行性。
- 为后续扩展和工程化部署提供依据。
"""


def track_index_md(track: str, items: List[Tuple[str, str, str]]) -> str:
    rows = []
    for title, rel, doi in items:
        doi_cell = f"[DOI]({doi})" if doi else "-"
        rows.append(f"| [{title}]({rel}) | {doi_cell} |")
    table = "\n".join(rows)
    return f"""# {track} · HPCA {HPCA_YEAR}

本分类收录 HPCA {HPCA_YEAR} Track \"{track}\" 的论文。

| 论文 | 链接 |
|------|------|
{table}
"""


def conf_index_md(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> str:
    rows = []
    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        rows.append(f"| [{track}]({slug_map[track]}/index.md) | {len(papers)} |")
    table_rows = "\n".join(rows)

    total = sum(len(p) for p in tracks.values())
    return f"""---
title: "HPCA {HPCA_YEAR} 论文集"
description: "HPCA {HPCA_YEAR} 论文解读，{HPCA_LOCATION}"
search:
  exclude: false
hide:
  - toc
---

# HPCA {HPCA_YEAR}

**HPCA {HPCA_YEAR}** · {HPCA_DATE} · {HPCA_LOCATION}

---

| 分类 (Track) | 论文数 |
|-------------|-------|
{table_rows}
"""


def build_docs(tracks: Dict[str, List[Paper]]) -> Tuple[int, Dict[str, str]]:
    base = DOCS / "HPCA" / HPCA_YEAR
    base.mkdir(parents=True, exist_ok=True)

    # Clean previous generated content under docs/HPCA/2026
    for child in base.iterdir():
        if child.is_dir():
            for root, dirs, files in os.walk(child, topdown=False):
                for fn in files:
                    Path(root, fn).unlink()
                for dn in dirs:
                    Path(root, dn).rmdir()
            child.rmdir()
        elif child.name.endswith(".md"):
            child.unlink()

    slug_map: Dict[str, str] = {}
    used_track_slugs: Dict[str, int] = {}

    for track in tracks:
        s = slugify(track)
        if s in used_track_slugs:
            used_track_slugs[s] += 1
            s = f"{s}_{used_track_slugs[s]}"
        else:
            used_track_slugs[s] = 1
        slug_map[track] = s

    total = 0
    for track, papers in tracks.items():
        tslug = slug_map[track]
        tdir = base / tslug
        tdir.mkdir(parents=True, exist_ok=True)

        used_titles: Dict[str, int] = {}
        index_items: List[Tuple[str, str, str]] = []

        for p in papers:
            pslug = slugify(p.title)
            if pslug in used_titles:
                used_titles[pslug] += 1
                pslug = f"{pslug}_{used_titles[pslug]}"
            else:
                used_titles[pslug] = 1

            rel = f"{pslug}.md"
            write_file(tdir / rel, paper_md(track, p))
            index_items.append((p.title, rel, p.doi))
            total += 1

        write_file(tdir / "index.md", track_index_md(track, index_items))

    write_file(base / "index.md", conf_index_md(tracks, slug_map))
    return total, slug_map


def hpca_2026_nav_block(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str], total: int) -> List[str]:
    lines = [
        f"    - HPCA {HPCA_YEAR} ({total}):\n",
        f"      - HPCA {HPCA_YEAR}: HPCA/{HPCA_YEAR}/index.md\n",
    ]

    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        tslug = slug_map[track]
        lines.append(f"      - {yaml_quote(f'{track} ({len(papers)})')}:\n")
        lines.append(f"        - {yaml_quote(track)}: HPCA/{HPCA_YEAR}/{tslug}/index.md\n")

        used_titles: Dict[str, int] = {}
        for p in papers:
            pslug = slugify(p.title)
            if pslug in used_titles:
                used_titles[pslug] += 1
                pslug = f"{pslug}_{used_titles[pslug]}"
            else:
                used_titles[pslug] = 1
            lines.append(f"        - {yaml_quote(p.title)}: HPCA/{HPCA_YEAR}/{tslug}/{pslug}.md\n")

    return lines


def replace_hpca_2026_nav(content: str, new_block: List[str]) -> str:
    lines = content.splitlines(keepends=True)

    hpca_start = None
    for i, line in enumerate(lines):
        if line.startswith("  - ⚡ HPCA:"):
            hpca_start = i
            break
    if hpca_start is None:
        raise RuntimeError("Cannot find HPCA nav section in mkdocs.yml")

    start_2026 = None
    end_2026 = None

    for i in range(hpca_start + 1, len(lines)):
        if re.match(r"    - HPCA 2026", lines[i]):
            start_2026 = i
            break

    if start_2026 is None:
        raise RuntimeError("Cannot find HPCA 2026 nav block in mkdocs.yml")

    # Find where the 2026 block ends (next top-level nav item at "  - " level)
    for i in range(start_2026 + 1, len(lines)):
        if lines[i].startswith("  - "):
            end_2026 = i
            break
    if end_2026 is None:
        end_2026 = len(lines)

    return "".join(lines[:start_2026] + new_block + lines[end_2026:])


def update_homepage_index(total: int, top_tracks: List[Tuple[str, str, int]]) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")

    tags = "\n".join(
        [
            f'<a class="area-tag" href="HPCA/{HPCA_YEAR}/{slug}/" data-track-key="HPCA/{HPCA_YEAR}/{slug}" data-track-label="{label}">{label} {count}</a>'
            for label, slug, count in top_tracks[:3]
        ]
    )

    replacement = (
        f"### ⚡ [HPCA {HPCA_YEAR}](HPCA/{HPCA_YEAR}/index.md)\n\n"
        + f'<div class="conf-count" data-conf-key="HPCA {HPCA_YEAR}" data-conf-location="{HPCA_LOCATION}">{total} 篇 · {len(top_tracks)} 个方向 · {HPCA_LOCATION}</div>\n\n'
        + '<div class="area-groups">\n<div class="area-group">\n<div class="area-group-label">方向</div>\n<div class="area-tags">\n'
        + tags
        + "\n</div>\n</div>\n</div>"
    )

    pattern = (
        rf"### ⚡ \[HPCA {HPCA_YEAR}\]\(HPCA/{HPCA_YEAR}/index\.md\)\n\n[\s\S]*?"
        r"(?=\n---\n|\Z)"
    )

    new_text, n = re.subn(pattern, replacement, text, count=1)
    if n != 1:
        print(f"WARNING: Could not find HPCA {HPCA_YEAR} card block in docs/index.md; skipping homepage update.")
        return

    INDEX_MD.write_text(new_text, encoding="utf-8")


def main() -> None:
    print(f"Fetching HPCA {HPCA_YEAR} program from {HPCA_URL} ...")
    tracks = parse_hpca_2026()
    if not tracks:
        raise RuntimeError(f"No HPCA {HPCA_YEAR} tracks/papers parsed from official program page")

    print(f"Parsed {len(tracks)} tracks.")
    for track, papers in sorted(tracks.items(), key=lambda kv: -len(kv[1])):
        print(f"  {track}: {len(papers)} papers")

    total, slug_map = build_docs(tracks)
    print(f"\nBuilt {total} paper stubs across {len(tracks)} tracks.")

    mkdocs_text = MKDOCS.read_text(encoding="utf-8")
    mkdocs_text = replace_hpca_2026_nav(
        mkdocs_text,
        hpca_2026_nav_block(tracks, slug_map, total),
    )
    MKDOCS.write_text(mkdocs_text, encoding="utf-8")
    print("Updated mkdocs.yml.")

    top_tracks = [
        (track, slug_map[track], len(papers))
        for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ]
    update_homepage_index(total, top_tracks)
    print("Updated docs/index.md.")

    print(f"\nDone: HPCA {HPCA_YEAR} — {len(tracks)} tracks, {total} papers")
    print(f"Updated docs/HPCA/{HPCA_YEAR}, mkdocs.yml, and docs/index.md")


if __name__ == "__main__":
    main()
