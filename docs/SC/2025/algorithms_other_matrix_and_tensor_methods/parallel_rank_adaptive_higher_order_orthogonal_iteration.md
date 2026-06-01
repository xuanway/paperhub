---
title: "Parallel Rank-Adaptive Higher-Order Orthogonal Iteration"
description: "SC 2025 · Algorithms: Other Matrix and Tensor Methods · Joao Pinheiro; Aditya Devarakonda; Grey Ballard"
tags:
  - "SC2025"
  - "Algorithms: Other Matrix and Tensor Methods"
---

# Parallel Rank-Adaptive Higher-Order Orthogonal Iteration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Other Matrix and Tensor Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Other Matrix and Tensor Methods</p>
</div>

**作者**：Joao Pinheiro; Aditya Devarakonda; Grey Ballard

**会议**：SC 2025 · St. Louis, MO

## 摘要

Higher-order orthogonal iteration (HOOI) is an iterative algorithm that computes a Tucker decomposition of fixed ranks of an input tensor. In this work we modify HOOI to determine ranks adaptively subject to a fixed approximation error, apply optimizations to reduce the cost of each HOOI iteration, and parallelize the method in order to scale to large, dense datasets. We show that HOOI is competitive with the sequentially truncated higher-order singular value decomposition (ST-HOSVD) algorithm, particularly in cases of high compression ratios. Our proposed rank-adaptive HOOI can achieve comparable approximation error to ST-HOSVD in less time, sometimes achieving a better compression ratio. We demonstrate that our parallelization scales well over thousands of cores and show, using three scientific simulation datasets, that HOOI outperforms ST-HOSVD in high-compression regimes. For example, for a 3D fluid-flow simulation dataset, HOOI computes a Tucker decomposition 82x faster and achiev

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
