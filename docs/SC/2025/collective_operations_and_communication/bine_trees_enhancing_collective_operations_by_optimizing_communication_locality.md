---
title: "Bine Trees: Enhancing Collective Operations by Optimizing Communication Locality"
description: "SC 2025 · Collective Operations and Communication · Daniele De Sensi; Saverio Pasqualoni; Lorenzo Piarulli; Tommaso Bonato; Seydou B"
tags:
  - "SC2025"
  - "Collective Operations and Communication"
---

# Bine Trees: Enhancing Collective Operations by Optimizing Communication Locality

**中文标题：** 通过优化通信局部性增强集合操作

**所属 Session：** [Collective Operations and Communication](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Collective Operations and Communication。</p>
<p class="paper-seo-summary__tags">SC 2025 · Collective Operations and Communication</p>
</div>

**作者**：Daniele De Sensi; Saverio Pasqualoni; Lorenzo Piarulli; Tommaso Bonato; Seydou Ba; Matteo Turisini; Jens Domke; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap505&sess=sess296)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Communication locality plays a key role in the performance of collective operations on large HPC systems, especially on oversubscribed networks where groups of nodes are fully connected internally but sparsely linked through global connections. We present \Bine (\textit{\underline{bi}nomial \underline{ne}gabinary}) trees, a family of collective algorithms that improve communication locality. \Bine trees maintain the generality of binomial trees and butterflies while cutting global-link traffic by up to $33\%$. We implement eight \Bine-based collectives and evaluate them on four large-scale supercomputers with Dragonfly, Dragonfly+, oversubscribed fat-tree, and torus topologies, achieving up to $5\times$ speedups and consistent reductions in global-link traffic across different vector sizes and node counts.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
