---
title: "Bine Trees: Enhancing Collective Operations by Optimizing Communication Locality"
description: "SC 2025 · Collective Operations and Communication · Daniele De Sensi; Saverio Pasqualoni; Lorenzo Piarulli; Tommaso Bonato; Seydou B"
tags:
  - "SC2025"
  - "Collective Operations and Communication"
---

# Bine Trees: Enhancing Collective Operations by Optimizing Communication Locality

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Collective Operations and Communication。</p>
<p class="paper-seo-summary__tags">SC 2025 · Collective Operations and Communication</p>
</div>

**作者**：Daniele De Sensi; Saverio Pasqualoni; Lorenzo Piarulli; Tommaso Bonato; Seydou Ba; Matteo Turisini; Jens Domke; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

## 摘要

Communication locality plays a key role in the performance of collective operations on large HPC systems, especially on oversubscribed networks where groups of nodes are fully connected internally but sparsely linked through global connections. We present \Bine (\textit{\underline{bi}nomial \underline{ne}gabinary}) trees, a family of collective algorithms that improve communication locality. \Bine trees maintain the generality of binomial trees and butterflies while cutting global-link traffic by up to $33\%$. We implement eight \Bine-based collectives and evaluate them on four large-scale supercomputers with Dragonfly, Dragonfly+, oversubscribed fat-tree, and torus topologies, achieving up to $5\times$ speedups and consistent reductions in global-link traffic across different vector sizes and node counts.

---

## 一句话总结

> 该工作属于 Collective Operations and Communication 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Collective Operations and Communication 领域贡献新的设计范式或评估框架。
