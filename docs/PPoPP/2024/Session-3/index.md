---
title: "Session 3: High Performance Computing"
description: "PPoPP 2024 Session 3（High Performance Computing），2024 年 3 月 4 日 14:20–15:40，Moorfoot，共 4 篇论文。"
tags:
  - "PPoPP2024"
  - "Session-3"
  - "High Performance Computing"
---

# Session 3: High Performance Computing

**PPoPP 2024 · 2024 年 3 月 4 日 14:20–15:40 · Moorfoot · Session Chair：Helen Xu**

涵盖高性能计算：拜占庭容错分析系统、共享内存多核上的非结构网格计算、异构众核上的极端规模湍流直接数值模拟，以及节点内共享内存消息传递。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2024 Main Conference Papers](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [OsirisBFT: Say No to Task Replication for Scalable Byzantine Fault Tolerant Analytics](osirisbft_say_no_to_task_replication_for_scalable_byzantine_fault_tolerant_analytics.md) | Kasra Jamshidi 等 2 人 | 以验证替代任务复制，容错规模与预期故障数解耦，吞吐与可扩展性更优 |
| 2 | [Towards Scalable Unstructured Mesh Computations on Shared Memory Many-Cores](towards_scalable_unstructured_mesh_computations_on_shared_memory_many_cores.md) | Haozhong Qiu 等 11 人 | 递归划分网格构建任务依赖树，工业 CFD 上最高 8.1× 提速 |
| 3 | [Extreme-scale Direct Numerical Simulation of Incompressible Turbulence on the Heterogeneous Many-core System](extreme_scale_direct_numerical_simulation_of_incompressible_turbulence_on_the_heterogeneous_many_core_system.md) | Jiabin Xie 等 6 人 | 天河异构 DNS 求解器：10.6× 加速、258 亿网格线性强扩展 |
| 4 | [Pure: Evolving Message Passing To Better Leverage Shared Memory Within Nodes](pure_evolving_message_passing_to_better_leverage_shared_memory_within_nodes.md) | James Psota 等 2 人 | 等待消息时窃取工作+节点内无锁消息，CoMD/miniAMR 最高 2.1× |

---

[← Session 2: Compilers and Runtimes for Parallel Systems](../Session-2/index.md) · [PPoPP 2024 总览](../index.md) · [Session 4: Graph Processing →](../Session-4/index.md)
