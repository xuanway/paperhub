---
title: "TNT: A Unified LUT-Centric Architecture for Ultra-Low-Bit LLM Inference via Native KV Computation"
description: "MICRO 2026 · Session 1B · TNT：通过原生 KV 计算实现超低比特大语言模型推理的统一查找表架构"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Quantization"
---

# TNT: A Unified LUT-Centric Architecture for Ultra-Low-Bit LLM Inference via Native KV Computation

**中文标题：** TNT：通过原生 KV 计算实现超低比特大语言模型推理的统一查找表架构

**所属 Session：** [Session 1B](index.md) · [MICRO 2026](../index.md)

**作者：** Zhirui Huang, Rui Ma, Ran Shu, Ting Cao, Chixiao Chen, Yongqiang Xiong

**来源：** MICRO 2026，pp. 191–206；[DOI](https://doi.org/10.1109/MICRO67795.2026.00029)

## 英文摘要

Quantizing both LLM weights and KV caches to ultra-low precision offers a promising path to improving compute efficiency and reducing memory footprint. Yet most efforts focus primarily on memory compression, overlooking the compute-efficiency potential of ultra-low-bit KV caches. The root cause is that ultra-low-bit KV quantization introduces a scaling direction orthogonal to the accumulation path of conventional tensor cores, necessitating expensive runtime dequantization and thereby capping compute efficiency. To enable end-to-end ultra-low-bit LLM inference, our key insight is a Prescale-then-LUT (lookup table) compute paradigm that exploits the outer-dimension sharing property of LUT-based computation to eliminate runtime dequantization. Based on this insight, we propose TNT, a LUT-centric algorithm-hardware co-design framework which centers on a Ternary LUT Core (TLC) that natively realizes low-bit attention computation via a Fused-Precomputing pipeline. To further improve TLC efficiency, we introduce an Orthogonal Two-Level Quantization (OTQ) that eliminates expensive floating-point arithmetic from the LUT pipeline. For high accuracy, we further propose Query-Aware Saliency Prediction (QSP), a dynamic mixed-precision KV quantization mechanism that enables structured block-wise attention computation as well as efficient memory compression. Built upon these techniques, the proposed TNT accelerator integrates a lightweight tile-based mixed-precision pipeline to orchestrate QSP execution and maximize TLC utilization. Extensive evaluations show that TNT achieves up to 6.2× KV cache compression versus the FP16 baseline while preserving accuracy. Hardware results demonstrate up to 3.3× speedup and 2.8× energy-efficiency improvement over three state-of-the-art accelerators, and up to 6.25× end-to-end speedup compared to FP16 tensor cores on Nvidia A100 GPU.

## 中文摘要

将 LLM 权重和 KV 缓存量化到超低精度为提高计算效率和减少内存占用提供了一条有希望的途径。然而，大多数努力主要集中在内存压缩上，忽视了超低位 KV 缓存的计算效率潜力。根本原因是超低位 KV 量化引入了与传统张量核心的累积路径正交的缩放方向，需要昂贵的运行时反量化，从而限制了计算效率。为了实现端到端超低位 LLM 推理，我们的关键见解是 Prescale-then-LUT（查找表）计算范式，该范式利用基于 LUT 的计算的外部维度共享属性来消除运行时反量化。基于这一见解，我们提出了 TNT，一种以 LUT 为中心的算法硬件协同设计框架，以三元 LUT 核心（TLC）为中心，通过融合预计算管道本机实现低位注意力计算。为了进一步提高 TLC 效率，我们引入了正交两级量化 (OTQ)，它消除了 LUT 管道中昂贵的浮点运算。为了获得高精度，我们进一步提出了查询感知显着性预测（QSP），这是一种动态混合精度 KV 量化机制，可以实现结构化的分块注意力计算以及高效的内存压缩。基于这些技术，所提出的 TNT 加速器集成了一个轻量级的基于分块的混合精度管道，以编排 QSP 执行并最大限度地提高 TLC 利用率。广泛的评估表明，与 FP16 基线相比，TNT 实现了高达 6.2 倍的 KV 缓存压缩，同时保持了准确性。硬件结果表明，与三个最先进的加速器相比，速度提高了 3.3 倍，能效提高了 2.8 倍，与 Nvidia A100 GPU 上的 FP16 张量核心相比，端到端加速提高了 6.25 倍。

## 中文关键词

大语言模型；键值缓存量化；键值缓存；查找表；算法与硬件协同设计

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1B](index.md) · [MICRO 2026 主页](../index.md)
