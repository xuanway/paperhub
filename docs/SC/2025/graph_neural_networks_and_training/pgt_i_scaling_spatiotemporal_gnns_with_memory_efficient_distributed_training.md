---
title: "PGT-I: Scaling Spatiotemporal GNNs with Memory-Efficient Distributed Training"
description: "SC 2025 · Graph Neural Networks and Training · Seth Ockerman; Amal Gueroudji; Tanwi Mallick; Yixuan He; Line Pouchard; Robert R"
tags:
  - "SC2025"
  - "Graph Neural Networks and Training"
---

# PGT-I: Scaling Spatiotemporal GNNs with Memory-Efficient Distributed Training

**中文标题：** 通过内存高效的分布式训练扩展时空图神经网络

**所属 Session：** [Graph Neural Networks and Training](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Neural Networks and Training。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Neural Networks and Training</p>
</div>

**作者**：Seth Ockerman; Amal Gueroudji; Tanwi Mallick; Yixuan He; Line Pouchard; Robert Ross; Shivaram Venkataraman

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap781&sess=sess282)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Spatiotemporal graph neural networks (ST-GNNs) are powerful tools for modeling spatial and temporal data dependencies. However, their applications have been limited primarily to small-scale datasets because of memory constraints. While distributed training offers a solution, current frameworks lack support for spatiotemporal models and overlook the properties of spatiotemporal data. Informed by a scaling study on a large-scale workload, we present PyTorch Geometric Temporal Index (PGT-I), an extension to PyTorch Geometric Temporal that integrates distributed data parallel training and two novel strategies: index-batching and distributed-index-batching. Our index techniques exploit spatiotemporal structure to construct snapshots dynamically at runtime, significantly reducing memory overhead, while distributed-index-batching extends this approach by enabling scalable processing across multiple GPUs. Our techniques enable the first-ever training of an ST-GNN on the entire PeMS dataset wit

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
