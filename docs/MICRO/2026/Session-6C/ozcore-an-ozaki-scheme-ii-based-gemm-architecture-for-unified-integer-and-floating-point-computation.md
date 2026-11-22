---
title: "OzCore: An Ozaki-Scheme-II-Based GEMM Architecture for Unified Integer and Floating-Point Computation"
description: "MICRO 2026 · Session 6C · OzCore：基于 Ozaki-Scheme-II、统一整数与浮点计算的 GEMM 架构"
tags:
  - "MICRO2026"
---

# OzCore: An Ozaki-Scheme-II-Based GEMM Architecture for Unified Integer and Floating-Point Computation

**中文标题：** OzCore：基于 Ozaki-Scheme-II、统一整数与浮点计算的 GEMM 架构

**所属 Session：** [Session 6C](index.md) · [MICRO 2026](../index.md)

**作者：** Jihoon Park, Junhee Lee, Howon Lee, Jinsu Kim, Jinseok Kim, Jae-Joon Kim

**来源：** MICRO 2026，pp. 2101–2116；[DOI](https://doi.org/10.1109/MICRO67795.2026.00146)

## 英文摘要

Modern large language model (LLM) accelerators must support a wide spectrum of numerical precisions, ranging from integer to multiple floating-point formats (FP8, FP16, BF16, FP32). Existing architectures address this requirement through datapath fusion, embedding multiple numerical formats into a single compute unit, which leads to substantial hardware overhead and reduced compute density. Alternatively, domain-specific NPUs often specialize in a single datatype, limiting flexibility and interoperability. In this work, we present OzCore, a general matrix multiplication (GEMM) architecture that enables unified integer and floating-point computation on a single INT8 compute fabric. Building on the mathematical foundation of Ozaki Scheme-II, OzCore reinterprets floating-point computation as a parallel decomposition across independent residue domains, allowing diverse numerical precisions to be supported without format-specific datapaths. By expressing precision as a controllable degree of parallel decomposition, OzCore transforms accuracy scaling into a form of structured parallelism. To realize this design, OzCore introduces a fully integer-only pipeline that eliminates all floating-point operations from preprocessing, modular reduction, and reconstruction, along with a tight scaling scheme that maximizes effective precision per residue domain. A tunable split count s controls the degree of decomposition, enabling a flexible trade-off between numerical accuracy and parallel execution. Our evaluation shows that OzCore augments a baseline INT8 GEMM unit with only 27.9% area overhead, while achieving 1.91 times higher TOPS/mm^2 and 1.40 times higher TOPS/W than a fused multi-format baseline at iso-accuracy. OzCore matches BF16 perplexity on LLaMA-3.1 8B and 70B at s = 3, and maintains stable per-layer numerical error comparable to BF16 across all layers at s >= 4. OzCore extends the Ozaki Scheme-II into the architectural domain, enabling integer-centric compute fabrics to natively support diverse numerical precisions through parallel decomposition, and offering a scalable and hardware-efficient alternative to datapath fusion for future AI accelerators.

## 中文摘要

现代大语言模型 (LLM) 加速器必须支持广泛的数值精度，范围从整数到多种浮点格式（FP8、FP16、BF16、FP32）。现有架构通过数据路径融合来满足这一要求，将多种数字格式嵌入到单个计算单元中，这会导致大量的硬件开销并降低计算密度。另外，特定领域的 NPU 通常专注于单一数据类型，从而限制了灵活性和互操作性。在这项工作中，我们提出了 OzCore，这是一种通用矩阵乘法 (GEMM) 架构，可在单个 INT8 计算结构上实现统一的整数和浮点计算。 OzCore 以 Ozaki Scheme-II 的数学基础为基础，将浮点计算重新解释为跨独立残差域的并行分解，从而无需特定于格式的数据路径即可支持不同的数值精度。通过将精度表示为并行分解的可控程度，OzCore 将精度缩放转换为结构化并行的形式。为了实现这一设计，OzCore 引入了一个完全纯整数的管道，该管道消除了预处理、模块化缩减和重构中的所有浮点运算，以及一个严格的缩放方案，可最大限度地提高每个残差域的有效精度。可调分割计数控制分解程度，从而实现数值精度和并行执行之间的灵活权衡。我们的评估表明，OzCore 仅以 27.9% 的面积开销增强了基线 INT8 GEMM 单元，同时在等精度下实现了比融合多格式基线高 1.91 倍的 TOPS/mm^2 和 1.40 倍的 TOPS/W。 OzCore 在 s = 3 时与 LLaMA-3.1 8B 和 70B 上的 BF16 困惑度相匹配，并在 s >= 4 时在所有层上保持与 BF16 相当的稳定的每层数值误差。OzCore 将 Ozaki 方案 II 扩展到架构领域，使以整数为中心的计算结构能够通过并行分解原生支持不同的数值精度，并为未来 AI 加速器的数据路径融合提供可扩展且硬件高效的替代方案。

## 中文关键词

大语言模型；浮点仿真；通用矩阵乘法；硬件加速器；Ozaki 分解

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21541963](https://doi.org/10.5281/zenodo.21541963)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6C](index.md) · [MICRO 2026 主页](../index.md)
