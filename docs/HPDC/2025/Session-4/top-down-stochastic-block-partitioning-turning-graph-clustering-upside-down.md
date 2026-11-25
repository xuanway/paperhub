---
title: "Top-Down Stochastic Block Partitioning: Turning Graph Clustering Upside Down"
description: "HPDC 2025 · Session 4 — Efficiency and Sustainability"
tags:
  - "HPDC2025"
  - "Session 4"
  - "Efficiency and Sustainability"
---

# Top-Down Stochastic Block Partitioning: Turning Graph Clustering Upside Down

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 4 — Efficiency and Sustainability（2025年7月22日 10:30–12:15 · Session Chair：Jarek Nabrzyski）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 4</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731589) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/wayne.pdf)

**作者**：Frank Wanye, Vitaliy Gleyzer, Edward Kao, Wu-chun Feng

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 4 — Efficiency and Sustainability（2025年7月22日 10:30–12:15 · Session Chair：Jarek Nabrzyski）

---

## 英文摘要

Stochastic block partitioning (SBP) is a statistical inference-based algorithm for clustering vertices within a graph. It has been shown to be statistically robust and highly accurate even on graphs with a complex structure, but its poor scalability limits its usability to smaller-sized graphs. In this manuscript we argue that one reason for its poor scalability is the agglomerative, or bottom-up, nature of SBP’s algorithmic design; the agglomerative computations cause high memory usage and create a large search space that slows down statistical inference, particularly in the algorithm’s initial iterations. To address this bottleneck, we propose Top-Down SBP, a novel algorithm that replaces the agglomerative (bottom-up) block merges in SBP with a block-splitting operation. This enables the algorithm to start with all vertices in one cluster and subdivide them over time into smaller clusters. We show that Top-Down SBP is up to 7.7× faster than Bottom-Up SBP without sacrificing accuracy and can process larger graphs than Bottom-Up SBP on the same hardware due to an up to 4.1× decrease in memory usage. Additionally, we adapt existing methods for accelerating Bottom-Up SBP to the Top-Down approach, leading to up to 13.2× speedup over accelerated Bottom-Up SBP and up to 403× speedup over sequential Bottom-Up SBP on 64 compute nodes. Thus, Top-Down SBP represents substantial improvements to the scalability of SBP, enabling the analysis of larger datasets on the same hardware.

## 中文摘要

随机块划分（SBP）是一种基于统计推断的图顶点聚类算法。它已被证明在结构复杂的图上依然具有统计稳健性与高精度，但可扩展性差，限制了其仅适用于较小规模的图。本文认为，其可扩展性差的一个原因是 SBP 算法设计的凝聚式（自底向上）特性；凝聚式计算导致高内存占用，并产生巨大的搜索空间，拖慢统计推断，尤其是在算法的初始迭代中。为突破这一瓶颈，我们提出 Top-Down SBP，一种新算法，用块分裂操作取代 SBP 中的凝聚式（自底向上）块合并。这使算法可以从所有顶点同属一个簇开始，随时间将其细分为更小的簇。我们表明，Top-Down SBP 相比 Bottom-Up SBP 最高快 7.7 倍且不牺牲精度，并因内存占用最多降低 4.1 倍而能在相同硬件上处理更大的图。此外，我们将加速 Bottom-Up SBP 的现有方法适配到自顶向下方法，在 64 个计算节点上相比加速版 Bottom-Up SBP 最高取得 13.2 倍加速，相比串行 Bottom-Up SBP 最高取得 403 倍加速。因此，Top-Down SBP 显著提升了 SBP 的可扩展性，使在相同硬件上分析更大数据集成为可能。

## 英文关键词

community detection, graph clustering, stochastic blockmodels, Bayesian inference, asynchronous Gibbs

## 中文关键词

社区发现，图聚类，随机块模型，贝叶斯推断，异步 Gibbs

---

[← 返回 Session 4 — Efficiency and Sustainability](index.md)
