---
title: "Moment: Co-Optimizing Physical Communication Topology and Data Placement for Multi-GPU Out-of-Core GNN Training"
description: "SC 2025 · Graph Neural Networks and Training · Zuocheng Shi; Jie Sun; Ziyu Song; Mo Sun; Yang Xiao; Fei Wu; Zeke Wang"
tags:
  - "SC2025"
  - "Graph Neural Networks and Training"
---

# Moment: Co-Optimizing Physical Communication Topology and Data Placement for Multi-GPU Out-of-Core GNN Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Neural Networks and Training。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Neural Networks and Training</p>
</div>

**作者**：Zuocheng Shi; Jie Sun; Ziyu Song; Mo Sun; Yang Xiao; Fei Wu; Zeke Wang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Graph neural networks (GNNs) are widely employed in applications like recommendation systems, social network analysis, and fraud detection, but training large-scale GNNs is challenging due to memory limitations. Existing systems face a trade-off between throughput and monetary cost: distributed systems require expensive memory scaling, while single-machine out-of-core systems are limited by GPU/PCIe throughput. To this end, we propose Moment, a physical communication topology and data placement co-optimizer to enable high-throughput and low-cost GNN training in a single multi-GPU machine. Moment addresses communication contention and GPU load imbalance by modeling the physical topology as capacity-constrained directed graphs and formulating communication scheduling as a max-flow problem. It also introduces a data distribution-aware knapsack algorithm for optimized data placement. Experimental results show that Moment outperforms out-of-core systems by up to 6.51× and distributed system

---

## 一句话总结

> 该工作属于 Graph Neural Networks and Training 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Graph Neural Networks and Training 领域贡献新的设计范式或评估框架。
