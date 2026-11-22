---
title: "Rivera: Turbo-Boosting Vector Architectures for Irregular Memory Access Patterns"
description: "MICRO 2026 · Session 7D · Rivera：加速向量架构中的不规则内存访问"
tags:
  - "MICRO2026"
---

# Rivera: Turbo-Boosting Vector Architectures for Irregular Memory Access Patterns

**中文标题：** Rivera：加速向量架构中的不规则内存访问

**所属 Session：** [Session 7D](index.md) · [MICRO 2026](../index.md)

**作者：** Julian Pavon, Ivan Vargas Valdivieso, Carlos Rojas, Roger Figueras, Francesc Moll, Osman Unsal, Mateo Valero, Adrian Cristal

**来源：** MICRO 2026，pp. 2703–2718；[DOI](https://doi.org/10.1109/MICRO67795.2026.00184)

## 英文摘要

The increasing prevalence of irregular memory accesses in domains such as sparse linear algebra, graph analytics, genome sequence analysis, among others, limits the efficiency of modern vector architectures. Designed primarily for regular unit-stride accesses, these architectures experience high latency, bandwidth underutilization, and core's resource contention when executing irregular memory operations. To address these challenges, we propose Rivera, a hardware-software co-designed vector architecture that accelerates irregular execution by placing frequently accessed data in a low-latency, multiported, element-grained scratchpad built from repurposed vector registers. Motivated by the observation that large vector register files (VRFs) in modern OoO CPUs are underutilized under workloads dominated by irregular memory accesses, Rivera dynamically partitions the physical vector registers into a standard VRF and an indexed VRF (iVRF). The iVRF operates either as a standard VRF—with its registers included in the renaming pool—or as a scratchpad memory—where they are removed from renaming. By storing data frequently accessed by irregular patterns in the iVRF, Rivera reduces pressure on the memory hierarchy and improves access latency through its multiported, element-level design. Rivera introduces a lightweight ISA extension to control the iVRF with minimal integration overhead. Across a diverse set of workloads, Rivera achieves average speedups of 2.2x, 2.0x and 1.2x over software, dedicated vector instructions and scratchpad-based solutions, respectively, with negligible area overhead (~0.03%) relative to an Intel Ice Lake baseline. By leveraging existing on-chip resources, Rivera provides a scalable and cost-effective solution for accelerating workloads with irregular memory accesses.

## 中文摘要

在稀疏线性代数、图分析、基因组序列分析等领域，不规则内存访问的日益普遍，限制了现代向量架构的效率。这些架构主要针对常规单位跨度访问而设计，在执行不规则内存操作时会遇到高时延、带宽利用率低以及核心资源争用等问题。为了应对这些挑战，我们提出了 Rivera，这是一种硬件-软件共同设计的向量架构，通过将频繁访问的数据放置在由重新调整用途的向量寄存器构建的低时延、多端口、元素粒度暂存器中来加速不规则执行。鉴于现代 OoO CPU 中的大型向量寄存器文件 (VRF) 在以不规则内存访问为主的工作负载下未得到充分利用，Rivera 将物理向量寄存器动态划分为标准 VRF 和索引 VRF (iVRF)。 iVRF 既可以作为标准 VRF 运行（其寄存器包含在重命名池中），也可以作为暂存存储器运行（在暂存器存储器中将它们从重命名中删除）。通过在 iVRF 中存储以不规则模式频繁访问的数据，Rivera 减少了内存层次结构的压力，并通过其多端口、元素级设计改善了访问时延。 Rivera 引入了轻量级 ISA 扩展，以最小的集成开销来控制 iVRF。在各种不同的工作负载中，Rivera 分别比软件、专用向量指令和基于暂存器的解决方案实现了 2.2 倍、2.0 倍和 1.2 倍的平均加速，相对于 Intel Ice Lake 基准，面积开销可以忽略不计（约 0.03%）。通过利用现有的片上资源，Rivera 提供了可扩展且经济高效的解决方案，可通过不规则的内存访问来加速工作负载。

## 中文关键词

向量计算；不规则内存访问；分散与聚集指令；软件管理暂存存储器

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7D](index.md) · [MICRO 2026 主页](../index.md)
