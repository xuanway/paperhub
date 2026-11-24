---
title: "R-Max: Extending Bélády’s MIN with Prefetching to Bound Realistic Cache Performance"
description: "ISCA 2026 · Session 9B · R-Max: Extending Bélády’s MIN with Prefetching to Bound Realistic Cache Performance"
tags:
  - "ISCA2026"
  - "Session 9B"
  - "Prefetching and Cache 2"
---

# R-Max: Extending Bélády’s MIN with Prefetching to Bound Realistic Cache Performance

**中文标题：** R-Max: 以预取扩展 Bélády 的 MIN 来界定现实缓存性能的上界

**所属 Session：** [Session 9B](index.md) · [ISCA 2026](../index.md)

**作者：** Lei Wang, Chia-Hang Lee, Maccoy Merrell, Gino Chacon, Daniel A. Jiménez, Paul V. Gratz

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Memory performance continues to lag behind the demand of processing elements, a well-known phenomenon known as the memory wall. Cache prefetching is a well-studied and effective method to bridge this gap. Despite a long history of study and the existence of many prefetchers, an open question remains with respect to the upper bound of performance that might be had from prefetching. A “perfect cache” where all accesses hit is often used as an upper bound. However, as we show, this bound is very unrealistic given bandwidth and miss status holding register (MSHR) constraints. Here, we propose a system, R-Max, to approximate ideal prefetching and replacement policy with realistic constraints on bandwidth, cache structure, and capacity but oracular knowledge of future accesses. We compare R-Max’s approximated ideal speedup against the speedup of current state-of- the-art prefetchers to show how much remaining performance gain may be left for prefetching. We show that, for a set of workloads taken from SPEC CPU2017, CVP, GAP and XSBench, up to 299.6% maximum and 72.6% average gains are possible under realistic assumptions for a prefetcher that perfectly predicts future accesses, outperforming current state-of-the-art prefetchers by 60.8%. Interestingly, we see that the workloads where R-Max shows the most potential have little relationship with those where existing prefetchers perform best. Taken together, our results highlight the need for new research into prefetching techniques for these under-exploited workloads.

## 中文摘要

内存性能持续落后于处理单元的需求，这一众所周知的现象被称为内存墙。缓存预取是一种经过充分研究且有效的弥合这一差距的方法。尽管研究历史悠久且存在许多预取器，但关于预取可能带来的性能上界仍是一个悬而未决的问题。一个所有访问都命中的“完美缓存”常被用作性能上界。然而，正如我们所展示的，考虑到带宽和未命中状态保持寄存器（MSHR）约束，这一上界非常不现实。在此，我们提出一个系统 R-Max，在带宽、缓存结构和容量受到现实约束但拥有未来访问的神谕式知识的情况下，逼近理想的预取和替换策略。我们将 R-Max 逼近的理想加速比与当前最先进预取器的加速比进行比较，以展示预取还剩下多少性能提升空间。我们表明，对于从 SPEC CPU2017、CVP、GAP 和 XSBench 中选取的一组工作负载，在现实假设下，一个能完美预测未来访问的预取器最多可实现 299.6% 的最大增益和 72.6% 的平均增益，比当前最先进的预取器高出 60.8%。有趣的是，我们发现 R-Max 展现出最大潜力的工作负载与现有预取器表现最佳的工作负载几乎没有关系。综上所述，我们的结果凸显了针对这些尚未被充分利用的工作负载开展新的预取技术研究的必要性。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9B](index.md) · [返回 ISCA 2026](../index.md)
