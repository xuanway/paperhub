---
title: "STEP: Spatial Footprint Prefetcher with Multi-Point Temporal Triggers"
description: "ISCA 2026 · Session 5D · STEP: Spatial Footprint Prefetcher with Multi-Point Temporal Triggers"
tags:
  - "ISCA2026"
  - "Session 5D"
  - "Potpourri"
---

# STEP: Spatial Footprint Prefetcher with Multi-Point Temporal Triggers

**中文标题：** STEP: 具备多点时间触发的空间足迹预取器

**所属 Session：** [Session 5D](index.md) · [ISCA 2026](../index.md)

**作者：** Yuanji Ye, Oliver Lenke, Thomas Wild, Andreas Herkersdorf

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Modern processors continue to face the memory wall, which heavily impacts computer performance. Besides sophisticated cache hierarchies, prefetching is a proven technique to hide latency and mitigate the problem. Spatial footprint prefetchers have attracted research interest due to their ability to cover diverse memory access patterns with relatively low hardware cost. However, current implementations trigger on a single-point-in-time event, forcing a trade-off between issuing prefetches early, which increases noise, and issuing them later, which reduces opportunities. We propose STEP, a spatial footprint prefetcher that introduces multiple sequential temporal decision points within a page’s cache lifetime and selectively issues prefetches when confidence is high. STEP coordinates these decisions through a lightweight prefetch-confidence evaluator, enabling early opportunities while retaining high accuracy with later prefetching triggers. Moreover, STEP consolidates metadata into a single Pattern History Table (PHT), reducing storage overhead. Experimental results on SPEC CPU2006, SPEC CPU2017, and CloudSuite show that STEP improves performance across a broad range of workloads. In the L2 single-core evaluation, STEP remains ahead of the strengthened ISO-storage baseline eBingo, while in the L1 single-core evaluation, STEP further outperforms Gaze, the strongest baseline at that level. STEP also delivers a stronger performance–storage trade-off, as eBingo requires substantially larger metadata capacity to approach STEP’s low-storage operating point.

## 中文摘要

现代处理器仍面临内存墙问题，这严重影响计算机性能。除精巧的缓存层次结构外，预取是被证明可隐藏延迟、缓解该问题的技术。空间足迹预取器因能以相对较低的硬件成本覆盖多样化的内存访问模式而受到研究关注。然而，当前的实现仅在单一时点事件上触发，因而不得不在提早发起预取（增加噪声）与延后发起预取（减少机会）之间权衡。我们提出 STEP，一种空间足迹预取器，它在页面的缓存生命周期内引入多个顺序的时间决策点，并在置信度高时选择性地发起预取。STEP 通过一个轻量级的预取置信度评估器协调这些决策，从而既能抓住早期机会，又能借助较晚的预取触发保持高准确率。此外，STEP 将元数据整合到单个模式历史表（PHT）中，从而降低存储开销。在 SPEC CPU2006、SPEC CPU2017 和 CloudSuite 上的实验结果表明，STEP 在广泛负载上均提升了性能。在 L2 单核评估中，STEP 领先于经强化、存储容量相同的基线 eBingo；在 L1 单核评估中，STEP 进一步优于该层级最强的基线 Gaze。STEP 还提供了更强的性能—存储权衡：eBingo 需要显著更大的元数据容量才能接近 STEP 的低存储工作点。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5D](index.md) · [返回 ISCA 2026](../index.md)
