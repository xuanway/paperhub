---
title: "Scalable Benchmarking Framework for Dynamic Quantum Circuits"
description: "MICRO 2026 · Session 8D · 面向动态量子电路的可扩展基准测试框架"
tags:
  - "MICRO2026"
  - "Quantum Computing"
---

# Scalable Benchmarking Framework for Dynamic Quantum Circuits

**中文标题：** 面向动态量子电路的可扩展基准测试框架

**所属 Session：** [Session 8D](index.md) · [MICRO 2026](../index.md)

**作者：** Sumeet Shirgure, Efekan Kökcü, Anupam Mitra, Wibe Albert de Jong, Costin Iancu, Siyuan Niu

**来源：** MICRO 2026，pp. 3072–3087；[DOI](https://doi.org/10.1109/MICRO67795.2026.00206)

## 英文摘要

Dynamic quantum circuits with mid-circuit measurements (MCMs) and feed-forward operations play a crucial role in various applications, such as quantum error correction and quantum algorithms. With advancements in quantum hardware enabling the implementation of MCM and feed-forward loops, the use of dynamic circuits has become increasingly prevalent. There is a significant need for a benchmarking framework specially designed for dynamic circuits to capture their unique properties, as current benchmarking tools are designed primarily for unitary circuits and cannot be trivially extended to dynamic circuits. We propose dynamarq, a scalable and hardware-agnostic benchmarking framework for dynamic circuits. We collect a suite of dynamic circuit benchmarks spanning various applications and propose a broad set of circuit features to characterize the structure of these dynamic circuits. We run them on two IBM quantum processors and the Quantinuum Helios-1E emulator, and propose scalable, application-dependent fidelity scores for each benchmark based on hardware execution results. We perform statistical modeling to identify correlations between circuit features and fidelity scores, and demonstrate highly accurate fidelity prediction using our model. Our model parameters are also transferable across hardware backends and calibration cycles. Our framework facilitates the understanding of dynamic circuit structures and provides insights for designing and optimizing dynamic circuits to achieve high execution fidelity on quantum hardware.

## 中文摘要

具有中电路测量（MCM）和前馈操作的动态量子电路在量子纠错和量子算法等各种应用中发挥着至关重要的作用。随着量子硬件的进步使得 MCM 和前馈环路的实现成为可能，动态电路的使用变得越来越普遍。非常需要一个专门为动态电路设计的基准测试框架来捕获其独特的属性，因为当前的基准测试工具主要是为单一电路设计的，不能轻易扩展到动态电路。我们提出了 dynamarq，一种可扩展且与硬件无关的动态电路基准测试框架。我们收集了一套涵盖各种应用的动态电路基准，并提出了一组广泛的电路特征来表征这些动态电路的结构。我们在两个 IBM 量子处理器和 Quantinuum Helios-1E 仿真器上运行它们，并根据硬件执行结果为每个基准测试提供可扩展的、依赖于应用程序的保真度分数。我们执行统计建模来识别电路特征和保真度分数之间的相关性，并使用我们的模型展示高度准确的保真度预测。我们的模型参数也可以跨硬件后端和校准周期传输。我们的框架有助于理解动态电路结构，并为设计和优化动态电路提供见解，以在量子硬件上实现高执行保真度。

## 中文关键词

量子计算；基准测试；动态量子电路；可扩展评估

## 代码与研究制品

- 代码仓库：[https://github.com/sumeetshirgure/dynamarq-execution](https://github.com/sumeetshirgure/dynamarq-execution)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21459804](https://doi.org/10.5281/zenodo.21459804)
- 代码仓库：[https://github.com/sumeetshirgure/dynamarq](https://github.com/sumeetshirgure/dynamarq)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8D](index.md) · [MICRO 2026 主页](../index.md)
