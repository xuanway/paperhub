---
title: "MXBLAS: Accelerating 8-Bit Deep Learning with a Unified Micro-Scaled GEMM Library"
description: "SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization · Weihu Wang; Yaqi Xia; Donglin Yang; Xiaobo Zhou; Dazhao Cheng"
tags:
  - "SC2025"
  - "Algorithms: Matrix Multiplication and GEMM Optimization"
---

# MXBLAS: Accelerating 8-Bit Deep Learning with a Unified Micro-Scaled GEMM Library

**中文标题：** 利用统一微缩放 GEMM 库加速 8 位深度学习

**所属 Session：** [Algorithms: Matrix Multiplication and GEMM Optimization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matrix Multiplication and GEMM Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization</p>
</div>

**作者**：Weihu Wang; Yaqi Xia; Donglin Yang; Xiaobo Zhou; Dazhao Cheng

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap327&sess=sess285)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Micro-scaling general matrix multiplication (MX-GEMM) uses 8-bit MX-format inputs to accelerate deep learning workloads. While the MX-format supports diverse scaling patterns and granularities, current MX-GEMM implementations are often model-specific. This leads to three main issues: tight coupling between models and kernels, inefficient promotion operations, and neglected quantization overhead. This paper introduces MXBLAS, a high-performance MX-GEMM library that supports the full range of MX-format variations. MXBLAS overcomes prior limitations with three key innovations: (1) a template-based design enabling flexible promotion patterns within a unified framework; (2) adaptive runtime kernel generation using template matching, guided search pruning, and auto-tuning to find optimal configurations; and (3) a compute-store co-optimization that fuses quantization into the kernel’s epilogue, reducing overhead. Experiments show MXBLAS outperforms existing MX-GEMM libraries by 33% on average

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
