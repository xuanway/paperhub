---
title: "GraphCube: Interconnection Hierarchy-aware Graph Processing"
description: "PPoPP 2024 Session Graph Processing：互连层次感知划分，79,024 节点上吞吐与可扩展性领先，Graph 500 登顶"
tags:
  - "PPoPP2024"
  - "Session-4"
  - "Graph Processing"
  - "Graph processing"
  - "Graph partitioning"
  - "Scalability"
authors:
  - "Xinbiao Gan"
  - "Guang Wu"
  - "Shenghao Qiu"
  - "Feng Xiong"
  - "Jiaqi Si"
  - "Jianbin Fang"
  - "Dezun Dong"
  - "Chunye Gong"
  - "Tiejun Li"
  - "Zheng Wang"
session: "Session 4: Graph Processing"
session_number: 4
session_chair: "Xipeng Shen"
date: "2024-03-04"
time: "16:30–16:50"
room: "Moorfoot"
doi: "10.1145/3627535.3638498"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# GraphCube: Interconnection Hierarchy-aware Graph Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">GraphCube 提出互连层次感知的图划分方法，在多达 79,024 节点、120 万以上核心上均衡负载并压低跨层通信，吞吐与可扩展性优于现有方法。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 4: Graph Processing</p>
</div>

**作者**：Xinbiao Gan, Guang Wu (NUDT); Shenghao Qiu (University of Leeds); Feng Xiong, Jiaqi Si, Jianbin Fang, Dezun Dong (NUDT); Chunye Gong (NUDT & National Supercomputer Center in Tianjin); Tiejun Li (NUDT); Zheng Wang (University of Leeds)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 16:30–16:50 · Session 4: Graph Processing（主席：Xipeng Shen）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638498) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Processing large-scale graphs with billions to trillions of edges requires efficiently utilizing parallel systems. However, current graph processing engines do not scale well beyond a few tens of computing nodes because they are oblivious to the communication cost variations across the interconnection hierarchy. We introduce GraphCube, a better approach to optimizing graph processing on large-scale parallel systems with complex interconnections. GraphCube features a new graph partitioning approach to achieve better load balancing and minimize communication overhead across multiple levels of the interconnection hierarchy. We evaluate GraphCube by applying it to fundamental graph operations performed on synthetic and real-world graph datasets. Our evaluation used up to 79,024 computing nodes and 1.2+ million processor cores. Our large-scale experiments show that GraphCube outperforms state-of-the-art parallel graph processing methods in throughput and scalability. Furthermore, GraphCube outperformed the top-ranked systems on the Graph 500 list.

## 中文摘要

处理从数十亿到数万亿条边的大规模图需要高效利用并行系统。然而，当前的图处理引擎在超过数十个计算节点后便难以扩展，因为它们忽视了互连层次结构中通信成本的差异。我们提出 GraphCube，一种在具有复杂互连结构的大规模并行系统上优化图处理的更优方法。GraphCube 采用一种新的图划分方法，以实现更好的负载均衡，并最小化跨互连层次多个层级的通信开销。我们通过在合成与真实图数据集上执行的基础图操作来评估 GraphCube。我们的评估使用了多达 79,024 个计算节点和 120 万以上处理器核心。大规模实验表明，GraphCube 在吞吐量和可扩展性上优于最先进的并行图处理方法。此外，GraphCube 在 Graph 500 榜单上超过了排名最高的系统。

## 英文关键词

Graph processing, Graph partitioning, Parallel computing, Vectorization, Graph500

## 中文关键词

图处理；图划分；并行计算；向量化；Graph500

---

## 一句话总结

> GraphCube 提出互连层次感知的图划分方法，在多达 79,024 节点、120 万以上核心上均衡负载并压低跨层通信，吞吐与可扩展性优于现有方法。

## 研究问题

现有图处理引擎对互连层次结构中通信成本的差异不敏感，超过数十个计算节点后便难以扩展，无法支撑十亿至万亿条边规模的图处理。

## 方法简述

- 提出新的图划分方法，在互连层次的多个层级上同时追求更好的负载均衡与最小化通信开销。
- 将互连层次中通信成本的变化纳入划分决策，避免仅按单层拓扑做静态切分。
- 在合成与真实图数据集上，以基础图操作评估该划分在大规模并行系统上的效果。

## 主要结果

- 大规模实验使用了多达 79,024 个计算节点和 120 万以上处理器核心。
- 在吞吐量与可扩展性上优于最先进的并行图处理方法。
- 在 Graph 500 榜单上超过了排名最高的系统。

---

> 所属 Session：[Session 4: Graph Processing](index.md) · 返回 [PPoPP 2024 总览](../index.md)
