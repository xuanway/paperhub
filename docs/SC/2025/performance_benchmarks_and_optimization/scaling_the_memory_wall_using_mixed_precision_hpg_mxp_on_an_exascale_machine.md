---
title: "Scaling the Memory Wall Using Mixed-Precision — HPG-MxP on an Exascale Machine"
description: "SC 2025 · Performance: Benchmarks and Optimization · Aditya Kashi; Nicholson Koukpaizan; Hao Lu; Michael Matheson; Sarp Oral; Feiyi W"
tags:
  - "SC2025"
  - "Performance: Benchmarks and Optimization"
---

# Scaling the Memory Wall Using Mixed-Precision — HPG-MxP on an Exascale Machine

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Benchmarks and Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Benchmarks and Optimization</p>
</div>

**作者**：Aditya Kashi; Nicholson Koukpaizan; Hao Lu; Michael Matheson; Sarp Oral; Feiyi Wang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Mixed-precision algorithms have been proposed as a way for scientific computing to benefit from some of the gains seen for AI on recent high performance computing (HPC) platforms. A few applications dominated by dense matrix operations have seen substantial speedups by utilizing low-precision formats such as FP16. However, a majority of scientific simulation applications are memory bandwidth limited. Beyond preliminary studies, the practical gain from using mixed-precision algorithms on a given HPC system is largely unclear. The High Performance GMRES Mixed Precision (HPG-MxP) benchmark has been proposed to measure the useful performance of an HPC system on sparse matrix-based mixed-precision applications. In this work, we present a highly optimized implementation of the HPG-MxP benchmark for an exascale system and describe our algorithm enhancements. We show for the first time a speedup of 1.6x using a combination of double and single precision on modern GPU-based supercomputers.

---

## 一句话总结

> 该工作属于 Performance: Benchmarks and Optimization 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Performance: Benchmarks and Optimization 领域贡献新的设计范式或评估框架。
