---
title: "PipeIMC: a Pipelined In-SRAM Computing Architecture"
description: "ISCA 2026 · Session 3B · PipeIMC: a Pipelined In-SRAM Computing Architecture"
tags:
  - "ISCA2026"
  - "Session 3B"
  - "DRAM and SRAM PIM/PNM"
---

# PipeIMC: a Pipelined In-SRAM Computing Architecture

**中文标题：** PipeIMC: 一种流水线式 SRAM 内计算架构

**所属 Session：** [Session 3B](index.md) · [ISCA 2026](../index.md)

**作者：** Yikai Cui, Renhao Fan, Weike Li, Mingzhao Li, Mingyu Wang, Zhaolin Li

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Generative large language models pose a significant challenge to the memory bandwidth and computing capabilities of traditional computing architectures. By performing computations inside the SRAM arrays, in-SRAM computing architectures can achieve substantial performance while reducing memory hierarchy bandwidth usage and energy consumption, making them a strong alternative to CPUs and GPUs for executing LLMs. However, prior in-SRAM computing architectures have found it challenging to achieve higher performance, because they are restricted by their in-order execution mechanism, in which each operation must wait for the completion of its preceding operations before execution. To address this problem, this paper proposes PipeIMC, a pipelined in-SRAM computing architecture with two stages: memory and calculation. Accordingly, each in-SRAM computing operation is segmented into the memory phase and the calculation phase. When the calculation phase of the current operation is being executed in the calculation stage, the memory stage can execute the memory phase of the next operation to fetch the required data. To alleviate the influence of data hazards and control hazards, we propose an out-of-order execution mechanism integrated with explicit register renaming. To further enhance performance, we propose a fine-grained issue mechanism that enables the next operation to be issued earlier during the idle cycles of the memory stage of the current operation. Evaluation results show that PipeIMC achieves 2.15x to 3.96x and 1.13x to 4.77x utilization, compared to EVE and Duality Cache, two state-of-the-art in-SRAM computing architectures. This improvement in utilization yields a performance of 2.17x and 1.68x per area, and an energy efficiency of 1.92x and 1.60x, on average, over EVE and Duality Cache on the Rodinia GPU benchmarks.

## 中文摘要

生成式大语言模型对传统计算架构的内存带宽和计算能力提出了重大挑战。通过在SRAM阵列内部执行计算，SRAM内计算架构可以在减少内存层次带宽使用和能耗的同时实现可观性能，使其成为执行LLM时CPU和GPU的有力替代方案。然而，先前的SRAM内计算架构由于受限于其顺序执行机制（每个操作必须等待前一个操作完成才能执行）而难以实现更高的性能。为解决此问题，本文提出了PipeIMC，一种具有两个阶段（内存和计算）的流水线式SRAM内计算架构。相应地，每个SRAM内计算操作被分割为内存阶段和计算阶段。当当前操作的计算阶段在计算级中执行时，内存级可以执行下一操作的内存阶段以获取所需数据。为减轻数据冒险和控制冒险的影响，我们提出了一种结合显式寄存器重命名的乱序执行机制。为进一步提高性能，我们提出了一种细粒度发射机制，使得下一个操作可以在当前操作内存级的空闲周期中更早地被发射。评估结果显示，与两种最先进的SRAM内计算架构EVE和Duality Cache相比，PipeIMC的利用率分别提高了2.15倍到3.96倍和1.13倍到4.77倍。这种利用率的提升带来了平均2.17倍和1.68倍的单位面积性能，以及在Rodinia GPU基准测试上相比EVE和Duality Cache平均1.92倍和1.60倍的能效。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2026](../index.md)
