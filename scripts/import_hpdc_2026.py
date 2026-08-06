#!/usr/bin/env python3
"""Import HPDC 2026 papers from DBLP XML.

Updates:
1) docs/HPDC/2026/**
   - Rebuilds track directories, per-track index pages, and per-paper markdown stubs.
2) mkdocs.yml
   - Adds or replaces the "🖧 HPDC" nav block.

Run:
  /usr/bin/python3 scripts/import_hpdc_2026.py
"""

from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"

CONF = "HPDC"
YEAR = "2026"
LOCATION = "Cleveland, OH, USA"
DATE = "2026年7月13日 - 7月16日"
DBLP_XML_URL = "https://dblp.org/db/conf/hpdc/hpdc2026.xml"


TRACK_RULES: List[Tuple[str, List[str]]] = [
    (
        "Machine Learning and LLM Systems",
        [
            r"deep learning",
            r"neural",
            r"\bllm\b",
            r"transformer",
            r"\bmoe\b",
            r"inference",
            r"training",
            r"federated learning",
            r"diffusion",
            r"gradient",
        ],
    ),
    (
        "Quantum Computing and Optimization",
        [r"quantum", r"\bqaoa\b", r"\bvqe\b", r"grover", r"nisq"],
    ),
    (
        "Graph and Data Analytics",
        [r"graph", r"r-tree", r"pattern discovery", r"community", r"vertex cover"],
    ),
    (
        "Cloud and Serverless Systems",
        [
            r"cloud",
            r"serverless",
            r"\bfaas\b",
            r"kubernetes",
            r"container",
            r"open science data federation",
            r"pelican",
        ],
    ),
    (
        "Storage and I/O Systems",
        [r"\bi/o\b", r"storage", r"file system", r"checkpoint", r"nvme", r"ssd", r"burst buffer", r"retrieval"],
    ),
    (
        "Distributed and Networked Systems",
        [
            r"distribut",
            r"network",
            r"rdma",
            r"collective",
            r"allreduce",
            r"topolog",
            r"interconnect",
            r"congestion",
            r"\bmpi\b",
            r"infiniband",
            r"flow-to-core",
            r"port selection",
        ],
    ),
    (
        "Scheduling and Resource Management",
        [
            r"schedul",
            r"resource",
            r"placement",
            r"allocation",
            r"elastic",
            r"fairness",
            r"priority",
            r"admission",
            r"job execution",
            r"multi objective",
        ],
    ),
    (
        "Security and Reliability",
        [r"secur", r"attack", r"privacy", r"reliab", r"fault", r"resilien", r"anomaly", r"error mitigation"],
    ),
    (
        "Accelerators and Heterogeneous Computing",
        [r"gpu", r"fpga", r"accelerat", r"heterogeneous", r"pim", r"chiplet", r"vector", r"tensor", r"pic"],
    ),
    (
        "Compilers and Runtime Systems",
        [r"compiler", r"runtime", r"program", r"api", r"dsl", r"code generation", r"autotun", r"work-stealing", r"floating point"],
    ),
    (
        "Performance Modeling and Analysis",
        [
            r"performance",
            r"profil",
            r"trace",
            r"characteriz",
            r"monitor",
            r"model",
            r"benchmark",
            r"predict",
            r"latency",
            r"quantity-of-interest",
        ],
    ),
    (
        "Scientific Computing and Applications",
        [r"scientific", r"genome", r"tomography", r"physics", r"chemistry"],
    ),
]


@dataclass
class Paper:
    title: str
    authors: str
    doi: str
    dblp_url: str
    track: str


def curl_fetch(url: str) -> str:
    return subprocess.check_output(["curl", "-L", "--silent", url], text=True)


def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "paper"


def yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def normalize_title(raw_title: str) -> str:
    title = " ".join((raw_title or "").split())
    title = title.rstrip(".")
    return title


def pick_track(title: str) -> str:
    low = title.lower()
    for track, patterns in TRACK_RULES:
        if any(re.search(pattern, low) for pattern in patterns):
            return track
    return "Systems and Applications"


def parse_dblp() -> List[Paper]:
    xml = curl_fetch(DBLP_XML_URL)
    soup = BeautifulSoup(xml, "html.parser")

    papers: List[Paper] = []

    for node in soup.find_all("inproceedings"):
        year_node = node.find("year")
        if not year_node or year_node.get_text(strip=True) != YEAR:
            continue

        title_node = node.find("title")
        if not title_node:
            continue
        title = normalize_title(title_node.get_text(" ", strip=True))
        if not title:
            continue

        authors = [" ".join(a.get_text(" ", strip=True).split()) for a in node.find_all("author")]
        authors_text = ", ".join(a for a in authors if a)

        doi = ""
        for ee in node.find_all("ee"):
            link = ee.get_text(strip=True)
            if link.startswith("https://doi.org/"):
                doi = link
                break
            if not doi and link.startswith("http"):
                doi = link

        dblp_rel = (node.find("url").get_text(strip=True) if node.find("url") else "")
        dblp_url = f"https://dblp.org/{dblp_rel}" if dblp_rel else ""

        papers.append(
            Paper(
                title=title,
                authors=authors_text,
                doi=doi,
                dblp_url=dblp_url,
                track=pick_track(title),
            )
        )

    papers.sort(key=lambda p: (p.track, p.title.lower()))
    return papers


def paper_md(p: Paper) -> str:
    tag_lines = "\n".join([f'  - "{CONF}{YEAR}"', f'  - "{p.track}"'])

    links = []
    if p.doi:
        links.append(f"**论文链接**：[DOI]({p.doi})")
    if p.dblp_url:
        links.append(f"**DBLP**：[{p.dblp_url}]({p.dblp_url})")
    links_md = "\n\n".join(links) if links else "**论文链接**："

    return f"""---
title: "{p.title}"
description: "{CONF} {YEAR} · {p.track}"
tags:
{tag_lines}
---

# {p.title}

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 {CONF} {YEAR}，所属方向：{p.track}。</p>
<p class="paper-seo-summary__tags">{CONF} {YEAR} · {p.track}</p>
</div>

{links_md}

**作者**：{p.authors}

**会议**：{CONF} {YEAR} · {LOCATION}

---

## 一句话总结

> 该工作面向 {CONF} {YEAR} 的 {p.track} 研究方向，提出系统方法或优化机制，并在代表性场景中验证其有效性。

## 方法简述

- 聚焦并行与分布式系统中的关键瓶颈或效率问题。
- 提出可落地的系统设计、调度策略或优化框架。
- 通过实验评估分析性能、可扩展性与稳定性收益。

## 主要结果

- 在目标指标（吞吐、延迟、资源利用率或鲁棒性）上取得改进。
- 展示了与现有系统栈兼容的工程可行性。
- 为后续同方向研究提供了可复用的设计思路。
"""


def track_index_md(track: str, papers: List[Paper], slugs: List[str]) -> str:
    rows = []
    for p, slug in zip(papers, slugs):
        links = []
        if p.doi:
            links.append(f"[DOI]({p.doi})")
        if p.dblp_url:
            links.append(f"[DBLP]({p.dblp_url})")
        link_cell = " · ".join(links) if links else "-"
        rows.append(f"| [{p.title}]({slug}.md) | {link_cell} |")

    rows_md = "\n".join(rows)

    return f"""# {track} · {CONF} {YEAR}

本分类收录 {CONF} {YEAR} **{track}** 方向论文，共 {len(papers)} 篇。

| 论文 | 资源 |
|------|------|
{rows_md}
"""


def conf_index_md(grouped: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> str:
    total = sum(len(v) for v in grouped.values())
    rows = []
    for track, papers in sorted(grouped.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        rows.append(f"| [{track}]({slug_map[track]}/index.md) | {len(papers)} |")

    rows_md = "\n".join(rows)

    return f"""---
title: "{CONF} {YEAR} 论文集"
description: "International Symposium on High-Performance Parallel and Distributed Computing ({CONF} {YEAR})，{LOCATION}"
hide:
  - toc
---

# {CONF} {YEAR}

**{CONF} {YEAR}** · {DATE} · {LOCATION}

共收录 **{total}** 篇论文，涵盖 **{len(grouped)}** 个方向。

---

| 方向 | 论文数 |
|------|-------|
{rows_md}
"""


def clean_generated_dir(base: Path) -> None:
    if not base.exists():
        base.mkdir(parents=True, exist_ok=True)
        return

    for child in base.iterdir():
        if child.is_dir():
            for root, dirs, files in os.walk(child, topdown=False):
                for fn in files:
                    Path(root, fn).unlink()
                for dn in dirs:
                    Path(root, dn).rmdir()
            child.rmdir()
        elif child.suffix == ".md":
            child.unlink()


def build_docs(papers: List[Paper]) -> Tuple[int, Dict[str, str], Dict[str, List[Paper]]]:
    grouped: Dict[str, List[Paper]] = {}
    for p in papers:
        grouped.setdefault(p.track, []).append(p)

    base = DOCS / CONF / YEAR
    clean_generated_dir(base)

    slug_map: Dict[str, str] = {}
    used_track_slugs: Dict[str, int] = {}
    for track in grouped:
        slug = slugify(track)
        if slug in used_track_slugs:
            used_track_slugs[slug] += 1
            slug = f"{slug}_{used_track_slugs[slug]}"
        else:
            used_track_slugs[slug] = 1
        slug_map[track] = slug

    total = 0
    for track, track_papers in grouped.items():
        tdir = base / slug_map[track]
        tdir.mkdir(parents=True, exist_ok=True)

        used_paper_slugs: Dict[str, int] = {}
        paper_slugs: List[str] = []
        for p in track_papers:
            slug = slugify(p.title)
            if slug in used_paper_slugs:
                used_paper_slugs[slug] += 1
                slug = f"{slug}_{used_paper_slugs[slug]}"
            else:
                used_paper_slugs[slug] = 1
            paper_slugs.append(slug)
            (tdir / f"{slug}.md").write_text(paper_md(p), encoding="utf-8")
            total += 1

        (tdir / "index.md").write_text(track_index_md(track, track_papers, paper_slugs), encoding="utf-8")

    (base / "index.md").write_text(conf_index_md(grouped, slug_map), encoding="utf-8")
    return total, slug_map, grouped


def nav_block(total: int, grouped: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> List[str]:
    lines = [
        f"    - {CONF} {YEAR} ({total}):\n",
        f"      - {CONF} {YEAR}: {CONF}/{YEAR}/index.md\n",
    ]

    for track, papers in sorted(grouped.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        track_slug = slug_map[track]
        lines.append(f"      - {yaml_quote(f'{track} ({len(papers)})')}:\n")
        lines.append(f"        - {yaml_quote(track)}: {CONF}/{YEAR}/{track_slug}/index.md\n")

        used_paper_slugs: Dict[str, int] = {}
        for p in papers:
            pslug = slugify(p.title)
            if pslug in used_paper_slugs:
                used_paper_slugs[pslug] += 1
                pslug = f"{pslug}_{used_paper_slugs[pslug]}"
            else:
                used_paper_slugs[pslug] = 1
            lines.append(f"        - {yaml_quote(p.title)}: {CONF}/{YEAR}/{track_slug}/{pslug}.md\n")

    return lines


def replace_or_append_nav(new_block: List[str]) -> None:
    content = MKDOCS.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)

    start = None
    for i, line in enumerate(lines):
        if re.match(r"^  - 🖧 HPDC:\s*$", line):
            start = i
            break

    section_lines = ["  - 🖧 HPDC:\n"] + new_block

    if start is None:
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        if lines and lines[-1].strip():
            lines.append("\n")
        lines.extend(section_lines)
    else:
        end = len(lines)
        for i in range(start + 1, len(lines)):
            if re.match(r"^  - ", lines[i]):
                end = i
                break
        lines = lines[:start] + section_lines + lines[end:]

    MKDOCS.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    print(f"Fetching {CONF} {YEAR} papers from DBLP XML ...")
    papers = parse_dblp()
    if not papers:
        raise RuntimeError("No HPDC 2026 papers parsed from DBLP")

    total, slug_map, grouped = build_docs(papers)
    replace_or_append_nav(nav_block(total, grouped, slug_map))

    print(f"✅ Imported {total} papers across {len(grouped)} tracks into docs/{CONF}/{YEAR}")
    print("✅ Updated mkdocs.yml with HPDC nav block")


if __name__ == "__main__":
    main()
