---
title: "Optimizing Deep Learning Inference Efficiency through Block Dependency Analysis"
description: "ASPLOS 2025 · Session 9A · 通过块级依赖分析优化深度学习推理效率"
tags:
  - "ASPLOS2025"
  - "Session 9A"
  - "ML Compilers"
---

# Optimizing Deep Learning Inference Efficiency through Block Dependency Analysis

**中文标题：** 通过块级依赖分析优化深度学习推理效率

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zhanyuan Di (SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Leping Wang (SKLP, Institute of Computing Technology, CAS), En Shao (SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Zhaojia Ma (SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Ziyi Ren (SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Feng Hua (SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Lixian Ma (SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Jie Zhao (Hunan University), Guangming Tan (SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Ninghui Sun (SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences)

**单位：** SKLP, Institute of Computing Technology, CAS,University of Chinese Academy of Sciences；SKLP, Institute of Computing Technology, CAS；Hunan University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716264) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Inter-operator optimization in deep neural networks (DNNs) relies on accurate data dependency analysis. Traditional machine learning compilers (MLCs) perform static data dependency analysis at the element and operator levels, leading to two key limitations: complex dependencies that hinder efficient inter-operator optimizations, and overlooked parallelizable computations that underutilize GPU resources. We introduce BlockDepend, a novel MLC framework that addresses these issues through block-level dependency analysis. By examining the lower-level phases of compilation, BlockDepend extracts crucial block-level dependency information, simplifying complex relationships between operators and uncovering hidden parallelization opportunities. This allows for targeted optimization strategies that enhance memory access efficiency and improve GPU utilization. Our experiments demonstrate BlockDepend's effectiveness, achieving speedups of 1.71× and 2.88× compared to NVIDIA TensorRT and AMD MIGraphX, respectively, across various workloads.

## 中文摘要

深度神经网络（DNN）中的算子间优化依赖于准确的数据依赖分析。传统的机器学习编译器（MLC）在元素与算子粒度上执行静态数据依赖分析，由此带来两个关键局限：复杂的依赖关系阻碍了高效的算子间优化，以及被忽视的可并行计算导致 GPU 资源利用不足。我们提出 BlockDepend，一个新颖的 MLC 框架，通过块级依赖分析来解决这些问题。通过考察编译过程中更底层的阶段，BlockDepend 提取关键的块级依赖信息，简化算子之间的复杂关系并揭示隐藏的并行化机会。这使得有针对性的优化策略成为可能，从而提升访存效率并改善 GPU 利用率。实验证明了 BlockDepend 的有效性：在多种工作负载上，它相较 NVIDIA TensorRT 与 AMD MIGraphX 分别取得 1.71× 和 2.88× 的加速。

## 英文关键词

Deep Neural Network, Compiler Optimization

## 中文关键词

深度神经网络；编译器优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716264)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2025](../index.md)
