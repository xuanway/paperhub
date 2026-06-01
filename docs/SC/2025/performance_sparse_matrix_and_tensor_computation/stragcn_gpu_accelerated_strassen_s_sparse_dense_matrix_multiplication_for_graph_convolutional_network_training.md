---
title: "StraGCN: GPU-Accelerated Strassen’s Sparse-Dense Matrix Multiplication for Graph Convolutional Network Training"
description: "SC 2025 · Performance: Sparse Matrix and Tensor Computation · Weidong He; Haikun Liu; Zhuohui Duan; Xiaofei Liao; Shuhao Zhang; Fubing Mao; Ha"
tags:
  - "SC2025"
  - "Performance: Sparse Matrix and Tensor Computation"
---

# StraGCN: GPU-Accelerated Strassen’s Sparse-Dense Matrix Multiplication for Graph Convolutional Network Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Weidong He; Haikun Liu; Zhuohui Duan; Xiaofei Liao; Shuhao Zhang; Fubing Mao; Hai Jin

**会议**：SC 2025 · St. Louis, MO

## 摘要

Graph convolutional networks (GCNs) are a fundamental approach to deep learning on graph-structured data. However, they face a significant challenge in training efficiency due to the high computational cost of Sparse-Dense Matrix Multiplication (SpMM). This paper presents StraGCN, the first GPU-accelerated SpMM implementation based on Strassen’s algorithm specifically designed for GCN training. First, we propose a horizontal fusion model for GPU kernels as an alternative to commonly-used multi-stream CUDA models, significantly improving data locality of on-chip shared memory for Strassen’s SpMM. Second, StraGCN exploits the immutability of the adjacency matrix in GCNs to reuse intermediate results from submatrix operations, substantially reducing redundant computations. Third, we propose two-stage matrix partitioning to mitigate load imbalance caused by the irregular distribution of non-zero elements. We evaluate StraGCN with 15 benchmark datasets. Experimental results show that StraGC

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
