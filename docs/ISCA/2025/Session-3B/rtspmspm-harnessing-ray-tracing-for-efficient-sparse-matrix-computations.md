---
title: "RTSpMSpM: Harnessing Ray Tracing for Efficient Sparse Matrix Computations"
description: "ISCA 2025 · Session 3B · RTSpMSpM：利用光线追踪实现高效稀疏矩阵计算"
tags:
  - "ISCA2025"
  - "Session 3B"
  - "Domain Specific Accelerators I"
---

# RTSpMSpM: Harnessing Ray Tracing for Efficient Sparse Matrix Computations

**中文标题：** RTSpMSpM：利用光线追踪实现高效稀疏矩阵计算

**所属 Session：** [Session 3B](index.md) · [ISCA 2025](../index.md)

**作者：** Hongrui Zhang, Yunan Zhang, Hung-Wei Tseng

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731072) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The significance of sparse matrix algebra pushes the development
of sparse matrix accelerators. Despite the general reception of us-
ing hardware accelerators to address application demands and the
convincement of substantial performance gain, integrating hetero-
geneous hardware accelerators always introduces manufacturing
costs on new hardware and challenges the system interconnects.

Inspired by the similar algorithmic behaviors between ray trac-
ing and sparse matrix problems, this paper exploits ray tracing
hardware. This increasingly popular accelerator has become the
standard in modern GPU architectures to address the demand for
virtual/augmented/mixed reality applications. We propose an al-
gorithm that maps the most classical sparse matrix multiplication
problem (SpMSpM) as a ray tracing problem. By implementing
the proposed algorithm using a modern ray tracing programming
framework, the resulting program, SW-RTSpMSpM can leverage the
accelerated intersection test unit in commercialized GPUs and re-
veals 1.85×speedup over the state-of-the-art SpMSpM library.

Despite the “similarities” in both problems enabling the potential
of accelerating SpMSpM using existing ray tracing hardware, the
“difference” between these two algorithms leaves room for perfor-
mance gain with architectural optimizations. The insights from
evaluating SW-RTSpMSpM guide the proposal of RT+SpMSpM, where
we present two major architectural optimizations that (1) allow si-
multaneous computation on multiplications along with intersection
tests and (2) ray mapping and scheduling and a small row accu-
mulation engine to leverage Gustavson’s dataflow and eliminate
the reliance of additional shader functions and redundant memory
operations.

The resulting RT+SpMSpM only introduces 0.2% area overhead
to a modern high-end ray-tracing-hardware-equipped GPU and
improves SW-RTSpMSpM by 1.66×, achieving 3.06×speedup over
software library and 80% performance per area compared to a state-
of-the-art SpMSpM accelerator, without losing the capability in
supporting ray tracing.

## 中文摘要

稀疏矩阵代数的重要性推动了稀疏矩阵加速器的发展。尽管硬件加速器能够满足应用需求、带来可观性能提升已得到广泛认可，但集成异构硬件加速器不仅会带来新硬件的制造成本，也对系统互连架构提出挑战。

受光线追踪与稀疏矩阵问题在算法行为上的相似性启发，本文复用光线追踪硬件。这类加速器如今应用越来越广泛，已成为现代GPU架构中的标配，用于支撑虚拟/增强/混合现实应用。本文提出一种算法，将最经典的稀疏矩阵乘法问题（SpMSpM）映射为光线追踪问题。基于现代光线追踪编程框架实现该算法后，得到的程序SW-RTSpMSpM可以利用商用GPU中加速的相交测试单元，相比当前最优SpMSpM库实现1.85倍性能提升。

虽然两类问题的相似性使得利用现有光线追踪硬件加速SpMSpM具备可行性，但两种算法之间的差异也说明，仍可通过架构优化进一步挖掘性能。基于对SW-RTSpMSpM的评测结论，本文提出RT+SpMSpM，并给出两项核心架构优化：（1）在执行相交测试的同时并行完成乘法运算；（2）射线映射与调度机制，搭配小型行累加引擎，适配Gustavson数据流，消除对额外着色器函数的依赖以及冗余访存操作。

最终的RT+SpMSpM仅给高端带光线追踪硬件的GPU增加0.2%的面积开销，相比SW-RTSpMSpM提速1.66倍，对比软件库实现3.06倍加速；单位面积性能达到专用SpMSpM加速器的80%，同时保留原有光线追踪功能。

## 英文关键词

Sparse matrix computation, ray tracing, hardware acceleration, SpMSpM

## 中文关键词

稀疏矩阵乘法, 光线追踪硬件复用, Gustavson 数据流, GPU, 相交测试

## 代码与研究制品

- [研究制品](https://zenodo.org/records/15093323)
- [代码仓库](https://github.com/escalab/RTSpMSpM)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731072)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2025](../index.md)
