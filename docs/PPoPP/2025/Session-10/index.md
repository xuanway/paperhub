---
title: "Session 10: GPU II"
description: "PPoPP 2025 Session 10（GPU II），2025 年 3 月 5 日 10:00–11:20，Acacia D，共 4 篇论文。"
tags:
  - "PPoPP2025"
  - "Session-10"
  - "GPU II"
---

# Session 10: GPU II

**PPoPP 2025 · 2025 年 3 月 5 日 10:00–11:20 · Acacia D · Session Chair：Zhijia Zhao**

关注 GPU 上的图与数值计算：用稀疏线性代数加速 Kernel K-means、GPU 上的 Louvain 社区发现、LUT 加速图模式挖掘，以及三对角化性能优化。

本 Session 共收录 **4** 篇论文。

**官方议程：** [PPoPP 2025 Main Conference](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Popcorn: Accelerating Kernel K-means on GPUs through Sparse Linear Algebra](popcorn_accelerating_kernel_k_means_on_gpus_through_sparse_linear_algebra.md) | Julian Bellavita 等 5 人 | SpMM/SpMV 表述 Kernel K-means，比 CPU 最高 123.8× |
| 2 | [Swift Unfolding of Communities: GPU-Accelerated Louvain Algorithm](swift_unfolding_of_communities_gpu_accelerated_louvain_algorithm.md) | Zhibin Wang 等 8 人 | 模块度增益剪枝 + 负载感知 kernel，平均超越 SOTA 6× |
| 3 | [GLUMIN: Fast Connectivity Check Based on LUTs For Efficient Graph Pattern Mining](glumin_fast_connectivity_check_based_on_luts_for_efficient_graph_pattern_mining.md) | Weichen Cao 等 4 人 | 运行时压缩 LUT 加速连通性检查，GPM 系统提速两个数量级 |
| 4 | [Improving Tridiagonalization Performance on GPU Architectures](improving_tridiagonalization_performance_on_gpu_architectures.md) | Hansheng Wang 等 8 人 | 双重分块 band reduction + GPU bulge chasing，最高 19.6 TFLOPs |

---

[← Session 9: Concurrent Data Structures and Synchronization II](../Session-9/index.md) · [PPoPP 2025 总览](../index.md) · [Session 11: Parallel Algorithms and Applications →](../Session-11/index.md)
