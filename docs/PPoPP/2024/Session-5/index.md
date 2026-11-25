---
title: "Session 5: Synchronization and Concurrency Control II"
description: "PPoPP 2024 Session 5（Synchronization and Concurrency Control II），2024 年 3 月 5 日 10:00–11:00，Moorfoot，共 3 篇论文。"
tags:
  - "PPoPP2024"
  - "Session-5"
  - "Synchronization and Concurrency Control II"
---

# Session 5: Synchronization and Concurrency Control II

**PPoPP 2024 · 2024 年 3 月 5 日 10:00–11:00 · Moorfoot · Session Chair：Erez Petrank**

继续并发数据结构与同步：有界并发队列的内存界、并发版本化指针，以及实用的硬件事务 vEB 树。

本 Session 共收录 **3** 篇论文。

官方议程：[PPoPP 2024 Main Conference Papers](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Memory Bounds for Concurrent Bounded Queues](memory_bounds_for_concurrent_bounded_queues.md) | Vitaly Aksenov 等 4 人 | 证明非阻塞有界队列的内存最优性需线性于并发进程数的开销 |
| 2 | [VERLIB: Concurrent Versioned Pointers](verlib_concurrent_versioned_pointers.md) | Guy E. Blelloch 等 2 人 | 版本化指针库 verlib：快照近零开销，支持无锁锁，B 树/ART/哈希可用 |
| 3 | [Practical Hardware Transactional vEB Trees](practical_hardware_transactional_veb_trees.md) | Mohammad Khalaji 等 4 人 | HTM 并发 vEB 树首次实现递归摘要，偏斜负载较并发映射平均 5× |

---

[← Session 4: Graph Processing](../Session-4/index.md) · [PPoPP 2024 总览](../index.md) · [Session 6: ML Workloads →](../Session-6/index.md)
