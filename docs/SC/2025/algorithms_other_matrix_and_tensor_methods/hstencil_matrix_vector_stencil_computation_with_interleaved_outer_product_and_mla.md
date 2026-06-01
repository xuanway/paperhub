---
title: "HStencil: Matrix-Vector Stencil Computation with Interleaved Outer Product and MLA"
description: "SC 2025 · Algorithms: Other Matrix and Tensor Methods · Han Huang; Jiabin Xie; Guangnan Feng; Xianwei Zhang; Dan Huang; Zhiguang Chen; Y"
tags:
  - "SC2025"
  - "Algorithms: Other Matrix and Tensor Methods"
---

# HStencil: Matrix-Vector Stencil Computation with Interleaved Outer Product and MLA

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Other Matrix and Tensor Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Other Matrix and Tensor Methods</p>
</div>

**作者**：Han Huang; Jiabin Xie; Guangnan Feng; Xianwei Zhang; Dan Huang; Zhiguang Chen; Yutong Lu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Stencil computations are fundamental to various HPC and intelligent computing applications, often consuming significant execution time. The emergence of specialized matrix units presents new opportunities to accelerate stencil computations. While scalable matrix compute units provide substantial computing horsepower, prior efforts fail to fully utilize the computing capabilities for stencils due to suboptimal matrix-unit utilization, limited instruction-level parallelism, and low cache hit rates. This paper introduces HStencil, a novel stencil computing framework utilizing matrix and vector units. HStencil addresses these challenges through three contributions: 1) microkernels that jointly leverage matrix and vector units to enhance hardware utilization; 2) fine-grained instruction scheduling with interleaved execution to enhance instruction-level parallelism; and 3) spatial prefetch to sustain high performance when working sets exceed cache capacity. Evaluations on representative benc

---

## 一句话总结

> 该工作属于 Algorithms: Other Matrix and Tensor Methods 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Other Matrix and Tensor Methods 领域贡献新的设计范式或评估框架。
