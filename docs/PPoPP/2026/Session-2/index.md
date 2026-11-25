---
title: "Session 2: Scheduling and Load Balancing"
description: "PPoPP 2026 Session 2（Scheduling and Load Balancing），2026 年 2 月 2 日 11:30–12:50，Pyrmont，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-2"
  - "Scheduling and Load Balancing"
---

# Session 2: Scheduling and Load Balancing

**PPoPP 2026 · 2026 年 2 月 2 日 11:30–12:50 · Pyrmont · Session Chair：V Krishna Nandivada**

关注调度与负载均衡：超订条件下的用户态线程调度、减少无效窃取的工作窃取、GPU 上的并行 DFS，以及多核 SpMV 的运行时自适应均衡。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [🏆 Rethinking Thread Scheduling under Oversubscription: A User-Space Framework for Coordinating Multi-runtime and Multi-process Workloads](rethinking_thread_scheduling_under_oversubscription_a_user_space_framework_for_coordinating_multi_runtime_and_multi_process_workloads.md) | Aleix Roca 等 2 人 | 用户态调度框架 + 协作策略，超订场景最高加速 2.4× |
| 2 | [Waste-Efficient Work Stealing](waste_efficient_work_stealing.md) | Kyle Singer 等 3 人 | 自适应调整活跃线程数，保持渐近时间并给出浪费上界 |
| 3 | [DiggerBees: Depth First Search Leveraging Hierarchical Block-Level Stealing on GPUs](diggerbees_depth_first_search_leveraging_hierarchical_block_level_stealing_on_gpus.md) | Yuyao Niu 等 4 人 | 两级栈 + 块内/块间窃取，较 GPU DFS 平均最高 30.18× |
| 4 | [PANA: A Fine-Grained Runtime-Adaptive Load Balancing for Parallel SpMV on Multicore CPUs](pana_a_fine_grained_runtime_adaptive_load_balancing_for_parallel_spmv_on_multicore_cpus.md) | Haodong Bian 等 5 人 | 微操作级细粒度自适应均衡，几何平均 1.36×–7.72× |

### 获奖

- **Rethinking Thread Scheduling under Oversubscription: A User-Space Framework for Coordinating Multi-runtime and Multi-process Workloads** —— Best Paper Nominee

---

[← Session 1: Concurrency Control](../Session-1/index.md) · [PPoPP 2026 总览](../index.md) · [Session 3: Concurrent Data Structures →](../Session-3/index.md)
