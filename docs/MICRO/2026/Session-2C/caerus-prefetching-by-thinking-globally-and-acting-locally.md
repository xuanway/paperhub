---
title: "Caerus: Prefetching by Thinking Globally and Acting Locally"
description: "MICRO 2026 · Session 2C · Caerus：通过全局思考与局部行动实现预取"
tags:
  - "MICRO2026"
  - "Prefetching"
---

# Caerus: Prefetching by Thinking Globally and Acting Locally

**中文标题：** Caerus：通过全局思考与局部行动实现预取

**所属 Session：** [Session 2C](index.md) · [MICRO 2026](../index.md)

**作者：** Jacky Wong, Jacob Alexandrou, Yinting Huang, Luke Panayi, Lev Mukhanov, Sam Ainsworth, Paul H. J. Kelly

**来源：** MICRO 2026，pp. 676–690；[DOI](https://doi.org/10.1109/MICRO67795.2026.00059)

## 英文摘要

Modern processors rely heavily on data prefetching to bridge the growing performance gap between computation and memory accesses. In offset prefetching, prefetches are issued at an address delta relative to the most recently observed access, selecting deltas that have exhibited high coverage in the recent access-stream history. The Best-Offset Prefetcher (BOP) exemplifies this approach by selecting a single uniformly-issued global offset that delivers timely prefetches. However, its lack of context-sensitive accuracy tracking results in significantly increased DRAM traffic and sometimes disappointing performance. Conversely, Berti, the state-of-the-art offset prefetcher, achieves impressive prefetching performance and accuracy. However, its Program-Counter (PC)-local approach to extracting offsets limits its ability to capture global memory patterns, meaning there are many scenarios where simpler global offset prefetchers, such as BOP, outperform it. Observing the limitations of contemporary offset prefetchers, we present Caerus: an offset prefetcher that employs PC-local filtering on multiple non-overlapping globally derived offsets. Caerus extracts multiple offsets from the global memory trace and maximizes their combined coverage by training each offset only on accesses not already covered by previously learned offsets. The accuracy of each extracted offset is tracked per-PC based on whether it can cover future accesses for any PC. This allows Caerus to address complex delta patterns while maintaining high accuracy. In SPECspeed 2017, Caerus gains a geomean speedup of 8.3%, outperforming Berti by 2.0% while achieving low hardware and DRAM-traffic overhead.

## 中文摘要

现代处理器严重依赖数据预取来弥合计算和内存访问之间日益扩大的性能差距。在偏移预取中，预取是在相对于最近观察到的访问的地址增量处发出的，选择在最近访问流历史中表现出高覆盖率的增量。最佳偏移预取器 (BOP) 通过选择一个统一发布的全局偏移来提供及时的预取，从而举例说明了这种方法。然而，它缺乏上下文敏感的准确度跟踪，导致 DRAM 流量显着增加，有时性能令人失望。相反，最先进的偏移预取器 Berti 实现了令人印象深刻的预取性能和准确性。然而，其提取偏移量的程序计数器 (PC) 本地方法限制了其捕获全局内存模式的能力，这意味着在许多情况下，更简单的全局偏移量预取器（例如 BOP）的性能优于它。观察当代偏移预取器的局限性，我们提出了 Caerus：一种偏移预取器，它对多个非重叠的全局导出偏移量采用 PC 本地过滤。 Caerus 从全局内存跟踪中提取多个偏移量，并通过仅在先前学习的偏移量尚未覆盖的访问上训练每个偏移量来最大化它们的组合覆盖范围。根据每个 PC 是否可以覆盖任何 PC 的未来访问，跟踪每个提取的偏移量的准确性。这使得 Caerus 能够处理复杂的增量模式，同时保持高精度。在 SPECspeed 2017 中，Caerus 获得了 8.3% 的几何平均加速比，比 Berti 高出 2.0%，同时实现了较低的硬件和 DRAM 流量开销。

## 中文关键词

数据预取；硬件预取；缓存系统；微架构；全局与局部协同

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/jw38176/Caerus_Artifact](https://github.com/jw38176/Caerus_Artifact)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21512560](https://doi.org/10.5281/zenodo.21512560)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2C](index.md) · [MICRO 2026 主页](../index.md)
