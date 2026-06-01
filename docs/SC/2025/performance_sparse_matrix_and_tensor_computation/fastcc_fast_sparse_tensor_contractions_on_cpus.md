---
title: "FaSTCC: Fast Sparse Tensor Contractions on CPUs"
description: "SC 2025 · Performance: Sparse Matrix and Tensor Computation · Saurabh Raje; Hunter McCoy; Atanas Rountev; Prashant Pandey; P. Sadayappan"
tags:
  - "SC2025"
  - "Performance: Sparse Matrix and Tensor Computation"
---

# FaSTCC: Fast Sparse Tensor Contractions on CPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Saurabh Raje; Hunter McCoy; Atanas Rountev; Prashant Pandey; P. Sadayappan

**会议**：SC 2025 · St. Louis, MO

## 摘要

Sparse tensor contractions are a core computational primitive in scientific computing and machine learning. Effective optimization of such contractions through loop permutation/tiling remains an open challenge. Our work performs the first comprehensive comparative analysis of data access costs and memory requirements for loop permutations for sparse tensor contractions. Based on these insights, we develop FaSTCC, a novel hashing-based parallel implementation of sparse tensor contractions. FaSTCC introduces a new 2D tiled contraction-index-outer scheme and a corresponding tile-aware design. Using probabilistic modeling, our approach automatically chooses between dense and sparse output tile accumulators and selects suitable tile size. We evaluate FaSTCC across two CPU platforms and a range of real-world workloads, demonstrating significant speedups on benchmarks from FROSTT and from quantum chemistry.

---

## 一句话总结

> 该工作属于 Performance: Sparse Matrix and Tensor Computation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Performance: Sparse Matrix and Tensor Computation 领域贡献新的设计范式或评估框架。
