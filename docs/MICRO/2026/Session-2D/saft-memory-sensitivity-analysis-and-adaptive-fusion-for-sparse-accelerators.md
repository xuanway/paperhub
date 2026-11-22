---
title: "SAFT: Memory Sensitivity Analysis and Adaptive Fusion for Sparse Accelerators"
description: "MICRO 2026 · Session 2D · SAFT：面向稀疏加速器的内存敏感性分析与自适应融合"
tags:
  - "MICRO2026"
---

# SAFT: Memory Sensitivity Analysis and Adaptive Fusion for Sparse Accelerators

**中文标题：** SAFT：面向稀疏加速器的内存敏感性分析与自适应融合

**所属 Session：** [Session 2D](index.md) · [MICRO 2026](../index.md)

**作者：** Guoyu Li, Zheng Guan, Zhiyi Chen, Jun Yu, Haodong Lu, Kun Wang

**来源：** MICRO 2026，pp. 863–877；[DOI](https://doi.org/10.1109/MICRO67795.2026.00071)

## 英文摘要

Sparse tensor applications arise in many domains, such as high-performance computing, recommender systems, and linear algebra. These applications often involve multiple sparse kernels, whose interactions and data reuse patterns critically affect performance. Consequently, understanding these relationships becomes crucial for accelerating sparse tensor computations. In this paper, we revisit the widely used producer-consumer reuse strategy, which is commonly applied in dense tensor operations, and examine its distinct characteristics in sparse tensor computations. We find that, due to the presence of diverse and irregular sparse patterns, employing conventional producer-consumer fusion approaches often results in severe performance degradation. Motivated by that limitation, we introduce SAFT, which employs an adaptive fusion strategy to improve sparse tensor computation performance. SAFT leverages a Memory Sensitivity Analysis method to characterize the reuse properties of sparse tensors by examining their nonzero element distributions. We can leverage these reuse properties to assess how different sparse patterns impact memory accesses during tensor computations, and to estimate the minimum memory capacity required to sustain optimal performance. We apply this method to sparse tensor applications, employing a Memory Allocation Model to determine optimal fusion strategies and memory distribution between producer and consumer kernels, with the goal of minimizing total memory traffic. In addition, we propose the SAFT optimization methods to further improve tensor computation performance and reduce analysis time. We conduct end-to-end evaluations on several classical sparse tensor applications. Compared to two prior fusion strategies, the adaptive approach adopted by SAFT achieves geomean speedups ranging from 1.18x to 2.02x and from 1.54x to 1.66xunder different memory configurations, respectively.

## 中文摘要

稀疏张量应用出现在许多领域，例如高性能计算、推荐系统和线性代数。这些应用程序通常涉及多个稀疏内核，其交互和数据重用模式严重影响性能。因此，理解这些关系对于加速稀疏张量计算至关重要。在本文中，我们重新审视了广泛使用的生产者-消费者重用策略，该策略通常应用于稠密张量运算，并研究其在稀疏张量计算中的独特特征。我们发现，由于存在多样化且不规则的稀疏模式，采用传统的生产者-消费者融合方法通常会导致严重的性能下降。受这一限制的启发，我们引入了 SAFT，它采用自适应融合策略来提高稀疏张量计算性能。 SAFT 利用内存敏感性分析方法通过检查稀疏张量的非零元素分布来表征稀疏张量的重用属性。我们可以利用这些重用属性来评估不同的稀疏模式在张量计算期间如何影响内存访问，并估计维持最佳性能所需的最小内存容量。我们将此方法应用于稀疏张量应用，采用内存分配模型来确定生产者和消费者内核之间的最佳融合策略和内存分配，目标是最小化总内存流量。此外，我们提出了SAFT优化方法来进一步提高张量计算性能并减少分析时间。我们对几个经典的稀疏张量应用进行端到端评估。与之前的两种融合策略相比，SAFT 采用的自适应方法在不同的内存配置下分别实现了 1.18 倍到 2.02 倍和 1.54 倍到 1.66 倍的几何平均加速。

## 中文关键词

稀疏张量；算子融合；内存流量优化；内存敏感性分析

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 2D](index.md) · [MICRO 2026 主页](../index.md)
