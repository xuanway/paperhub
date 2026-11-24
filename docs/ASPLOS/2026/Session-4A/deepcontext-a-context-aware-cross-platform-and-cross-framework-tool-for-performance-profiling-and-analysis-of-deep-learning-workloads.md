---
title: "DeepContext: A Context-aware, Cross-platform, and Cross-framework Tool for Performance Profiling and Analysis of Deep Learning Workloads"
description: "ASPLOS 2026 · Session 4A · DeepContext：一个面向深度学习工作负载性能剖析与分析的上下文感知、跨平台、跨框架工具"
tags:
  - "ASPLOS2026"
  - "Session 4A"
  - "ML Training & Monitoring"
---

# DeepContext: A Context-aware, Cross-platform, and Cross-framework Tool for Performance Profiling and Analysis of Deep Learning Workloads

**中文标题：** DeepContext：一个面向深度学习工作负载性能剖析与分析的上下文感知、跨平台、跨框架工具

**所属 Session：** [Session 4A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Qidong Zhao (North Carolina State University), Hao Wu (George Mason University), Yueming Hao (North Carolina State University), Zilingfeng Ye, Jiajia Li (North Carolina State University), Xu Liu (North Carolina State University), Keren Zhou (George Mason University)

**单位：** North Carolina State University；George Mason University

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736127) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Effective performance optimization of deep learning models requires comprehensive profiling across heterogeneous computing environments, yet existing tools fail to bridge the semantic gap between high-level operations and low-level execution. This paper presents DeepContext, a novel profiling system that correlates program contexts across Python code, deep learning frameworks, C/C++ libraries, and GPU execution. DeepContext features a framework-agnostic shim layer that seamlessly correlates the behavior of the deep learning framework with hardware performance metrics. Furthermore, DeepContext provides an automated performance analyzer that offers actionable optimization guidance based on its holistic view of the entire software stack of deep learning applications. DeepContext works for mainstream deep learning frameworks and runs on modern CPU+GPU architectures with low overhead. Our evaluation demonstrates that DeepContext uncovers previously hidden performance bottlenecks in real-world deep-learning applications. Guided by DeepContext, we are able to fix multiple performance issues, achieving speed-ups between 1.06× and 1.66×.

## 中文摘要

深度学习模型的有效性能优化需要在异构计算环境中进行全面的性能剖析，然而现有工具无法弥合高层操作与低层执行之间的语义鸿沟。本文提出 DeepContext，一个新颖的剖析系统，它能够跨 Python 代码、深度学习框架、C/C++ 库以及 GPU 执行关联程序上下文。DeepContext 具有一个与框架无关的垫层（shim layer），可将深度学习框架的行为与硬件性能指标无缝关联。此外，DeepContext 提供了一个自动化性能分析器，基于其对深度学习应用整个软件栈的整体视图，给出可操作的优化指导。DeepContext 适用于主流深度学习框架，并可在现代 CPU+GPU 架构上以低开销运行。我们的评估表明，DeepContext 能够揭示真实深度学习应用中此前隐藏的性能瓶颈。在 DeepContext 的指导下，我们能够修复多个性能问题，实现 1.06× 至 1.66× 的加速。

## 英文关键词

Profiling Tool; Deep Learning; Performance Tuning; Heterogeneous Computing; Context-aware Profiling; Automated Analysis; Cross-framework Profiling

## 中文关键词

性能剖析工具；深度学习；性能调优；异构计算；上下文感知剖析；自动化分析；跨框架剖析

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736127)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 4A](index.md) · [返回 ASPLOS 2026](../index.md)
