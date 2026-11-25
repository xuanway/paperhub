---
title: "Aggregating Funnels for Faster Fetch&Add and Queues"
description: "PPoPP 2025 Session 3（Concurrent Data Structures and Synchronization I）：批处理 + 多地址分散，消除单地址 fetch&add 热点"
tags:
  - "PPoPP2025"
  - "Session-3"
  - "Concurrent Data Structures and Synchronization I"
  - "Fetch&Add"
  - "Contention"
  - "Concurrent Queues"
authors:
  - "Younghun Roh"
  - "Yuanhao Wei"
  - "Eric Ruppert"
  - "Panagiota Fatourou"
  - "Siddhartha Jayanti"
  - "Julian Shun"
session: "Session 3: Concurrent Data Structures and Synchronization I"
session_number: 3
session_chair: "Yuanhao Wei"
date: "2025-03-03"
time: "14:20–14:40"
room: "Acacia D"
doi: "10.1145/3710848.3710873"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Aggregating Funnels for Faster Fetch&Add and Queues

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Aggregating Funnels 算法，把对单一热点地址的 fetch-and-add 分散到多个地址并按批聚合，在降低竞争的同时提升吞吐。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 3: Concurrent Data Structures and Synchronization I</p>
</div>

**作者**：Younghun Roh, Yuanhao Wei (Massachusetts Institute of Technology); Eric Ruppert (York University); Panagiota Fatourou (Institute of Computer Science, Foundation for Research and Technology - Hellas, and Computer Science Department, University of Crete); Siddhartha Jayanti (Google); Julian Shun (Massachusetts Institute of Technology)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 14:20–14:40 · Session 3: Concurrent Data Structures and Synchronization I（主席：Yuanhao Wei）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710873) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 Aggregating Funnels 算法，把对单一热点地址的 fetch-and-add 分散到多个地址并按批聚合，在降低竞争的同时提升吞吐。

## 研究问题

许多并发算法需要对同一内存位置执行 fetch-and-add，该位置很容易成为竞争热点，限制整体可扩展性。

## 方法简述

- 把 fetch-and-add 操作分散到多个内存位置。
- 将操作聚合成批，使一批只需一次硬件 fetch-and-add，批内各操作再对另一地址执行 fetch-and-add 得到结果。

## 主要结果

- 吞吐高于 Combining Funnels 等已有合并技术，可扩展性显著优于单地址硬件 fetch-and-add。
- 替换最先进并发队列中的 fetch-and-add 后消除瓶颈，队列整体吞吐大幅提升。

<details>
<summary>原文摘要（英文）</summary>

Many concurrent algorithms require processes to perform fetch-and-add operations on a single memory location, which can be a hot spot of contention. We present a novel algorithm called Aggregating Funnels that reduces this contention by spreading the fetch-and-add operations across multiple memory locations. It aggregates fetch-and-add operations into batches so that the batch can be performed by a single hardware fetch-and-add instruction on one location and all operations in the batch can efficiently compute their results by performing a fetch-and-add instruction on a different location. We show experimentally that this approach achieves higher throughput than previous combining techniques, such as Combining Funnels, and is substantially more scalable than applying hardware fetch-and-add instructions on a single memory location. We show that replacing the fetch-and-add instructions in the fastest state-of-the-art concurrent queue by our Aggregating Funnels eliminates a bottleneck and greatly improves the queue’s overall throughput.

</details>

---

> 所属 Session：[Session 3: Concurrent Data Structures and Synchronization I](index.md) · 返回 [PPoPP 2025 总览](../index.md)
