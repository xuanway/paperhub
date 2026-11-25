---
title: "Session 3: Concurrent Data Structures and Synchronization I"
description: "PPoPP 2025 Session 3（Concurrent Data Structures and Synchronization I），2025 年 3 月 3 日 14:00–15:20，Acacia D，共 4 篇论文。"
tags:
  - "PPoPP2025"
  - "Session-3"
  - "Concurrent Data Structures and Synchronization I"
---

# Session 3: Concurrent Data Structures and Synchronization I

**PPoPP 2025 · 2025 年 3 月 3 日 14:00–15:20 · Acacia D · Session Chair：Yuanhao Wei**

围绕并发数据结构与同步原语：互斥锁、fetch-and-add 聚合、读写锁公平性，以及并发数据结构的安全内存回收。

本 Session 共收录 **4** 篇论文。

**官方议程：** [PPoPP 2025 Main Conference](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Reciprocating Locks](reciprocating_locks.md) | Dave Dice 等 2 人 | 常数时间入场/释放，单等待元素，竞争下一致性流量低于 MCS/CLH |
| 2 | [Aggregating Funnels for Faster Fetch&Add and Queues](aggregating_funnels_for_faster_fetch_and_add_and_queues.md) | Younghun Roh 等 6 人 | 批处理 + 多地址分散，消除单地址 fetch&add 热点 |
| 3 | [Fairer and More Scalable Reader-Writer Locks by Optimizing Queue Management](fairer_and_more_scalable_reader_writer_locks_by_optimizing_queue_management.md) | Takashi Hoshino 等 2 人 | Freezer 机制解耦公平策略与快速路径，吞吐最高 3.5× |
| 4 | [🏆 Publish on Ping: A Better Way to Publish Reservations in Memory Reclamation for Concurrent Data Structures](publish_on_ping_a_better_way_to_publish_reservations_in_memory_reclamation_for_concurrent_data_structures.md) | Ajay Singh 等 2 人 | 按需发布预约替代全局可见预约，hazard pointer 上提速 1.2×–4× |

### 获奖

- **Publish on Ping: A Better Way to Publish Reservations in Memory Reclamation for Concurrent Data Structures** —— Distinguished Paper Award

---

[← Session 2: GPU I](../Session-2/index.md) · [PPoPP 2025 总览](../index.md) · [Session 4: Memory →](../Session-4/index.md)
