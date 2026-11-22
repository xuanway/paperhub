---
title: "MOSAIC: An Accelerator Design for Heterophilic Graph Learning"
description: "MICRO 2026 · Session 6C · MOSAIC：面向异配图学习的加速器设计"
tags:
  - "MICRO2026"
  - "Graph Processing"
---

# MOSAIC: An Accelerator Design for Heterophilic Graph Learning

**中文标题：** MOSAIC：面向异配图学习的加速器设计

**所属 Session：** [Session 6C](index.md) · [MICRO 2026](../index.md)

**作者：** Fangzhou Ye, Wei Zhang, Ahmed Louri, Hao Zheng

**来源：** MICRO 2026，pp. 2132–2146；[DOI](https://doi.org/10.1109/MICRO67795.2026.00148)

## 英文摘要

Heterophilic graphs are common in many real-world applications such as protein-protein interaction networks, where connected nodes often have dissimilar features. Traditional Graph Neural Networks (GNNs) operate exclusively on immediate neighbors and extend the receptive field through layer expansion, failing to capture crucial distant relationships and structural information due to the over-smoothing problem. Recent theoretical developments of higher-order GNNs are shifting towards K-hop feature aggregation, where each vertex can simultaneously aggregate information from distant vertices across several hops. Despite their theoretical promise, higher-order GNNs suffer from significant memory bottlenecks and can be up to 100× slower than traditional GNNs. This inefficiency arises primarily from (1) the requirement to maintain separate adjacency matrices for different hop distances (i.e., powers of the adjacency matrix), and (2) redundant computation and memory accesses caused by overlapping paths during multi-hop aggregation. In this paper, we propose a clique-centric accelerator design, called MOSAIC, that aims to decouple the computation and memory overheads of K-hop aggregation from the expanded receptive field. Our key observation is that clique graphs are the primitive components that capture the overlapping paths of distant feature aggregations. Based on the clique structure, we develop a framework to accelerate higher-order GNNs, achieving performance and latency comparable to traditional GNN models. First, we propose a clique-centric dataflow to eliminate the redundant computation and memory access caused by path overlapping due to simultaneous node aggregations with distinct distances. Second, we propose a K-hop degree partitioning algorithm that can incorporate the degree information of the extended receptive field with a balanced workload. Third, we propose a new data representation that can encode the graph connectivity of nodes with different distances, eliminating the need for separate adjacency matrices. Lastly, we propose a novel accelerator architecture to enable clique reuse as opposed to recomputing feature aggregation during concurrent aggregations. Our simulation results show an average speedup of 7.67 times, 6.73 times, and 4.88 times over I-GCN, Betty, and ReGNN for higher-order GNNs, respectively. Meanwhile, MOSAIC achieves energy reduction by 51.78%, 52.53%, and 56.84% on average compared with the baselines.

## 中文摘要

异嗜图在许多现实世界的应用中很常见，例如蛋白质-蛋白质相互作用网络，其中连接的节点通常具有不同的特征。传统的图神经网络（GNN）仅对直接邻居进行操作，并通过层扩展来扩展感受野，由于过度平滑问题而无法捕获关键的远距离关系和结构信息。高阶 GNN 的最新理论发展正在转向 K 跳特征聚合，其中每个顶点可以同时聚合来自多个跳的远距离顶点的信息。尽管理论上有希望，但高阶 GNN 仍面临严重的内存瓶颈，并且速度可能比传统 GNN 慢 100 倍。这种低效率主要源于（1）需要为不同的跳距离维护单独的邻接矩阵（即邻接矩阵的幂），以及（2）多跳聚合期间由重叠路径引起的冗余计算和内存访问。在本文中，我们提出了一种以派系为中心的加速器设计，称为 MOSAIC，旨在将 K 跳聚合的计算和内存开销与扩展的感受野解耦。我们的主要观察是，派图是捕获遥远特征聚合的重叠路径的原始组件。基于派系结构，我们开发了一个框架来加速高阶 GNN，实现与传统 GNN 模型相当的性能和时延。首先，我们提出了一种以派系为中心的数据流，以消除由于具有不同距离的同时节点聚合而导致的路径重叠导致的冗余计算和内存访问。其次，我们提出了一种 K 跳度划分算法，该算法可以在平衡工作负载的情况下结合扩展感受野的度信息。第三，我们提出了一种新的数据表示形式，可以对不同距离的节点的图连接性进行编码，从而消除了对单独邻接矩阵的需要。最后，我们提出了一种新颖的加速器架构，以实现团重用，而不是在并发聚合期间重新计算特征聚合。我们的模拟结果显示，对于高阶 GNN，与 I-GCN、Betty 和 ReGNN 相比，平均加速分别为 7.67 倍、6.73 倍和 4.88 倍。同时，与基线相比，MOSAIC 平均能耗降低了 51.78%、52.53% 和 56.84%。

## 中文关键词

高阶图神经网络；异配图学习；多跳聚合；加速器

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6C](index.md) · [MICRO 2026 主页](../index.md)
