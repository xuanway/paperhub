---
title: "BINGO: Radix-based Bias Factorization for Random Walk on Dynamic Graphs"
description: "EuroSys 2025 · Graph and Stream processing · Pinhuan Wang (Rutgers, The State University of New Jersey), Chengying Huan (Nanj"
tags:
  - "EuroSys2025"
  - "Graph and Stream processing"
---

# BINGO: Radix-based Bias Factorization for Random Walk on Dynamic Graphs

**中文标题：** 基于基数的偏置分解，支持动态图上的随机游走

**所属 Session：** [Session 5.1: Graph and Stream processing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Graph and Stream processing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Graph and Stream processing</p>
</div>

**作者**：Pinhuan Wang (Rutgers, The State University of New Jersey), Chengying Huan (Nanjing University), Zhibin Wang (Nanjing University), Chen Tian (Nanjing University), Yuede Ji (The University of Texas at Arlington), Hang Liu (Rutgers, The State University of New Jersey)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717456)

## 英文摘要

Random walks are a primary means for extracting information from large-scale graphs. While most real-world graphs are inherently dynamic, state-of-the-art random walk engines failed to efficiently support such a critical use case. This paper takes the initiative to build a general random walk engine for dynamically changing graphs with two key principles: (i) This system should support both low-latency streaming updates and high-throughput batched updates. (ii) This system should achieve fast sampling speed while maintaining acceptable space consumption to support dynamic graph updates. Upholding both standards, we introduce Bingo, a GPU-based random walk engine for dynamically changing graphs. First, we propose a novel radix-based bias factorization algorithm to support constant time sampling complexity while supporting fast streaming updates. Second, we present a group-adaption design to reduce space consumption dramatically. Third, we incorporate GPU-aware designs to support high-throughput batched graph updates on massively parallel platforms. Together, Bingo outperforms existing efforts across various applications, settings, and datasets, achieving up to a 271.11x speedup compared to the state-of-the-art efforts.

## 中文摘要

随机游走是从大规模图中提取信息的主要手段。尽管大多数真实图本质上是动态的，最先进的随机游走引擎却未能高效支持这一关键用例。本文率先构建一个面向动态变化图的通用随机游走引擎，遵循两条关键原则：（i）系统应同时支持低延迟的流式更新和高吞吐的批量更新；（ii）系统应在保持可接受的空间消耗以支持动态图更新的同时实现快速采样。秉持这两项标准，我们提出 Bingo，一个基于 GPU 的面向动态变化图的随机游走引擎。首先，我们提出一种新颖的基于基数的偏置分解算法，在支持快速流式更新的同时实现常数时间的采样复杂度。其次，我们提出一种分组自适应设计，大幅降低空间消耗。第三，我们融入 GPU 感知的设计，以在海量并行平台上支持高吞吐的批量图更新。综合而言，Bingo 在多种应用、场景和数据集上均优于现有工作，相比最先进的工作最高实现 271.11 倍加速。

**英文关键词：** Random Walk, Monte Carlo Sampling, GPUs

**中文关键词：** 随机游走、蒙特卡洛采样、GPU

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
