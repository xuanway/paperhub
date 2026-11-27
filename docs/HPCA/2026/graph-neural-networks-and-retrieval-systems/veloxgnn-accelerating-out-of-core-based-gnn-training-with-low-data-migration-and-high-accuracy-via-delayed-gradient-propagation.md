---
title: "VeloxGNN: Accelerating Out-of-Core based GNN Training with Low Data Migration and High Accuracy via Delayed Gradient Propagation"
description: "HPCA 2026 · Graph Neural Networks and Retrieval Systems"
tags:
  - "HPCA2026"
  - "Graph Neural Networks and Retrieval Systems"
---

# VeloxGNN: Accelerating Out-of-Core based GNN Training with Low Data Migration and High Accuracy via Delayed Gradient Propagation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Graph Neural Networks and Retrieval Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Graph Neural Networks and Retrieval Systems</p>
</div>

**论文链接**：
**作者**：Yi Li University of Texas at Dallas , Tsun-Yu Yang Center for Computational Evolutionary Intelligence, Electrical & Computer Engineering, Duke University , Zhaoyan Shen Shandong University , Ming-Chang Yang The Chinese University of Hong Kong (CUHK) , Bingzhe Li University of Texas at Dallas
**会议**：HPCA 2026

---

## 中文标题

VeloxGNN：通过延迟梯度传播以低数据迁移和高精度加速外存 GNN 训练

## 英文摘要

Training Graph Neural Networks (GNNs) on large-scale data is essential in various applications, e.g., transportation, and molecular biology. As graph sizes increasingly surpass main memory capacities, the out-of-core (OOC) GNN training system (OOC-based) has been proposed, a scheme that storing graphs on external storage, such as SSD or HDD, sequentially loading and processing smaller partitions. However, existing OOC-based systems face the key challenges: excessive data migration between storage and memory, as well as reduced model accuracy. In this paper, we theoretically and empirically analyze the limitations of state-of-the-art OOC-based systems and identify opportunities for optimization. Guided by our theoretical insights, we propose VeloxGNN, a novel system to improve data migration efficiency while maintaining high model accuracy. First, we introduce a novel algorithm, named Delayed Gradient Propagation (DGP), which specifically designed for OOC-based system. DGP leverages both historical node embeddings and unbiased gradients to achieve two key objectives simultaneously: minimizing the data migration (by ensuring that dataset is read at most once) while maintaining model accuracy. To support DGP, we then propose system-level optimizations: dynamic memory management, DGP-aware loading order, and a new graph partitioning method that separates labeled and unlabeled data. Experimental results show that VeloxGNN achieves memory-based accuracy while reducing training time by 17.7% to 73.3% across various datasets and GNN models, outperforming state-of-the-art methods. This result highlights VeloxGNN’s potential for efficient and scalable GNN training on large-scale graph data.

## 中文摘要

在大规模数据上训练图神经网络（GNN）在交通、分子生物学等应用中至关重要。随着图规模日益超过主存容量，外存（OOC）GNN 训练系统被提出：将图存放在 SSD 或 HDD 等外部存储上，顺序加载并处理较小的分区。然而，现有 OOC 系统面临关键挑战：存储与内存之间过量的数据迁移，以及模型精度下降。本文从理论上和实验上分析了最先进 OOC 系统的局限，并识别出优化机会。在理论洞见的指导下，我们提出 VeloxGNN，一种在保持高模型精度的同时提升数据迁移效率的新系统。首先，我们引入一种为 OOC 系统专门设计的新算法——延迟梯度传播（DGP），它同时利用历史节点嵌入与无偏梯度来实现两个目标：在保证数据集最多只被读取一次从而最小化数据迁移的同时保持模型精度。为支撑 DGP，我们进一步提出系统级优化：动态内存管理、DGP 感知的加载顺序，以及一种将带标签与无标签数据分离的新图划分方法。实验结果表明，VeloxGNN 在多种数据集与 GNN 模型上达到基于内存训练的精度，同时将训练时间缩短 17.7% 至 73.3%，优于最先进方法。这一结果凸显了 VeloxGNN 在大规模图数据上高效可扩展 GNN 训练的潜力。
