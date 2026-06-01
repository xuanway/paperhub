---
title: "T2-RELION: Task Parallelism, Tensor Core Accelerated RELION for Cryo-EM 3D Reconstruction"
description: "SC 2025 · Applications: Biological Modeling · Jiayu Fu; Jingle Xu; Lin Gan; Tianqi Mao; Zirong Shen; Yinuo Wang; Zeyu Song; Xi"
tags:
  - "SC2025"
  - "Applications: Biological Modeling"
---

# T2-RELION: Task Parallelism, Tensor Core Accelerated RELION for Cryo-EM 3D Reconstruction

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Biological Modeling。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Biological Modeling</p>
</div>

**作者**：Jiayu Fu; Jingle Xu; Lin Gan; Tianqi Mao; Zirong Shen; Yinuo Wang; Zeyu Song; Xiaohui Duan; Wei Xue; Guangwen Yang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Cryo-electron microscopy (cryo-EM) is a key technique for structural biology, but its computational efficiency, particularly during 3D reconstruction, remains a bottleneck. We introduce T2-RELION, a highly optimized version of RELION for cryo-EM 3D reconstruction on CPU-GPU platforms. RELION is a widely used open-source package in the cryo-EM community. We identify and resolve key inefficiencies in RELION’s parallelization strategy and memory management by proposing task parallelism and a three-phase GPU memory management strategy. Furthermore, we leverage Tensor Cores to accelerate the hot-spot kernel for difference calculation, employing an advanced pipelining strategy to hide latency and enable thread block-level data reuse. On a quad-A100 GPU machine, performance evaluations demonstrate that T2-RELION outperforms RELION 4.0. For the hot-spot kernel, our optimizations achieve 1.90-23.7 times speedup. For the whole application using CNG and Trpv1 datasets, we observe 3.86 times and 2

---

## 一句话总结

> 该工作属于 Applications: Biological Modeling 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Applications: Biological Modeling 领域贡献新的设计范式或评估框架。
