---
title: "Efficient Tracking of Communities on Evolving Graphs with Leiden Algorithm"
description: "HPDC 2026 · Session 7 — Graph Processing & Community Detection"
tags:
  - "HPDC2026"
  - "Session 7"
  - "Graph Processing & Community Detection"
---

# Efficient Tracking of Communities on Evolving Graphs with Leiden Algorithm

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 7 — Graph Processing & Community Detection（2026年7月15日 13:30–14:30 · Session Chair：Dilma Da Silva）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 7</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807601)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#Sahu26](https://dblp.org/db/conf/hpdc/hpdc2026.html#Sahu26)

**作者**：Subhajit Sahu

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 7 — Graph Processing & Community Detection（2026年7月15日 13:30–14:30 · Session Chair：Dilma Da Silva）

---

## 英文摘要

Community detection, or clustering, identifies groups of nodes in a graph that are more densely connected to each other than to the rest of the network. The Leiden algorithm, which improves upon the Louvain algorithm, efficiently detects high-quality communities in large networks. Yet, given the size and dynamic nature of real-world graphs, efficient dynamic community detection algorithms capable of tracking community evolution over time are crucial. However, existing algorithms based on Leiden are inefficient and lack support for tracking evolving communities. This paper introduces parallel Naive-dynamic (ND), Delta-screening (DS), and Dynamic Frontier (DF) Leiden algorithms that efficiently track communities over time.

## 中文摘要

社区发现（或称聚类）识别图中彼此连接比与网络其余部分更紧密的节点分组。Leiden 算法在 Louvain 算法基础上改进，能高效地在大型网络中检测高质量社区。然而，鉴于真实世界图的规模与动态特性，能够随时间跟踪社区演化的高效动态社区发现算法至关重要。但现有基于 Leiden 的算法效率低下，且缺乏对演化社区跟踪的支持。本文提出并行的朴素动态（ND）、增量筛选（DS）和动态前沿（DF）Leiden 算法，能够随时间高效跟踪社区。

## 英文关键词

Community detection, Leiden algorithm, Dynamic graphs, Community tracking, Parallel algorithms

## 中文关键词

社区发现，Leiden 算法，动态图，社区跟踪，并行算法

---

[← 返回 Session 7 — Graph Processing & Community Detection](index.md)
