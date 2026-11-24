---
title: "Lobster: A GPU-Accelerated Framework for Neurosymbolic Programming"
description: "ASPLOS 2026 · Session 8A · Lobster：面向神经符号编程的 GPU 加速框架"
tags:
  - "ASPLOS2026"
  - "Session 8A"
  - "GPU Programming"
---

# Lobster: A GPU-Accelerated Framework for Neurosymbolic Programming

**中文标题：** Lobster：面向神经符号编程的 GPU 加速框架

**所属 Session：** [Session 8A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Paul Biberstein (University of Pennsylvania), Ziyang Li (University of Pennsylvania), Joseph Devietti (University of Pennsylvania), Mayur Naik (University of Pennsylvania)

**单位：** University of Pennsylvania

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762232) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Neurosymbolic programs combine deep learning with symbolic reasoning to achieve better data efficiency, interpretability, and generalizability compared to standalone deep learning approaches. However, existing neurosymbolic learning frameworks implement an uneasy marriage between a highly scalable, GPU-accelerated neural component and a slower symbolic component that runs on CPUs. We propose Lobster, a unified framework for harnessing GPUs in an end-to-end manner for neurosymbolic learning. Lobster maps a general neurosymbolic language based on Datalog to the GPU programming paradigm. This mapping is implemented via compilation to a new intermediate language called APM. The extra abstraction provided by apm allows Lobster to be both flexible, supporting discrete, probabilistic, and differentiable modes of reasoning on GPU hardware with a library of provenance semirings, and performant, implementing new optimization passes. We demonstrate that Lobster programs can solve interesting problems spanning the domains of natural language processing, image processing, program reasoning, bioinformatics, and planning. On a suite of 9 applications, Lobster achieves an average speedup of 3.9x over Scallop, a state-of-the-art neurosymbolic framework, and enables scaling of neurosymbolic solutions to previously infeasible tasks.

## 中文摘要

神经符号程序将深度学习与符号推理相结合，相比独立的深度学习方法，可获得更好的数据效率、可解释性和泛化能力。然而，现有的神经符号学习框架所实现的，是将高度可扩展、GPU 加速的神经组件与运行在 CPU 上较慢的符号组件之间一种并不稳固的结合。我们提出 Lobster，一个以端到端方式利用 GPU 进行神经符号学习的统一框架。Lobster 将一种基于 Datalog 的通用神经符号语言映射到 GPU 编程范式。该映射通过编译到一种名为 APM 的新中间语言来实现。APM 提供的额外抽象使 Lobster 兼具灵活性——借助 provenance semiring 库在 GPU 硬件上支持离散、概率与可微推理模式——和高性能，可实现新的优化遍。我们证明 Lobster 程序能够求解横跨自然语言处理、图像处理、程序推理、生物信息学和规划等领域的有趣问题。在 9 个应用组成的测试集上，Lobster 相比最先进的神经符号框架 Scallop 取得平均 3.9 倍的加速，并使神经符号方案得以扩展到此前不可行的任务。

## 英文关键词

neurosymbolic programming, GPU acceleration, Datalog, compiler optimizations

## 中文关键词

神经符号编程；GPU 加速；Datalog；编译器优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762232)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8A](index.md) · [返回 ASPLOS 2026](../index.md)
