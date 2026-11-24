---
title: "KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta"
description: "ISCA 2026 · Session 4B · KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta"
tags:
  - "ISCA2026"
  - "Session 4B"
  - "Industry Track 1"
---

# KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta

**中文标题：** KernelEvolve: 面向 Meta 异构 AI 加速器的大规模智能体内核编码

**所属 Session：** [Session 4B](index.md) · [ISCA 2026](../index.md)

**作者：** Gang Liao, Hongsen Qin, Ying Wang, Alicia Golden, Michael Kuchnik, Yavuz Yetim, Ruichao Xiao, Jia Jiunn Ang, Chunli Fu, Yihan He, Samuel Hsia, Zewei Jiang, Roman Levenstein, Dianshi Li, Liyuan Li, Ajit Mathews, Varna Puvvada, Feng Shi, Nathan Yan, Xiayu Yu, Uladzimir Pashkevich, Matt Steiner, Carole-Jean Wu, Gaoxiang Liu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Making deep learning recommendation model (DLRM) inference fast and efficient is important. However, this presents three key system challenges – model architecture diversity, kernel primitive diversity, and hardware generation and architecture heterogeneity. The combination of the three diversity dimensions leads to a complex optimization space for fast, efficient inference at-scale. This paper presents KernelEvolve– an agentic kernel coding framework – to tackle heterogeneity at-scale for DLRM training and inference. KernelEvolve is designed to take kernel specifications as input and automate the process of kernel generation and optimization for recommendation model across heterogeneous hardware architectures. KernelEvolve does so by operating at multiple programming abstractions, from Triton and CuTe DSL to low-level hardware agnostic languages, spanning the full hardware-software optimization stack. The kernel optimization process is described as graph-based search with selection policy, universal operator, fitness function, and termination rule, dynamically adapts to runtime execution context through retrieval-augmented prompt synthesis. We designed, implemented, and deployed KernelEvolve to optimize a wide variety of production recommendation models across generations of NVIDIA and AMD GPUs, as well as Meta’s AI accelerators. We validate KernelEvolve on the publicly-available KernelBench suite, achieving 100% pass rate on all 250 problems across three difficulty levels, and 160 PyTorch ATen operators across three heterogeneous hardware platforms, demonstrating 100% correctness. KernelEvolve reduces development time from weeks to hours and achieves substantial performance improvements over PyTorch baselines across diverse production use cases and for heterogeneous AI systems at-scale. Beyond performance efficiency improvements, KernelEvolve significantly mitigates the programmability barrier for new AI hardware by enabling automated kernel generation for in-house developed AI hardware.


## 中文摘要

深度推荐模型（DLRM）推理的高效性面临模型架构多样性、内核原语多样性和硬件代际异构性三大挑战。本文提出 KernelEvolve——一种智能体内核编码框架——以应对大规模异构性挑战。KernelEvolve 接收内核规格作为输入，自动化跨异构硬件架构的内核生成与优化过程，在 Triton、CuTe DSL 到低级硬件无关语言的多种编程抽象上运行。通过基于图的搜索与选择策略、通用算子、适应度函数和终止规则，结合检索增强的提示合成动态适应运行时执行上下文。KernelEvolve 在公开 KernelBench 套件上 250 个问题中达到 100% 通过率，将开发时间从数周缩短至数小时，并显著降低新 AI 硬件的可编程性障碍。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4B](index.md) · [返回 ISCA 2026](../index.md)
