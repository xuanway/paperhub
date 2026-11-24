---
title: "TAGT: An Efficient Graph Transformer Accelerator with Topology-aware Sparsification and Merging"
description: "ISCA 2026 · Session 10D · TAGT: An Efficient Graph Transformer Accelerator with Topology-aware Sparsification and Merging"
tags:
  - "ISCA2026"
  - "Session 10D"
  - "Domain Specific Accelerators 3"
---

# TAGT: An Efficient Graph Transformer Accelerator with Topology-aware Sparsification and Merging

**中文标题：** TAGT: 基于拓扑感知稀疏化与合并的高效图 Transformer 加速器

**所属 Session：** [Session 10D](index.md) · [ISCA 2026](../index.md)

**作者：** Hui Yu, Wei Zhang, Ligang He, Jin Zhao, Yu Zhang, Zixiao Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Graph Transformers (GTs) have emerged as a powerful paradigm for graph representation learning, as their attention mechanism can capture long-range dependencies and model complex structural interactions beyond the local message-passing scope of conventional Graph Neural Networks (GNNs). This capability has enabled GTs to achieve strong accuracy across important domains, including recommendation systems and VLSI congestion prediction. However, the global attention mechanism in GTs requires each vertex to attend to all other vertices, incurring O(N 2) computation and intermediate data movement. As graph size increases, this quadratic complexity leads to prohibitive computational overhead and excessive off-chip memory traffic, fundamentally limiting the scalability and efficiency of GT execution. In this paper, we propose TAGT, the first efficient topology-aware Graph Transformer accelerator designed to mitigate these performance bottlenecks. Specifically, we integrate a topology-aware sparsification and merging approach into the accelerator design that dramatically reduces the O(N 2) complexity. TAGT introduces a structure-aware sparse subgraph, termed the Topology Dependency Subgraph (TDS), which exploits inherent topological dependencies and reduces the number of attended edges to O(N log N) on average. The TDS is designed to retain local neighborhood structure while capturing essential higher-order interrelationships. By performing attention on the TDS, TAGT approximates global attention over the entire graph with negligible accuracy loss while eliminating most unnecessary computations and off-chip data movements. To fully harness the performance potential of this approach, TAGT incorporates a data-driven loading and merging engine to minimize off-chip memory accesses and reduce TDS construction overhead on the fly. TAGT also introduces a TDS-based fast attention unit to improve the parallelism of attention computation. We implement and evaluate TAGT on a Xilinx Alveo U280 FPGA card. Experimental results show that TAGT achieves average speedups of 175.4× and 18.6×, together with energy savings of 217.2× and 24.8×, over state-of-the-art software GT solutions on Intel Xeon CPUs and NVIDIA A100 GPUs, respectively. Compared with representative GNN accelerators, including FlowGNN, MEGA, and BingoGCN, TAGT delivers average speedups of 8.2×, 6.9×, and 4.7×, and energy savings of 9.3×, 7.5×, and 5.2×, respectively.

## 中文摘要

图 Transformer（GT）已成为图表示学习的一种强大范式，因为其注意力机制能够捕捉长程依赖，并建模超越传统图神经网络（GNN）局部消息传递范围的复杂结构交互。这一能力使 GT 在推荐系统和 VLSI 拥塞预测等重要领域取得了很强的准确率。然而，GT 中的全局注意力机制要求每个顶点关注所有其他顶点，带来 O(N 2) 的计算量与中间数据搬移。随着图规模增长，这种二次复杂度导致高昂的计算开销和过多的片外访存流量，从根本上限制了 GT 执行的可扩展性与效率。本文提出 TAGT，首个高效的拓扑感知图 Transformer 加速器，旨在缓解这些性能瓶颈。具体而言，我们将拓扑感知的稀疏化与合并方法集成到加速器设计中，大幅降低 O(N 2) 复杂度。TAGT 引入一种结构感知的稀疏子图，称为拓扑依赖子图（TDS），它利用固有的拓扑依赖关系，将参与注意力的边数平均降至 O(N log N)。TDS 旨在保留局部邻域结构，同时捕捉必要的高阶相互关系。通过在 TDS 上执行注意力，TAGT 以可忽略的精度损失近似全图上的全局注意力，同时消除大部分不必要的计算和片外数据搬移。为充分挖掘该方法的性能潜力，TAGT 集成了一个数据驱动的加载与合并引擎，以最小化片外内存访问并即时降低 TDS 构建开销。TAGT 还引入基于 TDS 的快速注意力单元，以提升注意力计算的并行度。我们在 Xilinx Alveo U280 FPGA 卡上实现并评估了 TAGT。实验结果表明，与 Intel Xeon CPU 和 NVIDIA A100 GPU 上的最先进软件 GT 方案相比，TAGT 分别实现 175.4× 和 18.6× 的平均加速，以及 217.2× 和 24.8× 的能耗节省。与代表性 GNN 加速器（包括 FlowGNN、MEGA 和 BingoGCN）相比，TAGT 分别带来 8.2×、6.9×、4.7× 的平均加速和 9.3×、7.5×、5.2× 的能耗节省。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10D](index.md) · [返回 ISCA 2026](../index.md)
