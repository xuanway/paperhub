---
title: "Mithril: A Scalable System for Deep GNN Training"
description: "HPCA 2025 · Traversing Winning Paths"
tags:
  - "HPCA2025"
  - "Traversing Winning Paths"
---

# Mithril: A Scalable System for Deep GNN Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Traversing Winning Paths。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Traversing Winning Paths</p>
</div>

**论文链接**：
**作者**：Jingji Chen (Purdue University), Zhuoming Chen (Carnegie Mellon University), Xuehai Qian (Tsinghua University)
**会议**：HPCA 2025

---

## 中文标题

Mithril：面向深度 GNN 训练的可扩展系统

## 英文摘要

Communication is a key bottleneck for distributed graph neural network (GNN) training. Existing GNN training systems fail to scale to deep GNNs because of the tremendous amount of inter-GPU communication. This paper proposes Mithril, a new approach that significantly scales the distributed full-graph deep GNN training. Being the first to use layer-level model parallelism for GNN training, Mithril partitions GNN layers among GPUs, each device performs the computation for a disjoint subset of consecutive GNN layers on the whole graph. Compared to graph parallelism with each GPU handling a graph partition, Mithril reduces the communication volume by a factor of the number of GNN layers to scale to deep models. Mithril overcomes the unique challenges for pipelined layer-level model parallelism on the whole graph by partitioning it into dependent chunks, breaking the dependencies with embedding speculation, and applying specific training techniques to ensure convergence. We also propose a hybrid approach by combining Mithril with graph parallelism to handle large graphs, achieve better computer resource utilization and ensure model convergence. We build a general GNN training system supporting all three parallelism settings. Extensive experiments show that Mithril reduces the per-epoch communication volume by up to 22.89× (on average 6.78×). It achieves a maximum training time speedup of 2.34× (on average 1.49×) on a GPU cluster with a high-performance InfiniBand network. On another cluster with a commodity Ethernet, Mithril outperforms the baseline by up to 10.21× (on average 7.16×). Mithril also achieves a comparable level of model accuracy and convergence speed compared to graph parallelism.

## 中文摘要

通信是分布式图神经网络（GNN）训练的关键瓶颈。现有 GNN 训练系统因 GPU 间通信量巨大而无法扩展到深层 GNN。本文提出 Mithril，一种能显著扩展分布式全图深度 GNN 训练的新方法。Mithril 首次将层级模型并行用于 GNN 训练，它把 GNN 层划分到多个 GPU 上，每个设备在整个图上对互不相交的连续 GNN 层子集进行计算。与每个 GPU 处理一个图分区的图并行相比，Mithril 把通信量降低为原来的 1/GNN 层数，从而可扩展到深层模型。为克服整图上流水线式层级模型并行特有的挑战，Mithril 将图划分为相互依赖的块，用嵌入推测打破依赖关系，并采用特定训练技术保证收敛。我们还提出将 Mithril 与图并行结合的混合方法，以处理大图、获得更好的计算资源利用率并确保模型收敛。我们构建了支持全部三种并行设置的通用 GNN 训练系统。大量实验表明，Mithril 将每轮通信量最多降低 22.89 倍（平均 6.78 倍）。在具有高性能 InfiniBand 网络的 GPU 集群上，它实现最高 2.34 倍（平均 1.49 倍）的训练时间加速比。在另一个采用商用以太网的集群上，Mithril 最多优于基线 10.21 倍（平均 7.16 倍）。与图并行相比，Mithril 还达到相当的模型精度与收敛速度。
