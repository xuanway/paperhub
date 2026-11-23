---
title: "Magellan: A High-Performance Loop-Guided Prefetcher for Indirect Memory Access"
description: "ISCA 2025 · Session 4B · Magellan：面向间接内存访问的高性能循环引导预取器"
tags:
  - "ISCA2025"
  - "Session 4B"
  - "Microarchitecture I"
---

# Magellan: A High-Performance Loop-Guided Prefetcher for Indirect Memory Access

**中文标题：** Magellan：面向间接内存访问的高性能循环引导预取器

**所属 Session：** [Session 4B](index.md) · [ISCA 2025](../index.md)

**作者：** Gelin Fu, Tian Xia, Mingzhuo Yu, Prashant Nair, Mieszko Lis, pengju ren

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731054) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Graph analytics and sparse linear algebra applications heavily rely on indirect memory access (IMA). IMAs are characterized by poor temporal and spatial locality, which causes frequent high-latency DRAM accesses. While dedicated hardware prefetchers for IMA have been explored, they target narrow access patterns and tend to introduce significant hardware complexity. Software prefetch- ing offers a promising alternative, leveraging compiler analysis to prefetch indirection patterns. However, existing software prefetch- ers struggle with sparse applications due to limited loop iterations and complex IMA patterns across nested loops. We propose Magellan, a novel loop-guided software prefetcher designed to detect and schedule IMA prefetches efficiently. Mag- ellan introduces two key innovations: (1) extracting dependence graphs across loop levels to detect complex IMA patterns and (2) cap- turing inner-outer loop semantics to prefetch for both current and future iterations. We evaluate Magellan on 14 memory-intensive benchmarks using real-world datasets from social networks and web graphs. Compared to the best existing IMA software prefetcher, Magellan reduces cache misses by 25% and dynamic instruction counts by 14% on average. This results in a 1.14×average speedup, with performance gains of up to 1.41×.

## 中文摘要

图分析与稀疏线性代数应用高度依赖间接访存（IMA）。间接访存的时间局部性与空间局部性较差，会引发大量高延迟的DRAM访问。尽管已有面向间接访存的专用硬件预取器研究，但它们仅适配有限的访问模式，并且硬件复杂度高。软件预取是一个很有前景的替代方案，借助编译器分析对间接访问模式进行预取。然而现有软件预取器在稀疏负载上效果不佳，原因是循环迭代数有限，嵌套循环下的间接访存模式十分复杂。

本文提出Magellan，一种基于循环引导的新型软件预取器，能够高效识别并调度间接访存预取。Magellan包含两项核心创新：（1）跨循环层级提取依赖图，识别复杂的间接访存模式；（2）捕捉内外层循环语义，同时为当前迭代和未来迭代执行预取。我们基于社交网络、网页图等真实数据集，在14个访存密集型基准上对Magellan进行测试。对比现有最优的间接访存软件预取器，Magellan平均将缓存缺失降低25%，动态指令数减少14%，实现平均1.14倍加速，最高提速1.41倍。

## 英文关键词

Software Prefetcher, Indirect Memory Access, Memory Hierarchy

## 中文关键词

软件预取器, 间接内存访问, 内存层次结构

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731054)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4B](index.md) · [返回 ISCA 2025](../index.md)
