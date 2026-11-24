---
title: "DAS-ILU: A Distributed Asynchronous Parallel ILU Factorization Based on Domain Decomposition"
description: "SC 2025 · Algorithms: Other Matrix and Tensor Methods · Fan Yuan; Shengguo Li; Xiaojian Yang; Yunqing Huang; Hongxia Wang; Jianchun Wang"
tags:
  - "SC2025"
  - "Algorithms: Other Matrix and Tensor Methods"
---

# DAS-ILU: A Distributed Asynchronous Parallel ILU Factorization Based on Domain Decomposition

**中文标题：** 基于区域分解的分布式异步并行不完全 LU 分解

**所属 Session：** [Algorithms: Other Matrix and Tensor Methods](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Other Matrix and Tensor Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Other Matrix and Tensor Methods</p>
</div>

**作者**：Fan Yuan; Shengguo Li; Xiaojian Yang; Yunqing Huang; Hongxia Wang; Jianchun Wang; Chuanfu Xu; Dezun Dong; Tiejun Li; Jie Liu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap799&sess=sess172)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

This paper presents DAS-ILU, a distributed asynchronous parallel incomplete LU factorization method based on domain decomposition. DAS-ILU partitions the computational domain into independently processed interior nodes and asynchronously updated separator nodes, thereby reducing cross-processor dependencies and halving the separator size compared to conventional methods. To further improve performance, it employs optimized data exchange patterns to minimize communication overhead and extends support to block-structured sparse matrices via exact block inversions. Comprehensive evaluations on a range of problem types—including structural mechanics, computational fluid dynamics, and reservoir simulation—demonstrate the superior performance of DAS-ILU. Compared to state-of-the-art ILU implementations, DAS-ILU achieves solve time speedups of up to $2.07\times$ over Chow-Patel's fine-grained parallel ILU and up to $4.11\times$ over HYPRE's ILU. Moreover, DAS-ILU exhibits strong robustness wh

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
