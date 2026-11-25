---
title: "Session 2: Compilers and Runtimes for Parallel Systems"
description: "PPoPP 2024 Session 2（Compilers and Runtimes for Parallel Systems），2024 年 3 月 4 日 11:30–12:50，Moorfoot，共 4 篇论文。"
tags:
  - "PPoPP2024"
  - "Session-2"
  - "Compilers and Runtimes for Parallel Systems"
---

# Session 2: Compilers and Runtimes for Parallel Systems

**PPoPP 2024 · 2024 年 3 月 4 日 11:30–12:50 · Moorfoot · Session Chair：Mohamed Riyadh Baghdadi**

关注编译与运行时系统：分布式大模型推理的算子内外并行交织、仿射程序的混合精度自动生成与调优、Future 死锁的静态检测，以及下标递推的自动并行化。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2024 Main Conference Papers](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Liger: Interleaving Intra- and Inter-Operator Parallelism for Distributed Large Model Inference](liger_interleaving_intra_and_inter_operator_parallelism_for_distributed_large_model_inference.md) | Jiangsu Du 等 7 人 | 跨请求交错计算与通信，4 卡延迟降 36.0%、吞吐升 1.34× |
| 2 | [A Holistic Approach to Automatic Mixed-Precision Code Generation and Tuning for Affine Programs](a_holistic_approach_to_automatic_mixed_precision_code_generation_and_tuning_for_affine_programs.md) | Jinchen Xu 等 6 人 | 统一参数耦合混合精度代码生成与调优，CPU 上比 LuIs 快 3.28× |
| 3 | [Language-Agnostic Static Deadlock Detection for Futures](language_agnostic_static_deadlock_detection_for_futures.md) | Stefan K Muller | 基于图类型的可靠类型系统，实现语言无关的 futures 死锁检测 |
| 4 | [Recurrence Analysis for Automatic Parallelization of Subscripted Subscripts](recurrence_analysis_for_automatic_parallelization_of_subscripted_subscripts.md) | Akshay Bhosale 等 2 人 | 递归分析判定 a[b[i]] 不规则/多维单调性，10/12 基准提速 |

---

[← Session 1: Synchronization and Concurrency Control I](../Session-1/index.md) · [PPoPP 2024 总览](../index.md) · [Session 3: High Performance Computing →](../Session-3/index.md)
