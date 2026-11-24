---
title: "DiTile-DGNN: An Efficient Accelerator for Distributed Dynamic Graph Neural Network Inference"
description: "ISCA 2025 · Session 7A · DiTile-DGNN：面向分布式动态图神经网络推理的高效加速器"
tags:
  - "ISCA2025"
  - "Session 7A"
  - "ML Acceleration III"
---

# DiTile-DGNN: An Efficient Accelerator for Distributed Dynamic Graph Neural Network Inference

**中文标题：** DiTile-DGNN：面向分布式动态图神经网络推理的高效加速器

**所属 Session：** [Session 7A](index.md) · [ISCA 2025](../index.md)

**作者：** Jiaqi Yang, Hao Zheng, Ahmed Louri

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731017) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Dynamic Graph Neural Networks (DGNNs) have recently emerged as a promising model for learning complex temporal and spatial relationships in evolving graphs. The performance of DGNNs is enabled by the simultaneous integration of both graph neural net- works (GNNs) and recurrent neural networks (RNNs). Despite the theoretical advancements, the design space of such complex mod- els has significantly exploded due to the combinatorial challenges of heterogeneous computation kernels and intricate data depen- dency (i.e., intra- and inter-snapshot data dependency). This makes the computations of DGNN hard to scale, posing significant chal- lenges in parallelism, data reuse, and communication. To address this challenge, we propose DiTile-DGNN, an efficient accelerator for large-scale DGNN execution. The proposed DiTile-DGNN con- sists of a redundancy-free parallelism strategy, workload balance optimization, and a reconfigurable accelerator architecture. Specifi- cally, we propose a redundancy-free framework that can efficiently find an efficient parallelism strategy that can fully eliminate the data redundancy between graph snapshots while minimizing the communication complexity. Additionally, we propose a workload balance optimization for DGNN models to enhance resource utiliza- tion and eliminate synchronization overhead between snapshots. Lastly, we propose a reconfigurable accelerator architecture, with a flexible interconnect, that can be dynamically configured in sup- port of various DGNN dataflows. Our simulations demonstrate that DiTile-DGNN achieves 48.4%, 56.1%, 23.2%, and 36.1% reductions in execution time and 83.4%, 84.0%, 75.6%, and 71.4% improvements in energy efficiency compared to state-of-the-art accelerators, includ- ing ReaDy [20], DGNN-Booster [8], RACE [51], and MEGA [12], on average across multiple DGNN datasets.

## 中文摘要

动态图神经网络（DGNN）是当下热门模型，用于在演化图上学习复杂的时空关联。DGNN同时融合图神经网络（GNN）与循环神经网络（RNN）来实现计算。虽然理论上取得进展，但这类复杂模型的设计空间急剧膨胀：异构计算核组合、复杂的数据依赖（快照内、快照间依赖）带来巨大挑战，导致DGNN计算难以扩展，在并行挖掘、数据复用、通信开销上存在瓶颈。

针对该问题，本文提出DiTile-DGNN，面向大规模DGNN推理的高效加速器。DiTile-DGNN包含无冗余并行策略、负载均衡优化以及一套可重构加速器架构。首先，本文提出无冗余框架，寻找高效并行方案，消除图快照之间的数据冗余，同时降低通信复杂度；其次，针对DGNN做负载均衡优化，提升资源利用率，消除快照之间的同步开销；最后，设计带灵活互联的可重构加速器，支持动态切换，适配多种DGNN数据流。

仿真结果表明：在多个DGNN数据集上，对比前沿加速器ReaDy、DGNN-Booster、RACE、MEGA，DiTile-DGNN平均执行时间分别降低48.4%、56.1%、23.2%、36.1%；能效分别提升83.4%、84.0%、75.6%、71.4%。

## 英文关键词

Dynamic graph neural networks, distributed inference, accelerator, tiling

## 中文关键词

动态图神经网络, 分布式推理, 数据复用

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731017)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2025](../index.md)
