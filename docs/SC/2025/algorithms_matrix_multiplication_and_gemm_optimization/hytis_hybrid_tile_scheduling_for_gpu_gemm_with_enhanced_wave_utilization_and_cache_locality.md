---
title: "HyTiS: Hybrid Tile Scheduling for GPU GEMM with Enhanced Wave Utilization and Cache Locality"
description: "SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization · Zheng Zhang; Hulin Wang; Hongming Xu; Donglin Yang; Xiaobo Zhou; Dazhao Cheng"
tags:
  - "SC2025"
  - "Algorithms: Matrix Multiplication and GEMM Optimization"
---

# HyTiS: Hybrid Tile Scheduling for GPU GEMM with Enhanced Wave Utilization and Cache Locality

**中文标题：** 提高 GPU GEMM 波次利用率和缓存局部性的混合分块调度

**所属 Session：** [Algorithms: Matrix Multiplication and GEMM Optimization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matrix Multiplication and GEMM Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization</p>
</div>

**作者**：Zheng Zhang; Hulin Wang; Hongming Xu; Donglin Yang; Xiaobo Zhou; Dazhao Cheng

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap132&sess=sess285)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

General matrix-matrix multiplication (GEMM) is a core operation in both deep learning and scientific applications. However, as modern GPUs continue to scale in compute capability and adopt larger tile sizes, the wave quantization problem becomes increasingly unavoidable. Existing solutions either exhibit low execution efficiency or introduce additional synchronization overhead. To address these challenges, we propose HyTiS, a hybrid tile scheduling framework that integrates two-level tile scheduling with adaptive tile layout selection. To enable this with minimal tuning overhead, throughput- and latency-oriented micro-kernels are identified during an offline profiling phase, forming an efficient runtime search space. Additionally, we investigate the impact of tile layouts on L2 cache and introduce an analytical model to select optimal layouts that minimize traffic from DRAM to the L2 cache at the wave granularity. Extensive evaluations on NVIDIA H100 and A100 demonstrate that HyTiS sig

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
