---
title: "Session 5: Stencil and Sparse Matrix Computation"
description: "PPoPP 2026 Session 5（Stencil and Sparse Matrix Computation），2026 年 2 月 3 日 09:50–11:10，Pyrmont，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-5"
  - "Stencil and Sparse Matrix Computation"
---

# Session 5: Stencil and Sparse Matrix Computation

**PPoPP 2026 · 2026 年 2 月 3 日 09:50–11:10 · Pyrmont · Session Chair：Shoaib Kamil**

聚焦 stencil 与稀疏矩阵计算：稀疏张量核 stencil、Arm SME 上的 SpMM、Tensor Core 上的 SpMV，以及 GPU 稀疏矩阵-稀疏向量乘。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [SPIDER: Unleashing Sparse Tensor Cores for Stencil Computation via Strided Swapping](spider_unleashing_sparse_tensor_cores_for_stencil_computation_via_strided_swapping.md) | Qiqi Gu 等 4 人 | 首个用稀疏张量核加速模板计算，比 cuDNN 快 6.23× |
| 2 | [ASM-SpMM: Unleashing the Potential of Arm SME for Sparse Matrix Multiplication Acceleration](asm_spmm_unleashing_the_potential_of_arm_sme_for_sparse_matrix_multiplication_acceleration.md) | Jiazhi Jiang 等 6 人 | SME 感知 SpMM 库，异构核工作窃取，最高 7.9× 加速 |
| 3 | [Exploiting Efficient Mapping and Pipelined Execution for Accelerating SpMV on Tensor Cores](exploiting_efficient_mapping_and_pipelined_execution_for_accelerating_spmv_on_tensor_cores.md) | Kaige Zhang 等 8 人 | zig-zag 链式存储 + 多级寄存器流水，FP32 下 2.95× |
| 4 | [VDHA: Vector-Driven Hash Aggregation for Sparse Matrix-Sparse Vector Multiplication on GPUs](vdha_vector_driven_hash_aggregation_for_sparse_matrix_sparse_vector_multiplication_on_gpus.md) | Yuchen Li 等 4 人 | 块私有哈希表做局部聚合，网页图几何平均 1.41× |

---

[← Session 4: GPU and Heterogeneous Computing](../Session-4/index.md) · [PPoPP 2026 总览](../index.md) · [Session 6: Mixed Precision and Quantization →](../Session-6/index.md)
