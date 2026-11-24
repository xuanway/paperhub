---
title: "SMOOTH: Hardware-Assisted Fine-Grained On-Chip Memory Management for Efficient On-Device LLM Inference"
description: "ISCA 2026 · Session 4A · SMOOTH: Hardware-Assisted Fine-Grained On-Chip Memory Management for Efficient On-Device LLM Inference"
tags:
  - "ISCA2026"
  - "Session 4A"
  - "LLM 2"
---

# SMOOTH: Hardware-Assisted Fine-Grained On-Chip Memory Management for Efficient On-Device LLM Inference

**中文标题：** SMOOTH: 面向高效端侧 LLM 推理的硬件辅助细粒度片上内存管理

**所属 Session：** [Session 4A](index.md) · [ISCA 2026](../index.md)

**作者：** Seulki Kim, Bokyeong Kim, Kyeonghyeon Ryu, Yeji Jung, Hwanjun Lee, Sungju Kim, Yunhyeong Jeon, Daehoon Kim

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The growing demand for running large language models (LLMs) directly on mobile devices has intensified the need for efficient on-device inference under stringent memory and bandwidth constraints. While compiler-level optimizations such as memory tiling and lifetime-based allocation improve on-chip SRAM utilization, they remain ineffective in addressing bursty memory traffic and fragmentation arising from the alternating compute- and I/O-bound phases of autoregressive decoding. This paper proposes SMOOTH, a hardware-assisted on-chip memory management framework that dynamically optimizes scratchpad usage at runtime. First, a fine-grained, block-based allocation and preloading scheme improves effective SRAM utilization and exploits idle memory bandwidth. Second, a hardware-driven early reclamation mechanism leverages buffer-level signals to promptly release unused memory blocks, enabling more aggressive and timely preloading. We implement SMOOTH in Verilog and integrate it into LLMCompass, an LLM-optimized extension of ScaleSim, for cycle-accurate evaluation. Experimental results demonstrate that SMOOTH reduces Time-to-First-Token (TTFT) by up to 59.2% and Time-to-Last-Token (TTLT) by up to 73.0% compared to prior baseline approaches on memory-constrained mobile SoCs, achieving average energy reductions of up to 51.2% compared to state-of-the-art baselines.

## 中文摘要

在移动设备上直接运行大语言模型（LLM）的需求日益增长，对严格内存和带宽约束下的高效设备端推理提出了更高要求。本文提出SMOOTH，一种硬件辅助的片上内存管理框架，在运行时动态优化暂存器使用。该框架采用细粒度、基于块的分配和预加载方案提升SRAM利用率，并利用硬件驱动的早期回收机制及时释放未使用的内存块以实现更积极的预加载。实验结果表明，在内存受限的移动SoC上，SMOOTH相比先前基线方法将首Token延迟（TTFT）降低最高59.2%，末Token延迟（TTLT）降低最高73.0%，相比最先进基线平均能效提升最高51.2%。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：skkim-caslab/SMOOTH](https://github.com/skkim-caslab/SMOOTH)
- [实验材料归档（Zenodo 20020344）](https://zenodo.org/records/20020344)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2026](../index.md)
