---
title: "HyTiS: Hybrid Tile Scheduling for GPU GEMM with Enhanced Wave Utilization and Cache Locality"
description: "SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization · Zheng Zhang; Hulin Wang; Hongming Xu; Donglin Yang; Xiaobo Zhou; Dazhao Cheng"
tags:
  - "SC2025"
  - "Algorithms: Matrix Multiplication and GEMM Optimization"
---

# HyTiS: Hybrid Tile Scheduling for GPU GEMM with Enhanced Wave Utilization and Cache Locality

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matrix Multiplication and GEMM Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization</p>
</div>

**作者**：Zheng Zhang; Hulin Wang; Hongming Xu; Donglin Yang; Xiaobo Zhou; Dazhao Cheng

**会议**：SC 2025 · St. Louis, MO

## 摘要

General matrix-matrix multiplication (GEMM) is a core operation in both deep learning and scientific applications. However, as modern GPUs continue to scale in compute capability and adopt larger tile sizes, the wave quantization problem becomes increasingly unavoidable. Existing solutions either exhibit low execution efficiency or introduce additional synchronization overhead. To address these challenges, we propose HyTiS, a hybrid tile scheduling framework that integrates two-level tile scheduling with adaptive tile layout selection. To enable this with minimal tuning overhead, throughput- and latency-oriented micro-kernels are identified during an offline profiling phase, forming an efficient runtime search space. Additionally, we investigate the impact of tile layouts on L2 cache and introduce an analytical model to select optimal layouts that minimize traffic from DRAM to the L2 cache at the wave granularity. Extensive evaluations on NVIDIA H100 and A100 demonstrate that HyTiS sig

---

## 一句话总结

> 该工作属于 Algorithms: Matrix Multiplication and GEMM Optimization 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Matrix Multiplication and GEMM Optimization 领域贡献新的设计范式或评估框架。
