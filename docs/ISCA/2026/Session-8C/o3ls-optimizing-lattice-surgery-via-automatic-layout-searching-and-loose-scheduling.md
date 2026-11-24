---
title: "O3LS: Optimizing Lattice Surgery via Automatic Layout Searching and Loose Scheduling"
description: "ISCA 2026 · Session 8C · O3LS: Optimizing Lattice Surgery via Automatic Layout Searching and Loose Scheduling"
tags:
  - "ISCA2026"
  - "Session 8C"
  - "Quantum 2"
---

# O3LS: Optimizing Lattice Surgery via Automatic Layout Searching and Loose Scheduling

**中文标题：** O3LS: 通过自动布局搜索与宽松调度优化格点手术

**所属 Session：** [Session 8C](index.md) · [ISCA 2026](../index.md)

**作者：** Chenghong Zhu, Xian Wu, Jiahan Chen, Keming He, Junjie Wu, Xin Wang, Lingling Lao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Toward the large-scale, practical realization of quantum computing, quantum error correction is essential. Among various quantum error-correcting codes, the surface code stands out as a leading candidate, and lattice surgery based on surface codes has emerged as a promising technique for fault-tolerant quantum computation (FTQC). However, implementing quantum algorithms using lattice surgery introduces both resource and time overhead. Existing approaches typically focus on large layout designs, with compiler passes aimed primarily at optimizing time overhead. This often overlooks the trade-off between rotation bottlenecks and movement distance, which leads to inefficient resource utilization and prevents further reduction of the quantum computation failure rate. To address these challenges, we introduce O3LS, a framework for optimizing lattice surgery through automatic layout search and loose scheduling. O3LS achieves an optimal balance by automatically generating squeezed data layouts to reduce space requirements and employing loose scheduling algorithms combined with circuit synthesis techniques to reduce time overhead, thereby effectively minimizing overall logical error rates. Numerical results indicate that O3LS can reduce space overhead by 28.0% over standard layouts and 46.7% over sparse layouts without increasing the number of time steps, leading to suppression of logical error rates by up to 16% relative to larger data layout designs. O3LS can also achieve time overhead reductions of 36.07% and 24.76% in compact and standard data layout designs, respectively. It suppresses logical error rates by up to an order of magnitude compared to prior compilers that focus primarily on maximizing parallelism.

## 中文摘要

面向量子计算的大规模实际落地，量子纠错不可或缺。在各类量子纠错码中，表面码脱颖而出成为领先候选，而基于表面码的格点手术已成为容错量子计算（FTQC）的一项有前景技术。然而，使用格点手术实现量子算法会带来资源与时间开销。现有方法通常聚焦于大规模布局设计，其编译器 pass 主要旨在优化时间开销。这往往忽视了旋转瓶颈与移动距离之间的权衡，导致资源利用效率低下，并阻碍量子计算失败率的进一步降低。为应对这些挑战，我们提出 O3LS，一个通过自动布局搜索与宽松调度来优化格点手术的框架。O3LS 通过自动生成压缩的数据布局以减少空间需求，并采用结合电路合成技术的宽松调度算法以减少时间开销，从而实现最优平衡，有效最小化整体逻辑错误率。数值结果表明，在不增加时间步数的情况下，O3LS 相较标准布局可将空间开销降低 28.0%，相较稀疏布局降低 46.7%，从而使逻辑错误率相较更大的数据布局设计最多降低 16%。在紧凑与标准数据布局设计中，O3LS 还可分别实现 36.07% 与 24.76% 的时间开销降低。相较此前主要着眼于最大化并行度的编译器，它最多可将逻辑错误率降低一个数量级。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8C](index.md) · [返回 ISCA 2026](../index.md)
