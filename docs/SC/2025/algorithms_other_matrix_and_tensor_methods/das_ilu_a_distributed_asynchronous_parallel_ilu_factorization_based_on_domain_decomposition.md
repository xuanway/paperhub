---
title: "DAS-ILU: A Distributed Asynchronous Parallel ILU Factorization Based on Domain Decomposition"
description: "SC 2025 · Algorithms: Other Matrix and Tensor Methods · Fan Yuan; Shengguo Li; Xiaojian Yang; Yunqing Huang; Hongxia Wang; Jianchun Wang"
tags:
  - "SC2025"
  - "Algorithms: Other Matrix and Tensor Methods"
---

# DAS-ILU: A Distributed Asynchronous Parallel ILU Factorization Based on Domain Decomposition

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Other Matrix and Tensor Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Other Matrix and Tensor Methods</p>
</div>

**作者**：Fan Yuan; Shengguo Li; Xiaojian Yang; Yunqing Huang; Hongxia Wang; Jianchun Wang; Chuanfu Xu; Dezun Dong; Tiejun Li; Jie Liu

**会议**：SC 2025 · St. Louis, MO

## 摘要

This paper presents DAS-ILU, a distributed asynchronous parallel incomplete LU factorization method based on domain decomposition. DAS-ILU partitions the computational domain into independently processed interior nodes and asynchronously updated separator nodes, thereby reducing cross-processor dependencies and halving the separator size compared to conventional methods. To further improve performance, it employs optimized data exchange patterns to minimize communication overhead and extends support to block-structured sparse matrices via exact block inversions. Comprehensive evaluations on a range of problem types—including structural mechanics, computational fluid dynamics, and reservoir simulation—demonstrate the superior performance of DAS-ILU. Compared to state-of-the-art ILU implementations, DAS-ILU achieves solve time speedups of up to $2.07\times$ over Chow-Patel's fine-grained parallel ILU and up to $4.11\times$ over HYPRE's ILU. Moreover, DAS-ILU exhibits strong robustness wh

---

## 一句话总结

> 该工作属于 Algorithms: Other Matrix and Tensor Methods 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Other Matrix and Tensor Methods 领域贡献新的设计范式或评估框架。
