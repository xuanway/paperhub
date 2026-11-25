---
title: "Session 7: Parallel Algorithms"
description: "PPoPP 2024 Session 7（Parallel Algorithms），2024 年 3 月 5 日 14:20–15:40，Moorfoot，共 4 篇论文。"
tags:
  - "PPoPP2024"
  - "Session-7"
  - "Parallel Algorithms"
---

# Session 7: Parallel Algorithms

**PPoPP 2024 · 2024 年 3 月 5 日 14:20–15:40 · Moorfoot · Session Chair：Prashant Pandey**

聚焦并行算法：可扩展且确定性的并行图 ANNS、带批量更新与异步读的并行 k-core 分解、并行整数排序，以及非线性 stencil 的期权定价。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2024 Main Conference Papers](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [ParlayANN: Scalable and Deterministic Parallel Graph-Based Approximate Nearest Neighbor Search Algorithms](parlayann_scalable_and_deterministic_parallel_graph_based_approximate_nearest_neighbor_search_algorithms.md) | Magdalen Dobson Manohar 等 7 人 | 确定性并行图 ANNS 库，可扩展到十亿级数据集 |
| 2 | [Parallel k-Core Decomposition with Batched Updates and Asynchronous Reads](parallel_k_core_decomposition_with_batched_updates_and_asynchronous_reads.md) | Quanquan C. Liu 等 3 人 | 异步读与更新批并发的 k-core 结构，读延迟降低达 4.05×10⁵ 倍 |
| 3 | [Parallel Integer Sort: Theory and Practice](parallel_integer_sort_theory_and_practice.md) | Xiaojun Dong 等 4 人 | DovetailSort：融合整数排序与比较排序思想以利用重复键 |
| 4 | [Fast American Option Pricing using Nonlinear Stencils](fast_american_option_pricing_using_nonlinear_stencils.md) | Zafar Ahmad 等 6 人 | 以 FFT 求解非线性 stencil 的期权定价，T≈0.5×10⁶ 时提速超 500× |

---

[← Session 6: ML Workloads](../Session-6/index.md) · [PPoPP 2024 总览](../index.md) · [Session 8: Optimizing for Memory →](../Session-8/index.md)
