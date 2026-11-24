---
title: "mLR: Scalable Laminography Reconstruction Based on Memoization"
description: "SC 2025 · Performance: Benchmarks and Optimization · Bin Ma; Victor Nikitin; Xi Wang; Tekin Bicer; Dong Li"
tags:
  - "SC2025"
  - "Performance: Benchmarks and Optimization"
---

# mLR: Scalable Laminography Reconstruction Based on Memoization

**中文标题：** 基于记忆化的可扩展层析成像重建

**所属 Session：** [Performance: Benchmarks and Optimization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Benchmarks and Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Benchmarks and Optimization</p>
</div>

**作者**：Bin Ma; Victor Nikitin; Xi Wang; Tekin Bicer; Dong Li

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap304&sess=sess184)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

ADMM-FFT is an iterative method with high reconstruction accuracy for laminography but suffers from excessive computation time and large memory consumption. We introduce mLR, which employs memoization to replace the time-consuming Fast Fourier Transform (FFT) operations based on the unique observation that similar FFT operations appear in iterations of ADMM-FFT. We introduce a series of techniques to make the application of memoization to ADMM-FFT performance-beneficial and scalable. We also introduce variable offloading to save CPU memory and scale ADMM-FFT across GPUs within and across nodes. Using mLR, we are able to scale ADMM-FFT on an input problem of $2K \times 2K \times 2K$, which is the largest input problem laminography reconstruction has ever worked on with the ADMM-FFT solution on limited memory; mLR brings 52.8\% performance improvement on average (up to 65.4\%), compared to the original ADMM-FFT.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
