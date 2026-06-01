---
title: "MXBLAS: Accelerating 8-Bit Deep Learning with a Unified Micro-Scaled GEMM Library"
description: "SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization · Weihu Wang; Yaqi Xia; Donglin Yang; Xiaobo Zhou; Dazhao Cheng"
tags:
  - "SC2025"
  - "Algorithms: Matrix Multiplication and GEMM Optimization"
---

# MXBLAS: Accelerating 8-Bit Deep Learning with a Unified Micro-Scaled GEMM Library

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matrix Multiplication and GEMM Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization</p>
</div>

**作者**：Weihu Wang; Yaqi Xia; Donglin Yang; Xiaobo Zhou; Dazhao Cheng

**会议**：SC 2025 · St. Louis, MO

## 摘要

Micro-scaling general matrix multiplication (MX-GEMM) uses 8-bit MX-format inputs to accelerate deep learning workloads. While the MX-format supports diverse scaling patterns and granularities, current MX-GEMM implementations are often model-specific. This leads to three main issues: tight coupling between models and kernels, inefficient promotion operations, and neglected quantization overhead. This paper introduces MXBLAS, a high-performance MX-GEMM library that supports the full range of MX-format variations. MXBLAS overcomes prior limitations with three key innovations: (1) a template-based design enabling flexible promotion patterns within a unified framework; (2) adaptive runtime kernel generation using template matching, guided search pruning, and auto-tuning to find optimal configurations; and (3) a compute-store co-optimization that fuses quantization into the kernel’s epilogue, reducing overhead. Experiments show MXBLAS outperforms existing MX-GEMM libraries by 33% on average

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
