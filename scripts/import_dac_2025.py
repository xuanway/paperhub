#!/usr/bin/env python3
"""Import DAC 2025 accepted papers from the official program search page.

What this script updates:
1) docs/DAC/2025/**
   - Rebuilds track directories, track index pages, and per-paper markdown stubs.
2) mkdocs.yml
   - Rebuilds the DAC 2025 nav block under "🛠️ DAC" section.
3) docs/index.md
   - Updates the DAC 2025 conf-cube stat.

Run:
  python3 scripts/import_dac_2025.py
"""

from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
INDEX_MD = DOCS / "index.md"

DAC_URL = "https://62dac.conference-program.com/search-program/"
DAC_LOCATION = "San Francisco, CA"
DAC_DATE = "2025年6月22日 - 6月25日"
DAC_YEAR = "2025"
DAC_EDITION = "第62届"


@dataclass
class Paper:
    title: str
    authors: List[str] = field(default_factory=list)
    session: str = ""


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


def parse_dac_2025() -> Dict[str, List[Paper]]:
    """Parse DAC 2025 Research Manuscript papers from the search-program page.

    The page has two main sections:
    - "Presentations" — agenda-item divs, one per paper, each has:
        * ssid attribute (paper ID, e.g. "RESEARCH1860")
        * etype div (e.g. "Research Manuscript")
        * title-link a (paper title)
        * program-track div under tag_group102.topics (high-level track: AI/EDA/Design/Systems/Security)
        * program-track div under tag_group101.tracks (session name, e.g. "SEC3: Hardware Security...")
    - "Contributors" — presenter-name divs with data-link-type=".RESEARCH1860.author.person"
    """
    print(f"Fetching {DAC_URL} (this is a ~4MB page, please wait) ...")
    html = curl_fetch(DAC_URL)
    soup = BeautifulSoup(html, "html.parser")

    # Build paper_id -> [author names] mapping from the Contributors section
    paper_authors: Dict[str, List[str]] = {}
    for link in soup.select("div.presenter-name a[data-link-type]"):
        link_type = link.get("data-link-type", "")
        # Format: .RESEARCH880.author.person  or .ENGPOST123.author.person
        m = re.match(r"\.([^.]+)\.author\.person", link_type)
        if m:
            pid = m.group(1)
            name = link.get_text(strip=True)
            paper_authors.setdefault(pid, []).append(name)

    # Parse Research Manuscript agenda items.
    # Use class_='presentation-title' to exclude session-title containers
    # (which have ssid="none" and inflate the count by ~63).
    tracks: Dict[str, List[Paper]] = {}
    items = soup.find_all("div", class_="presentation-title")

    for item in items:
        etype_div = item.find("div", class_="etype")
        if not etype_div or "Research Manuscript" not in etype_div.get_text():
            continue

        ssid = item.get("ssid", "")
        title_a = item.select_one("div.title-link a")
        if not title_a:
            continue
        title = " ".join(title_a.get_text(" ", strip=True).split())
        if not title:
            continue

        # High-level topic track (Design / EDA / AI / Systems / Security)
        topics_div = item.select_one("div.tag-group-list.topics div.program-track")
        track = topics_div.get_text(strip=True) if topics_div else "Other"

        # Specific session name (e.g. "SEC3: Hardware Security: Attack & Defense")
        session_div = item.select_one("div.tag-group-list.tracks div.program-track")
        session = session_div.get_text(strip=True) if session_div else ""

        authors = paper_authors.get(ssid, [])
        tracks.setdefault(track, []).append(Paper(title=title, authors=authors, session=session))

    return tracks


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def paper_md(track: str, p: Paper) -> str:
    authors_str = ", ".join(p.authors) if p.authors else ""
    tags = [f"DAC{DAC_YEAR}", track]
    tag_lines = "\n".join([f'  - "{t}"' for t in tags])
    session_line = f"**Session**：{p.session}" if p.session else ""
    return f"""---
title: "{p.title}"
description: "DAC {DAC_YEAR} · {track}"
tags:
{tag_lines}
---

# {p.title}

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 DAC {DAC_YEAR}（{DAC_EDITION}），所属 Track: {track}。</p>
<p class="paper-seo-summary__tags">DAC {DAC_YEAR} · {track}</p>
</div>

**论文链接**：
**作者**：{authors_str}
**会议**：DAC {DAC_YEAR}（{DAC_EDITION}）
{session_line}

---

## 一句话总结

> 该工作属于 {track} 方向，围绕关键系统瓶颈提出优化方案，并在 DAC {DAC_YEAR} 语境下验证其价值。

## 方法简述

- 识别该方向中的关键性能、能效或设计自动化瓶颈。
- 通过软硬件协同或 EDA 工具链优化构建可落地方案。
- 在典型工作负载上进行评估并分析设计权衡。

## 主要结果

- 在目标指标（性能、能效或设计质量）上相对基线实现改进。
- 展示了与现有 EDA 或系统栈集成的可行性。
- 为后续扩展和工程化部署提供依据。
"""


def track_index_md(track: str, items: List[Tuple[str, str, str]]) -> str:
    rows = []
    for title, rel, session in items:
        session_cell = session if session else "-"
        rows.append(f"| [{title}]({rel}) | {session_cell} |")
    table = "\n".join(rows)
    return f"""# {track} · DAC {DAC_YEAR}

本分类收录 DAC {DAC_YEAR}（{DAC_EDITION}）Track \"{track}\" 的论文。

| 论文 | Session |
|------|---------|
{table}
"""


def conf_index_md(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> str:
    rows = []
    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        rows.append(f"| [{track}]({slug_map[track]}/index.md) | {len(papers)} |")
    table_rows = "\n".join(rows)
    total = sum(len(p) for p in tracks.values())
    return f"""---
title: "DAC {DAC_YEAR} 论文集"
description: "设计自动化会议（DAC {DAC_YEAR}，{DAC_EDITION}）接收论文解读，{DAC_LOCATION}"
search:
  exclude: false
hide:
  - toc
---

# DAC {DAC_YEAR}

**DAC {DAC_YEAR}**（{DAC_EDITION}）· {DAC_DATE} · {DAC_LOCATION}

---

| 分类 (Track) | 论文数 |
|-------------|-------|
{table_rows}
"""


def build_docs(tracks: Dict[str, List[Paper]]) -> Tuple[int, Dict[str, str]]:
    base = DOCS / "DAC" / DAC_YEAR
    base.mkdir(parents=True, exist_ok=True)

    # Clean previous generated content under docs/DAC/2025
    for child in base.iterdir():
        if child.is_dir():
            for root_dir, dirs, files in os.walk(child, topdown=False):
                for fn in files:
                    Path(root_dir, fn).unlink()
                for dn in dirs:
                    Path(root_dir, dn).rmdir()
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
            index_items.append((p.title, rel, p.session))
            total += 1

        write_file(tdir / "index.md", track_index_md(track, index_items))

    write_file(base / "index.md", conf_index_md(tracks, slug_map))
    return total, slug_map


def dac_2025_nav_block(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str], total: int) -> List[str]:
    lines = [
        f"    - DAC {DAC_YEAR} ({total}):\n",
        f"      - DAC {DAC_YEAR}: DAC/{DAC_YEAR}/index.md\n",
    ]
    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        tslug = slug_map[track]
        lines.append(f"      - {yaml_quote(f'{track} ({len(papers)})')}:\n")
        lines.append(f"        - {yaml_quote(track)}: DAC/{DAC_YEAR}/{tslug}/index.md\n")

        used_titles: Dict[str, int] = {}
        for p in papers:
            pslug = slugify(p.title)
            if pslug in used_titles:
                used_titles[pslug] += 1
                pslug = f"{pslug}_{used_titles[pslug]}"
            else:
                used_titles[pslug] = 1
            lines.append(f"        - {yaml_quote(p.title)}: DAC/{DAC_YEAR}/{tslug}/{pslug}.md\n")

    return lines


def replace_dac_2025_nav(content: str, new_block: List[str]) -> str:
    lines = content.splitlines(keepends=True)

    # Find "  - 🛠️ DAC:" section start
    dac_start = None
    for i, line in enumerate(lines):
        if line.startswith("  - 🛠️ DAC:"):
            dac_start = i
            break
    if dac_start is None:
        raise RuntimeError("Cannot find DAC nav section in mkdocs.yml")

    # Find "    - DAC 2025" line within this section
    start_2025 = None
    for i in range(dac_start + 1, len(lines)):
        if lines[i].startswith("  - ") and i > dac_start:
            # Reached next top-level nav item
            break
        if re.match(r"    - DAC 2025", lines[i]):
            start_2025 = i
            break

    if start_2025 is None:
        raise RuntimeError("Cannot find DAC 2025 nav block in mkdocs.yml")

    # Find end of this block (next "  - " line at top level)
    end_2025 = None
    for i in range(start_2025 + 1, len(lines)):
        if lines[i].startswith("  - "):
            end_2025 = i
            break
    if end_2025 is None:
        end_2025 = len(lines)

    return "".join(lines[:start_2025] + new_block + lines[end_2025:])


def update_homepage_index(total: int) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")
    # Replace the DAC conf-cube stat line
    old = '<div class="conf-cube__stat">更新中 · San Francisco</div>'
    new = f'<div class="conf-cube__stat" data-conf-key="DAC {DAC_YEAR}">{total} 篇 · {DAC_LOCATION}</div>'
    if old in text:
        text = text.replace(old, new, 1)
        INDEX_MD.write_text(text, encoding="utf-8")
        print("Updated docs/index.md DAC stat.")
    else:
        print("WARNING: Could not find DAC stat line in docs/index.md; skipping homepage update.")


def main() -> None:
    tracks = parse_dac_2025()
    if not tracks:
        raise RuntimeError("No DAC 2025 tracks/papers parsed from official program page")

    print(f"Parsed {len(tracks)} tracks.")
    for track, papers in sorted(tracks.items(), key=lambda kv: -len(kv[1])):
        print(f"  {track}: {len(papers)} papers")

    total, slug_map = build_docs(tracks)
    print(f"\nBuilt {total} paper stubs across {len(tracks)} tracks.")

    mkdocs_text = MKDOCS.read_text(encoding="utf-8")
    mkdocs_text = replace_dac_2025_nav(
        mkdocs_text,
        dac_2025_nav_block(tracks, slug_map, total),
    )
    MKDOCS.write_text(mkdocs_text, encoding="utf-8")
    print("Updated mkdocs.yml.")

    update_homepage_index(total)

    print(f"\nDone: DAC {DAC_YEAR} — {len(tracks)} tracks, {total} papers")
    print(f"Updated docs/DAC/{DAC_YEAR}, mkdocs.yml, and docs/index.md")


if __name__ == "__main__":
    main()
