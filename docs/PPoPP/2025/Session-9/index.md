---
title: "Session 9: Concurrent Data Structures and Synchronization II"
description: "PPoPP 2025 Session 9（Concurrent Data Structures and Synchronization II），2025 年 3 月 4 日 15:40–17:00，Acacia D，共 4 篇论文。"
tags:
  - "PPoPP2025"
  - "Session-9"
  - "Concurrent Data Structures and Synchronization II"
---

# Session 9: Concurrent Data Structures and Synchronization II

**PPoPP 2025 · 2025 年 3 月 4 日 15:40–17:00 · Acacia D · Session Chair：Pengfei Su**

涵盖并发数据结构与系统软件：图 ANNS 的构建与搜索、松弛 FIFO 队列、基于光线追踪的空间索引，以及并行 EVM 上的智能合约编程模型。

本 Session 共收录 **4** 篇论文。

**官方议程：** [PPoPP 2025 Main Conference](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [PANNS: Enhancing Graph-based Approximate Nearest Neighbor Search through Recency-aware Construction and Parameterized Search](panns_enhancing_graph_based_approximate_nearest_neighbor_search_through_recency_aware_construction_and_parameterized_search.md) | Xizhe Yin 等 4 人 | 时序感知建图 + 参数化 beam search，吞吐最高 3.7× |
| 2 | [Balanced Allocations over Efficient Queues: A Fast Relaxed FIFO Queue](balanced_allocations_over_efficient_queues_a_fast_relaxed_fifo_queue.md) | Kåre von Geijer 等 4 人 | 按操作计数做 d-choice 均衡，吞吐 4× 且误差降至千分之一 |
| 3 | [LibRTS: A Spatial Indexing Library by Ray Tracing](librts_a_spatial_indexing_library_by_ray_tracing.md) | Liang Geng 等 3 人 | 把空间查询映射为 RT 问题，点查询最高 85.1× |
| 4 | [Crystality: A Programming Model for Smart Contracts on Parallel EVMs](crystality_a_programming_model_for_smart_contracts_on_parallel_evms.md) | Hao Wang 等 3 人 | 可编程合约作用域 + 异步中继，在 64 核上优于 Ethereum/Aptos/Sui |

---

[← Session 8: Tensor Cores](../Session-8/index.md) · [PPoPP 2025 总览](../index.md) · [Session 10: GPU II →](../Session-10/index.md)
