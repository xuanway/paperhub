---
title: "Plexus: Taming Billion-Edge Graphs with 3D Parallel Full-Graph GNN Training"
description: "SC 2025 · Graph Neural Networks and Training · Aditya K. Ranjan; Siddharth Singh; Cunyang Wei; Abhinav Bhatele"
tags:
  - "SC2025"
  - "Graph Neural Networks and Training"
---

# Plexus: Taming Billion-Edge Graphs with 3D Parallel Full-Graph GNN Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Neural Networks and Training。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Neural Networks and Training</p>
</div>

**作者**：Aditya K. Ranjan; Siddharth Singh; Cunyang Wei; Abhinav Bhatele

**会议**：SC 2025 · St. Louis, MO

## 摘要

Graph neural networks leverage the connectivity and structure of real-world graphs to learn intricate properties and relationships between nodes. Many real-world graphs exceed the memory capacity of a GPU due to their sheer size, and distributed full-graph training suffers from high communication overheads and load imbalance due to the irregular structure of graphs. We propose a three-dimensional parallel approach for full-graph training that tackles these issues and scales to billion-edge graphs. In addition, we introduce optimizations such as a double permutation scheme for load balancing, and a performance model to predict the optimal 3D configuration of our parallel implementation: Plexus. We evaluate Plexus on six different graph datasets and show scaling results on up to 2,048 GPUs of Perlmutter, and 1,024 GPUs of Frontier. Plexus achieves unprecedented speedups of 2.3-12.5X over prior state of the art, and a reduction in time-to-solution by 5.2-8.7X on Perlmutter and 7.0-54.2X o

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
