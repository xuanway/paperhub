---
title: "PGT-I: Scaling Spatiotemporal GNNs with Memory-Efficient Distributed Training"
description: "SC 2025 · Graph Neural Networks and Training · Seth Ockerman; Amal Gueroudji; Tanwi Mallick; Yixuan He; Line Pouchard; Robert R"
tags:
  - "SC2025"
  - "Graph Neural Networks and Training"
---

# PGT-I: Scaling Spatiotemporal GNNs with Memory-Efficient Distributed Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Neural Networks and Training。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Neural Networks and Training</p>
</div>

**作者**：Seth Ockerman; Amal Gueroudji; Tanwi Mallick; Yixuan He; Line Pouchard; Robert Ross; Shivaram Venkataraman

**会议**：SC 2025 · St. Louis, MO

## 摘要

Spatiotemporal graph neural networks (ST-GNNs) are powerful tools for modeling spatial and temporal data dependencies. However, their applications have been limited primarily to small-scale datasets because of memory constraints. While distributed training offers a solution, current frameworks lack support for spatiotemporal models and overlook the properties of spatiotemporal data. Informed by a scaling study on a large-scale workload, we present PyTorch Geometric Temporal Index (PGT-I), an extension to PyTorch Geometric Temporal that integrates distributed data parallel training and two novel strategies: index-batching and distributed-index-batching. Our index techniques exploit spatiotemporal structure to construct snapshots dynamically at runtime, significantly reducing memory overhead, while distributed-index-batching extends this approach by enabling scalable processing across multiple GPUs. Our techniques enable the first-ever training of an ST-GNN on the entire PeMS dataset wit

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
