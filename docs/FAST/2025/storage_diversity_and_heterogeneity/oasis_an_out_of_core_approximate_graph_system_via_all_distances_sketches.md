---
title: "Oasis: An Out-of-core Approximate Graph System via All-Distances Sketches"
description: "FAST 2025 · Storage Diversity and Heterogeneity · 把 ADS 图处理搬到外存：内存省 13.8 倍，构图仅慢 1.8 倍"
tags:
  - "FAST2025"
  - "Storage Diversity and Heterogeneity"
  - "All-Distances Sketch"
  - "out-of-core graph processing"
---

# Oasis: An Out-of-core Approximate Graph System via All-Distances Sketches

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">ADS 能把图邻域查询加速数个数量级，但构建全部顶点的草图需要图本身 30 到 60 倍的内存，已有实现只能全内存运行。Oasis 把草图构建与估计搬到外存，用分区、无锁边布局与查询重调度换取 13.8 倍内存节省，构图与估计仅慢约 1.8 倍与 1.7 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Storage Diversity and Heterogeneity</p>
</div>

**中文标题**：Oasis：基于全距离草图的外存近似图系统

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/yang](https://www.usenix.org/conference/fast25/presentation/yang)

**论文 PDF**：[fast25-yang.pdf](https://www.usenix.org/system/files/fast25-yang.pdf)

**作者**：Tsun-Yu Yang（The Chinese University of Hong Kong (CUHK)）；Yi Li（The University of Texas at Dallas）；Yizou Chen（The Chinese University of Hong Kong (CUHK)）；Bingzhe Li（The University of Texas at Dallas）；Ming-Chang Yang（The Chinese University of Hong Kong (CUHK)）

**会议**：FAST 2025 · Santa Clara, CA · 第 523–537 页

**Session**：Storage Diversity and Heterogeneity · 2025-02-27 10:50–12:10 · Chair：Avani Wildani（Cloudflare and Emory University）

**所属 Session**：[Storage Diversity and Heterogeneity](index.md) · [FAST 2025](../index.md)

**关键词**：All-Distances Sketch, out-of-core graph processing, approximate graph queries, neighborhood sketching, storage I/O

---

## 英文摘要

The All-Distances Sketch (ADS) is a powerful and theoretically-sound sketching scheme that captures neighborhood information in graphs for approximate processing. It enables high-accuracy estimation of many useful applications with a guarantee of accuracy and can significantly accelerate the execution times by orders of magnitude. However, ADS requires a substantial amount of space that is multiple times larger than the graph data. More seriously, existing studies mainly focus on managing ADSs in memory, posing an increasing challenge for users who aim to leverage ADS for large-scale graph processing, particularly in light of the exponential growth of real-world graphs nowadays.

To this end, this paper introduces Oasis, an O ut-of-core A pproximate graph SYS tem that brings the ADS technique into practical use by leveraging storage effectively. Specifically, Oasis offers a holistic framework that facilitates both ADS construction and estimation. For ADS construction, it allows users to adjust the memory usage based on the machine’s available memory and enable an efficient construction process. For ADS estimation, Oasis provides a user-friendly interface to easily execute the estimators while mitigating the impact of slow storage I/O. Evaluation results show that Oasis provides a practical graph processing solution with exceptional execution time and low memory usage, at the cost of a slight decrease in accuracy.

## 中文摘要

全距离草图（All-Distances Sketch，ADS）是一种强大且理论完备的草图方案，它刻画图中的邻域信息以支持近似处理。ADS 能以精度保证对许多有用的应用场景进行高精度估计，并可将执行时间加速数个数量级。然而，ADS 需要大量空间，可达图数据的数倍。更严重的是，已有研究主要在内存中管理 ADS，这对希望利用 ADS 进行大规模图处理的用户构成了日益严峻的挑战，尤其考虑到当今真实图数据的指数级增长。为此，本文提出 Oasis——一种外存近似图系统，通过有效利用存储把 ADS 技术带入实际应用。具体而言，Oasis 提供了一个同时支持 ADS 构建与估计的整体框架。在 ADS 构建方面，它允许用户根据机器可用内存调整内存使用，并实现高效的构建过程。在 ADS 估计方面，Oasis 提供用户友好的接口，便于执行估计器，同时缓解慢速存储 I/O 的影响。评估结果表明，Oasis 以轻微精度下降为代价，提供了具有出色执行时间与低内存占用的实用图处理方案。

## 一句话总结

> ADS 的瓶颈不是精度而是内存：把草图放进外存、按内存预算分区构图，就能用 1.8 倍时间换 13.8 倍内存。

## 研究背景与问题

- **邻域查询的代价**：社交网络影响力分析、推荐系统等应用需要对大量甚至全部顶点做图遍历，图规模指数增长后，精确遍历难以在可接受时间内完成。
- **ADS 的代价**：All-Distances Sketch 为每个顶点保存到采样地标的距离摘要，是唯一同时具备多功能、可调精度保证与近线性构图复杂度的草图方案，但构建全部顶点的 ADS 需要图本身 30 到 60 倍的内存——512 GB 的图就要 30 TB，普通机器无法承受。
- **已有实现的局限**：现有 ADS 研究集中在理论，实验都在全内存环境、相对较小的图上完成；而外存图处理系统按每轮活跃顶点 O(V) 设计，ADS 需对所有顶点做有界遍历，活跃顶点可达 O(V²)，直接套用会耗尽内存或产生大量 I/O。
- **切入点**：不改动 ADS 理论，只在系统层为构图与估计分别设计外存路径，让内存占用成为用户可调的旋钮。

## 核心贡献

- **首个外存 ADS 系统**：提出 Oasis，把 ADS 构建与估计统一进一个外存框架，用户可按机器可用内存调节占用。
- **分区式构建**：把图划分为 P 个分区，按分区把活跃顶点的 ADS 换入内存，用分区数在内存与 I/O 之间取舍。
- **构建期系统优化**：无锁边布局消除线程同步开销，活跃数据分离与选择性 ADS 访问减少不必要的草图加载 I/O。
- **估计框架**：提供让用户实现并执行估计器的接口，并以位置感知查询分配与网格化估计重排查询以改善访问局部性。

## 方法与技术要点

- **构图数据流**：按顶点 ID 把图切分为 P 个分区，构建时只把当前活跃顶点的 ADS 留在内存，其余留在存储；分区越少 I/O 越少但内存越高，用户按可用内存取最小可行分区数。
- **无锁边布局**：边数据按分区与顶点 ID 排序存放，多线程遍历时无需加锁即可读取，去掉同步开销。
- **选择性 ADS 访问**：区分活跃与冷数据，只加载本轮计算真正需要的 ADS 项，避免整份草图反复换入换出。
- **查询重调度**：位置感知查询分配把访问同一分区的查询排在一起；网格化估计进一步利用相邻查询网格之间的局部性，把分散访问聚成局部性更好的访问序列。
- **一次构建多次估计**：ADS 对每个图只构建一次，之后用同一份草图反复估计邻域函数、最短路径、接近中心性、接近相似度等性质。

## 评估与主要结果

- **对比内存 ADS 方案**：在 soc-LiveJournal、Pokec、hollywood、Twitter 等图上，Oasis 构图慢约 1.8 倍、估计慢约 1.7 倍，但内存节省 13.8 倍，因而能处理内存放不下的大图。
- **网格化估计**：相对 Basic Oasis，在 soc-LiveJournal、Pokec、hollywood、Twitter 上把执行时间分别再缩短 13.8%、14.2%、16.7%、11.8%。
- **内存可调**：在 soc-LiveJournal、k = 32 下，P = 64 时构图只需 668 MB 但耗时 1236 秒；P = 4 时需 8638 MB、676 秒完成，内存与时间呈反比。
- **对比精确计算系统**：执行时间快数个数量级，仅损失少量精度。

## 代码与研究制品

- [代码仓库](https://github.com/tsunyuyang/Oasis)

[返回 Storage Diversity and Heterogeneity](index.md) · [返回 FAST 2025](../index.md)
