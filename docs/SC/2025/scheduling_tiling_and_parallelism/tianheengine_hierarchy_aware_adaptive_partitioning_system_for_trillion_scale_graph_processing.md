---
title: "TianheEngine: Hierarchy-Aware Adaptive Partitioning System for Trillion-Scale Graph Processing"
description: "SC 2025 · Scheduling, Tiling, and Parallelism · Xinbiao Gan; Tiejun Li; Yiqi Wang; Qiang Zhang; Yongming Yi; Chunye Gong; Jie Li"
tags:
  - "SC2025"
  - "Scheduling, Tiling, and Parallelism"
---

# TianheEngine: Hierarchy-Aware Adaptive Partitioning System for Trillion-Scale Graph Processing

**中文标题：** 面向万亿规模图处理的层次感知自适应划分系统

**所属 Session：** [Scheduling, Tiling, and Parallelism](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Scheduling, Tiling, and Parallelism。</p>
<p class="paper-seo-summary__tags">SC 2025 · Scheduling, Tiling, and Parallelism</p>
</div>

**作者**：Xinbiao Gan; Tiejun Li; Yiqi Wang; Qiang Zhang; Yongming Yi; Chunye Gong; Jie Liu; Kai Lu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap478&sess=sess286)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Graph partitioning is essential for effectively processing large-scale graphs in distributed computing systems. However, traditional graph partitioning strategies frequently lead to elevated communication costs, particularly within distributed computing systems that utilize thousands of computing nodes. This is because prior partitioning methods fail to consider the variations in communication costs across the communication hierarchies. We propose TianheEngine for leveraging the communication hierarchy among distributed computing systems containing thousands of computing nodes. TianheEngine introduces an adaptive, communication hierarchy-aware methodology to partition and distribute large graphs across computing nodes. It exploits the communication hierarchy of the underlying distributed computing system and the sparsity characteristics of the input graphs to improve communication efficiency. We evaluated TianheEngine on fundamental graph operations using both synthetic and real-world

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
