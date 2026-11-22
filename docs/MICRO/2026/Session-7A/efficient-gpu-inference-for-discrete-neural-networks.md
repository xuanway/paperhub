---
title: "Efficient GPU Inference for Discrete Neural Networks"
description: "MICRO 2026 · Session 7A · 离散神经网络的高效 GPU 推理"
tags:
  - "MICRO2026"
  - "GPU"
  - "Neural Networks"
---

# Efficient GPU Inference for Discrete Neural Networks

**中文标题：** 离散神经网络的高效 GPU 推理

**所属 Session：** [Session 7A](index.md) · [MICRO 2026](../index.md)

**作者：** Ke Yang, Guanghui Song, Junhui Peng, En Shao, Xia Zhao, Zhuo Tang, Kenli Li, Jie Zhao

**来源：** MICRO 2026，pp. 2373–2387；[DOI](https://doi.org/10.1109/MICRO67795.2026.00163)

## 英文摘要

Discrete neural networks (DiNNs), including spik-Discrete neural networks (DiNNs), including spiking, binary, and Boolean models, replace floating-point convolutions and matrix multiplications with discrete operators, enabling faster inference and lower energy consumption. Despite their algorithmic diversity, these workloads share a common execution property: computations reduce to discretized activations combined with bitwise or low-precision arithmetic, forming structured operator patterns that differ fundamentally from dense floating-point workloads and are not well supported by existing GPU software stacks. We present Helios, a cross-layer framework that accelerates DiNN inference through compiler and GPU execution co-design. Helios introduces pattern-specialized primitives for discretized operators, a pattern-driven compiler with algebraic transformations and execution-aware fusion, and runtime integration with CUDA Graphs to improve both performance and energy efficiency. We evaluate Helios on eight DiNN workloads spanning quantized, binary, Boolean, and spiking models across three NVIDIA GPUs (RTX 4090, A100, and V100). Compared with PyTorch, TVM, BladeDISC, Welder, TensorRT, BitBLAS, CUTLASS, Brain2CUDA, and TCBNN, Helios achieves over 2x mean improvements in both inference latency and energy efficiency, demonstrating the effectiveness of unified execution support for DiNNs on modern GPUs.

## 中文摘要

离散神经网络 (DiNN)，包括尖峰离散神经网络 (DiNN)，包括尖峰模型、二值模型和布尔模型，用离散运算符取代浮点卷积和矩阵乘法，从而实现更快的推理和更低的能耗。尽管算法多种多样，但这些工作负载共享一个共同的执行属性：计算减少为与按位或低精度算术相结合的离散激活，形成与密集浮点工作负载根本不同的结构化运算符模式，并且现有 GPU 软件堆栈无法很好地支持。我们推出了 Helios，这是一个跨层框架，可通过编译器和 GPU 执行协同设计来加速 DiNN 推理。 Helios 引入了用于离散运算符的模式专用原语、具有代数变换和执行感知融合的模式驱动编译器，以及与 CUDA 图形的运行时集成，以提高性能和能效。我们在跨三个 NVIDIA GPU（RTX 4090、A100 和 V100）的量化、二进制、布尔和尖峰模型的八个 DiNN 工作负载上评估 Helios。与 PyTorch、TVM、BladeDISC、Welder、TensorRT、BitBLAS、CUTLASS、Brain2CUDA 和 TCBNN 相比，Helios 在推理时延和能效方面实现了超过 2 倍的平均改进，展示了现代 GPU 上对 DiNN 统一执行支持的有效性。

## 中文关键词

图形处理器；深度学习；量化；脉冲网络；能耗

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7A](index.md) · [MICRO 2026 主页](../index.md)
