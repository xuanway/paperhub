---
title: "A Diagonal Block Memory-Aware Polynomial Preconditioner for Linear and Eigenvalue Solvers"
description: "PPoPP 2026 Session 13（Matrix and Linear Algebra Algorithms）：对角块划分矩阵幂核，MPK 提升 26.6–38.4%，端到端 18.6–34.0%"
tags:
  - "PPoPP2026"
  - "Session-13"
  - "Matrix and Linear Algebra Algorithms"
  - "Preconditioner"
  - "Krylov Methods"
  - "Sparse Linear Algebra"
authors:
  - "Xiaojian Yang"
  - "Yuhui Ni"
  - "Fan Yuan"
  - "Shengguo Li"
  - "Dezun Dong"
  - "Chuanfu Xu"
  - "Haipeng Jia"
  - "Jie Liu"
session: "Session 13: Matrix and Linear Algebra Algorithms"
session_number: 13
session_chair: "William S. Moses"
date: "2026-02-04"
time: "10:10–10:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786446"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# A Diagonal Block Memory-Aware Polynomial Preconditioner for Linear and Eigenvalue Solvers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 DBMPK，将对角块划分用于矩阵幂核以复用块内数据、消除块间依赖，在 x86 与 Arm 平台上使 MPK 提升 26.6%–38.4%、端到端加速 18.6%–34.0%。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 13: Matrix and Linear Algebra Algorithms</p>
</div>

**作者**：Xiaojian Yang, Yuhui Ni, Fan Yuan, Shengguo Li, Dezun Dong, Chuanfu Xu, Haipeng Jia, and Jie Liu — National University of Defense Technology, China; Xiangtan University, China; University of Chinese Academy of Sciences, China

**会议**：PPoPP 2026 · 2026 年 2 月 4 日 10:10–10:30 · Session 13: Matrix and Linear Algebra Algorithms（主席：William S. Moses）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786446) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Krylov subspace methods are widely used in scientific computing to solve large sparse linear systems and eigenvalue problems. Their performance bottleneck is often dominated by high-order matrix-power kernels (MPK), especially in polynomial preconditioners that must scale to millions or billions of variables. We present Diagonal Block MPK (DBMPK), a lightweight and parallel-friendly optimization that partitions the input matrix into diagonal blocks and off-diagonal regions. This design enables efficient intra-block data reuse and eliminates inter-block dependencies. It improves cache locality, parallelism, and reduces preprocessing overheads, compared to existing techniques. Our evaluation on x86 and Arm HPC platforms shows that DBMPK improves MPK performance by 26.6%-38.4%. When applied to polynomial preconditioners for linear systems and eigenvalue problems, it achieves consistent end-to-end speedups of 18.6%-34.0%, These authors contribute equally to this research.

## 中文摘要

Krylov 子空间方法被广泛用于科学计算中求解大规模稀疏线性系统与特征值问题。其性能瓶颈通常由高阶矩阵幂核函数（MPK）主导，在必须扩展到数百万乃至数十亿变量的多项式预条件子中尤为如此。我们提出对角块 MPK（DBMPK），一种轻量且易于并行的优化方法，它将输入矩阵划分为对角块与非对角区域。该设计实现了高效的块内数据复用，并消除了块间依赖。与现有技术相比，它改善了缓存局部性与并行性，并降低了预处理开销。在 x86 与 Arm HPC 平台上的评测表明，DBMPK 将 MPK 性能提升 26.6%–38.4%。将其应用于线性系统与特征值问题的多项式预条件子时，可获得 18.6%–34.0% 的一致端到端加速。

## 英文关键词

Matrix-Power Kernel, Diagonal Block, Polynomial Preconditioning

## 中文关键词

矩阵幂核；对角块；多项式预条件

---

## 一句话总结

> 提出 DBMPK，将对角块划分用于矩阵幂核以复用块内数据、消除块间依赖，在 x86 与 Arm 平台上使 MPK 提升 26.6%–38.4%、端到端加速 18.6%–34.0%。

## 研究问题

Krylov 子空间方法求解稀疏线性系统与特征值问题时，性能瓶颈常由高阶矩阵幂核（MPK）主导；多项式预条件器需扩展到百万乃至十亿级变量，而现有实现在缓存局部性、并行性与预处理开销上存在不足。

## 方法简述

- 提出 DBMPK，将输入矩阵划分为对角块与对角外区域两部分。
- 该划分实现高效的块内数据复用并消除块间依赖，从而改善缓存局部性、提升并行性。
- 相比现有技术降低预处理开销，并保持轻量、对并行友好的设计。

## 主要结果

- 在 x86 与 Arm HPC 平台上，MPK 性能提升 26.6%–38.4%。
- 用于线性系统与特征值问题的多项式预条件器时，取得 18.6%–34.0% 的端到端稳定加速。

---

> 所属 Session：[Session 13: Matrix and Linear Algebra Algorithms](index.md) · 返回 [PPoPP 2026 总览](../index.md)
