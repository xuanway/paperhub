---
title: "Wasp: Efficient Asynchronous Single-Source Shortest Path on Multicore Systems via Work Stealing"
description: "SC 2025 · Algorithms: Matching System Capabilities · Marco D'Antonio; Thai Son Mai; Philippas Tsigas; Hans Vandierendonck"
tags:
  - "SC2025"
  - "Algorithms: Matching System Capabilities"
---

# Wasp: Efficient Asynchronous Single-Source Shortest Path on Multicore Systems via Work Stealing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matching System Capabilities。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matching System Capabilities</p>
</div>

**作者**：Marco D'Antonio; Thai Son Mai; Philippas Tsigas; Hans Vandierendonck

**会议**：SC 2025 · St. Louis, MO

## 摘要

The Single-Source Shortest Path (SSSP) problem is a fundamental graph problem with an extensive set of real-world applications. State-of-the-art parallel algorithms for SSSP, such as the ∆-stepping algorithm, create parallelism through priority coarsening. Priority coarsening results in redundant computations that diminish the benefits of parallelization and limit parallel scalability. This paper introduces Wasp, a novel SSSP algorithm that reduces parallelism-induced redundant work by utilizing asynchrony and an efficient priority-aware work stealing scheme. Contrary to previous work, Wasp introduces redundant computations only when threads have no high-priority work locally available to execute. This is achieved by a novel priority-aware work stealing mechanism that controls the inefficiencies of indiscriminate priority coarsening. Experimental evaluation shows competitive or better performance compared to GAP, GBBS, MultiQueues, Galois, ∆*-stepping, and ρ-stepping on 13 diverse grap

---

## 一句话总结

> 该工作属于 Algorithms: Matching System Capabilities 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Matching System Capabilities 领域贡献新的设计范式或评估框架。
