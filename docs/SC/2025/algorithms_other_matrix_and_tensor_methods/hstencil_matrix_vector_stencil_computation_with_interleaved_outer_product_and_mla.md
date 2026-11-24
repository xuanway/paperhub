---
title: "HStencil: Matrix-Vector Stencil Computation with Interleaved Outer Product and MLA"
description: "SC 2025 · Algorithms: Other Matrix and Tensor Methods · Han Huang; Jiabin Xie; Guangnan Feng; Xianwei Zhang; Dan Huang; Zhiguang Chen; Y"
tags:
  - "SC2025"
  - "Algorithms: Other Matrix and Tensor Methods"
---

# HStencil: Matrix-Vector Stencil Computation with Interleaved Outer Product and MLA

**中文标题：** 采用交错外积与 MLA 的矩阵向量模板计算

**所属 Session：** [Algorithms: Other Matrix and Tensor Methods](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Other Matrix and Tensor Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Other Matrix and Tensor Methods</p>
</div>

**作者**：Han Huang; Jiabin Xie; Guangnan Feng; Xianwei Zhang; Dan Huang; Zhiguang Chen; Yutong Lu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap115&sess=sess172)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Stencil computations are fundamental to various HPC and intelligent computing applications, often consuming significant execution time. The emergence of specialized matrix units presents new opportunities to accelerate stencil computations. While scalable matrix compute units provide substantial computing horsepower, prior efforts fail to fully utilize the computing capabilities for stencils due to suboptimal matrix-unit utilization, limited instruction-level parallelism, and low cache hit rates. This paper introduces HStencil, a novel stencil computing framework utilizing matrix and vector units. HStencil addresses these challenges through three contributions: 1) microkernels that jointly leverage matrix and vector units to enhance hardware utilization; 2) fine-grained instruction scheduling with interleaved execution to enhance instruction-level parallelism; and 3) spatial prefetch to sustain high performance when working sets exceed cache capacity. Evaluations on representative benc

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
