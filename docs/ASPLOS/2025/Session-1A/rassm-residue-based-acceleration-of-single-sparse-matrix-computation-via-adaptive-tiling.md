---
title: "RASSM: Residue-based Acceleration of Single Sparse Matrix Computation via Adaptive Tiling"
description: "ASPLOS 2025 · Session 1A · RASSM：基于残差的自适应分块单稀疏矩阵计算加速"
tags:
  - "ASPLOS2025"
  - "Session 1A"
  - "ML Acceleration"
---

# RASSM: Residue-based Acceleration of Single Sparse Matrix Computation via Adaptive Tiling

**中文标题：** RASSM：基于残差的自适应分块单稀疏矩阵计算加速

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Anirudh Jain (Georgia Institute of Technology), Pulkit Gupta (Georgia Institute of Technology), Thomas M. Conte (Georgia Institute of Technology)

**单位：** Georgia Institute of Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707219) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Single-Sparse-Matrix Kernels (SSMKs) such as SpMM, SDDMM, SpMV, and SpTS form the backbone of applications such as data analytics, graph processing, finite-element analysis, machine learning (including GNNs and LLMs), etc. This paper introduces Residue-based Acceleration of Single Sparse Matrix Computation via Adaptive Tiling (RASSM), an input-dependent, adaptive 2-dimensional tiling technique for SSMKs. The adaptation leverages the concept of a residue matrix: a data structure that compactly captures the pattern of non-zeros in the sparse matrix. With residues, we show it is possible to make intelligent decisions on adaptive tile sizes, resulting in increased cache occupancy. Residues allow for optimizations across both spatial and temporal locality. RASSM improves data movement and overall performance as compared to prior techniques. For example, using spatial analysis for SpMM on commodity server CPUs, RASSM has 1.30× speedup over MKL, 1.32× over J-Stream, 1.20× over ASpT, 1.11× over CSF-4 uniform-shape, and 1.10× over CSF-4 uniform-occupancy. RASSM with temporal analysis improves this to 1.36× (vs. MKL), 1.38× (vs. J-Stream), 1.26× (vs. ASpT), 1.17× (vs. CSF-4 uniform-shape), and 1.16× (vs. CSF-4 uniform-occupancy).

## 中文摘要

单稀疏矩阵内核（SSMK），如 SpMM、SDDMM、SpMV 和 SpTS，是数据分析、图处理、有限元分析、机器学习（包括 GNN 和 LLM）等应用的骨干。本文提出了基于残差的自适应分块单稀疏矩阵计算加速（RASSM），一种面向 SSMK 的输入相关的自适应二维分块技术。该自适应方法利用了残差矩阵的概念：一种紧凑刻画稀疏矩阵中非零元素模式的数据结构。借助残差，我们表明可以对自适应分块尺寸做出智能决策，从而提高缓存占用率。残差使得在空间局部性和时间局部性两方面进行优化成为可能。与先前技术相比，RASSM 改进了数据移动和整体性能。例如，在商用服务器 CPU 上对 SpMM 使用空间分析时，RASSM 相比 MKL 有 1.30× 加速，相比 J-Stream 有 1.32×，相比 ASpT 有 1.20×，相比 CSF-4 uniform-shape 有 1.11×，相比 CSF-4 uniform-occupancy 有 1.10×。采用时间分析的 RASSM 将此提升至 1.36×（对比 MKL）、1.38×（对比 J-Stream）、1.26×（对比 ASpT）、1.17×（对比 CSF-4 uniform-shape）和 1.16×（对比 CSF-4 uniform-occupancy）。

## 英文关键词

Sparse Computations, Caching, Auto-Tiling, Multicore, SpMM, SDDMM, Sparse Matrix, Sparse Signatures

## 中文关键词

稀疏计算；缓存；自动分块；多核；SpMM；SDDMM；稀疏矩阵；稀疏签名

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707219)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2025](../index.md)
