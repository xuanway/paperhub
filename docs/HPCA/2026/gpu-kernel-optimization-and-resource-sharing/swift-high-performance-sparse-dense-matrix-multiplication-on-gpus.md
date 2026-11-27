---
title: "Swift: High-Performance Sparse-Dense Matrix Multiplication on GPUs"
description: "HPCA 2026 · GPU Kernel Optimization and Resource Sharing"
tags:
  - "HPCA2026"
  - "GPU Kernel Optimization and Resource Sharing"
---

# Swift: High-Performance Sparse-Dense Matrix Multiplication on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: GPU Kernel Optimization and Resource Sharing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · GPU Kernel Optimization and Resource Sharing</p>
</div>

**论文链接**：
**作者**：Jinyu Hu Hunan University , Huizhang Luo Hunan University , Hong Jiang UT Arlington , Marc Casas Barcelona Supercomputing Center , Kenli Li National Supercomputing Center in Changsha, Hunan University , Chubo Liu Hunan University
**会议**：HPCA 2026

---

## 中文标题

Swift：GPU 上的高性能稀疏-稠密矩阵乘法

## 英文摘要

Sparse-Dense Matrix Multiplication (SpMM) on GPUs has gained significant attention because of its importance in modern applications and the increasing computing power of GPUs in the last decade. Previous SpMM studies have focused on the importance of storage format and load balance for the overall performance of SpMM on GPUs. However, very little attention has been paid to the efficacy of coalesced memory access in improving the efficiency of data loading, which incurs a notable overhead that amounts to an average of more than 32% of the overall performance, according to our experimental observation. Existing state-of-the-art (SOTA) solutions fail to adequately support coalesced memory access of both sparse and dense matrices between the global memory and threads on GPUs. In this paper, we propose an efficient algorithm called Swift.1 that speeds up the loading of both sparse and dense matrices of SpMM on modern GPUs. Leveraging coalesced memory access, Swift achieves high loading efficiency by sorting both the columns of the sparse matrix and elements of the dense matrix based on the number of non-zero elements and balancing the load by handling the regular and irregular parts differently and judiciously. Swift takes the Compressed Sparse Column format as an implementation case study to prove the concept and gain insights. We conduct a comprehensive comparison of Swift with four SOTA solutions: ASpT, cuSPARSE, RoDe, and Sputnik, using the full SuiteSparse Matrix Collection as the workload. The experimental results on RTX 4080s, RTX 3090Ti, A100, and V100 demonstrate that our method outperforms the baselines significantly.

## 中文摘要

GPU 上的稀疏-稠密矩阵乘法（SpMM）因在现代应用中十分重要、且近十年 GPU 算力不断提升而受到广泛关注。以往研究关注存储格式与负载均衡对 SpMM 整体性能的重要性，却很少注意合并访存对提升数据加载效率的作用；据我们的实验观察，数据加载开销平均占整体性能的 32% 以上。现有最先进方案无法在 GPU 全局内存与线程之间充分支持稀疏矩阵与稠密矩阵的合并访存。本文提出高效算法 Swift，加速现代 GPU 上 SpMM 对稀疏与稠密矩阵的加载。Swift 借助合并访存，按非零元数量对稀疏矩阵的列和稠密矩阵的元素排序，并对规则与不规则部分区别且审慎地处理以均衡负载，从而获得高加载效率。Swift 以压缩稀疏列（CSC）格式作为实现案例验证该思路并获得洞见。我们以完整的 SuiteSparse 矩阵集合为负载，将 Swift 与 ASpT、cuSPARSE、RoDe 和 Sputnik 四种最先进方案进行全面比较。在 RTX 4080s、RTX 3090Ti、A100 和 V100 上的实验结果表明，我们的方法显著优于基线。
