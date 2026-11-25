---
title: "Memory Bounds for Concurrent Bounded Queues"
description: "PPoPP 2024 Session Synchronization and Concurrency Control II：证明非阻塞有界队列的内存最优性需线性于并发进程数的开销"
tags:
  - "PPoPP2024"
  - "Session-5"
  - "Synchronization and Concurrency Control II"
  - "concurrency"
  - "bounded queue"
  - "memory overhead"
authors:
  - "Vitaly Aksenov"
  - "Nikita Koval"
  - "Petr Kuznetsov"
  - "Anton Paramonov"
session: "Session 5: Synchronization and Concurrency Control II"
session_number: 5
session_chair: "Erez Petrank"
date: "2024-03-05"
time: "10:00–10:20"
room: "Moorfoot"
doi: "10.1145/3627535.3638497"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Memory Bounds for Concurrent Bounded Queues

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该文研究非阻塞有界队列的内存最优性，证明在 ABA 问题存在的一般情形下，内存最优实现的开销随并发进程数线性增长。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 5: Synchronization and Concurrency Control II</p>
</div>

**作者**：Vitaly Aksenov (City, University of London); Nikita Koval (JetBrains); Petr Kuznetsov (Telecom Paris, Institut Polytechnique Paris); Anton Paramonov (EPFL)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 10:00–10:20 · Session 5: Synchronization and Concurrency Control II（主席：Erez Petrank）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638497) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Concurrent data structures often require additional memory for handling synchronization issues in addition to memory for storing elements. Depending on the amount of this additional memory, implementations can be more or less memory-friendly. A memory-optimal implementation enjoys the minimal possible memory overhead, which, in practice, reduces cache misses and unnecessary memory reclamation. In this paper, we discuss the memory-optimality of nonblocking bounded queues. Essentially, we investigate the possibility of constructing an implementation that utilizes a pre-allocated array to store elements and constant memory overhead, e.g., two positioning counters for enqueue(..) and dequeue() operations. Such an implementation can be readily constructed when the ABA problem is precluded, e.g., assuming that the hardware supports LL/SC instructions or all inserted elements are distinct. However, in the general case, we show that a memory-optimal non-blocking bounded queue incurs linear overhead in the number of concurrent processes. These results not only provide helpful intuition for concurrent algorithm developers but also open a new research avenue on the memory-optimality phenomenon in concurrent data structures. The full version of this paper is available on arXiv [2].

## 中文摘要

并发数据结构除了存储元素所需的内存外，通常还需要额外内存来处理同步问题。根据这部分额外内存的多少，实现可能在内存友好性上有所优劣。内存最优的实现享有最小的可能内存开销，这在实践中可减少缓存缺失和不必要的内存回收。本文讨论非阻塞有界队列的内存最优性。本质上，我们研究构造这样一种实现的可能性：它使用预分配数组存储元素，并具有常数内存开销，例如两个分别用于 enqueue(..) 和 dequeue() 操作的定位计数器。当 ABA 问题被排除时，例如假设硬件支持 LL/SC 指令，或所有插入的元素互不相同，这样的实现可以很容易地构造出来。然而，在一般情形下，我们证明内存最优的非阻塞有界队列会带来与并发进程数成线性的开销。这些结果不仅为并发算法开发者提供了有益的直觉，也开辟了关于并发数据结构中内存最优性现象的新研究途径。本文的完整版本可在 arXiv [2] 获取。

## 英文关键词

concurrency, memory overhead, bounded queue, memory-optimality

## 中文关键词

并发；内存开销；有界队列；内存最优性

---

## 一句话总结

> 该文研究非阻塞有界队列的内存最优性，证明在 ABA 问题存在的一般情形下，内存最优实现的开销随并发进程数线性增长。

## 研究问题

并发队列除元素存储外还需额外内存处理同步，但把开销降到常数（预分配数组加两个定位计数器）仅在 ABA 问题被排除时可行，一般情形下缺少理论界定。

## 方法简述

- 将内存最优实现建模为「预分配数组存元素 + 常数内存开销」，即以两个分别供 enqueue(..) 与 dequeue() 使用的定位计数器为例。
- 在 ABA 问题可被排除的假设下（硬件支持 LL/SC 指令，或所有插入元素互不相同）给出常数开销构造。
- 在一般情形下给出下界结果，说明额外内存开销与并发进程数成线性关系。

## 主要结果

- 证明一般情形下内存最优的非阻塞有界队列在并发进程数上产生线性内存开销。
- 指出 ABA 可排除时可用两个定位计数器实现常数开销，并为并发数据结构的内存最优性现象开辟新研究方向。

---

> 所属 Session：[Session 5: Synchronization and Concurrency Control II](index.md) · 返回 [PPoPP 2024 总览](../index.md)
