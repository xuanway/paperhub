---
title: "RESCU: Optimizing GPU Register Management for Effective Kernel Fusion"
description: "MICRO 2026 · Session 1A · RESCU：优化 GPU 寄存器管理以实现高效内核融合"
tags:
  - "MICRO2026"
  - "GPU"
  - "Register Management"
  - "Kernel Fusion"
---

# RESCU: Optimizing GPU Register Management for Effective Kernel Fusion

**中文标题：** RESCU：优化 GPU 寄存器管理以实现高效内核融合

**所属 Session：** [Session 1A](index.md) · [MICRO 2026](../index.md)

**作者：** Ruixiao Huang, Shouzhe Zhang, Weishi Shi, Hui Zhao

**来源：** MICRO 2026，pp. 82–96；[DOI](https://doi.org/10.1109/MICRO67795.2026.00022)

## 英文摘要

GPUs are widely used to accelerate emerging machine learning models, where performance is often limited by memory bandwidth. In mitigation, recent algorithmic optimizations employ kernel fusion techniques by incorporating GEMM and memory-intensive operations into a single kernel (e.g., FlashAttention). Although such optimizations can effectively reduce global memory accesses, they shift pressure to registers and create a new performance bottleneck which is generally ignored. This is because fused kernels rely heavily on registers to store intermediate values that often outnumber available registers. As a commonly used solution, register spilling is applied to selectively offload some values from registers to the next-level SRAM memory. These values are later fetched back to the registers when needed in computation. Our investigation reveals that the existing spilling mechanism is suboptimal in overcoming the register challenge raised by kernel fusion. This is due to several reasons: firstly, the selection of spilling targets causes unnecessary thrashing. Secondly, there are excessive register spills caused by cross-thread reduction that can be consolidated through near-register computing. Thirdly, unmanaged SRAM accesses from normal and spilling operations cause severe interference and bandwidth contention. In this work, we propose an architectural and compilation framework named RESCU. Through compiler optimization, RESCU selects more appropriate registers to spill so that the spilling frequency can be reduced. A novel near-register computing mechanism is developed to aggregate intermediate values across concurrent threads to decrease register usage. Furthermore, a spilling-aware scheduler is developed to coordinate accesses to SRAM between spilling and normal operations. Our evaluation results show that RESCU can improve performance by as much as 1.61× and achieve an average speedup of 1.32×.

## 中文摘要

GPU 被广泛用于加速新兴机器学习模型，但性能常受内存带宽限制。为缓解这一问题，近期算法优化采用内核融合，将 GEMM 与访存密集型操作整合进同一内核，例如 FlashAttention。虽然这能有效减少全局内存访问，却会将压力转移到寄存器，形成通常被忽视的新性能瓶颈。这是因为融合内核大量依赖寄存器保存中间值，而中间值数量经常超过可用寄存器数量。常见方案是寄存器溢出：选择部分值从寄存器卸载到下一级 SRAM，在后续计算需要时再读回。我们的研究发现，现有溢出机制难以高效应对内核融合带来的寄存器压力，原因有三。第一，溢出目标选择不当会造成不必要的反复换入换出。第二，跨线程归约引发大量寄存器溢出，而这些操作可以通过近寄存器计算合并。第三，正常操作与溢出操作缺乏协调的 SRAM 访问会产生严重干扰与带宽争用。本文提出架构与编译协同框架 RESCU。它通过编译器优化选择更合适的溢出寄存器，降低溢出频率；引入新的近寄存器计算机制，聚合并发线程间的中间值，减少寄存器使用；并设计溢出感知调度器，协调正常操作与溢出操作对 SRAM 的访问。评估表明，RESCU 最高获得 1.61 倍加速，平均加速比为 1.32。

## 中文关键词

GPU 寄存器管理；内核融合；寄存器分配；资源利用率

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1A](index.md) · [MICRO 2026 主页](../index.md)
