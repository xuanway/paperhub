---
title: "OASIS: Outlier-Aware LUT-Based GEMM with Dual-Side Quantization for LLM Inference Acceleration"
description: "ISCA 2026 · Session 3A · OASIS: Outlier-Aware LUT-Based GEMM with Dual-Side Quantization for LLM Inference Acceleration"
tags:
  - "ISCA2026"
  - "Session 3A"
  - "ML Accelerators 1"
---

# OASIS: Outlier-Aware LUT-Based GEMM with Dual-Side Quantization for LLM Inference Acceleration

**中文标题：** OASIS: 面向 LLM 推理加速的异常值感知双边量化 LUT GEMM

**所属 Session：** [Session 3A](index.md) · [ISCA 2026](../index.md)

**作者：** Xueying Wu, Baijun Zhou, Zhihui Gao, Yuzhe Fu, Qilin Zheng, Yintao He, Hai Li

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large language models (LLMs) have demonstrated impressive capabilities across a wide range of applications, but demand substantial memory and compute resources during inference. Existing quantization methods expose a trade-off between efficiency and accuracy: weight-only quantization (WOQ) incurs costly dequantization overheads, while integer weight-and-activation quantization (INT-WAQ) reduces precision and degrades model quality. Non-uniform weight-and-activation quantization (NU-WAQ) can better capture the non-uniform distributions of LLM weights and activations, yet remains incompatible with conventional low-precision compute units. This paper presents OASIS, a lookup table (LUT)-based architecture that enables efficient general matrix multiplication (GEMM) between non-uniformly quantized weights and activations without requiring dequantization. OASIS employs pre-computed Cartesian Product LUTs, achieving a 64× reduction in LUT size and enabling a 1024× higher computational parallelism over existing LUT-based GEMM methods. To preserve accuracy under aggressive activation quantization, OASIS introduces an outlier-aware quantization scheme with concurrent LUT-based GEMM and error compensation for outliers. Furthermore, we design Orizuru, an efficient top-k detection engine for real-time activation outlier identification. According to extensive evaluations, OASIS incurs an average accuracy drop of only 1.94% compared to the FP16 baseline, which is 6.34% lower than Atom. On the hardware side, OASIS achieves an average 3.00× speedup and a 1.44× energy efficiency improvement compared to the FIGLUT accelerator.

## 中文摘要

大语言模型（LLM）在各种应用中展现了令人印象深刻的能力，但在推理过程中需要大量的内存和计算资源。现有的量化方法在效率和精度之间需要权衡：仅权重量化（WOQ）带来了昂贵的反量化开销，而整数权值-激活值量化（INT-WAQ）降低了精度并损害了模型质量。非均匀权值-激活值量化（NU-WAQ）能够更好地捕捉LLM权值和激活值的非均匀分布，但与传统的低精度计算单元不兼容。本文提出OASIS，一种基于查找表（LUT）的架构，能够在非均匀量化的权值和激活值之间实现高效的通用矩阵乘法（GEMM），而无需反量化。OASIS采用预计算的笛卡尔积查找表，相比现有基于LUT的GEMM方法实现了64倍的查找表尺寸缩减和1024倍的计算并行度提升。为在激进的激活值量化下保持精度，OASIS引入了异常值感知量化机制，并结合了基于LUT的GEMM与异常值误差补偿。此外，我们设计了Orizuru，一种高效的top-k检测引擎，用于实时识别激活值异常。广泛评估表明，与FP16基线相比，OASIS的平均精度损失仅为1.94%，比Atom低6.34%。在硬件方面，与FIGLUT加速器相比，OASIS实现了平均3.00倍的加速和1.44倍的能效提升。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2026](../index.md)
