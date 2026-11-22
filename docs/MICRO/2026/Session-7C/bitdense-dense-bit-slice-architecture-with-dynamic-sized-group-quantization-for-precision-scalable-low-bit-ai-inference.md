---
title: "BitDense: Dense Bit-Slice Architecture with Dynamic-Sized Group Quantization for Precision-Scalable Low-Bit AI Inference"
description: "MICRO 2026 · Session 7C · BitDense：采用动态分组大小量化的密集位切片架构，实现精度可扩展的低比特 AI 推理"
tags:
  - "MICRO2026"
  - "Quantization"
---

# BitDense: Dense Bit-Slice Architecture with Dynamic-Sized Group Quantization for Precision-Scalable Low-Bit AI Inference

**中文标题：** BitDense：采用动态分组大小量化的密集位切片架构，实现精度可扩展的低比特 AI 推理

**所属 Session：** [Session 7C](index.md) · [MICRO 2026](../index.md)

**作者：** Jungjun Oh, Sangjin Kim, Yueseon Choi, Jingu Lee, Hoi-Jun Yoo

**来源：** MICRO 2026，pp. 2577–2592；[DOI](https://doi.org/10.1109/MICRO67795.2026.00176)

## 英文摘要

Low-bit and group-wise quantization have become essential for scaling modern LLM inference, yet they fundamentally conflict with existing sparsity-driven bit-slice accelerators: slice-level zeros vanish under small group sizes, and multi-precision support incurs prohibitive sign-handling and reconfiguration overhead. Floating-point low-bit formats (e.g., MXFP, NVFP) mitigate some accuracy degradation but remain limited in precision scalability due to exponent–mantissa datapath complexity. We present BitDense, a dense integer bit-slice accelerator co-designed with a dynamic-sized group quantization algorithm to enable precise and energy-efficient low-bit inference. BitDense entirely eliminates slice skipping and employs a fully dense 2-bit datapath based on a Shared-Sign-Logic GEMM (SSL-GEMM), which removes slice-wise sign extension and bit-enlarged multipliers while preserving full two's-complement range. To reduce the high dequantization cost of small group sizes, we introduce Dynamic-Sized Group Quantization (DSGQ), a gradient-guided, channel-reordered quantization method that applies fine or coarse groups only where beneficial. A decoupled intra-/inter-group accumulation pipeline maintains high utilization across mixed group sizes. Evaluations show that BitDense achieves up to 2.56× higher speedup and 2.52× higher energy efficiency than the strongest sparsity-driven bit-slice accelerator baseline. Compared with the strongest dense LLM accelerator baseline using advanced quantization, BitDense achieves up to 1.64× higher speedup and 1.34× higher energy efficiency. BitDense also achieves better efficiency–accuracy trade-offs than industry FP formats such as MXFP and NVFP, establishing dense INT bit-slicing as a scalable path for future low-bit LLM hardware.

## 中文摘要

低位和分组量化对于扩展现代 LLM 推理至关重要，但它们从根本上与现有的稀疏驱动的位片加速器相冲突：片级零在小组大小下消失，并且多精度支持会产生令人望而却步的符号处理和重新配置开销。浮点低位格式（例如 MXFP、NVFP）可减轻一定程度的精度下降，但由于指数尾数数据路径的复杂性，精度可扩展性仍然受到限制。我们推出了 BitDense，这是一种密集整数位片加速器，与动态大小的组量化算法共同设计，可实现精确且节能的低位推理。 BitDense 完全消除了切片跳跃，并采用基于共享符号逻辑 GEMM (SSL-GEMM) 的全密集 2 位数据路径，它消除了切片符号扩展和位放大乘法器，同时保留完整的二进制补码范围。为了降低小组大小的高反量化成本，我们引入了动态大小组量化（DSGQ），这是一种梯度引导、通道重新排序的量化方法，仅在有益的情况下应用精细或粗略组。解耦的组内/组间累积管道可在混合组大小之间保持高利用率。评估表明，与最强的稀疏驱动位片加速器基线相比，BitDense 的加速比提高了 2.56 倍，能效提高了 2.52 倍。与使用高级量化的最强密集 LLM 加速器基线相比，BitDense 实现了高达 1.64 倍的加速比和 1.34 倍的能效。 BitDense 还实现了比 MXFP 和 NVFP 等行业 FP 格式更好的效率与准确性权衡，将密集 INT 位切片建立为未来低位 LLM 硬件的可扩展路径。

## 中文关键词

分组量化；低比特大语言模型推理；混合精度；位切片架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7C](index.md) · [MICRO 2026 主页](../index.md)
