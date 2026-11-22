---
title: "MiX: Micro-Inverted-Scaling for End-to-End Low-Bit Vision-Language Model Acceleration"
description: "MICRO 2026 · Session 7C · MiX：用于端到端低比特视觉语言模型加速的微粒度逆缩放"
tags:
  - "MICRO2026"
  - "Quantization"
---

# MiX: Micro-Inverted-Scaling for End-to-End Low-Bit Vision-Language Model Acceleration

**中文标题：** MiX：用于端到端低比特视觉语言模型加速的微粒度逆缩放

**所属 Session：** [Session 7C](index.md) · [MICRO 2026](../index.md)

**作者：** Yuan Liao, Jae-sun Seo

**来源：** MICRO 2026，pp. 2495–2511；[DOI](https://doi.org/10.1109/MICRO67795.2026.00171)

## 英文摘要

The deployment of Vision-Language Models (VLMs) on edge devices is severely bottlenecked by memory bandwidth, necessitating aggressive sub-8-bit quantization. Since edge accelerators are strictly constrained by area and power, they require end-to-end quantized models. However, the extreme dynamic range gap between multi-modal tokens causes standard block formats to suffer "microscaling collapse," where a single massive outlier hijacks the shared exponent, underflowing surrounding elements and destroying attention maps. To break this bottleneck, we propose Micro-Inverted-Scaling (MiX), a novel format that mathematically inverts the microscaling paradigm: rather than grouping multiple mantissas under one shared exponent, MiX groups private, per-element exponents under a single shared mantissa. To handle asymmetric VLM outlier topologies, we introduce an adaptive dual-format (MiX-MX) inference framework. By algebraically factoring out the shared MiX mantissa, this framework maps to a custom accelerator, replacing multipliers with efficient shifters. Evaluated end-to-end on multiple VLMs, our 4.5-bit MiX formulation exhibits equivalent or superior accuracy on multi-modal benchmarks compared to NVFP4. Simultaneously, the MiX accelerator delivers a 25% improvement in area efficiency over the NVFP4 baseline and a 2.3-4.5x speedup with 1.4-2.9x energy reduction across models compared to the state-of-the-art accelerator Focus, proving the inverted-scaling datapath is physically superior for efficient VLM deployment.

## 中文摘要

在边缘设备上部署视觉语言模型 (VLM) 受到内存带宽的严重瓶颈，需要积极的低于 8 位量化。由于边缘加速器受到面积和功率的严格限制，因此它们需要端到端的量化模型。然而，多模态标记之间的极端动态范围差距导致标准块格式遭受“微尺度崩溃”，其中单个巨大异常值劫持共享指数，使周围元素下溢并破坏注意力图。为了打破这一瓶颈，我们提出了微反转缩放（MiX），这是一种在数学上反转微缩放范式的新颖格式：MiX 不是将多个尾数分组在一个共享指数下，而是将私有的、每个元素的指数分组在单个共享尾数下。为了处理非对称 VLM 异常拓扑，我们引入了自适应双格式 (MiX-MX) 推理框架。通过以代数方式分解出共享的 MiX 尾数，该框架映射到自定义加速器，用高效的移位器取代乘法器。在多个 VLM 上进行端到端评估后，我们的 4.5 位 MiX 公式在多模式基准测试中表现出与 NVFP4 相当或更高的精度。同时，与最先进的加速器 Focus 相比，MiX 加速器的面积效率比 NVFP4 基准提高了 25%，加速提高了 2.3-4.5 倍，各个模型的能耗降低了 1.4-2.9 倍，这证明了反向扩展数据路径在物理上对于高效 VLM 部署而言具有优越性。

## 中文关键词

视觉语言模型；边缘计算；量化；软硬件协同设计；低比特推理

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21530344](https://doi.org/10.5281/zenodo.21530344)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 7C](index.md) · [MICRO 2026 主页](../index.md)
