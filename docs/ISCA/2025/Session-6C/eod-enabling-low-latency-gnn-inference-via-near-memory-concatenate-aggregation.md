---
title: "EOD: Enabling Low Latency GNN Inference via Near-Memory Concatenate Aggregation"
description: "ISCA 2025 · Session 6C · EOD: 通过近存合并聚合实现低延迟GNN推理"
tags:
  - "ISCA2025"
  - "Session 6C"
  - "Memory Acceleration"
---

# EOD: Enabling Low Latency GNN Inference via Near-Memory Concatenate Aggregation

**中文标题：** EOD: 通过近存合并聚合实现低延迟GNN推理

**所属 Session：** [Session 6C](index.md) · [ISCA 2025](../index.md)

**作者：** Taehwan Kim, Yunki Han, Seohye Ha, Jiwan Kim, Lee-Sup Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731083) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

As online services based on graph databases increasingly integrate with machine learning, serving low-latency Graph Neural Network (GNN) inference for individual requests has become a critical chal- lenge. Real-time GNN inference services operate in an inductive setup, which can handle newly added, previously unseen nodes and their edges. In this setup, the system must prepare the computa- tional graph and input node features for target nodes, followed by GNN inference using the given input data. However, the workflow of a GNN serving system presents two key challenges that hinder low-latency inference. The first challenge arises from the extensive preparation step, which involves heavy memory access in host memory and significant data I/O to devices, constituting the largest portion of end-to-end inference latency. The second challenge is the well-known neighborhood explosion problem in GNN research. As the receptive field for target nodes increases exponentially with the number of layers, this issue exacerbates overall latency. To address these challenges, we propose a Near-Memory Process- ing (NMP) based low-latency GNN inference serving system named EOD. To ensure low-latency real-time GNN service, we co-design the algorithm and hardware to tackle the aforementioned issues. First, to mitigate the neighborhood explosion problem, we pro- pose a precomputation method for the training node set, reducing memory access and computational complexity from exponential to linear growth. Additionally, we introduce a concatenated ZVC com- pression method to minimize the overhead of storing precomputed hidden features. Finally, to alleviate heavy host-side memory access and data I/O, we design an NMP architecture that enables efficient aggregation on concatenated ZVC-compressed data. As a result, EOD achieves a geometric mean of 981.1×and 912.0×aggregation speedup over the baseline and the existing architecture for GNN aggregation. Additionally, EOD achieves a geometric mean of 17.9×, and up to 74.3×end-to-end latency speedup over the GPU baseline.

## 中文摘要

随着基于图数据库的在线服务越来越多地融合机器学习，为单请求提供低延迟的图神经网络（GNN）推理服务成为一项关键难题。实时GNN推理服务采用归纳式场景设置，能够处理新增、训练时未见过的节点及其边。在该场景下，系统需要为目标节点构建计算图、准备输入节点特征，再基于这些输入执行GNN推理。但GNN服务流程存在两大阻碍低延迟推理的痛点：第一，图准备阶段开销巨大，主机内存访存密集、主机到设备的数据I/O量大，占据端到端推理延迟的主要部分；第二，是GNN领域熟知的邻域爆炸问题：目标节点的感受野随网络层数指数增长，进一步推高整体延迟。

针对上述问题，本文提出基于近内存处理（NMP）的低延迟GNN推理服务系统EOD。本文通过算法硬件协同设计实现低延迟实时GNN服务：首先，针对邻域爆炸问题，提出训练集节点预计算方案，将访存与计算复杂度从指数增长降至线性增长；其次，提出拼接式ZVC压缩方法，降低预计算隐特征的存储开销；最后，为缓解主机侧繁重访存与数据I/O，设计NMP架构，直接在经过ZVC压缩拼接的数据上高效完成聚合运算。实验结果表明：在GNN聚合算子上，EOD相比基线架构与已有架构，几何平均提速分别达到981.1倍和912.0倍；端到端延迟相比GPU基线几何平均提速17.9倍，最高可达74.3倍。

## 英文关键词

Graph Neural Network, Near-Memory Processing, ML Acceleration, Data Compression, Real-time service

## 中文关键词

图神经网络, 近内存处理, 机器学习加速, 数据压缩, 实时服务

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731083)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2025](../index.md)
