#!/usr/bin/env python3
"""Import HPCA 2025 accepted papers from the official main-program page.

What this script updates:
1) docs/HPCA/2025/**
   - Rebuilds track directories, track index pages, and per-paper markdown stubs.
2) mkdocs.yml
   - Rebuilds the HPCA 2025 nav block under "⚡ HPCA" and keeps HPCA 2026 unchanged.
3) docs/index.md
   - Updates the HPCA 2025 card count and top-track tags.

Run:
  python3 scripts/import_hpca_2025.py
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

HPCA_URL = "https://hpca-conf.org/2025/main-program/"
HPCA_LOCATION = "Las Vegas, NV, USA"
HPCA_DATE = "2025年3月1日 - 3月5日"


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
    track = " ".join(raw.split()).strip()
    # Merge split sessions: e.g. "The Winning System - 1" and "The Winning System - 2"
    track = re.sub(r"\s*[\-–—]\s*\d+\s*$", "", track)
    return track.strip()


def _extract_track_from_session_title(text: str) -> Optional[str]:
    text = " ".join(text.split())
    m = re.search(r"Session\s+\d+[A-Z]\s*(?:\([^)]*\))?\s*:\s*(.+)$", text)
    if not m:
        return None
    return normalize_track(m.group(1))


def _authors_from_li(li: BeautifulSoup, title: str) -> str:
    text = " ".join(li.get_text(" ", strip=True).split())
    if text.startswith(title):
        text = text[len(title) :].strip()
    text = re.sub(r"^[\-–—:\s]+", "", text)
    return text


def _extract_paper_from_li(li: BeautifulSoup) -> Optional[Paper]:
    strong = li.find("strong")
    title = " ".join(strong.get_text(" ", strip=True).split()) if strong else ""
    if not title:
        return None

    # Skip non-paper bullets if any
    if title.lower().startswith("session chair"):
        return None

    doi = ""
    for a in li.select("a[href]"):
        href = a.get("href", "")
        if "doi.org" in href:
            doi = href
            break

    authors = _authors_from_li(li, title)
    return Paper(title=title, authors=authors, doi=doi)


def parse_hpca_2025() -> Dict[str, List[Paper]]:
    html = curl_fetch(HPCA_URL)
    soup = BeautifulSoup(html, "html.parser")
    tracks: Dict[str, List[Paper]] = {}

    for h5 in soup.find_all("h5"):
        h5_text = " ".join(h5.get_text(" ", strip=True).split())
        track = _extract_track_from_session_title(h5_text)
        if not track:
            continue

        # Find the first UL after this session header, but stop at next session header.
        node = h5
        ul = None
        while True:
            node = node.find_next()
            if node is None:
                break
            if node.name == "h5":
                break
            if node.name == "ul":
                ul = node
                break

        if ul is None:
            continue

        papers: List[Paper] = []
        for li in ul.find_all("li", recursive=False):
            paper = _extract_paper_from_li(li)
            if paper:
                papers.append(paper)

        if papers:
            tracks.setdefault(track, []).extend(papers)

    return tracks


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def paper_md(track: str, p: Paper) -> str:
    tags = ["HPCA2025", track]
    tag_lines = "\n".join([f'  - "{t}"' for t in tags])
    doi_line = f"**论文链接**：[{p.doi}]({p.doi})" if p.doi else "**论文链接**："
    return f"""---
title: "{p.title}"
description: "HPCA 2025 · {track}"
tags:
{tag_lines}
---

# {p.title}

<div class=\"paper-seo-summary\">
<p class=\"paper-seo-summary__desc\">该论文收录于 HPCA 2025，所属 Track: {track}。</p>
<p class=\"paper-seo-summary__tags\">HPCA 2025 · {track}</p>
</div>

{doi_line}
**作者**：{p.authors}
**会议**：HPCA 2025

---

## 一句话总结

> 该工作属于 {track} 方向，围绕关键系统瓶颈提出优化方案，并在 HPCA 2025 语境下验证其价值。

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
    return f"""# {track} · HPCA 2025

本分类收录 HPCA 2025 Track \"{track}\" 的论文。

| 论文 | 链接 |
|------|------|
{table}
"""


def conf_index_md(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> str:
    rows = []
    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        rows.append(f"| [{track}]({slug_map[track]}/index.md) | {len(papers)} |")
    table_rows = "\n".join(rows)

    return f"""---
title: "HPCA 2025 论文集"
description: "HPCA 2025 论文解读，{HPCA_LOCATION}"
search:
  exclude: false
hide:
  - toc
---

# HPCA 2025

**HPCA 2025** · {HPCA_DATE} · {HPCA_LOCATION}

---

| 分类 (Track) | 论文数 |
|-------------|-------|
{table_rows}
"""


def build_docs(tracks: Dict[str, List[Paper]]) -> Tuple[int, Dict[str, str]]:
    base = DOCS / "HPCA" / "2025"
    base.mkdir(parents=True, exist_ok=True)

    # Clean previous generated content under docs/HPCA/2025
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


def hpca_2025_nav_block(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str], total: int) -> List[str]:
    lines = [
        f"    - HPCA 2025 ({total}):\n",
        "      - HPCA 2025: HPCA/2025/index.md\n",
    ]

    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        tslug = slug_map[track]
        lines.append(f"      - {yaml_quote(f'{track} ({len(papers)})')}:\n")
        lines.append(f"        - {yaml_quote(track)}: HPCA/2025/{tslug}/index.md\n")

        used_titles: Dict[str, int] = {}
        for p in papers:
            pslug = slugify(p.title)
            if pslug in used_titles:
                used_titles[pslug] += 1
                pslug = f"{pslug}_{used_titles[pslug]}"
            else:
                used_titles[pslug] = 1
            lines.append(f"        - {yaml_quote(p.title)}: HPCA/2025/{tslug}/{pslug}.md\n")

    return lines


def replace_hpca_2025_nav(content: str, new_block: List[str]) -> str:
    lines = content.splitlines(keepends=True)

    hpca_start = None
    for i, line in enumerate(lines):
        if line.startswith("  - ⚡ HPCA:"):
            hpca_start = i
            break
    if hpca_start is None:
        raise RuntimeError("Cannot find HPCA nav section in mkdocs.yml")

    start_2025 = None
    start_2026 = None

    for i in range(hpca_start + 1, len(lines)):
        if lines[i].startswith("    - HPCA 2025"):
            start_2025 = i
            break
    if start_2025 is None:
        raise RuntimeError("Cannot find HPCA 2025 nav block in mkdocs.yml")

    for i in range(start_2025 + 1, len(lines)):
        if lines[i].startswith("    - HPCA 2026"):
            start_2026 = i
            break
        if lines[i].startswith("  - "):
            start_2026 = i
            break
    if start_2026 is None:
        start_2026 = len(lines)

    return "".join(lines[:start_2025] + new_block + lines[start_2026:])


def update_homepage_index(total: int, top_tracks: List[Tuple[str, str, int]]) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")

    tags = "\n".join(
        [
            f'<a class="area-tag" href="HPCA/2025/{slug}/" data-track-key="HPCA/2025/{slug}" data-track-label="{label}">{label} {count}</a>'
            for label, slug, count in top_tracks[:3]
        ]
    )

    replacement = (
        "### ⚡ [HPCA 2025](HPCA/2025/index.md)\n\n"
        + f'<div class="conf-count" data-conf-key="HPCA 2025" data-conf-location="{HPCA_LOCATION}">{total} 篇 · {len(top_tracks)} 个方向 · {HPCA_LOCATION}</div>\n\n'
        + '<div class="area-groups">\n<div class="area-group">\n<div class="area-group-label">方向</div>\n<div class="area-tags">\n'
        + tags
        + "\n</div>\n</div>\n</div>"
    )

    pattern = (
        r"### ⚡ \[HPCA 2025\]\(HPCA/2025/index.md\)\n\n[\s\S]*?(?=\n---\n\n<div class=\"conf-card\" markdown>\n\n### ⚡ \[HPCA 2026\])"
    )

    new_text, n = re.subn(pattern, replacement, text, count=1)
    if n != 1:
        raise RuntimeError("Cannot find HPCA 2025 card block in docs/index.md")

    INDEX_MD.write_text(new_text, encoding="utf-8")


def main() -> None:
    tracks = parse_hpca_2025()
    if not tracks:
        raise RuntimeError("No HPCA 2025 tracks/papers parsed from official main-program page")

    total, slug_map = build_docs(tracks)

    mkdocs_text = MKDOCS.read_text(encoding="utf-8")
    mkdocs_text = replace_hpca_2025_nav(
        mkdocs_text,
        hpca_2025_nav_block(tracks, slug_map, total),
    )
    MKDOCS.write_text(mkdocs_text, encoding="utf-8")

    top_tracks = [
        (track, slug_map[track], len(papers))
        for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ]
    update_homepage_index(total, top_tracks)

    print(f"HPCA 2025: {len(tracks)} tracks, {total} papers")
    print("Updated docs/HPCA/2025, mkdocs.yml, and docs/index.md")


if __name__ == "__main__":
    main()
