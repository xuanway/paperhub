---
title: "Fixing Non-blocking Data Structures for Better Compatibility with Memory Reclamation Schemes"
description: "PPoPP 2026 Session 1（Concurrency Control）：让 Harris 链表等乐观遍历结构兼容 HP/HE/IBR/Hyaline"
tags:
  - "PPoPP2026"
  - "Session-1"
  - "Concurrency Control"
  - "Memory Reclamation"
  - "Optimistic Traversal"
  - "Lock-free"
authors:
  - "Md Amit Hasan Arovi"
  - "Ruslan Nikolaev"
session: "Session 1: Concurrency Control"
session_number: 1
session_chair: "Madan Musuvathi"
date: "2026-02-02"
time: "10:30–10:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786455"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Fixing Non-blocking Data Structures for Better Compatibility with Memory Reclamation Schemes

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Safe Concurrent Optimistic Traversals（SCOT），使带乐观遍历的经典数据结构（如 Harris 链表与 Natarajan–Mittal 树）可与 HP、HE、IBR、Hyaline 等稳健 SMR 方案兼容。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 1: Concurrency Control</p>
</div>

**作者**：Md Amit Hasan Arovi and Ruslan Nikolaev — Pennsylvania State University, USA

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 10:30–10:50 · Session 1: Concurrency Control（主席：Madan Musuvathi）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786455) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

We present a new technique, Safe Concurrent Optimistic Traversals (SCOT), to address a well-known problem related to optimistic traversals with classical and more recent safe memory reclamation (SMR) schemes, such as Hazard Pointers (HP), Hazard Eras (HE), Interval-Based Reclamation (IBR), and Hyaline. Unlike Epoch-Based Reclamation (EBR), these (robust) schemes protect against stalled threads but lack support for well-known data structures with optimistic traversals, e.g., Harris’ list and the Natarajan-Mittal tree. Such schemes are either incompatible with them or need changes with performance trade-offs (e.g., the Harris-Michael list). SCOT keeps existing SMR schemes intact and retains performance benefits of original data structures. We implement and evaluate SCOT with Harris’ list and the Natarajan-Mittal tree, but it is also applicable to other data structures. Furthermore, we provide a simple modification for wait-free traversals. We observe similar performance speedups (e.g., Harris vs. Harris-Michael lists) that were previously available only to EBR users. Our version of the tree also achieves very high throughput, comparable to that of EBR, which is often treated as a practical upper bound.

## 中文摘要

我们提出一种新技术——安全并发乐观遍历（Safe Concurrent Optimistic Traversals，SCOT），用于解决与乐观遍历相关的一个众所周知的问题，该问题出现在经典及较新的安全内存回收（safe memory reclamation，SMR）方案中，例如 Hazard Pointers（HP）、Hazard Eras（HE）、基于区间的回收（Interval-Based Reclamation，IBR）以及 Hyaline。与基于纪元的回收（Epoch-Based Reclamation，EBR）不同，这些（鲁棒的）方案能够防护停滞的线程，但不支持采用乐观遍历的众所周知的数据结构，例如 Harris 链表与 Natarajan-Mittal 树。此类方案要么与这些数据结构不兼容，要么需要做出改动并付出性能代价（例如 Harris-Michael 链表）。SCOT 保持现有 SMR 方案不变，并保留原始数据结构的性能优势。我们以 Harris 链表和 Natarajan-Mittal 树实现并评估了 SCOT，但它同样适用于其他数据结构。此外，我们还给出了一种针对无等待（wait-free）遍历的简单修改。我们观察到与以往仅 EBR 用户才能获得的相当的性能加速（例如 Harris 链表与 Harris-Michael 链表的对比）。我们的树版本还实现了非常高的吞吐量，可与 EBR 相媲美，而 EBR 常被视为实际的上界。

## 英文关键词

hazard pointers, non-blocking, wait-free, Harris’ list, Natarajan-Mittal tree

## 中文关键词

危险指针（Hazard Pointers）；非阻塞（non-blocking）；无等待（wait-free）；Harris 链表；Natarajan-Mittal 树

---

## 一句话总结

> 提出 Safe Concurrent Optimistic Traversals（SCOT），使带乐观遍历的经典数据结构（如 Harris 链表与 Natarajan–Mittal 树）可与 HP、HE、IBR、Hyaline 等稳健 SMR 方案兼容。

## 研究问题

这些稳健的 SMR 方案能抵御停滞线程，却不支持采用乐观遍历的经典数据结构，或需要付出性能代价修改结构（如 Harris-Michael 链表）。

## 方法简述

- 保持现有 SMR 方案不变，同时保留原数据结构的性能优势。
- 在 Harris 链表与 Natarajan–Mittal 树上实现并评估 SCOT，该方法也适用于其他数据结构。
- 为 wait-free 遍历给出简单修改。

## 主要结果

- 获得此前只有 EBR 用户才能得到的类似加速（如 Harris 与 Harris-Michael 链表对比）。
- 其树实现的吞吐可与常被视为性能上界的 EBR 相比。

---

> 所属 Session：[Session 1: Concurrency Control](index.md) · 返回 [PPoPP 2026 总览](../index.md)
