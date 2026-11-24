---
title: "StraGCN: GPU-Accelerated Strassen’s Sparse-Dense Matrix Multiplication for Graph Convolutional Network Training"
description: "SC 2025 · Performance: Sparse Matrix and Tensor Computation · Weidong He; Haikun Liu; Zhuohui Duan; Xiaofei Liao; Shuhao Zhang; Fubing Mao; Ha"
tags:
  - "SC2025"
  - "Performance: Sparse Matrix and Tensor Computation"
---

# StraGCN: GPU-Accelerated Strassen’s Sparse-Dense Matrix Multiplication for Graph Convolutional Network Training

**中文标题：** 面向图卷积网络训练的 GPU 加速 Strassen 稀疏矩阵乘稠密矩阵

**所属 Session：** [Performance: Sparse Matrix and Tensor Computation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Weidong He; Haikun Liu; Zhuohui Duan; Xiaofei Liao; Shuhao Zhang; Fubing Mao; Hai Jin

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap452&sess=sess299)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Graph convolutional networks (GCNs) are a fundamental approach to deep learning on graph-structured data. However, they face a significant challenge in training efficiency due to the high computational cost of Sparse-Dense Matrix Multiplication (SpMM). This paper presents StraGCN, the first GPU-accelerated SpMM implementation based on Strassen’s algorithm specifically designed for GCN training. First, we propose a horizontal fusion model for GPU kernels as an alternative to commonly-used multi-stream CUDA models, significantly improving data locality of on-chip shared memory for Strassen’s SpMM. Second, StraGCN exploits the immutability of the adjacency matrix in GCNs to reuse intermediate results from submatrix operations, substantially reducing redundant computations. Third, we propose two-stage matrix partitioning to mitigate load imbalance caused by the irregular distribution of non-zero elements. We evaluate StraGCN with 15 benchmark datasets. Experimental results show that StraGC

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
