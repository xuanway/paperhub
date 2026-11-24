---
title: "SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips"
description: "ASPLOS 2026 · Session 2A · SuperOffload：在超级芯片上释放大规模 LLM 训练的能力"
tags:
  - "ASPLOS2026"
  - "Session 2A"
  - "LLM Training Systems"
---

# SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips

**中文标题：** SuperOffload：在超级芯片上释放大规模 LLM 训练的能力

**所属 Session：** [Session 2A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xinyu Lian (University of Illinois Urbana Champaign), Masahiro Tanaka (Microsoft), Olatunji Ruwase (Snowflake), Minjia Zhang (University of Illinois Urbana Champaign)

**单位：** University of Illinois Urbana Champaign；Microsoft；Snowflake

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762217) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The emergence of Superchips represents a significant advancement in next-generation AI hardware. These Superchips employ a tightly coupled heterogeneous architecture that integrates GPU and CPU on the same package, which offers unprecedented computational power. However, there has been scant research investigating how LLM training benefits from this new architecture. In this work, for the first time, we study LLM training solutions based on offloading for Superchips. We observe important differences between Superchips and traditional loosely-coupled GPU-CPU architecture, which necessitate revisiting prevailing assumptions about offloading. Based on that, we present SuperOffload, a Superchip-centric offloading system that simultaneously uses Hopper GPU, Grace CPU, and NVLink-C2C interconnect more efficiently. SuperOffload accomplishes this via a combination of techniques, such as adaptive weight offloading, bucketization repartitioning, Superchip-aware casting, speculative execution, and a highly optimized Adam optimizer for Grace CPUs. Our evaluation of SuperOffload on NVIDIA GH200 demonstrates up to 2.5× throughput improvement compared to state-of-the-art offloading-based systems, enabling training of up to 25B model on a single Superchip while achieving high training throughput. We also extend SuperOffload with ZeRO-style data parallelism and DeepSpeed-Ulysses sequence parallelism, enabling training of 13B model with sequence lengths up to 1 million tokens on 8 GH200 while achieving 55% MFU.

## 中文摘要

超级芯片（Superchip）的出现代表了下一代 AI 硬件的重要进步。这些超级芯片采用紧耦合的异构架构，在同一封装内集成 GPU 与 CPU，从而提供了前所未有的计算能力。然而，关于 LLM 训练如何从这一新架构中获益的研究仍然很少。在本工作中，我们首次研究了基于卸载的面向超级芯片的 LLM 训练方案。我们观察到超级芯片与传统松耦合 GPU-CPU 架构之间存在重要差异，这些差异使得有必要重新审视关于卸载的既有假设。基于此，我们提出 SuperOffload，一个以超级芯片为中心的卸载系统，它同时更高效地利用 Hopper GPU、Grace CPU 和 NVLink-C2C 互连。SuperOffload 通过一系列技术实现这一点，例如自适应权重卸载、分桶重划分、超级芯片感知的类型转换、推测执行，以及针对 Grace CPU 高度优化的 Adam 优化器。我们在 NVIDIA GH200 上对 SuperOffload 的评估表明，与最先进的基于卸载的系统相比，吞吐量提升最高达 2.5×，使得在单个超级芯片上训练高达 25B 的模型并能同时实现高训练吞吐。我们还用 ZeRO 风格的数据并行和 DeepSpeed-Ulysses 序列并行扩展了 SuperOffload，使得在 8 块 GH200 上训练序列长度高达 100 万 token 的 13B 模型并达到 55% MFU 成为可能。

## 英文关键词

Large Language Model; Efficient Deep Learning Training; Heterogeneous Memory; Superchip

## 中文关键词

大语言模型；高效的深度学习训练；异构内存；超级芯片

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762217)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2A](index.md) · [返回 ASPLOS 2026](../index.md)
