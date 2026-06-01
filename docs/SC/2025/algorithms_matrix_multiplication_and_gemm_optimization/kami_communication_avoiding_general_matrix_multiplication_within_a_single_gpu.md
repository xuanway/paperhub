---
title: "KAMI: Communication-Avoiding General Matrix Multiplication Within a Single GPU"
description: "SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization · Hemeng Wang; Yang Du; Sidu Li; Xiaowen Tian; Qingxiao Sun; Weifeng Liu"
tags:
  - "SC2025"
  - "Algorithms: Matrix Multiplication and GEMM Optimization"
---

# KAMI: Communication-Avoiding General Matrix Multiplication Within a Single GPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matrix Multiplication and GEMM Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization</p>
</div>

**作者**：Hemeng Wang; Yang Du; Sidu Li; Xiaowen Tian; Qingxiao Sun; Weifeng Liu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Efficient general matrix multiplication (GEMM) has attracted significant research attention in HPC and AI workloads. While large-scale GEMM has nearly achieved the peak floating-point performance of GPUs, substantial opportunities for optimization remain in small and batched GEMM operations. In this paper we propose KAMI, a set of 1D, 2D, and 3D GEMM algorithms that extend the theory of communication-avoiding (CA) techniques within a single GPU. KAMI optimizes thread block-level GEMM by utilizing tensor cores as computational units, low-latency thread registers as local memory, and high-latency on-chip shared memory as a communication medium. We provide a theoretical analysis of CA performance from the perspective of GPU clock cycles, rather than the traditional execution time. Also, we implement SpMM and SpGEMM with this compute-communication pattern. Experimental results for general, low-rank, batched and sparse multiplication operations on the latest NVIDIA, AMD, and Intel GPUs show

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
