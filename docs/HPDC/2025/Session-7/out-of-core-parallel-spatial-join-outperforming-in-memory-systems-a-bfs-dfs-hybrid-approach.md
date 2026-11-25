---
title: "Out-of-Core Parallel Spatial Join Outperforming In-Memory Systems: A BFS-DFS Hybrid Approach"
description: "HPDC 2025 · Session 7 — Best Paper and Best Student Paper Finalists"
tags:
  - "HPDC2025"
  - "Session 7"
  - "Best Paper and Best Student Paper Finalists"
---

# Out-of-Core Parallel Spatial Join Outperforming In-Memory Systems: A BFS-DFS Hybrid Approach

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 7 — Best Paper and Best Student Paper Finalists（2025年7月23日 13:00–14:30 · Session Chair：Robert Wisniewski）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 7</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731572)

**作者**：Lyuheng Yuan, Da Yan, Akhlaque Ahmad, Jiao Han, Saugat Adhikari, Yang Zhou

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 7 — Best Paper and Best Student Paper Finalists（2025年7月23日 13:00–14:30 · Session Chair：Robert Wisniewski）

**荣誉**：HPDC 2025 最佳论文（Best Paper）

---

## 英文摘要

Spatial join is a fundamental operation in many applications such as geographic information system (GIS) and simulation sciences. Recent works advocate in-memory spatial join for efficiency, but they require entire datasets to be loaded into memory, and they were only tested on small to medium-sized datasets. In this paper, we target out-of-core parallel spatial join to handle massive data, and surprisingly, we find that our solution can be orders of magnitude faster than the state-of-the-art in-memory solutions. Our system, called T-Spatial, decomposes a spatial-join job into tasks to expose massive parallelism opportunities. A BFS-DFS hybrid execution model is designed to enable memory-bounded high-throughput task processing, which exploits spatial locality to reuse cached data as much as possible to reduce disk IOs. T-Spatial also effectively overlaps computations with disk IOs by prefetching, and integrates a few optimization techniques including work stealing to avoid stragglers, write contention mitigation under multithreading, and a NUMA-aware design. Extensive experiments show that T-Spatial significantly outperforms state-of-the-art in-memory approaches (e.g., PBSM, TOUCH) and cloud-based parallel spatial systems (e.g., Apache Sedona) with 2–3 orders of magnitude of speedup ratio, and it is the first in the literature to test spatial joins on billion-scale datasets.

## 中文摘要

空间连接是地理信息系统（GIS）与仿真科学等许多应用中的基础操作。近期工作主张采用内存空间连接以提升效率，但它们需要将整个数据集加载到内存，且仅在小到中等规模数据集上测试过。本文面向外存并行空间连接以处理海量数据，并且令人惊讶地发现，我们的方案可以比最先进的内存方案快数个数量级。我们的系统 T-Spatial 将空间连接作业分解为任务，以释放海量并行机会。设计了 BFS-DFS 混合执行模型，实现内存受限的高吞吐任务处理，利用空间局部性尽可能复用缓存数据以减少磁盘 I/O。T-Spatial 还通过预取有效重叠计算与磁盘 I/O，并集成若干优化技术，包括用于避免慢节点的工作窃取、多线程下的写争用缓解，以及 NUMA 感知设计。大量实验表明，T-Spatial 显著优于最先进的内存方案（如 PBSM、TOUCH）和基于云的并行空间系统（如 Apache Sedona），加速比达 2–3 个数量级，并且是文献中首个在十亿规模数据集上测试空间连接的工作。

---

[← 返回 Session 7 — Best Paper and Best Student Paper Finalists](index.md)
