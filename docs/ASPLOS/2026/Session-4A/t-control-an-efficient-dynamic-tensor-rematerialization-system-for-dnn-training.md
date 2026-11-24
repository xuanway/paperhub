---
title: "T-Control: An Efficient Dynamic Tensor Rematerialization System for DNN Training"
description: "ASPLOS 2026 · Session 4A · T-Control：一个面向 DNN 训练的高效动态张量重计算系统"
tags:
  - "ASPLOS2026"
  - "Session 4A"
  - "ML Training & Monitoring"
---

# T-Control: An Efficient Dynamic Tensor Rematerialization System for DNN Training

**中文标题：** T-Control：一个面向 DNN 训练的高效动态张量重计算系统

**所属 Session：** [Session 4A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zehua Wang (Institute of Computing Technology, Chinese Academy of Sciences), Junmin Xiao (Institute of Computing Technology, Chinese Academy of Sciences), Xiaochuan Deng (Institute of Computing Technology, Chinese Academy of Sciences), Huibing Wang (Institute of Computing Technology, Chinese Academy of Sciences), Hui Ma (Institute of Computing Technology, Chinese Academy of Sciences), Mingyi Li (Institute of Computing Technology, Chinese Academy of Sciences), Yunfei Pang (Institute of Computing Technology, Chinese Academy of Sciences), Guangming Tan (Institute of Computing Technology, Chinese Academy of Sciences)

**单位：** Institute of Computing Technology, Chinese Academy of Sciences

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790230) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

With the continuous growth of model and batch sizes, DNN model training increasingly suffers from excessive memory consumption. Tensor rematerialization has emerged as an effective technique to enable training under limited memory constraints. However, dynamic rematerialization methods often underperform static approaches, primarily due to their greedy tensor eviction schedules and runtime overhead. In this work, we develop T-Control, a dynamic tensor rematerialization system for DNN model training. T-Control integrates the topology of the traced tensor dependency graph with real-time memory usage to make informed, adaptive tensor retention decisions, preserving critical tensors and reducing eviction-induced recomputation. Furthermore, by extending PyTorch's native memory manager with our fine-grained memory management strategy, T-control effectively improves memory utilization, thereby reducing unnecessary tensor eviction. Experimental results demonstrate that TControl boosts throughput by up to 1.58× and 1.91× over state-of-the-art static and dynamic tensor rematerialization systems.

## 中文摘要

随着模型规模和批量大小的持续增长，DNN 模型训练日益受到内存消耗过大的困扰。张量重计算已成为一种在有限内存约束下实现训练的有效技术。然而，动态重计算方法往往表现不如静态方法，主要原因在于其贪心的张量驱逐调度以及运行时开销。在本工作中，我们开发了 T-Control，一个面向 DNN 模型训练的动态张量重计算系统。T-Control 将被追踪的张量依赖图拓扑与实时内存使用情况相结合，以做出有充分依据的、自适应的张量保留决策，从而保留关键张量并减少驱逐所引发的重计算。此外，通过以我们的细粒度内存管理策略扩展 PyTorch 的原生内存管理器，T-control 有效提升了内存利用率，从而减少了不必要的张量驱逐。实验结果表明，TControl 相较于最先进的静态与动态张量重计算系统，将吞吐分别提升最高 1.58× 和 1.91×。

## 英文关键词

Tensor Rematerialization; Memory Management; GPU; Deep Learning

## 中文关键词

张量重计算；内存管理；GPU；深度学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790230)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4A](index.md) · [返回 ASPLOS 2026](../index.md)
