#!/usr/bin/env python3
"""Import SC 2025 accepted papers from the SC25 conference program.

Strategy:
1. Fetch the contributors page to discover all unique paper IDs.
2. For each paper ID, fetch the individual presentation page to get
   full title, session name, authors, and abstract.
3. Group papers by session name.
4. Write docs, patch mkdocs.yml, update index.md.

Updates:
1) docs/SC/2025/**  – session directories, index pages, per-paper markdown stubs
2) mkdocs.yml       – rebuilds the SC 2025 nav block
3) docs/index.md    – updates the SC 2025 card count & stat

Run:
  python3 scripts/import_sc_2025.py
"""
from __future__ import annotations
import os, re, subprocess, time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
INDEX_MD = DOCS / "index.md"

CONF = "SC"
YEAR = "2025"
LOCATION = "St. Louis, MO"
DATE = "2025年11月16日 - 11月21日"
CONTRIBUTORS_URL = "https://sc25.conference-program.com/contributors/"
PAPER_URL_TEMPLATE = "https://sc25.conference-program.com/?post_type=page&p=14&id={pap_id}&sess={sess_id}"


@dataclass
class Paper:
    title: str
    authors: str
    abstract: str = ""
    session: str = ""


def curl_fetch(url: str) -> str:
    result = subprocess.run(
        ["curl", "-L", "--silent", "-A", "Mozilla/5.0", url],
        capture_output=True, text=True, timeout=30
    )
    return result.stdout


def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "paper"


def yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def discover_papers(html: str) -> List[Dict]:
    """Extract unique paper IDs and session IDs from contributors page."""
    soup = BeautifulSoup(html, "html.parser")
    seen = set()
    papers = []
    for a in soup.find_all("a", href=True):
        m = re.search(r"id=(pap\d+)&sess=(sess\d+)", a["href"])
        if m:
            pap_id = m.group(1)
            if pap_id not in seen:
                seen.add(pap_id)
                papers.append({
                    "id": pap_id,
                    "sess": m.group(2),
                    "title_partial": a.get_text(strip=True),
                })
    return papers


def parse_paper_page(html: str) -> Tuple[str, str, str, str]:
    """Return (full_title, session_name, authors_str, abstract)."""
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(" ", strip=True)

    # The page text contains nav clutter followed by:
    # "Happening Now [TITLE] Session [SESSION] Description [ABSTRACT] Authors"
    # Split on "Happening Now" and take the last segment for the actual content
    parts = text.split("Happening Now")
    last_part = parts[-1].strip() if len(parts) >= 2 else text

    full_title = ""
    session_name = ""
    abstract = ""

    title_m = re.search(r"^(.+?)\s+Session\s+(.+?)\s+Description", last_part, re.DOTALL)
    if title_m:
        full_title = " ".join(title_m.group(1).split())
        session_name = " ".join(title_m.group(2).split())

    # Abstract: text after "Description" and before "Authors"
    abstract_m = re.search(r"Description\s+(.+?)\s+Authors\s+", last_part, re.DOTALL)
    abstract = " ".join(abstract_m.group(1).split())[:1000] if abstract_m else ""

    # Authors: from presenter-name elements
    names = [e.get_text(" ", strip=True) for e in soup.find_all("div", class_="presenter-name")]
    authors = "; ".join(names) if names else ""

    return full_title, session_name, authors, abstract


def paper_md(session: str, p: Paper) -> str:
    tags = [f"{CONF}{YEAR}", session]
    tag_lines = "\n".join(f'  - "{t}"' for t in tags)
    abstract_section = f"\n## 摘要\n\n{p.abstract}\n" if p.abstract else ""
    return f"""---
title: "{p.title}"
description: "{CONF} {YEAR} · {session} · {p.authors[:80]}"
tags:
{tag_lines}
---

# {p.title}

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 {CONF} {YEAR}，所属方向：{session}。</p>
<p class="paper-seo-summary__tags">{CONF} {YEAR} · {session}</p>
</div>

**作者**：{p.authors}

**会议**：{CONF} {YEAR} · {LOCATION}
{abstract_section}
---

## 一句话总结

> 该工作属于 {session} 方向，在高性能计算领域提出关键设计，在 {CONF} {YEAR} 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 {session} 领域贡献新的设计范式或评估框架。
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
description: "超算国际大会 {CONF} {YEAR}，{LOCATION}"
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
        if re.match(r"  - 🌩️ SC:", l):
            start = i; break
    if start is None:
        raise RuntimeError("Cannot find '🌩️ SC:' nav section in mkdocs.yml")
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
        r'(<div class="conf-cube conf-cube--sc">.*?<div class="conf-cube__stat")[^<]*(</div>)',
        lambda m: m.group(1) + f' data-conf-key="{CONF} {YEAR}">{total} 篇 · {LOCATION}' + m.group(2),
        text, flags=re.DOTALL
    )
    INDEX_MD.write_text(text, encoding="utf-8")


def main() -> None:
    print(f"Fetching contributors list from {CONTRIBUTORS_URL} ...")
    contrib_html = curl_fetch(CONTRIBUTORS_URL)
    paper_refs = discover_papers(contrib_html)
    if not paper_refs:
        raise RuntimeError("No paper IDs found on contributors page. The page structure may have changed.")
    print(f"Discovered {len(paper_refs)} unique papers.")

    tracks: Dict[str, List[Paper]] = {}
    failed = []
    for i, ref in enumerate(paper_refs):
        url = PAPER_URL_TEMPLATE.format(pap_id=ref["id"], sess_id=ref["sess"])
        print(f"  [{i+1}/{len(paper_refs)}] Fetching {ref['id']} ...", end=" ", flush=True)
        try:
            html = curl_fetch(url)
            full_title, session_name, authors, abstract = parse_paper_page(html)
            if not full_title:
                full_title = ref["title_partial"]
            if not session_name:
                session_name = "General"
            print(f"{full_title[:60]}")
            tracks.setdefault(session_name, []).append(
                Paper(title=full_title, authors=authors, abstract=abstract, session=session_name)
            )
        except Exception as e:
            print(f"FAILED: {e}")
            failed.append(ref)
        # Be polite to the server
        if i % 10 == 9:
            time.sleep(0.5)

    if failed:
        print(f"\nFailed to fetch {len(failed)} papers: {[f['id'] for f in failed]}")

    if not tracks:
        raise RuntimeError("No papers parsed. All fetches may have failed.")

    print(f"\nParsed {sum(len(p) for p in tracks.values())} papers in {len(tracks)} sessions.")
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

    print(f"\nDone: {CONF} {YEAR} — {len(tracks)} sessions, {total} papers")


if __name__ == "__main__":
    main()
