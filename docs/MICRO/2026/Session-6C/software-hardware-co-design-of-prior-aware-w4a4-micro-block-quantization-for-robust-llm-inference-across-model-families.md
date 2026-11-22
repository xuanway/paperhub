---
title: "Software-Hardware Co-Design of Prior-Aware W4A4 Micro-Block Quantization for Robust LLM Inference Across Model Families"
description: "MICRO 2026 · Session 6C · 先验感知 W4A4 微块量化的软硬件协同设计，实现跨模型家族的稳健 LLM 推理"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Quantization"
  - "HW-SW Co-design"
---

# Software-Hardware Co-Design of Prior-Aware W4A4 Micro-Block Quantization for Robust LLM Inference Across Model Families

**中文标题：** 先验感知 W4A4 微块量化的软硬件协同设计，实现跨模型家族的稳健 LLM 推理

**所属 Session：** [Session 6C](index.md) · [MICRO 2026](../index.md)

**作者：** Yijian Wei, Tianchang Yang, Sicheng Tao, Miao Hao, Tianyi Liu, Tingting Zhang, Fuxin Zhang, Jian Wang

**来源：** MICRO 2026，pp. 2084–2100；[DOI](https://doi.org/10.1109/MICRO67795.2026.00145)

## 英文摘要

Jointly quantizing both weights and activations to 4 bits (W4A4) has become increasingly popular for efficient large language model inference, but robust activation quantization across model families remains difficult. Industrial FP4 micro- block formats such as NVFP4 and MXFP4 still show large robustness disparities across model families, indicating that current methods lack outlier awareness at the micro-block level. We find that this disparity is mainly determined by a small frac- tion of all micro-blocks. These micro-blocks have high internal variance, and we define them as vulnerable micro-blocks (VMBs). Existing methods often improve activation handling through mixed-precision implementation or expensive calibration, but these choices increase hardware cost or calibration cost. We propose MBPriorQ, a software-hardware co-design for robust LLM inference under W4A4 post-training quantization. MBPri- orQ selectively refines only VMBs, uses low-cost online prior refinement to track their temporal variation, and is supported by a low-overhead mixed-granularity hardware implementation. Across 19 model entries from multiple model families, MBPriorQ achieves the strongest robustness in our evaluation. It reduces perplexity degradation by up to 40 percent on vulnerable models relative to NVFP4 with minimal storage overhead on average and negligible dense-calibration compute overhead. Compared with state-of-the-art open accelerator designs, MBPriorQ delivers speedups ranging from 1.16 to 2.28 times for core matrix multiplication. These results show that robust W4A4 micro-block quantization across model families can remain practical under a low-overhead hardware implementation.

## 中文摘要

对于高效的大语言模型推理来说，将权重和激活联合量化为 4 位 (W4A4) 已变得越来越流行，但跨模型系列的鲁棒激活量化仍然很困难。工业 FP4 微块格式（例如 NVFP4 和 MXFP4）在模型系列之间仍然表现出巨大的鲁棒性差异，这表明当前的方法缺乏微块级别的异常值意识。我们发现这种差异主要是由所有微块的一小部分决定的。这些微块具有很高的内部方差，我们将它们定义为易受攻击的微块（VMB）。现有方法通常通过混合精度实现或昂贵的校准来改进激活处理，但这些选择会增加硬件成本或校准成本。我们提出了 MBPriorQ，这是一种软件-硬件协同设计，用于在 W4A4 训练后量化下进行稳健的 LLM 推理。 MBPriorQ 仅选择性地细化 VMB，使用低成本在线先验细化来跟踪其时间变化，并由低开销混合粒度硬件实现支持。在来自多个模型系列的 19 个模型条目中，MBPriorQ 在我们的评估中实现了最强的鲁棒性。相对于 NVFP4，它可以将易受攻击的模型的困惑度降低最多 40%，平均存储开销最小，密集校准计算开销可以忽略不计。与最先进的开放式加速器设计相比，MBPriorQ 可为核心矩阵乘法提供 1.16 至 2.28 倍的加速。这些结果表明，跨模型系列的稳健 W4A4 微块量化在低开销硬件实现下仍然实用。

## 中文关键词

大语言模型；训练后量化；软硬件协同设计；W4A4；微块量化

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21505490](https://doi.org/10.5281/zenodo.21505490)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6C](index.md) · [MICRO 2026 主页](../index.md)
