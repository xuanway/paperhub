---
title: "ORBIT-2: Scaling Exascale Vision Foundation Models for Weather and Climate Downscaling"
description: "SC 2025 · ACM Gordon Bell Finalists Presentations · Xiao Wang; Jong-Youl Choi; Takuya Kurihaya; Isaac Lyngaas; Hong-Jun Yoon; Nasik "
tags:
  - "SC2025"
  - "ACM Gordon Bell Finalists Presentations"
---

# ORBIT-2: Scaling Exascale Vision Foundation Models for Weather and Climate Downscaling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：ACM Gordon Bell Finalists Presentations。</p>
<p class="paper-seo-summary__tags">SC 2025 · ACM Gordon Bell Finalists Presentations</p>
</div>

**作者**：Xiao Wang; Jong-Youl Choi; Takuya Kurihaya; Isaac Lyngaas; Hong-Jun Yoon; Nasik Muhammad Nafi; Aristeidis Tsaris; Fan Ming; Ashwin M Aji; Maliha Hossain; Mohamed Wahib; Dali Wang; Peter Thornton; Moetasim Ashfaq; Prasanna Balaprakash; Dan Lu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Sparse observations and coarse-resolution climate models limit regional decision-making, underscoring the need for robust downscaling. However, existing AI methods struggle with generalization across variables and geographies and are constrained by the quadratic complexity of Vision Transformer (ViT) self-attention. We introduce ORBIT-2, a scalable foundation model for global, high-resolution climate downscaling. ORBIT-2 incorporates two key innovations: (1) Residual Slim ViT (Reslim), a lightweight architecture with residual learning and Bayesian regularization for efficient, robust prediction; and (2) TILES, a tile-wise sequence-scaling algorithm that reduces self-attention complexity from quadratic to linear, enabling long-sequence processing and massive parallelism. ORBIT-2 scales to 10 billion parameters across 32,768 GPUs, achieving up to 1.8 ExaFLOPS sustained throughput and 92%–98% strong scaling efficiency. It supports downscaling to 0.9 km global resolution and processes sequ

---

## 一句话总结

> 该工作属于 ACM Gordon Bell Finalists Presentations 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 ACM Gordon Bell Finalists Presentations 领域贡献新的设计范式或评估框架。
