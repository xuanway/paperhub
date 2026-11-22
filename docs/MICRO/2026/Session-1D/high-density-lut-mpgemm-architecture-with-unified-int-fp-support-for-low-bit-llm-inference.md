---
title: "High-Density LUT mpGEMM Architecture with Unified INT/FP Support for Low-Bit LLM Inference"
description: "MICRO 2026 · Session 1D · 面向低比特 LLM 推理、统一支持整数与浮点运算的高密度查找表 mpGEMM 架构"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Quantization"
---

# High-Density LUT mpGEMM Architecture with Unified INT/FP Support for Low-Bit LLM Inference

**中文标题：** 面向低比特 LLM 推理、统一支持整数与浮点运算的高密度查找表 mpGEMM 架构

**所属 Session：** [Session 1D](index.md) · [MICRO 2026](../index.md)

**作者：** Jiageng Shi, Yang Shi, Hao Wang, Ruiqiang Song, Jingwei Cai, Zhe Li, Junzhong Shen, Chen Xu, Yaohua Wang

**来源：** MICRO 2026，pp. 404–417；[DOI](https://doi.org/10.1109/MICRO67795.2026.00043)

## 英文摘要

With the rapid adoption of low-bit large language models (LLMs), mixed-precision GEMM (mpGEMM) has become a key efficiency bottleneck, which entails multiplying low-precision weights with high-precision activations. Lookup table (LUT)-based mpGEMM is a promising alternative that exploits data reuse opportunities by directly retrieving precomputed partial sums (psums). However, 2existing LUT-based designs suffer from two fundamental deficiencies. First, the reliance on inherently integer-only bit-serial compression renders them incompatible with modern FP4-family weights. Second, they necessitate dedicated precomputing units that, despite a duty cycle of less than 1%, may occupy up to 1/2 of the core area, leading to a severe structural area-utility paradox. To bridge these gaps, we propose Slime, the first high-density format-unified LUT-based mpGEMM architecture that provides native support for a diverse spectrum of 4-bit (and lower) integer and floating-point formats, including those with fine-grained scaling. Slime is underpinned by two key architectural innovations: (1) Exp-fold, a mathematical-to-architectural unification method that decomposes numbers into base and exponent components. By structurally folding the static exponential logic out of the memory table, it forms a highly compressed common representation, enabling a single LUT fabric to process both INT4 and FP4-family weights seamlessly. (2) Flow-match, a dynamic resource-recycling mechanism that repurposes the LUT fabric between precomputing and computation modes. It adaptively matches the hardware throughput and resource flow to the varying granularities of modern block-wise scaling. These mechanisms are physically realized through a novel multi-mapping LUT fabric that decouples logical lookups from physical storage. At core level, RTL implementation and evaluation demonstrate that Slime achieves up to 2.8× higher compute density and 1.2× higher energy efficiency compared to state-of-the-art LUT-based accelerators across representative LLM workloads.

## 中文摘要

随着低位大语言模型（LLM）的快速采用，混合精度 GEMM（mpGEMM）已成为关键的效率瓶颈，这需要将低精度权重与高精度激活相乘。基于查找表 (LUT) 的 mpGEMM 是一种很有前途的替代方案，它通过直接检索预先计算的部分和 (psum) 来利用数据重用机会。然而，现有的基于 LUT 的设计存在两个基本缺陷。首先，对固有的纯整数位串行压缩的依赖使得它们与现代 FP4 系列权重不兼容。其次，它们需要专用的预计算单元，尽管占空比小于 1%，但可能会占用高达 1/2 的核心区域，导致严重的结构面积-效用悖论。为了弥补这些差距，我们提出了 Slime，这是第一个基于 LUT 的高密度格式统一 mpGEMM 架构，它为各种 4 位（及更低）整数和浮点格式（包括具有细粒度缩放的格式）提供原生支持。 Slime 的基础是两个关键的架构创新：(1) Exp-fold，一种数学到架构的统一方法，可将数字分解为基数和指数分量。通过在结构上将静态指数逻辑折叠出内存表，它形成了高度压缩的通用表示，使单个 LUT 结构能够无缝处理 INT4 和 FP4 系列权重。 (2) Flow-match，一种动态资源回收机制，可在预计算和计算模式之间重新调整 LUT 结构的用途。它自适应地将硬件吞吐量和资源流与现代块级扩展的不同粒度相匹配。这些机制是通过一种新颖的多重映射 LUT 结构在物理上实现的，该结构将逻辑查找与物理存储分离。在核心级别，RTL 实施和评估表明，与最先进的基于 LUT 的加速器相比，Slime 在代表性的 LLM 工作负载中实现了高达 2.8 倍的计算密度和 1.2 倍的能效。

## 中文关键词

大语言模型；混合精度矩阵乘法；查找表；低比特量化；神经处理单元

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

## 来源核对说明

论文集元数据在“existing”前夹入了一个孤立数字；中文译文按 PDF 的正常句意整理。

[返回 Session 1D](index.md) · [MICRO 2026 主页](../index.md)
