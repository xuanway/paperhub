---
title: "GPUs All Grown-Up: Fully Device-Driven SpMV Using GPU Work Graphs"
description: "ISCA 2025 · Session 9B · 成熟的 GPU：利用 GPU 工作图实现完全设备驱动的 SpMV"
tags:
  - "ISCA2025"
  - "Session 9B"
  - "HPC"
---

# GPUs All Grown-Up: Fully Device-Driven SpMV Using GPU Work Graphs

**中文标题：** 成熟的 GPU：利用 GPU 工作图实现完全设备驱动的 SpMV

**所属 Session：** [Session 9B](index.md) · [ISCA 2025](../index.md)

**作者：** Fabian Wildgrube, Pete Ehrett, Paul Trojahn, Richard Membarth, Brad Beckmann, Dominik Baumeister, Matth?us Chajdas

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731060) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Sparse matrix-vector multiplication (SpMV) is a key operation across high-performance computing, graph analytics, and many more applications. In these applications, the matrix characteristics, notably non-zero elements per row, can vary widely and impact which algorithm performs best. Thus, Graphics Processing Unit (GPU) SpMV algorithms often rely on costly preprocessing to deter- mine what per-row algorithm to select to achieve high performance. In this work we combine SpMV preprocessing and the subsequent per-row processing on the GPU by leveraging the novel “Work Graphs” GPU programming model—initially designed for graphics applications—for dynamic on-device self-scheduling. Work Graphs allow for fine-grain dataflow execution of individual workgroups using emerging hardware and firmware support. As soon as pre- processing has generated sufficient work, workgroups of individual processing kernels are self-scheduled and executed, interleaved with those of other kernels. This improves cache locality and elimi- nates host interaction altogether. Across a suite of 59 sparse matri- ces, the best of various novel Work Graphs SpMV implementations outperforms state-of-the-art rocSPARSE “LRB” for a single SpMV by up to 7.19×(mean: 3.35×, SD: 1.89). Furthermore, it achieves much more stable performance across various sparsity patterns than the rocSPARSE CSR-General algorithm, and even beats the advanced rocSPARSE CSR-Adaptive algorithm for up to 92 consecu- tive SpMV calculations. In addition, compared to rocSPARSE LRB, it reduces code complexity by 75%. Its memory footprint for support- ing data structures is a fixed∼25 MiB independent of matrix size, compared to rocSPARSE LRB’s data structures that scale with matrix size to hundreds of megabytes. Overall, this work showcases the performance potential of emerging dynamic on-device scheduling techniques for GPU compute applications.

## 中文摘要

稀疏矩阵向量乘法（SpMV）是高性能计算、图分析等众多应用里的核心算子。在这类应用中，矩阵特征（尤其是每行非零元数量）差异很大，会直接决定哪种算法性能最优。因此现有的GPU SpMV算法通常需要开销不菲的预处理，为每一行挑选合适的计算策略，以此拿到高性能。

本文借助全新的GPU编程模型**工作图（Work Graphs）**——该模型最初面向图形渲染设计，实现GPU端动态自调度，将SpMV的预处理与后续逐行计算全部放在GPU上完成。依托新硬件与固件支持，工作图可以对各个工作组做细粒度数据流执行。只要预处理产出足够任务，各个计算核的工作组就能够自调度、交错执行，提升缓存局部性，并且完全不需要主机参与交互。

在59个稀疏矩阵构成的测试集上，多种基于工作图的SpMV实现中最优版本，单次SpMV相比前沿rocSPARSE LRB最高提速7.19倍（均值3.35倍，标准差1.89）。同时，它在不同稀疏模式下的性能稳定性远优于rocSPARSE CSR-General；在连续92次SpMV的场景下，性能甚至超过更先进的rocSPARSE CSR-Adaptive。
此外，对比rocSPARSE LRB，该方案代码复杂度降低75%；支撑数据结构的内存占用固定约25 MiB，和矩阵大小无关，而rocSPARSE LRB的辅助结构会随矩阵规模增长至数百MB。
综上，这项工作展示了新兴的GPU端动态调度技术在通用GPU计算场景中的性能潜力。

## 英文关键词

Dynamic Scheduling, GPU Computing, HPC, SpMV, Work Graphs

## 中文关键词

动态调度, GPU计算, 高性能计算, 稀疏矩阵向量乘法, 工作图

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731060)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9B](index.md) · [返回 ISCA 2025](../index.md)
