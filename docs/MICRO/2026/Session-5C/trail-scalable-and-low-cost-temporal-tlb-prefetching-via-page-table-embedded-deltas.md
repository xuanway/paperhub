---
title: "Trail: Scalable and Low-Cost Temporal TLB Prefetching via Page-Table-Embedded Deltas"
description: "MICRO 2026 · Session 5C · Trail：通过页表内嵌差分实现可扩展低成本时序 TLB 预取"
tags:
  - "MICRO2026"
  - "Prefetching"
  - "Address Translation"
---

# Trail: Scalable and Low-Cost Temporal TLB Prefetching via Page-Table-Embedded Deltas

**中文标题：** Trail：通过页表内嵌差分实现可扩展低成本时序 TLB 预取

**所属 Session：** [Session 5C](index.md) · [MICRO 2026](../index.md)

**作者：** Konstantinos Kanellopoulos, Konstantinos Sgouras, Harsh Songara, Rahul Bera, Onur Mutlu

**来源：** MICRO 2026，pp. 1746–1766；[DOI](https://doi.org/10.1109/MICRO67795.2026.00125)

## 英文摘要

Address translation is a significant performance bottleneck in modern data-intensive workloads. Prefetching virtual-to-physical address mappings into the TLBs and the cache hierarchy before they are demanded is a promising technique to hide address translation latency. However, accurately capturing address translation patterns is challenging as translation-intensive workloads often exhibit irregular memory access patterns. Existing TLB prefetchers have two key shortcomings: (i) spatial prefetchers fail to capture irregular translation patterns, and (ii) temporal prefetchers record address deltas (i.e., distances between virtual memory regions that successively trigger page table walks) in fixed-capacity hardware structures that cannot scale with the application's memory footprint. In this work, we conduct a large-scale study across 200 translation-intensive workloads and find that, despite the irregularity of the applications' memory accesses, deltas exhibit a highly predictable structure: (i) for a given virtual memory region, the set of candidate deltas is small and recurring, and (ii) more than 95% of observed deltas fit in an 18-bit signed representation. We introduce Trail, a new temporal TLB prefetcher that embeds deltas directly in unused bits of the last-level entries of the page table (PTEs) to enable effective, low-cost, and scalable prefetching. When a virtual memory region (the destination region) triggers a page table walk, Trail identifies the region (the source region) that last triggered a walk from the same instruction and records the delta between the two in the source region's PTE. The next time a page table walk fetches the source region's PTE, Trail retrieves the recorded deltas at no additional memory access cost, identifies the regions most likely to trigger the next page table walks and prefetches the corresponding PTEs into the TLBs and the cache hierarchy. Trail comes with three key benefits: (i) compactly storing multiple deltas in a single PTE enables Trail to issue prefetches for multiple destination regions, improving prefetch coverage, (ii) embedding deltas in PTEs requires no dedicated SRAM or extra memory capacity, and (iii) since deltas reside in PTEs already allocated by the application, prefetch metadata capacity scales with the application's memory footprint at no extra cost. Our evaluation shows that Trail improves performance in single-core (four-core) systems by 5.5% (11.0%) on average over a no-prefetch baseline across 200 translation-intensive workloads (100 multiprogrammed mixes), outperforming the second-best TLB prefetcher by 2.2% (6.1%). These gains come at a very small hardware cost: Trail requires only a 64-entry PC table since all prefetch metadata resides in the page table. Trail is freely available at github.com/CMU-SAFARI/Virtuoso/TRAIL.

## 中文摘要

地址转换是现代数据密集型工作负载中的一个重要性能瓶颈。在需要之前将虚拟到物理地址映射预取到 TLB 和缓存层次结构中，是一种隐藏地址转换时延的有前途的技术。然而，准确捕获地址转换模式具有挑战性，因为转换密集型工作负载通常表现出不规则的内存访问模式。现有的 TLB 预取器有两个主要缺点：(i) 空间预取器无法捕获不规则的转换模式，(ii) 时间预取器在无法随应用程序的内存占用扩展的固定容量硬件结构中记录地址增量（即，连续触发页表遍历的虚拟内存区域之间的距离）。在这项工作中，我们对 200 个翻译密集型工作负载进行了大规模研究，发现尽管应用程序的内存访问不规则，但增量表现出高度可预测的结构：(i) 对于给定的虚拟内存区域，候选增量集很小且重复出现，(ii) 超过 95% 的观察到的增量适合 18 位有符号表示。我们引入了 Trail，这是一种新的时序 TLB 预取器，它将增量直接嵌入页表 (PTE) 最后一级条目的未使用位中，以实现有效、低成本且可扩展的预取。当虚拟内存区域（目标区域）触发页表遍历时，Trail 会识别上次从同一指令触发页表遍历的区域（源区域），并将两者之间的增量记录在源区域的 PTE 中。下次页表遍历获取源区域的 PTE 时，Trail 会检索记录的增量，无需额外的内存访问成本，识别最有可能触发下一次页表遍历的区域，并将相应的 PTE 预取到 TLB 和缓存层次结构中。 Trail 具有三个主要优点：(i) 在单个 PTE 中紧凑地存储多个增量，使 Trail 能够为多个目标区域发出预取，从而提高预取覆盖率；(ii) 在 PTE 中嵌入增量不需要专用 SRAM 或额外的内存容量；(iii) 由于增量驻留在应用程序已分配的 PTE 中，因此预取元数据容量可随应用程序的内存占用而扩展，无需额外成本。我们的评估表明，在 200 个翻译密集型工作负载（100 个多程序混合）中，Trail 在单核（四核）系统中的性能比无预取基准平均提高了 5.5% (11.0%)，比第二好的 TLB 预取器高出 2.2% (6.1%)。这些收益是以非常小的硬件成本实现的：Trail 仅需要一个 64 条目的 PC 表，因为所有预取元数据都驻留在页表中。 Trail 可在 github.com/CMU-SAFARI/Virtuoso/TRAIL 免费获取。

## 中文关键词

地址转换后备缓冲器；时序预取；页表；增量编码；硬件开销

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/CMU-SAFARI/Virtuoso/tree/trail-artifact-release](https://github.com/CMU-SAFARI/Virtuoso/tree/trail-artifact-release)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21541804](https://doi.org/10.5281/zenodo.21541804)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 5C](index.md) · [MICRO 2026 主页](../index.md)
