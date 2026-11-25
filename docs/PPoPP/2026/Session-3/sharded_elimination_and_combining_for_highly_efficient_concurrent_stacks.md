---
title: "Sharded Elimination and Combining for Highly-Efficient Concurrent Stacks"
description: "PPoPP 2026 Session 3（Concurrent Data Structures）：分片+消除+合并，多线程高竞争下最高快 2×"
tags:
  - "PPoPP2026"
  - "Session-3"
  - "Concurrent Data Structures"
  - "Concurrent Stacks"
  - "Elimination"
  - "Combining"
authors:
  - "Ajay Singh"
  - "Nikos Metaxakis"
  - "Panagiota Fatourou"
session: "Session 3: Concurrent Data Structures"
session_number: 3
session_chair: "Calin Cascaval"
date: "2026-02-02"
time: "14:30–14:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786458"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Sharded Elimination and Combining for Highly-Efficient Concurrent Stacks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出基于分片与 fetch&increment 的阻塞线性一致并发栈，融合新的消除机制与高效合并方案降低共享访问竞争，在多种场景下比现有并发栈快至多 2×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 3: Concurrent Data Structures</p>
</div>

**作者**：Ajay Singh, Nikos Metaxakis, and Panagiota Fatourou — ICS-FORTH, Greece; University of Crete, Greece

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 14:30–14:50 · Session 3: Concurrent Data Structures（主席：Calin Cascaval）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786458) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

We present a new blocking linearizable stack implementation which utilizes sharding and fetch&increment to achieve significantly better performance than all existing concurrent stacks. The proposed implementation is based on a novel elimination mechanism and an efficient combining scheme that are efficiently blended to gain high performance. Our implementation results in enhanced parallelism and low contention when accessing the shared stack. Experiments show that the proposed stack implementation outperforms all existing concurrent stacks by up to 2× in many cases. It is particularly efficient in systems supporting a large number of threads and in high contention scenarios.

## 中文摘要

我们提出一种新的阻塞式可线性化栈实现，它利用分片（sharding）与 fetch&increment 来获得显著优于所有现有并发栈的性能。所提出的实现基于一种新颖的消除（elimination）机制与一种高效的合并（combining）方案，二者被高效地融合在一起以取得高性能。我们的实现提高了访问共享栈时的并行度并降低了竞争。实验表明，所提出的栈实现在许多情形下以最高 2× 的优势优于所有现有并发栈。在支持大量线程的系统中以及高竞争场景下，它尤其高效。

## 英文关键词

concurrent data structures, elimination, software combining, concurrent stacks, linearizability

## 中文关键词

并发数据结构；消除（elimination）；软件合并（software combining）；并发栈；可线性化（linearizability）

---

## 一句话总结

> 提出基于分片与 fetch&increment 的阻塞线性一致并发栈，融合新的消除机制与高效合并方案降低共享访问竞争，在多种场景下比现有并发栈快至多 2×。

## 研究问题

现有并发栈在高竞争、多线程场景下对共享栈的访问竞争激烈、并行度受限，缺少能同时保持低竞争与高吞吐的实现。

## 方法简述

- 采用分片（sharding）与 fetch&increment 组织共享栈，降低共享栈访问竞争并获得更高并行度。
- 提出新的消除（elimination）机制，使入栈与出栈操作可在不触碰共享结构的情况下配对完成。
- 设计高效的合并（combining）方案，并与消除机制有机融合以取得高性能，同时保持阻塞、线性一致的语义。

## 主要结果

- 在多种情况下比所有现有并发栈实现快至多 2×。
- 在支持大量线程的系统以及高竞争场景中尤为高效。

---

> 所属 Session：[Session 3: Concurrent Data Structures](index.md) · 返回 [PPoPP 2026 总览](../index.md)
