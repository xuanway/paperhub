---
title: "Harmonia: A Unified Hierarchical Scheduling Framework for Sparse Matrix Multiplication"
description: "ISCA 2026 · Session 8D · Harmonia: A Unified Hierarchical Scheduling Framework for Sparse Matrix Multiplication"
tags:
  - "ISCA2026"
  - "Session 8D"
  - "HPC"
---

# Harmonia: A Unified Hierarchical Scheduling Framework for Sparse Matrix Multiplication

**中文标题：** Harmonia: 面向稀疏矩阵乘法的统一层次化调度框架

**所属 Session：** [Session 8D](index.md) · [ISCA 2026](../index.md)

**作者：** Jingkui Yang, Fangxin Liu, Xin Ju, Ning Yang, Chenyang Guan, Junjie Wang, Zongwu Wang, Mei Wen, Jian Liu, Li Jiang, Haibing Guan

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Sparse tensor computation is a critical primitive across many domains. The highly irregular structure of sparse matrices limits the performance and efficiency of sparse tensor computation on conventional platforms, motivating extensive efforts on specialized hardware accelerators. However, existing accelerators typically rely on rigid execution dataflows such as inner-product, outer-product, or row-based schemes. Each dataflow is optimized for a particular sparsity pattern and fails to deliver robust performance across the wide diversity of real workloads. Although sparsity reduces computation and memory cost, effectively exploiting it on hardware remains challenging because sparsity patterns vary widely and often change at runtime. Recent accelerators attempt to balance efficiency and generality by introducing architectural flexibility, but fixed-dataflow designs degrade under pattern shifts, while flexible designs support multiple modes only at the cost of higher complexity and static configuration. To address these limitations, we propose Harmonia, a hierarchical scheduling approach that allows a sparse accelerator to efficiently adapt to different sparsity patterns. Harmonia first uses a lightweight offline model to derive a near-optimal initial tiling strategy and dataflow mapping. Both tile shape and dataflow mode are configurable to match diverse sparsity characteristics. At runtime, Harmonia detects the current sparsity pattern and dynamically selects the most effective dataflow mode based on tile-level observations. The underlying hardware supports this adaptive execution with fast, low-cost reconfiguration and load balancing. Extensive evaluations demonstrate that Harmonia delivers an average of 1.75× higher performance and 2.47× better energy efficiency compared to state-of-the-art accelerators, while maintaining robust and stable throughput across highly variable runtime sparsity patterns.

## 中文摘要

稀疏张量计算是众多领域中的一项关键基础操作。稀疏矩阵高度不规则的结构限制了稀疏张量计算在传统平台上的性能与效率，这促使人们在专用硬件加速器上投入大量努力。然而，现有加速器通常依赖固定的执行数据流，如内积、外积或按行的方案。每种数据流都针对特定的稀疏模式进行优化，无法在丰富多样的真实工作负载上提供稳健的性能。尽管稀疏性降低了计算与内存成本，但在硬件上有效利用它仍具挑战，因为稀疏模式差异极大且常常在运行时变化。近期加速器试图通过引入架构灵活性来平衡效率与通用性，但固定数据流设计在模式变化时会性能下降，而灵活设计仅以更高的复杂度和静态配置为代价支持多种模式。为解决这些局限，我们提出 Harmonia，一种分层调度方法，使稀疏加速器能够高效适应不同的稀疏模式。Harmonia 首先使用轻量级离线模型推导出接近最优的初始分块策略与数据流映射；分块形状与数据流模式均可配置，以匹配多样的稀疏特征。在运行时，Harmonia 检测当前的稀疏模式，并基于分块级观测动态选择最有效的数据流模式。底层硬件通过快速、低成本的重配置与负载均衡来支持这种自适应执行。大量评估表明，相较最先进的加速器，Harmonia 平均性能提升 1.75×，能效提升 2.47×，同时在高度变化的运行时稀疏模式下保持稳健而稳定的吞吐量。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8D](index.md) · [返回 ISCA 2026](../index.md)
