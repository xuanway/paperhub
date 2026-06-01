---
title: "Insights from Optimizing HPL Performance on Exascale Systems: A Comparative Analysis of Panel Factorization"
description: "SC 2025 · State of the Practice · Hao Lu; Michael Matheson; Noel Chalmers; Aditya Kashi; Nicholas Malaya; Feiyi Wa"
tags:
  - "SC2025"
  - "State of the Practice"
---

# Insights from Optimizing HPL Performance on Exascale Systems: A Comparative Analysis of Panel Factorization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：State of the Practice。</p>
<p class="paper-seo-summary__tags">SC 2025 · State of the Practice</p>
</div>

**作者**：Hao Lu; Michael Matheson; Noel Chalmers; Aditya Kashi; Nicholas Malaya; Feiyi Wang

**会议**：SC 2025 · St. Louis, MO

## 摘要

High Performance LINPACK (HPL) remains the primary benchmark for evaluating supercomputing performance. It includes many parts with substantial internal complexity, and its performance is affected by a large number of parameters that interact in ways that are difficult to predict on large-scale heterogeneous supercomputer systems. We present a comprehensive performance analysis of HPL on Frontier, the world's first exascale supercomputer, which achieved HPL performance of 1.35 exaflops. Through empirical parameter tuning, detailed modeling, and comparative evaluation, we uncover critical performance insights, share lessons learned, and outline best practices for effective parameter tuning on exascale systems. We introduce and evaluate two novel PDFACT strategies: a dedicated-thread (DT) variant and a GPU-based variant (GPUPDFACT) implementation using HIP cooperative groups, demonstrating that GPU-based factorization outperforms conventional CPU-based PDFACT on Frontier's architecture. 

---

## 一句话总结

> 该工作属于 State of the Practice 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 State of the Practice 领域贡献新的设计范式或评估框架。
