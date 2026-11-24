---
title: "Rethinking Back Transformation in Two-Stage Eigenvalue Decomposition on Heterogeneous Architectures"
description: "SC 2025 · Algorithms: Other Matrix and Tensor Methods · Hansheng Wang; Dajun Huang; Gaoyuan Zou; Lu Shi; Xu Jiang; Xi Wu; Hancong Duan; "
tags:
  - "SC2025"
  - "Algorithms: Other Matrix and Tensor Methods"
---

# Rethinking Back Transformation in Two-Stage Eigenvalue Decomposition on Heterogeneous Architectures

**中文标题：** 重新思考异构架构上两阶段特征值分解中的反变换

**所属 Session：** [Algorithms: Other Matrix and Tensor Methods](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Other Matrix and Tensor Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Other Matrix and Tensor Methods</p>
</div>

**作者**：Hansheng Wang; Dajun Huang; Gaoyuan Zou; Lu Shi; Xu Jiang; Xi Wu; Hancong Duan; Shaoshuai Zhang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap123&sess=sess172)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The two-stage eigenvalue decomposition (EVD) method outperforms conventional one-stage methods on GPUs and heterogeneous architectures, especially when eigenvectors are not required. However, its performance advantage diminishes when performing back transformation to obtain eigenvectors. To address this, we propose two key solutions: 1) replacing BLAS3 operations with BLAS2 operations during the bulge-chasing back transformation for better performance, and 2) reordering the back transformation workflow from a backward pattern to a new parallelism-driven pattern to hide divide-and-conquer latency, at the cost of one additional GEMM computation. Experimentally, the proposed back transformation algorithm demonstrates significant performance improvements, outperforming the SOTA implementation in MAGMA by an average factor of 3.58x. For complete FP64 precision symmetric EVD with eigenvectors, the proposed algorithm, incorporating both solutions, surpasses the SOTA implementations in MAGMA a

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
