---
title: "DTMiner: A Data-Centric System for Efficient Temporal Motif Mining"
description: "PPoPP 2026 Session 11（Graphs and Graph Neural Networks）：LES 执行模型共享同一图遍历，性能提升 1.14–11.98×"
tags:
  - "PPoPP2026"
  - "Session-11"
  - "Graphs and Graph Neural Networks"
  - "Temporal Motif Mining"
  - "Data-Centric"
  - "Cache Locality"
authors:
  - "Yinbo Hou"
  - "Hao Qi"
  - "Ligang He"
  - "Jin Zhao"
  - "Yu Zhang"
  - "Hui Yu"
  - "Longlong Lin"
  - "Lin Gu"
  - "Wenbin Jiang"
  - "Xiaofei Liao"
  - "Hai Jin"
session: "Session 11: Graphs and Graph Neural Networks"
session_number: 11
session_chair: "Ali Jannesari"
date: "2026-02-03"
time: "16:50–17:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786416"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# DTMiner: A Data-Centric System for Efficient Temporal Motif Mining

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 DTMiner，基于数据访问空间相似性与时间单调性观察的时间模体挖掘系统，引入加载—探索—同步执行模型让不同任务共享图遍历，性能提升 1.14–11.98×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 11: Graphs and Graph Neural Networks</p>
</div>

**作者**：Yinbo Hou, Hao Qi, Ligang He, Jin Zhao, Yu Zhang, Hui Yu, Longlong Lin, Lin Gu, Wenbin Jiang, Xiaofei Liao, and Hai Jin — Huazhong University of Science and Technology, China; University of Warwick, UK; Hong Kong University of Science and Technology, China; South- west University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 16:50–17:10 · Session 11: Graphs and Graph Neural Networks（主席：Ali Jannesari）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786416) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Mining temporal motifs in temporal graphs is essential for many critical applications. Although several solutions have been proposed to handle temporal motif mining, they still suffer from substantial inefficiencies due to significant redundant graph traversals and fragmented memory access, both caused by irregular search tree expansions across different motif matching tasks. In this work, we observe that data accesses issued by these tasks exhibit strong spatial similarity and temporal monotonicity. Based on these observations, this paper proposes an efficient data-centric temporal motif mining system DTMiner, which introduces a novel Load-Explore-Synchronize (LES) execution model to efficiently regularize data accesses to the common temporal graph data among different tasks. Specifically, DTMiner enables the temporal graph chunks to be sequentially loaded into the cache in temporal order and then triggers all relevant tasks to explore only these loaded data for search tree expansions in a fine-grained synchronization mechanism. In this way, different tasks can share the graph traversal corresponding to the same chunks, while fragmented memory accesses are restricted to the graph data residing in the cache, significantly reducing data access overhead. Experimental results demonstrate that DTMiner achieves 1.14×-11.98× performance improvement in comparison with the state-of-the-art temporal motif mining solutions.

## 中文摘要

在时序图中挖掘时序模体（temporal motif）对许多关键应用至关重要。尽管已有若干方案用于处理时序模体挖掘，但由于不同模体匹配任务之间不规则的搜索树扩展导致大量冗余的图遍历与碎片化的内存访问，这些方案仍存在严重的低效问题。在本工作中，我们观察到这些任务所发出的数据访问表现出很强的空间相似性与时间单调性。基于这些观察，本文提出一个高效的数据中心式时序模体挖掘系统 DTMiner，它引入新颖的“加载—探索—同步（Load-Explore-Synchronize，LES）”执行模型，以高效地将不同任务对公共时序图数据的访问规整化。具体而言，DTMiner 使时序图块按时间顺序依次加载到缓存中，随后以细粒度同步机制触发所有相关任务仅对这些已加载数据进行搜索树扩展的探索。如此，不同任务可以共享同一批图块所对应的图遍历，而碎片化的内存访问被限制在驻留于缓存中的图数据上，从而显著降低数据访问开销。实验结果表明，与最先进的时序模体挖掘方案相比，DTMiner 取得 1.14×–11.98× 的性能提升。

## 英文关键词

Temporal Motif Mining; Spatial Similarity; Temporal Monotonicity; Data-Centric

## 中文关键词

时序模体挖掘；空间相似性；时间单调性；数据中心式

---

## 一句话总结

> 提出 DTMiner，基于数据访问空间相似性与时间单调性观察的时间模体挖掘系统，引入加载—探索—同步执行模型让不同任务共享图遍历，性能提升 1.14–11.98×。

## 研究问题

现有时间模体挖掘方案因不同匹配任务的不规则搜索树扩展，产生大量冗余图遍历与碎片化内存访问，效率低下。

## 方法简述

- 观察到不同任务发出的数据访问呈现强空间相似性与时间单调性。
- 引入加载—探索—同步（LES）执行模型，按时间顺序把时间图分块依次加载进缓存。
- 触发所有相关任务仅探索已加载数据来扩展搜索树，并采用细粒度同步机制。
- 使不同任务共享同一分块对应的图遍历，把碎片化访存限制在缓存内的图数据上，显著降低访存开销。

## 主要结果

- 相比最先进的时间模体挖掘方案，性能提升 1.14×–11.98×。
- 通过任务间共享图遍历与缓存内访存，显著降低了数据访问开销。

---

> 所属 Session：[Session 11: Graphs and Graph Neural Networks](index.md) · 返回 [PPoPP 2026 总览](../index.md)
