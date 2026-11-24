---
title: "Moment: Co-Optimizing Physical Communication Topology and Data Placement for Multi-GPU Out-of-Core GNN Training"
description: "SC 2025 · Graph Neural Networks and Training · Zuocheng Shi; Jie Sun; Ziyu Song; Mo Sun; Yang Xiao; Fei Wu; Zeke Wang"
tags:
  - "SC2025"
  - "Graph Neural Networks and Training"
---

# Moment: Co-Optimizing Physical Communication Topology and Data Placement for Multi-GPU Out-of-Core GNN Training

**中文标题：** 协同优化物理通信拓扑与数据放置以支持多 GPU 外存图神经网络训练

**所属 Session：** [Graph Neural Networks and Training](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Neural Networks and Training。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Neural Networks and Training</p>
</div>

**作者**：Zuocheng Shi; Jie Sun; Ziyu Song; Mo Sun; Yang Xiao; Fei Wu; Zeke Wang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap212&sess=sess282)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Graph neural networks (GNNs) are widely employed in applications like recommendation systems, social network analysis, and fraud detection, but training large-scale GNNs is challenging due to memory limitations. Existing systems face a trade-off between throughput and monetary cost: distributed systems require expensive memory scaling, while single-machine out-of-core systems are limited by GPU/PCIe throughput. To this end, we propose Moment, a physical communication topology and data placement co-optimizer to enable high-throughput and low-cost GNN training in a single multi-GPU machine. Moment addresses communication contention and GPU load imbalance by modeling the physical topology as capacity-constrained directed graphs and formulating communication scheduling as a max-flow problem. It also introduces a data distribution-aware knapsack algorithm for optimized data placement. Experimental results show that Moment outperforms out-of-core systems by up to 6.51× and distributed system

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
