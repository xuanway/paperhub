---
title: "Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction"
description: "ASPLOS 2025 · Session 7B · Micro Blossom：面向量子纠错的最小权重完美匹配加速解码"
tags:
  - "ASPLOS2025"
  - "Session 7B"
  - "Quantum Error Correction"
---

# Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction

**中文标题：** Micro Blossom：面向量子纠错的最小权重完美匹配加速解码

**所属 Session：** [Session 7B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yue Wu (Yale University), Namitha Liyanage (Yale University), Lin Zhong (Yale University)

**单位：** Yale University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716005) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Minimum-Weight Perfect Matching (MWPM) decoding is important to quantum error correction decoding because of its accuracy. However, many believe that it is difficult, if possible at all, to achieve the microsecond latency requirement posed by superconducting qubits. This work presents the first publicly known MWPM decoder, called Micro Blossom, that achieves sub-microsecond decoding latency. Micro Blossom employs a heterogeneous architecture that carefully partitions a state-of-the-art MWPM decoder between software and a programmable accelerator with parallel processing units, one of each vertex/edge of the decoding graph. On a surface code with code distance 𝑑and a circuit-level noise model with physical error rate 𝑝, Micro Blossom's accelerator employs 𝑂(𝑑3) parallel processing units to reduce the worst-case latency from 𝑂(𝑑12) to 𝑂(𝑑9) and reduce the average latency from 𝑂(𝑝𝑑3 + 1) to 𝑂(𝑝2𝑑2 + 1) when 𝑝≪1. We report a prototype implementation of Micro Blossom using FPGA. Measured at 𝑑= 13 and 𝑝= 0.1%, the prototype achieves an average decoding latency of 0.8 𝜇s at a moderate clock frequency of 62 MHz. Micro Blossom is the first publicly known hardware-accelerated exact MWPM decoder, and the decoding latency of 0.8 𝜇s is 8 times shorter than the best latency of MWPM decoder implementations reported in the literature.

## 中文摘要

最小权重完美匹配（MWPM）解码因其准确性而对量子纠错解码十分重要。然而，许多人认为，要满足超导量子比特所提出的微秒级时延要求，即使可能也十分困难。本工作提出了首个公开已知的、可实现亚微秒解码时延的 MWPM 解码器，称为 Micro Blossom。Micro Blossom 采用异构架构，将一个最先进的 MWPM 解码器谨慎地划分到软件与一个带有并行处理单元的可编程加速器之间，解码图的每个顶点/边对应一个处理单元。在码距为 𝑑 的表面码以及物理错误率为 𝑝 的电路级噪声模型下，Micro Blossom 的加速器采用 𝑂(𝑑3) 个并行处理单元，将最坏情况时延从 𝑂(𝑑12) 降低到 𝑂(𝑑9)，并在 𝑝≪1 时将平均时延从 𝑂(𝑝𝑑3 + 1) 降低到 𝑂(𝑝2𝑑2 + 1)。我们报告了使用 FPGA 的 Micro Blossom 原型实现。在 𝑑= 13 与 𝑝= 0.1% 下测得，该原型在 62 MHz 的中等时钟频率下实现了 0.8 𝜇s 的平均解码时延。Micro Blossom 是首个公开已知的硬件加速精确 MWPM 解码器，其 0.8 𝜇s 的解码时延比文献中报道的 MWPM 解码器实现的最佳时延短 8 倍。

## 英文关键词

Minimum-Weight Perfect Matching (MWPM) Decoder, Quantum Error Correction, Heterogeneous Architecture

## 中文关键词

最小权重完美匹配（MWPM）解码器；量子纠错；异构架构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716005)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7B](index.md) · [返回 ASPLOS 2025](../index.md)
