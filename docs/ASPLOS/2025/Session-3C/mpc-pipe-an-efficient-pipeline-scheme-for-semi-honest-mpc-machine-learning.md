---
title: "MPC-Pipe: an Efficient Pipeline Scheme for Semi-honest MPC Machine Learning"
description: "ASPLOS 2025 · Session 3C · MPC-Pipe：面向半诚实 MPC 机器学习的高效流水线方案"
tags:
  - "ASPLOS2025"
  - "Session 3C"
  - "ML Security"
---

# MPC-Pipe: an Efficient Pipeline Scheme for Semi-honest MPC Machine Learning

**中文标题：** MPC-Pipe：面向半诚实 MPC 机器学习的高效流水线方案

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yongqin Wang (Department of Electrical & Computer Engineering, University of Southern California), Rachit Rajat (Department of Electrical & Computer Engineering, University of Southern California), Murali Annavaram (Department of Electrical & Computer Engineering, University of Southern California)

**单位：** Department of Electrical & Computer Engineering, University of Southern California

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674175) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Multi-party computing (MPC) has been gaining popularity as a secure computing model over the past few years. However, prior works have demonstrated that MPC protocols still pay substantial performance penalties compared to plaintext, particularly when applied to ML algorithms. The overhead is due to added computation and communication costs. Prior studies, as well as our own analysis, found that most MPC protocols today sequentially perform communication and computation. The participating parties must compute on their shares first and then perform data communication to allow the distribution of new secret shares before proceeding to the next computation step. In this work, we show that serialization is unnecessary, particularly in the context of ML computations (both in Convolutional neural networks and in Transformer-based models). We demonstrate that it is possible to carefully orchestrate the computation and communication steps to overlap. We propose MPC-Pipe, an efficient MPC system for both training and inference of ML workloads, which pipelines computations and communications in an MPC protocol during the online phase. MPC-Pipe proposes three pipeline schemes to optimize the online phase of ML in the semihonest majority adversary setting. The three pipeline schemes are 1) inter-linear pipeline, 2) inner-layer pipeline, and 3) inter-batch pipeline. Inter-linear pipeline focuses on linear layers; inner-layer pipeline focuses on non-linear layers; inter-batch pipeline focuses on communication and computation overlaps in different input batches. We implement MPC-Pipe by augmenting a modified version of CrypTen, which separates online and offline phases. We evaluate the end-to-end system performance benefits of the online phase of MPC using deep neural networks (VGG16, ResNet50) and Transformers using different network settings. We show that ML workloads.

## 中文摘要

过去几年，多方计算（MPC）作为一种安全计算模型日益流行。然而，先前的工作已经表明，MPC 协议相比明文仍然要付出可观的性能代价，尤其是在应用于 ML 算法时。这种开销源于额外的计算与通信成本。先前的研究以及我们自己的分析发现，如今大多数 MPC 协议按顺序执行通信与计算。参与各方必须先在各自的份额上进行计算，然后进行数据通信以分发新的秘密份额，之后才能进入下一个计算步骤。在本工作中，我们表明这种串行化是不必要的，尤其是在 ML 计算场景中（无论是卷积神经网络还是基于 Transformer 的模型）。我们证明，可以精心编排计算与通信步骤使其相互重叠。我们提出 MPC-Pipe，一个面向 ML 工作负载训练与推理的高效 MPC 系统，它在在线阶段对 MPC 协议中的计算与通信进行流水化处理。MPC-Pipe 提出三种流水线方案来优化半诚实多数敌手设定下 ML 的在线阶段。这三种流水线方案是：1）线性层间流水线，2）层内流水线，3）批次间流水线。线性层间流水线关注线性层；层内流水线关注非线性层；批次间流水线关注不同输入批次间的通信与计算重叠。我们通过在 CrypTen 的一个修改版本上进行增强来实现 MPC-Pipe，该版本将在线阶段与离线阶段分离。我们使用深度神经网络（VGG16、ResNet50）以及采用不同网络设置的 Transformer 来评估 MPC 在线阶段的端到端系统性能收益。我们展示了 ML 工作负载。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674175)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2025](../index.md)
