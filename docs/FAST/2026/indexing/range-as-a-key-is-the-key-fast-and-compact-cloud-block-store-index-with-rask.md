---
title: "\"Range as a Key\" is the Key! Fast and Compact Cloud Block Store Index with RASK"
description: "FAST 2026 · Indexing · 第 183–202 页"
tags:
  - "FAST2026"
  - "Indexing"
---

# "Range as a Key" is the Key! Fast and Compact Cloud Block Store Index with RASK

**中文标题**：“以范围为键”才是关键！基于 RASK 的快速紧凑云块存储索引

**Session**：Indexing · 2026-02-24 14:00–15:40 · Chair：Zhichao Cao（Arizona State University）

**作者**：Haoru Zhao, Mingkai Dong, and Erci Xu, Shanghai Jiao Tong University; Zhongyu Wang, Alibaba Group; Haibo Chen, Shanghai Jiao Tong University

**会议**：FAST 2026 · Santa Clara, CA · 第 183–202 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/zhao](https://www.usenix.org/conference/fast26/presentation/zhao)

**论文 PDF**：[fast26-zhao.pdf](https://www.usenix.org/system/files/fast26-zhao.pdf)

---

## 英文摘要

In cloud block store, indexing is on the critical path of I/O operations and typically resides in memory. With the scaling of users and the emergence of denser storage media, the index has become a primary memory consumer, causing memory strain. Our extensive analysis of production traces reveals that write requests exhibit a strong tendency to target continuous block ranges in cloud storage systems. Thus, compared to current per-block indexing, our insight is that *we should directly index block ranges (i.e., range-as-a-key) to save memory*.

In this paper, we propose RASK, a memory-efficient and high-performance tree-structured index that natively indexes ranges. While range-as-a-key offers the potential to save memory and improve performance, realizing this idea is challenging due to the range overlap and range fragmentation issues. To handle range overlap efficiently, RASK introduces the log-structured leaf, combined with range-tailored search and garbage collection. To reduce range fragmentation, RASK employs range-aware split and merge mechanisms. Our evaluations on four production traces show that RASK reduces memory footprint by up to 98.9% and increases throughput by up to 31.0× compared to ten state-of-the-art indexes.

## 中文摘要

在云块存储中，索引位于 I/O 操作的关键路径上，通常驻留在内存中。随着用户规模扩大以及更密集存储介质的出现，索引已成为主要的内存消耗者，造成内存压力。我们对生产环境跟踪数据的大量分析表明，云存储系统中的写请求强烈倾向于针对连续的块范围。因此，与当前按块索引相比，我们的洞见是：应当直接对块范围建立索引（即 range-as-a-key），以节省内存。

本文提出 RASK，一种原生索引范围的内存高效、高性能树形索引。虽然以范围为键具有节省内存和提升性能的潜力，但由于范围重叠和范围碎片化问题，实现这一想法颇具挑战。为高效处理范围重叠，RASK 引入日志结构叶节点，并结合面向范围的搜索和垃圾回收。为减少范围碎片化，RASK 采用范围感知的拆分与合并机制。我们在四个生产跟踪数据上的评估表明，与十种最先进索引相比，RASK 将内存占用最多减少 98.9%，并将吞吐量最多提升 31.0 倍。
