#!/usr/bin/env python3
"""Import FAST 2025 accepted papers from USENIX technical-sessions page.

Updates:
1) docs/FAST/2025/**  – session directories, index pages, per-paper markdown stubs
2) mkdocs.yml         – rebuilds the FAST 2025 nav block
3) docs/index.md      – updates the FAST 2025 card count & stat

Run:
  python3 scripts/import_fast_2025.py
"""
from __future__ import annotations
import os, re, subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
INDEX_MD = DOCS / "index.md"

CONF = "FAST"
YEAR = "2025"
LOCATION = "Santa Clara, CA"
DATE = "2025年2月25日 - 2月27日"
URL = "https://www.usenix.org/conference/fast25/technical-sessions"
BASE_URL = "https://www.usenix.org"
# Sessions to skip (not regular papers)
SKIP_SESSIONS = {"Opening", "Keynote Address", "Closing Remarks", "Awards", "Keynote", "Award", "Reception"}


@dataclass
class Paper:
    title: str
    authors: str
    pdf: str = ""
    slides: str = ""
    video: str = ""
    page_url: str = ""


def curl_fetch(url: str) -> str:
    return subprocess.check_output(["curl", "-L", "--silent", url], text=True)


def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "paper"


def yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse_usenix_sessions(html: str, conf_slug: str, year: str) -> Dict[str, List[Paper]]:
    """Parse USENIX technical-sessions page into {session_name: [Paper, ...]}."""
    soup = BeautifulSoup(html, "html.parser")
    tracks: Dict[str, List[Paper]] = {}

    sessions = soup.find_all("article", class_=lambda c: c and "node-session" in (c or ""))
    for sess in sessions:
        # Get session name from h2
        h2 = sess.find("h2")
        sess_name = h2.get_text(strip=True) if h2 else ""
        # Skip non-paper sessions
        if not sess_name:
            continue
        # Skip non-paper sessions
        if any(sess_name.lower() == skip.lower() or sess_name.lower().startswith(skip.lower() + " ") for skip in SKIP_SESSIONS):
            continue
        # Clean up session name (remove "Session N:" prefix or extra info)
        sess_name = re.sub(r"^Session\s+\d+[:\-]\s*", "", sess_name).strip()

        papers_articles = sess.find_all("article", class_=lambda c: c and "node-paper" in (c or ""))
        for pap in papers_articles:
            # Title
            h2_pap = pap.find("h2")
            if not h2_pap:
                continue
            a_tag = h2_pap.find("a")
            if a_tag:
                title = a_tag.get_text(" ", strip=True)
                page_url = BASE_URL + a_tag.get("href", "")
            else:
                title = h2_pap.get_text(" ", strip=True)
                page_url = ""
            title = " ".join(title.split())
            if not title:
                continue

            # Authors
            auth_div = pap.find("div", class_=lambda c: c and "presented-by" in (c or ""))
            authors = " ".join(auth_div.get_text(" ", strip=True).split()) if auth_div else ""

            # Media links (PDF, slides, video) from group-available-media
            media_div = pap.find("div", class_=lambda c: c and "group-available-media" in (c or ""))
            pdf = slides = video = ""
            if media_div:
                for a in media_div.find_all("a", href=True):
                    href = a["href"]
                    if not href.startswith("http"):
                        href = BASE_URL + href
                    txt = a.get_text(strip=True).lower()
                    if href.endswith(".pdf") and "slide" in href.lower():
                        slides = href
                    elif href.endswith(".pdf"):
                        pdf = href
                    elif "video" in txt or "youtube" in href or "usenix.org" in href and "video" in txt:
                        video = href

            tracks.setdefault(sess_name, []).append(
                Paper(title=title, authors=authors, pdf=pdf, slides=slides, video=video, page_url=page_url)
            )

    return tracks


def paper_md(track: str, p: Paper) -> str:
    tags = [f"{CONF}{YEAR}", track]
    tag_lines = "\n".join(f'  - "{t}"' for t in tags)

    links = []
    if p.pdf:
        links.append(f"**论文 PDF**：[下载 PDF]({p.pdf})")
    if p.slides:
        links.append(f"**幻灯片**：[下载 Slides]({p.slides})")
    if p.video:
        links.append(f"**视频**：[观看视频]({p.video})")
    if p.page_url:
        links.append(f"**USENIX 页面**：[{p.page_url}]({p.page_url})")
    links_md = "\n\n".join(links) or "**论文链接**："

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

{links_md}

**作者**：{p.authors}

**会议**：{CONF} {YEAR} · {LOCATION}

---

## 一句话总结

> 该工作属于 {track} 方向，探索文件与存储系统领域的关键优化问题，在 {CONF} {YEAR} 语境下验证其价值。

## 方法简述

- 识别文件/存储系统的关键性能或可靠性瓶颈。
- 提出针对性的系统设计或优化方案。
- 在真实或模拟工作负载上进行充分评估。

## 主要结果

- 在性能、可靠性或资源效率方面相对基线实现改进。
- 展示与现有存储栈的兼容性与可部署性。
- 为后续存储系统研究提供新的设计思路。
"""


def track_index_md(track: str, papers: List[Paper], slugs: List[str]) -> str:
    rows = []
    for p, s in zip(papers, slugs):
        links = []
        if p.pdf:
            links.append(f"[PDF]({p.pdf})")
        if p.slides:
            links.append(f"[Slides]({p.slides})")
        link_cell = " · ".join(links) if links else "-"
        rows.append(f"| [{p.title}]({s}.md) | {link_cell} |")
    table = "\n".join(rows)
    return f"""# {track} · {CONF} {YEAR}

本分类收录 {CONF} {YEAR} **{track}** Session 的论文，共 {len(papers)} 篇。

| 论文 | 资源 |
|------|------|
{table}
"""


def conf_index_md(tracks: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> str:
    total = sum(len(v) for v in tracks.values())
    rows = "\n".join(
        f"| [{t}]({slug_map[t]}/index.md) | {len(p)} |"
        for t, p in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    )
    return f"""---
title: "{CONF} {YEAR} 论文集"
description: "USENIX 文件与存储技术大会 {CONF} {YEAR}，{LOCATION}"
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
    # Clean previous
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
    used: Dict[str, int] = {}
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
        if re.match(r"  - 💾 FAST:", l):
            start = i; break
    if start is None:
        raise RuntimeError("Cannot find '💾 FAST:' nav section in mkdocs.yml")
    # Find first child sub-block start (4-space indented lines after start)
    sub_start = None
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("    - "):
            sub_start = i; break
    if sub_start is None:
        # No sub-items yet; insert after the section line
        sub_start = start + 1
        end = start + 1
    else:
        # Find end: next top-level nav item at "  - "
        for i in range(sub_start, len(lines)):
            if lines[i].startswith("  - "):
                end = i; break
        if end is None:
            end = len(lines)
    return "".join(lines[:sub_start] + new_block + lines[end:])


def update_index(total: int, tracks: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")
    replacement = (
        f'  <div class="conf-cube__stat" data-conf-key="{CONF} {YEAR}">'
        f'{total} 篇 · {LOCATION}</div>'
    )
    # Update cube stat
    text = re.sub(
        rf'(<div class="conf-cube conf-cube--fast">.*?<div class="conf-cube__stat")[^<]*(</div>)',
        lambda m: m.group(1) + f' data-conf-key="{CONF} {YEAR}">' + f'{total} 篇 · {LOCATION}' + m.group(2),
        text, flags=re.DOTALL
    )
    INDEX_MD.write_text(text, encoding="utf-8")


def main() -> None:
    print(f"Fetching {CONF} {YEAR} from {URL} ...")
    html = curl_fetch(URL)
    tracks = parse_usenix_sessions(html, CONF.lower(), YEAR)
    if not tracks:
        raise RuntimeError(f"No tracks parsed from {URL}")

    print(f"Parsed {len(tracks)} tracks:")
    for t, ps in sorted(tracks.items(), key=lambda kv: -len(kv[1])):
        print(f"  {t}: {len(ps)} papers")

    total, slug_map = build_docs(tracks)
    print(f"\nBuilt {total} paper stubs in {len(tracks)} tracks.")

    mkdocs = MKDOCS.read_text(encoding="utf-8")
    mkdocs = replace_nav(mkdocs, nav_block(tracks, slug_map, total))
    MKDOCS.write_text(mkdocs, encoding="utf-8")
    print("Updated mkdocs.yml.")

    update_index(total, tracks, slug_map)
    print("Updated docs/index.md.")

    print(f"\nDone: {CONF} {YEAR} — {len(tracks)} tracks, {total} papers")


if __name__ == "__main__":
    main()
