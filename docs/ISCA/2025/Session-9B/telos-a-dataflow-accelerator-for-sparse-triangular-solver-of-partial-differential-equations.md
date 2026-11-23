---
title: "Telos: A Dataflow Accelerator for Sparse Triangular Solver of Partial Differential Equations"
description: "ISCA 2025 · Session 9B · Telos：面向偏微分方程稀疏三角求解器的数据流加速器"
tags:
  - "ISCA2025"
  - "Session 9B"
  - "HPC"
---

# Telos: A Dataflow Accelerator for Sparse Triangular Solver of Partial Differential Equations

**中文标题：** Telos：面向偏微分方程稀疏三角求解器的数据流加速器

**所属 Session：** [Session 9B](index.md) · [ISCA 2025](../index.md)

**作者：** Xiaochen Hao, Hao Luo, Chu Wang, Chao Yang, Yun Liang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731078) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Partial Differential Equations (PDEs) serve as the backbone of nu- merous scientific problems. Their solutions often rely on numer- ical methods, which transform these equations into large, sparse systems of linear equations. These systems, solved with iterative methods, exhibit structured sparsity patterns when derived from stencil-based numerical schemes. In preconditioned solvers, the sparse triangular solve procedure, SpTRSV, usually dominates the entire execution due to its loop-carried dependencies. Optimizing SpTRSV requires extracting parallelism from dependent computa- tions. However, prior works have struggled to achieve both high parallelism and data locality, leading to suboptimal performance. We propose Telos, a dataflow accelerator for SpTRSV that ex- ploits structured sparsity patterns in PDE solving. The dataflow execution leverages stencil patterns, efficiently utilizing pipeline parallelism to resolve data dependencies with minimal overhead. We tackle the challenge of complex data dependencies by propos- ing a plane-parallel pipelining technique that maps computations onto processing elements (PEs) while preserving data locality. A cross-plane communication aggregation technique is developed to streamline data transfers into a systolic manner. Our accelera- tor features effective pipelining of dependent computations and overlapping of computations with memory accesses. Experiments demonstrate that Telos delivers average speedups of 61×, 8×, and 11×over CPUs, GPUs, state-of-the-art accelerator, respectively.

## 中文摘要

偏微分方程（PDE）是大量科学问题的基础。求解这类方程通常依靠数值方法，将方程转化为大规模稀疏线性方程组。若该方程组由基于模板（stencil）的数值格式离散得到，采用迭代法求解时，会呈现结构化稀疏特征。在预条件求解器中，稀疏三角求解SpTRSV存在循环携带依赖，往往是整个流程里的性能瓶颈。优化SpTRSV需要从存在依赖的计算中挖掘并行度，但已有方案很难同时兼顾高并行度与良好的数据局部性，性能难以达到最优。

本文提出Telos，一款面向SpTRSV的数据流加速器，专门利用PDE求解场景下的结构化稀疏特性。该数据流执行机制依托模板特征，以很低开销利用流水线并行化解数据依赖。
针对复杂数据依赖难题，本文提出**平面并行流水线技术**，在把计算映射到处理单元（PE）的同时保留数据局部性；同时设计跨平面通信聚合技术，让数据传输以脉动阵列方式规整流转。该加速器可以对存在依赖的计算做高效流水线，并实现计算与访存的重叠。实验结果表明：Telos相比CPU、GPU、前沿加速器，平均分别提速61倍、8倍、11倍。

## 英文关键词

Partial Differential Equations, SpTRSV, Dataflow Architecture

## 中文关键词

偏微分方程, SpTRSV, 数据流架构

## 代码与研究制品

- [代码仓库](https://github.com/pku-liang/telos)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731078)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9B](index.md) · [返回 ISCA 2025](../index.md)
