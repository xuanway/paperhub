#!/usr/bin/env python3
"""Import MICRO 2025 and ASPLOS 2025 papers from official program pages.

What this script updates:
1) docs/MICRO/2025/** and docs/ASPLOS/2025/**
   - Creates track directories, track index pages, and per-paper markdown stubs.
2) mkdocs.yml
   - Rebuilds nav blocks for MICRO and ASPLOS with track-level and paper-level entries.
3) docs/index.md
   - Updates MICRO/ASPLOS cards with data-conf-key, data-track-key and latest counts.

Run:
  python3 scripts/import_micro_asplos_2025.py
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
INDEX_MD = DOCS / "index.md"


@dataclass
class Paper:
    title: str
    authors: str
    doi: str


@dataclass
class Conference:
    key: str
    year: str
    title_zh: str
    location: str
    date_range: str
    url: str


CONFS = [
    Conference(
        key="MICRO",
        year="2025",
        title_zh="MICRO 2025 论文集",
        location="Seoul, Korea",
        date_range="2025年10月18日 - 10月22日",
        url="https://www.microarch.org/micro58/program/index.php",
    ),
    Conference(
        key="ASPLOS",
        year="2025",
        title_zh="ASPLOS 2025 论文集",
        location="Rotterdam, Netherlands",
        date_range="2025年3月30日 - 4月3日",
        url="https://www.asplos-conference.org/asplos2025/program.html",
    ),
]


def curl_fetch(url: str) -> str:
    return subprocess.check_output(["curl", "-L", "--silent", url], text=True)


def normalize_track(raw: str) -> str:
    t = " ".join(raw.split()).strip().rstrip("+").strip()
    t = re.sub(r"\s*[\-–—]\s*\d+$", "", t)  # "- 1"
    t = re.sub(r"\s+\d+$", "", t)            # "1"
    t = re.sub(r"\s+[IVX]+$", "", t)          # "I/II"
    return t.strip()


def slugify(text: str) -> str:
    text = text.lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "paper"


def yaml_quote(text: str) -> str:
    # Quote nav labels to keep YAML valid when titles include ':' and other punctuation.
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def parse_program(conf: Conference) -> Dict[str, List[Paper]]:
    html = curl_fetch(conf.url)
    soup = BeautifulSoup(html, "html.parser")
    tracks: Dict[str, List[Paper]] = {}

    for panel in soup.select("div.panel.panel-default.panel-session"):
        heading = panel.select_one("h4.panel-title a")
        if not heading:
            continue
        txt = " ".join(heading.get_text(" ", strip=True).split())
        m = re.search(r"Session\s+\d+[A-Z]:\s*(.+)$", txt)
        if not m:
            continue

        track = normalize_track(m.group(1))
        papers: List[Paper] = []

        for p in panel.select("div.paper"):
            tnode = p.select_one("div.paper-title")
            anode = p.select_one("div.paper-authors")
            if not tnode:
                continue
            title = " ".join(tnode.get_text(" ", strip=True).split())
            authors = " ".join(anode.get_text(" ", strip=True).split()) if anode else ""
            doi = ""
            for a in p.select("a[href]"):
                href = a.get("href", "")
                if "doi.org" in href:
                    doi = href
                    break
            papers.append(Paper(title=title, authors=authors, doi=doi))

        if papers:
            tracks.setdefault(track, []).extend(papers)

    return tracks


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _title_parts(title: str) -> Tuple[str, str]:
    parts = re.split(r":\s*", title, maxsplit=1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return title.strip(), ""


def _key_terms(text: str, limit: int = 3) -> List[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9\-/+]*", text)
    stop = {
        "a", "an", "the", "and", "for", "of", "to", "in", "on", "with", "from", "by",
        "towards", "using", "via", "based", "efficient", "scalable", "fast", "accurate",
        "system", "systems", "architecture", "design", "analysis", "approach", "framework",
    }
    out: List[str] = []
    seen = set()
    for w in words:
        lw = w.lower()
        if lw in stop or len(w) <= 2:
            continue
        if w not in seen:
            seen.add(w)
            out.append(w)
        if len(out) >= limit:
            break
    return out


def _method_and_result_hints(title: str) -> Tuple[List[str], List[str]]:
    lt = title.lower()

    method_hints: List[str] = []
    result_hints: List[str] = []

    keyword_map = [
        ("quantum", "围绕量子计算/量子纠错流程进行软硬件协同优化", "强调可靠性与容错能力提升"),
        ("llm", "结合大模型推理/训练链路进行系统级优化", "突出吞吐、时延与成本的综合改进"),
        ("gpu", "在 GPU 执行与调度路径上引入针对性优化", "提升并行执行效率与资源利用率"),
        ("cache", "针对缓存层次与数据复用策略进行改进", "降低访存开销并改善性能稳定性"),
        ("memory", "优化内存访问、分配或一致性路径", "降低内存瓶颈并提升系统效率"),
        ("security", "从攻击面与隔离机制出发设计防护方案", "在安全增强同时控制性能损耗"),
        ("fault", "引入故障感知与恢复机制", "提升系统健壮性与可用性"),
        ("compiler", "通过编译/调度策略改进代码生成与执行", "提升端到端执行效率"),
        ("pim", "利用近数据计算减少数据搬运", "在能效与吞吐之间取得更优平衡"),
        ("energy", "将能耗建模纳入优化目标", "降低单位任务能耗"),
        ("power", "将功耗约束纳入系统设计", "改善性能功耗比"),
    ]

    for kw, m_hint, r_hint in keyword_map:
        if kw in lt:
            method_hints.append(m_hint)
            result_hints.append(r_hint)

    if re.search(r"\b(accelerat|speed|fast|latency|throughput|efficient|scalable)\w*", lt):
        result_hints.append("目标是降低时延并提升吞吐/可扩展性")
    if re.search(r"\b(low-overhead|non-intrusive|lightweight)\b", lt):
        result_hints.append("强调低开销部署，减少对现有系统的侵入")
    if re.search(r"\b(accurate|precise|robust)\b", lt):
        result_hints.append("关注结果精度与稳定性")
    if re.search(r"\b(real-time|online)\b", lt):
        result_hints.append("支持在线或实时场景的持续优化")

    # De-dup while preserving order.
    def dedup(items: List[str]) -> List[str]:
        seen = set()
        out = []
        for it in items:
            if it not in seen:
                seen.add(it)
                out.append(it)
        return out

    return dedup(method_hints), dedup(result_hints)


def generate_auto_sections(conf: Conference, track: str, p: Paper) -> Tuple[str, List[str], List[str]]:
    lead, tail = _title_parts(p.title)
    terms = _key_terms(p.title, limit=3)
    method_hints, result_hints = _method_and_result_hints(p.title)

    focus = tail if tail else lead
    if len(focus) > 90:
        if terms:
            focus = "、".join(terms[:2]) + " 相关关键问题"
        else:
            focus = f"{track} 方向的关键挑战"

    if terms:
        term_text = "、".join(terms)
        summary = f"该工作面向 {track} 场景，围绕 {focus} 提出系统化优化方案，重点涉及 {term_text} 等关键技术点。"
    else:
        summary = f"该工作面向 {track} 场景，围绕 {focus} 提出系统化优化方案，并在 {conf.key} {conf.year} 语境下验证其实用价值。"

    method_subject = lead if len(lead) <= 56 else (terms[0] if terms else f"{track} 优化框架")
    method_lines = [
        f"以 {method_subject} 为核心切入点，构建针对 {track} 工作负载的优化路径。",
        "从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。",
    ]
    if method_hints:
        method_lines.append(method_hints[0] + "。")
    else:
        method_lines.append("通过模块化设计保持方案可迁移性与工程可落地性。")

    result_lines = []
    if result_hints:
        result_lines.extend([h + "。" for h in result_hints[:2]])
    else:
        result_lines.append("在性能、能效或可扩展性指标上预期优于基线方案。")
    result_lines.append("方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。")
    if len(result_lines) < 3:
        result_lines.insert(1, "在真实系统落地时兼顾实现复杂度与工程可维护性。")

    return summary, method_lines[:3], result_lines[:3]


def paper_md(conf: Conference, track: str, p: Paper) -> str:
    tags = [f"{conf.key}{conf.year}", track]
    tag_lines = "\n".join([f'  - "{t}"' for t in tags])
    doi_line = f"**论文链接**：[{p.doi}]({p.doi})" if p.doi else "**论文链接**："
    summary, method_lines, result_lines = generate_auto_sections(conf, track, p)
    method_block = "\n".join([f"- {line}" for line in method_lines])
    result_block = "\n".join([f"- {line}" for line in result_lines])
    return f"""---
title: "{p.title}"
description: "{conf.key} {conf.year} · {track}"
tags:
{tag_lines}
---

# {p.title}

<div class=\"paper-seo-summary\">
<p class=\"paper-seo-summary__desc\">该论文收录于 {conf.key} {conf.year}，所属 Track: {track}。</p>
<p class=\"paper-seo-summary__tags\">{conf.key} {conf.year} · {track}</p>
</div>

{doi_line}
**作者**：{p.authors}
**会议**：{conf.key} {conf.year}

---

## 一句话总结

> {summary}

## 方法简述

{method_block}

## 主要结果

{result_block}
"""


def track_index_md(conf: Conference, track: str, items: List[Tuple[str, str, str]]) -> str:
    rows = []
    for title, rel, doi in items:
        doi_cell = f"[DOI]({doi})" if doi else "-"
        rows.append(f"| [{title}]({rel}) | {doi_cell} |")
    table = "\n".join(rows)
    return f"""# {track} · {conf.key} {conf.year}

本分类收录 {conf.key} {conf.year} Track \"{track}\" 的论文。

| 论文 | 链接 |
|------|------|
{table}
"""


def conf_index_md(conf: Conference, tracks: Dict[str, List[Paper]], slug_map: Dict[str, str]) -> str:
    rows = []
    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        slug = slug_map[track]
        rows.append(f"| [{track}]({slug}/index.md) | {len(papers)} |")
    table_rows = "\n".join(rows)

    return f"""---
title: "{conf.title_zh}"
description: "{conf.key} {conf.year} 论文解读，{conf.location}"
search:
  exclude: false
hide:
  - toc
---

# {conf.key} {conf.year}

**{conf.key} {conf.year}** · {conf.date_range} · {conf.location}

---

| 分类 (Track) | 论文数 |
|-------------|-------|
{table_rows}
"""


def build_conf_docs(conf: Conference, tracks: Dict[str, List[Paper]]) -> Tuple[int, Dict[str, int], Dict[str, str]]:
    base = DOCS / conf.key / conf.year
    # clean previous generated content (keep top index for overwrite later)
    for child in base.iterdir():
        if child.is_dir():
            for root, dirs, files in os.walk(child, topdown=False):
                for fn in files:
                    Path(root, fn).unlink()
                for dn in dirs:
                    Path(root, dn).rmdir()
            child.rmdir()

    slug_map: Dict[str, str] = {}
    seen_track_slug: Dict[str, int] = {}

    for track in tracks:
        s = slugify(track)
        if s in seen_track_slug:
            seen_track_slug[s] += 1
            s = f"{s}_{seen_track_slug[s]}"
        else:
            seen_track_slug[s] = 1
        slug_map[track] = s

    per_track_count: Dict[str, int] = {}
    total = 0

    for track, papers in tracks.items():
        track_slug = slug_map[track]
        track_dir = base / track_slug
        track_dir.mkdir(parents=True, exist_ok=True)

        used: Dict[str, int] = {}
        index_items: List[Tuple[str, str, str]] = []

        for p in papers:
            ps = slugify(p.title)
            if ps in used:
                used[ps] += 1
                ps = f"{ps}_{used[ps]}"
            else:
                used[ps] = 1
            rel = f"{ps}.md"
            write_file(track_dir / rel, paper_md(conf, track, p))
            index_items.append((p.title, rel, p.doi))

        write_file(track_dir / "index.md", track_index_md(conf, track, index_items))
        per_track_count[f"{conf.key}/{conf.year}/{track_slug}"] = len(papers)
        total += len(papers)

    write_file(base / "index.md", conf_index_md(conf, tracks, slug_map))
    return total, per_track_count, slug_map


def nav_block(conf: Conference, tracks: Dict[str, List[Paper]], slug_map: Dict[str, str], icon: str) -> List[str]:
    lines = [f"  - {icon} {conf.key}:\n", f"    - {conf.key} {conf.year}:\n", f"      - {conf.key} {conf.year}: {conf.key}/{conf.year}/index.md\n"]

    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        tslug = slug_map[track]
        lines.append(f"      - {yaml_quote(track)}:\n")
        lines.append(f"        - {yaml_quote(track)}: {conf.key}/{conf.year}/{tslug}/index.md\n")

        used: Dict[str, int] = {}
        for p in papers:
            ps = slugify(p.title)
            if ps in used:
                used[ps] += 1
                ps = f"{ps}_{used[ps]}"
            else:
                used[ps] = 1
            lines.append(f"        - {yaml_quote(p.title)}: {conf.key}/{conf.year}/{tslug}/{ps}.md\n")

    return lines


def replace_nav_section(content: str, section_name: str, new_block: List[str]) -> str:
    lines = content.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if line.startswith(f"  - {section_name}"):
            start = i
            break
    if start is None:
        return content

    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("  - "):
            end = j
            break

    return "".join(lines[:start] + new_block + lines[end:])


def update_homepage_index(micro_total: int, asplos_total: int, micro_tracks: List[Tuple[str, str, int]], asplos_tracks: List[Tuple[str, str, int]]) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")

    text = re.sub(
        r'<div class="conf-count">更新中 · (Austin, Texas|Seoul, Korea)</div>',
        f'<div class="conf-count" data-conf-key="MICRO 2025" data-conf-location="Seoul, Korea">{micro_total} 篇 · {len(micro_tracks)} 个方向 · Seoul, Korea</div>',
        text,
    )

    text = re.sub(
        r'<div class="conf-count">更新中 · Rotterdam, Netherlands</div>',
        f'<div class="conf-count" data-conf-key="ASPLOS 2025" data-conf-location="Rotterdam, Netherlands">{asplos_total} 篇 · {len(asplos_tracks)} 个方向 · Rotterdam, Netherlands</div>',
        text,
    )

    micro_tags = "\n".join(
        [f'<a class="area-tag" href="MICRO/2025/{slug}/" data-track-key="MICRO/2025/{slug}" data-track-label="{label}">{label} {count}</a>' for label, slug, count in micro_tracks[:3]]
    )
    asplos_tags = "\n".join(
        [f'<a class="area-tag" href="ASPLOS/2025/{slug}/" data-track-key="ASPLOS/2025/{slug}" data-track-label="{label}">{label} {count}</a>' for label, slug, count in asplos_tracks[:3]]
    )

    text = re.sub(
        r'### 🔬 \[MICRO 2025\]\(MICRO/2025/index.md\)\n\n<div class="conf-count"[\s\S]*?<div class="area-tags">[\s\S]*?</div>\n</div>',
        "### 🔬 [MICRO 2025](MICRO/2025/index.md)\n\n"
        + f'<div class="conf-count" data-conf-key="MICRO 2025" data-conf-location="Seoul, Korea">{micro_total} 篇 · {len(micro_tracks)} 个方向 · Seoul, Korea</div>\n\n'
        + '<div class="area-groups">\n<div class="area-group">\n<div class="area-group-label">方向</div>\n<div class="area-tags">\n'
        + micro_tags
        + '\n</div>\n</div>\n</div>',
        text,
        count=1,
    )

    text = re.sub(
        r'### 🔄 \[ASPLOS 2025\]\(ASPLOS/2025/index.md\)\n\n<div class="conf-count"[\s\S]*?<div class="area-tags">[\s\S]*?</div>\n</div>',
        "### 🔄 [ASPLOS 2025](ASPLOS/2025/index.md)\n\n"
        + f'<div class="conf-count" data-conf-key="ASPLOS 2025" data-conf-location="Rotterdam, Netherlands">{asplos_total} 篇 · {len(asplos_tracks)} 个方向 · Rotterdam, Netherlands</div>\n\n'
        + '<div class="area-groups">\n<div class="area-group">\n<div class="area-group-label">方向</div>\n<div class="area-tags">\n'
        + asplos_tags
        + '\n</div>\n</div>\n</div>',
        text,
        count=1,
    )

    INDEX_MD.write_text(text, encoding="utf-8")


def main() -> None:
    parsed: Dict[str, Dict[str, List[Paper]]] = {}
    totals: Dict[str, int] = {}
    slug_maps: Dict[str, Dict[str, str]] = {}

    for conf in CONFS:
        tracks = parse_program(conf)
        parsed[conf.key] = tracks
        total, _, slug_map = build_conf_docs(conf, tracks)
        totals[conf.key] = total
        slug_maps[conf.key] = slug_map
        print(f"{conf.key} {conf.year}: {len(tracks)} tracks, {total} papers")

    mk = MKDOCS.read_text(encoding="utf-8")
    micro_block = nav_block(CONFS[0], parsed["MICRO"], slug_maps["MICRO"], "🔬")
    asplos_block = nav_block(CONFS[1], parsed["ASPLOS"], slug_maps["ASPLOS"], "🔄")
    mk = replace_nav_section(mk, "🔬 MICRO", micro_block)
    mk = replace_nav_section(mk, "🔄 ASPLOS", asplos_block)
    MKDOCS.write_text(mk, encoding="utf-8")

    micro_tracks = [
        (track, slug_maps["MICRO"][track], len(papers))
        for track, papers in sorted(parsed["MICRO"].items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ]
    asplos_tracks = [
        (track, slug_maps["ASPLOS"][track], len(papers))
        for track, papers in sorted(parsed["ASPLOS"].items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ]
    update_homepage_index(totals["MICRO"], totals["ASPLOS"], micro_tracks, asplos_tracks)

    print("Updated docs, mkdocs.yml, and docs/index.md")


if __name__ == "__main__":
    main()
