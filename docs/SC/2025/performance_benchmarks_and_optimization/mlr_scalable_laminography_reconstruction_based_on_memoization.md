---
title: "mLR: Scalable Laminography Reconstruction Based on Memoization"
description: "SC 2025 · Performance: Benchmarks and Optimization · Bin Ma; Victor Nikitin; Xi Wang; Tekin Bicer; Dong Li"
tags:
  - "SC2025"
  - "Performance: Benchmarks and Optimization"
---

# mLR: Scalable Laminography Reconstruction Based on Memoization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Benchmarks and Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Benchmarks and Optimization</p>
</div>

**作者**：Bin Ma; Victor Nikitin; Xi Wang; Tekin Bicer; Dong Li

**会议**：SC 2025 · St. Louis, MO

## 摘要

ADMM-FFT is an iterative method with high reconstruction accuracy for laminography but suffers from excessive computation time and large memory consumption. We introduce mLR, which employs memoization to replace the time-consuming Fast Fourier Transform (FFT) operations based on the unique observation that similar FFT operations appear in iterations of ADMM-FFT. We introduce a series of techniques to make the application of memoization to ADMM-FFT performance-beneficial and scalable. We also introduce variable offloading to save CPU memory and scale ADMM-FFT across GPUs within and across nodes. Using mLR, we are able to scale ADMM-FFT on an input problem of $2K \times 2K \times 2K$, which is the largest input problem laminography reconstruction has ever worked on with the ADMM-FFT solution on limited memory; mLR brings 52.8\% performance improvement on average (up to 65.4\%), compared to the original ADMM-FFT.

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
