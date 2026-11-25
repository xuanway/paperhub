---
title: "Extending Sparse Patterns to Improve Inverse Preconditioning on GPU Architectures"
description: "HPDC 2024 · Session 6 — Accelerators & Scientific applications"
tags:
  - "HPDC2024"
  - "Session 6"
  - "Accelerators & Scientific applications"
---

# Extending Sparse Patterns to Improve Inverse Preconditioning on GPU Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 6 — Accelerators & Scientific applications（2024年6月7日 10:00–11:15 · Session Chair：Raffaele Montella）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 6</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658683)

**作者**：Sergi Laut, Ricard Borrell, Marc Casas

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 6 — Accelerators & Scientific applications（2024年6月7日 10:00–11:15 · Session Chair：Raffaele Montella）

---

## 英文摘要

Graphic Processing Units (GPUs) have become a key component of high-end computing infrastructures due to their massively parallel architecture, which delivers large floating-point operations per cycle rates. Many scientific workloads benefit from GPUs and, in particular, numerical methods solving linear systems of equations Ax = b typically run on GPUs. Among them, the Conjugate Gradient (CG) method, which targets linear systems with Symmetric and Positive Definite (SPD) matrices, runs on GPUs using its preconditioned form. However, state-of-the-art preconditioning techniques like the Factorized Sparse Approximate Inverse (FSAI) preconditioner ignore the benefits of data coalescence and locality on GPU architectures and leave substantial performance on the table. These approaches are exclusively based on numerical criteria. This paper proposes the GPU-aware Factorized Sparse Approximate Inverse (GFSAI) preconditioner. GFSAI generates sparse patterns that enhance the numerical benefits of FSAI and improve data locality and coalescence on GPU architectures. We evaluate GFSAI considering NVIDIA V100 and AMD MI50 GPUs and a set of 47 sparse matrices. GFSAI improves the state-of-the-art by reducing the average CG iteration count by 27.48% and 31.25% on NVIDIA and AMD, respectively, which leads to average decreases in execution time of 23.83% and 26.07% in these two GPU architectures.

## 中文摘要

图形处理器（GPU）凭借其大规模并行架构，每个时钟周期可提供大量浮点运算，已成为高端计算基础设施的关键组件。许多科学负载受益于 GPU，特别是求解线性方程组 Ax = b 的数值方法通常运行在 GPU 上。其中，针对对称正定（SPD）矩阵线性系统的共轭梯度（CG）方法以预处理形式在 GPU 上运行。然而，因子化稀疏近似逆（FSAI）预处理等最先进预处理技术忽略了 GPU 架构上数据合并与局部性的收益，损失了大量性能。这些方法完全基于数值准则。本文提出 GPU 感知的因子化稀疏近似逆（GFSAI）预处理器。GFSAI 生成的稀疏模式既增强了 FSAI 的数值收益，又改善了 GPU 架构上的数据局部性与合并。我们在 NVIDIA V100 与 AMD MI50 GPU 以及 47 个稀疏矩阵上评估 GFSAI。GFSAI 超越最先进水平，在 NVIDIA 与 AMD 上分别将平均 CG 迭代次数减少 27.48% 与 31.25%，从而使这两种 GPU 架构上的执行时间平均减少 23.83% 与 26.07%。

## 英文关键词

Sparse Linear Algebra, GPUs, Memory Coalescing, Spatial Locality

## 中文关键词

稀疏线性代数，GPU，内存合并，空间局部性

---

[← 返回 Session 6 — Accelerators & Scientific applications](index.md)
