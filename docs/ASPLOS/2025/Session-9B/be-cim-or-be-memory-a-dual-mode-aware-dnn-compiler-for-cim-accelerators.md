---
title: "Be CIM or Be Memory: A Dual-mode-aware DNN Compiler for CIM Accelerators"
description: "ASPLOS 2025 · Session 9B · 做 CIM 还是做内存：面向 CIM 加速器的双模式感知 DNN 编译器"
tags:
  - "ASPLOS2025"
  - "Session 9B"
  - "Processing in Memory"
---

# Be CIM or Be Memory: A Dual-mode-aware DNN Compiler for CIM Accelerators

**中文标题：** 做 CIM 还是做内存：面向 CIM 加速器的双模式感知 DNN 编译器

**所属 Session：** [Session 9B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shixin Zhao (Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences), Yuming Li (Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences), Bing Li (Institute of Microelectronics, Chinese Academy of Sciences), Yintao He (Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences), Mengdi Wang (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences), Yinhe Han (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences), Ying Wang (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences)

**单位：** Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences；Institute of Microelectronics, Chinese Academy of Sciences；State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716248) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Computing-in-memory (CIM) architectures demonstrate superior performance over traditional architectures. To unleash the potential of CIM accelerators, many compilation methods have been proposed, focusing on application scheduling optimization specific to CIM. However, existing compilation methods often overlook CIM's capability to switch dynamically between compute and memory modes, which is crucial for accommodating the diverse memory and computational needs of real-world deep neural network architectures, especially the emerging large language models. To fill this gap, we introduce CMSwitch, a novel compiler to optimize resource allocation for CIM accelerators with adaptive modeswitching capabilities, thereby enhancing the performance of DNN applications. Specifically, our approach integrates the compute-memory mode switch into the CIM compilation optimization space by introducing a new hardware abstraction. Then, we propose a novel compilation optimization pass that identifies the optimal network segment and the corresponding mode resource allocations using dynamic programming and mixed-integer programming. CMSwitch uses the tailored meta-operator to express the compilation result in a generalized manner. Evaluation results demonstrate that CMSwitch achieves an average speedup of 1.31× compared to existing SOTA CIM compilation works, highlighting CMSwitch's effectiveness in fully exploiting the potential of CIM processors for a wide range of real-world DNN applications.

## 中文摘要

存内计算（CIM）架构相比传统架构展现出更优越的性能。为释放 CIM 加速器的潜力，已有许多编译方法被提出，它们聚焦于针对 CIM 的应用调度优化。然而，现有编译方法常常忽视 CIM 在计算模式与内存模式之间动态切换的能力，而这种能力对于适配真实世界深度神经网络架构（尤其是新兴的大语言模型）多样化的内存与计算需求至关重要。为填补这一空白，我们提出 CMSwitch，一种新颖的编译器，可针对具备自适应模式切换能力的 CIM 加速器优化资源分配，从而提升 DNN 应用的性能。具体而言，我们的方法通过引入一种新的硬件抽象，将计算—内存模式切换纳入 CIM 编译优化空间。随后，我们提出一种新颖的编译优化 pass，利用动态规划与混合整数规划确定最优的网络分段以及相应的模式资源分配。CMSwitch 使用定制的元算子（meta-operator）以泛化的方式表达编译结果。评估结果表明，与现有最先进的 CIM 编译工作相比，CMSwitch 平均取得 1.31× 的加速，凸显了 CMSwitch 在面向广泛真实 DNN 应用充分挖掘 CIM 处理器潜力方面的有效性。

## 英文关键词

Compute-in-memory (CIM), Compilation, Deep Neural Network (DNN)

## 中文关键词

存内计算（CIM）；编译；深度神经网络（DNN）

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716248)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9B](index.md) · [返回 ASPLOS 2025](../index.md)
