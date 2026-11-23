---
title: "LightNobel: Improving Sequence Length Limitation in Protein Structure Prediction Model via Adaptive Activation Quantization"
description: "ISCA 2025 · Session 10B · LightNobel：通过自适应激活量化突破蛋白质结构预测模型的序列长度限制"
tags:
  - "ISCA2025"
  - "Session 10B"
  - "Domain Specific Accelerators III"
---

# LightNobel: Improving Sequence Length Limitation in Protein Structure Prediction Model via Adaptive Activation Quantization

**中文标题：** LightNobel：通过自适应激活量化突破蛋白质结构预测模型的序列长度限制

**所属 Session：** [Session 10B](index.md) · [ISCA 2025](../index.md)

**作者：** Seunghee Han, Soongyu Choi, Joo-Young Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731006) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

翻译 Recent advances in Protein Structure Prediction Models (PPMs), such as AlphaFold2 and ESMFold, have revolutionized computa- tional biology by achieving unprecedented accuracy in predicting three-dimensional protein folding structures. However, these mod- els face significant scalability challenges, particularly when process- ing proteins with long amino acid sequences (e.g., sequence length > 1,000). The primary bottleneck that arises from the exponential growth in activation sizes is driven by the unique data structure in PPM, which introduces an additional dimension that leads to substantial memory and computational demands. These limitations have hindered the effective scaling of PPM for real-world applica- tions, such as analyzing large proteins or complex multimers with critical biological and pharmaceutical relevance. In this paper, we present LightNobel, the first hardware-software co-designed accelerator developed to overcome scalability limita- tions on the sequence length in PPM. At the software level, we pro- pose Token-wise Adaptive Activation Quantization (AAQ), which leverages unique token-wise characteristics, such as distogram patterns in PPM activations, to enable fine-grained quantization techniques without compromising accuracy. At the hardware level, LightNobel integrates the multi-precision reconfigurable matrix processing unit (RMPU) and versatile vector processing unit (VVPU) to enable the efficient execution of AAQ. Through these innova- tions, LightNobel achieves up to 8.44×, 8.41×speedup and 37.29×, 43.35×higher power efficiency over the latest NVIDIA A100 and H100 GPUs, respectively, while maintaining negligible accuracy loss. It also reduces the peak memory requirement up to 120.05×in PPM, enabling scalable processing for proteins with long sequences.

## 中文摘要

蛋白质结构预测模型（PPM），例如AlphaFold2、ESMFold等最新进展，彻底变革了计算生物学领域，可以超高精度预测蛋白质三维折叠结构。但这类模型在处理长氨基酸序列蛋白（例如序列长度>1000）时，面临严重的可扩展性瓶颈。PPM独特的数据结构会引入额外维度，造成激活值体量呈指数增长，带来巨大的显存与计算开销。这些短板制约了PPM在真实场景中的扩展，例如对具有重要生物学、制药价值的大型蛋白、复杂多聚体开展分析。

本文提出LightNobel，首款面向解决PPM序列长度扩展瓶颈的软硬件协同加速器。软件层面，提出**逐Token自适应激活量化（AAQ）**：利用PPM激活中距离图（distogram）等逐Token独有特征，实现细粒度量化，并且不损失精度。硬件层面，LightNobel集成多精度可重构矩阵处理单元（RMPU）与通用向量处理单元（VVPU），高效支撑AAQ的执行。

依托上述创新，在精度几乎无损的前提下，LightNobel对比最新NVIDIA A100、H100 GPU，最高分别提速8.44倍、8.41倍，功耗效率分别提升37.29倍、43.35倍；同时PPM峰值显存需求最高降低120.05倍，支持长序列蛋白的规模化推理。

## 英文关键词

Protein Structure Prediction Model (PPM), AlphaFold2, ESMFold, Attention-based Model, Quantization, Hardware Accelerator, Hardware-Software Co-design

## 中文关键词

蛋白质结构预测模型, AlphaFold2, ESMFold, 基于注意力的模型, 量化, 硬件加速器, 软硬件协同设计

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731006)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10B](index.md) · [返回 ISCA 2025](../index.md)
