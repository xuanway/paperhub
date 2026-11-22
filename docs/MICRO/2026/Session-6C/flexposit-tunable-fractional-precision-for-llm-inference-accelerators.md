---
title: "FlexPosit: Tunable Fractional Precision for LLM Inference Accelerators"
description: "MICRO 2026 · Session 6C · FlexPosit：面向 LLM 推理加速器的可调小数精度"
tags:
  - "MICRO2026"
  - "LLM Inference"
---

# FlexPosit: Tunable Fractional Precision for LLM Inference Accelerators

**中文标题：** FlexPosit：面向 LLM 推理加速器的可调小数精度

**所属 Session：** [Session 6C](index.md) · [MICRO 2026](../index.md)

**作者：** Yimin Gao, Liangtao Dai, Jun Yin, Xinfei Guo, Mircea Stan

**来源：** MICRO 2026，pp. 2067–2083；[DOI](https://doi.org/10.1109/MICRO67795.2026.00144)

## 英文摘要

Large language models (LLMs) offer remarkable capabilities but impose prohibitive compute and energy costs. Quantization plays an essential role in practical inference deployment by helping govern the trade-offs between accuracy and hardware efficiency across the granularity and bit-width (precision) dimensions. Finer granularity (e.g., group-wise) has good accuracy but incurs large scaling and control overhead, while coarser granularity (e.g., channel-wise) has lower overhead but leads to losses in accuracy at lower precision. In terms of bit-width, modern mixed-precision quantization methods expose rich accuracy–efficiency trade-offs at the algorithmic level; however, existing LLM accelerators are limited to discrete precision modes. For aggressive low-bit regimes, the optimal precision under a fixed resource budget often lies between discrete levels—a fractional design space that existing hardware cannot exploit. FlexPosit bridges these gaps through co-design of Posit-based quantization and a precision-tunable bit-serial architecture that transforms precision into a tunable fractional design knob for jointly optimizing accuracy, throughput, and energy. Algorithmically, FlexPosit employs distribution-aware quantization with hardware-aligned, sensitivity-guided mixed-precision allocation, leveraging the Posit format's tapered precision to achieve group-wise-like accuracy with channel-wise-like regularity. Architecturally, FlexPosit is a unified bit-serial systolic array with lightweight per-column decoders, unified Processing Elements (PEs), and a global precision controller, enabling tunable fractional precision while preserving fully regular systolic dataflow. Evaluated across diverse LLMs, FlexPosit achieves near-FP16 accuracy with sub-5-bit fractional weights. Compared with state-of-the-art quantized LLM accelerators, it achieves 1.8× higher throughput and 1.2× lower energy over BitMoD (group-wise quantization) and 1.5× higher throughput and 2.0× lower energy over OliVe (channel-wise quantization), establishing a new Pareto frontier for precision-tunable LLM acceleration.

## 中文摘要

大语言模型 (LLM) 提供卓越的功能，但会带来高昂的计算和能源成本。量化通过帮助管理跨粒度和位宽（精度）维度的准确性和硬件效率之间的权衡，在实际推理部署中发挥着重要作用。较细的粒度（例如，按组）具有良好的准确性，但会产生较大的缩放和控制开销，而较粗的粒度（例如，按通道）具有较低的开销，但会导致较低精度下的准确性损失。就位宽而言，现代混合精度量化方法在算法层面暴露了丰富的精度与效率权衡；然而，现有的大语言模型加速器仅限于离散精度模式。对于激进的低位机制，固定资源预算下的最佳精度通常位于离散级别之间——现有硬件无法利用的部分设计空间。 FlexPosit 通过基于 Posit 的量化和精度可调位串行架构的共同设计来弥补这些差距，该架构将精度转换为可调分数设计旋钮，以共同优化精度、吞吐量和能量。在算法上，FlexPosit 采用分布感知量化和硬件对齐、灵敏度引导的混合精度分配，利用 Posit 格式的锥形精度来实现类似分组的精度和类似通道的规律性。从架构上讲，FlexPosit 是一个统一的位串行脉动阵列，具有轻量级每列解码器、统一的处理元件 (PE) 和全局精度控制器，可实现可调分数精度，同时保留完全规则的脉动数据流。经过不同大语言模型的评估，FlexPosit 通过低于 5 位的分数权重实现了接近 FP16 的精度。与最先进的量化LLM加速器相比，它的吞吐量比BitMoD（分组量化）高1.8倍，能耗低1.2倍，比OliVe（通道量化）吞吐量高1.5倍，能耗低2.0倍，为精确可调的LLM加速建立了新的帕累托前沿。

## 中文关键词

大语言模型推理；混合精度量化；Posit 算术；精度可调加速器

## 代码与研究制品

- 代码仓库：[https://github.com/hplp/FlexPosit](https://github.com/hplp/FlexPosit)
- 代码与复现实验仓库：[https://github.com/hplp/FlexPosit_artifact](https://github.com/hplp/FlexPosit_artifact)
- 研究制品归档：[https://doi.org/10.5281/zenodo.22681859](https://doi.org/10.5281/zenodo.22681859)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6C](index.md) · [MICRO 2026 主页](../index.md)
