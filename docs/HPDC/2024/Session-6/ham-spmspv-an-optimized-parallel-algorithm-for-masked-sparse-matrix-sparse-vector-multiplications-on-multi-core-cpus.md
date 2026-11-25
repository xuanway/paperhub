---
title: "HAM-SpMSpV: an Optimized Parallel Algorithm for Masked Sparse Matrix-Sparse Vector Multiplications on multi-core CPUs"
description: "HPDC 2024 · Session 6 — Accelerators & Scientific applications"
tags:
  - "HPDC2024"
  - "Session 6"
  - "Accelerators & Scientific applications"
---

# HAM-SpMSpV: an Optimized Parallel Algorithm for Masked Sparse Matrix-Sparse Vector Multiplications on multi-core CPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 6 — Accelerators & Scientific applications（2024年6月7日 10:00–11:15 · Session Chair：Raffaele Montella）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 6</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658680)

**作者**：Lei Xu, Haipeng Jia, Yunquan Zhang, Luhan Wang, Xianmeng Jiang

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 6 — Accelerators & Scientific applications（2024年6月7日 10:00–11:15 · Session Chair：Raffaele Montella）

---

## 英文摘要

The efficiency of Sparse Matrix-Sparse Vector Multiplication (SpMSpV) is critically important in fields such as machine learning and graph analytics. In certain algorithms, masked SpMSpV computes only a subset of the result entries. Despite its significance, this selective computation poses unique challenges, and existing algorithms often struggle to exploit the sparsity of the input and the mask vectors concurrently. To boost the efficiency of masked SpMSpV on shared memory architectures, we introduce a hybrid adaptive masked SpMSpV algorithm (HAM-SpMSpV) designed to select the efficient kernel automatically based on input features. This approach builds upon the foundation of a conventional algorithm, incorporating two novel masked SpMSpVs: the pre-bucketing masked SPA-based algorithm and the pre-masking bucketed hash-based algorithm. The newly proposed algorithms significantly expedite computation, especially in scenarios with high sparsity in input vectors and masks. Our evaluation involved extensive testing across a diverse range of real-world graphs, utilizing various sparsity of input vectors and masks. This rigorous testing confirmed that our approach notably outperforms existing solutions. Specifically, it achieves a speedup of up to 1.96 times compared to SuiteSparse:GraphBLAS and a remarkable 6.28 times relative to MKL Graph, demonstrating significant advancements in SpMSpV efficiency.

## 中文摘要

稀疏矩阵-稀疏向量乘法（SpMSpV）的效率在机器学习与图分析等领域至关重要。在某些算法中，带掩码的 SpMSpV 只计算结果条目的一个子集。尽管意义重大，这种选择性计算带来了独特挑战，现有算法往往难以同时利用输入向量与掩码向量的稀疏性。为提升共享内存架构上带掩码 SpMSpV 的效率，我们提出一种混合自适应带掩码 SpMSpV 算法（HAM-SpMSpV），旨在根据输入特征自动选择高效核。该方法建立在传统算法基础之上，纳入两种新颖的带掩码 SpMSpV：预分桶的基于掩码 SPA 的算法，以及预掩码的基于分桶哈希的算法。新提出的算法显著加速计算，尤其在输入向量与掩码高度稀疏的场景中。我们的评估在多种真实图上进行了广泛测试，使用不同稀疏度的输入向量与掩码。这一严格测试证实，我们的方法明显优于现有方案：相比 SuiteSparse:GraphBLAS 最高加速 1.96 倍，相比 MKL Graph 高达 6.28 倍，展现了 SpMSpV 效率的显著进步。

## 英文关键词

Sparse Matrix-Sparse Vector Multiplication (SpMSpV), Mask, Shared Memory, Adaptive Method

## 中文关键词

稀疏矩阵-稀疏向量乘法（SpMSpV），掩码，共享内存，自适应方法

---

[← 返回 Session 6 — Accelerators & Scientific applications](index.md)
