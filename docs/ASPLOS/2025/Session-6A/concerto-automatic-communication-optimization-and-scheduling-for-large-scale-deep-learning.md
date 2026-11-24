---
title: "Concerto: Automatic Communication Optimization and Scheduling for Large-Scale Deep Learning"
description: "ASPLOS 2025 · Session 6A · Concerto：面向大规模深度学习的通信优化与调度自动化"
tags:
  - "ASPLOS2025"
  - "Session 6A"
  - "ML Systems 2"
---

# Concerto: Automatic Communication Optimization and Scheduling for Large-Scale Deep Learning

**中文标题：** Concerto：面向大规模深度学习的通信优化与调度自动化

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shenggan Cheng (National University of Singapore), Shengjie Lin (Georgia Institute of Technology), Lansong Diao (Alibaba Group), Hao Wu (George Mason University), Siyu Wang (Alibaba Group), Chang Si (Alibaba Group), Ziming Liu (National University of Singapore), Xuanlei Zhao (National University of Singapore), Jiangsu Du (Sun Yat-sen University), Wei Lin (Alibaba Group), Yang You (National University of Singapore)

**单位：** National University of Singapore；Georgia Institute of Technology；Alibaba Group；George Mason University；Sun Yat-sen University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707223) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

With the exponential growth of deep learning (DL), there arises an escalating need for scalability. Despite significant advancements in communication hardware capabilities, the time consumed by communication remains a bottleneck during training. The existing various optimizations are coupled within parallel systems to implement specific computation-communication overlap. These approaches pose challenges in terms of performance, programmability, and generality. In this paper, we introduce Concerto, a compiler framework designed to address these challenges by automatically optimizing and scheduling communication. We formulate the scheduling problem as a resource-constrained project scheduling problem and use off-the-shelf solver to get the near-optimal scheduling. And use auto-decomposition to create overlap opportunity for critical (synchronous) communication. Our evaluation shows Concerto can match or outperform state-of-the-art parallel frameworks, including Megatron-LM, JAX/XLA, DeepSpeed, and Alpa, all of which include extensive hand-crafted optimization. Unlike previous works, Concerto decouples the parallel approach and Attribution International 4.0 License. e to a wide variety of parallelisms without manual optimization.

## 中文摘要

随着深度学习（DL）的指数级增长，对可扩展性的需求不断攀升。尽管通信硬件能力已取得显著进步，但通信所消耗的时间在训练过程中仍然是瓶颈。现有的各类优化被耦合在并行系统内部，以实现特定的计算—通信重叠。这些方法在性能、可编程性和通用性方面都面临挑战。本文提出 Concerto，一个编译器框架，通过自动优化和调度通信来应对这些挑战。我们将调度问题建模为资源受限的项目调度问题，并使用现成的求解器获得接近最优的调度。同时利用自动分解为关键（同步）通信创造重叠机会。我们的评估表明，Concerto 能够匹配或超越最先进的并行框架，包括 Megatron-LM、JAX/XLA、DeepSpeed 和 Alpa，而这些框架都包含了大量手工优化。与以往工作不同，Concerto 将并行方式与 Attribution International 4.0 License. e 解耦，可适配各种并行方式而无需手工优化。

## 英文关键词

Distributed Deep Learning, Collective Communication, GPUs, Fine-grained Overlap

## 中文关键词

分布式深度学习；集合通信；GPU；细粒度重叠

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707223)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6A](index.md) · [返回 ASPLOS 2025](../index.md)
