---
title: "Plexus: Taming Billion-Edge Graphs with 3D Parallel Full-Graph GNN Training"
description: "SC 2025 · Graph Neural Networks and Training · Aditya K. Ranjan; Siddharth Singh; Cunyang Wei; Abhinav Bhatele"
tags:
  - "SC2025"
  - "Graph Neural Networks and Training"
---

# Plexus: Taming Billion-Edge Graphs with 3D Parallel Full-Graph GNN Training

**中文标题：** 通过三维并行全图 GNN 训练驾驭十亿边图

**所属 Session：** [Graph Neural Networks and Training](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Neural Networks and Training。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Neural Networks and Training</p>
</div>

**作者**：Aditya K. Ranjan; Siddharth Singh; Cunyang Wei; Abhinav Bhatele

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap882&sess=sess282)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Graph neural networks leverage the connectivity and structure of real-world graphs to learn intricate properties and relationships between nodes. Many real-world graphs exceed the memory capacity of a GPU due to their sheer size, and distributed full-graph training suffers from high communication overheads and load imbalance due to the irregular structure of graphs. We propose a three-dimensional parallel approach for full-graph training that tackles these issues and scales to billion-edge graphs. In addition, we introduce optimizations such as a double permutation scheme for load balancing, and a performance model to predict the optimal 3D configuration of our parallel implementation: Plexus. We evaluate Plexus on six different graph datasets and show scaling results on up to 2,048 GPUs of Perlmutter, and 1,024 GPUs of Frontier. Plexus achieves unprecedented speedups of 2.3-12.5X over prior state of the art, and a reduction in time-to-solution by 5.2-8.7X on Perlmutter and 7.0-54.2X o

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
