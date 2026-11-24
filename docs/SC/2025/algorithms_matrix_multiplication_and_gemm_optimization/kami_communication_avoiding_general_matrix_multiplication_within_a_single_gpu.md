---
title: "KAMI: Communication-Avoiding General Matrix Multiplication Within a Single GPU"
description: "SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization · Hemeng Wang; Yang Du; Sidu Li; Xiaowen Tian; Qingxiao Sun; Weifeng Liu"
tags:
  - "SC2025"
  - "Algorithms: Matrix Multiplication and GEMM Optimization"
---

# KAMI: Communication-Avoiding General Matrix Multiplication Within a Single GPU

**中文标题：** 单 GPU 内规避通信的通用矩阵乘法

**所属 Session：** [Algorithms: Matrix Multiplication and GEMM Optimization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matrix Multiplication and GEMM Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization</p>
</div>

**作者**：Hemeng Wang; Yang Du; Sidu Li; Xiaowen Tian; Qingxiao Sun; Weifeng Liu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap926&sess=sess285)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Efficient general matrix multiplication (GEMM) has attracted significant research attention in HPC and AI workloads. While large-scale GEMM has nearly achieved the peak floating-point performance of GPUs, substantial opportunities for optimization remain in small and batched GEMM operations. In this paper we propose KAMI, a set of 1D, 2D, and 3D GEMM algorithms that extend the theory of communication-avoiding (CA) techniques within a single GPU. KAMI optimizes thread block-level GEMM by utilizing tensor cores as computational units, low-latency thread registers as local memory, and high-latency on-chip shared memory as a communication medium. We provide a theoretical analysis of CA performance from the perspective of GPU clock cycles, rather than the traditional execution time. Also, we implement SpMM and SpGEMM with this compute-communication pattern. Experimental results for general, low-rank, batched and sparse multiplication operations on the latest NVIDIA, AMD, and Intel GPUs show

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
