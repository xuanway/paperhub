---
title: "TurboFNO: High-Performance Fourier Neural Operator with Fused FFT-GEMM-iFFT on GPU"
description: "SC 2025 · Machine Learning: Methods · Shixun Wu; Yujia Zhai; Hairui Zhao; Huangliang Dai; Yue Zhu; Haiyang Hu; Zizhong"
tags:
  - "SC2025"
  - "Machine Learning: Methods"
---

# TurboFNO: High-Performance Fourier Neural Operator with Fused FFT-GEMM-iFFT on GPU

**中文标题：** 利用 GPU 融合 FFT、GEMM 与逆 FFT 实现高性能傅里叶神经算子

**所属 Session：** [Machine Learning: Methods](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Methods</p>
</div>

**作者**：Shixun Wu; Yujia Zhai; Hairui Zhao; Huangliang Dai; Yue Zhu; Haiyang Hu; Zizhong Chen

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap137&sess=sess183)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Fourier neural operators (FNOs) are widely used for learning partial differential equation solution operators. However, FNOs lack architecture-aware optimizations, with their Fourier layers executing FFT, filtering, GEMM, zero padding, and iFFT as separate stages, incurring multiple kernel launches and significant global memory traffic. We propose TurboFNO, the first fully fused FFT-GEMM-iFFT GPU kernel with built-in FFT optimizations. We first develop FFT and GEMM kernels from scratch, achieving performance comparable to cuBLAS and cuFFT. Additionally, our FFT integrates a built-in high-frequency truncation, input zero-padding, and pruning feature to avoid additional memory copy kernels. To fuse FFT and GEMM, we propose an FFT variant where a threadblock iterates over hidden dimension to align with GEMM’s $k$-loop, along with two shared memory swizzling patterns that ensure 100\% bank utilization when forwarding FFT output to GEMM and retrieving results for iFFT. Experimental results

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
