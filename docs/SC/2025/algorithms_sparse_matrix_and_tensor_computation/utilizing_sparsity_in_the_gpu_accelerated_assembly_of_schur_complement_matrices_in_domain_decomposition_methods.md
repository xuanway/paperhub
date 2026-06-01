---
title: "Utilizing Sparsity in the GPU-Accelerated Assembly of Schur Complement Matrices in Domain Decomposition Methods"
description: "SC 2025 · Algorithms: Sparse Matrix and Tensor Computation · Jakub Homola; Ondřej Meca; Lubomír Říha; Tomáš Brzobohatý"
tags:
  - "SC2025"
  - "Algorithms: Sparse Matrix and Tensor Computation"
---

# Utilizing Sparsity in the GPU-Accelerated Assembly of Schur Complement Matrices in Domain Decomposition Methods

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Jakub Homola; Ondřej Meca; Lubomír Říha; Tomáš Brzobohatý

**会议**：SC 2025 · St. Louis, MO

## 摘要

Schur complement matrices emerge in many domain decomposition methods that can utilize supercomputers to solve complex engineering problems. As most of today's high-performance clusters' performance lies in GPUs, these methods should also be accelerated. Typically, the offloaded components are the explicitly assembled dense Schur complement matrices used later in the iterative solver for multiplication with a vector. As the explicit assembly is expensive, it adds a significant overhead to this approach of acceleration. It has already been shown that the overhead can be minimized by assembling the Schur complements directly on the GPU. This paper shows that the GPU assembly can be further improved by wisely utilizing the matrix sparsity. In the context of FETI, we achieved a speedup of 5.1 in the GPU section of the code and 3.3 for the whole assembly, making the acceleration beneficial from as few as 10 iterations for subdomains with 1,000-70,000 unknowns.

---

## 一句话总结

> 该工作属于 Algorithms: Sparse Matrix and Tensor Computation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Sparse Matrix and Tensor Computation 领域贡献新的设计范式或评估框架。
