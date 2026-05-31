#!/usr/bin/env python3
"""PaperHub: Generate word cloud keyword data from paper frontmatter tags.

Run:  python3 scripts/gen_wordcloud_data.py
Out:  docs/assets/word_data.json

Called automatically by scripts/hooks.py on every mkdocs build.
"""

import os, re, json, hashlib
from collections import defaultdict
from datetime import datetime

DOCS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs"
)
OUTPUT = os.path.join(DOCS_DIR, "assets", "word_data.json")


REPO_DIR = os.path.dirname(DOCS_DIR)
MKDOCS_YML = os.path.join(REPO_DIR, "mkdocs.yml")

# Canonical track-dir aliases (merge similar dirs into one direction name)
TRACK_CANONICAL = {
    "crypto_fhe": "fhe",
    "llm": "llm_inference",
}


def compute_content_hash(total_papers, keywords):
    payload = json.dumps(
        {"total_papers": total_papers, "keywords": keywords},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def has_chinese(text):
    """Return True if text contains Chinese characters."""
    return any("\u4e00" <= ch <= "\u9fff" for ch in text)

# ── Chinese / mixed → English academic keyword map ────────────────────────
ZH_TO_EN = {
    "LLM推理":       "LLM Inference",
    "硬件安全":       "Hardware Security",
    "同态加密":       "Homomorphic Encryption",
    "DRAM安全":       "DRAM Security",
    "量子计算":       "Quantum Computing",
    "内存安全":       "Memory Security",
    "存内计算":       "Processing-in-Memory",
    "侧信道攻击":     "Side-Channel Attack",
    "侧信道":        "Side-Channel Attack",
    "容错量子计算":   "Fault-Tolerant QC",
    "调度":          "Scheduling",
    "能效":          "Energy Efficiency",
    "量子纠错":      "Quantum Error Correction",
    "光子计算":      "Photonic Computing",
    "激活量化":      "Activation Quantization",
    "近内存计算":    "Near-Memory Computing",
    "数据中心":      "Data Center",
    "推测执行":      "Speculative Execution",
    "量化":          "Quantization",
    "ML加速器":      "ML Accelerator",
    "编译器":        "Compiler",
    "全栈加速":      "Full-Stack Accel.",
    "处理器架构":    "Processor Architecture",
    "长上下文":      "Long Context",
    "异步执行":      "Async Execution",
    "隐私计算":      "Private Computing",
    "可编程防御":    "Programmable Defense",
    "推理型LLM":     "Reasoning LLM",
    "视觉语言模型":  "Vision-Language Model",
    "量子最优控制":  "Quantum Optimal Control",
    "长文本":        "Long Context",
    "分布式训练":    "Distributed Training",
    "模拟计算":      "Analog Computing",
    "片上网络":      "On-Chip Network",
    "拓扑优化":      "Topology Optimization",
    "可靠性":        "Reliability",
    "子阵列":        "Subarray",
    "编译优化":      "Compiler Optimization",
    "进程隔离":      "Process Isolation",
    "协议硬件协同":  "HW-SW Co-design",
    "电源分析":      "Power Analysis",
    "远程攻击":      "Remote Attack",
    "读扰动":        "Read Disturb",
    "实验分析":      "Empirical Analysis",
    "In-Storage计算":"In-Storage Computing",
    "优先队列":      "Priority Queue",
    "量子化学":      "Quantum Chemistry",
    "量子编译":      "Quantum Compilation",
    "3D并行":        "3D Parallelism",
    "On-device AI":  "On-Device AI",
    "On-deviceAI":   "On-Device AI",
    "GPU调度":       "GPU Scheduling",
    "GPU加速":       "GPU Acceleration",
    "LLM服务":       "LLM Serving",
    "容量优化":      "Capacity Optimization",
    "数据格式":      "Data Format",
    "KVCache":       "KV Cache",
    "KV Cache":      "KV Cache",
    "Tensor Core":   "Tensor Core",
    "TensorCore":    "Tensor Core",
    "FHE加速器":     "FHE Accelerator",
    "Obliv":         "Oblivious Memory",
    "Oblivious Memory": "Oblivious Memory",
    "Fermion-to-Qubit": "Fermion-to-Qubit",
    "Clifford门":    "Clifford Gate",
    "T门优化":       "T-Gate Optimization",
    "QCCD":          "QCCD",
    "QOC":           "Quantum Opt. Control",
}

# ── Tags to skip entirely ──────────────────────────────────────────────────
SKIP_SET = {
    # Conference year identifiers
    "HPCA2025","HPCA2026","ISCA2025","ISCA2026","MICRO2025","ASPLOS2025",
    "DAC2025","NeurIPS2025","ICML2025","ICLR2025","CVPR2025","ACL2025",
    # Institutions
    "UIUC","Tsinghua","GeorgiaTech","ETHZürich","ETH Zürich","CAS",
    "Microsoft","IBMResearch","IBM Research","AntGroup","Ant Group",
    "SamsungSDS","Samsung SDS","SKhynix","SK hynix","SJTU","Stanford",
    "Duke","KAIST","ANL","NTT","UBC","UPenn","Michigan","DGIST",
    "KULeuven","KU Leuven","首尔대학교","首尔大学","YonseiUniversity",
    "Yonsei University","DukeUniversity","Duke University","东京大学",
    "清华大学","北京大学","南京大学","上海交通大学","NCState","NC State",
    # Misc / not useful for word cloud
    "Best Paper","LLM服务","SoC","NVMe","BFV","TFHE",
    "Georgia Tech","GeorgiaTech","C-state","Intel DSA",
    "Speculative Store Bypass",
    # These are too institution-specific:
    "Tsinghua","CAS",
}


def conf_from_path(relpath):
    """Return 'CONF YEAR' string from a relative docs path."""
    parts = relpath.replace("\\", "/").split("/")
    if len(parts) >= 2:
        return f"{parts[0].upper()} {parts[1]}"
    return "Unknown"


def relpath_to_url(relpath):
    return relpath.replace("\\", "/").replace(".md", "/")


def extract_frontmatter_field(frontmatter, field):
    match = re.search(rf'^{field}:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_heading(content):
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else ""


def paper_sort_key(paper):
    year = re.search(r'(\d{4})', paper["conf"])
    year_value = -int(year.group(1)) if year else 0
    return (year_value, paper["conf"], paper["title"])


def normalize(tag):
    """Translate tag to English, return None to skip."""
    tag = re.sub(r"\s+", " ", tag.strip().strip("\"'"))
    compact = tag.replace(" ", "")

    if not tag or tag in SKIP_SET or compact in SKIP_SET:
        return None
    # Pattern skip: pure institution-like all-caps or contains digits (year)
    if re.match(r'^[A-Z]+\d{4}$', tag):
        return None
    translated = ZH_TO_EN.get(tag, ZH_TO_EN.get(compact, None))
    if translated:
        return translated
    # Skip tags that contain Chinese characters but have no English translation
    if has_chinese(tag):
        return None
    return tag


def update_mkdocs_nav(per_track_raw, per_conf_stats):
    """Patch (N) counts in mkdocs.yml nav for both year-level and track-level sections.

    - Year-level  (e.g. "- HPCA 2025:")    → total papers for that conf/year
    - Track-level (e.g. "- 同态加密 (4):") → papers in that track dir
    Adds (N) if absent; updates if the number changed.
    """
    if not os.path.exists(MKDOCS_YML):
        return

    # Build conf_by_path: "HPCA/2025" -> 19
    conf_by_path = {}
    for conf_key, info in per_conf_stats.items():  # "HPCA 2025" -> {"total": N, ...}
        parts = conf_key.split()
        if len(parts) == 2:
            conf_by_path[f"{parts[0]}/{parts[1]}"] = info["total"]

    with open(MKDOCS_YML, encoding="utf-8") as f:
        lines = f.readlines()

    def format_label_with_count(label, count):
        label = label.strip()
        # If the label is quoted, keep the count inside the same quotes.
        q = re.match(r'^(["\'])(.*)\1$', label)
        if q:
            quote = q.group(1)
            inner = q.group(2).strip()
            inner = re.sub(r'\s+\(\d+\+?\)$', '', inner).strip()
            return f"{quote}{inner} ({count}){quote}"
        base = re.sub(r'\s+\(\d+\+?\)$', '', label).strip()
        return f"{base} ({count})"

    new_lines = []
    i = 0
    changed = False
    while i < len(lines):
        line = lines[i]
        # Match ANY section header (ends with bare ":" — no path after it)
        # Works for both "- Label:" and "- Label (N):"
        m = re.match(r'^(\s*)-\s+(.+?)(?:\s+\(\d+\+?\))?\s*:\s*$', line.rstrip('\n'))
        if m:
            prefix_indent = len(m.group(1))   # spaces before "-"
            label_clean  = m.group(2).strip() # label without any existing (N)
            child_indent = prefix_indent + 2  # direct children are 2 spaces deeper

            # Scan for the FIRST direct child that is a page link with index.md.
            # Stop at the first non-blank direct child if it is a sub-section header
            # (ends with bare ":"), to avoid descending into nested sections.
            track_dir = None
            j = i + 1
            while j < len(lines):
                sub = lines[j].rstrip('\n')
                if not sub.strip():
                    j += 1
                    continue
                sub_indent = len(sub) - len(sub.lstrip())
                if sub_indent < child_indent:
                    break  # left the section entirely
                if sub_indent == child_indent:
                    # Page link with index.md?
                    path_m = re.search(r':\s+(\S+/index\.md)\s*$', sub)
                    if path_m:
                        track_dir = os.path.dirname(path_m.group(1)).replace("\\", "/")
                        break
                    # Sub-section header (no path, ends with ":")?  Stop here —
                    # don't go deeper or we'd mismatch parent sections.
                    if re.search(r':\s*$', sub):
                        break
                j += 1

            if track_dir:
                path_parts = track_dir.split("/")
                new_count = None
                if len(path_parts) == 3:
                    # Track-level: HPCA/2025/fhe
                    new_count = per_track_raw.get(track_dir)
                elif len(path_parts) == 2:
                    # Conference-year level: HPCA/2025
                    new_count = conf_by_path.get(track_dir)

                if new_count is not None:
                    spaces   = ' ' * prefix_indent
                    counted_label = format_label_with_count(label_clean, new_count)
                    new_line = f"{spaces}- {counted_label}:\n"
                    if new_line != line:
                        changed = True
                    new_lines.append(new_line)
                    i += 1
                    continue

        new_lines.append(line)
        i += 1

    if changed:
        with open(MKDOCS_YML, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("✅ mkdocs.yml nav counts updated")
    else:
        print("✅ mkdocs.yml nav counts unchanged")


def generate():
    # tag → { count, by_conf: {conf: count}, papers: {url: paper-meta} }
    tag_data = defaultdict(
        lambda: {"count": 0, "by_conf": defaultdict(int), "papers": {}}
    )
    total_papers = 0
    # Per-conference and per-track raw counts (ALL non-index .md files)
    per_conf_raw = defaultdict(int)   # e.g. {"HPCA 2025": 19}
    per_track_raw = defaultdict(int)  # e.g. {"HPCA/2025/fhe": 4}

    for root, dirs, files in os.walk(DOCS_DIR):
        # Skip non-content dirs
        dirs[:] = [d for d in dirs if d not in ("assets", "stylesheets", ".git", "site")]
        for fname in files:
            if fname == "index.md" or not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            relpath = os.path.relpath(fpath, DOCS_DIR)
            parts = relpath.replace("\\", "/").split("/")
            conf = conf_from_path(relpath)

            # Always count every non-index .md as a paper (regardless of tags)
            total_papers += 1
            if len(parts) >= 2:
                conf_key = f"{parts[0].upper()} {parts[1]}"
                per_conf_raw[conf_key] += 1
            if len(parts) >= 3:
                track_key = "/".join(parts[:3])
                per_track_raw[track_key] += 1

            with open(fpath, encoding="utf-8") as f:
                content = f.read()

            fm = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not fm:
                continue
            frontmatter = fm.group(1)
            body = content[fm.end():]

            # Inline array: tags: ["a", "b"]
            inline = re.search(r'tags:\s*\[([^\]]+)\]', frontmatter)
            if inline:
                raw_tags = re.findall(r'["\']([^"\']+)["\']', inline.group(1))
            else:
                # Block list: tags:\n  - "a"\n  - "b"
                block = re.search(r'tags:\s*\n((?:[ \t]*-[^\n]*\n)+)', frontmatter)
                if not block:
                    continue
                raw_tags = re.findall(
                    r'-\s*["\']?([^"\'#\n\[\]]+?)["\']?\s*$',
                    block.group(1), re.MULTILINE
                )

            paper_title = extract_heading(body) or extract_frontmatter_field(frontmatter, "title")
            paper_desc = extract_frontmatter_field(frontmatter, "description")
            paper_url = relpath_to_url(relpath)
            paper_meta = {
                "title": paper_title or os.path.splitext(os.path.basename(relpath))[0],
                "url": paper_url,
                "conf": conf,
                "summary": paper_desc,
            }

            seen_tags = set()
            for raw in raw_tags:
                en = normalize(raw.strip())
                if not en or en in seen_tags:
                    continue
                seen_tags.add(en)
                tag_data[en]["count"] += 1
                tag_data[en]["by_conf"][conf] += 1
                tag_data[en]["papers"][paper_url] = paper_meta

    # Build output list with trend calculation
    keywords = []
    for text, info in tag_data.items():
        count_2025 = sum(v for k, v in info["by_conf"].items() if "2025" in k)
        count_2026 = sum(v for k, v in info["by_conf"].items() if "2026" in k)

        if count_2026 > count_2025:
            trend = 1   # rising
        elif count_2025 > count_2026:
            trend = -1  # declining
        else:
            trend = 0   # stable

        # Conference info string for tooltip
        conf_parts = [
            f"{c} ({n} paper{'s' if n > 1 else ''})"
            for c, n in sorted(info["by_conf"].items())
        ]

        keywords.append({
            "text":        text,
            "count":       info["count"],
            "trend":       trend,
            "conf_info":   " · ".join(conf_parts),
            "search_term": text,
            "papers":      sorted(info["papers"].values(), key=paper_sort_key),
        })

    # Sort by count descending, keep top 50
    keywords.sort(key=lambda x: (-x["count"], x["text"]))
    keywords = keywords[:50]

    # ── Build stats section ──────────────────────────────────────────────
    # conferences_count: top-level conf dirs in docs/ (e.g. HPCA, ISCA, ...)
    conf_dirs = [
        d for d in os.listdir(DOCS_DIR)
        if os.path.isdir(os.path.join(DOCS_DIR, d))
        and d not in ("assets", "stylesheets", ".git", "site")
    ]
    conferences_count = len(conf_dirs)

    # per_conf summary: total papers + track count per "CONF YEAR"
    per_conf_stats = {}
    for conf_key, total in sorted(per_conf_raw.items()):
        # tracks = unique track dirs under this conf/year that have papers
        prefix = conf_key.replace(" ", "/", 1).replace(" ", "/") + "/"
        tracks_with_papers = {
            k.split("/")[2]
            for k in per_track_raw
            if k.startswith(conf_key.replace(" ", "/", 1) + "/")
        }
        per_conf_stats[conf_key] = {
            "total": total,
            "tracks": len(tracks_with_papers),
        }

    # directions_count: unique canonical track names with papers
    canonical_tracks = {
        TRACK_CANONICAL.get(k.split("/")[2], k.split("/")[2])
        for k in per_track_raw
        if per_track_raw[k] > 0 and len(k.split("/")) >= 3
    }
    directions_count = len(canonical_tracks)

    stats = {
        "total_papers":       total_papers,
        "conferences_count":  conferences_count,
        "directions_count":   directions_count,
        "per_conf":           per_conf_stats,
        "per_track":          dict(per_track_raw),
    }

    content_hash = compute_content_hash(total_papers, keywords)
    previous = None
    if os.path.exists(OUTPUT):
        try:
            with open(OUTPUT, encoding="utf-8") as f:
                previous = json.load(f)
        except Exception:
            previous = None

    if previous and previous.get("content_hash") == content_hash:
        print(
            f"✅ word_data.json unchanged: {len(keywords)} keywords from {total_papers} papers"
        )
        update_mkdocs_nav(per_track_raw, per_conf_stats)
        return previous

    data = {
        "updated":      datetime.now().strftime("%Y-%m-%d"),
        "content_hash": content_hash,
        "total_papers": total_papers,
        "stats":        stats,
        "keywords":     keywords,
    }

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ word_data.json updated: {len(keywords)} keywords from {total_papers} papers")
    update_mkdocs_nav(per_track_raw, per_conf_stats)
    return data


if __name__ == "__main__":
    generate()
