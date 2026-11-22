---
title: "Ultra-DSP: A Universal Lossless DSP Overpacking Framework for Low-Bit LLM Inference"
description: "MICRO 2026 · Session 9A · Ultra-DSP：面向低比特 LLM 推理的通用无损 DSP 超额打包框架"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Quantization"
---

# Ultra-DSP: A Universal Lossless DSP Overpacking Framework for Low-Bit LLM Inference

**中文标题：** Ultra-DSP：面向低比特 LLM 推理的通用无损 DSP 超额打包框架

**所属 Session：** [Session 9A](index.md) · [MICRO 2026](../index.md)

**作者：** Chenyu Zhang, Chenxi Xu, Jiaxiang Zou, Jingyu Guo, Rui Meng, Xinyu Chen

**来源：** MICRO 2026，pp. 3162–3178；[DOI](https://doi.org/10.1109/MICRO67795.2026.00213)

## 英文摘要

Quantized LLM inference on FPGAs relies heavily on low-bit multiply-accumulate (MAC) operations. Yet DSPs, the main MAC engines in FPGAs, are built for high-precision computation and are therefore severely underutilized by low-bit arithmetic. Existing DSP packing techniques improve efficiency by packing multiple low-precision operations into one DSP, but they still cannot simultaneously achieve lossless high-density overpacking, universal support across precisions and DSP configurations, and efficient execution for both prefilling and decoding. In this paper, we propose Ultra-DSP, a high-density, lossless, and universal DSP overpacking framework for low-bit LLM inference. First, Ultra-DSP enables lossless high-density overpacking by decoupling signs from the packing domain and correcting overlap-induced MSB, LSB, and carry errors through coordinated boundary correction and LSB concatenation. Second, it introduces an overhead-aware Integer Linear Programming (ILP) solver that automatically generates efficient overpacking layouts across different precisions. Third, it builds a sharing-aware Adaptive Compute Engine (ACE) that supports both prefilling and decoding through hybrid packing-layout selection and shared correction hardware. Evaluations show that Ultra-DSP achieves 1.5x-2.25x higher throughput than state-of-the-art DSP packing baselines, delivers a 2.22x geometric-mean energy-efficiency gain over FlightLLM, and improves energy efficiency by up to 9.43x over the GPU baseline on batch-1 GEMV workloads. The Ultra-DSP source code is available at https://github.com/zcy-001-001/Ultra-DSP-MICRO26-AE.

## 中文摘要

FPGA 上的量化 LLM 推理很大程度上依赖于低位乘法累加 (MAC) 运算。然而，DSP（FPGA 中的主要 MAC 引擎）是为高精度计算而构建的，因此低位运算的利用率严重不足。现有的DSP打包技术通过将多个低精度运算打包到一个DSP中来提高效率，但仍然无法同时实现无损高密度过打包、跨精度和DSP配置的通用支持以及预填充和解码的高效执行。在本文中，我们提出了 Ultra-DSP，一种用于低位 LLM 推理的高密度、无损且通用的 DSP 过度封装框架。首先，Ultra-DSP 通过从打包域中解耦符号并通过协调边界校正和 LSB 串联来校正重叠引起的 MSB、LSB 和进位错误，从而实现无损高密度过打包。其次，它引入了一个开销感知整数线性规划 (ILP) 求解器，可以自动生成跨不同精度的高效重叠布局。第三，它构建了一个共享感知的自适应计算引擎（ACE），通过混合打包布局选择和共享校正硬件支持预填充和解码。评估表明，与最先进的 DSP 封装基准相比，Ultra-DSP 的吞吐量提高了 1.5 倍至 2.25 倍，与 FlightLLM 相比，几何平均能效增益提高了 2.22 倍，在批量 1 GEMV 工作负载上，能效比 GPU 基准提高了 9.43 倍。 Ultra-DSP 源代码可从 https://github.com/zcy-001-001/Ultra-DSP-MICRO26-AE 获取。

## 中文关键词

数字信号处理单元；无损超打包；低比特大语言模型推理；现场可编程门阵列

## 代码与研究制品

- 代码仓库：[https://github.com/CLab-HKUST-GZ/Ultra-DSP-MICRO26-AE](https://github.com/CLab-HKUST-GZ/Ultra-DSP-MICRO26-AE)
- 代码与复现实验仓库：[https://github.com/zcy-001-001/Ultra-DSP-MICRO26-AE](https://github.com/zcy-001-001/Ultra-DSP-MICRO26-AE)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21485040](https://doi.org/10.5281/zenodo.21485040)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9A](index.md) · [MICRO 2026 主页](../index.md)
