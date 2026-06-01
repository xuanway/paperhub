---
title: "Bubble: Towards Scalable Evolving Graph Processing via Mini-Batch Sorting"
description: "SC 2025 · Graph Processing and Pattern Matching · Long Deng; Yongkun Li; Zaigui Zhang; Yinlong Xu; John C. S. Lui"
tags:
  - "SC2025"
  - "Graph Processing and Pattern Matching"
---

# Bubble: Towards Scalable Evolving Graph Processing via Mini-Batch Sorting

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Processing and Pattern Matching。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Processing and Pattern Matching</p>
</div>

**作者**：Long Deng; Yongkun Li; Zaigui Zhang; Yinlong Xu; John C. S. Lui

**会议**：SC 2025 · St. Louis, MO

## 摘要

Evolving graph processing has become a critical component in various applications and is gaining increasing attention. However, existing evolving graph systems suffer from cache contention and workload imbalance between threads, which leads to poor scalability and performance degradation on modern multi-core computers. In this paper, we introduce Bubble, a high-performance evolving graph processing engine designed with high scalability. By employing a novel graph format based on mini-batch sorting, Bubble utilizes the private caches of modern processor cores, achieving near-linear scalability in graph ingestion, while maintaining high performance for graph analytics. Compared with state-of-the-art systems, including LSGraph, GraphOne, and XPGraph, Bubble achieves 2.46×-8.86× higher throughput in graph ingestion and 0.77×-3.29× speedups when running common graph algorithms.

---

## 一句话总结

> 该工作属于 Graph Processing and Pattern Matching 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Graph Processing and Pattern Matching 领域贡献新的设计范式或评估框架。
