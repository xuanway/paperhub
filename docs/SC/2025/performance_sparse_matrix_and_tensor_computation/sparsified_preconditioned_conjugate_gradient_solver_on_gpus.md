---
title: "Sparsified Preconditioned Conjugate Gradient Solver on GPUs"
description: "SC 2025 · Performance: Sparse Matrix and Tensor Computation · Da Ma; Khalid Ahmad; Kazem Cheshmi; Hari Sundar; Mary Hall"
tags:
  - "SC2025"
  - "Performance: Sparse Matrix and Tensor Computation"
---

# Sparsified Preconditioned Conjugate Gradient Solver on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Da Ma; Khalid Ahmad; Kazem Cheshmi; Hari Sundar; Mary Hall

**会议**：SC 2025 · St. Louis, MO

## 摘要

Preconditioned iterative sparse linear solvers are memory-efficient for large scientific simulations, but the dependences between iterations introduced by preconditioners limit parallelization. This issue is exacerbated on GPUs, which feature many parallel cores. We propose a sparsified preconditioned conjugate gradient (SPCG) solver that increases parallelism by reducing dependences through sparsification, while preserving convergence behavior. We evaluate the proposed SPCG using both ILU(0) and ILU(K) preconditioners on a wide range of symmetric positive definite (SPD) matrices. The proposed SPCG improves the performance of the iterative phase of SPCG by a geometric mean speedup of 1.23$\times$ and 1.65$\times$ over the non-sparsified PCG using ILU(0) and ILU(K), respectively, on an NVIDIA A100 GPU. SPCG also yields geometric mean end-to-end speedups of 1.68$\times$ and 3.73$\times$ over the non-sparsified versions with ILU(0) and ILU(K), respectively, on the same platform.

---

## 一句话总结

> 该工作属于 Performance: Sparse Matrix and Tensor Computation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Performance: Sparse Matrix and Tensor Computation 领域贡献新的设计范式或评估框架。
