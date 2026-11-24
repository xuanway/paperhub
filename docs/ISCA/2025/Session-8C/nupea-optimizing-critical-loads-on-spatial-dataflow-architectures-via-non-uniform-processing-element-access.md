---
title: "NUPEA: Optimizing Critical Loads on Spatial Dataflow Architectures via Non-Uniform Processing-Element Access"
description: "ISCA 2025 · Session 8C · NUPEA：通过非均匀处理单元访问优化空间数据流架构中的关键加载"
tags:
  - "ISCA2025"
  - "Session 8C"
  - "Domain Specific Accelerators II"
---

# NUPEA: Optimizing Critical Loads on Spatial Dataflow Architectures via Non-Uniform Processing-Element Access

**中文标题：** NUPEA：通过非均匀处理单元访问优化空间数据流架构中的关键加载

**所属 Session：** [Session 8C](index.md) · [ISCA 2025](../index.md)

**作者：** Souradip Ghosh, Graham Gobieski, Keyi Zhang, Brandon Lucia, Nathan Beckmann, Tony Nowatzki

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731061) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Data movement is the dominant energy, performance, and scala- bility bottleneck in modern architectures. Systems have tackled data movement by distributing data, e.g., via non-uniform memory access (NUMA) architectures. However, to reduce data movement, these architectures must identify critical data and place it closer to compute. Clever data placement is complex and often ineffective. Spatial dataflow architectures (SDAs) present a new opportunity to tackle data movement. SDAs distribute program instructions across a spatial fabric of processing elements (PEs). On large SDAs, some PEs are necessarily closer to memory than others, giving rise to non-uniform processing-element access (NUPEA). Clever instruc- tion placement can thus reduce data movement by, e.g., placing critical loads close to memory. This paper introduces NUPEA and contrasts it with prior data- centric approaches to scaling data movement. We find that it is often easier for the compiler to identify critical loads than the data they access, making NUPEA applicable where NUMA is not. We present simple architecture and compiler optimizations for NUPEA and implement them on the Monaco SDA architecture and effcc compiler, both industry products by Efficient Computer. On Monaco, across a range of important kernels, NUPEA yields an avg 28% speedup over a uniform-PE-access (UPEA) SDA and an avg 20% speed over a UPEA SDA with NUMA.

## 中文摘要

数据搬运是现代架构中制约能耗、性能与可扩展性的首要瓶颈。现有系统常采用数据分发的方式缓解该问题，例如非一致内存访问（NUMA）架构。但这类架构想要减少数据搬运，需要识别关键数据并将其放置在靠近计算单元的位置；而巧妙的数据放置策略实现复杂，且效果往往有限。

空间数据流架构（SDA）为解决数据搬运问题提供了新思路。SDA将程序指令分布在由处理单元（PE）构成的空间阵列上。在大规模SDA中，部分PE天然比其他PE更靠近存储，由此形成**非一致处理单元访问（NUPEA）**。通过合理的指令放置，例如把关键加载指令部署在靠近存储的PE上，NUPEA能够减少数据搬运。

本文正式提出NUPEA，并将其与以往以数据为中心的规模化数据搬运优化方案做对比。研究发现：编译器识别关键加载指令，通常比识别这些指令所访问的数据更容易，因此NUPEA可以在NUMA难以生效的场景下发挥作用。本文给出适配NUPEA的简易架构与编译器优化，并在Efficient Computer的商用产品Monaco SDA架构与effcc编译器上完成实现。
在Monaco平台上，对多款核心计算内核测试：相比采用一致PE访问（UPEA）的SDA，NUPEA平均提速28%；相比搭载NUMA的UPEA-SDA，NUPEA平均提速20%。

## 英文关键词

spatial dataflow architecture, data movement

## 中文关键词

空间数据流架构, 数据搬运

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731061)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8C](index.md) · [返回 ISCA 2025](../index.md)
