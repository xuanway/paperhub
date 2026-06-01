---
title: "TianheEngine: Hierarchy-Aware Adaptive Partitioning System for Trillion-Scale Graph Processing"
description: "SC 2025 · Scheduling, Tiling, and Parallelism · Xinbiao Gan; Tiejun Li; Yiqi Wang; Qiang Zhang; Yongming Yi; Chunye Gong; Jie Li"
tags:
  - "SC2025"
  - "Scheduling, Tiling, and Parallelism"
---

# TianheEngine: Hierarchy-Aware Adaptive Partitioning System for Trillion-Scale Graph Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Scheduling, Tiling, and Parallelism。</p>
<p class="paper-seo-summary__tags">SC 2025 · Scheduling, Tiling, and Parallelism</p>
</div>

**作者**：Xinbiao Gan; Tiejun Li; Yiqi Wang; Qiang Zhang; Yongming Yi; Chunye Gong; Jie Liu; Kai Lu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Graph partitioning is essential for effectively processing large-scale graphs in distributed computing systems. However, traditional graph partitioning strategies frequently lead to elevated communication costs, particularly within distributed computing systems that utilize thousands of computing nodes. This is because prior partitioning methods fail to consider the variations in communication costs across the communication hierarchies. We propose TianheEngine for leveraging the communication hierarchy among distributed computing systems containing thousands of computing nodes. TianheEngine introduces an adaptive, communication hierarchy-aware methodology to partition and distribute large graphs across computing nodes. It exploits the communication hierarchy of the underlying distributed computing system and the sparsity characteristics of the input graphs to improve communication efficiency. We evaluated TianheEngine on fundamental graph operations using both synthetic and real-world 

---

## 一句话总结

> 该工作属于 Scheduling, Tiling, and Parallelism 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Scheduling, Tiling, and Parallelism 领域贡献新的设计范式或评估框架。
