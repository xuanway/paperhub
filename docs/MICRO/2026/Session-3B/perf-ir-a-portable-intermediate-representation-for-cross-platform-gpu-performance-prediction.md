---
title: "Perf-IR: A Portable Intermediate Representation for Cross-Platform GPU Performance Prediction"
description: "MICRO 2026 · Session 3B · Perf-IR：面向跨平台 GPU 性能预测的可移植中间表示"
tags:
  - "MICRO2026"
  - "GPU"
---

# Perf-IR: A Portable Intermediate Representation for Cross-Platform GPU Performance Prediction

**中文标题：** Perf-IR：面向跨平台 GPU 性能预测的可移植中间表示

**所属 Session：** [Session 3B](index.md) · [MICRO 2026](../index.md)

**作者：** Jiyu Luo, Ruike Liu, Jingwei Sun, Guangzhong Sun

**来源：** MICRO 2026，pp. 1054–1068；[DOI](https://doi.org/10.1109/MICRO67795.2026.00083)

## 英文摘要

Predicting application performance across diverse GPUs is a critical task for guiding hardware design, code optimization, and system scheduling. Existing methods present a difficult trade-off between accuracy and efficiency. High-fidelity simulations are prohibitively slow, while analytical models often struggle with accuracy. Moreover, modern machine learning approaches exhibit poor generalization to unseen hardware, requiring costly retraining for new platforms. To resolve this dilemma, we introduce Perf-IR, a novel and portable intermediate representation for GPU performance. The core innovation of Perf-IR is decoupling a GPU kernel's intrinsic behavior from the target hardware's characteristics. First, we model a kernel as a linear composition of hardware-agnostic IR primitives that embody fundamental computation and memory access patterns. The resulting coefficient vector constitutes the kernel's unique signature, which we can derive efficiently by formulating it as a non-negative linear projection problem. Second, we characterize a hardware platform with a one-time profiling of this small set of IR primitives. The performance prediction for any kernel on that platform is then reduced to a simple dot product between the kernel's Perf-IR and the hardware's performance vector. We extend this kernel-level model to full applications using a DAG-based framework. Our evaluation across distinct GPU architectures demonstrates high prediction accuracy (average error of 10%) with low overhead, validating Perf-IR as a practical and generalizable solution for performance modeling.

## 中文摘要

预测不同 GPU 上的应用程序性能是指导硬件设计、代码优化和系统调度的一项关键任务。现有方法在准确性和效率之间难以权衡。高保真度模拟速度极其缓慢，而分析模型往往难以准确。此外，现代机器学习方法对看不见的硬件的泛化能力很差，需要对新平台进行昂贵的再训练。为了解决这个困境，我们引入了 Perf-IR，一种新颖且可移植的 GPU 性能中间表示。 Perf-IR 的核心创新是将 GPU 内核的固有行为与目标硬件的特性解耦。首先，我们将内核建模为与硬件无关的 IR 原语的线性组合，这些原语体现了基本计算和内存访问模式。得到的系数向量构成了内核的独特签名，我们可以通过将其表示为非负线性投影问题来有效地导出该签名。其次，我们通过对这一小组 IR 原语的一次性分析来表征硬件平台。然后，该平台上任何内核的性能预测都会简化为内核的 Perf-IR 和硬件性能向量之间的简单点积。我们使用基于 DAG 的框架将此内核级模型扩展到完整的应用程序。我们对不同 GPU 架构的评估展示了高预测精度（平均误差为 10%）和低开销，验证了 Perf-IR 作为性能建模的实用且可推广的解决方案。

## 中文关键词

图形处理器；性能建模；中间表示；跨平台；工作负载特征分析

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3B](index.md) · [MICRO 2026 主页](../index.md)
