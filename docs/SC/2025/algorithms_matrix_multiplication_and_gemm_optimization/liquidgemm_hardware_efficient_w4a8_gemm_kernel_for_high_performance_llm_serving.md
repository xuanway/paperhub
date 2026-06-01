---
title: "LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving"
description: "SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization · Huanqi Hu; Bowen Xiao; Shixuan Sun; Jianian Yin; Zhexi Zhang; Xiang Luo; Chengqu"
tags:
  - "SC2025"
  - "Algorithms: Matrix Multiplication and GEMM Optimization"
---

# LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matrix Multiplication and GEMM Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization</p>
</div>

**作者**：Huanqi Hu; Bowen Xiao; Shixuan Sun; Jianian Yin; Zhexi Zhang; Xiang Luo; Chengquan Jiang; Weiqi Xu; Xiaoying Jia; Xin Liu; Minyi Guo

**会议**：SC 2025 · St. Louis, MO

## 摘要

Quantization is a critical technique for accelerating LLM inference by reducing memory footprint and improving computational efficiency. Among various schemes, 4-bit weight and 8-bit activation quantization (W4A8) offers a strong balance between accuracy and performance. However, existing W4A8 GEMM kernels fall short in practice due to inefficient dequantization on CUDA Cores, which cannot keep pace with the high throughput of Tensor Cores. In this paper, we present LiquidGEMM, a hardware-efficient W4A8 GEMM kernel for efficient LLM serving. LiquidGEMM designs two key techniques: LiquidQuant, a hardware-efficient quantization method that enables fast, overflow-safe dequantization using just two arithmetic instructions per four elements; and an implicit fine-grained pipeline that fully overlaps weight loading, dequantization, and MMA across warp groups without software synchronization or redundant memory traffic. Experimental results show that LiquidGEMM achieves up to 2.90x speedup ove

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
