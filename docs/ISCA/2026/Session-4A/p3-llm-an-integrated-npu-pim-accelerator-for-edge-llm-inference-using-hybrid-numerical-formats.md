---
title: "P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats"
description: "ISCA 2026 · Session 4A · P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats"
tags:
  - "ISCA2026"
  - "Session 4A"
  - "LLM 2"
---

# P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats

**中文标题：** P3-LLM: 使用混合数值格式的边缘 LLM 推理集成 NPU-PIM 加速器

**所属 Session：** [Session 4A](index.md) · [ISCA 2026](../index.md)

**作者：** Yuzong Chen, Chao Fang, Xilai Dai, Yuheng Wu, Thierry Tambe, Marian Verhelst, Mohamed S. Abdelfattah

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The substantial memory bandwidth and computational demands of large language models (LLMs) present critical challenges for efficient inference. To tackle this, the literature has explored heterogeneous systems that combine neural processing units (NPUs) with DRAM-based processing-in-memory (PIM) for LLM acceleration. However, the high-precision PIM compute units incur significant area and power overhead in DRAM technology, limiting the effective computation throughput. In this paper, we introduce P3-LLM, a novel NPU-PIM integrated accelerator for edge LLM inference. Our approach is threefold: First, we propose a flexible mixed-precision quantization scheme, which leverages hybrid numerical formats to quantize different LLM operands with high compression efficiency and minimal accuracy loss. Second, we architect an efficient PIM accelerator for P3-LLM, featuring enhanced compute units to support hybrid numerical formats. Our careful choice of numerical formats allows to co-design low-precision PIM compute units that significantly boost the computation throughput under iso-area constraints. Third, we optimize the low-precision dataflow of different LLM modules by applying operator fusion to minimize the overhead of runtime dequantization. Evaluations on diverse LLMs and tasks demonstrate that P3-LLM achieves higher accuracy than state-of-the-art KV-cache quantization and weight-activation quantization algorithms. Combining the proposed quantization scheme with low-precision PIM architecture co-design, P3-LLM yields an average of 4.9×, 2.0×, and 3.4× speedups over state-of-the-art LLM accelerators HBM-PIM, Ecco, and Pimba, respectively. Code is available at https://github.com/yc2367/P3-LLM.

## 中文摘要

大语言模型（LLM）的高内存带宽和计算需求给高效推理带来了严峻挑战。本文提出 P3-LLM，一种面向边缘 LLM 推理的 NPU-PIM 集成加速器。其方法包括三方面：一是提出灵活的混合精度量化方案，利用混合数值格式高效压缩不同 LLM 操作数且精度损失极小；二是设计增强的 PIM 计算单元以支持混合数值格式，在等面积约束下显著提升计算吞吐；三是通过算子融合优化低精度数据流，减少运行时反量化的开销。在多种 LLM 和任务上的评测表明，P3-LLM 在精度上优于最先进的 KV 缓存量化和权重-激活量化算法，相比 HBM-PIM、Ecco 和 Pimba 分别实现 4.9×、2.0× 和 3.4× 的平均加速。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：yc2367/P3-LLM](https://github.com/yc2367/P3-LLM)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2026](../index.md)
