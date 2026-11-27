---
title: "I-DGNN: A Graph Dissimilarity-based Framework for Designing Scalable and Efficient DGNN Accelerators"
description: "HPCA 2025 · Traversing Winning Paths"
tags:
  - "HPCA2025"
  - "Traversing Winning Paths"
---

# I-DGNN: A Graph Dissimilarity-based Framework for Designing Scalable and Efficient DGNN Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Traversing Winning Paths。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Traversing Winning Paths</p>
</div>

**论文链接**：
**作者**：Jiaqi Yang (George Washington University), Hao Zheng (University of Central Florida), Ahmed Louri (George Washington University)
**会议**：HPCA 2025

---

## 中文标题

I-DGNN：基于图差异性的可扩展高效 DGNN 加速器设计框架

## 英文摘要

Dynamic Graph Neural Networks (DGNNs) have recently been used in numerous application domains, comprehending the intricate dynamics of time-evolving graph data. Despite their theoretical advancements, effectively implementing scalable DGNNs continues to be a formidable challenge due to the constantly evolving graph data and heterogeneous computation kernels. Recent efforts attempted to either exploit the graph data reuse to reduce memory access or eliminate the redundant computations between consecutive graph snapshots to scale the DGNN acceleration. These efforts are still falling short. In prior work, each graph snapshot, regardless of its size and connectivity, passes through the entire DGNN computation pipeline from layer to layer. Consequently, substantial intermediate data is generated throughout the DGNN computation, which leads to excessive off-chip memory access. To address this crucial challenge, we argue that the computations between evolving graph snapshots should be decoupled from the DGNN execution pipeline. In this paper, we propose I-DGNN, a theoretical, architectural, and algorithmic framework with the aim of designing scalable and efficient accelerators for DGNN execution with improved performance and energy efficiency. On the theory side, the key idea is to identify essential computations between consecutive graph snapshots and encapsulate them as a separate kernel independent from the DGNN model. Specifically, the proposed one-pass DGNN computing model extracts the process of graph update as a chained matrix multiplication between evolving graphs through rigorous mathematical derivations. Consequently, consecutive snapshots utilize a one-pass computation kernel instead of passing through the entire DGNN execution pipeline, thereby eliminating the costly data movement of intermediate results across DGNN layers. On the architecture side, we propose a unified accelerator architecture that can be dynamically configured to support the computation characteristics of the proposed I-DGNN computing model with improved data and pipeline parallelism. On the algorithm side, we propose a new dataflow and mapping tailored for I-DGNN to further improve the data locality of inter-kernel data across the DGNN pipeline. Simulation results show that the proposed accelerator achieves 65.9%, 71.1%, and 58.8% reductions in execution time and 88.4%, 87.0%, and 85.9% improvements in energy efficiency on average across multiple DGNN datasets compared to state-of-the-art accelerators [1]–[3].

## 中文摘要

动态图神经网络（DGNN）近来被用于众多领域，以理解随时间演化的图数据中复杂的动态性。尽管理论上不断进步，但由于图数据持续演化且计算内核异构，高效实现可扩展的 DGNN 仍是艰巨挑战。近期工作或利用图数据复用减少内存访问，或消除相邻快照间的冗余计算，但仍显不足。此前每个图快照无论规模与连通性都逐层通过整个 DGNN 流水线，产生大量中间数据并带来过多片外内存访问。为此我们主张将演化图快照间的计算与 DGNN 执行流水线解耦。本文提出 I-DGNN，一个涵盖理论、架构与算法的框架，用于设计可扩展且高效的 DGNN 加速器。理论上，核心思想是识别相邻快照间的必要计算并封装为独立于 DGNN 模型的内核；所提出的一次性 DGNN 计算模型通过严谨数学推导，将图更新过程提取为演化图之间的链式矩阵乘法。于是相邻快照改用一次性计算内核而非遍历整个 DGNN 流水线，消除了中间结果跨层搬运的高昂数据移动。架构上，我们提出可动态配置的统一加速器架构，以匹配该模型计算特征并提升数据与流水线并行度。算法上，我们提出新的数据流与映射以改善跨内核数据的局部性。模拟结果表明，与最先进加速器 [1]–[3] 相比，所提加速器在多个 DGNN 数据集上平均分别降低 65.9%、71.1% 和 58.8% 的执行时间，并将能效平均分别提升 88.4%、87.0% 和 85.9%。
