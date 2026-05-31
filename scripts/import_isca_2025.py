#!/usr/bin/env python3
"""Import ISCA 2025 accepted papers from the official program page.

What this script updates:
1) docs/ISCA/2025/**
   - Rebuilds track directories, track index pages, and per-paper markdown stubs.
2) mkdocs.yml
   - Rebuilds the ISCA 2025 nav block under "🏗️ ISCA".
3) docs/index.md
   - Updates the ISCA 2025 card count and top-track tags.

Run:
  python3 scripts/import_isca_2025.py
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

ISCA_URL = "https://www.iscaconf.org/isca2025/program/"
ISCA_LOCATION = "Tokyo, Japan"
ISCA_DATE = "2025年6月21日 - 6月25日"


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


# ── Track normalization ───────────────────────────────────────────────────────

def normalize_track(raw: str) -> str:
    """Normalize session track name.

    - Strip trailing Roman numerals  (I, II, III, IV …) added to parallel sessions.
    - Normalise "ML Acceleration" → "ML Accelerators" for consistency across sessions.
    """
    t = " ".join(raw.split()).strip()
    # Strip trailing Roman-numeral suffix, e.g. "Quantum II" → "Quantum"
    t = re.sub(r"\s+[IVX]+\s*$", "", t).strip()
    # Merge the one "ML Acceleration" session with the "ML Accelerators" series
    t = re.sub(r"\bML Acceleration\b", "ML Accelerators", t)
    return t


# ── Paper-entry parser ────────────────────────────────────────────────────────

# Time-slot prefix, e.g.  "10:05 AM – 10:25 AM"
_TIME_RE = re.compile(
    r"\d{1,2}:\d{2}\s+[AP]M\s+[–\-−]\s*\d{1,2}:\d{2}\s+[AP]M",
    re.IGNORECASE,
)

# One person name: "Firstname [Initial] Lastname"  (no hyphens in the match to
# avoid matching hyphenated technical terms like "Battery-Aware")
_FIRSTNAME = r"[A-Z][a-zA-Z']{1,15}"
_LASTNAME  = r"[A-Z][a-zA-Z']{1,20}"
_NAME      = rf"{_FIRSTNAME}(?:\s+[A-Z]\.?)?\s+{_LASTNAME}"

# Three consecutive names separated by commas — reliable author-list anchor
_THREE_NAMES_RE = re.compile(
    rf"({_NAME}),\s*{_NAME},\s*{_NAME}",
)
# Two consecutive names — fallback for 2-author papers
_TWO_NAMES_RE = re.compile(
    rf"({_NAME}),\s*{_NAME}",
)


def _split_title_authors(text: str) -> Tuple[str, str]:
    """Split a 'Title Authors' blob into (title, authors).

    Strategy:
      1. Find the first position that starts a sequence of 3 comma-separated
         person-name pairs — this is the start of the author list.
      2. Fall back to 2 consecutive names if 3 not found.
      3. If no author pattern is found, return (text, "").
    """
    text = " ".join(text.split()).strip()
    if not text:
        return "", ""

    for pattern in (_THREE_NAMES_RE, _TWO_NAMES_RE):
        m = pattern.search(text)
        if m:
            title   = text[: m.start()].strip()
            authors = text[m.start() :].strip()
            if title:
                return title, authors

    # Last resort: return the whole thing as the title
    return text, ""


def _is_name_word(word: str) -> bool:
     """Return True if word could be part of a person's name."""
     return bool(re.match(r"^[A-Z][a-zA-Z.\-']+$", word))


def _is_name_token(tok: str) -> bool:
     """Return True if a comma-separated token looks like a 2-4 word person name."""
     words = tok.strip().split()
     return 2 <= len(words) <= 4 and all(_is_name_word(w) for w in words)


def _parse_session_text(text: str) -> List[Paper]:
    """Extract papers from the raw text block of one session.

    The text looks like:
        Session Chair: NAME  HH:MM AM – HH:MM AM  Paper Title  Author1, Author2…
        HH:MM AM – HH:MM AM  Paper Title  Author1, Author2…
        …
    """
    # Split on time stamps; part[0] is "Session Chair: …" metadata
    parts = _TIME_RE.split(text)
    papers: List[Paper] = []
    seen: set[str] = set()

    for part in parts[1:]:  # skip pre-time chair info
        part = " ".join(part.split()).strip()
        if not part:
            continue
        title, authors = _split_title_authors(part)
        if not title:
            continue
        # Deduplicate (page sometimes repeats sessions for JS accordion display)
        key = slugify(title)[:80]
        if key in seen:
            continue
        seen.add(key)
        papers.append(Paper(title=title, authors=authors))

    return papers


# ── Page parser ───────────────────────────────────────────────────────────────

# Session header pattern: "Session 1A: Track Name −"
_SESSION_HDR_RE = re.compile(
    r"^Session\s+\d+[A-Z]{1,2}\s*:\s*(.+?)(?:\s*[−–—\-]+\s*)?$",
    re.IGNORECASE,
)


def parse_isca_2025() -> Dict[str, List[Paper]]:
    """Fetch and parse the ISCA 2025 program page into {track: [Paper]}.

    Page structure:
      div.panel-session
        div.panel-heading
          h4  "Session 1A: ML Accelerators I"
          h5  "Location: ..."
        div.panel-paper.panel-collapse
          "Session Chair: NAME  HH:MM AM – HH:MM AM  PaperTitle Authors  ..."
    """
    html = curl_fetch(ISCA_URL)
    soup = BeautifulSoup(html, "html.parser")

    tracks: Dict[str, List[Paper]] = {}
    track_paper_keys: Dict[str, set] = {}

    for panel in soup.find_all("div", class_="panel-session"):
        heading = panel.find("div", class_="panel-heading")
        if heading is None:
            continue
        h4 = heading.find("h4")
        if h4 is None:
            continue

        h4_text = " ".join(h4.get_text(" ", strip=True).split())
        m = _SESSION_HDR_RE.match(h4_text)
        if not m:
            continue

        track = normalize_track(m.group(1).strip())

        paper_div = panel.find("div", class_="panel-paper")
        if paper_div is None:
            continue

        session_text = " ".join(paper_div.get_text(" ", strip=True).split())
        papers = _parse_session_text(session_text)

        if track not in track_paper_keys:
            track_paper_keys[track] = set()
        existing = track_paper_keys[track]

        for p in papers:
            key = slugify(p.title)[:80]
            if key not in existing:
                existing.add(key)
                tracks.setdefault(track, []).append(p)

    return tracks
def parse_isca_2025() -> Dict[str, List[Paper]]:
    """Fetch and parse the ISCA 2025 program page into {track: [Paper]}.

    Page structure:
      div.panel-session
        div.panel-heading
          h4  "Session 1A: ML Accelerators I"
          h5  "Location: ..."
        div.panel-paper.panel-collapse
          "Session Chair: NAME  HH:MM AM – HH:MM AM  PaperTitle Authors  ..."
    """
    html = curl_fetch(ISCA_URL)
    soup = BeautifulSoup(html, "html.parser")

    tracks: Dict[str, List[Paper]] = {}
    track_paper_keys: Dict[str, set] = {}

    for panel in soup.find_all("div", class_="panel-session"):
        heading = panel.find("div", class_="panel-heading")
        if heading is None:
            continue
        h4 = heading.find("h4")
        if h4 is None:
            continue

        h4_text = " ".join(h4.get_text(" ", strip=True).split())
        m = _SESSION_HDR_RE.match(h4_text)
        if not m:
            continue

        track = normalize_track(m.group(1).strip())

        paper_div = panel.find("div", class_="panel-paper")
        if paper_div is None:
            continue

        session_text = " ".join(paper_div.get_text(" ", strip=True).split())
        papers = _parse_session_text(session_text)

        if track not in track_paper_keys:
            track_paper_keys[track] = set()
        existing = track_paper_keys[track]

        for p in papers:
            key = slugify(p.title)[:80]
            if key not in existing:
                existing.add(key)
                tracks.setdefault(track, []).append(p)

    return tracks


# ── Doc builder ───────────────────────────────────────────────────────────────

def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def paper_md(track: str, p: Paper) -> str:
    tags = ["ISCA2025", track]
    tag_lines = "\n".join([f'  - "{t}"' for t in tags])
    doi_line = f"**论文链接**：[{p.doi}]({p.doi})" if p.doi else "**论文链接**："
    return f"""---
title: "{p.title.replace('"', "'")}"
description: "ISCA 2025 · {track}"
tags:
{tag_lines}
---

# {p.title}

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ISCA 2025，所属 Track: {track}。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · {track}</p>
</div>

{doi_line}
**作者**：{p.authors}
**会议**：ISCA 2025

---

## 一句话总结

> 该工作属于 {track} 方向，围绕关键系统瓶颈提出优化方案，并在 ISCA 2025 语境下验证其价值。

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
    return f"""# {track} · ISCA 2025

本分类收录 ISCA 2025 Track \"{track}\" 的论文。

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
title: "ISCA 2025 论文集"
description: "ISCA 2025 论文解读，{ISCA_LOCATION}"
search:
  exclude: false
hide:
  - toc
---

# ISCA 2025

**ISCA 2025** · {ISCA_DATE} · {ISCA_LOCATION}

---

| 分类 (Track) | 论文数 |
|-------------|-------|
{table_rows}
"""


def build_docs(tracks: Dict[str, List[Paper]]) -> Tuple[int, Dict[str, str]]:
    base = DOCS / "ISCA" / "2025"
    base.mkdir(parents=True, exist_ok=True)

    # Clean previous generated content
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
    used_slugs: Dict[str, int] = {}

    for track in tracks:
        s = slugify(track)
        if s in used_slugs:
            used_slugs[s] += 1
            s = f"{s}_{used_slugs[s]}"
        else:
            used_slugs[s] = 1
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


# ── mkdocs.yml updater ────────────────────────────────────────────────────────

def isca_2025_nav_block(
    tracks: Dict[str, List[Paper]], slug_map: Dict[str, str], total: int
) -> List[str]:
    lines: List[str] = [
        f"    - ISCA 2025 ({total}):\n",
        "      - ISCA 2025: ISCA/2025/index.md\n",
    ]

    for track, papers in sorted(tracks.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        tslug = slug_map[track]
        lines.append(f"      - {yaml_quote(f'{track} ({len(papers)})')}:\n")
        lines.append(f"        - {yaml_quote(track)}: ISCA/2025/{tslug}/index.md\n")

        used_titles: Dict[str, int] = {}
        for p in papers:
            pslug = slugify(p.title)
            if pslug in used_titles:
                used_titles[pslug] += 1
                pslug = f"{pslug}_{used_titles[pslug]}"
            else:
                used_titles[pslug] = 1
            lines.append(
                f"        - {yaml_quote(p.title)}: ISCA/2025/{tslug}/{pslug}.md\n"
            )

    return lines


def replace_isca_2025_nav(content: str, new_block: List[str]) -> str:
    lines = content.splitlines(keepends=True)

    # Find "  - 🏗️ ISCA:" section
    isca_section = None
    for i, line in enumerate(lines):
        if line.startswith("  - 🏗️ ISCA:"):
            isca_section = i
            break
    if isca_section is None:
        raise RuntimeError("Cannot find ISCA nav section in mkdocs.yml")

    # Find the start of ISCA 2025 block (4-space indent)
    start_2025 = None
    for i in range(isca_section + 1, len(lines)):
        if lines[i].startswith("    - ISCA 2025"):
            start_2025 = i
            break
    if start_2025 is None:
        raise RuntimeError("Cannot find ISCA 2025 nav block in mkdocs.yml")

    # Find end: next top-level (2-space) section
    end_2025 = len(lines)
    for i in range(start_2025 + 1, len(lines)):
        if lines[i].startswith("  - "):
            end_2025 = i
            break

    return "".join(lines[:start_2025] + new_block + lines[end_2025:])


# ── docs/index.md updater ─────────────────────────────────────────────────────

def update_homepage_index(
    total: int, top_tracks: List[Tuple[str, str, int]], num_tracks: int
) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")

    tags = "\n".join(
        [
            f'<a class="area-tag" href="ISCA/2025/{slug}/" '
            f'data-track-key="ISCA/2025/{slug}" '
            f'data-track-label="{label}">{label} {count}</a>'
            for label, slug, count in top_tracks[:3]
        ]
    )

    replacement = (
        "### 🏗️ [ISCA 2025](ISCA/2025/index.md)\n\n"
        + f'<div class="conf-count" data-conf-key="ISCA 2025" '
        + f'data-conf-location="{ISCA_LOCATION}">'
        + f"{total} 篇 · {num_tracks} 个方向 · {ISCA_LOCATION}</div>\n\n"
        + '<div class="area-groups">\n<div class="area-group">\n'
        + '<div class="area-group-label">方向</div>\n<div class="area-tags">\n'
        + tags
        + "\n</div>\n</div>\n</div>"
    )

    # Match the entire ISCA 2025 card block
    pattern = (
        r"### 🏗️ \[ISCA 2025\]\(ISCA/2025/index\.md\)\n\n"
        r"[\s\S]*?"
        r"(?=\n---\n)"
    )
    new_text, n = re.subn(pattern, replacement, text, count=1)
    if n != 1:
        raise RuntimeError("Cannot find ISCA 2025 card block in docs/index.md")

    INDEX_MD.write_text(new_text, encoding="utf-8")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print("Fetching ISCA 2025 program…")
    tracks = parse_isca_2025()
    if not tracks:
        raise RuntimeError("No ISCA 2025 tracks/papers parsed from official program page")

    total, slug_map = build_docs(tracks)

    mkdocs_text = MKDOCS.read_text(encoding="utf-8")
    mkdocs_text = replace_isca_2025_nav(
        mkdocs_text,
        isca_2025_nav_block(tracks, slug_map, total),
    )
    MKDOCS.write_text(mkdocs_text, encoding="utf-8")

    top_tracks = sorted(
        [(track, slug_map[track], len(papers)) for track, papers in tracks.items()],
        key=lambda x: -x[2],
    )
    update_homepage_index(total, top_tracks, len(tracks))

    print(f"ISCA 2025: {len(tracks)} tracks, {total} papers")
    print("Updated docs/ISCA/2025, mkdocs.yml, and docs/index.md")


if __name__ == "__main__":
    main()
