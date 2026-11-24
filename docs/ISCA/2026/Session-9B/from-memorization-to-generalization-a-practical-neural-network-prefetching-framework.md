---
title: "From Memorization to Generalization: A Practical Neural Network Prefetching Framework"
description: "ISCA 2026 · Session 9B · From Memorization to Generalization: A Practical Neural Network Prefetching Framework"
tags:
  - "ISCA2026"
  - "Session 9B"
  - "Prefetching and Cache 2"
---

# From Memorization to Generalization: A Practical Neural Network Prefetching Framework

**中文标题：** 从记忆到泛化：实用的神经网络预取框架

**所属 Session：** [Session 9B](index.md) · [ISCA 2026](../index.md)

**作者：** Xuan Tang, Zicong Wang, Shuiyi He, Hao Tang, Dezun Dong, Xiangke Liao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Data prefetchers are instrumental in mitigating the memory wall by anticipating future memory accesses. The first-level (L1) cache is the ideal location for prefetching, as it observes the complete, unfiltered stream of memory requests. However, its severely limited hardware resources have historically restricted L1 prefetchers to simple, pattern-based strategies, which struggle with complex access patterns. Conversely, recent machine learning (ML) based prefetchers like Pythia and Pathfinder demonstrate broader coverage but their prohibitive storage and computational costs relegate them to the L2 or last-level cache, making them too slow to be effective for the L1. This creates a critical design tension: the most powerful prefetching intelligence is stranded far from where it is needed most. To resolve this tension, we propose Moirai, a practical neural network prefetching framework designed specifically for the L1 data cache. Moirai’s core is CaPNet, a highly compact Binarized Neural Network we designed to achieve high-accuracy predictions within a tiny hardware footprint. Our evaluation shows that Moirai delivers competitive performance against state-of-the-art prefetchers while consuming only 780 Bytes of storage, an area reduction of over 97% compared to recent ML-based designs. Moirai thus charts a practical path forward for deploying powerful, generalization-based predictors in the most resource-sensitive parts of a modern processor.

## 中文摘要

数据预取器通过预测未来的内存访问，在缓解内存墙方面发挥着重要作用。一级（L1）缓存是进行预取的理想位置，因为它能观察到完整、未经筛选的内存请求流。然而，其严重受限的硬件资源历来将 L1 预取器限制在简单的、基于模式的策略上，而这些策略难以应对复杂的访问模式。相反，近期基于机器学习（ML）的预取器（如 Pythia 和 Pathfinder）展现了更广的覆盖范围，但其高昂的存储和计算成本使其只能被安置在 L2 或末级缓存，这使得它们对于 L1 而言过于缓慢而难以奏效。这造成了一个关键的设计张力：最强大的预取智能被搁置在离最需要它的地方很远的位置。为解决这一张力，我们提出 Moirai，一个专为 L1 数据缓存设计的实用神经网络预取框架。Moirai 的核心是 CaPNet，一个我们设计的、极其紧凑的二值化神经网络，旨在以极小的硬件占用实现高精度预测。我们的评估表明，Moirai 在仅消耗 780 字节存储的情况下，取得了与最先进预取器相当的性能，与近期基于 ML 的设计相比面积减少了 97% 以上。因此，Moirai 为在现代处理器最资源敏感的部分部署强大的、基于泛化的预测器开辟了一条实用路径。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：comp-arch-research/Moirai_ISCA2026](https://github.com/comp-arch-research/Moirai_ISCA2026)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9B](index.md) · [返回 ISCA 2026](../index.md)
