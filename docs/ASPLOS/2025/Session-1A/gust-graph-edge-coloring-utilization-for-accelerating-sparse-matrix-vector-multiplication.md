---
title: "GUST: Graph Edge-Coloring Utilization for Accelerating Sparse Matrix Vector Multiplication"
description: "ASPLOS 2025 · Session 1A · GUST：利用图边着色加速稀疏矩阵向量乘法"
tags:
  - "ASPLOS2025"
  - "Session 1A"
  - "ML Acceleration"
---

# GUST: Graph Edge-Coloring Utilization for Accelerating Sparse Matrix Vector Multiplication

**中文标题：** GUST：利用图边着色加速稀疏矩阵向量乘法

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Armin Gerami (Computer Science, University of Maryland), Bahar Asgari (Computer Science, University of Maryland)

**单位：** Computer Science, University of Maryland

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674186) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Sparse matrix-vector multiplication (SpMV) plays a vital role in various scientific and engineering fields, from scientific computing to machine learning. Traditional general-purpose processors often fall short of their peak performance with sparse data, leading to the development of domain-specific architectures to enhance SpMV. Yet, these specialized approaches, whether tailored explicitly for SpMV or adapted from matrix-matrix multiplication accelerators, still face challenges in fully utilizing hardware resources as a result of sparsity. To tackle this problem, we introduce GUST, a hardware/software co-design, the key insight of which lies in separating multipliers and adders in the hardware, thereby enabling resource sharing across multiple rows and columns, leading to efficient hardware utilization and ameliorating negative performance impacts from sparsity. Resource sharing, however, can lead to collisions, a problem we address through a specially devised edge-coloring scheduling algorithm. Our comparisons with various prior domain specific architectures using real-world datasets shows the effectiveness of GUST, with an average hardware utilization of 33.67%. We further evaluate GUST by comparing SpMV execution time and energy consumption of length-256 and -87 GUST with length-256 1-dimensional systolic array (1D), achieving an average speedup of 411× and 108×, and energy efficiency improvement of 137× and 148×, respectively. To asses the implementation aspect, we compare resource consumption of GUST with 1D as a baseline through FPGA synthesis. Length-256 GUST uses the same number of arithmetic units as length-256 1D, while length-87 GUST uses considerably less. We also compare GUST with Serpens, a state-of-the-art FPGA-based SpMV accelerator, with GUST achieving lower ower energy consumption on four.

## 中文摘要

稀疏矩阵向量乘法（SpMV）在从科学计算到机器学习的众多科学与工程领域中都发挥着至关重要的作用。传统通用处理器在稀疏数据上往往达不到峰值性能，这促使人们开发领域专用架构来增强 SpMV。然而，这些专门方法——无论是为 SpMV 显式定制，还是从矩阵-矩阵乘法加速器改造而来——由于稀疏性的存在，在充分利用硬件资源方面仍面临挑战。为解决这一问题，我们提出 GUST，一种硬件/软件协同设计，其核心洞见在于在硬件中将乘法器与加法器分离，从而实现跨多个行和列的资源共享，带来高效的硬件利用率并缓解稀疏性带来的负面性能影响。然而，资源共享可能导致冲突，我们通过专门设计的边着色调度算法解决了这一问题。我们使用真实数据集与多种先前的领域专用架构进行比较，显示了 GUST 的有效性，其平均硬件利用率为 33.67%。我们进一步通过比较长度-256 和 -87 的 GUST 与长度-256 一维脉动阵列（1D）的 SpMV 执行时间和能耗来评估 GUST，平均分别取得 411× 和 108× 的加速，能效分别提升 137× 和 148×。为评估实现层面，我们通过 FPGA 综合将 GUST 的资源消耗与作为基线的 1D 进行比较。长度-256 的 GUST 使用的算术单元数量与长度-256 的 1D 相同，而长度-87 的 GUST 使用的算术单元则少得多。我们还将 GUST 与 Serpens——一种最先进的基于 FPGA 的 SpMV 加速器——进行比较，GUST 在其中四个上实现了更低的能耗。

## 英文关键词

SpMV, SpMV Accelerator, Edge Coloring, FPGA

## 中文关键词

SpMV；SpMV 加速器；边着色；FPGA

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674186)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2025](../index.md)
