---
title: "HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference"
description: "MICRO 2026 · Session 6C · HBQ：面向精确 LLM 推理、采用硬件效率感知设计的分层缩放块量化"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Quantization"
---

# HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference

**中文标题：** HBQ：面向精确 LLM 推理、采用硬件效率感知设计的分层缩放块量化

**所属 Session：** [Session 6C](index.md) · [MICRO 2026](../index.md)

**作者：** Chun-Ting Chen, Dongmin Han, Hangyeol Mun, Jake Hyun, Arnab Raha, Amit Agarwal, Mark Anders, Mohamed Abdelfattah, Jae-sun Seo

**来源：** MICRO 2026，pp. 2051–2066；[DOI](https://doi.org/10.1109/MICRO67795.2026.00143)

## 英文摘要

Block Quantization (BQ) has emerged as a promising approach for efficient deployment of large language models (LLMs), enabling low-precision computation with controlled accuracy degradation. Compared to scalar weight-only quantization (WoQ), BQ quantizes both weight and activation, offering substantially higher hardware efficiency and enables end-to-end inference on unified datapath, but its design space—spanning bit-width, block size, scaling, and numeric formats—remains underexplored in prior works. We provide extensive hardware/benchmark results and guidelines for hardware designers through design space exploration (DSE). Particularly, we identify that increasing block size is critical for improving hardware efficiency by amortizing dequantization and accumulation costs, but degrades accuracy significantly. This trade-off fundamentally limits the efficiency of conventional BQ methods. Motivated by this insight, we propose Hierarchical Block Quantization (HBQ). Unlike prior hierarchical quantization methods[1], [2], which adopt relatively small block sizes and conventional Power-of-Two (PoT) or integer-based scaling, HBQ uses large blocks to maximize efficiency and introduces a novel low-overhead significand (SIG) scaling for second level quantization. By allocating quantization levels more effectively and accounting for the distinct characteristics of activation and weight distributions, SIG scaling compensates for the additional error introduced by large blocks more effectively than prior PoT and INT schemes. The proposed HBQ-A (accurate) configuration achieves W4A16-level accuracy using only a W4A5 setting while requiring less silicon area than NVFP4. HBQ-E (efficient) further reduces hardware cost by 17% while maintaining higher accuracy than all existing BQ methods. We implemented a 28nm ASIC accelerator which applied HBQ on weight, activation, and KV cache, and also integrated a novel partial sum BQ scheme to further reduce EMA energy. Compared to state-of-the-art WoQ, HBQ delivers 2.3x/4.6x higher area/energy efficiency at the same accuracy level; 1.6-3.3x system energy reduction and 1.5-3.0 speedup over prior BQ methods while providing best accuracy. Our implementation is publicly available at: https://github.com/SeoLabCornell/HBQ.git.

## 中文摘要

块量化 (BQ) 已成为高效部署大语言模型 (LLM) 的一种有前途的方法，可实现低精度计算并控制精度下降。与纯标量权重量化 (WoQ) 相比，BQ 对权重和激活进行量化，提供了更高的硬件效率，并支持统一数据路径上的端到端推理，但其设计空间（涵盖位宽、块大小、缩放和数字格式）在之前的工作中仍未得到充分探索。我们通过设计空间探索 (DSE) 为硬件设计人员提供广泛的硬件/基准测试结果和指南。特别是，我们发现增加块大小对于通过分摊反量化和累积成本来提高硬件效率至关重要，但会显着降低准确性。这种权衡从根本上限制了传统 BQ 方法的效率。受这种见解的启发，我们提出了分层块量化（HBQ）。与采用相对较小的块大小和传统的二次幂 (PoT) 或基于整数的缩放的先前分层量化方法 [1]、[2] 不同，HBQ 使用大块来最大限度地提高效率，并为二级量化引入了一种新颖的低开销有效数 (SIG) 缩放。通过更有效地分配量化级别并考虑激活和权重分布的独特特征，SIG 缩放比之前的 PoT 和 INT 方案更有效地补偿大块引入的额外误差。所提出的 HBQ-A（精确）配置仅使用 W4A5 设置即可实现 W4A16 级精度，同时所需的硅面积比 NVFP4 更少。 HBQ-E（高效）进一步降低了 17% 的硬件成本，同时保持比所有现有 BQ 方法更高的精度。我们实现了一个 28nm ASIC 加速器，该加速器在权重、激活和 KV 缓存上应用了 HBQ，并且还集成了一种新颖的部分和 BQ 方案以进一步降低 EMA 能量。与最先进的 WoQ 相比，HBQ 在相同精度水平下的面积/能效提高了 2.3 倍/4.6 倍；与之前的 BQ 方法相比，系统能耗降低了 1.6-3.3 倍，加速提高了 1.5-3.0 倍，同时提供了最佳精度。我们的实现公开在：https://github.com/SeoLabCornell/HBQ.git。

## 中文关键词

量化；硬件加速器；大语言模型推理；层次化缩放；分块量化

## 代码与研究制品

- 代码仓库：[https://github.com/SeoLabCornell/HBQ](https://github.com/SeoLabCornell/HBQ)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6C](index.md) · [MICRO 2026 主页](../index.md)
