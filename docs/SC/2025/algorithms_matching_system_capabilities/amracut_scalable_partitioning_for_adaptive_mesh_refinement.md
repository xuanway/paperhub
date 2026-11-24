---
title: "AMRaCut: Scalable Partitioning for Adaptive Mesh Refinement"
description: "SC 2025 · Algorithms: Matching System Capabilities · Budvin Edippuliarachchi; David Van Komen; Hari Sundar"
tags:
  - "SC2025"
  - "Algorithms: Matching System Capabilities"
---

# AMRaCut: Scalable Partitioning for Adaptive Mesh Refinement

**中文标题：** 面向自适应网格细化的可扩展分区

**所属 Session：** [Algorithms: Matching System Capabilities](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matching System Capabilities。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matching System Capabilities</p>
</div>

**作者**：Budvin Edippuliarachchi; David Van Komen; Hari Sundar

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap670&sess=sess307)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Mesh partitioning is critical for scalable distributed PDE solvers. Traditional methods like spatial ordering and multi-level graph partitioning have significant tradeoffs between partition quality and parallel scalability. We present AMRaCut, a distributed-parallel mesh partitioner that bridges this gap using parallel label propagation and graph diffusion. It operates mostly locally on initial partitions, limiting inter-process communications to neighboring processes. This locality is especially effective in AMR, where mesh evolves dynamically with mostly local changes. AMRaCut achieves 5x-10x speedups over multi-level partitioners (ParMETIS, PT-Scotch) while producing partitions of comparable quality and minimized boundaries. Its efficiency is comparable to sorting-based methods like space-filling curves. AMRaCut maintains maximum partition load within 2x of optimal, sufficient for distributed scalability. We verify that AMRaCut is effective in downstream tasks by evaluating a Finite

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
