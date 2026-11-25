---
title: "Session 8: Tensor Cores"
description: "PPoPP 2025 Session 8（Tensor Cores），2025 年 3 月 4 日 14:00–15:20，Acacia D，共 4 篇论文。"
tags:
  - "PPoPP2025"
  - "Session-8"
  - "Tensor Cores"
---

# Session 8: Tensor Cores

**PPoPP 2025 · 2025 年 3 月 4 日 14:00–15:20 · Acacia D · Session Chair：Jeffrey Vetter**

聚焦张量核上的稀疏与结构化计算：稀疏矩阵乘、通用 SpMM 库、位张量核 BFS，以及由 FFT 驱动的 stencil 计算。

本 Session 共收录 **4** 篇论文。

**官方议程：** [PPoPP 2025 Main Conference](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [FlashSparse: Minimizing Computation Redundancy for Fast Sparse Matrix Multiplications on Tensor Cores](flashsparse_minimizing_computation_redundancy_for_fast_sparse_matrix_multiplications_on_tensor_cores.md) | Jinliang Shi 等 6 人 | swap-and-transpose 最小化稀疏粒度，几何平均 5.5× 加速 |
| 2 | [Acc-SpMM: Accelerating General-purpose Sparse Matrix-Matrix Multiplication with GPU Tensor Cores](acc_spmm_accelerating_general_purpose_sparse_matrix_matrix_multiplication_with_gpu_tensor_cores.md) | Haisha Zhao 等 13 人 | 四项系统优化，H100 上平均 1.58×、最高 3.60× |
| 3 | [🏆 BerryBees: Breadth First Search by Bit-Tensor-Cores](berrybees_breadth_first_search_by_bit_tensor_cores.md) | Yuyao Niu 等 2 人 | 位图 BRS + TCU MMA，较 SOTA 平均最高 5.05×；获两项大奖 |
| 4 | [FlashFFTStencil: Bridging Fast Fourier Transforms to Memory-Efficient Stencil Computations on Tensor Core Units](flashfftstencil_bridging_fast_fourier_transforms_to_memory_efficient_stencil_computations_on_tensor_core_units.md) | Haozhi Han 等 10 人 | HBM/SMEM/TCU 三层优化，平均加速 2.57× |

### 获奖

- **BerryBees: Breadth First Search by Bit-Tensor-Cores** —— Distinguished Paper Award · Best Artifact Award

---

[← Session 7: Scheduling and Resource Management](../Session-7/index.md) · [PPoPP 2025 总览](../index.md) · [Session 9: Concurrent Data Structures and Synchronization II →](../Session-9/index.md)
