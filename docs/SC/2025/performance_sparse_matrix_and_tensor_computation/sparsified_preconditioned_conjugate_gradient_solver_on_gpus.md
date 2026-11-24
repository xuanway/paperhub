---
title: "Sparsified Preconditioned Conjugate Gradient Solver on GPUs"
description: "SC 2025 · Performance: Sparse Matrix and Tensor Computation · Da Ma; Khalid Ahmad; Kazem Cheshmi; Hari Sundar; Mary Hall"
tags:
  - "SC2025"
  - "Performance: Sparse Matrix and Tensor Computation"
---

# Sparsified Preconditioned Conjugate Gradient Solver on GPUs

**中文标题：** GPU 上的稀疏化预条件共轭梯度求解器

**所属 Session：** [Performance: Sparse Matrix and Tensor Computation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Da Ma; Khalid Ahmad; Kazem Cheshmi; Hari Sundar; Mary Hall

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap268&sess=sess299)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Preconditioned iterative sparse linear solvers are memory-efficient for large scientific simulations, but the dependences between iterations introduced by preconditioners limit parallelization. This issue is exacerbated on GPUs, which feature many parallel cores. We propose a sparsified preconditioned conjugate gradient (SPCG) solver that increases parallelism by reducing dependences through sparsification, while preserving convergence behavior. We evaluate the proposed SPCG using both ILU(0) and ILU(K) preconditioners on a wide range of symmetric positive definite (SPD) matrices. The proposed SPCG improves the performance of the iterative phase of SPCG by a geometric mean speedup of 1.23$\times$ and 1.65$\times$ over the non-sparsified PCG using ILU(0) and ILU(K), respectively, on an NVIDIA A100 GPU. SPCG also yields geometric mean end-to-end speedups of 1.68$\times$ and 3.73$\times$ over the non-sparsified versions with ILU(0) and ILU(K), respectively, on the same platform.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
