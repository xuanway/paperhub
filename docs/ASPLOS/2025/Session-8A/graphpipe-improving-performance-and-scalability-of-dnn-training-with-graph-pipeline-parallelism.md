---
title: "GraphPipe: Improving Performance and Scalability of DNN Training with Graph Pipeline Parallelism"
description: "ASPLOS 2025 · Session 8A · GraphPipe：以图流水线并行提升 DNN 训练的性能与可扩展性"
tags:
  - "ASPLOS2025"
  - "Session 8A"
  - "ML Training"
---

# GraphPipe: Improving Performance and Scalability of DNN Training with Graph Pipeline Parallelism

**中文标题：** GraphPipe：以图流水线并行提升 DNN 训练的性能与可扩展性

**所属 Session：** [Session 8A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Byungsoo Jeon (NVIDIA), Mengdi Wu (Carnegie Mellon Univerisity), Shiyi Cao (UC Berkeley), Sunghyun Kim (Massachusetts Institute of Technology), Sunghyun Park (NVIDIA), Neeraj Aggarwal (Carnegie Mellon University), Colin Unger (Stanford University), Daiyaan Arfeen (Carnegie Mellon University), Peiyuan Liao (Carnegie Mellon University), Xupeng Miao (Carnegie Mellon University), Mohammad Alizadeh (Massachusetts Institute of Technology), Gregory R. Ganger (Carnegie Mellon University), Tianqi Chen (Carnegie Mellon University), Zhihao Jia (Carnegie Mellon University)

**单位：** NVIDIA；Carnegie Mellon Univerisity；UC Berkeley；Massachusetts Institute of Technology；Carnegie Mellon University；Stanford University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707220) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Deep neural networks (DNNs) continue to grow rapidly in size, making them infeasible to train on a single device. Pipeline parallelism is commonly used in existing DNN systems to support large-scale DNN training by partitioning a DNN into multiple stages, which concurrently perform DNN training for different micro-batches in a pipeline fashion. However, existing pipeline-parallel approaches only consider sequential pipeline stages and thus ignore the topology of a DNN, resulting in missed model-parallel opportunities. This paper presents graph pipeline parallelism (GPP), a new pipeline-parallel scheme that partitions a DNN into pipeline stages whose dependencies are identified by a directed acyclic graph. GPP generalizes existing sequential pipeline parallelism and preserves the inherent topology of a Attribution International 4.0 License. ionallyindependent operators, resulting in reduced memory requirement and improved GPU performance. In addition, we develop GraphPipe, a distributed system that exploits GPP strategies to enable performant and scalable DNN training. GraphPipe partitions a DNN into a graph of stages, optimizes micro-batch schedules for these stages, and parallelizes DNN training using the discovered GPP strategies. Evaluation on a variety of DNNs shows that GraphPipe outperforms existing pipeline-parallel systems such as PipeDream and Piper by up to 1.6×. GraphPipe also reduces the search time by 9-21× compared to PipeDream and Piper.

## 中文摘要

深度神经网络（DNN）的规模持续快速增大，使其难以在单一设备上完成训练。现有 DNN 系统通常采用流水线并行来支撑大规模 DNN 训练，其做法是将 DNN 划分为多个阶段，由这些阶段以流水线方式并发地对不同微批（micro-batch）执行 DNN 训练。然而，现有的流水线并行方法只考虑顺序的流水线阶段，因而忽略了 DNN 的拓扑结构，导致错失模型并行的机会。本文提出图流水线并行（graph pipeline parallelism，GPP），这是一种新的流水线并行方案，它把 DNN 划分为若干流水线阶段，这些阶段之间的依赖关系由有向无环图来标识。GPP 泛化了现有的顺序流水线并行，并保留了 DNN 的固有拓扑结构；Attribution International 4.0 License。ionallyindependent 算子，从而降低内存需求并提升 GPU 性能。此外，我们开发了 GraphPipe，这是一个利用 GPP 策略来实现高性能、可扩展 DNN 训练的分布式系统。GraphPipe 将 DNN 划分为阶段图，为这些阶段优化微批调度，并利用所发现的 GPP 策略并行化 DNN 训练。在多种 DNN 上的评测表明，GraphPipe 相比 PipeDream、Piper 等现有流水线并行系统最高可快 1.6×。与 PipeDream 和 Piper 相比，GraphPipe 还将搜索时间减少了 9-21×。

## 英文关键词

Distributed Systems, Deep Neural Network, Training, Parallelism

## 中文关键词

分布式系统；深度神经网络；训练；并行

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707220)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8A](index.md) · [返回 ASPLOS 2025](../index.md)
