---
title: "Utilizing Sparsity in the GPU-Accelerated Assembly of Schur Complement Matrices in Domain Decomposition Methods"
description: "SC 2025 · Algorithms: Sparse Matrix and Tensor Computation · Jakub Homola; Ondřej Meca; Lubomír Říha; Tomáš Brzobohatý"
tags:
  - "SC2025"
  - "Algorithms: Sparse Matrix and Tensor Computation"
---

# Utilizing Sparsity in the GPU-Accelerated Assembly of Schur Complement Matrices in Domain Decomposition Methods

**中文标题：** 在区域分解方法的 GPU 加速 Schur 补矩阵组装中利用稀疏性

**所属 Session：** [Algorithms: Sparse Matrix and Tensor Computation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Jakub Homola; Ondřej Meca; Lubomír Říha; Tomáš Brzobohatý

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap998&sess=sess170)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Schur complement matrices emerge in many domain decomposition methods that can utilize supercomputers to solve complex engineering problems. As most of today's high-performance clusters' performance lies in GPUs, these methods should also be accelerated. Typically, the offloaded components are the explicitly assembled dense Schur complement matrices used later in the iterative solver for multiplication with a vector. As the explicit assembly is expensive, it adds a significant overhead to this approach of acceleration. It has already been shown that the overhead can be minimized by assembling the Schur complements directly on the GPU. This paper shows that the GPU assembly can be further improved by wisely utilizing the matrix sparsity. In the context of FETI, we achieved a speedup of 5.1 in the GPU section of the code and 3.3 for the whole assembly, making the acceleration beneficial from as few as 10 iterations for subdomains with 1,000-70,000 unknowns.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
