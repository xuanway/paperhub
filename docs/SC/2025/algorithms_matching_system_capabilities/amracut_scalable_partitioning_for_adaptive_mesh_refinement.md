---
title: "AMRaCut: Scalable Partitioning for Adaptive Mesh Refinement"
description: "SC 2025 · Algorithms: Matching System Capabilities · Budvin Edippuliarachchi; David Van Komen; Hari Sundar"
tags:
  - "SC2025"
  - "Algorithms: Matching System Capabilities"
---

# AMRaCut: Scalable Partitioning for Adaptive Mesh Refinement

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matching System Capabilities。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matching System Capabilities</p>
</div>

**作者**：Budvin Edippuliarachchi; David Van Komen; Hari Sundar

**会议**：SC 2025 · St. Louis, MO

## 摘要

Mesh partitioning is critical for scalable distributed PDE solvers. Traditional methods like spatial ordering and multi-level graph partitioning have significant tradeoffs between partition quality and parallel scalability. We present AMRaCut, a distributed-parallel mesh partitioner that bridges this gap using parallel label propagation and graph diffusion. It operates mostly locally on initial partitions, limiting inter-process communications to neighboring processes. This locality is especially effective in AMR, where mesh evolves dynamically with mostly local changes. AMRaCut achieves 5x-10x speedups over multi-level partitioners (ParMETIS, PT-Scotch) while producing partitions of comparable quality and minimized boundaries. Its efficiency is comparable to sorting-based methods like space-filling curves. AMRaCut maintains maximum partition load within 2x of optimal, sufficient for distributed scalability. We verify that AMRaCut is effective in downstream tasks by evaluating a Finite

---

## 一句话总结

> 该工作属于 Algorithms: Matching System Capabilities 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Matching System Capabilities 领域贡献新的设计范式或评估框架。
