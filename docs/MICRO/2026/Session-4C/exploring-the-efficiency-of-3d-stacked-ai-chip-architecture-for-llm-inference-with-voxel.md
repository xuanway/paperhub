---
title: "Exploring the Efficiency of 3D-Stacked AI Chip Architecture for LLM Inference with VOXEL"
description: "MICRO 2026 · Session 4C · 利用 VOXEL 探索三维堆叠 AI 芯片架构的 LLM 推理效率"
tags:
  - "MICRO2026"
  - "LLM Inference"
---

# Exploring the Efficiency of 3D-Stacked AI Chip Architecture for LLM Inference with VOXEL

**中文标题：** 利用 VOXEL 探索三维堆叠 AI 芯片架构的 LLM 推理效率

**所属 Session：** [Session 4C](index.md) · [MICRO 2026](../index.md)

**作者：** Yiqi Liu, Noelle Crawford, Michael Wang, Jilong Xue, Jian Huang

**来源：** MICRO 2026，pp. 1474–1491；[DOI](https://doi.org/10.1109/MICRO67795.2026.00109)

## 英文摘要

To overcome the well-known memory bottleneck of AI chips, 3D-stacked architectures that employ advanced packaging technology with high-density through-silicon vias (TSVs) pins have proven to be a promising solution. The 3D-stacked AI chip enables ultra-high memory bandwidth between compute and memory by stacking numerous DRAM banks atop many AI cores in a distributed manner. However, it is not easy to explore the efficiency of the 3D-stacked AI chip, due to its unique distributed nature. And we need to carefully consider multiple intertwined factors that range from upper-level computing paradigm to machine learning (ML) compiler optimizations, and to the underlying hardware architecture. In this paper, we develop VOXEL, a fast and compiler-aware end-to-end simulation framework to facilitate exploring the efficiency of 3D-stacked AI chips for large language model (LLM) inference. VOXEL enables the software/hardware co-exploration by employing a programming interface that allows ML compilers to customize the model execution plans. After validating the results of VOXEL with an emulator on real silicon, we thoroughly examine the impact and correlation of different aspects of 3D-stacked AI chips, including state-of-the-art compute paradigms, tile-to-core mapping, tensor-to-bank mapping, NoC topologies and link bandwidth, DRAM bank bandwidth, per-core SRAM capacity, and energy/thermal constraints. Our findings disclose that the end-to-end efficiency of a 3D stacked AI chip not only is determined by the cooperative function of these factors, but also significantly depends on the mappings from tiles to AI core and DRAM banks. We report our findings in the paper, expecting that they will shed light on the development of 3D-stacked AI chip ecosystem. We open source VOXEL for public research.

## 中文摘要

为了克服 AI 芯片众所周知的内存瓶颈，采用先进封装技术和高密度硅通孔 (TSV) 引脚的 3D 堆叠架构已被证明是一种有前途的解决方案。 3D 堆叠 AI 芯片通过在许多 AI 核心之上以分布式方式堆叠大量 DRAM 组，实现计算和内存之间的超高内存带宽。然而，由于其独特的分布式特性，探索3D堆叠AI芯片的效率并不容易。我们需要仔细考虑多个相互交织的因素，从上层计算范例到机器学习（ML）编译器优化，再到底层硬件架构。在本文中，我们开发了 VOXEL，这是一种快速且具有编译器感知能力的端到端仿真框架，有助于探索 3D 堆叠 AI 芯片在大语言模型 (LLM) 推理方面的效率。 VOXEL 通过采用允许 ML 编译器自定义模型执行计划的编程接口来实现软件/硬件协同探索。在真实芯片上使用仿真器验证 VOXEL 的结果后，我们彻底检查了 3D 堆叠 AI 芯片不同方面的影响和相关性，包括最先进的计算范例、块到核心映射、张量到组映射、NoC 拓扑和链路带宽、DRAM 组带宽、每核 SRAM 容量以及能量/热约束。我们的研究结果表明，3D 堆叠式 AI 芯片的端到端效率不仅取决于这些因素的协同作用，而且很大程度上取决于从 Tile 到 AI 核心和 DRAM Bank 的映射。我们在论文中报告了我们的发现，期望它们能够为 3D 堆叠 AI 芯片生态系统的发展提供启示。我们开源 VOXEL 供公共研究。

## 中文关键词

三维堆叠 DRAM；大语言模型加速器；仿真；软硬件协同探索

## 代码与研究制品

- 代码仓库：[https://github.com/yiqiliu2/voxelsim](https://github.com/yiqiliu2/voxelsim)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21433909](https://doi.org/10.5281/zenodo.21433909)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 4C](index.md) · [MICRO 2026 主页](../index.md)
