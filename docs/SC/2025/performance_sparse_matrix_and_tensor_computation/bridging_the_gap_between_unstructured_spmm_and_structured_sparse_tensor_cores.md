---
title: "Bridging the Gap Between Unstructured SpMM and Structured Sparse Tensor Cores"
description: "SC 2025 · Performance: Sparse Matrix and Tensor Computation · Yukang Dong; Ziyuan Shen; Wenbin Jiang; Zhenghang Liu; Ye Xu; Bingyi He; Ran Zhe"
tags:
  - "SC2025"
  - "Performance: Sparse Matrix and Tensor Computation"
---

# Bridging the Gap Between Unstructured SpMM and Structured Sparse Tensor Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Yukang Dong; Ziyuan Shen; Wenbin Jiang; Zhenghang Liu; Ye Xu; Bingyi He; Ran Zheng; Hai Jin

**会议**：SC 2025 · St. Louis, MO

## 摘要

The acceleration of Sparse-dense Matrix Multiplication (SpMM) using Tensor Cores (TCs) in GPUs has recently garnered significant attention. TCs are designed for block-wise matrix multiplication; however, block partitioning of general unstructured sparse matrices often results in low-level density, causing a substantial waste of computational resources. Sparse Tensor Cores (SpTCs) can mitigate this issue by skipping 50% of zero values; however, SpTCs are limited to strict 2:4 or 1:2 structured sparsity. To bridge this gap, we propose MP-SpMM, a novel matching and padding approach that transforms general sparse matrices into structured sparsity, drawing inspiration from the maximum matching problem in graph theory. Moreover, we introduce a novel storage format and a highly optimized GPU kernel that fully exploits the capabilities of SpTCs. Extensive experiments on modern GPUs demonstrate that MP-SpMM outperforms state-of-the-art SpMM libraries, DTC-SpMM and RoDe, with an average speedup 

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
