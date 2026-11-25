---
title: "Practical Hardware Transactional vEB Trees"
description: "PPoPP 2024 Session Synchronization and Concurrency Control II：HTM 并发 vEB 树首次实现递归摘要，偏斜负载较并发映射平均 5×"
tags:
  - "PPoPP2024"
  - "Session-5"
  - "Synchronization and Concurrency Control II"
  - "Concurrent Data Structures"
  - "van Emde Boas Trees"
  - "Transactional Memory"
authors:
  - "Mohammad Khalaji"
  - "Trevor Brown"
  - "Khuzaima Daudjee"
  - "Vitaly Aksenov"
session: "Session 5: Synchronization and Concurrency Control II"
session_number: 5
session_chair: "Erez Petrank"
date: "2024-03-05"
time: "10:40–11:00"
room: "Moorfoot"
doi: "10.1145/3627535.3638504"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Practical Hardware Transactional vEB Trees

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该文用硬件事务内存实现并发 vEB 树集合与映射，首次实现递归摘要，无竞争下保持双对数操作，中等偏斜负载上平均快于先进并发映射 5 倍。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 5: Synchronization and Concurrency Control II</p>
</div>

**作者**：Mohammad Khalaji, Trevor Brown, Khuzaima Daudjee (University of Waterloo); Vitaly Aksenov (City, University of London)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 10:40–11:00 · Session 5: Synchronization and Concurrency Control II（主席：Erez Petrank）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638504) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

van Emde Boas (vEB) trees are sequential data structures optimized for extremely fast predecessor and successor queries. Such queries are an important incentive to use ordered sets or maps such as vEB trees. All operations in a vEB tree are doubly logarithmic in the universe size. Attempts to implement concurrent vEB trees have either simplified their structure in a way that eliminated their ability to perform fast predecessor and successor queries, or have otherwise compromised on doubly logarithmic complexity. In this work, we leverage Hardware Transactional Memory (HTM) to implement vEB tree-based sets and maps in which operations are doubly logarithmic in the absence of contention. Our proposed concurrent vEB tree is the first to implement recursive summaries, the key algorithmic component of fast predecessor and successor operations. Through extensive experiments, we demonstrate that our algorithm outperforms state-of-the-art concurrent maps by an average of 5× in a moderately skewed workload, and the single-threaded C++ standard ordered map and its unordered map by 70% and 14%, respectively. And, it does so while using two orders of magnitude less memory than traditional vEB trees.

## 中文摘要

van Emde Boas（vEB）树是为极快的前驱与后继查询而优化的顺序数据结构。此类查询是使用 vEB 树等有序集合或映射的重要动机。vEB 树中的所有操作都是关于全域大小的双对数复杂度。已有的并发 vEB 树实现要么以某种方式简化了其结构，从而消除了执行快速前驱与后继查询的能力，要么在双对数复杂度上做出了妥协。在本工作中，我们利用硬件事务内存（HTM）实现基于 vEB 树的集合与映射，在无竞争情况下其操作具有双对数复杂度。我们提出的并发 vEB 树是首个实现递归摘要（recursive summaries）的实现，而递归摘要是快速前驱与后继操作的关键算法组件。通过大量实验，我们证明该算法在中等偏斜的工作负载下平均比最先进的并发映射快 5 倍，相比单线程 C++ 标准有序映射及其无序映射分别快 70% 和 14%。同时，它使用的内存比传统 vEB 树少两个数量级。

## 英文关键词

Concurrent Data Structures, vEB Trees, van Emde Boas Trees, Transactional Memory, Lock Elision

## 中文关键词

并发数据结构；vEB 树；van Emde Boas 树；事务内存；锁消除

---

## 一句话总结

> 该文用硬件事务内存实现并发 vEB 树集合与映射，首次实现递归摘要，无竞争下保持双对数操作，中等偏斜负载上平均快于先进并发映射 5 倍。

## 研究问题

已有的并发 vEB 树实现要么简化结构以致丧失快速前驱/后继查询能力，要么在双对数复杂度上做出妥协，无法兼顾两者。

## 方法简述

- 采用硬件事务内存（HTM）实现基于 vEB 树的集合与映射，使无竞争情形下各操作保持关于全域大小的双对数复杂度。
- 首次在并发 vEB 树中实现递归摘要（recursive summaries），保留快速前驱与后继操作的关键算法组件。
- 以事务化执行替代显式加锁（锁消除），在保留顺序 vEB 树结构的前提下获得并发性。

## 主要结果

- 在中等偏斜的工作负载上平均比最先进的并发映射快 5 倍。
- 相比单线程 C++ 标准有序映射与无序映射分别快 70% 和 14%。
- 内存占用比传统 vEB 树低两个数量级。

---

> 所属 Session：[Session 5: Synchronization and Concurrency Control II](index.md) · 返回 [PPoPP 2024 总览](../index.md)
