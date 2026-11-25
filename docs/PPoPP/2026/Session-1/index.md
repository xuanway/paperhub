---
title: "Session 1: Concurrency Control"
description: "PPoPP 2026 Session 1（Concurrency Control），2026 年 2 月 2 日 09:50–11:10，Pyrmont，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-1"
  - "Concurrency Control"
---

# Session 1: Concurrency Control

**PPoPP 2026 · 2026 年 2 月 2 日 09:50–11:10 · Pyrmont · Session Chair：Madan Musuvathi**

聚焦并发控制与同步：二进制兼容的临界区代理、可扩展互斥锁、面向内存回收的非阻塞结构改造，以及动态多版本事务内存。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [🏆 Binary Compatible Critical Section Delegation](binary_compatible_critical_section_delegation.md) | Junyao Zhang 等 3 人 | 内核代理 + 二进制兼容，现有程序无需改代码即可降低临界区竞争 |
| 2 | [Hapax Locks: Scalable Value-Based Mutual Exclusion](hapax_locks_scalable_value_based_mutual_exclusion.md) | Dave Dice 等 2 人 | 常数时间入场/解锁与 FIFO 顺序，性能对标最好的 SOTA 锁 |
| 3 | [Fixing Non-blocking Data Structures for Better Compatibility with Memory Reclamation Schemes](fixing_non_blocking_data_structures_for_better_compatibility_with_memory_reclamation_schemes.md) | Md Amit Hasan Arovi 等 2 人 | 让 Harris 链表等乐观遍历结构兼容 HP/HE/IBR/Hyaline |
| 4 | [Multiverse: Transactional Memory with Dynamic Multiversioning](multiverse_transactional_memory_with_dynamic_multiversioning.md) | Gaetano Coccimiglio 等 3 人 | 有版本/无版本事务并发，长读负载吞吐高几个数量级 |

### 获奖

- **Binary Compatible Critical Section Delegation** —— Best Paper Award

---

[PPoPP 2026 总览](../index.md) · [Session 2: Scheduling and Load Balancing →](../Session-2/index.md)
