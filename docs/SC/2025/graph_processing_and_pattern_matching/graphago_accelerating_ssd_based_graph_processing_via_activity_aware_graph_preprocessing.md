---
title: "Graphago: Accelerating SSD-Based Graph Processing via Activity-Aware Graph Preprocessing"
description: "SC 2025 · Graph Processing and Pattern Matching · Xianghao Xu; Yucheng Zhang; Gongxuan Zhang; Yongli Cheng; Fang Wang"
tags:
  - "SC2025"
  - "Graph Processing and Pattern Matching"
---

# Graphago: Accelerating SSD-Based Graph Processing via Activity-Aware Graph Preprocessing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Processing and Pattern Matching。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Processing and Pattern Matching</p>
</div>

**作者**：Xianghao Xu; Yucheng Zhang; Gongxuan Zhang; Yongli Cheng; Fang Wang

**会议**：SC 2025 · St. Louis, MO

## 摘要

SSD-based graph processing systems have emerged as a cost-effective solution for handling large-scale graphs. However, the large access granularity (e.g., 4KB) of an SSD often leads to low I/O efficiency. In this paper, we propose Graphago, an activity-aware graph preprocessing technique for SSD-based graph processing systems. The main idea of Graphago is the combined use of three key designs that synergistically optimize the graph storage and organization based on the active extent of graph data, thereby achieving both high I/O efficiency and satisfactory processing performance: 1) a dual-centrality activity prediction model to efficiently predict the active extent of each vertex, 2) an activity-neighborhood graph ordering technique to minimize read amplification without sacrificing graph traversal efficiency, and 3) an active-data-balanced graph partitioning scheme to address the I/O imbalance problem. Our evaluation results show that Graphago outperforms state-of-the-art SSD-based g

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
