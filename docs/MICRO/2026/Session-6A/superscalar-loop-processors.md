---
title: "Superscalar Loop Processors"
description: "MICRO 2026 · Session 6A · 超标量循环处理器"
tags:
  - "MICRO2026"
---

# Superscalar Loop Processors

**中文标题：** 超标量循环处理器

**所属 Session：** [Session 6A](index.md) · [MICRO 2026](../index.md)

**作者：** Luca Colagrande, Pascal Etterli, Luca Benini

**来源：** MICRO 2026，pp. 1915–1931；[DOI](https://doi.org/10.1109/MICRO67795.2026.00135)

## 英文摘要

To sustain the computational demands of modern ML and HPC workloads, programmable accelerators integrate large arrays of processing elements (PEs), typically built around single-issue in-order cores to maximize integration density and energy efficiency. As a result, each PE's instruction throughput is upper-bounded at one instruction per cycle (IPC), often suffering from significant underutilization of its functional units (FUs). Conventional superscalar processors can improve FU utilization by increasing IPC, but they typically incur substantial area and energy overheads. This work proposes the Superscalar Loop Processor (SLP) architecture, a lightweight approach to superscalar execution that targets regular, compute-intensive loop kernels. We present the SLP execution model, which exploits the static structure of these workloads to enable efficient multiple-issue execution without the complexity of dynamic out-of-order scheduling. We demonstrate the SLP architecture through an open-source prototype implementation, Schnizo, developed as an enhancement of a tiny RV32I core with floating-point support. Across several ML and HPC microkernels, Schnizo achieves substantially higher IPC and FPU utilization than the scalar baseline while retaining the efficiency of lightweight in-order designs. These results demonstrate that SLPs can provide an efficient architectural solution for programmable accelerators targeting regular, compute-intensive workloads.

## 中文摘要

为了满足现代 ML 和 HPC 工作负载的计算需求，可编程加速器集成了大量处理元件 (PE)，通常围绕单问题有序核心构建，以最大限度地提高集成密度和能效。因此，每个 PE 的指令吞吐量上限为每周期一条指令 (IPC)，通常会受到其功能单元 (FU) 严重未充分利用的影响。传统的超标量处理器可以通过增加 IPC 来提高 FU 利用率，但它们通常会产生大量的面积和能量开销。这项工作提出了超标量循环处理器 (SLP) 架构，这是一种针对常规计算密集型循环内核的轻量级超标量执行方法。我们提出了 SLP 执行模型，它利用这些工作负载的静态结构来实现高效的多问题执行，而无需复杂的动态无序调度。我们通过开源原型实现 Schnizo 演示了 SLP 架构，Schnizo 是作为具有浮点支持的微型 RV32I 内核的增强版而开发的。在多个 ML 和 HPC 微内核中，Schnizo 实现了比标量基线更高的 IPC 和 FPU 利用率，同时保留了轻量级有序设计的效率。这些结果表明，SLP 可以为针对常规计算密集型工作负载的可编程加速器提供高效的架构解决方案。

## 中文关键词

指令级并行性；超标量处理器；循环加速；可编程加速器；RISC-V

## 代码与研究制品

- 代码仓库：[https://github.com/colluca/schnizo](https://github.com/colluca/schnizo)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6A](index.md) · [MICRO 2026 主页](../index.md)
