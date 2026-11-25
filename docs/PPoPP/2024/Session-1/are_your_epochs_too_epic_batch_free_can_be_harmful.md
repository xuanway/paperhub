---
title: "Are Your Epochs Too Epic? Batch Free Can Be Harmful"
description: "PPoPP 2024 Session Synchronization and Concurrency Control I：EBR 批量释放绕过分配器线程缓存致退化，摊销修复使 9/10 算法提速"
tags:
  - "PPoPP2024"
  - "Session-1"
  - "Synchronization and Concurrency Control I"
  - "safe memory reclamation"
  - "memory allocator"
  - "concurrent data structures"
authors:
  - "Daewoo Kim"
  - "Trevor Brown"
  - "Ajay Singh"
session: "Session 1: Synchronization and Concurrency Control I"
session_number: 1
session_chair: "Michael Scott"
date: "2024-03-04"
time: "10:40–11:00"
room: "Moorfoot"
doi: "10.1145/3627535.3638491"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Are Your Epochs Too Epic? Batch Free Can Be Harmful

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">揭示 EBR 性能退化根因：大批量释放绕过分配器的有界线程缓存，提出将释放开销在时间上摊销的修复，应用于十种回收算法后九种提速，令牌传递变体比已知最快算法快 1.5–2.6×。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 1: Synchronization and Concurrency Control I</p>
</div>

**作者**：Daewoo Kim, Trevor Brown, Ajay Singh (University of Waterloo)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 10:40–11:00 · Session 1: Synchronization and Concurrency Control I（主席：Michael Scott）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638491) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Epoch based memory reclamation (EBR) is one of the most popular techniques for reclaiming memory in lock-free and optimistic locking data structures, due to its ease of use and good performance in practice. However, EBR is known to be sensitive to thread delays, which can result in performance degradation. Moreover, the exact mechanism for this performance degradation is not well understood. This paper illustrates this performance degradation in a popular data structure benchmark, and does a deep dive to uncover its root cause—a subtle interaction between EBR and state of the art memory allocators. In essence, modern allocators attempt to reduce the overhead of freeing by maintaining bounded thread caches of objects for local reuse, actually freeing them (a very high latency operation) only when thread caches become too large. EBR immediately bypasses these mechanisms whenever a particularly large batch of objects is freed, substantially increasing overheads and latencies. Beyond EBR, many memory reclamation algorithms, and data structures, that reclaim objects in large batches suffer similar deleterious interactions with popular allocators. We propose a simple algorithmic fix for such algorithms to amortize the freeing of large object batches over time, and apply this technique to ten existing memory reclamation algorithms, observing performance improvements for nine out of ten, and over 50% improvement for six out of ten in experiments on a high performance lock-free ABtree. We also present an extremely simple token passing variant of EBR and show that, with our fix, it performs 1.5-2.6× faster than the fastest known memory reclamation algorithm, and 1.2-1.5× faster than not reclaiming at all, on a 192 thread four socket Intel system..

## 中文摘要

基于 epoch 的内存回收（EBR）是无锁与乐观锁数据结构中最流行的内存回收技术之一，因为它易于使用且在实践中性能良好。然而，EBR 已知对线程延迟敏感，这可能导致性能退化。此外，这种性能退化的确切机制尚未被很好地理解。本文在一个流行的数据结构基准中展示了这种性能退化，并深入探究以揭示其根本原因——EBR 与最先进内存分配器之间微妙的交互。本质上，现代分配器试图通过维护有界的对象线程缓存以供本地复用来降低释放开销，只有当线程缓存变得过大时才真正释放对象（一项延迟非常高的操作）。而 EBR 每当释放特别大的批量对象时就会立即绕过这些机制，从而大幅增加开销与延迟。除 EBR 之外，许多以大批量方式回收对象的内存回收算法与数据结构也会与流行分配器产生类似的有害交互。我们针对这类算法提出了一种简单的算法修复，将大批量对象的释放开销在时间上摊销，并将该技术应用于十种现有内存回收算法；在高性能无锁 ABtree 上的实验中，我们观察到十种算法中有九种性能提升，其中六种提升超过 50%。我们还给出了一种极其简单的 EBR 令牌传递变体，并表明在 192 线程四路 Intel 系统上，配合我们的修复后，它比已知最快的内存回收算法快 1.5–2.6×，比完全不进行回收还快 1.2–1.5×。

## 英文关键词

safe memory reclamation, memory allocator, concurrent data structures, memory management

## 中文关键词

安全内存回收；内存分配器；并发数据结构；内存管理

---

## 一句话总结

> 揭示 EBR 性能退化根因：大批量释放绕过分配器的有界线程缓存，提出将释放开销在时间上摊销的修复，应用于十种回收算法后九种提速，令牌传递变体比已知最快算法快 1.5–2.6×。

## 研究问题

EBR 对线程延迟敏感、会导致性能退化，但其确切机制此前未被很好理解；现代分配器的有界线程缓存与大批量立即释放之间存在此前未被认识的有害交互。

## 方法简述

- 在流行的数据结构基准上复现 EBR 的性能退化，并深入分析其根因：EBR 与最先进内存分配器之间的微妙交互
- 揭示失效机理：现代分配器依靠有界线程缓存做本地复用、仅在缓存过大时才真正释放，而 EBR 在释放特别大的对象批量时会立即绕过这些机制
- 提出一种简单的算法修复，把大批量对象的释放开销在时间上摊销，并将其应用于十种现有内存回收算法
- 提出一种极其简单的 EBR 令牌传递（token passing）变体

## 主要结果

- 在高性能无锁 ABtree 上，十种回收算法中九种性能提升，其中六种提升超过 50%
- 带该修复的令牌传递 EBR 变体比已知最快的内存回收算法快 1.5–2.6×，比完全不回收还快 1.2–1.5×（192 线程四路 Intel 系统）
- 表明该问题不限于 EBR，许多以大批量回收对象的内存回收算法与数据结构都会与流行分配器产生类似的有害交互

---

> 所属 Session：[Session 1: Synchronization and Concurrency Control I](index.md) · 返回 [PPoPP 2024 总览](../index.md)
