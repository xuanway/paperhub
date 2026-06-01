---
title: "ATLAHS: An Application-centric Network Simulator Toolchain for AI, HPC, and Distributed Storage"
description: "SC 2025 · Performance: Analysis Tools · Siyuan Shen; Tommaso Bonato; Zhiyi Hu; Pasquale Jordan; Tiancheng Chen; Torsten "
tags:
  - "SC2025"
  - "Performance: Analysis Tools"
---

# ATLAHS: An Application-centric Network Simulator Toolchain for AI, HPC, and Distributed Storage

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Analysis Tools。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Analysis Tools</p>
</div>

**作者**：Siyuan Shen; Tommaso Bonato; Zhiyi Hu; Pasquale Jordan; Tiancheng Chen; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

## 摘要

Network simulators play a crucial role in evaluating the performance of large-scale systems. However, most existing simulators rely heavily on synthetic microbenchmarks or narrowly focus on a specific domain. In this paper, we introduce ATLAHS, a flexible, extensible, and open-source toolchain designed to trace real-world applications and accurately simulate their network behavior. ATLAHS leverages the GOAL format to efficiently model communication and computation patterns in AI, HPC, and distributed storage applications. It supports multiple network simulation backends and natively handles multi-job and multi-tenant scenarios. Through extensive validation, we demonstrate that ATLAHS achieves high accuracy in simulating real application workloads (consistently less than 5% error), while significantly outperforming AstraSim, the current state-of-the-art AI systems simulator. We further illustrate ATLAHS's utility via case studies, highlighting the impact of congestion control algorithms

---

## 一句话总结

> 该工作属于 Performance: Analysis Tools 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Performance: Analysis Tools 领域贡献新的设计范式或评估框架。
