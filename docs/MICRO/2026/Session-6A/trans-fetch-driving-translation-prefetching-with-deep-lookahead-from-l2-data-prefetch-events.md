---
title: "TRANS-FETCH: Driving Translation Prefetching with Deep Lookahead from L2 Data Prefetch Events"
description: "MICRO 2026 · Session 6A · TRANS-FETCH：利用 L2 数据预取事件的深度前瞻驱动地址转换预取"
tags:
  - "MICRO2026"
  - "Prefetching"
---

# TRANS-FETCH: Driving Translation Prefetching with Deep Lookahead from L2 Data Prefetch Events

**中文标题：** TRANS-FETCH：利用 L2 数据预取事件的深度前瞻驱动地址转换预取

**所属 Session：** [Session 6A](index.md) · [MICRO 2026](../index.md)

**作者：** Cansong Zhou, Xiaohang Wang, Peng Liu

**来源：** MICRO 2026，pp. 1832–1847；[DOI](https://doi.org/10.1109/MICRO67795.2026.00130)

## 英文摘要

Translation Lookaside Buffer (TLB) misses increasingly limit the performance of memory-intensive workloads, yet existing translation prefetching techniques often fail to provide accurate and timely page-walk prefetching, making TLB misses a major bottleneck. Cross-page prefetching is a promising approach to help TLB warming. But prior approaches rely on L1 cross-page prefetching, where virtual-address-based prefetchers naturally extend predictions across page boundaries and warm the TLB as a side effect. We show that this strategy is fundamentally constrained by its position in the memory hierarchy: across two representative L1 prefetchers, cross-page prefetches achieve only up to 23.7% second-level translation lookaside buffer (STLB) warming accuracy, and many useful translations arrive too late to hide page-walk latency, making them ineffective to warm the TLB. We identify a new opportunity in L2 prefetching. Since L2 prefetchers are designed to tolerate hundreds of cycles latency, their cross-page prefetching can provide the deep lookahead needed to warm the TLB. However, conventional physically addressed L2 prefetchers discard this information since physical addresses are not contiguous like virtual addresses. We show that utilizing these cross-page predictions to warm the TLB can dramatically improve translation-prefetch accuracy and Instructions-per-Cycle (IPC) over the independent TLB prefetcher and L1-based cross-page prefetching approaches. We propose TRANS-FETCH, a lightweight cooperative architecture that recovers these discarded cross-page predictions and forwards them to the translation subsystem through a 16-entry reverse-translation cache and a low-priority translation queue, at a total cost under 0.3 KB, with no independent page-level predictor and no modification to the prefetcher, page walker, or coherence protocol. On a baseline where Berti already performs L1 cross-page prefetching and warms the STLB, TRANS-FETCH achieves 70.2-74.4% translation-warming accuracy versus 34.7-37.4% for the state of the art (SOTA) independent predictor Agile TLB Prefetcher (ATP), and improves geomean IPC by +1.78-3.83% on SPEC (+1.67-6.43% overall) across three architecturally diverse L2 prefetchers, where ATP delivers at most +0.3%.

## 中文摘要

地址转换后备缓冲器 (TLB) 缺失日益限制内存密集型工作负载的性能，而现有的转换预取技术通常无法提供准确且及时的页表遍历预取，这使得 TLB 缺失成为主要瓶颈。跨页预取是一种很有前景的帮助 TLB 预热的方法。但之前的方法依赖于 L1 跨页预取，其中基于虚拟地址的预取器自然会跨页边界扩展预测，并作为副作用预热 TLB。我们表明，该策略从根本上受到其在内存层次结构中的位置的限制：在两个代表性的 L1 预取器中，跨页预取仅实现高达 23.7% 的二级地址转换后备缓冲器 (STLB) 预热精度，并且许多有用的转换到达得太晚而无法隐藏页表遍历时延，从而使它们无法有效地预热 TLB。我们发现了 L2 预取的新机会。由于 L2 预取器的设计可以容忍数百个周期的时延，因此它们的跨页预取可以提供预热 TLB 所需的深度前瞻。然而，传统的物理寻址 L2 预取器会丢弃该信息，因为物理地址不像虚拟地址那样连续。我们表明，与独立的 TLB 预取器和基于 L1 的跨页预取方法相比，利用这些跨页预测来预热 TLB 可以显着提高转换预取精度和每周期指令数 (IPC)。我们提出了 TRANS-FETCH，一种轻量级的协作架构，它可以恢复这些被丢弃的跨页预测，并通过 16 项反向翻译缓存和低优先级翻译队列将它们转发到翻译子系统，总成本低于 0.3 KB，没有独立的页面级预测器，也没有对预取器、页表遍历器或一致性协议进行修改。在 Berti 已经执行 L1 跨页预取并预热 STLB 的基线上，TRANS-FETCH 实现了 70.2-74.4% 的翻译预热精度，而最先进的 (SOTA) 独立预测器 Agile TLB Prefetcher (ATP) 的翻译预热精度为 34.7-37.4%，并且在 SPEC 上将几何平均 IPC 提高了 1.78-3.83%（总体提高了 1.67-6.43%）三个架构不同的 L2 预取器，其中 ATP 最多提供 +0.3%。

## 中文关键词

预取；地址转换；跨页预取；反向地址转换；内存层次结构

## 代码与研究制品

- 代码与研究制品归档：[https://zenodo.org/records/21508114](https://zenodo.org/records/21508114)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6A](index.md) · [MICRO 2026 主页](../index.md)
