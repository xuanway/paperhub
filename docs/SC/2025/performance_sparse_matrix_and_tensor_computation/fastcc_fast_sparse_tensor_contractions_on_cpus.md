---
title: "FaSTCC: Fast Sparse Tensor Contractions on CPUs"
description: "SC 2025 · Performance: Sparse Matrix and Tensor Computation · Saurabh Raje; Hunter McCoy; Atanas Rountev; Prashant Pandey; P. Sadayappan"
tags:
  - "SC2025"
  - "Performance: Sparse Matrix and Tensor Computation"
---

# FaSTCC: Fast Sparse Tensor Contractions on CPUs

**中文标题：** CPU 上的快速稀疏张量收缩

**所属 Session：** [Performance: Sparse Matrix and Tensor Computation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Saurabh Raje; Hunter McCoy; Atanas Rountev; Prashant Pandey; P. Sadayappan

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap542&sess=sess299)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Sparse tensor contractions are a core computational primitive in scientific computing and machine learning. Effective optimization of such contractions through loop permutation/tiling remains an open challenge. Our work performs the first comprehensive comparative analysis of data access costs and memory requirements for loop permutations for sparse tensor contractions. Based on these insights, we develop FaSTCC, a novel hashing-based parallel implementation of sparse tensor contractions. FaSTCC introduces a new 2D tiled contraction-index-outer scheme and a corresponding tile-aware design. Using probabilistic modeling, our approach automatically chooses between dense and sparse output tile accumulators and selects suitable tile size. We evaluate FaSTCC across two CPU platforms and a range of real-world workloads, demonstrating significant speedups on benchmarks from FROSTT and from quantum chemistry.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
