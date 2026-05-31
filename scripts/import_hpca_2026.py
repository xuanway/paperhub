#!/usr/bin/env python3
"""Import HPCA 2026 accepted papers from the official main-conference track page.

What this script updates:
1) docs/HPCA/2026/**
   - Rebuilds track directories, track index pages, and per-paper markdown stubs.
2) mkdocs.yml
   - Rebuilds the HPCA 2026 nav block under "⚡ HPCA" and keeps HPCA 2025 unchanged.
3) docs/index.md
   - Updates the HPCA 2026 card count and top-track tags.

Source:
  https://2026.hpca-conf.org/track/hpca-2026-main-conference#program

Note:
  Track names are cleaned by removing the trailing "at ..." location suffix,
  e.g. "... at Collaroy" -> "...".

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

HPCA_URL = "https://2026.hpca-conf.org/track/hpca-2026-main-conference#program"
HPCA_LOCATION = "Sydney, Australia"
HPCA_DATE = "2026年2月28日 - 3月4日"


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


def _clean_text(text: str) -> str:
    return " ".join(text.split()).strip()


def _normalize_track(raw: str) -> str:
    t = _clean_text(raw)
    # Remove trailing session chair metadata.
    t = re.sub(r"\s+Chair\(s\):.*$", "", t, flags=re.I)
    # Keep text before location segment, e.g. "... at Collaroy".
    t = re.sub(r"\s+at\s+[^,;]+$", "", t, flags=re.I)
    # Strip trailing venue qualifier, e.g. "... Main Conference".
    t = re.sub(r"\s+Main Conference\s*$", "", t, flags=re.I)
    return t.strip()


def parse_hpca_2026() -> Dict[str, List[Paper]]:
    html = curl_fetch(HPCA_URL)
    soup = BeautifulSoup(html, "html.parser")

    tracks: Dict[str, List[Paper]] = {}
    seen_titles: set[str] = set()

    current_track: Optional[str] = None

    # Session headings and paper rows are sibling <tr> nodes in program tables.
    for tr in soup.find_all("tr"):
        classes = tr.get("class", [])

        if "session-details" in classes:
            info = tr.select_one("div.session-info-in-table")
            if info:
                current_track = _normalize_track(_clean_text(info.get_text(" ", strip=True)))
            continue

        slot_id = tr.get("data-slot-id")
        if not slot_id:
            continue

        event_type = _clean_text(tr.select_one("div.event-type").get_text(" ", strip=True)) if tr.select_one("div.event-type") else ""
        if event_type != "Talk":
            continue
        if not current_track:
            continue

        title_node = tr.select_one("a[data-event-modal]")
        title = _clean_text(title_node.get_text(" ", strip=True)) if title_node else ""
        if not title:
            continue

        # Same talk may appear multiple times in mirrored views; keep one copy.
        if title in seen_titles:
            continue
        seen_titles.add(title)

        performers = tr.select_one("div.performers")
        authors = _clean_text(performers.get_text(" ", strip=True)) if performers else ""

        doi = ""
        for a in tr.select("a[href]"):
            href = a.get("href", "")
            if "doi.org" in href:
                doi = href
                break

        tracks.setdefault(current_track, []).append(Paper(title=title, authors=authors, doi=doi))

    return tracks


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def paper_md(track: str, p: Paper) -> str:
    tags = ["HPCA2026", track]
    tag_lines = "\n".join([f'  - "{t}"' for t in tags])
    doi_line = f"**论文链接**：[{p.doi}]({p.doi})" if p.doi else "**论文链接**："
    return f"""---
title: "{p.title}"
description: "HPCA 2026 · {track}"
tags:
{tag_lines}
---

# {p.title}

<div class=\"paper-seo-summary\">
<p class=\"paper-seo-summary__desc\">该论文收录于 HPCA 2026，所属 Track: {track}。</p>
<p class=\"paper-seo-summary__tags\">HPCA 2026 · {track}</p>
</div>

{doi_line}
**作者**：{p.authors}
**会议**：HPCA 2026

---

## 一句话总结

> 该工作属于 {track} 方向，围绕关键系统瓶颈提出优化方案，并在 HPCA 2026 语境下验证其价值。

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
    return f"""# {track} · HPCA 2026

本分类收录 HPCA 2026 Track \"{track}\" 的论文。

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
title: "HPCA 2026 论文集"
description: "HPCA 2026 论文解读，{HPCA_LOCATION}"
search:
  exclude: false
hide:
  - toc
---

# HPCA 2026

**HPCA 2026** · {HPCA_DATE} · {HPCA_LOCATION}

---

| 分类 (Track) | 论文数 |
|-------------|-------|
{table_rows}
"""


def build_docs(tracks: Dict[str, List[Paper]]) -> Tuple[int, Dict[str, str]]:
    base = DOCS / "HPCA" / "2026"
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
        f"    - HPCA 2026 ({total}):\n",
        "      - HPCA 2026: HPCA/2026/index.md\n",
    ]

    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        tslug = slug_map[track]
        lines.append(f"      - {yaml_quote(f'{track} ({len(papers)})')}:\n")
        lines.append(f"        - {yaml_quote(track)}: HPCA/2026/{tslug}/index.md\n")

        used_titles: Dict[str, int] = {}
        for p in papers:
            pslug = slugify(p.title)
            if pslug in used_titles:
                used_titles[pslug] += 1
                pslug = f"{pslug}_{used_titles[pslug]}"
            else:
                used_titles[pslug] = 1
            lines.append(f"        - {yaml_quote(p.title)}: HPCA/2026/{tslug}/{pslug}.md\n")

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
    for i in range(hpca_start + 1, len(lines)):
        if lines[i].startswith("    - HPCA 2026"):
            start_2026 = i
            break
    if start_2026 is None:
        raise RuntimeError("Cannot find HPCA 2026 nav block in mkdocs.yml")

    end_2026 = len(lines)
    for i in range(start_2026 + 1, len(lines)):
        if lines[i].startswith("  - "):
            end_2026 = i
            break

    return "".join(lines[:start_2026] + new_block + lines[end_2026:])


def update_homepage_index(total: int, top_tracks: List[Tuple[str, str, int]]) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")

    tags = "\n".join(
        [
            f'<a class="area-tag" href="HPCA/2026/{slug}/" data-track-key="HPCA/2026/{slug}" data-track-label="{label}">{label} {count}</a>'
            for label, slug, count in top_tracks[:3]
        ]
    )

    replacement = (
        "### ⚡ [HPCA 2026](HPCA/2026/index.md)\n\n"
        + f'<div class="conf-count" data-conf-key="HPCA 2026" data-conf-location="{HPCA_LOCATION}">{total} 篇 · {len(top_tracks)} 个方向 · {HPCA_LOCATION}</div>\n\n'
        + '<div class="area-groups">\n<div class="area-group">\n<div class="area-group-label">方向</div>\n<div class="area-tags">\n'
        + tags
        + "\n</div>\n</div>\n</div>"
    )

    pattern = (
        r"### ⚡ \[HPCA 2026\]\(HPCA/2026/index.md\)\n\n[\s\S]*?(?=\n\n<div class=\"conf-card\" markdown>\n\n### 🏗️ \[ISCA 2025\])"
    )

    new_text, n = re.subn(pattern, replacement, text, count=1)
    if n != 1:
        raise RuntimeError("Cannot find HPCA 2026 card block in docs/index.md")

    INDEX_MD.write_text(new_text, encoding="utf-8")


def main() -> None:
    tracks = parse_hpca_2026()
    if not tracks:
        raise RuntimeError("No HPCA 2026 tracks/papers parsed from official track page")

    total, slug_map = build_docs(tracks)

    mkdocs_text = MKDOCS.read_text(encoding="utf-8")
    mkdocs_text = replace_hpca_2026_nav(
        mkdocs_text,
        hpca_2026_nav_block(tracks, slug_map, total),
    )
    MKDOCS.write_text(mkdocs_text, encoding="utf-8")

    top_tracks = [
        (track, slug_map[track], len(papers))
        for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ]
    update_homepage_index(total, top_tracks)

    print(f"HPCA 2026: {len(tracks)} tracks, {total} papers")
    print("Updated docs/HPCA/2026, mkdocs.yml, and docs/index.md")


if __name__ == "__main__":
    main()
