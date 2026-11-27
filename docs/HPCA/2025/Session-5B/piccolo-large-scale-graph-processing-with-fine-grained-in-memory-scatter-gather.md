---
title: "Piccolo: Large-Scale Graph Processing with Fine-Grained In-Memory Scatter-Gather"
description: "HPCA 2025 · Doubling Down with PIM"
tags:
  - "HPCA2025"
  - "Doubling Down with PIM"
---

# Piccolo: Large-Scale Graph Processing with Fine-Grained In-Memory Scatter-Gather

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Doubling Down with PIM。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Doubling Down with PIM</p>
</div>

**论文链接**：
**作者**：Changmin Shin (Seoul National University), Jaeyong Song (Seoul National University), Hongsun Jang (Seoul National University), Dogeun Kim (Seoul National University), Jun Sung (Seoul National University), Taehee Kwon (Seoul National University), Jae Hyung Ju (Seoul National University), Frank Liu (Old Dominion University), Yeonkyu Choi (Samsung), Jinho Lee (Seoul National University)
**会议**：HPCA 2025

---

## 中文标题

Piccolo：基于细粒度存内散射-收集的大规模图处理

## 英文摘要

Graph processing requires irregular, fine-grained random access patterns incompatible with contemporary off-chip memory architecture, leading to inefficient data access. This inefficiency makes graph processing an extremely memory-bound application. Because of this, existing graph processing accelerators typically employ a graph tiling-based or processing-in-memory (PIM) approach to relieve the memory bottleneck. In the tiling-based approach, a graph is split into chunks that fit within the on-chip cache to maximize data reuse. In the PIM approach, arithmetic units are placed within memory to perform operations such as reduction or atomic addition. However, both approaches have several limitations, especially when implemented on current memory standards (i.e., DDR). Because the access granularity provided by DDR is much larger than that of the graph vertex property data, much of the bandwidth and cache capacity are wasted. PIM is meant to alleviate such issues, but it is difficult to use in conjunction with the tiling-based approach, resulting in a significant disadvantage. Furthermore, placing arithmetic units inside a memory chip is expensive, thereby supporting multiple types of operation is thought to be impractical. To address the above limitations, we present Piccolo, an end-to-end efficient graph processing accelerator with fine-grained in-memory random scatter-gather. Instead of placing expensive arithmetic units in off-chip memory, Piccolo focuses on reducing the off-chip traffic with non-arithmetic function-in-memory of random scatter-gather. To fully benefit from in-memory scatter-gather, Piccolo redesigns the cache and miss-handling architecture (MHA) of the accelerator such that it can enjoy both the advantage of tiling and in-memory operations. Piccolo achieves a maximum speedup of 3.28× and a geometric mean speedup of 1.62×, along with up to 59.7% reduction in energy consumption across various and extensive benchmarks.

## 中文摘要

图处理需要不规则、细粒度的随机访问模式，这与当代片外内存架构不兼容，导致数据访问效率低下。这使其成为极度受限于内存的应用。因此，现有图处理加速器通常采用基于图分块或存内处理（PIM）的方法来缓解内存瓶颈。在基于分块的方法中，图被切分为可放入片上缓存的块以最大化数据复用。在 PIM 方法中，算术单元被放置在内存内部以执行归约或原子加等操作。然而，这两种方法都有若干局限，尤其是在当前内存标准（即 DDR）上实现时。因为 DDR 提供的访问粒度远大于图顶点属性数据的粒度，大量带宽与缓存容量被浪费。PIM 本意是缓解此类问题，却难以与基于分块的方法结合，反而带来明显劣势。此外，将算术单元放入内存芯片代价高昂，因此支持多种操作类型被认为不切实际。为解决上述局限，我们提出 Piccolo，一种具备细粒度存内随机散射-收集的端到端高效图处理加速器。Piccolo 不在片外内存中放置昂贵的算术单元，而是聚焦于以非算术的随机散射-收集存内功能来减少片外流量。为充分受益于存内散射-收集，Piccolo 重新设计了加速器的缓存与缺失处理架构（MHA），使其既能享受图分块的优势，又能利用存内操作。在大量基准测试上，Piccolo 取得最高 3.28× 的加速比与 1.62× 的几何平均加速比，同时能耗最多降低 59.7%。
