---
title: "MeHyper: Accelerating Hypergraph Neural Networks by Exploring Implicit Dataflows"
description: "HPCA 2025 · Traversing Winning Paths"
tags:
  - "HPCA2025"
  - "Traversing Winning Paths"
---

# MeHyper: Accelerating Hypergraph Neural Networks by Exploring Implicit Dataflows

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Traversing Winning Paths。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Traversing Winning Paths</p>
</div>

**论文链接**：
**作者**：Wenju Zhao (Huazhong University of Science and Technology), Pengcheng Yao (Huazhong University of Science and Technology), Dan Chen (National University of Singapore), Long Zheng (Huazhong University of Science and Technology), Xiaofei Liao (Huazhong University of Science and Technology), Qinggang Wang (Huazhong University of Science and Technology), Shaobo Ma (Huazhong University of Science and Technology), Yu Li (Huazhong University of Science and Technology), Haifeng Liu (Huazhong University of Science and Technology), Wenjing Xiao (Guangxi University), Yufei Sun (Huazhong University of Science and Technology), Bing Zhu (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology), Jingling Xue (University of New South Wales)
**会议**：HPCA 2025

---

## 中文标题

MeHyper：挖掘隐式数据流加速超图神经网络

## 英文摘要

Hypergraph Neural Networks (HGNNs) are increasingly utilized to analyze complex inter-entity relationships. Traditional HGNN systems, based on a hyperedge-centric dataflow model, independently process aggregation tasks for hyperedges and vertices, leading to significant computational redundancy. This redundancy arises from recalculating shared information across different tasks. For the first time, we identify and harness implicit dataflows (i.e., dependencies) within HGNNs, introducing the microedge concept to effectively capture and reuse intricate shared information among aggregation tasks, thereby minimizing redundant computations. We have developed a new microedge-centric dataflow model that processes shared information as fine-grained microedge aggregation tasks. This dataflow model is supported by the Read-Process-Activate-Generate execution model, which aims to optimize parallelism among these tasks. Furthermore, our newly developed MeHyper, a microedge-centric HGNN accelerator, incorporates a decoupled pipeline for improved computational parallelism and a hierarchical feature management strategy to reduce off-chip memory accesses for large volumes of intermediate feature vectors generated. Our evaluation demonstrates that MeHyper substantially outperforms the leading CPU-based system PyG-CPU and the GPU-based system HyperGef, delivering performance improvements of 1,032.23× and 10.51×, and energy efficiencies of 1,169.03× and 9.96×, respectively.

## 中文摘要

超图神经网络（HGNN）正日益被用于分析实体间的复杂关系。传统 HGNN 系统基于以超边为中心的数据流模型，独立处理超边与顶点的聚合任务，导致显著的冗余计算。这种冗余源于对不同任务间共享信息的重复计算。我们首次识别并利用了 HGNN 中的隐式数据流（即依赖关系），引入微边概念以有效捕捉并复用聚合任务间复杂的共享信息，从而最小化冗余计算。我们开发了新的以微边为中心的数据流模型，将共享信息处理为细粒度的微边聚合任务。该数据流模型由 Read-Process-Activate-Generate 执行模型支撑，旨在优化这些任务间的并行性。此外，我们新开发的 MeHyper 是一个以微边为中心的 HGNN 加速器，它包含解耦流水线以提升计算并行度，并采用层次化特征管理策略以减少大量生成的中间特征向量带来的片外内存访问。评估表明，MeHyper 大幅优于领先的 CPU 系统 PyG-CPU 与 GPU 系统 HyperGef，性能分别提升 1,032.23 倍和 10.51 倍，能效分别提升 1,169.03 倍和 9.96 倍。
