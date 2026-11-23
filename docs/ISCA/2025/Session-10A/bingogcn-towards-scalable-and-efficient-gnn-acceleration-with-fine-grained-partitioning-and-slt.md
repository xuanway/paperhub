---
title: "BingoGCN: Towards Scalable and Efficient GNN Acceleration with Fine-Grained Partitioning and SLT"
description: "ISCA 2025 · Session 10A · BingoGCN: 细粒度分区与SLT实现可扩展高效GNN加速"
tags:
  - "ISCA2025"
  - "Session 10A"
  - "ML Accelerators IV"
---

# BingoGCN: Towards Scalable and Efficient GNN Acceleration with Fine-Grained Partitioning and SLT

**中文标题：** BingoGCN: 细粒度分区与SLT实现可扩展高效GNN加速

**所属 Session：** [Session 10A](index.md) · [ISCA 2025](../index.md)

**作者：** Jiale Yan, Hiroaki Ito, Yuta Nagahara, Kazushi Kawamura, Masato Motomura, Thiem Van Chu, Daichi Fujiki

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731115) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Graph Neural Networks (GNNs) are increasingly popular due to their wide applicability to tasks requiring the understanding of unstructured graph data, such as those in social network analy- sis and autonomous driving. However, real-time, large-scale GNN inference faces challenges due to the large size of node features and adjacency matrices, leading to memory communication and buffer size overheads caused by irregular memory access patterns. While graph partitioning can help with localized access patterns and reduction in on-chip buffer size, fine-grained partitioning results in increased inter-partition edges and off-chip memory accesses, negatively impacting overall performance. To overcome these limitations, we propose BingoGCN, a scalable GNN acceleration framework that introduces multidimensional dynamic feature summarization called Cross-Partition Message Quantization (CMQ) for inter-partition message passing. This elim- inates irregular off-chip memory access without additional training and accuracy loss, even with fine-grained partitioning. By shifting the bottleneck from memory to computation, BingoGCN allows for further performance optimization through the Strong Lottery Ticket (SLT) theory using randomly generated weights. BingoGCN addresses the challenge of SLT’s unstructured sparsity in hardware acceleration with a novel training algorithm and random weight generator designs, enabling fine-grained (FG) sparsity and improved load balancing. We integrated CMQ and FG-SLT into the message- passing of GNNs and designed an efficient hardware architecture to support this flow. Our FPGA-based implementation achieves a sig- nificant reduction in memory accesses while preserving accuracy comparable to the original models.

## 中文摘要

图神经网络（GNN）应用广泛，在社交网络分析、自动驾驶等需要理解非结构化图数据的任务中得到越来越多使用。但大规模GNN实时推理面临难题：节点特征与邻接矩阵体量庞大，不规则访存模式带来巨大的存储通信开销与缓存压力。图划分可以改善访问局部性、减小片上缓存容量需求；但细粒度划分会增加跨分区边数量，引发更多片外访存，反而拖累整体性能。

针对上述问题，本文提出BingoGCN，一种可扩展的GNN加速框架。它引入多维动态特征汇总机制——**跨分区消息量化（CMQ）**，用于跨分区消息传递。该方法在细粒度划分下，依然可以消除不规则的片外访存，且无需额外训练、不会损失精度。
该设计把性能瓶颈从访存转移到计算端，进而借助强彩票票（SLT）理论，利用随机权重进一步优化性能。SLT本身的非结构化稀疏特性不利于硬件加速，本文配套设计全新训练算法与随机权重生成器，支持细粒度稀疏并改善负载均衡。我们将CMQ与细粒度SLT（FG-SLT）融入GNN消息传递流程，并搭建高效硬件架构支撑该流水线。基于FPGA的实现能够大幅减少访存次数，同时保持与原始模型相当的精度。

## 英文关键词

Graph neural networks, Computer architecture, Hardware acceler- ators, Quantization

## 中文关键词

图神经网络, 计算机体系结构, 硬件加速器, 量化

## 代码与研究制品

- [代码仓库](https://github.com/LouiValley/BingoGCN)
- [研究制品](https://doi.org/10.5281/zenodo.15104938)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731115)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2025](../index.md)
