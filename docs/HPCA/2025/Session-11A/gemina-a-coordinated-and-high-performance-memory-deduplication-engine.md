---
title: "Gemina: A Coordinated and High-Performance Memory Deduplication Engine"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# Gemina: A Coordinated and High-Performance Memory Deduplication Engine

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Zhehua Zhang (Xiamen University), Suzhen Wu (Xiamen University), Wenyan You (Xiamen University), Chunfeng Du (Xiamen University), Bo Mao (Xiamen University)
**会议**：HPCA 2025

---

## 中文标题

Gemina：一个协同的高性能内存去重引擎

## 英文摘要

Memory deduplication is widely used to effectively reduce the memory footprint in operating systems, while huge pages are employed to enhance access performance by increasing TLB hit rates. Unfortunately, duplicate huge pages are very rare in memory, leading to most huge pages being split into base pages during deduplication, which degrades access performance by up to 43%. Although asynchronous huge page promotion attempts to elevate multiple base pages to huge pages to maximize performance, deduplication disrupts the uniformity of page attributes, limiting the effectiveness of such promotions. To address this problem, we designed Gemina, a new memory deduplication scheme that coordinates huge page management. Gemina employs a fine-grained detector to distinguish pages’ redundancy and hotness, a distributor to process pages conservatively and avoid frequent switches, and an adapter to organize memory for fast conversion. This approach balances the trade-off between performance and space efficiency in memory management. Experimental evaluations show that, compared to the naive KSM-based deduplication scheme, Gemina can achieve 96.1% of the memory savings of KSM while also improving memory access performance by 43.1% in random access.

## 中文摘要

内存去重被广泛用于有效降低操作系统的内存占用，而大页则通过提高 TLB 命中率来增强访问性能。不幸的是，内存中重复的大页非常罕见，导致大多数大页在去重过程中被拆分为基页，使访问性能最多下降 43%。尽管异步大页提升尝试将多个基页提升为大页以最大化性能，但去重破坏了页属性的统一性，限制了这类提升的效果。为解决该问题，我们设计了 Gemina，一种协同大页管理的新型内存去重方案。Gemina 采用细粒度检测器来区分页的冗余度与热度，采用分发器以保守方式处理页并避免频繁切换，还采用适配器来组织内存以实现快速转换。该方法在内存管理的性能与空间效率之间取得平衡。实验评估表明，与朴素的基于 KSM 的去重方案相比，Gemina 可达到 KSM 内存节省量的 96.1%，同时在随机访问中将内存访问性能提升 43.1%。
