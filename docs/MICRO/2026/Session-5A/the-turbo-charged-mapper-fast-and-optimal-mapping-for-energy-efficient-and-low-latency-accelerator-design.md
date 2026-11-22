---
title: "The Turbo-Charged Mapper: Fast and Optimal Mapping for Energy-Efficient and Low-Latency Accelerator Design"
description: "MICRO 2026 · Session 5A · The Turbo-Charged Mapper：面向高能效低时延加速器设计的快速最优映射"
tags:
  - "MICRO2026"
  - "Energy Efficiency"
---

# The Turbo-Charged Mapper: Fast and Optimal Mapping for Energy-Efficient and Low-Latency Accelerator Design

**中文标题：** The Turbo-Charged Mapper：面向高能效低时延加速器设计的快速最优映射

**所属 Session：** [Session 5A](index.md) · [MICRO 2026](../index.md)

**作者：** Michael Gilbert, Tanner Andrulis, Vivienne Sze, Joel S. Emer

**来源：** MICRO 2026，pp. 1614–1628；[DOI](https://doi.org/10.1109/MICRO67795.2026.00117)

## 英文摘要

The energy and latency of an accelerator running a deep neural network (DNN) depend on how the computation and data movement are scheduled in the accelerator (i.e., mapping), and picking an optimal mapping is essential to achieve high-performance accelerators. However, it is challenging to find mappings that maximize accelerator performance. The space of mappings is large, and prior works cannot guarantee finding optimal mappings because they use heuristics or metaheuristics to narrow the search space. To address this challenge, we propose the Turbo-Charged Mapper (TCM), a fast mapper that finds optimal mappings. The key to our approach is that we define a new mapping concept called dataplacement, which, like the prior concept of dataflow, allows for clear analysis and comparison of mappings. Through it, we identify opportunities to prune redundant and suboptimal mappings, reducing search space by up to 32 orders of magnitude (10^37→10^5). TCM leverages these insights to perform full mapspace searches, making it the first mapper that can find optimal mappings in feasible runtime. Compared to prior mappers, TCM improves accelerator energy-delay-product by 1.2-6.5× while simultaneously reducing mapping search time by 1000× (5 hours → 17 seconds).

## 中文摘要

运行深度神经网络 (DNN) 的加速器的能量和时延取决于加速器中计算和数据移动的安排方式（即映射），选择最佳映射对于实现高性能加速器至关重要。然而，找到最大化加速器性能的映射是具有挑战性的。映射空间很大，先前的工作不能保证找到最佳映射，因为它们使用启发式或元启发式来缩小搜索空间。为了应对这一挑战，我们提出了 Turbo-Charged Mapper (TCM)，这是一种可以找到最佳映射的快速映射器。我们方法的关键是我们定义了一个称为数据放置的新映射概念，它与之前的数据流概​​念一样，可以对映射进行清晰的分析和比较。通过它，我们找到了修剪冗余和次优映射的机会，将搜索空间减少多达 32 个数量级 (10^37→10^5)。 TCM 利用这些见解来执行完整的映射空间搜索，使其成为第一个可以在可行的运行时找到最佳映射的映射器。与之前的映射器相比，TCM 将加速器能量时延积提高了 1.2-6.5 倍，同时将映射搜索时间缩短了 1000 倍（5 小时 → 17 秒）。

## 中文关键词

映射优化；加速器；设计空间探索；深度神经网络；能效与时延

## 代码与研究制品

- 代码仓库：[https://github.com/Accelergy-Project/accelforge](https://github.com/Accelergy-Project/accelforge)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 5A](index.md) · [MICRO 2026 主页](../index.md)
