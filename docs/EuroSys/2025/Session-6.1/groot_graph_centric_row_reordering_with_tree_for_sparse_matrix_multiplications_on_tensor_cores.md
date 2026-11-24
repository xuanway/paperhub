---
title: "Groot: Graph-Centric Row Reordering with Tree for Sparse Matrix Multiplications on Tensor Cores"
description: "EuroSys 2025 · ML systems · YuAng Chen (The Chinese University of Hong Kong), Jiadong Xie (The Chinese Unive"
tags:
  - "EuroSys2025"
  - "ML systems"
---

# Groot: Graph-Centric Row Reordering with Tree for Sparse Matrix Multiplications on Tensor Cores

**中文标题：** 通过以图为中心的树结构行重排加速张量核心上的稀疏矩阵乘法

**所属 Session：** [Session 6.1: ML systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：ML systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · ML systems</p>
</div>

**作者**：YuAng Chen (The Chinese University of Hong Kong), Jiadong Xie (The Chinese University of Hong Kong), Siyi Teng (The Chinese University of Hong Kong), Wenqi Zeng (Hong Kong University of Science and Technology), Jeffrey Xu Yu (The Chinese University of Hong Kong)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717460)

## 英文摘要

Sparse matrix multiplications are essential in scientific computing and machine learning applications. Recent researches offload sparse operations, such as sparse matrix-matrix multiplication (SpMM) and sampled dense-dense matrix multiplication (SDDMM), on Tensor Cores (TCs) for improved performance. However, their performance is often limited by the matrix’s inherent sparsity and irregularity. In this paper, we find row reordering can potentially improve sparse operations on TCs, but existing reordering techniques exhibit limitations that hinder their effectiveness. To address the issues, we propose Groot, a graph-centric row reordering algorithm with tree. Groot aims to minimize row differences across the matrix, which is proved to be a NP-hard problem. To approximate the optimal solution, Groot firstly captures the local structure of the sparse matrix by constructing a k-nearest neighbor graph, where rows are represented as nodes. Then, it extracts a minimum spanning tree from the constructed graph for global structure optimization. Lastly, Groot traverses the extracted tree to obtain the final ordering. We evaluate Groot using real-world datasets in comparison with state-of-the-art reordering algorithms. Our results show that Groot significantly enhances the computational intensity of SpMM and SDDMM on TCs, delivering the average speedups of 1.8× and 2.0×, respectively. Furthermore, the performance gains extend broadly to sparse computations on CUDA cores and GNN systems.

## 中文摘要

稀疏矩阵乘法在科学计算与机器学习应用中至关重要。近期研究将稀疏矩阵乘稀疏矩阵（SpMM）和采样稠密矩阵乘稠密矩阵（SDDMM）等稀疏运算卸载到张量核（TC）上以提升性能。然而，其性能常常受矩阵固有稀疏性和不规则性的限制。本文发现行重排序有望改善 TC 上的稀疏运算，但现有重排序技术存在局限，影响了其效果。为解决这些问题，我们提出 Groot，一种以图为中心的树形行重排序算法。Groot 旨在最小化矩阵各行之间的差异，该问题已被证明是 NP 难的。为近似最优解，Groot 首先通过构建 k 近邻图来捕获稀疏矩阵的局部结构，其中行被表示为节点。然后，它从构建的图中提取最小生成树以进行全局结构优化。最后，Groot 遍历提取出的树以获得最终排序。我们使用真实数据集将 Groot 与最先进的重排序算法进行比较评估。结果表明，Groot 显著提升了 TC 上 SpMM 和 SDDMM 的计算强度，平均加速分别为 1.8 倍和 2.0 倍。此外，性能收益还广泛延伸至 CUDA 核上的稀疏计算和 GNN 系统。

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
