---
title: "MISA-AKMC: Achieve Kinetic Monte Carlo Simulation of 20 Quadrillion Atoms on GPU Clusters"
description: "SC 2025 · Applications: Atomistic Modeling · Shunde Li; Zhijie Pan; Ningming Nie; Jue Wang; He Bai; Genshen Chu; Yan Zeng; Xi"
tags:
  - "SC2025"
  - "Applications: Atomistic Modeling"
---

# MISA-AKMC: Achieve Kinetic Monte Carlo Simulation of 20 Quadrillion Atoms on GPU Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Atomistic Modeling。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Atomistic Modeling</p>
</div>

**作者**：Shunde Li; Zhijie Pan; Ningming Nie; Jue Wang; He Bai; Genshen Chu; Yan Zeng; Xinfu He; Yangang Wang; Changjun Hu; Xuebin Chi

**会议**：SC 2025 · St. Louis, MO

## 摘要

The Atomic Kinetic Monte Carlo (AKMC) method provides insights into the macroscopic behavior of materials through atomistic-level simulations and finds broad applications in materials science innovation. Improving simulation scale and performance remains a consistent focus in the development of parallel AKMC software. We port the AKMC software to GPU clusters. To alleviate the memory pressure in large-scale complex system simulations, we redesign the data layout and propose the lattice data compression and vacancy data decompression algorithms. Additionally, we propose a multi-level pipeline scheme combined with an on-demand communication forwarding and merging strategy to reduce data transfer and communication overhead. Compared to state-of-the-art KMC software, MISA-AKMC\footnotemark achieves a 10.41-fold improvement in computational throughput and a 52.07-fold expansion in simulation scale. We implement the first true micrometer-scale AKMC simulation involving 20 quadrillion atoms o

---

## 一句话总结

> 该工作属于 Applications: Atomistic Modeling 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Applications: Atomistic Modeling 领域贡献新的设计范式或评估框架。
