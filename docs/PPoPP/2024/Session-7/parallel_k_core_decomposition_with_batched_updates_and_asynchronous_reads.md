---
title: "Parallel k-Core Decomposition with Batched Updates and Asynchronous Reads"
description: "PPoPP 2024 Session Parallel Algorithms：异步读与更新批并发的 k-core 结构，读延迟降低达 4.05×10⁵ 倍"
tags:
  - "PPoPP2024"
  - "Session-7"
  - "Parallel Algorithms"
  - "k-core Decomposition"
  - "Concurrent Data Structures"
  - "Batch-Parallel"
authors:
  - "Quanquan C. Liu"
  - "Julian Shun"
  - "Igor Zablotchi"
session: "Session 7: Parallel Algorithms"
session_number: 7
session_chair: "Prashant Pandey"
date: "2024-03-05"
time: "14:40–15:00"
room: "Moorfoot"
doi: "10.1145/3627535.3638508"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Parallel k-Core Decomposition with Batched Updates and Asynchronous Reads

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出支持异步读与批量更新的混合并发-并行动态 k-core 数据结构，通过跟踪更新间因果依赖使相关更新对读者呈原子性，读延迟降低数个数量级。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 7: Parallel Algorithms</p>
</div>

**作者**：Quanquan C. Liu (Yale University); Julian Shun (Massachusetts Institute of Technology); Igor Zablotchi (Mysten Labs)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 14:40–15:00 · Session 7: Parallel Algorithms（主席：Prashant Pandey）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638508) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Maintaining a dynamic k-core decomposition is an important problem that identifies dense subgraphs in dynamically changing graphs. Recent work by Liu et al. [SPAA 2022] presents a parallel batch-dynamic algorithm for maintaining an approximate k-core decomposition. In their solution, both reads and updates need to be batched, and therefore each type of operation can incur high latency waiting for the other type to finish. To tackle most real-world workloads, which are dominated by reads, this paper presents a novel hybrid concurrent-parallel dynamic k-core data structure where asynchronous reads can proceed concurrently with batches of updates, leading to significantly lower read latencies. Our approach is based on tracking causal dependencies between updates, so that causally related groups of updates appear atomic to concurrent readers. Our data structure guarantees linearizability and liveness for both reads and updates, and maintains the same approximation guarantees as prior work. Our experimental evaluation on a 30-core machine shows that our approach reduces read latency by orders of magnitude compared to the batch-dynamic algorithm, up to a 4.05 · 10^5-factor. Compared to an unsynchronized (non-linearizable) baseline, our read latency overhead is only up to a 3.21-factor greater, while improving accuracy of coreness estimates by up to a factor of 52.7.

## 中文摘要

维护动态 k-core 分解是一个重要问题，它用于在动态变化的图中识别稠密子图。Liu 等人 [SPAA 2022] 的近期工作提出了一种用于维护近似 k-core 分解的并行批动态算法。在他们的解决方案中，读操作和更新都需要批处理，因此每一类操作都可能因等待另一类操作完成而产生高延迟。为了解决以读为主的大多数真实工作负载，本文提出了一种新颖的混合并发-并行动态 k-core 数据结构，其中异步读可以与更新批并发进行，从而显著降低读延迟。我们的方法基于跟踪更新之间的因果依赖，使得因果相关的一组更新对并发读者呈现原子性。我们的数据结构保证读与更新的线性一致性和活性，并保持与先前工作相同的近似保证。在 30 核机器上的实验评估表明，与批动态算法相比，我们的方法将读延迟降低了数个数量级，最高达 4.05·10^5 倍。与无同步（非线线性一致）基线相比，我们的读延迟开销最多只高出 3.21 倍，同时将 coreness 估计的精度最多提升 52.7 倍。

## 英文关键词

parallelism, concurrency, k-core decomposition

## 中文关键词

并行性；并发；k-core 分解

---

## 一句话总结

> 提出支持异步读与批量更新的混合并发-并行动态 k-core 数据结构，通过跟踪更新间因果依赖使相关更新对读者呈原子性，读延迟降低数个数量级。

## 研究问题

Liu 等人 [SPAA 2022] 的并行批动态算法要求读与更新都成批处理，任一类操作都要等待另一类完成，因而延迟很高；而真实负载大多以读为主。

## 方法简述

- 提出新型混合并发-并行动态 k-core 数据结构，允许异步读与更新批并发执行，以显著降低读延迟
- 基于跟踪更新之间的因果依赖，使因果相关的一组更新对并发读者呈现原子性
- 设计使读与更新同时具备线性一致性（linearizability）与活性（liveness）的机制
- 保持与先前工作相同的近似保证

## 主要结果

- 在 30 核机器上，相比批动态算法将读延迟降低数个数量级，最高达 4.05×10^5 倍
- 相比无同步（非线线性一致）基线，读延迟开销最多仅高出 3.21 倍
- 同时将 coreness 估计的精度最多提升 52.7 倍

---

> 所属 Session：[Session 7: Parallel Algorithms](index.md) · 返回 [PPoPP 2024 总览](../index.md)
