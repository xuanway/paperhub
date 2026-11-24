---
title: "A Data-Driven Dynamic Execution Orchestration Architecture"
description: "ASPLOS 2026 · Session 7D · 一种数据驱动的动态执行编排架构"
tags:
  - "ASPLOS2026"
  - "Session 7D"
  - "Processor Microarchitecture"
---

# A Data-Driven Dynamic Execution Orchestration Architecture

**中文标题：** 一种数据驱动的动态执行编排架构

**所属 Session：** [Session 7D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhenyu Bai (National University of Singapore), Pranav Dangi (National University Of Singapore), Rohan Juneja (National University of Singapore), Zhaoying Li (National University of Singapore), Zhanglu Yan (National university of Singapore), Huiying Lan (Lumai Ltd.), Tulika Mitra (National University of Singapore)

**单位：** National University of Singapore；National University Of Singapore；National university of Singapore；Lumai Ltd.

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762226) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Domain-specific accelerators deliver exceptional performance on their target workloads through fabrication-time orchestrated datapaths. However, such specialized architectures often exhibit performance fragility when exposed to new kernels or irregular input patterns. In contrast, programmable architectures like FPGAs, CGRAs, and GPUs rely on compile-time orchestration to support a broader range of applications; but they are typically less efficient under irregular or sparse data. Pushing the boundaries of programmable architectures requires designs that can achieve efficiency and high-performance on par with specialized accelerators while retaining the agility of general-purpose architectures. We introduce Canon, a parallel architecture that bridges the gap between specialized and general purpose architectures. Canon exploits data-level and instruction-level parallelism through its novel design. First, it employs a novel dynamic data-driven orchestration mechanism using programmable Finite State Machines (FSMs). These FSMs are programmed at compile time to encode high-level dataflow per state and translate incoming meta-information (e.g., sparse coordinates) into control instructions at runtime. Second, er several cycles, creating a staggered pipelined execution. These innovations amortize control overhead, allowing dynamic instruction changes while constructing a continuously evolving dataflow that maximizes parallelism. Experimental evaluation shows that Canon delivers high performance across diverse data-agnostic and data-driven kernels while achieving efficiency comparable to specialized accelerators, yet retaining the flexibility of a general-purpose architecture.

## 中文摘要

领域专用加速器通过制造时编排的数据通路，在其目标工作负载上提供卓越性能。然而，此类专用架构在暴露于新内核或不规则输入模式时往往表现出性能脆弱性。相比之下，FPGA、CGRA 和 GPU 等可编程架构依赖编译时编排来支持更广泛的应用范围；但它们在不规则或稀疏数据下通常效率较低。推动可编程架构的边界，需要既能在效率与高性能上与专用加速器相当、又能保持通用架构敏捷性的设计。我们提出 Canon，一种弥合专用架构与通用架构之间差距的并行架构。Canon 通过其新颖设计利用数据级并行性与指令级并行性。首先，它采用一种新颖的、使用可编程有限状态机（FSM）的动态数据驱动编排机制。这些 FSM 在编译时被编程，以编码每个状态的高层数据流，并在运行时将传入的元信息（例如稀疏坐标）转换为控制指令。其次，……经过若干周期，形成交错的流水化执行。这些创新摊销了控制开销，允许动态指令变化，同时构建持续演化、最大化并行性的数据流。实验评估表明，Canon 在多样的数据无关与数据驱动内核上都能提供高性能，同时实现与专用加速器相当的效率，并保持通用架构的灵活性。

## 英文关键词

Dataflow Architectures, Sparse Accelerators

## 中文关键词

数据流架构；稀疏加速器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762226)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7D](index.md) · [返回 ASPLOS 2026](../index.md)
