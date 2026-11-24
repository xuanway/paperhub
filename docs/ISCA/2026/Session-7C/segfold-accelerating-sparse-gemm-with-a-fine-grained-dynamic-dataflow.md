---
title: "SegFold: Accelerating Sparse GEMM with a Fine-Grained Dynamic Dataflow"
description: "ISCA 2026 · Session 7C · SegFold: Accelerating Sparse GEMM with a Fine-Grained Dynamic Dataflow"
tags:
  - "ISCA2026"
  - "Session 7C"
  - "Domain Specific Accelerators 2"
---

# SegFold: Accelerating Sparse GEMM with a Fine-Grained Dynamic Dataflow

**中文标题：** SegFold: 以细粒度动态数据流加速稀疏 GEMM

**所属 Session：** [Session 7C](index.md) · [ISCA 2026](../index.md)

**作者：** Xinrui Wu, Hanyu Wang, Jason Cong, Tony Nowatzki

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Generalized sparse matrix-matrix multiplication (SpGEMM) is critical in many domains. Existing CPUs and GPUs, as well as specialized accelerators, rely on static dataflows (e.g., inner product, outer product, Gustavson, etc.). Each static dataflow sacrifices some data reuse opportunities and imposes constraints on load balance. To address this inefficiency, we extend the typical SpGEMM dataflows by considering dynamism. Specifically, we add fine-grained dynamic scheduling to optimize reuse and reduce resource contention. We also develop dynamic remapping of partially completed work to improve load balance and parallelism. These ideas are formalized into a specific dataflow called Segment. To demonstrate Segment, we codesign a SpGEMM accelerator called SegFold. SegFold includes a memory controller that identifies fine-grained reuse opportunities in a local window of the stationary input array and exploits them through dynamic work assignment. It also incorporates a merge network that routes inputs to appropriate processing elements (PEs) for computation while dynamically remapping the work assigned to each PE to balance load. Across diverse densities and matrix sizes, SegFold achieves a geometric-mean 1.95× speedup over state-of-the-art SpGEMM accelerators and 5.3× over the best static dataflow configuration, demonstrating that adding dynamism to the dataflow design space unlocks reuse and load-balance gains that no static scheduling choice can achieve in isolation.

## 中文摘要

广义稀疏矩阵–矩阵乘法（SpGEMM）在许多领域都至关重要。现有 CPU 和 GPU 以及专用加速器都依赖于静态数据流（如内积、外积、Gustavson 等）。每种静态数据流都会牺牲一些数据重用机会，并对负载均衡施加约束。为解决这种低效，我们通过考虑动态性来扩展典型的 SpGEMM 数据流。具体而言，我们加入细粒度动态调度以优化重用并减少资源争用。我们还开发了对部分完成工作的动态重映射，以改善负载均衡和并行性。这些思想被形式化为一种称为 Segment 的特定数据流。为演示 Segment，我们协同设计了一个名为 SegFold 的 SpGEMM 加速器。SegFold 包含一个内存控制器，它在驻留输入数组的局部窗口中识别细粒度重用机会，并通过动态工作分配加以利用。它还包含一个合并网络，将输入路由到合适的处理单元（PE）进行计算，同时动态重映射分配给每个 PE 的工作以均衡负载。在不同的密度和矩阵规模下，SegFold 相比最先进的 SpGEMM 加速器实现了几何平均 1.95× 的加速，相比最佳静态数据流配置实现 5.3× 的加速，表明在数据流设计空间中加入动态性可以释放任何单一静态调度选择都无法企及的重用与负载均衡收益。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2026](../index.md)
