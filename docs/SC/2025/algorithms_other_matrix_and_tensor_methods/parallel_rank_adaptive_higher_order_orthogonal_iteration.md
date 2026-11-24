---
title: "Parallel Rank-Adaptive Higher-Order Orthogonal Iteration"
description: "SC 2025 · Algorithms: Other Matrix and Tensor Methods · Joao Pinheiro; Aditya Devarakonda; Grey Ballard"
tags:
  - "SC2025"
  - "Algorithms: Other Matrix and Tensor Methods"
---

# Parallel Rank-Adaptive Higher-Order Orthogonal Iteration

**中文标题：** 并行秩自适应高阶正交迭代

**所属 Session：** [Algorithms: Other Matrix and Tensor Methods](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Other Matrix and Tensor Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Other Matrix and Tensor Methods</p>
</div>

**作者**：Joao Pinheiro; Aditya Devarakonda; Grey Ballard

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap675&sess=sess172)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Higher-order orthogonal iteration (HOOI) is an iterative algorithm that computes a Tucker decomposition of fixed ranks of an input tensor. In this work we modify HOOI to determine ranks adaptively subject to a fixed approximation error, apply optimizations to reduce the cost of each HOOI iteration, and parallelize the method in order to scale to large, dense datasets. We show that HOOI is competitive with the sequentially truncated higher-order singular value decomposition (ST-HOSVD) algorithm, particularly in cases of high compression ratios. Our proposed rank-adaptive HOOI can achieve comparable approximation error to ST-HOSVD in less time, sometimes achieving a better compression ratio. We demonstrate that our parallelization scales well over thousands of cores and show, using three scientific simulation datasets, that HOOI outperforms ST-HOSVD in high-compression regimes. For example, for a 3D fluid-flow simulation dataset, HOOI computes a Tucker decomposition 82x faster and achiev

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
