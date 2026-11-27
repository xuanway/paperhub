---
title: "Efficient Caching with A Tag-enhanced DRAM"
description: "HPCA 2025 · Cacheno Royale"
tags:
  - "HPCA2025"
  - "Cacheno Royale"
---

# Efficient Caching with A Tag-enhanced DRAM

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Cacheno Royale。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Cacheno Royale</p>
</div>

**论文链接**：
**作者**：Maryam Babaie (University of California Davis), Ayaz Akram (Samsung Electronics), Wendy Elsasser (Rambus Inc.), Brent Haukness (Rambus Inc.), Michael R. Miller (Rambus Inc.), Taeksang Song (Samsung Electronics), Thomas Vogelsang (Rambus Inc.), Steven C. Woo (Rambus Inc.), Jason Lowe-Power (University of California, Davis)
**会议**：HPCA 2025

---

## 中文标题

采用标签增强型 DRAM 的高效缓存

## 英文摘要

As SRAM-based caches are hitting a scaling wall, manufacturers are integrating DRAM-based caches into system designs to continue increasing cache sizes. While DRAM caches can improve the performance of memory systems, existing DRAM cache designs suffer from high miss penalties, wasted data movement, and interference between misses and demands. In this paper, we propose TDRAM, a novel DRAM microarchitecture tailored for caching. TDRAM enhances existing DRAM, such as HBM3, by adding small, low-latency mats to store tags and metadata on the same die as the data mats. These mats enable tag and data access in lockstep, in-DRAM tag comparison, and conditional data response based on the comparison result (reducing wasted data transfers), akin to SRAM cache mechanisms. TDRAM further optimizes hit and miss latencies through opportunistic early tag probing. Moreover, TDRAM introduces a flush buffer to store conflicting dirty data on write misses, eliminating data bus turnaround delays on write demands. We evaluate TDRAM in a full-system simulation using a set of HPC workloads with large memory footprints, showing that TDRAM, on average, provides 2.65× faster tag checks, 1.23× speedup, and 21% less energy consumption compared to state-of-the-art commercial and research designs.

## 中文摘要

随着基于 SRAM 的缓存在扩展上遭遇瓶颈，厂商正把基于 DRAM 的缓存集成进系统设计，以继续增大缓存容量。虽然 DRAM 缓存可以提升内存系统的性能，但现有 DRAM 缓存设计仍受制于高缺失代价、无效的数据搬移以及缺失与需求之间的相互干扰。本文提出 TDRAM，一种专为缓存定制的新型 DRAM 微架构。TDRAM 增强 HBM3 等现有 DRAM，在与数据 mat 相同的 die 上增加小而低延迟的 mat 来存放标签与元数据。这些 mat 使标签与数据能够同步访问、实现 DRAM 内标签比较，并依据比较结果有条件地返回数据（减少无效的数据传输），类似于 SRAM 缓存机制。TDRAM 进一步通过机会式提前标签探查来优化命中与缺失时延。此外，TDRAM 引入冲刷缓冲区，在写缺失时存放冲突的脏数据，从而消除写需求时的数据总线转向延迟。我们在全系统仿真中使用一组具有大内存占用的 HPC 负载评估 TDRAM，结果表明，与最先进的商业与学术设计相比，TDRAM 平均提供 2.65 倍更快的标签检查、1.23 倍的加速比以及 21% 的能耗降低。
