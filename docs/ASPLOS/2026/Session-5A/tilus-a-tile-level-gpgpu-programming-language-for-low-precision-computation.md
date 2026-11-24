---
title: "Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation"
description: "ASPLOS 2026 · Session 5A · Tilus：面向低精度计算的 Tile 级 GPGPU 编程语言"
tags:
  - "ASPLOS2026"
  - "Session 5A"
  - "Generative Model Serving"
---

# Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation

**中文标题：** Tilus：面向低精度计算的 Tile 级 GPGPU 编程语言

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yaoyao Ding (Univerisity of Toronto / CentML), Bohan Hou (Carnegie Mellon University), Xiao Zhang (University of Toronto), Allan Lin (University of Waterloo), Tianqi Chen (Carnegie Mellon University), Cody Yu Hao (Anyscale), Yida Wang (Amazon), Gennady Pekhimenko (Univerisity of Toronto / CentML)

**单位：** Univerisity of Toronto / CentML；Carnegie Mellon University；University of Toronto；University of Waterloo；Anyscale；Amazon

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762219) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Serving Large Language Models (LLMs) is critical for AIpowered applications, yet it demands substantial computational resources, particularly in memory bandwidth and computational throughput. Low-precision computation has emerged as a key technique to improve efficiency while reducing resource consumption. Existing approaches for generating low-precision kernels are limited to weight bit widths that are powers of two and suffer from suboptimal performance because of high-level GPU programming abstractions. These abstractions restrict critical optimizations, such as fine-grained register management and optimized memory access patterns, that are essential for efficient lowprecision computations. In this paper, we introduce Tilus, a domain-specific language designed for General-Purpose GPU (GPGPU) computing that supports low-precision data types with arbitrary bit widths from 1 to 8 while maintaining GPU programmability. Tilus features a thread-block-level programming model, a hierarchical memory space, a novel algebraic layout system, and extensive support for diverse low-precision data types. Tilus programs are compiled into highly efficient GPU programs through automatic vectorization and instruction selection. Extensive experiments demonstrate that Tilus efficiently supports a full spectrum of lowprecision data types, and outperforms state-of-the-art lowprecision kernels. Compared to existing compilers such as Triton and Ladder, as well as hand-optimized kernels such as QuantLLM and Marlin, Tilus achieves performance improvements of: 1.75×, 2.61×, 1.29× and 1.03×, respectively. We open-source Tilus at

## 中文摘要

服务大型语言模型（LLM）对 AI 驱动的应用至关重要，但它需要大量计算资源，尤其是在内存带宽和计算吞吐方面。低精度计算已成为在降低资源消耗的同时提升效率的一项关键技术。现有生成低精度内核的方法局限于 2 的幂的权重位宽，并且由于高层的 GPU 编程抽象而性能欠佳。这些抽象限制了细粒度寄存器管理和优化的内存访问模式等关键优化，而这些优化对于高效的低精度计算至关重要。本文提出 Tilus，这是一种为通用 GPU（GPGPU）计算设计的领域特定语言，支持 1 至 8 的任意位宽的低精度数据类型，同时保持 GPU 可编程性。Tilus 具有线程块级编程模型、分层内存空间、新颖的代数布局系统，以及对多样低精度数据类型的广泛支持。Tilus 程序通过自动向量化和指令选择被编译为高效的 GPU 程序。大量实验表明，Tilus 能够高效支持全谱系的低精度数据类型，并优于最先进的低精度内核。与 Triton 和 Ladder 等现有编译器以及 QuantLLM 和 Marlin 等手工优化内核相比，Tilus 分别实现了 1.75×、2.61×、1.29× 和 1.03× 的性能提升。我们在以下地址开源 Tilus：

## 英文关键词

GPU; programming language; parallel computation; low-precision computation; quantization

## 中文关键词

GPU；编程语言；并行计算；低精度计算；量化

## 代码与研究制品

- [代码仓库](https://github.com/NVIDIA/tilus)
- [研究制品（Zenodo）](https://doi.org/10.5281/zenodo.16756860)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762219)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2026](../index.md)
