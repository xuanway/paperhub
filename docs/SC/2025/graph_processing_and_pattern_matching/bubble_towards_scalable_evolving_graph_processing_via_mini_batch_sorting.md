---
title: "Bubble: Towards Scalable Evolving Graph Processing via Mini-Batch Sorting"
description: "SC 2025 · Graph Processing and Pattern Matching · Long Deng; Yongkun Li; Zaigui Zhang; Yinlong Xu; John C. S. Lui"
tags:
  - "SC2025"
  - "Graph Processing and Pattern Matching"
---

# Bubble: Towards Scalable Evolving Graph Processing via Mini-Batch Sorting

**中文标题：** 通过小批量排序实现可扩展的演化图处理

**所属 Session：** [Graph Processing and Pattern Matching](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Processing and Pattern Matching。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Processing and Pattern Matching</p>
</div>

**作者**：Long Deng; Yongkun Li; Zaigui Zhang; Yinlong Xu; John C. S. Lui

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap947&sess=sess180)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Evolving graph processing has become a critical component in various applications and is gaining increasing attention. However, existing evolving graph systems suffer from cache contention and workload imbalance between threads, which leads to poor scalability and performance degradation on modern multi-core computers. In this paper, we introduce Bubble, a high-performance evolving graph processing engine designed with high scalability. By employing a novel graph format based on mini-batch sorting, Bubble utilizes the private caches of modern processor cores, achieving near-linear scalability in graph ingestion, while maintaining high performance for graph analytics. Compared with state-of-the-art systems, including LSGraph, GraphOne, and XPGraph, Bubble achieves 2.46×-8.86× higher throughput in graph ingestion and 0.77×-3.29× speedups when running common graph algorithms.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
