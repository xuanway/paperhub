---
title: "SkewQ: Skewness-Aware Cross-Layer Quantization for Efficient LLM Inference via Software-Hardware Co-Design"
description: "MICRO 2026 · Session 6C · SkewQ：通过软硬件协同设计实现偏度感知跨层量化与高效 LLM 推理"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Quantization"
  - "HW-SW Co-design"
---

# SkewQ: Skewness-Aware Cross-Layer Quantization for Efficient LLM Inference via Software-Hardware Co-Design

**中文标题：** SkewQ：通过软硬件协同设计实现偏度感知跨层量化与高效 LLM 推理

**所属 Session：** [Session 6C](index.md) · [MICRO 2026](../index.md)

**作者：** Wenju Zhao, Jianhui Yue, Pengcheng Yao, Jiaqi Zhai, Yundong Zhang, Yu Huang, Shunsen Lv, Bing Zhu, Zhongtian Long, Long Zheng, Chencheng Ye, Lihong Gu, Jingling Xue, Hai Jin, Xiaofei Liao

**来源：** MICRO 2026，pp. 2117–2131；[DOI](https://doi.org/10.1109/MICRO67795.2026.00147)

## 英文摘要

Large language models (LLMs) deliver state-of-the-art performance but incur substantial compute and memory costs during inference due to their massive parameter sizes. While weight quantization reduces these costs, existing approaches suffer significant accuracy degradation below 4-bit precision. In this work, we show that LLM layer sensitivities follow a highly skewed distribution, where a small fraction of weight substructures across layers dominates inference quality. This challenges prior strategies based on uniform allocation or relative sensitivity ranking, which fail to capture the magnitude disparity of importance. Leveraging this insight, we propose SkewQ, a skewness-aware cross-layer quantization framework with software-hardware co-design. SkewQ employs tile-based cross-layer quantization to capture fine-grained parameter importance and introduces an automatic bit-allocation strategy that assigns precision based on global importance. Combined with a differential quantization scheme, SkewQ enables 3-bit quantization with minimal accuracy loss. To translate this compression into hardware efficiency, SkewQ introduces an Add-First Dot Product (AFDP) microarchitecture that reduces both multiplication and dequantization overhead. Across representative LLMs, SkewQ improves speed and energy efficiency by 1.16x-1.77x and 1.07x-1.41x for generative inference, and by 1.61x–1.86x and 1.25x–1.46x for discriminative inference, over ANT, OliVe, and BitMoD.

## 中文摘要

大语言模型 (LLM) 提供最先进的性能，但由于其庞大的参数大小，在推理过程中会产生大量的计算和内存成本。虽然权重量化降低了这些成本，但现有方法的精度显着下降，低于 4 位精度。在这项工作中，我们证明了 LLM 层敏感性遵循高度倾斜的分布，其中跨层权重子结构的一小部分主导了推理质量。这对基于统一分配或相对敏感性排名的先前策略提出了挑战，这些策略无法捕捉重要性的大小差异。利用这种洞察力，我们提出了 SkewQ，一种具有软硬件协同设计的偏度感知跨层量化框架。 SkewQ 采用基于分块的跨层量化来捕获细粒度参数重要性，并引入自动位分配策略，根据全局重要性分配精度。与差分量化方案相结合，SkewQ 能够以最小的精度损失实现 3 位量化。为了将这种压缩转化为硬件效率，SkewQ 引入了先加点积 (AFDP) 微架构，可减少乘法和反量化开销。在代表性的大语言模型中，与 ANT、OliVe 和 BitMoD 相比，SkewQ 将生成推理的速度和能效提高了 1.16x-1.77x 和 1.07x-1.41x，将判别推理提高了 1.61x-1.86x 和 1.25x-1.46x。

## 中文关键词

大语言模型；量化；软硬件协同设计；偏度感知；跨层优化

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6C](index.md) · [MICRO 2026 主页](../index.md)
