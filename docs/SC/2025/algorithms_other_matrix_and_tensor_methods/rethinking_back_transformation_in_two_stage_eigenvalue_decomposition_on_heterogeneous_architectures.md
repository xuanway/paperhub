---
title: "Rethinking Back Transformation in Two-Stage Eigenvalue Decomposition on Heterogeneous Architectures"
description: "SC 2025 · Algorithms: Other Matrix and Tensor Methods · Hansheng Wang; Dajun Huang; Gaoyuan Zou; Lu Shi; Xu Jiang; Xi Wu; Hancong Duan; "
tags:
  - "SC2025"
  - "Algorithms: Other Matrix and Tensor Methods"
---

# Rethinking Back Transformation in Two-Stage Eigenvalue Decomposition on Heterogeneous Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Other Matrix and Tensor Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Other Matrix and Tensor Methods</p>
</div>

**作者**：Hansheng Wang; Dajun Huang; Gaoyuan Zou; Lu Shi; Xu Jiang; Xi Wu; Hancong Duan; Shaoshuai Zhang

**会议**：SC 2025 · St. Louis, MO

## 摘要

The two-stage eigenvalue decomposition (EVD) method outperforms conventional one-stage methods on GPUs and heterogeneous architectures, especially when eigenvectors are not required. However, its performance advantage diminishes when performing back transformation to obtain eigenvectors. To address this, we propose two key solutions: 1) replacing BLAS3 operations with BLAS2 operations during the bulge-chasing back transformation for better performance, and 2) reordering the back transformation workflow from a backward pattern to a new parallelism-driven pattern to hide divide-and-conquer latency, at the cost of one additional GEMM computation. Experimentally, the proposed back transformation algorithm demonstrates significant performance improvements, outperforming the SOTA implementation in MAGMA by an average factor of 3.58x. For complete FP64 precision symmetric EVD with eigenvectors, the proposed algorithm, incorporating both solutions, surpasses the SOTA implementations in MAGMA a

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
