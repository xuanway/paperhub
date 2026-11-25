---
title: "BCCE: Block-Centric GPU Co-Design for Real-Time Range-Top-K Query at Scale"
description: "HPDC 2026 · Session 10 — Data Systems for AI & Analytics"
tags:
  - "HPDC2026"
  - "Session 10"
  - "Data Systems for AI & Analytics"
---

# BCCE: Block-Centric GPU Co-Design for Real-Time Range-Top-K Query at Scale

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 10 — Data Systems for AI & Analytics（2026年7月16日 11:30–12:30 · Session Chair：Xiaoyi Lu）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 10</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807585)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#HuanMYLZWWMWZGW26](https://dblp.org/db/conf/hpdc/hpdc2026.html#HuanMYLZWWMWZGW26)

**作者**：Chengying Huan, Ziheng Meng, Zhengyi Yang, Yongchao Liu, Jie Zhang, Qing Wang, Jing Wang, Shaonan Ma, Zhibin Wang, Mingxing Zhang, Rong Gu, Baokun Wang, Guihai Chen, Chen Tian

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 10 — Data Systems for AI & Analytics（2026年7月16日 11:30–12:30 · Session Chair：Xiaoyi Lu）

---

## 英文摘要

Range-top-k queries retrieve the top-k elements within an arbitrary subrange of a large array and are a key primitive in real-time analytics. Unlike one-shot top-k selection, practical deployments issue large volumes of queries over varying and often overlapping ranges, frequently interleaved with streaming updates. In this setting, applying conventional GPU top-k kernels per query is inefficient: each query triggers range rescans or O(n)-scale passes that overwhelm HBM bandwidth, thrash on-chip caches, and provide little reuse across overlapping windows. We present BCCE, a GPU-co-designed, block-centric engine that makes range-top-k efficient by exposing a reusable intermediate representation of the data. BCCE partitions the array into locally sorted blocks and builds a compact interval-aware auxiliary index, reducing each query to a small set of contiguous active slices that remain amenable to SIMT execution. Queries are answered via a two-layer search: a global rank-thresholding step identifies the candidate value interval, followed by block-local verification restricted to the corresponding slices. This design constrains the active working set to O(√n) and achieves O(√n logn) per-query time with largely coalesced accesses and high on-chip reuse. To further improve throughput, BCCE employs a DP-based cache placement policy to keep hot slices resident in L2 or shared memory, and a range-grouped batching scheme that amortizes PCIe transfers for out-of-core datasets by reusing fetched slices across queries. Finally, BCCE supports incremental, block-local insertions and deletions without global rebuilds, sustaining performance under continuous data evolution. Across 17 datasets, including up to 70B elements (256 GB), BCCE achieves sub-millisecond query latency and up to 56,308× higher throughput than state-of-the-art GPU baselines, while performing billion-scale dynamic updates in milliseconds.

## 中文摘要

Range-top-k 查询用于检索大数组中任意子范围内的前 k 个元素，是实时分析的关键原语。与一次性 top-k 选择不同，实际部署会针对变化且常常重叠的范围发出大量查询，并频繁与流式更新交错。在这种场景下，对每个查询套用常规 GPU top-k 核效率低下：每次查询都会触发范围重扫描或 O(n) 量级的遍历，压垮 HBM 带宽、颠簸片上缓存，且难以在重叠窗口间复用。我们提出 BCCE，一个 GPU 协同设计的块中心（block-centric）引擎，通过暴露可复用的数据中间表示使 range-top-k 变得高效。BCCE 将数组划分为局部有序的块，并构建紧凑的区间感知辅助索引，将每个查询归约为少量连续的活动切片，这些切片仍适合 SIMT 执行。查询通过两层搜索回答：全局秩阈值化步骤确定候选值区间，随后是限制在相应切片上的块内验证。该设计将活动工作集约束在 O(√n)，并以基本合并的访问和高片上复用实现 O(√n log n) 的单查询时间。为进一步提升吞吐，BCCE 采用基于动态规划（DP）的缓存放置策略，将热切片常驻于 L2 或共享内存，并采用 range 分组批处理方案，通过在查询间复用已取切片来摊销外存数据集的 PCIe 传输。最后，BCCE 支持增量式块内插入与删除而无需全局重建，在持续数据演化下保持性能。在包括多达 700 亿元素（256 GB）在内的 17 个数据集上，BCCE 实现亚毫秒级查询延迟，吞吐比最先进 GPU 基线最高提升 56,308 倍，同时能在毫秒级完成十亿规模的动态更新。

## 英文关键词

GPU computing, Range-Top-k, Parallel algorithms

## 中文关键词

GPU 计算，Range-Top-k，并行算法

---

[← 返回 Session 10 — Data Systems for AI & Analytics](index.md)
