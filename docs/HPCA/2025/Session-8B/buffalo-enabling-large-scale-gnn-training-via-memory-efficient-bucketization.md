---
title: "Buffalo: Enabling Large-Scale GNN Training via Memory-Efficient Bucketization"
description: "HPCA 2025 · Traversing Winning Paths"
tags:
  - "HPCA2025"
  - "Traversing Winning Paths"
---

# Buffalo: Enabling Large-Scale GNN Training via Memory-Efficient Bucketization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Traversing Winning Paths。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Traversing Winning Paths</p>
</div>

**论文链接**：
**作者**：Shuangyan Yang (University of California, Merced), Minjia Zhang (University of Illinois Urbana-Champaign), Dong Li (University of California, Merced)
**会议**：HPCA 2025

---

## 中文标题

Buffalo：通过内存高效的分桶实现大规模 GNN 训练

## 英文摘要

Graph Neural Networks (GNNs) have demonstrated outstanding results in many graph-based deep-learning tasks. However, training GNNs on a large graph can be difficult due to memory capacity limitations. To address this problem, we can divide the graph into multiple partitions. However, this strategy faces a memory explosion problem. This problem stems from a long tail in the degree distribution of graph nodes. This strategy also suffers from time-consuming graph partitioning, difficulty in estimating the memory consumption of each partition, and time-consuming data preparation (e.g., block generation). To address the above problems, we introduce Buffalo, a GNN training system. Buffalo enables flexible mapping between the nodes and partitions to address the memory explosion problem, and enables fast graph partitioning based on node bucketing. Buffalo also introduces lightweight analytical modeling for memory estimation, and reduces block generation time by leveraging graph sampling. Evaluating large-scale real-world datasets (including billion-scale datasets), we show that Buffalo effectively addresses the memory capacity limitation, enabling scalable GNN training and outperforming prior works in the compute-vs-memory efficiency Pareto frontier. With a limited memory budget, Buffalo achieves an end-to-end reduction of training time by 70.9% on average, compared to state-of-the-art (DGL [73], PyG [12], and Betty [93]).

## 中文摘要

图神经网络（GNN）在许多基于图的深度学习任务上取得了出色结果。然而受内存容量限制，在大图上训练 GNN 可能十分困难。为解决该问题，我们可以将图划分为多个分区。但这一策略面临内存爆炸问题，其根源在于图节点度分布中的长尾。该策略还存在图划分耗时、难以估计各分区内存消耗以及数据准备（如块生成）耗时等问题。针对上述问题，我们提出 Buffalo，一个 GNN 训练系统。Buffalo 通过支持节点与分区之间的灵活映射来解决内存爆炸问题，并基于节点分桶实现快速图划分。Buffalo 还引入轻量级解析建模进行内存估计，并利用图采样缩短块生成时间。在大规模真实数据集（包括十亿级数据集）上的评估表明，Buffalo 有效解决了内存容量限制，实现了可扩展的 GNN 训练，并在计算与内存效率的帕累托前沿上优于先前工作。在有限内存预算下，与最先进方案（DGL [73]、PyG [12] 和 Betty [93]）相比，Buffalo 端到端平均降低 70.9% 的训练时间。
