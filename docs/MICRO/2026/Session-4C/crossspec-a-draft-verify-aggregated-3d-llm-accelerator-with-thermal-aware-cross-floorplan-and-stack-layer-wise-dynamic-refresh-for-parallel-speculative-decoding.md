---
title: "CrossSpec: A Draft-Verify Aggregated 3D LLM Accelerator with Thermal-Aware Cross Floorplan and Stack-Layer-Wise Dynamic Refresh for Parallel Speculative Decoding"
description: "MICRO 2026 · Session 4C · CrossSpec：面向并行推测解码、融合草拟与验证并采用热感知交叉布局及逐堆叠层动态刷新的三维 LLM 加速器"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Thermal Management"
---

# CrossSpec: A Draft-Verify Aggregated 3D LLM Accelerator with Thermal-Aware Cross Floorplan and Stack-Layer-Wise Dynamic Refresh for Parallel Speculative Decoding

**中文标题：** CrossSpec：面向并行推测解码、融合草拟与验证并采用热感知交叉布局及逐堆叠层动态刷新的三维 LLM 加速器

**所属 Session：** [Session 4C](index.md) · [MICRO 2026](../index.md)

**作者：** Yutong Su, Huanyu Wang, Ruikang Guo, Mengfei Shen, Huiming Han, Yang Wang, Yang Hu, Shouyi Yin

**来源：** MICRO 2026，pp. 1529–1543；[DOI](https://doi.org/10.1109/MICRO67795.2026.00112)

## 英文摘要

Parallel speculative decoding (PSD) breaks the mutual waiting between drafting and verification and thus provides a promising path to accelerate LLM inference. However, PSD remains fundamentally memory-bound on conventional 2.5D GPU/XPU platforms, especially in low-batch edge scenarios. Emerging 3D hybrid-bonding system (3D HB) offers a compelling substrate for PSD with much higher memory bandwidth, but naively deploying PSD on 3D HB is inefficient. Specifically, 3D-PSD suffers from dual-region resource under-utilization, severe vertical thermal coupling, and inefficient DRAM refresh overhead. To address these challenges, we propose CrossSpec, a system-architecture co-design accelerator for 3D-PSD. At the scheduling level, we propose a communication-aware D-V aggregation paradigm that co-executes draft and verify within each SD macro-tile to improve resource utilization. At the architecture level, we propose a thermal-cross microarchitecture that partitions each tile into D-Zone and V-Zone to match the asymmetric resource demands of draft and verify while addressing the issue of vertical thermal coupling. At the system level, we design a thermal-graded refresh and memory management system that jointly considers the error-tolerance heterogeneity of PSD data and the vertical thermal gradient in 3D DRAM, thereby addressing inefficient DRAM refresh and reducing power consumption. Extensive experiments show that CrossSpec achieves up to 2.34x speedup and 1.43x higher energy efficiency over baseline 3D-PSD accelerator, and up to 22.38x speedup and 9.47x higher energy efficiency over GPU baseline.

## 中文摘要

并行推测解码（PSD）打破了起草和验证之间的相互等待，从而为加速LLM推理提供了一条有希望的途径。然而，PSD 在传统 2.5D GPU/XPU 平台上基本上仍然受内存限制，尤其是在低批量边缘场景中。新兴的 3D 混合键合系统 (3D HB) 为具有更高内存带宽的 PSD 提供了引人注目的基材，但在 3D HB 上简单地部署 PSD 效率很低。具体来说，3D-PSD面临双区资源利用不足、垂直热耦合严重以及DRAM刷新开销低效等问题。为了应对这些挑战，我们提出了 CrossSpec，一种 3D-PSD 的系统架构协同设计加速器。在调度级别，我们提出了一种通信感知的 D-V 聚合范例，该范例在每个 SD 宏块内共同执行草稿和验证，以提高资源利用率。在架构层面，我们提出了一种热交叉微架构，将每个块划分为 D 区和 V 区，以满足草稿和验证的不对称资源需求，同时解决垂直热耦合问题。在系统层面，我们设计了热分级刷新和内存管理系统，共同考虑PSD数据的容错异构性和3D DRAM中的垂直热梯度，从而解决低效的DRAM刷新问题并降低功耗。大量实验表明，与基准 3D-PSD 加速器相比，CrossSpec 的加速速度提高了 2.34 倍，能效提高了 1.43 倍；与 GPU 基准加速器相比，加速速度提高了 22.38 倍，能效提高了 9.47 倍。

## 中文关键词

三维混合键合；并行推测解码；近存处理；热感知布局；动态刷新

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4C](index.md) · [MICRO 2026 主页](../index.md)
