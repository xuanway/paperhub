---
title: "Insum: Sparse GPU Kernels Simplified and Optimized with Indirect Einsums"
description: "ASPLOS 2026 · Session 2C · Insum：用间接 Einsum 简化并优化稀疏 GPU 内核"
tags:
  - "ASPLOS2026"
  - "Session 2C"
  - "GPU Systems & Scheduling"
---

# Insum: Sparse GPU Kernels Simplified and Optimized with Indirect Einsums

**中文标题：** Insum：用间接 Einsum 简化并优化稀疏 GPU 内核

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jaeyeon Won (MIT), Willow Ahrens (Georgia Tech), Joel Emer (MIT/NVIDIA), Saman Amarasinghe (MIT)

**单位：** MIT；Georgia Tech；MIT/NVIDIA

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790176) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Programming high-performance sparse GPU kernels is notoriously difficult, requiring both substantial effort and deep expertise. Sparse compilers aim to simplify this process, but existing systems fall short in two key ways. First, they are primarily designed for CPUs and rarely produce high-performance GPU code. Second, when computations involve both sparse and dense regions, these compilers often fail to optimize the dense portions effectively. In this paper, we propose a new approach for expressing sparse computations. We start from format-agnostic Einsums over sparse tensors and rewrite them into format-conscious indirect Einsums, which explicitly encode format information by mapping sparse data and metadata onto dense tensor operations through indirect indexing. To execute indirect Einsums, we introduce the Insum compiler, which generates efficient GPU code for these Einsums by lowering to the PyTorch compiler, extended to better support Tensor Core–enabled indirect Einsums. We also present two fixed-length sparse formats, GroupCOO and BlockGroupCOO, designed to fit naturally with indirect Einsums. Our approach achieves 1.14×–3.81× speedups across a range of sparse GPU applications while reducing lines of code by 202×–4491× compared to hand-written implementations. The source code for Insum is publicly

## 中文摘要

编写高性能稀疏 GPU 内核是出了名的困难，既需要大量精力投入，也需要深厚的专业知识。稀疏编译器旨在简化这一过程，但现有系统在两个关键方面存在不足。第一，它们主要面向 CPU 设计，很少能生成高性能的 GPU 代码。第二，当计算同时涉及稀疏区域和稠密区域时，这些编译器往往无法有效优化稠密部分。在本文中，我们提出一种表达稀疏计算的新方法。我们从作用于稀疏张量的格式无关 Einsum 出发，将其重写为格式感知的间接 Einsum，后者通过间接索引把稀疏数据与元数据映射到稠密张量操作上，从而显式编码格式信息。为执行间接 Einsum，我们引入 Insum 编译器，它通过下沉到 PyTorch 编译器来为这些 Einsum 生成高效的 GPU 代码，并对该编译器加以扩展，以更好地支持启用 Tensor Core 的间接 Einsum。我们还提出两种定长稀疏格式 GroupCOO 和 BlockGroupCOO，它们被设计为与间接 Einsum 自然契合。与手写实现相比，我们的方法在一系列稀疏 GPU 应用中取得 1.14×–3.81× 的加速，同时将代码行数减少 202×–4491×。Insum 的源代码已公开

## 英文关键词

Tensor compilers; GPU code generation; Sparse tensor compilers; Sparse GPU kernels; Einsums

## 中文关键词

张量编译器；GPU 代码生成；稀疏张量编译器；稀疏 GPU 内核；Einsum

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790176)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2026](../index.md)
