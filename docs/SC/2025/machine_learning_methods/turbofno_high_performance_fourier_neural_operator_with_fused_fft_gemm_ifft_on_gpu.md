---
title: "TurboFNO: High-Performance Fourier Neural Operator with Fused FFT-GEMM-iFFT on GPU"
description: "SC 2025 · Machine Learning: Methods · Shixun Wu; Yujia Zhai; Hairui Zhao; Huangliang Dai; Yue Zhu; Haiyang Hu; Zizhong"
tags:
  - "SC2025"
  - "Machine Learning: Methods"
---

# TurboFNO: High-Performance Fourier Neural Operator with Fused FFT-GEMM-iFFT on GPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Methods</p>
</div>

**作者**：Shixun Wu; Yujia Zhai; Hairui Zhao; Huangliang Dai; Yue Zhu; Haiyang Hu; Zizhong Chen

**会议**：SC 2025 · St. Louis, MO

## 摘要

Fourier neural operators (FNOs) are widely used for learning partial differential equation solution operators. However, FNOs lack architecture-aware optimizations, with their Fourier layers executing FFT, filtering, GEMM, zero padding, and iFFT as separate stages, incurring multiple kernel launches and significant global memory traffic. We propose TurboFNO, the first fully fused FFT-GEMM-iFFT GPU kernel with built-in FFT optimizations. We first develop FFT and GEMM kernels from scratch, achieving performance comparable to cuBLAS and cuFFT. Additionally, our FFT integrates a built-in high-frequency truncation, input zero-padding, and pruning feature to avoid additional memory copy kernels. To fuse FFT and GEMM, we propose an FFT variant where a threadblock iterates over hidden dimension to align with GEMM’s $k$-loop, along with two shared memory swizzling patterns that ensure 100\% bank utilization when forwarding FFT output to GEMM and retrieving results for iFFT. Experimental results 

---

## 一句话总结

> 该工作属于 Machine Learning: Methods 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Methods 领域贡献新的设计范式或评估框架。
