---
title: "Streamlined On-Chip Temporal Prefetching"
description: "HPCA 2026 · Caching and Prefetching"
tags:
  - "HPCA2026"
  - "Caching and Prefetching"
---

# Streamlined On-Chip Temporal Prefetching

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Caching and Prefetching。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Caching and Prefetching</p>
</div>

**论文链接**：
**作者**：Quang Duong The University of Texas at Austin , Calvin Lin The University of Texas at Austin
**会议**：HPCA 2026

---

## 中文标题

精简的片上时序预取

## 英文摘要

In this paper, we present the Streamline temporal prefetcher, which introduces a stream-based metadata representation that produces three significant benefits over Triangel, the previous state-of-the-art in temporal prefetching. First, it removes redundancy present in Triangel’s metadata. Second, it prioritizes the storage of those metadata entries that have higher prefetch utility. Third, it eliminates the need for the untenable LLC traffic that is induced when Triangel dynamically adjusts the size of its metadata store. The end result is that for memory-intensive SPEC 2006, SPEC 2017, and GAP benchmarks, Streamline outperforms Triangel by 6.7 percentage points on an 8-core system with a stride prefetcher. This performance benefit comes from Streamline’s improved storage efficiency: It holds 33% more correlations than Triangel, which translates to 12.5 percentage points better prefetch coverage. Significantly, Streamline matches the performance of Triangel even when Triangel is given twice the metadata storage.

## 中文摘要

本文提出名为 Streamline 的时序预取器，它引入一种基于流的元数据表示方式，相比时序预取领域此前最先进的 Triangel，这一表示方式带来了三项显著优势。第一，它消除了 Triangel 的元数据中所存在的冗余信息。第二，它对那些具有更高预取效用的元数据条目予以优先存储。第三，它消除了 Triangel 在动态调整其元数据存储容量时所引发的、难以承受的 LLC 流量。最终的结果便是，在配备步幅预取器的 8 核系统上，针对内存密集型的 SPEC 2006、SPEC 2017 与 GAP 基准测试，Streamline 的性能比 Triangel 高出 6.7 个百分点。这一性能收益源自 Streamline 更高的存储效率：它所保存的关联数量比 Triangel 多出 33%，这转化为 12.5 个百分点的预取覆盖率提升。值得注意的是，即使给 Triangel 提供两倍的元数据存储空间，Streamline 仍能达到与 Triangel 相当的性能水平。
