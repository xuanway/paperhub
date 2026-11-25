---
title: "PANNS: Enhancing Graph-based Approximate Nearest Neighbor Search through Recency-aware Construction and Parameterized Search"
description: "PPoPP 2025 Session 9（Concurrent Data Structures and Synchronization II）：时序感知建图 + 参数化 beam search，吞吐最高 3.7×"
tags:
  - "PPoPP2025"
  - "Session-9"
  - "Concurrent Data Structures and Synchronization II"
  - "ANNS"
  - "Vector Database"
  - "Beam Search"
authors:
  - "Xizhe Yin"
  - "Chao Gao"
  - "Zhijia Zhao"
  - "Rajiv Gupta"
session: "Session 9: Concurrent Data Structures and Synchronization II"
session_number: 9
session_chair: "Pengfei Su"
date: "2025-03-04"
time: "15:40–16:00"
room: "Acacia D"
doi: "10.1145/3710848.3710867"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# PANNS: Enhancing Graph-based Approximate Nearest Neighbor Search through Recency-aware Construction and Parameterized Search

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 PANNS，在近邻图构建中嵌入查询与结果之间的时间相关性，并引入完全参数化的 beam search，在保持召回率的同时提升图 ANNS 的查询吞吐。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 9: Concurrent Data Structures and Synchronization II</p>
</div>

**作者**：Xizhe Yin, Chao Gao, Zhijia Zhao, Rajiv Gupta (University of California Riverside)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 15:40–16:00 · Session 9: Concurrent Data Structures and Synchronization II（主席：Pengfei Su）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710867) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 PANNS，在近邻图构建中嵌入查询与结果之间的时间相关性，并引入完全参数化的 beam search，在保持召回率的同时提升图 ANNS 的查询吞吐。

## 研究问题

图 ANNS 的设计空间仍有两点未被充分探索：构建阶段常忽略输入查询与结果之间的时间相关性；搜索阶段对 beam search 的参数化缺乏系统探索。

## 方法简述

- 在 proximity graph 构建中嵌入时序信息，捕获 query-result 之间的相关性。
- 提出全参数化 beam search 算法，支持对搜索过程做系统性性能优化。

## 主要结果

- 相比 SOTA 图 ANNS 方法，查询吞吐最高提升 3.7×，且召回率相当。
- 在不降低查询质量的前提下，将图规模最多缩小 30%。

<details>
<summary>原文摘要（英文）</summary>

Approximate Nearest-Neighbor Search (ANNS) has become the standard querying method in vector databases, especially with the recent surge in large-scale, high-dimensional data driven by LLM-based applications. Recently, graph-based ANNS has shown improved throughput by constructing a graph from the dataset, with edges representing the distances between data points, and using best-first or beam search algorithms for query evaluation. This work highlights that key aspects of the design space for both graph construction and search in graph-based ANNS remain under-explored. Specifically, the construction phase often neglects the potential temporal correlation between input queries and their results, while the search phase lacks a thorough exploration of beam search parameterization. To address these gaps, we present PANNS, a system that embeds temporal information in the proximity graph construction to capture query-result correlations. Moreover, it introduces a fully parameterized beam search algorithm, enabling extensive performance optimization. PANNS achieves up to a 3.7× improvement in query throughput over state-of-the-art graph-based ANNS methods, while maintaining equivalent recall levels. Furthermore, it reduces graph size by up to 30% without degrading query quality.

</details>

---

> 所属 Session：[Session 9: Concurrent Data Structures and Synchronization II](index.md) · 返回 [PPoPP 2025 总览](../index.md)
