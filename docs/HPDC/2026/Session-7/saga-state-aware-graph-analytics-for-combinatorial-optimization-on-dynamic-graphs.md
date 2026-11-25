---
title: "SAGA: State-Aware Graph Analytics for Combinatorial Optimization on Dynamic Graphs"
description: "HPDC 2026 · Session 7 — Graph Processing & Community Detection"
tags:
  - "HPDC2026"
  - "Session 7"
  - "Graph Processing & Community Detection"
---

# SAGA: State-Aware Graph Analytics for Combinatorial Optimization on Dynamic Graphs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 7 — Graph Processing & Community Detection（2026年7月15日 13:30–14:30 · Session Chair：Dilma Da Silva）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 7</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807595)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#PrajapatiNB26](https://dblp.org/db/conf/hpdc/hpdc2026.html#PrajapatiNB26)

**作者**：Rohit Prajapati, Prajjwal Nijhara, Dip Sankar Banerjee

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 7 — Graph Processing & Community Detection（2026年7月15日 13:30–14:30 · Session Chair：Dilma Da Silva）

---

## 英文摘要

Combinatorial optimization problems on graphs, such as Maximal Independent Set (MIS), Graph Coloring (GC), and Maximal Matching (MM), are computationally challenging and are significantly harder in dynamic settings where edges and vertices evolve continuously. Maintaining valid solutions under high-rate updates requires more than recomputation or static parallelism. We present SAGA, a high-performance framework for real-time combinatorial optimization on dynamic graphs. SAGA adopts a state-aware execution model in which each vertex maintains compact local state, enabling incremental and localized updates in response to graph changes. By coupling fine-grained task parallelism with data-parallel execution, SAGA minimizes communication overhead through state-aware partitioning and distributed state management. The SAGA compute engine maintains evolving solutions consistently across worker nodes while supporting low-latency queries. We evaluate SAGA on a distributed memory cluster against three state-of-the-art graph frameworks. On streaming instances of MIS, MM, and GC, SAGA achieves speedups of up to 11.8×, 6.2×, and 8.4×, respectively, sustains up to 7.2M operations per second, and delivers over 10.8× lower query latency compared to state-of-the-art graph analytics frameworks under concurrent update workloads.

## 中文摘要

图上的组合优化问题，如最大独立集（MIS）、图着色（GC）和最大匹配（MM），在计算上极具挑战，而在边与顶点持续演化的动态场景下更是难上加难。在高更新率下维持有效解，需要的不仅仅是重计算或静态并行。我们提出 SAGA，一个面向动态图上实时组合优化的高性能框架。SAGA 采用状态感知的执行模型，其中每个顶点维护紧凑的局部状态，从而能够针对图变化进行增量、局部化的更新。通过将细粒度任务并行与数据并行执行相结合，SAGA 借助状态感知划分和分布式状态管理最小化通信开销。SAGA 计算引擎在各工作节点间一致地维护演化中的解，同时支持低延迟查询。我们在分布式内存集群上，将 SAGA 与三种最先进的图框架进行了评估。在 MIS、MM 和 GC 的流式实例上，SAGA 分别取得最高 11.8 倍、6.2 倍和 8.4 倍的加速，持续达到每秒 720 万次操作，并在并发更新负载下相比最先进的图分析框架将查询延迟降低 10.8 倍以上。

## 英文关键词

Dynamic graphs, Combinatorial optimization, Streaming graph processing, Distributed computing, State-aware execution, Parallel graph analytics

## 中文关键词

动态图，组合优化，流式图处理，分布式计算，状态感知执行，并行图分析

---

[← 返回 Session 7 — Graph Processing & Community Detection](index.md)
