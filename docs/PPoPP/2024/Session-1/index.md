---
title: "Session 1: Synchronization and Concurrency Control I"
description: "PPoPP 2024 Session 1（Synchronization and Concurrency Control I），2024 年 3 月 4 日 10:00–11:00，Moorfoot，共 3 篇论文。"
tags:
  - "PPoPP2024"
  - "Session-1"
  - "Synchronization and Concurrency Control I"
---

# Session 1: Synchronization and Concurrency Control I

**PPoPP 2024 · 2024 年 3 月 4 日 10:00–11:00 · Moorfoot · Session Chair：Michael Scott**

聚焦并发控制与同步：基于慢时钟的事务内存、按资源公平调度锁占用，以及 epoch 批量回收的开销分析。

本 Session 共收录 **3** 篇论文。

官方议程：[PPoPP 2024 Main Conference Papers](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Scaling Up Transactions with Slower Clocks](scaling_up_transactions_with_slower_clocks.md) | Pedro Ramalhete 等 2 人 | DCTL/DCOTL 让不相交事务不递增中央时钟，高核数下可扩展 |
| 2 | [Locks as a Resource: Fairly Scheduling Lock Occupation with CFL](locks_as_a_resource_fairly_scheduling_lock_occupation_with_cfl.md) | Jonggyu Park 等 2 人 | CFL 把锁占用当作可调度资源，按优先级与 cgroup 公平分配 |
| 3 | [Are Your Epochs Too Epic? Batch Free Can Be Harmful](are_your_epochs_too_epic_batch_free_can_be_harmful.md) | Daewoo Kim 等 3 人 | EBR 批量释放绕过分配器线程缓存致退化，摊销修复使 9/10 算法提速 |

---

[PPoPP 2024 总览](../index.md) · [Session 2: Compilers and Runtimes for Parallel Systems →](../Session-2/index.md)
