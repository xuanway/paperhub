---
title: "Fairer and More Scalable Reader-Writer Locks by Optimizing Queue Management"
description: "PPoPP 2025 Session 3（Concurrent Data Structures and Synchronization I）：Freezer 机制解耦公平策略与快速路径，吞吐最高 3.5×"
tags:
  - "PPoPP2025"
  - "Session-3"
  - "Concurrent Data Structures and Synchronization I"
  - "Reader-Writer Locks"
  - "MCS Lock"
  - "Fairness"
authors:
  - "Takashi Hoshino"
  - "Kenjiro Taura"
session: "Session 3: Concurrent Data Structures and Synchronization I"
session_number: 3
session_chair: "Yuanhao Wei"
date: "2025-03-03"
time: "14:40–15:00"
room: "Acacia D"
doi: "10.1145/3710848.3710877"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Fairer and More Scalable Reader-Writer Locks by Optimizing Queue Management

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Freezer 机制及四种队列式读写锁优化，在避免使用堆内存的前提下降低 mutex 访问竞争，并使公平策略与快速路径可以独立选择。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 3: Concurrent Data Structures and Synchronization I</p>
</div>

**作者**：Takashi Hoshino (Cybozu Labs, Inc.); Kenjiro Taura (The University of Tokyo)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 14:40–15:00 · Session 3: Concurrent Data Structures and Synchronization I（主席：Yuanhao Wei）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710877) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 Freezer 机制及四种队列式读写锁优化，在避免使用堆内存的前提下降低 mutex 访问竞争，并使公平策略与快速路径可以独立选择。

## 研究问题

MCS 锁及其两阶段变体虽提升了多核可扩展性，但仍存在 mutex 访问竞争；在存在快速路径时，公平性也受到限制。

## 方法简述

- Freezer 机制扩展 MCS 锁的链表操作，在不使用堆内存的情况下减少 mutex 访问。
- 将公平策略与快速路径的选择解耦，使二者可独立配置。
- 针对队列式读写锁提出四种优化方法。

## 主要结果

- 三个基准测试验证了所提公平读写锁的有效性。
- 相比基线吞吐最高提升 3.5×，尾延迟最高改善 2.7×。

<details>
<summary>原文摘要（英文）</summary>

MCS lock and its variants provide scalability on many-core architectures, using lists of lock requests to reduce access contention on the mutex data. Most recent variants have adopted a two-stage design, allowing requests to be allocated from stack memory rather than heap. However, this design still produces mutex access contention and limits fairness in the presence of fast paths. This paper proposes the Freezer mechanism and its optimization methods, which extend the list structure operations of MCS lock, to reduce mutex access without using heap memory and enable an independent choice of fairness policies and fast paths. Additionally, we propose four optimization methods for queue-based reader-writer locks. Our evaluation using three benchmarks demonstrated the effectiveness of the proposed fair reader-writer locks. They achieved up to 3.5× higher throughput and improved tail latency by up to 2.7× compared to the baselines.

</details>

---

> 所属 Session：[Session 3: Concurrent Data Structures and Synchronization I](index.md) · 返回 [PPoPP 2025 总览](../index.md)
