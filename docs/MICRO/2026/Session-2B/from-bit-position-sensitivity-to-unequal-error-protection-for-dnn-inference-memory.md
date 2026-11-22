---
title: "From Bit-Position Sensitivity to Unequal Error Protection for DNN Inference Memory"
description: "MICRO 2026 · Session 2B · 从比特位置敏感性到 DNN 推理内存的不等错误保护"
tags:
  - "MICRO2026"
  - "Neural Networks"
---

# From Bit-Position Sensitivity to Unequal Error Protection for DNN Inference Memory

**中文标题：** 从比特位置敏感性到 DNN 推理内存的不等错误保护

**所属 Session：** [Session 2B](index.md) · [MICRO 2026](../index.md)

**作者：** Muhammad Husnain Mubarik, Karthik Mohan Kumar, Pedro Antonio Pena, Keshavan Varadarajan, Kunal Tyagi

**来源：** MICRO 2026，pp. 644–659；[DOI](https://doi.org/10.1109/MICRO67795.2026.00057)

## 英文摘要

We characterize per-bit-position fault sensitivity in ML inference across 16 workloads — spanning transformer based models and attention-free CNNs — and across three floating-point formats. Our central empirical finding is a sharp bit-sensitivity transition: flipping any of the least-significant fraction bits up to a data-type-specific threshold, Xsafe, degrades task metrics by less than 1% under deterministic single-bit stress tests. Sensitivity rises through the upper fraction bits and spikes at the exponent-mantissa boundary, where a single-bit flip causes catastrophic collapse. Because low-order bits are largely inconsequential while high-order and exponent bits are critical, uniform SECDED protection—which guards every bit equally at 12.5% storage overhead—is unnecessarily conservative. We derive per-data-type Xsafe floors {FP16: 6, BF16: 4, FP32: 15} and workload-aware tiers that widen the unprotected region for resilient model classes, raising ECC savings to 37.5–62.5% without retraining. Text-conditioned diffusion models dictate the conservative floor; vision encoders, NLU models, and resilient LLMs tolerate wider bypass regions. These floors and tiers drive an Unequal Error Protection (UEP) codec with per-cacheline data-type tags and a dual-partition SRAM architecture for ML accelerators. Validation across 870+ fault-injection runs confirms selective protection holds under contiguous 2- and 3-bit upsets. The codec reduces ECC area by 27.8% relative to uniform SECDED; dual-voltage operation of the non-critical partition lowers gross BF16 read energy by approximately 17%, with an approximately 4% dual-partition macro-area overhead.

## 中文摘要

我们描述了跨 16 个工作负载（涵盖基于Transformer的模型和无注意力 CNN）以及三种浮点格式的 ML 推理中的每比特位置故障敏感性。我们的核心实证发现是急剧的位敏感性转变：将任何最低有效分数位翻转到特定于数据类型的阈值 Xsafe，在确定性单位压力测试下，任务指标的性能下降不到 1%。灵敏度通过较高的分数位上升，并在指数尾数边界处达到峰值，其中一位翻转会导致灾难性崩溃。由于低阶位在很大程度上无关紧要，而高阶位和指数位至关重要，因此统一的 SECDED 保护（以 12.5% 的存储开销同等保护每一位）是不必要的保守。我们推导出每个数据类型的 Xsafe 楼层 {FP16: 6, BF16: 4, FP32: 15} 和工作负载感知层，扩大了弹性模型类的未受保护区域，无需重新训练即可将 ECC 节省提高到 37.5-62.5%。文本条件扩散模型决定保守下限；视觉编码器、NLU 模型和弹性 LLM 可以容忍更宽的旁路区域。这些层和层驱动具有每个缓存行数据类型标签的不等错误保护 (UEP) 编解码器和用于 ML 加速器的双分区 SRAM 架构。超过 870 次故障注入运行的验证证实了选择性保护在连续 2 位和 3 位翻转下保持不变。该编解码器相对于统一的 SECDED 减少了 27.8% 的 ECC 面积；非关键分区的双电压操作可将 BF16 总读取能量降低约 17%，双分区宏区域开销约降低 4%。

## 中文关键词

选择性纠错码；深度神经网络推理；比特位置敏感性；浮点可靠性；非均等错误保护

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 2B](index.md) · [MICRO 2026 主页](../index.md)
