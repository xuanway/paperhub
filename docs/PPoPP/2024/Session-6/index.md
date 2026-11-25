---
title: "Session 6: ML Workloads"
description: "PPoPP 2024 Session 6（ML Workloads），2024 年 3 月 5 日 11:30–12:30，Moorfoot，共 3 篇论文。"
tags:
  - "PPoPP2024"
  - "Session-6"
  - "ML Workloads"
---

# Session 6: ML Workloads

**PPoPP 2024 · 2024 年 3 月 5 日 11:30–12:30 · Moorfoot · Session Chair：Xipeng Shen**

关注 ML 负载：GPU 稀疏卷积的访存复用、异构 SoC 上共享内存争用感知的并发 DNN 执行，以及 DeePMD 模型的快速在线训练。

本 Session 共收录 **3** 篇论文。

官方议程：[PPoPP 2024 Main Conference Papers](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Tetris: Accelerating Sparse Convolution by Exploiting Memory Reuse on GPU](tetris_accelerating_sparse_convolution_by_exploiting_memory_reuse_on_gpu.md) | Xiaoyan Liu 等 5 人 | GPU 稀疏卷积：输入复用 + SPF 打包 + bank 感知重排，优于稠密/稀疏库 |
| 2 | [Shared Memory-contention-aware Concurrent DNN Execution for Diversely Heterogeneous System-on-Chips](shared_memory_contention_aware_concurrent_dnn_execution_for_diversely_heterogeneous_system_on_chips.md) | Ismet Dagli 等 2 人 | 按层映射异构加速器，内存竞争降 45%、延迟降 32%、吞吐升 29% |
| 3 | [Training one DeePMD Model in Minutes: a Step towards Online Learning](training_one_deepmd_model_in_minutes_a_step_towards_online_learning.md) | Siyu Hu 等 9 人 | 小批量拟牛顿优化器，8 数据集平均 32.2×，DeePMD 训练降至分钟级 |

---

[← Session 5: Synchronization and Concurrency Control II](../Session-5/index.md) · [PPoPP 2024 总览](../index.md) · [Session 7: Parallel Algorithms →](../Session-7/index.md)
