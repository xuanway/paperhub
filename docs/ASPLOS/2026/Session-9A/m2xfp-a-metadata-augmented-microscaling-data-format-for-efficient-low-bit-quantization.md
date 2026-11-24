---
title: "M2XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization"
description: "ASPLOS 2026 · Session 9A · M2XFP：一种面向高效低比特量化的元数据增强微缩放数据格式"
tags:
  - "ASPLOS2026"
  - "Session 9A"
  - "Systems Profiling & Optimization"
---

# M2XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization

**中文标题：** M2XFP：一种面向高效低比特量化的元数据增强微缩放数据格式

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Weiming Hu (Shanghai Jiao Tong University), Zihan Zhang (Shanghai Jiao Tong University), Haoyan Zhang (Shanghai Jiao Tong University), Chen Zhang (Shanghai Jiao Tong University), Cong Guo (Shanghai Jiao Tong University), Yu Feng (Shanghai Jiao Tong University), Tianchi Hu (Computing Product Line, Huawei), Guanglin Li (Computing Product Line, Huawei), Guipeng Hu (Computing Product Line, Huawei), Junsong Wang (Computing Product Line, Huawei), Jingwen Leng (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University；Computing Product Line, Huawei

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790185) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Existing low-bit Microscaling (MX) formats, such as MXFP4, often suffer from substantial accuracy degradation due to the use of a shared scaling factor with the Power-of-Two format. In this work, we explore strategies that introduce minimal metadata to recover accuracy lost during quantization while maintaining high bit efficiency across a wide range of large language models. We propose a complete algorithm-hardware co-design based on flexible metadata, featuring an online quantization with simple encoding. To support the proposed method efficiently, we implement a lightweight hardware unit and integrate it into the accelerator. Evaluation results demonstrate that our method substantially narrows the accuracy gap, achieving on average a 70.63% reduction in accuracy loss compared to MXFP4 and a 37.30% reduction relative to the latest NVFP4 on LLM benchmarks. Furthermore, our design delivers up to 1.91× speedup and 1.75× energy savings over state-of-the-art accelerators.

## 中文摘要

已有的低比特微缩放（MX）格式（如 MXFP4）由于采用 2 的幂（Power-of-Two）格式的共享缩放因子，往往会出现显著的精度下降。本文探索引入最少元数据的策略，以恢复量化过程中损失的精度，同时在一系列广泛的大语言模型上保持高比特效率。我们提出一种基于灵活元数据的完整算法—硬件协同设计，其特点是采用简单编码的在线量化。为高效支持所提出的方法，我们实现了一个轻量级硬件单元并将其集成到加速器中。评估结果表明，我们的方法大幅缩小了精度差距：在 LLM 基准测试上，相比 MXFP4 平均降低精度损失 70.63%，相比最新的 NVFP4 降低 37.30%。此外，与当前最优加速器相比，我们的设计最高带来 1.91× 的加速和 1.75× 的能耗节省。

## 英文关键词

Low-bit Quantization; Microscaling Data Formats; Hardware Acceleration

## 中文关键词

低比特量化；微缩放数据格式；硬件加速

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790185)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2026](../index.md)
