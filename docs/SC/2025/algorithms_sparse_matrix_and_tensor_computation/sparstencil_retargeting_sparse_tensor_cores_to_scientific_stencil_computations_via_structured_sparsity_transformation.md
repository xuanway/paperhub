---
title: "SparStencil: Retargeting Sparse Tensor Cores to Scientific Stencil Computations via Structured Sparsity Transformation"
description: "SC 2025 · Algorithms: Sparse Matrix and Tensor Computation · Qi Li; Kun Li; Liang Yuan; Yunquan Zhang; Junshi Chen; Hong An; Ting Cao; Mao Ya"
tags:
  - "SC2025"
  - "Algorithms: Sparse Matrix and Tensor Computation"
---

# SparStencil: Retargeting Sparse Tensor Cores to Scientific Stencil Computations via Structured Sparsity Transformation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Qi Li; Kun Li; Liang Yuan; Yunquan Zhang; Junshi Chen; Hong An; Ting Cao; Mao Yang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Sparse Tensor Cores offer exceptional performance gains for AI workloads by exploiting structured 2:4 sparsity. However, their potential remains untapped for core scientific workloads such as stencil computations, which exhibit irregular sparsity patterns. This paper presents SparStencil, the first system to retarget sparse TCUs for scientific stencil computations through structured sparsity transformation. SparStencil introduces three key techniques: (1) Adaptive Layout Morphing, which restructures stencil patterns into staircase-aligned sparse matrices via a flatten-and-crush pipeline; (2) Structured Sparsity Conversion, which formulates transformation as a graph matching problem to ensure compatibility with 2:4 sparsity constraints; (3) Automatic Kernel Generation, which compiles transformed stencils into optimized sparse MMA kernels via layout search and table-driven memory mapping. Evaluated on 79 stencil kernels spanning diverse scientific domains, SparStencil achieves up to 7.1x

---

## 一句话总结

> 该工作属于 Algorithms: Sparse Matrix and Tensor Computation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Sparse Matrix and Tensor Computation 领域贡献新的设计范式或评估框架。
