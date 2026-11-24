---
title: "Cascade: A Dependency-aware Efficient Training Framework for Temporal Graph Neural Network"
description: "ASPLOS 2025 · Session 8A · Cascade：面向时序图神经网络的依赖感知高效训练框架"
tags:
  - "ASPLOS2025"
  - "Session 8A"
  - "ML Training"
---

# Cascade: A Dependency-aware Efficient Training Framework for Temporal Graph Neural Network

**中文标题：** Cascade：面向时序图神经网络的依赖感知高效训练框架

**所属 Session：** [Session 8A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yue Dai (Department of Computer Science, University of Pittsburgh), Xulong Tang (Department of Computer Science, University of Pittsburgh), Youtao Zhang (Department of Computer Science, University of Pittsburgh)

**单位：** Department of Computer Science, University of Pittsburgh

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716250) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Temporal graph neural networks (TGNN) have gained significant momentum in many real-world dynamic graph tasks. These models use graph changes (i.e., events) as inputs to update nodes' status vectors (i.e., memories), which are then exploited to assist predictions. Despite their improved accuracies, the efficiency of TGNN training is significantly limited due to the inherent temporal relationship between the input events. Although larger training batches can improve parallelism and speed up TGNN training, they lead to infrequent memory updates, which cause outdated information and reduced accuracy. This trade-off forces current methods to use small batches, resulting in high latency and underutilized hardware. To address this, we propose an efficient TGNN training framework, Cascade, to adaptively boost TGNN training parallelism based on nodes' spatial and temporal dependencies. Cascade adopts a topology-aware scheduler that includes as many spatial-independent events in the same batches. Moreover, it leverages node memories' similarities to break temporal dependencies on stabilized nodes, enabling it to pack more temporal-independent events in the same batches. Additionally, Cascade adaptively decides nodes' update frequencies based on runtime feedback. Compared to prior state-of-the-art TGNN training frameworks, our approach can averagely achieve 2.3× (up to 5.1×) speed up without jeopardizing the resulted models' accuracy.

## 中文摘要

时序图神经网络（TGNN）在许多真实世界的动态图任务中已获得显著发展。这类模型以图的变化（即事件）作为输入来更新节点的状态向量（即记忆），随后利用这些记忆辅助预测。尽管其精度有所提升，但由于输入事件之间固有的时序关系，TGNN 训练的效率显著受限。增大训练批次可以提升并行度并加速 TGNN 训练，但这会导致记忆更新不频繁，从而引入过时信息并降低精度。这种权衡迫使现有方法使用小批次，结果造成高时延与硬件利用率不足。为解决该问题，我们提出一种高效的 TGNN 训练框架 Cascade，它基于节点的空间与时间依赖关系自适应地提升 TGNN 训练的并行度。Cascade 采用拓扑感知的调度器，将尽可能多的空间无关事件纳入同一批次。此外，它利用节点记忆之间的相似性来打破已稳定节点上的时间依赖，从而能够在同一批次中打包更多时间无关事件。另外，Cascade 基于运行时反馈自适应地决定节点的更新频率。与先前最先进的 TGNN 训练框架相比，我们的方法在不损害所得模型精度的前提下，平均可实现 2.3×（最高 5.1×）的加速。

## 英文关键词

Temporal Graph Neural Network, Dynamic Graph, Efficient Deep Learning, Parallel Computing

## 中文关键词

时序图神经网络；动态图；高效深度学习；并行计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716250)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8A](index.md) · [返回 ASPLOS 2025](../index.md)
