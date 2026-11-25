---
title: "Session 13: Matrix and Linear Algebra Algorithms"
description: "PPoPP 2026 Session 13（Matrix and Linear Algebra Algorithms），2026 年 2 月 4 日 09:50–11:10，Pyrmont，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-13"
  - "Matrix and Linear Algebra Algorithms"
---

# Session 13: Matrix and Linear Algebra Algorithms

**PPoPP 2026 · 2026 年 2 月 4 日 09:50–11:10 · Pyrmont · Session Chair：William S. Moses**

关注矩阵与线性代数算法：秩亏矩阵的高效 SVD、内存感知多项式预条件子、性能波动下的分布式矩阵-块-向量乘，以及矩阵乘单元的跨模式刻画。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Towards Singular Value Decomposition for Rank-Deficient Matrices: An Efficient and Accurate Algorithm on GPU Architectures](towards_singular_value_decomposition_for_rank_deficient_matrices_an_efficient_and_accurate_algorithm_on_gpu_architectures.md) | Lu Shi 等 3 人 | 秩揭示 QB 分解的秩亏 SVD，较 cuSOLVER 满 SVD 最高 6978× |
| 2 | [A Diagonal Block Memory-Aware Polynomial Preconditioner for Linear and Eigenvalue Solvers](a_diagonal_block_memory_aware_polynomial_preconditioner_for_linear_and_eigenvalue_solvers.md) | Xiaojian Yang 等 8 人 | 对角块划分矩阵幂核，MPK 提升 26.6–38.4%，端到端 18.6–34.0% |
| 3 | [A Distributed Matrix-Block-Vector Multiplication in Presence of System Performance Variability](a_distributed_matrix_block_vector_multiplication_in_presence_of_system_performance_variability.md) | Yuchen Ma 等 3 人 | 1D 流水线 + 静态调度，较 COSMA 1.85×、ScaLAPACK 17× |
| 4 | [Characterizing Matrix Multiplication Units across General Parallel Patterns in Scientific Computing](characterizing_matrix_multiplication_units_across_general_parallel_patterns_in_scientific_computing.md) | Yuechen Lu 等 4 人 | 10 个 MMU 核 + 四象限分类，给出 9 条关键观察 |

---

[← Session 12: Optimizing Transformers](../Session-12/index.md) · [PPoPP 2026 总览](../index.md)
