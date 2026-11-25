---
title: "VERLIB: Concurrent Versioned Pointers"
description: "PPoPP 2024 Session Synchronization and Concurrency Control II：版本化指针库 verlib：快照近零开销，支持无锁锁，B 树/ART/哈希可用"
tags:
  - "PPoPP2024"
  - "Session-5"
  - "Synchronization and Concurrency Control II"
  - "multiversioning"
  - "snapshots"
  - "concurrent data structures"
authors:
  - "Guy E. Blelloch"
  - "Yuanhao Wei"
session: "Session 5: Synchronization and Concurrency Control II"
session_number: 5
session_chair: "Erez Petrank"
date: "2024-03-05"
time: "10:20–10:40"
room: "Moorfoot"
doi: "10.1145/3627535.3638501"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# VERLIB: Concurrent Versioned Pointers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">verlib 以版本化指针支持常数时间快照，用 indirection-on-need 解除指针限制并以幂等 CAS 支持无锁锁，快照化结构性能接近原版。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 5: Synchronization and Concurrency Control II</p>
</div>

**作者**：Guy E. Blelloch, Yuanhao Wei (Carnegie Mellon University)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 10:20–10:40 · Session 5: Synchronization and Concurrency Control II（主席：Erez Petrank）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638501) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Recent work has shown how to augment any CAS-based concurrent data structure to support taking a snapshot of the current memory state. Taking the snapshot, as well as loads and CAS (Compare and Swap) operations, take constant time. Importantly, such snapshotting can be used to easily implement linearizable queries, such as range queries, over any part of a data structure. In this paper, we make two significant improvements over this approach. The first improvement removes a subtle and hard to reason about restriction that was needed to avoid a level of indirection on pointers. We introduce an approach, which we refer to as indirection-on-need, that removes the restriction, but yet almost always avoids indirection. The second improvement is to efficiently support snapshotting with lock-free locks. This requires supporting an idempotent CAS. We show a particularly simple solution to the problem that leverages the data structures used for snapshotting. Based on these ideas we implemented an easy-to-use C++ library, verlib, centered around a versioned pointer type. The library works with lock (standard or lock-free) and CAS based algorithms, or any combination. Converting existing concurrent data-structures to use the library takes minimal effort. We present results for experiments that use verlib to convert state-of-the-art data structures for ordered maps (a B-tree), radix-ordered maps (an ART-tree), and unordered maps (an optimized hash table) to be snapshottable. The snapshottable versions perform almost as well as the original versions and far outperform any previous implementations that support atomic range queries.

## 中文摘要

近期工作已表明，如何增强任何基于 CAS 的并发数据结构，使其支持对当前内存状态拍摄快照。拍摄快照以及 load 与 CAS（比较并交换）操作都只需常数时间。重要的是，这种快照机制可以很容易地实现可线性化的查询，例如对数据结构任意部分的范围查询。本文对该方法做出两项重要改进。第一项改进移除了一处微妙且难以推理的限制，该限制原本是为了避免指针上的一层间接寻址而必需的。我们引入一种称为 indirection-on-need 的方法，它移除了该限制，却几乎总能避免间接寻址。第二项改进是高效支持使用无锁锁（lock-free locks）的快照，这需要支持幂等 CAS。我们给出了该问题一个特别简单的解决方案，它复用了用于快照的数据结构。基于这些思想，我们实现了一个易于使用的 C++ 库 verlib，其核心是一个版本化指针类型。该库可与基于锁（标准锁或无锁锁）的算法、基于 CAS 的算法，或它们的任意组合配合使用。将现有的并发数据结构转换为使用该库只需极小的改动。我们展示了使用 verlib 将最先进的有序映射（B 树）、基数有序映射（ART 树）和无序映射（优化的哈希表）改造为可快照版本的实验结果。这些可快照版本的性能几乎与原版相当，并远超以往任何支持原子范围查询的实现。

## 英文关键词

multiversioning, concurrent data structures, snapshots, lock-based, lock-free

## 中文关键词

多版本化；并发数据结构；快照；基于锁；无锁

---

## 一句话总结

> verlib 以版本化指针支持常数时间快照，用 indirection-on-need 解除指针限制并以幂等 CAS 支持无锁锁，快照化结构性能接近原版。

## 研究问题

先前的快照增强方法带有一个微妙且难以推理的限制——为避免指针上的一层间接寻址而必须约束结构；同时它无法高效支持基于无锁锁（lock-free locks）的快照，因为那需要幂等 CAS。

## 方法简述

- 提出 indirection-on-need 方法，移除原有的指针间接限制，同时在绝大多数情况下避免真正的间接寻址。
- 借助快照所用的数据结构给出一套特别简单的幂等 CAS 方案，从而高效支持无锁锁下的快照。
- 实现易用的 C++ 库 verlib，以版本化指针类型为中心，兼容基于锁（标准锁或无锁锁）与基于 CAS 的算法及其任意组合。

## 主要结果

- 快照化的 B 树、ART 树与优化哈希表性能几乎与原版相当。
- 远超以往任何支持原子范围查询的实现。
- 把现有并发数据结构改造为使用该库只需极小改动。

---

> 所属 Session：[Session 5: Synchronization and Concurrency Control II](index.md) · 返回 [PPoPP 2024 总览](../index.md)
