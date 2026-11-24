---
title: "Linear Layouts: Robust Code Generation of Efficient Tensor Computation Using F2"
description: "ASPLOS 2026 · Session 4B · Linear Layouts：使用 F2 实现高效张量计算的健壮代码生成"
tags:
  - "ASPLOS2026"
  - "Session 4B"
  - "ML Compilers & Tensor Programs"
---

# Linear Layouts: Robust Code Generation of Efficient Tensor Computation Using F2

**中文标题：** Linear Layouts：使用 F2 实现高效张量计算的健壮代码生成

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Keren Zhou (George Mason University and OpenAI), Mario Lezcano (OpenAI), Adam Goucher (OpenAI), Akhmed Rakhmati (OpenAI), Jeff Niu (OpenAI), Justin Lebar (OpenAI), Pawel Szczerbuk (OpenAI), Peter Bell (OpenAI), Phil Tillet (OpenAI), Thomas Raoux (OpenAI), Zahi Moudallal (OpenAI)

**单位：** George Mason University and OpenAI；OpenAI

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762221) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Efficient tensor computation is a cornerstone of modern deep learning (DL) workloads, yet existing approaches struggle to achieve flexible and performant design and implementation of tensor layouts—mappings between logical tensors and hardware resources. The increasing complexity of DL algorithms and hardware demands a generic and systematic approach to handling tensor layouts. In this work, we introduce Linear Layouts, a novel approach that models tensor layouts using linear algebra over F2. By representing tensor layouts as binary matrices acting on the bits of the hardware representation, our approach enables a generic layout definition—as opposed to the classical case-by-case approach—and allows for generic layout-to-layout conversions, eliminating the quadratic explosion that plagues existing solutions. We integrate linear layouts with Triton and demonstrate their effectiveness in optimizing individual Triton operators as well as kernels written in Triton. We also show that linear layouts reduce engineering effort in the compiler backend while fixing several bugs in Triton's legacy layout system.

## 中文摘要

高效张量计算是现代深度学习（DL）工作负载的基石，然而现有方法难以灵活且高性能地设计与实现张量布局——即逻辑张量与硬件资源之间的映射。DL 算法与硬件日益增长的复杂性要求一种通用且系统化的方法来处理张量布局。本文提出 Linear Layouts，这是一种使用 F2 上的线性代数对张量布局进行建模的新颖方法。通过将张量布局表示为作用于硬件表示各个位的二进制矩阵，我们的方法实现了通用的布局定义——而非经典的一例一议方式——并支持通用的布局间转换，消除了困扰现有方案的二次爆炸问题。我们将线性布局与 Triton 集成，并展示了其在优化单个 Triton 算子以及用 Triton 编写的内核方面的有效性。我们还表明，线性布局减少了编译器后端的工程投入，同时修复了 Triton 旧版布局系统中的若干缺陷。

## 英文关键词

GPU, Linear Algebra, Triton, Tensor Layouts, Deep Learning

## 中文关键词

GPU；线性代数；Triton；张量布局；深度学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762221)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2026](../index.md)
