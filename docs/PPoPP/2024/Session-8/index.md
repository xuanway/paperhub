---
title: "Session 8: Optimizing for Memory"
description: "PPoPP 2024 Session 8（Optimizing for Memory），2024 年 3 月 5 日 16:10–17:10，Moorfoot，共 3 篇论文。"
tags:
  - "PPoPP2024"
  - "Session-8"
  - "Optimizing for Memory"
---

# Session 8: Optimizing for Memory

**PPoPP 2024 · 2024 年 3 月 5 日 16:10–17:10 · Moorfoot · Session Chair：Yan Gu**

关注内存优化：把 stencil 计算转换为张量核矩阵乘的 ConvStencil、无指针的批量并行压缩集合，以及通用 GPU 内存管理器。

本 Session 共收录 **3** 篇论文。

官方议程：[PPoPP 2024 Main Conference Papers](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [🏆 ConvStencil: Transform Stencil Computation to Matrix Multiplication on Tensor Cores](convstencil_transform_stencil_computation_to_matrix_multiplication_on_tensor_cores.md) | Yuetao Chen 等 10 人 | 将 stencil 计算转为张量核矩阵乘，显著超越 AMOS、cuDNN 等框架 |
| 2 | [CPMA: An Efficient Batch-Parallel Compressed Set Without Pointers](cpma_an_efficient_batch_parallel_compressed_set_without_pointers.md) | Brian Wheatman 等 4 人 | 无指针的批并行压缩 PMA，批量插入 3×、范围查询 4× 吞吐 |
| 3 | [Gallatin: A General-Purpose GPU Memory Manager](gallatin_a_general_purpose_gpu_memory_manager.md) | Hunter McCoy 等 2 人 | 基于 vEB 树的通用 GPU 内存管理器，混合尺寸分配最高 264× |

### 获奖

- **ConvStencil: Transform Stencil Computation to Matrix Multiplication on Tensor Cores** —— Best Paper Award

---

[← Session 7: Parallel Algorithms](../Session-7/index.md) · [PPoPP 2024 总览](../index.md) · [Session 9: Linear Algebra →](../Session-9/index.md)
