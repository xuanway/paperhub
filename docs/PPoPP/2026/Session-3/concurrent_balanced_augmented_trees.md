---
title: "Concurrent Balanced Augmented Trees"
description: "PPoPP 2026 Session 3（Concurrent Data Structures）：首个通用增强无锁平衡树，更新快 2.2–30×"
tags:
  - "PPoPP2026"
  - "Session-3"
  - "Concurrent Data Structures"
  - "Lock-Free Data Structures"
  - "Augmented Search Trees"
  - "Memory Reclamation"
authors:
  - "Evan Wrench"
  - "Ajay Singh"
  - "Younghun Roh"
  - "Panagiota Fatourou"
  - "Siddhartha Jayanti"
  - "Eric Ruppert"
  - "Yuanhao Wei"
session: "Session 3: Concurrent Data Structures"
session_number: 3
session_chair: "Calin Cascaval"
date: "2026-02-02"
time: "14:50–15:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786437"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Concurrent Balanced Augmented Trees

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出首个支持通用增强函数的无锁增强平衡搜索树，并给出基于委托的优化版本，多数负载下性能提升 2 倍以上，更新速度远超增强非平衡树。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 3: Concurrent Data Structures</p>
</div>

**作者**：Evan Wrench, Ajay Singh, Younghun Roh, Panagiota Fatourou, Siddhartha Jayanti, Eric Ruppert, and Yuanhao Wei — University of British Columbia, Canada; ICS-FORTH, Greece; Massachusetts Institute of Technology, USA; University of Crete, Greece; Dartmouth College, USA; York University, Canada

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 14:50–15:10 · Session 3: Concurrent Data Structures（主席：Calin Cascaval）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786437) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Augmentation makes search trees tremendously more versatile, allowing them to support efficient aggregation queries, order-statistic queries, and range queries in addition to insertion, deletion, and lookup. In this paper, we present the first lock-free augmented balanced search tree supporting generic augmentation functions. Our algorithmic ideas build upon a recent augmented unbalanced search tree presented by Fatourou and Ruppert [DISC, 2024]. We implement both data structures, solving some memory reclamation challenges in the process, and provide an experimental performance analysis of them. We also present optimized versions of our balanced tree that use delegation to achieve better scalability and performance (by more than 2x in most workloads). Our experiments show that our augmented balanced tree completes updates 2.2 to 30 times faster than the unbalanced augmented tree, and outperforms unaugmented trees by up to several orders of magnitude on 120 threads.

## 中文摘要

增强（augmentation）使搜索树的功能极大地扩展，使其除插入、删除与查找之外，还能支持高效的聚合查询、顺序统计查询与范围查询。本文提出首个支持通用增强函数的无锁增强平衡搜索树。我们的算法思想建立在 Fatourou 与 Ruppert 近期提出的增强非平衡搜索树 [DISC, 2024] 之上。我们实现了这两种数据结构，并在过程中解决了若干内存回收方面的挑战，还对它们进行了实验性能分析。我们还给出了平衡树的优化版本，利用委派（delegation）获得更好的可扩展性与性能（在多数工作负载上提升超过 2 倍）。实验表明，我们的增强平衡树完成更新的速度比增强非平衡树快 2.2 至 30 倍，并在 120 个线程上以最高若干数量级的优势优于未增强的树。

## 英文关键词

Lock-free, Balanced BST, Augmentation, Ordered Statistics Queries, Range Query, Delegation

## 中文关键词

无锁；平衡二叉搜索树（Balanced BST）；增强（augmentation）；顺序统计查询；范围查询；委派（delegation）

---

## 一句话总结

> 提出首个支持通用增强函数的无锁增强平衡搜索树，并给出基于委托的优化版本，多数负载下性能提升 2 倍以上，更新速度远超增强非平衡树。

## 研究问题

增强使搜索树能支持聚合、顺序统计与范围查询，但已有增强搜索树要么不平衡，要么不支持无锁并发，缺少兼具平衡、通用增强与无锁特性的结构。

## 方法简述

- 在 Fatourou 与 Ruppert（DISC 2024）的增强非平衡搜索树基础上，设计首个支持通用增强函数的无锁增强平衡搜索树。
- 实现平衡与非平衡两种数据结构，并在实现过程中解决内存回收方面的挑战。
- 设计采用委托（delegation）的优化版本，以提升可扩展性与性能。
- 对两种数据结构开展实验性能分析。

## 主要结果

- 基于委托的优化版本在多数负载下带来 2 倍以上性能提升。
- 增强平衡树完成更新的速度比增强非平衡树快 2.2 至 30 倍。
- 在 120 线程下，相比未增强的树快达数个数量级。

---

> 所属 Session：[Session 3: Concurrent Data Structures](index.md) · 返回 [PPoPP 2026 总览](../index.md)
