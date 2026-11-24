---
title: "Bridging the Gap Between Unstructured SpMM and Structured Sparse Tensor Cores"
description: "SC 2025 · Performance: Sparse Matrix and Tensor Computation · Yukang Dong; Ziyuan Shen; Wenbin Jiang; Zhenghang Liu; Ye Xu; Bingyi He; Ran Zhe"
tags:
  - "SC2025"
  - "Performance: Sparse Matrix and Tensor Computation"
---

# Bridging the Gap Between Unstructured SpMM and Structured Sparse Tensor Cores

**中文标题：** 弥合非结构化 SpMM 与结构化稀疏张量核心之间的差距

**所属 Session：** [Performance: Sparse Matrix and Tensor Computation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Yukang Dong; Ziyuan Shen; Wenbin Jiang; Zhenghang Liu; Ye Xu; Bingyi He; Ran Zheng; Hai Jin

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap588&sess=sess299)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The acceleration of Sparse-dense Matrix Multiplication (SpMM) using Tensor Cores (TCs) in GPUs has recently garnered significant attention. TCs are designed for block-wise matrix multiplication; however, block partitioning of general unstructured sparse matrices often results in low-level density, causing a substantial waste of computational resources. Sparse Tensor Cores (SpTCs) can mitigate this issue by skipping 50% of zero values; however, SpTCs are limited to strict 2:4 or 1:2 structured sparsity. To bridge this gap, we propose MP-SpMM, a novel matching and padding approach that transforms general sparse matrices into structured sparsity, drawing inspiration from the maximum matching problem in graph theory. Moreover, we introduce a novel storage format and a highly optimized GPU kernel that fully exploits the capabilities of SpTCs. Extensive experiments on modern GPUs demonstrate that MP-SpMM outperforms state-of-the-art SpMM libraries, DTC-SpMM and RoDe, with an average speedup

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
