---
title: "MXFFP: Microscaling Flexible Floating Point Format for Large-Scale AI Model Acceleration"
description: "ISCA 2026 · Session 10B · MXFFP: Microscaling Flexible Floating Point Format for Large-Scale AI Model Acceleration"
tags:
  - "ISCA2026"
  - "Session 10B"
  - "ML Accelerators 2"
---

# MXFFP: Microscaling Flexible Floating Point Format for Large-Scale AI Model Acceleration

**中文标题：** MXFFP: 面向大规模 AI 模型加速的微缩放灵活浮点格式

**所属 Session：** [Session 10B](index.md) · [ISCA 2026](../index.md)

**作者：** Sungwoo Kim, Sungbin Kim, Dongho Ha, Hyunwuk Lee, Junsung Kim, Seunghyun Lee, Mingu Jung, Murali Annavaram, Won Woo Ro

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The rise of AI/ML applications has reignited interest in floating-point formats beyond the IEEE 754 standard, leading to innovations such as Microscaling Floating-Point (MXFP). MXFP groups values into blocks that share a common exponent, allowing them to be represented as scaled FP values. This enables a reduced memory footprint and efficient hardware execution. However, due to the trend of shrinking bit-widths and increasing block sizes, MXFP faces growing inter-block and intra-block value diversity. The limited number of exponent and mantissa bits forces a tradeoff between range and precision across blocks, while packing more values into a block amplifies the variation within each block. As a result, fewer bits with larger blocks often lead to precision loss and degraded model accuracy. In this paper, we observe that these limitations can be addressed by flexibly assigning exponent and mantissa bits to match the value distribution of each block or element within a block, rather than relying on a single fixed MXFP configuration. Based on this observation, we propose MXFFP, a flexible numeric format that leverages diverse exponent-mantissa configurations at both the block and sub-block levels. This diversity allows MXFFP to better preserve the original value distribution, leading to higher inference accuracy for ML models even with larger block sizes. To support this format, we introduce efficient conversion mechanisms that transform FP16/BF16 values into MXFFP with a minimal runtime overhead and design a Tensor Core based hardware architecture that interprets and executes MXFFP using only a single configuration bit per block. Our evaluation shows that MXFFP significantly improves numerical accuracy, reducing perplexity by 2–5× in 4-bit settings across multiple LLMs, while maintaining hardware performance comparable to MXFP.

## 中文摘要

AI/ML 应用的兴起重新激发了对 IEEE 754 标准之外浮点格式的兴趣，催生了 Microscaling Floating-Point（MXFP）等创新。MXFP 将数值分组成共享同一指数的块，使其可表示为经过缩放的 FP 值。这带来了更低的内存占用和高效的硬件执行。然而，随着位宽不断收缩、块尺寸不断增大，MXFP 面临日益严重的块间与块内数值多样性问题。有限的指数位与尾数位数量迫使在块之间对范围与精度进行权衡，而将更多数值打包进一个块又会放大每个块内部的差异。因此，位宽更少、块更大的做法往往导致精度损失和模型准确率下降。在本文中，我们观察到：可以通过灵活地为块或块内元素分配指数位与尾数位，以匹配其数值分布，而不是依赖单一的固定 MXFP 配置，来缓解这些限制。基于这一观察，我们提出 MXFFP，一种灵活的数值格式，在块级和子块级利用多样化的指数-尾数配置。这种多样性使 MXFFP 能更好地保持原始数值分布，从而即使块尺寸更大也能为 ML 模型带来更高的推理精度。为支持该格式，我们引入了高效的转换机制，以极小的运行时开销将 FP16/BF16 数值转换为 MXFFP，并设计了一种基于 Tensor Core 的硬件架构，仅使用每块一个配置位来解释和执行 MXFFP。我们的评估表明，MXFFP 显著提升了数值精度，在 4-bit 设置下使多个 LLM 的困惑度降低 2–5×，同时保持与 MXFP 相当的硬件性能。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10B](index.md) · [返回 ISCA 2026](../index.md)
