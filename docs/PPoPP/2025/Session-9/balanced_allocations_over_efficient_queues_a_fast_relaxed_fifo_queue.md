---
title: "Balanced Allocations over Efficient Queues: A Fast Relaxed FIFO Queue"
description: "PPoPP 2025 Session 9（Concurrent Data Structures and Synchronization II）：按操作计数做 d-choice 均衡，吞吐 4× 且误差降至千分之一"
tags:
  - "PPoPP2025"
  - "Session-9"
  - "Concurrent Data Structures and Synchronization II"
  - "Relaxed Queues"
  - "Load Balancing"
  - "FIFO"
authors:
  - "Kåre von Geijer"
  - "Philippas Tsigas"
  - "Elias Johansson"
  - "Sebastian Hermansson"
session: "Session 9: Concurrent Data Structures and Synchronization II"
session_number: 9
session_chair: "Pengfei Su"
date: "2025-03-04"
time: "16:00–16:20"
room: "Acacia D"
doi: "10.1145/3710848.3710892"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Balanced Allocations over Efficient Queues: A Fast Relaxed FIFO Queue

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">在松弛 FIFO 队列场景重新审视 d-choice 负载均衡，按操作计数把操作均匀分配到 n 个子队列，实现与队列规模无关的低松弛误差，并能直接复用高性能线性化队列。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 9: Concurrent Data Structures and Synchronization II</p>
</div>

**作者**：Kåre von Geijer, Philippas Tsigas (Chalmers University of Technology and University of Gothenburg); Elias Johansson, Sebastian Hermansson (Chalmers University of Technology)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 16:00–16:20 · Session 9: Concurrent Data Structures and Synchronization II（主席：Pengfei Su）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710892) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 在松弛 FIFO 队列场景重新审视 d-choice 负载均衡，按操作计数把操作均匀分配到 n 个子队列，实现与队列规模无关的低松弛误差，并能直接复用高性能线性化队列。

## 研究问题

松弛语义通过弱化顺序语义换取并行度，但已有基于均衡分配的松弛 FIFO 队列设计存在松弛误差随规模增长、且无法把性能最好的线性化队列作为组件复用的问题。

## 方法简述

- 提出基于操作计数的负载均衡方案，把操作均匀分布到 n 个子队列。
- 证明该方案在一类可能执行上以高概率具有低松弛误差上界。
- 与已有方案不同，可直接接入并组合文献中最快的线性化队列设计。

## 主要结果

- 相比此前最好的均衡分配设计，吞吐提升 4× 以上，同时松弛误差不到其千分之一。
- 在并发广度优先搜索基准中，稳定优于松弛与严格的 SOTA FIFO 队列。

<details>
<summary>原文摘要（英文）</summary>

Relaxed semantics have been introduced to increase the achievable parallelism of concurrent data structures in exchange for weakening their ordering semantics. In this paper, we revisit the balanced allocations 𝑑-choice load balancing scheme in the context of relaxed FIFO queues. Our novel load balancing approach distributes operations evenly across 𝑛sub-queues based on operation counts, achieving low relaxation errors independent on the queues size, as opposed to similar earlier designs. We prove its relaxation errors to be of O( 𝑛log log𝑛 log𝑑 ) with high probability for a collection of possible executions. Furthermore, our scheme, contrary to previous ones, manages to interface and integrate the most performant linearizable queue designs from the literature as components. Our resulting relaxed FIFO queue is experimentally shown to outperform the previously best design using balanced allocations by more than four times in throughput, while simultaneously incurring less than a thousandth of its relaxation errors. In a concurrent breadth-first-search benchmark, our queue consistently outperforms both relaxed and strict state-of-the-art FIFO queues.

</details>

---

> 所属 Session：[Session 9: Concurrent Data Structures and Synchronization II](index.md) · 返回 [PPoPP 2025 总览](../index.md)
