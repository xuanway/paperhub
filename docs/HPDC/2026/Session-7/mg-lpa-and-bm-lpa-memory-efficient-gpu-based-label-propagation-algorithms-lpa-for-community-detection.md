---
title: "νMG-LPA and νBM-LPA: Memory Efficient GPU-based Label Propagation Algorithms (LPA) for Community Detection"
description: "HPDC 2026 · Session 7 — Graph Processing & Community Detection"
tags:
  - "HPDC2026"
  - "Session 7"
  - "Graph Processing & Community Detection"
---

# νMG-LPA and νBM-LPA: Memory Efficient GPU-based Label Propagation Algorithms (LPA) for Community Detection

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 7 — Graph Processing & Community Detection（2026年7月15日 13:30–14:30 · Session Chair：Dilma Da Silva）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 7</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807602)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#Sahu26a](https://dblp.org/db/conf/hpdc/hpdc2026.html#Sahu26a)

**作者**：Subhajit Sahu

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 7 — Graph Processing & Community Detection（2026年7月15日 13:30–14:30 · Session Chair：Dilma Da Silva）

---

## 英文摘要

Community detection involves grouping nodes in a graph with dense connections within groups, than between them. Recently, efficient multicore (GVE-LPA) and GPU-based (ν-LPA) implementations of Label Propagation Algorithm (LPA) for community detection have been proposed. However, these methods incur high memory overhead due to their per-thread/per-vertex hashtables. This makes it challenging to process large graphs on shared memory systems. In this paper, we introduce memory-efficient GPU-based LPA, using weighted Boyer-Moore (BM) and Misra-Gries (MG) sketches. Our νMG8-LPA, using an 8-slot MG sketch, reduces memory usage by 98× and 44× compared to GVE-LPA and ν-LPA, respectively. It is also 2.4× faster than GVE-LPA and only 1.1× slower than ν-LPA, with minimal quality loss (below 5% on average).

## 中文摘要

社区发现是将图中节点分组，使组内连接比组间更稠密。近期已提出用于社区发现的标签传播算法（LPA）的高效多核（GVE-LPA）与基于 GPU（ν-LPA）实现。然而，这些方法由于每线程/每顶点的哈希表而带来高内存开销，使得在共享内存系统上处理大图颇具挑战。本文提出内存高效的基于 GPU 的 LPA，使用加权 Boyer-Moore（BM）与 Misra-Gries（MG）概要。我们的 νMG8-LPA 采用 8 槽 MG 概要，相比 GVE-LPA 和 ν-LPA 分别将内存占用降低 98 倍和 44 倍。它也比 GVE-LPA 快 2.4 倍，仅比 ν-LPA 慢 1.1 倍，且质量损失极小（平均低于 5%）。

## 英文关键词

Community detection, LPA, Memory efficient, GPU-based

## 中文关键词

社区发现，LPA，内存高效，基于 GPU

---

[← 返回 Session 7 — Graph Processing & Community Detection](index.md)
