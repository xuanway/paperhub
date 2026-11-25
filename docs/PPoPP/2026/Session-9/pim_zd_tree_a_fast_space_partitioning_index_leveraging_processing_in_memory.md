---
title: "PIM-zd-tree: A Fast Space-Partitioning Index Leveraging Processing-in-Memory"
description: "PPoPP 2026 Session 9（Parallel Algorithms）：首个真实 PIM 上的空间划分索引，吞吐最高 4.25×/99×"
tags:
  - "PPoPP2026"
  - "Session-9"
  - "Parallel Algorithms"
  - "Processing-in-Memory"
  - "Spatial Index"
  - "Load Balance"
authors:
  - "Yiwei Zhao"
  - "Hongbo Kang"
  - "Ziyang Men"
  - "Yan Gu"
  - "Guy E. Blelloch"
  - "Laxman Dhulipala"
  - "Charles McGuffey"
  - "Phillip B. Gibbons"
session: "Session 9: Parallel Algorithms"
session_number: 9
session_chair: "Kenjiro Taura"
date: "2026-02-03"
time: "15:10–15:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786411"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# PIM-zd-tree: A Fast Space-Partitioning Index Leveraging Processing-in-Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 PIM-zd-tree，首个面向真实 PIM 系统的空间划分索引，用可调多层结构与分层布局/划分/缓存策略实现负载均衡与低通信，吞吐最高提升 4.25× 与 99×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 9: Parallel Algorithms</p>
</div>

**作者**：Yiwei Zhao, Hongbo Kang, Ziyang Men, Yan Gu, Guy E. Blelloch, Laxman Dhulipala, Charles McGuffey, and Phillip B. Gibbons — Carnegie Mellon University, USA; Tsinghua University, China; University of California at Riverside, USA; University of Maryland, USA; Reed College, USA

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 15:10–15:30 · Session 9: Parallel Algorithms（主席：Kenjiro Taura）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786411) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Space-partitioning indexes are widely used for managing multi-dimensional data, but their throughput is often memory-bottlenecked. Processing-in-memory (PIM), an emerging architectural paradigm, mitigates memory bottlenecks by embedding processing cores directly within memory modules, allowing computation to be offloaded to these PIM cores. In this paper, we present PIM-zd-tree, the first space-partitioning index specifically designed for real-world PIM systems. PIM-zd-tree employs a tunable multi-layer structure, with each layer adopting distinct data layouts, partitioning schemes, and caching strategies. Its design is theoretically grounded to achieve load balance, minimal memory-channel communication, and low space overhead. To bridge theory and practice, we incorporate implementation techniques such as practical chunking and lazy counters. Evaluation on a real-world PIM system shows that PIM-zd-tree’s throughput is up to 4.25× and 99× higher than two state-of-the-art shared-memory baselines.

## 中文摘要

空间划分索引被广泛用于管理多维数据，但其吞吐量常常受限于内存瓶颈。存内计算（PIM）作为一种新兴的体系结构范式，通过将处理核心直接嵌入内存模块、允许将计算卸载到这些 PIM 核心上来缓解内存瓶颈。本文提出 PIM-zd-tree，这是首个专为真实 PIM 系统设计的空间划分索引。PIM-zd-tree 采用可调的多层结构，其中每一层采用不同的数据布局、划分方案与缓存策略。其设计具有理论基础，可实现负载均衡、最小的内存通道通信以及低空间开销。为弥合理论与实践之间的差距，我们引入了实用分块（practical chunking）与惰性计数器等实现技术。在真实 PIM 系统上的评估表明，PIM-zd-tree 的吞吐量比两个最先进的共享内存基线分别高出最高 4.25 倍和 99 倍。

## 英文关键词

space-partitioning index, processing-in-memory, near-data-processing, nearest neighbor search

## 中文关键词

空间划分索引；存内计算；近数据处理；最近邻搜索

---

## 一句话总结

> 提出 PIM-zd-tree，首个面向真实 PIM 系统的空间划分索引，用可调多层结构与分层布局/划分/缓存策略实现负载均衡与低通信，吞吐最高提升 4.25× 与 99×。

## 研究问题

空间划分索引广泛用于多维数据管理，但吞吐常受内存瓶颈限制；存内计算（PIM）虽能缓解，此前缺少专门面向真实 PIM 系统设计的空间划分索引。

## 方法简述

- 设计可调的多层结构，每层采用不同的数据布局、划分方案与缓存策略。
- 以理论分析为基础，使设计达到负载均衡、最小的内存通道通信与低空间开销。
- 引入实用分块（practical chunking）与惰性计数器等实现技术，弥合理论设计与实际系统之间的差距。

## 主要结果

- 在真实 PIM 系统上，吞吐比两个最先进的共享内存基线最高分别高出 4.25× 与 99×。
- 实际硬件验证了其理论设计目标：负载均衡、内存通道通信最小且空间开销低。

---

> 所属 Session：[Session 9: Parallel Algorithms](index.md) · 返回 [PPoPP 2026 总览](../index.md)
