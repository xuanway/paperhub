---
title: "Virgo: Cluster-level Matrix Unit Integration in GPUs for Scalability and Energy Efficiency"
description: "ASPLOS 2025 · Session 10A · Virgo：面向可扩展性与能效的 GPU 簇级矩阵单元集成"
tags:
  - "ASPLOS2025"
  - "Session 10A"
  - "GPGPU"
---

# Virgo: Cluster-level Matrix Unit Integration in GPUs for Scalability and Energy Efficiency

**中文标题：** Virgo：面向可扩展性与能效的 GPU 簇级矩阵单元集成

**所属 Session：** [Session 10A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Hansung Kim (University of California, Berkeley), Ruohan Richard Yan (University of California, Berkeley), Joshua You (University of California, Berkeley), Tieliang Vamber Yang (NVIDIA Corporation), Yakun Sophia Shao (University of California, Berkeley)

**单位：** University of California, Berkeley；NVIDIA Corporation

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716281) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Modern GPUs incorporate specialized matrix units such as Tensor Cores to accelerate GEMM operations, which are central to deep learning workloads. However, existing matrix unit designs are tightly coupled to the SIMT core, restricting operation size due to register file capacity and bandwidth constraints. Such a limitation in scalability makes it difficult to simultaneously improve compute throughput and energy efficiency in GPUs. To address this challenge, we propose Virgo, a GPU microarchitecture that integrates dedicated matrix units at the SIMT core cluster level. By decoupling the matrix unit from the SIMT core, Virgo eliminates scalability constraints imposed by the core microarchitecture. Consequently, Virgo increases operation granularity at the hardware level, reducing energy overhead from core instruction processing. Physical disaggregation also enables a unified matrix unit design and offloading both operand and accumulator accesses from the register file, improving data reuse and energy efficiency. Furthermore, this disaggregation supports efficient concurrent execution of the SIMT core and matrix unit, optimizing mapping for fused DNN workloads. Our evaluations using synthesizable RTL demonstrate that Virgo achieves 67.3% and 24.2% reduction in on-chip active power consumption, compared to the baseline Ampere-style and Hopper-style core-coupled designs.

## 中文摘要

现代 GPU 引入 Tensor Cores 等专用矩阵单元来加速 GEMM 运算，而 GEMM 是深度学习工作负载的核心。然而，现有的矩阵单元设计与 SIMT 核心紧密耦合，受寄存器堆容量和带宽约束的限制，运算规模难以扩大。这种可扩展性上的局限使得 GPU 难以同时提升计算吞吐与能效。为应对这一挑战，我们提出 Virgo，一种在 SIMT 核心簇（cluster）层级集成专用矩阵单元的 GPU 微架构。通过将矩阵单元与 SIMT 核心解耦，Virgo 消除了核心微架构施加的可扩展性约束。因此，Virgo 在硬件层面提高了运算粒度，减少了核心指令处理带来的能耗开销。物理上的解耦还使统一的矩阵单元设计成为可能，并将操作数与累加器的访问从寄存器堆中卸载出去，从而改善数据复用与能效。此外，这种解耦支持 SIMT 核心与矩阵单元的高效并发执行，优化了融合 DNN 工作负载的映射。我们使用可综合 RTL 的评估表明，与 Ampere 风格和 Hopper 风格的基线核心耦合设计相比，Virgo 的片上有功功耗分别降低了 67.3% 和 24.2%。

## 英文关键词

GPUs, Microarchitecture, Accelerators, Scalability, Power and Energy, Machine Learning

## 中文关键词

GPU；微架构；加速器；可扩展性；功耗与能效；机器学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716281)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10A](index.md) · [返回 ASPLOS 2025](../index.md)
