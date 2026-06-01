---
title: "Improving SpGEMM Performance Through Matrix-Reordering and Cluster-Wise Computation"
description: "SC 2025 · Algorithms: Sparse Matrix and Tensor Computation · Abdullah Al Raqibul Islam; Helen Xu; Dong Dai; Aydin Buluç"
tags:
  - "SC2025"
  - "Algorithms: Sparse Matrix and Tensor Computation"
---

# Improving SpGEMM Performance Through Matrix-Reordering and Cluster-Wise Computation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Abdullah Al Raqibul Islam; Helen Xu; Dong Dai; Aydin Buluç

**会议**：SC 2025 · St. Louis, MO

## 摘要

Sparse matrix-sparse matrix multiplication (SpGEMM) is a key kernel in many scientific applications and graph workloads. Significant work has been devoted to developing row reordering schemes towards improving locality in sparse operations, but prior studies mostly focus on the case of sparse-matrix vector multiplication (SpMV). In this paper, we address these issues with hierarchical clustering for SpGEMM that leverages both row reordering and cluster-wise computation to improve reuse in the B matrix with a novel row-clustered matrix format and access pattern in the left-hand side matrix. We find that hierarchical clustering can speed up SpGEMM by 1.39× on average with low preprocessing cost. Additionally, this paper sheds light on the role of both row re-ordering and clustering for SpGEMM with a comprehensive empirical study of the effect of 10 different reordering algorithms and three clustering schemes on SpGEMM performance on a suite of 110 matrices.

---

## 一句话总结

> 该工作属于 Algorithms: Sparse Matrix and Tensor Computation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Sparse Matrix and Tensor Computation 领域贡献新的设计范式或评估框架。
