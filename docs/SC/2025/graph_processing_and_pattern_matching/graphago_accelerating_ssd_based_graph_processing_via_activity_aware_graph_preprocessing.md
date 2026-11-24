---
title: "Graphago: Accelerating SSD-Based Graph Processing via Activity-Aware Graph Preprocessing"
description: "SC 2025 · Graph Processing and Pattern Matching · Xianghao Xu; Yucheng Zhang; Gongxuan Zhang; Yongli Cheng; Fang Wang"
tags:
  - "SC2025"
  - "Graph Processing and Pattern Matching"
---

# Graphago: Accelerating SSD-Based Graph Processing via Activity-Aware Graph Preprocessing

**中文标题：** 通过活动感知图预处理加速基于 SSD 的图处理

**所属 Session：** [Graph Processing and Pattern Matching](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Processing and Pattern Matching。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Processing and Pattern Matching</p>
</div>

**作者**：Xianghao Xu; Yucheng Zhang; Gongxuan Zhang; Yongli Cheng; Fang Wang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap592&sess=sess180)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

SSD-based graph processing systems have emerged as a cost-effective solution for handling large-scale graphs. However, the large access granularity (e.g., 4KB) of an SSD often leads to low I/O efficiency. In this paper, we propose Graphago, an activity-aware graph preprocessing technique for SSD-based graph processing systems. The main idea of Graphago is the combined use of three key designs that synergistically optimize the graph storage and organization based on the active extent of graph data, thereby achieving both high I/O efficiency and satisfactory processing performance: 1) a dual-centrality activity prediction model to efficiently predict the active extent of each vertex, 2) an activity-neighborhood graph ordering technique to minimize read amplification without sacrificing graph traversal efficiency, and 3) an active-data-balanced graph partitioning scheme to address the I/O imbalance problem. Our evaluation results show that Graphago outperforms state-of-the-art SSD-based g

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
