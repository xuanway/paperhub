---
title: "SLAWS: Spatial Locality Analysis and Workload Orchestration for Sparse Matrix Multiplication"
description: "ASPLOS 2026 · Session 6C · SLAWS：面向稀疏矩阵乘法的空间局部性分析与工作负载编排"
tags:
  - "ASPLOS2026"
  - "Session 6C"
  - "Graph & Sparse Computing"
---

# SLAWS: Spatial Locality Analysis and Workload Orchestration for Sparse Matrix Multiplication

**中文标题：** SLAWS：面向稀疏矩阵乘法的空间局部性分析与工作负载编排

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Guoyu Li (Fudan University), Zheng Guan (Fudan University), Beichen Zhang (Fudan University), Jun Yu (Fudan University), Kun Wang (Fudan University)

**单位：** Fudan University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790222) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Sparse matrix-sparse matrix multiplication (SpMSpM) is widely used in modern scientific applications, including high-performance computing, linear algebra, and graph processing. However, the highly variable distribution of nonzero elements in these matrices presents a significant challenge to computational efficiency. While existing sparse matrix accelerators often rely on specialized architectures tailored for specific dataflow, these designs sacrifice generality and fail to fully exploit potential data reuse opportunities. In this paper, we propose Slaws, an efficient and general-purpose accelerator architecture for SpMSpM. This design accelerates computation by analyzing distinct sparsity patterns and leveraging various data reuse opportunities. We introduce two key strategies to address the challenges of different matrix operand positions. For the left multiplicand, we present a Pass-Aware strategy to analyze matrix structures, identify unique sparsity patterns, and optimize memory access. For the right multiplicand, we introduce a ShuffleCompare strategy to dynamically balance the multiplication workload across computing units. By approximating the top𝐾outputs per cycle, this method minimizes idle time and ensures a balanced workload distribution. We implement both strategies in Slaws and conduct extensive experiments. The results show that Slaws achieves 1.46× and 1.43× speedups over two state-of-the-art accelerators, and 1.55× speedup over GPU.

## 中文摘要

稀疏矩阵-稀疏矩阵乘法（SpMSpM）被广泛应用于现代科学应用中，包括高性能计算、线性代数和图处理。然而，这些矩阵中非零元素分布的高度可变性对计算效率构成了重大挑战。现有稀疏矩阵加速器往往依赖为特定数据流定制的专用架构，但这些设计牺牲了通用性，并且未能充分利用潜在的数据复用机会。本文提出 Slaws，一种面向 SpMSpM 的高效且通用的加速器架构。该设计通过分析不同的稀疏模式并利用各种数据复用机会来加速计算。我们引入两种关键策略，以应对不同矩阵操作数位置带来的挑战。对于左侧乘数，我们提出 Pass-Aware 策略，用于分析矩阵结构、识别独特的稀疏模式并优化内存访问。对于右侧乘数，我们引入 ShuffleCompare 策略，在计算单元之间动态均衡乘法工作负载。通过每个周期近似得到 top𝐾 输出，该方法最小化了空闲时间并确保工作负载分布均衡。我们在 Slaws 中实现了这两种策略并开展了大量实验。结果表明，与两个最先进的加速器相比，Slaws 分别取得 1.46× 和 1.43× 的加速，与 GPU 相比取得 1.55× 的加速。

## 英文关键词

Sparse matrix multiplication; Hardware acceleration; Data reuse; Workload balancing

## 中文关键词

稀疏矩阵乘法；硬件加速；数据复用；工作负载均衡

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790222)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6C](index.md) · [返回 ASPLOS 2026](../index.md)
