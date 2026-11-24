---
title: "Improving SpGEMM Performance Through Matrix-Reordering and Cluster-Wise Computation"
description: "SC 2025 · Algorithms: Sparse Matrix and Tensor Computation · Abdullah Al Raqibul Islam; Helen Xu; Dong Dai; Aydin Buluç"
tags:
  - "SC2025"
  - "Algorithms: Sparse Matrix and Tensor Computation"
---

# Improving SpGEMM Performance Through Matrix-Reordering and Cluster-Wise Computation

**中文标题：** 通过矩阵重排序和按簇计算提高稀疏矩阵乘法性能

**所属 Session：** [Algorithms: Sparse Matrix and Tensor Computation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Abdullah Al Raqibul Islam; Helen Xu; Dong Dai; Aydin Buluç

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap839&sess=sess170)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Sparse matrix-sparse matrix multiplication (SpGEMM) is a key kernel in many scientific applications and graph workloads. Significant work has been devoted to developing row reordering schemes towards improving locality in sparse operations, but prior studies mostly focus on the case of sparse-matrix vector multiplication (SpMV). In this paper, we address these issues with hierarchical clustering for SpGEMM that leverages both row reordering and cluster-wise computation to improve reuse in the B matrix with a novel row-clustered matrix format and access pattern in the left-hand side matrix. We find that hierarchical clustering can speed up SpGEMM by 1.39× on average with low preprocessing cost. Additionally, this paper sheds light on the role of both row re-ordering and clustering for SpGEMM with a comprehensive empirical study of the effect of 10 different reordering algorithms and three clustering schemes on SpGEMM performance on a suite of 110 matrices.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
