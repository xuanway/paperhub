---
title: "T-MAC: CPU Renaissance via Table Lookup for Low-Bit LLM Deployment on Edge"
description: "EuroSys 2025 · LLM Serving · Jianyu Wei (USTC and Microsoft Research), Shijie Cao (Microsoft Research), Ting "
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# T-MAC: CPU Renaissance via Table Lookup for Low-Bit LLM Deployment on Edge

**中文标题：** 通过查表实现边缘低比特大语言模型部署中的 CPU 复兴

**所属 Session：** [Session 2.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Jianyu Wei (USTC and Microsoft Research), Shijie Cao (Microsoft Research), Ting Cao (Microsoft Research), Lingxiao Ma (Microsoft Research), Lei Wang (UCAS and Microsoft Research), Yanyong Zhang (University of Science and Technology of China), Mao Yang (Microsoft Research)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696099)

## 英文摘要

The deployment of Large Language Models (LLMs) on edge devices is increasingly important to enhance on-device intelligence. Weight quantization is crucial for reducing the memory footprint of LLMs on devices. However, low-bit LLMs necessitate mixed precision matrix multiplication (mpGEMM) of low precision weights and high precision activations during inference. Existing systems, lacking native support for mpGEMM, resort to dequantize weights for high precision computation. Such an indirect way can lead to a significant inference overhead.

In this paper, we introduce T-MAC, an innovative lookup table(LUT)-based method designed for efficient low-bit LLM (i.e., weight-quantized LLM) inference on CPUs. T-MAC directly supports mpGEMM without dequantization, while simultaneously eliminating multiplications and reducing additions required. Specifically, T-MAC transforms the traditional data-type-centric multiplication to bit-wise table lookup, and enables a unified and scalable mpGEMM solution.

Our LUT-based kernels scale linearly to the weight bitwidth. Evaluated on low-bit Llama and BitNet models, T-MAC demonstrates up to 4× increase in throughput and 70% reduction in energy consumption compared to llama.cpp. For BitNet-b1.58-3B, T-MAC delivers a token generation throughput of 30 tokens/s with a single core and 71 tokens/s with eight cores on M2-Ultra, and 11 tokens/s on Raspberry Pi 5. T-MAC with LUT-based computing paradigm, paves the way for the practical deployment of low-bit LLMs on resource-constrained edge devices without compromising computational efficiency. The system is open-sourced at https://github.com/microsoft/T-MAC.

## 中文摘要

在边缘设备上部署大语言模型（LLM）对于增强端侧智能日益重要。权重量化是降低 LLM 在设备上内存占用的关键。然而，低位 LLM 在推理时需要低精度权重与高精度激活的混合精度矩阵乘法（mpGEMM）。现有系统由于缺乏对 mpGEMM 的原生支持，只能将权重反量化为高精度后再计算。这种间接方式会带来显著的推理开销。

本文介绍 T-MAC，一种创新的基于查找表（LUT）的方法，旨在于 CPU 上高效推理低位 LLM（即权重量化的 LLM）。T-MAC 无需反量化即可直接支持 mpGEMM，同时消除了乘法并减少了所需的加法。具体而言，T-MAC 将传统的以数据类型为中心的乘法转化为按位的查表，从而提供统一且可扩展的 mpGEMM 方案。

我们的 LUT 内核随权重位宽线性扩展。在低位 Llama 和 BitNet 模型上的评估显示，与 llama.cpp 相比，T-MAC 的吞吐量最高提升 4 倍，能耗降低 70%。对于 BitNet-b1.58-3B，T-MAC 在 M2-Ultra 上单核可达 30 tokens/s、八核可达 71 tokens/s 的 token 生成吞吐，在树莓派 5 上达到 11 tokens/s。采用基于 LUT 的计算范式，T-MAC 为低位 LLM 在资源受限的边缘设备上的实际部署铺平了道路，且不牺牲计算效率。该系统已在 https://github.com/microsoft/T-MAC 开源。

**英文关键词：** Large Language Models, General Matrix Multiplication, Low-bit Quantization, Computing Algorithms

**中文关键词：** 大语言模型、通用矩阵乘法、低位量化、计算算法

## 代码与研究制品

- 代码：[https://github.com/microsoft/T-MAC](https://github.com/microsoft/T-MAC)

以上链接来自论文现有摘要中的公开资料。

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
