#!/usr/bin/env python3
"""Import PPoPP 2025 accepted papers from the SIGPLAN program page.

Updates:
1) docs/PPoPP/2025/**  – session directories, index pages, per-paper markdown stubs
2) mkdocs.yml          – rebuilds the PPoPP 2025 nav block
3) docs/index.md       – updates the PPoPP 2025 card count & stat

Run:
  python3 scripts/import_ppopp_2025.py
"""
from __future__ import annotations
import os, re, subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
INDEX_MD = DOCS / "index.md"

CONF = "PPoPP"
YEAR = "2025"
LOCATION = "Las Vegas, NV"
DATE = "2025年3月1日 - 3月5日"
URL = "https://ppopp25.sigplan.org/program/program-PPoPP-2025/"


@dataclass
class Paper:
    title: str
    authors: str


def curl_fetch(url: str) -> str:
    return subprocess.check_output(["curl", "-L", "--silent", url], text=True)


def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "paper"


def yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse_ppopp(html: str) -> Dict[str, List[Paper]]:
    """Parse PPoPP SIGPLAN program page into {session_name: [Paper, ...]}."""
    soup = BeautifulSoup(html, "html.parser")
    tracks: Dict[str, List[Paper]] = {}

    session_tables = soup.find_all("table", class_="session-table")
    for tbl in session_tables:
        rows = tbl.find_all("tr")
        if not rows:
            continue

        # Get session name from first row (class 'session-details')
        session_name = ""
        details_row = None
        for r in rows:
            if "session-details" in (r.get("class") or []):
                details_row = r
                break
        if details_row:
            detail_text = details_row.get_text(" ", strip=True)
            # Pattern: "HH:MM - HH:MM Session N: Topic (Session Chair: ...) Main Conference at Room"
            m = re.search(r"Session\s+\d+:\s*(.+?)\s*\(Session Chair:", detail_text)
            if m:
                session_name = m.group(1).strip()
            else:
                # Try simpler pattern
                m2 = re.search(r"Session\s+\d+:\s*(.+?)\s+Main Conference", detail_text)
                if m2:
                    session_name = m2.group(1).strip()

        if not session_name:
            continue

        # Get papers from 'hidable' rows that have "Main Conference" and "Talk"
        for r in rows:
            if "hidable" not in (r.get("class") or []):
                continue
            row_text = r.get_text(" ", strip=True)
            # Filter: must have "Main Conference" and end-time with "Talk"
            if "Main Conference" not in row_text:
                continue
            # Pattern: "[time] [duration]m Talk [Title] Main Conference [Authors]"
            m = re.search(r"\d+m\s+Talk\s+(.+?)\s+Main Conference\s+(.+)$", row_text)
            if not m:
                continue
            title = " ".join(m.group(1).split())
            authors_raw = " ".join(m.group(2).split())
            # Clean authors: format is "FirstName LastName Affiliation , FirstName LastName Affiliation"
            # We'll keep as is for now
            authors = authors_raw.strip()
            if not title or len(title) < 5:
                continue
            tracks.setdefault(session_name, []).append(Paper(title=title, authors=authors))

    return tracks


def paper_md(track: str, p: Paper) -> str:
    tags = [f"{CONF}{YEAR}", track]
    tag_lines = "\n".join(f'  - "{t}"' for t in tags)
    return f"""---
title: "{p.title}"
description: "{CONF} {YEAR} · {track} · {p.authors[:80]}"
tags:
{tag_lines}
---

# {p.title}

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 {CONF} {YEAR}，所属方向：{track}。</p>
<p class="paper-seo-summary__tags">{CONF} {YEAR} · {track}</p>
</div>

**作者**：{p.authors}

**会议**：{CONF} {YEAR} · {LOCATION}

---

## 一句话总结

> 该工作属于 {track} 方向，在并行编程与性能优化领域提出关键设计，在 {CONF} {YEAR} 语境下验证其价值。

## 方法简述

- 识别并行计算或多核系统中的核心性能或正确性挑战。
- 提出针对性的编程模型、运行时系统或优化算法。
- 在多核、众核或分布式系统上进行充分评估。

## 主要结果

- 在并行效率、可扩展性或代码可移植性方面相对基线实现改进。
- 为 {track} 领域提供新的设计视角与优化策略。
"""


def track_index_md(track: str, papers: List[Paper], slugs: List[str]) -> str:
    rows = "\n".join(f"| [{p.title}]({s}.md) | {p.authors[:60]} |" for p, s in zip(papers, slugs))
    return f"""# {track} · {CONF} {YEAR}

本分类收录 {CONF} {YEAR} **{track}** Session 的论文，共 {len(papers)} 篇。

| 论文 | 作者 |
|------|------|
{rows}
"""


def conf_index_md(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> str:
    total = sum(len(v) for v in tracks.values())
    rows = "\n".join(
        f"| [{t}]({slug_map[t]}/index.md) | {len(p)} |"
        for t, p in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    )
    return f"""---
title: "{CONF} {YEAR} 论文集"
description: "ACM SIGPLAN 并行编程与性能优化大会 {CONF} {YEAR}，{LOCATION}"
hide:
  - toc
---

# {CONF} {YEAR}

**{CONF} {YEAR}** · {DATE} · {LOCATION}

共收录 **{total}** 篇论文，涵盖 **{len(tracks)}** 个方向。

---

| 方向 | 论文数 |
|------|-------|
{rows}
"""


def build_docs(tracks: Dict[str, List[Paper]]) -> Tuple[int, Dict[str, str]]:
    base = DOCS / CONF / YEAR
    base.mkdir(parents=True, exist_ok=True)
    for child in base.iterdir():
        if child.is_dir():
            for r, ds, fs in os.walk(child, topdown=False):
                for f in fs:
                    Path(r, f).unlink()
                for d in ds:
                    Path(r, d).rmdir()
            child.rmdir()
        elif child.name.endswith(".md"):
            child.unlink()

    slug_map: Dict[str, str] = {}
    used_slugs: Dict[str, int] = {}
    for t in tracks:
        s = slugify(t)
        if s in used_slugs:
            used_slugs[s] += 1; s = f"{s}_{used_slugs[s]}"
        else:
            used_slugs[s] = 1
        slug_map[t] = s

    total = 0
    for track, papers in tracks.items():
        tdir = base / slug_map[track]
        tdir.mkdir(parents=True, exist_ok=True)
        used: Dict[str, int] = {}
        paper_slugs: List[str] = []
        for p in papers:
            ps = slugify(p.title)
            if ps in used:
                used[ps] += 1; ps = f"{ps}_{used[ps]}"
            else:
                used[ps] = 1
            paper_slugs.append(ps)
            (tdir / f"{ps}.md").write_text(paper_md(track, p), encoding="utf-8")
            total += 1
        (tdir / "index.md").write_text(track_index_md(track, papers, paper_slugs), encoding="utf-8")

    (base / "index.md").write_text(conf_index_md(tracks, slug_map), encoding="utf-8")
    return total, slug_map


def nav_block(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str], total: int) -> List[str]:
    lines = [
        f"    - {CONF} {YEAR} ({total}):\n",
        f"      - {CONF} {YEAR}: {CONF}/{YEAR}/index.md\n",
    ]
    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        tslug = slug_map[track]
        lines.append(f"      - {yaml_quote(f'{track} ({len(papers)})')}:\n")
        lines.append(f"        - {yaml_quote(track)}: {CONF}/{YEAR}/{tslug}/index.md\n")
        used_p: Dict[str, int] = {}
        for p in papers:
            ps = slugify(p.title)
            if ps in used_p:
                used_p[ps] += 1; ps = f"{ps}_{used_p[ps]}"
            else:
                used_p[ps] = 1
            lines.append(f"        - {yaml_quote(p.title)}: {CONF}/{YEAR}/{tslug}/{ps}.md\n")
    return lines


def replace_nav(content: str, new_block: List[str]) -> str:
    lines = content.splitlines(keepends=True)
    start = end = None
    for i, l in enumerate(lines):
        if re.match(r"  - ⚡ PPoPP:", l):
            start = i; break
    if start is None:
        raise RuntimeError("Cannot find '⚡ PPoPP:' nav section in mkdocs.yml")
    sub_start = None
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("    - "):
            sub_start = i; break
    if sub_start is None:
        sub_start = start + 1
        end = start + 1
    else:
        for i in range(sub_start, len(lines)):
            if lines[i].startswith("  - "):
                end = i; break
        if end is None:
            end = len(lines)
    return "".join(lines[:sub_start] + new_block + lines[end:])


def update_index(total: int) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")
    text = re.sub(
        r'(<div class="conf-cube conf-cube--ppopp">.*?<div class="conf-cube__stat")[^<]*(</div>)',
        lambda m: m.group(1) + f' data-conf-key="{CONF} {YEAR}">{total} 篇 · {LOCATION}' + m.group(2),
        text, flags=re.DOTALL
    )
    INDEX_MD.write_text(text, encoding="utf-8")


def main() -> None:
    print(f"Fetching {CONF} {YEAR} from {URL} ...")
    html = curl_fetch(URL)
    tracks = parse_ppopp(html)
    if not tracks:
        raise RuntimeError(f"No tracks parsed from {URL}. The page structure may have changed.")

    print(f"Parsed {len(tracks)} tracks:")
    for t, ps in sorted(tracks.items(), key=lambda kv: -len(kv[1])):
        print(f"  {t}: {len(ps)} papers")

    total, slug_map = build_docs(tracks)
    print(f"\nBuilt {total} paper stubs in {len(tracks)} tracks.")

    mkdocs = MKDOCS.read_text(encoding="utf-8")
    mkdocs = replace_nav(mkdocs, nav_block(tracks, slug_map, total))
    MKDOCS.write_text(mkdocs, encoding="utf-8")
    print("Updated mkdocs.yml.")

    update_index(total)
    print("Updated docs/index.md.")

    print(f"\nDone: {CONF} {YEAR} — {len(tracks)} tracks, {total} papers")


if __name__ == "__main__":
    main()
