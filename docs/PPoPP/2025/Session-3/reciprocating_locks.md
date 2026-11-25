---
title: "Reciprocating Locks"
description: "PPoPP 2025 Session 3（Concurrent Data Structures and Synchronization I）：常数时间入场/释放，单等待元素，竞争下一致性流量低于 MCS/CLH"
tags:
  - "PPoPP2025"
  - "Session-3"
  - "Concurrent Data Structures and Synchronization I"
  - "Mutual Exclusion"
  - "Spin Locks"
  - "Cache-Coherent"
authors:
  - "Dave Dice"
  - "Alex Kogan"
session: "Session 3: Concurrent Data Structures and Synchronization I"
session_number: 3
session_chair: "Yuanhao Wei"
date: "2025-03-03"
time: "14:00–14:20"
room: "Acacia D"
doi: "10.1145/3710848.3710862"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Reciprocating Locks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向缓存一致性共享内存的互斥锁 Reciprocating Locks：入场与释放均为常数时间，等待线程本地自旋，且每个线程无论持锁多少都只需一个等待元素。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 3: Concurrent Data Structures and Synchronization I</p>
</div>

**作者**：Dave Dice, Alex Kogan (Oracle Labs)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 14:00–14:20 · Session 3: Concurrent Data Structures and Synchronization I（主席：Yuanhao Wei）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710862) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出面向缓存一致性共享内存的互斥锁 Reciprocating Locks：入场与释放均为常数时间，等待线程本地自旋，且每个线程无论持锁多少都只需一个等待元素。

## 研究问题

可扩展自旋锁需要在竞争下同时做到高吞吐、低延迟、低一致性流量和强抗饥饿性，并且要能直接用于 pthreads、C++ 等通用编程环境。

## 方法简述

- 入场阶段与 Release 操作均以常数时间完成。
- 等待线程采用本地自旋；每个线程只需一个等待元素，不随其持有锁的数量增长。
- 不提供严格 FIFO 入场，但限制插队（bypass）并具备强抗饥饿性质。

## 主要结果

- 竞争下吞吐高，无竞争时延迟低。
- 持续竞争时产生的一致性流量少于 MCS 与 CLH。
- 性能与最好的可扩展队列自旋锁相当，且常常更优。

<details>
<summary>原文摘要（英文）</summary>

We present Reciprocating Locks, a novel mutual exclusion locking algorithm, targeting cache-coherent shared memory (CC), that enjoys a number of desirable properties. The doorway arrival phase and the Release operation both run in constant-time. Waiting threads use local spinning and only a single waiting element is required per thread, regardless of the number of locks a thread might hold at a given time. While our lock does not provide strict FIFO admission, it bounds bypass and has strong anti-starvation properties. The lock is compact, space efficient, and has been intentionally designed to be readily usable in real-world general purpose computing environments such as pthreads, or C++. We show the lock exhibits high throughput under contention and low latency in the uncontended case. Under sustained contention, Reciprocating Locks generate less coherence traffic than MCS and CLH. The performance of Reciprocating Locks is competitive with and often better than the best state-of-the-art scalable queue-based spin locks.

</details>

---

> 所属 Session：[Session 3: Concurrent Data Structures and Synchronization I](index.md) · 返回 [PPoPP 2025 总览](../index.md)
