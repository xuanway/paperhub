---
title: "LUT Tensor Core: A Software-Hardware Co-Design for LUT-Based Low-Bit LLM Inference"
description: "ISCA 2025 · Session 4A · LUT Tensor Core: 基于查找表的低比特LLM推理软硬件协同"
tags:
  - "ISCA2025"
  - "Session 4A"
  - "LLMs"
---

# LUT Tensor Core: A Software-Hardware Co-Design for LUT-Based Low-Bit LLM Inference

**中文标题：** LUT Tensor Core: 基于查找表的低比特LLM推理软硬件协同

**所属 Session：** [Session 4A](index.md) · [ISCA 2025](../index.md)

**作者：** Zhiwen Mo, Lei Wang, Jianyu Wei, Zhichen Zeng, Shijie Cao, Lingxiao Ma, Naifeng Jing, Ting Cao, Jilong Xue, Fan Yang, Mao Yang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731057) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Large Language Model (LLM) inference becomes resource-intensive, prompting a shift toward low-bit model weights to reduce the mem- ory footprint and improve efficiency. Such low-bit LLMs necessitate the mixed-precision matrix multiplication (mpGEMM), an impor- tant yet underexplored operation involving the multiplication of lower-precision weights with higher-precision activations. Off-the- shelf hardware does not support this operation natively, leading to indirect, thus inefficient, dequantization-based implementations. In this paper, we study the lookup table (LUT)-based approach for mpGEMM and find that a conventional LUT implementation fails to achieve the promised gains. To unlock the full potential of LUT-based mpGEMM, we propose LUT Tensor Core, a software- hardware co-design for low-bit LLM inference. LUT Tensor Core differentiates itself from conventional LUT designs through: 1) software-based optimizations to minimize table precompute over- head and weight reinterpretation to reduce table storage; 2) a LUT- based Tensor Core hardware design with an elongated tiling shape to maximize table reuse and a bit-serial design to support diverse precision combinations in mpGEMM; 3) a new instruction set and compilation optimizations for LUT-based mpGEMM. LUT Ten- sor Core significantly outperforms existing pure software LUT implementations and achieves a 1.44×improvement in compute density and energy efficiency compared to previous state-of-the-art LUT-based accelerators.

## 中文摘要

大语言模型（LLM）推理对资源消耗巨大，业界开始采用低位宽模型权重，以降低内存占用、提升能效。这类低位宽LLM依赖混合精度矩阵乘法（mpGEMM）。该运算将低精度权重与高精度激活值相乘，是一项重要但研究尚不充分的运算。现有商用硬件并不原生支持该运算，只能基于反量化间接实现，效率低下。本文研究基于查找表（LUT）实现mpGEMM的方案，发现传统LUT实现方式无法兑现预期收益。为充分挖掘LUT型mpGEMM的潜力，本文提出LUT Tensor Core，一种面向低位宽LLM推理的软硬件协同设计方案。LUT Tensor Core相比传统LUT方案有三点创新：1）软件层面优化，降低表预计算开销，通过权重重解释减少查表存储量；2）基于LUT的Tensor Core硬件设计，采用长条分块策略最大化查表复用，配合位串行设计，支持mpGEMM中多种精度组合；3）面向LUT型mpGEMM设计全新指令集与编译优化。LUT Tensor Core显著优于纯软件LUT实现；对比此前最优的LUT加速器，计算密度与能效提升1.44倍。

## 英文关键词

Low-bit LLM, Software-hardware co-design, LUT, Accelerator

## 中文关键词

低位宽大语言模型, 软硬件协同设计, 查找表, 加速器

## 代码与研究制品

- [代码仓库](https://github.com/microsoft/T-MAC/tree/LUTTensorCore_ISCA25)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731057)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2025](../index.md)
