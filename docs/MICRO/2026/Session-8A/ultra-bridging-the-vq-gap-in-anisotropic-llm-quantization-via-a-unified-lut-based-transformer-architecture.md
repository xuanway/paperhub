---
title: "ULTRA: Bridging the VQ Gap in Anisotropic LLM Quantization via a Unified LUT-Based TRansformer Architecture"
description: "MICRO 2026 · Session 8A · ULTRA：通过统一查找表 Transformer 架构弥合各向异性 LLM 量化中的向量量化差距"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Quantization"
---

# ULTRA: Bridging the VQ Gap in Anisotropic LLM Quantization via a Unified LUT-Based TRansformer Architecture

**中文标题：** ULTRA：通过统一查找表 Transformer 架构弥合各向异性 LLM 量化中的向量量化差距

**所属 Session：** [Session 8A](index.md) · [MICRO 2026](../index.md)

**作者：** Zongwu Wang, Zhongyi Tang, Fangxin Liu, Shiyuan Huang, Chenyang Guan, Haomin Li, Gang Li, Liqiang Lu, Mingyu Gao, Li Jiang, Haibing Guan

**来源：** MICRO 2026，pp. 2770–2784；[DOI](https://doi.org/10.1109/MICRO67795.2026.00188)

## 英文摘要

Large Language Models (LLMs) are increasingly memory-bound during autoregressive decoding due to the massive movement of weights and KV caches. While Vector Quantization (VQ) offers a path to ultra-low-bit inference via lookup-table (LUT) based execution, existing VQ schemes exhibit a critical hardware-software mismatch: algorithmic codebook fragmentation forces frequent, low-reuse LUT reloads, while contemporary accelerators, optimized for dense matrix multiplication, lack native support for the index-gather and anisotropic table-lookup operations that VQ demands across heterogeneous linear layers. To bridge this gap, we propose ULTRA, a hardware-algorithm co-design for VQ-based LLM inference. Algorithmically, we eliminate codebook fragmentation via a hardware-friendly, block-wise framework with unified per-layer codebooks, enabling single-pass distance table construction through standard GEMM—a crucial step to leverage dense compute units. We recover sub-3-bit accuracy through a cascade of outlier-aware scaling and GPTQ-based error compensation. Architecturally, we address the resulting LUT access irregularity with a dual-mode computation engine that natively fuses both input-dimension and output-dimension VQ within a unified datapath, eliminating runtime dequantization overhead and fully enabling anisotropic quantization. Prototyped on a Xilinx U280 FPGA, ULTRA effectively bridges the gap between the theoretical compression benefits of VQ and practical deployment, delivering up to 2.63× end-to-end speedup over the FP16 GPU baseline and up to 2.97× over the state-of-the-art VQ framework Quip#, while achieving up to 35.6× energy efficiency improvement over Quip# on a commercial GPU.

## 中文摘要

由于权重和 KV 缓存的大量移动，大语言模型 (LLM) 在自回归解码过程中越来越受内存限制。虽然矢量量化 (VQ) 通过基于查找表 (LUT) 的执行提供了超低位推理的途径，但现有的 VQ 方案表现出严重的硬件-软件不匹配：算法码本碎片迫使频繁、低重用的 LUT 重新加载，而针对密集矩阵乘法进行优化的当代加速器缺乏对 VQ 跨异构线性层所需的索引收集和各向异性表查找操作的原生支持。为了弥补这一差距，我们提出了 ULTRA，这是一种用于基于 VQ 的 LLM 推理的硬件算法协同设计。在算法上，我们通过硬件友好的、具有统一每层码本的分块框架消除了码本碎片，从而通过标准 GEMM 实现单程距离表构建——这是利用密集计算单元的关键一步。我们通过一系列异常值感知缩放和基于 GPTQ 的误差补偿来恢复低于 3 位的精度。在架构上，我们使用双模式计算引擎解决了由此产生的 LUT 访问不规则性，该引擎在统一数据路径中本地融合输入维度和输出维度 VQ，消除运行时反量化开销并完全启用各向异性量化。 ULTRA 在 Xilinx U280 FPGA 上进行原型设计，有效弥合了 VQ 的理论压缩优势与实际部署之间的差距，与 FP16 GPU 基准相比，端到端加速高达 2.63 倍，与最先进的 VQ 框架 Quip# 相比，端到端加速高达 2.97 倍，同时在商用 GPU 上实现比 Quip# 高达 35.6 倍的能效提升。

## 中文关键词

大语言模型；向量量化；现场可编程门阵列；查找表；Transformer 架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8A](index.md) · [MICRO 2026 主页](../index.md)
