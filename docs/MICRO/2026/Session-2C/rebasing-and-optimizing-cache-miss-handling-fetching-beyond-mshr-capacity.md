---
title: "Rebasing and Optimizing Cache Miss Handling: Fetching Beyond MSHR Capacity"
description: "MICRO 2026 · Session 2C · 重新组织并优化缓存未命中处理：突破 MSHR 容量限制的数据获取"
tags:
  - "MICRO2026"
  - "Cache"
---

# Rebasing and Optimizing Cache Miss Handling: Fetching Beyond MSHR Capacity

**中文标题：** 重新组织并优化缓存未命中处理：突破 MSHR 容量限制的数据获取

**所属 Session：** [Session 2C](index.md) · [MICRO 2026](../index.md)

**作者：** Simranjit Singh, Agustín Navarro-Torres, Biswabandan Panda, Alberto Ros

**来源：** MICRO 2026，pp. 723–737；[DOI](https://doi.org/10.1109/MICRO67795.2026.00062)

## 英文摘要

Miss Status Handling Registers (MSHRs) track cache miss information while cache lines are being fetched from higher cache levels or memory. In traditional implementations, when all MSHR entries are occupied, the cache cannot process new misses, stalling demand requests and dropping or delaying prefetches, and in the end, limiting memory-level parallelism. Scaling the number of MSHR entries is not straightforward, as they must support associative lookups for high performance. In addition, hardware prefetching further increases MSHR pressure. This paper first observes that academic work has largely over- looked industrial implementations of MSHRs, with important implications for performance. Then, it details the implementation of industry-like MSHR designs, namely Homeless, in which prefetch requests can still be issued when MSHRs are full but are degraded to fill higher cache levels, and its demand- to-prefetch (D2P) variant, where a demand miss that cannot allocate an MSHR entry is instead issued as a prefetch-style request. Finally, we analyze the need for the first-level data cache (L1D) MSHR information for both demand and prefetch misses, and propose Nomad, a microarchitectural technique that (i) enables prefetching to L1D even when the MSHR is full and (ii) allows incoming demand misses to reclaim L1D MSHR entries occupied by prefetch requests. Across six benchmark suites, Nomad delivers the strongest improvements on AI/ML and GAP, where L1D MSHR pressure is highest, and performs similarly to Homeless-D2P on the remaining suites. For AI/ML workloads and in the absence of an L1D prefetcher, Nomad reaches 11.3% speedup, while Homeless-D2P achieves 8.3%. With an L1D Berti prefetcher, Nomad reaches 14.4% speedup compared to the 9.4% achieved by Homeless-D2P. These improvements come with no storage cost.

## 中文摘要

未命中状态处理寄存器 (MSHR) 在从更高的高速缓存级别或内存中获取高速缓存行时跟踪高速缓存未命中信息。在传统实现中，当所有 MSHR 条目都被占用时，缓存无法处理新的未命中，从而停止需求请求并丢弃或时延预取，最终限制内存级并行性。扩展 MSHR 条目的数量并不简单，因为它们必须支持关联查找以获得高性能。此外，硬件预取进一步增加了MSHR的压力。本文首先指出，学术工作在很大程度上忽视了 MSHR 的工业实施，这对绩效具有重要影响。然后，它详细介绍了类似行业的 MSHR 设计（即 Homeless）的实现，其中当 MSHR 已满时仍然可以发出预取请求，但会降级以填充更高的缓存级别，以及它的需求预取（D2P）变体，其中无法分配 MSHR 条目的需求未命中而是作为预取样式请求发出。最后，我们分析了需求和预取未命中对一级数据缓存 (L1D) MSHR 信息的需求，并提出了 Nomad，这是一种微架构技术，该技术 (i) 即使在 MSHR 已满时也能够预取到 L1D，并且 (ii) 允许传入的需求未命中回收预取请求占用的 L1D MSHR 条目。在六个基准套件中，Nomad 在 AI/ML 和 GAP 方面提供了最强的改进，其中 L1D MSHR 压力最高，并且在其余套件上的表现与 Homeless-D2P 类似。对于 AI/ML 工作负载，在没有 L1D 预取器的情况下，Nomad 的加速速度达到 11.3%，而 Homeless-D2P 的加速速度达到 8.3%。借助 L1D Berti 预取器，Nomad 的加速速度达到 14.4%，而 Homeless-D2P 的加速速度为 9.4%。这些改进无需存储成本。

## 中文关键词

未命中状态处理寄存器；预取；内存级并行性；缓存未命中处理；微架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 2C](index.md) · [MICRO 2026 主页](../index.md)
