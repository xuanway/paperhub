---
title: "GCStack+GCScaler: Fast and Accurate GPU Performance Analyses Using Fine-Grained Stall Cycle Accounting and Interval Analysis"
description: "ISCA 2025 · Session 8A · GCStack+GCScaler：基于细粒度停顿周期计数与区间分析的快速精准 GPU 性能分析"
tags:
  - "ISCA2025"
  - "Session 8A"
  - "Performance and Modeling"
---

# GCStack+GCScaler: Fast and Accurate GPU Performance Analyses Using Fine-Grained Stall Cycle Accounting and Interval Analysis

**中文标题：** GCStack+GCScaler：基于细粒度停顿周期计数与区间分析的快速精准 GPU 性能分析

**所属 Session：** [Session 8A](index.md) · [ISCA 2025](../index.md)

**作者：** Hanna Cha, Sungchul Lee, Jounghoo Lee, Yeonan Ha, Joonsung Kim, Youngsok Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731068) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

To design next-generation Graphics Processing Units (GPUs), GPU architects rely on GPU performance analyses to identify key GPU performance bottlenecks and explore GPU design spaces. Unfortu- nately, the existing GPU performance analysis mechanisms make it difficult for GPU architects to conduct fast and accurate GPU perfor- mance analyses. The existing mechanisms can provide misleading insights into GPU performance bottlenecks. They characterize the performance-degrading stall events of a GPU using coarse-grained, issue-stage-centric, and priority-based cycle stacks which tend to exaggerate memory-side stall events and hide concurrently occur- ring stall events. The existing mechanisms also incur high GPU design space exploration overhead, as they involve repetitive cycle- level timing simulations for evaluating alternative GPU designs. In this paper, we propose two GPU performance analysis mecha- nisms, namely GCStack and GCScaler. The two mechanisms enable fast and accurate GPU performance analyses by (1) accurately char- acterizing the performance bottlenecks of a baseline GPU using fine-grained stall cycle accounting, and (2) accurately scaling the stall cycles of the baseline GPU using interval analysis and analyti- cal scaling models. GCStack captures all the concurrently occurring stall events within each stall cycle, and characterizes the perfor- mance as a fine-grained cycle stack. Using the fine-grained cycle stack, GCScaler leverages the existing GPU interval analysis tech- niques’ accurate stall cycle scaling capability to estimate the cycle stack for an alternative GPU design. GCScaler further employs ana- lytical scaling models designed to scale the idle and synchronization stall cycles accurately. Our evaluation using 47 benchmarks shows that GCStack and GCScaler accelerate an exploration of 1,000 GPU designs by 32.7×over repetitive timing simulations while achieving a low mean absolute performance estimation error rate of 6.37%.

## 中文摘要

为设计下一代图形处理器（GPU），GPU架构研究者依靠GPU性能分析来识别关键性能瓶颈、开展设计空间探索。然而现有GPU性能分析机制难以实现快速且精准的性能分析，甚至会给出具有误导性的瓶颈结论。这类机制采用粗粒度、以发射阶段为中心、基于优先级的周期栈来刻画造成性能下降的阻塞事件，容易夸大访存侧阻塞的影响，同时掩盖并行发生的阻塞事件。此外，现有方案需要反复运行周期级时序仿真来评估不同候选架构，GPU设计空间探索开销巨大。

本文提出两套GPU性能分析机制：GCStack与GCScaler。二者实现快速精准性能分析的思路分为两点：（1）基于细粒度阻塞周期核算，准确刻画基准GPU的性能瓶颈；（2）借助区间分析与解析缩放模型，对基准GPU的阻塞周期做精准缩放推算。
GCStack会记录每一个阻塞周期内所有同时发生的阻塞事件，以细粒度周期栈的形式表征性能。基于该细粒度周期栈，GCScaler利用已有GPU区间分析技术的阻塞周期缩放能力，估算其他候选GPU架构对应的周期栈；同时搭配专门设计的解析缩放模型，对空闲周期与同步阻塞周期进行精准缩放。

基于47个基准测试的实验结果表明：相比重复时序仿真，GCStack+GCScaler在遍历1000种GPU架构时提速32.7倍，同时平均性能估计误差仅为6.37%。

## 英文关键词

Graphics Processing Unit (GPU), performance analysis, design space exploration, cycle accounting, interval analysis

## 中文关键词

图形处理器（GPU）, 性能分析, 设计空间探索, 周期核算, 区间分析

## 代码与研究制品

- [代码仓库](https://github.com/yonsei-hpcp/gcstack_gcscaler)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731068)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8A](index.md) · [返回 ISCA 2025](../index.md)
