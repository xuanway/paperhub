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


def compute_content_hash(total_papers, keywords):
    payload = json.dumps(
        {"total_papers": total_papers, "keywords": keywords},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

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
    return ZH_TO_EN.get(tag, ZH_TO_EN.get(compact, tag))


def generate():
    # tag → { count, by_conf: {conf: count}, papers: {url: paper-meta} }
    tag_data = defaultdict(
        lambda: {"count": 0, "by_conf": defaultdict(int), "papers": {}}
    )
    total_papers = 0

    for root, dirs, files in os.walk(DOCS_DIR):
        # Skip non-content dirs
        dirs[:] = [d for d in dirs if d not in ("assets", "stylesheets", ".git", "site")]
        for fname in files:
            if fname == "index.md" or not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            relpath = os.path.relpath(fpath, DOCS_DIR)
            conf = conf_from_path(relpath)

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

            total_papers += 1
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
        return previous

    data = {
        "updated":      datetime.now().strftime("%Y-%m-%d"),
        "content_hash": content_hash,
        "total_papers": total_papers,
        "keywords":     keywords,
    }

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ word_data.json updated: {len(keywords)} keywords from {total_papers} papers")
    return data


if __name__ == "__main__":
    generate()
