---
title: "LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving"
description: "SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization · Huanqi Hu; Bowen Xiao; Shixuan Sun; Jianian Yin; Zhexi Zhang; Xiang Luo; Chengqu"
tags:
  - "SC2025"
  - "Algorithms: Matrix Multiplication and GEMM Optimization"
---

# LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving

**中文标题：** 面向高性能大语言模型服务的硬件高效 W4A8 GEMM 内核

**所属 Session：** [Algorithms: Matrix Multiplication and GEMM Optimization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matrix Multiplication and GEMM Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matrix Multiplication and GEMM Optimization</p>
</div>

**作者**：Huanqi Hu; Bowen Xiao; Shixuan Sun; Jianian Yin; Zhexi Zhang; Xiang Luo; Chengquan Jiang; Weiqi Xu; Xiaoying Jia; Xin Liu; Minyi Guo

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap605&sess=sess285)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Quantization is a critical technique for accelerating LLM inference by reducing memory footprint and improving computational efficiency. Among various schemes, 4-bit weight and 8-bit activation quantization (W4A8) offers a strong balance between accuracy and performance. However, existing W4A8 GEMM kernels fall short in practice due to inefficient dequantization on CUDA Cores, which cannot keep pace with the high throughput of Tensor Cores. In this paper, we present LiquidGEMM, a hardware-efficient W4A8 GEMM kernel for efficient LLM serving. LiquidGEMM designs two key techniques: LiquidQuant, a hardware-efficient quantization method that enables fast, overflow-safe dequantization using just two arithmetic instructions per four elements; and an implicit fine-grained pipeline that fully overlaps weight loading, dequantization, and MMA across warp groups without software synchronization or redundant memory traffic. Experimental results show that LiquidGEMM achieves up to 2.90x speedup ove

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
