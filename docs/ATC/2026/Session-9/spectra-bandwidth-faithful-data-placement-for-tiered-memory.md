# Spectra: Bandwidth-Faithful Data Placement for Tiered Memory

**中文标题**：Spectra：面向分层内存的带宽保真数据放置

**所属 Session**：[Session 9: Memory Tiering and Management](index.md) · [ATC 2026](../index.md)

**作者**：Jiahui Zhang (Huazhong University of Science and Technology), Qiang Cao (Huazhong University of Science and Technology), Hong Jiang (UT Arlington)

## 英文摘要
Tiered memory systems rely mainly on page-table (PT) scanning or precise event-based sampling (PEBS) to track memory accesses and guide data placement. The tracked accesses are used to quantify data hotness and reflect how intensely data accesses memory. However, we find that the accesses observed by PT and PEBS are not equal to the accesses that reach physical memory, because the cache hierarchy filters and hides the interaction between cores and memory. PT observes accesses before the cache hierarchy and intercepts cache hits that never touch memory. PEBS typically samples LLC misses, so it overlooks prefetches and requests for ownership. This mismatch matters because the performance of tiered systems is increasingly bandwidth-bound, while existing tracking methods do not faithfully reflect the bandwidth consumed by data. We observe 20% to 30% slowdowns in state-of-the-art systems for modern applications. We present Spectra, a tiered memory system that places data by actual memory access intensity (AMAI), the rate at which each object transfers cachelines between the cache hierarchy and physical memory. AMAI counts exactly what physical memory serves. It excludes cache hits that mislead PT and includes the hidden traffic missed by PEBS. Ranking objects by AMAI therefore enables bandwidth-faithful placement. The difficulty is that memory traffic arrives mixed with no provenance. Spectra first builds an analytical model that decomposes the mixed traffic into semantically distinct request classes, each induced by a distinct architectural mechanism. Then each class is attributed to its originating objects through the signal exposed by the corresponding mechanism. Finally, a two-regime policy places data by the recovered AMAI, maximizing aggregate bandwidth utilization. In our evaluation, Spectra reduces execution time by 14.26%–17.45% over the best baseline on memory-intensive applications.

## 中文摘要
分层内存系统主要依赖页表（PT）扫描或基于事件的精确采样（PEBS）来跟踪内存访问并指导数据放置。所跟踪的访问被用于量化数据的热度，并反映数据访问内存的强度。然而，我们发现 PT 与 PEBS 观测到的访问并不等于真正到达物理内存的访问，因为缓存层次结构对核心与内存之间的交互进行了过滤和隐藏。PT 在缓存层次结构之前观测访问，会拦截那些从未触及内存的缓存命中。PEBS 通常对 LLC 未命中进行采样，因此会遗漏预取和请求所有权（RFO）的流量。这种不匹配之所以重要，是因为分层系统的性能正日益受限于带宽，而现有的跟踪方法并不能忠实反映数据所消耗的带宽。我们在最先进的系统中观察到现代应用出现 20% 到 30% 的减速。我们提出 Spectra，一个按实际内存访问强度（AMAI）放置数据的分层内存系统，AMAI 即每个对象在缓存层次结构与物理内存之间传输缓存行的速率。AMAI 精确地统计物理内存实际服务的流量。它排除了误导 PT 的缓存命中，并包含了 PEBS 遗漏的隐藏流量。因此，按 AMAI 对对象排序可实现带宽保真的放置。困难在于内存流量到达时混杂在一起且没有来源信息。Spectra 首先构建一个分析模型，将混杂流量分解为语义上不同的请求类别，每一类都由一种不同的体系结构机制引起。然后，通过相应机制所暴露的信号将每个类别归因到其来源对象。最后，一种双区制策略按恢复出的 AMAI 放置数据，从而最大化总体带宽利用率。在我们的评估中，Spectra 在内存密集型应用上相比最佳基线将执行时间减少 14.26%–17.45%。

## 英文关键词
tiered memory, CXL memory, memory bandwidth

## 中文关键词
分层内存，CXL 内存，内存带宽

[返回 Session 9](index.md) · [返回 ATC 2026](../index.md)
