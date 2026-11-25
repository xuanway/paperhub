---
title: "Publish on Ping: A Better Way to Publish Reservations in Memory Reclamation for Concurrent Data Structures"
description: "PPoPP 2025 Session 3（Concurrent Data Structures and Synchronization I）：按需发布预约替代全局可见预约，hazard pointer 上提速 1.2×–4×"
tags:
  - "PPoPP2025"
  - "Session-3"
  - "Concurrent Data Structures and Synchronization I"
  - "Memory Reclamation"
  - "Hazard Pointers"
  - "POSIX Signals"
authors:
  - "Ajay Singh"
  - "Trevor Brown"
session: "Session 3: Concurrent Data Structures and Synchronization I"
session_number: 3
session_chair: "Yuanhao Wei"
date: "2025-03-03"
time: "15:00–15:20"
room: "Acacia D"
doi: "10.1145/3710848.3710890"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
award: "Distinguished Paper Award"
---

# Publish on Ping: A Better Way to Publish Reservations in Memory Reclamation for Concurrent Data Structures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 publish-on-ping 内存回收技术，用 POSIX 信号与延迟回收取代读取前的全局可见预约，可作为 hazard pointer 与 hazard era 的直接替代。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 3: Concurrent Data Structures and Synchronization I</p>
</div>

**作者**：Ajay Singh, Trevor Brown (University of Waterloo)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 15:00–15:20 · Session 3: Concurrent Data Structures and Synchronization I（主席：Yuanhao Wei）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710890) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

> 🏆 **Distinguished Paper Award**

---

## 一句话总结

> 提出 publish-on-ping 内存回收技术，用 POSIX 信号与延迟回收取代读取前的全局可见预约，可作为 hazard pointer 与 hazard era 的直接替代。

## 研究问题

hazard pointer、hazard era 等基于逐次读预约的回收技术，要求在每次读之前发布预约并插入 fence 使其全局可见；在读密集负载中即使几乎不发生回收，这部分开销仍然被全额付出。

## 方法简述

- 线程私密地记录自己正在访问的记录，仅当回收线程需要时（ping）才按需共享。
- 结合 POSIX 信号与延迟回收，消除使用前的全局可见预约。
- 在 hazard pointer 基础上构造 EpochPOP，用 epoch 在常态下逼近 epoch-based 回收的性能，同时保留 hazard pointer 的鲁棒性。

## 主要结果

- 相对原始 hazard pointer 提升 1.2×–4×，相对 Folly 级高度优化实现最高提升 20%，相对 hazard era 最高快 3×。
- EpochPOP 性能与 epoch-based 回收相近，但提供更强的安全性保证。

<details>
<summary>原文摘要（英文）</summary>

Safe memory reclamation techniques that utilize per read reservations, such as hazard pointers and hazard eras, often cause significant overhead in traversals of linked concurrent data structures. This is primarily due to the need to announce a reservation, and fence to make it globally visible (and enforce appropriate ordering), before each read. In real world read-intensive workloads, this overhead is amplified because, even if relatively little memory reclamation actually occurs, the full overhead of reserving records before use is still incurred while traversing data structures. In this paper, we propose a novel memory reclamation technique by combining POSIX signals and delayed reclamation, introducing a publish-on-ping approach. This method eliminates the need to make reservations globally visible before use. Instead, threads privately track which records they are accessing, and share this information on demand with threads that intend to reclaim memory. The approach can serve as a drop-in replacement for hazard pointers and hazard eras. Furthermore, the capability to retain reservations during traversals in data structure operations and publish them on demand facilitates the construction of a variant of hazard pointers (EpochPOP). This variant uses epochs to approach the performance of epoch-based reclamation in the common case where threads are not frequently delayed (while retaining the robustness of hazard pointers). Our publish-on-ping implementations based on hazard pointers and hazard eras, when applied to various data structures, exhibit significant performance improvements. The improvements across various workloads and data structures range from 1.2X to 4X over the original HP, up to 20% compared to a heavily optimized HP implementation similar to the one in the Folly open-source library, and up to 3X faster than hazard eras. EpochPOP delivers performance similar to epoch-based reclamation while providing stronger guarantees.

</details>

---

> 所属 Session：[Session 3: Concurrent Data Structures and Synchronization I](index.md) · 返回 [PPoPP 2025 总览](../index.md)
