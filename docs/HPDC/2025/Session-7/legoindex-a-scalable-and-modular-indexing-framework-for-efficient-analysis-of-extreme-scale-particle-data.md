---
title: "LegoIndex: A Scalable and Modular Indexing Framework for Efficient Analysis of Extreme-Scale Particle Data"
description: "HPDC 2025 · Session 7 — Best Paper and Best Student Paper Finalists"
tags:
  - "HPDC2025"
  - "Session 7"
  - "Best Paper and Best Student Paper Finalists"
---

# LegoIndex: A Scalable and Modular Indexing Framework for Efficient Analysis of Extreme-Scale Particle Data

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 7 — Best Paper and Best Student Paper Finalists（2025年7月23日 13:00–14:30 · Session Chair：Robert Wisniewski）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 7</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731591) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/guo.pdf)

**作者**：Chang Guo, Ning Yan, Lipeng Wan, Zhichao Cao

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 7 — Best Paper and Best Student Paper Finalists（2025年7月23日 13:00–14:30 · Session Chair：Robert Wisniewski）

**荣誉**：HPDC 2025 最佳学生论文（Best Student Paper）

---

## 英文摘要

Particle-in-Cell (PIC) simulations play a critical role in various scientific domains, including plasma physics, astrophysics, and fusion energy research, by enabling the modeling of complex interactions between charged particles and electromagnetic fields. As PIC simulations scale up in size and complexity, they generate massive volumes of particle data at enormous speeds (TBs/hour). This enormous amount of data presents significant challenges for post-simulation analysis, as existing analysis tools (typically designed for smaller datasets) struggle with low query performance and high resource utilization. While incorporating indexes for PIC data can alleviate some of these inefficiencies, current indexing solutions often fall short of addressing the diverse analysis needs of scientists, substantial index construction overhead during simulation runs, and inefficient small I/O operations. To address these challenges, we present LegoIndex, a scalable, modular, and elastic post-simulation indexing framework designed to improve data access efficiency while minimizing unnecessary data I/Os and memory usage. LegoIndex offers users the flexibility to customize indexing components, structures, and statistic metrics based on the data scale and specific analysis needs. LegoIndex parallelizes the index construction process, enabling efficient processing of datasets of varying sizes. To further enhance query performance, LegoIndex intelligently clusters scattered index results that are spatially or temporally related and optimizes computation logic to effectively reduce data I/Os and memory usage. We conducted comprehensive evaluations of LegoIndex based on large-scale real-world PIC datasets. Integrating LegoIndex with the existing analysis tool can achieve up to a 2276× improvement in overall performance, a 3068× reduction in memory usage, and a 3001× decrease in I/O numbers for large datasets.

## 中文摘要

粒子网格（PIC）模拟在等离子体物理、天体物理和聚变能源研究等多个科学领域中发挥着关键作用，能够对带电粒子与电磁场之间的复杂相互作用建模。随着 PIC 模拟在规模与复杂度上不断扩大，它们以极高速率（TB/小时）产生海量粒子数据。如此庞大的数据给仿真后分析带来重大挑战，因为现有分析工具（通常为较小数据集设计）面临查询性能低、资源占用高的问题。为 PIC 数据引入索引可缓解部分低效，但当前索引方案往往难以满足科学家多样的分析需求、在仿真运行期间产生大量索引构建开销，并且小 I/O 操作效率低下。为应对这些挑战，我们提出 LegoIndex，一个可扩展、模块化且弹性的仿真后索引框架，旨在提升数据访问效率，同时尽量减少不必要的数据 I/O 与内存占用。LegoIndex 让用户能够根据数据规模与具体分析需求灵活定制索引组件、结构与统计指标。LegoIndex 并行化索引构建过程，可高效处理不同规模的数据集。为进一步提升查询性能，LegoIndex 智能地对空间或时间相关的分散索引结果进行聚类，并优化计算逻辑以有效减少数据 I/O 与内存占用。我们基于大规模真实 PIC 数据集对 LegoIndex 进行了全面评估。将 LegoIndex 与现有分析工具集成，在大数据集上可实现整体性能最高 2276 倍提升、内存占用最高 3068 倍降低、I/O 次数最高 3001 倍减少。

## 英文关键词

Scientific Data, Indexing, High-Performance Computing, Particle Data

## 中文关键词

科学数据，索引，高性能计算，粒子数据

---

[← 返回 Session 7 — Best Paper and Best Student Paper Finalists](index.md)
