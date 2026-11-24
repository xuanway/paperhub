---
title: "ATX: Accelerator Task Extensions"
description: "ISCA 2026 · Session 2B · ATX: Accelerator Task Extensions"
tags:
  - "ISCA2026"
  - "Session 2B"
  - "Memory Systems and PIM/PNM"
---

# ATX: Accelerator Task Extensions

**中文标题：** ATX: 加速器任务扩展

**所属 Session：** [Session 2B](index.md) · [ISCA 2026](../index.md)

**作者：** Gerasimos Gerogiannis, Stijn Eyerman, Josep Torrellas, Wim Heirman

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Integrating accelerators in CPU multicores combines the benefits of accelerated computation with the flexibility and programmability of CPUs. CPU-integrated accelerators can be classified into In-Core Accelerators (ICAs), which typically reside inside the core’s pipeline, and Out-of-Core Accelerators (OCAs), which are typically attached at the core’s cache subsystem. Both designs have shortcomings: ICAs can be bottlenecked by the core’s general-purpose memory access interface, while OCAs’ core-accelerator interface can limit execution overlap and expose communication overheads. In this paper we introduce Near-Core Accelerators (NCAs), a new class of accelerators that aims to combine the advantages of ICAs and OCAs, and address their shortcomings. Specifically, NCAs have their own read interface to the memory system, eliminating ICAs’ bottleneck. At the same time, NCAs can be invoked speculatively and out-of-order, enabling both core-accelerator execution overlap and low-overhead core-accelerator communication. We also propose the Accelerator Task Extensions (ATX), a set of instructions and hardware extensions to support NCAs. With ATX instructions, CPU cores can speculatively invoke a diverse range of NCAs. ATX includes the Unified Transfer Engine (UTE), a programmable hardware module that efficiently supplies data to NCAs and virtualizes the interface between the CPU core and the NCAs. The UTE interfaces the CPU core with multiple NCAs and the cache subsystem, fetching and prefetching accelerator data, and scheduling tasks to potentially multiple NCAs transparently to the CPU core. We evaluate ATX NCAs with a variety of important kernels from machine learning and scientific computing. We show that ATX NCAs accelerate these kernels by 1.3–18× over various CPU-integrated accelerator alternatives.

## 中文摘要

将加速器集成到CPU多核中，兼顾了加速计算的优势与CPU的灵活性和可编程性。CPU集成加速器可分为核内加速器（ICA，通常位于核内流水线中）和核外加速器（OCA，通常挂载于核的缓存子系统）。两种设计均有不足：ICA可能受限于核的通用内存访问接口，而OCA的核-加速器接口会限制执行重叠并暴露通信开销。本文提出近核加速器（NCA），一种旨在结合ICA和OCA优点并克服其不足的新型加速器。NCA拥有独立的存储系统读取接口，消除了ICA的瓶颈；同时可被推测性乱序调用，实现核与加速器的执行重叠与低开销通信。我们还提出了加速器任务扩展（ATX），一套支持NCA的指令和硬件扩展。通过ATX指令，CPU核可推测性调用多种NCA。ATX包含统一传输引擎（UTE），这是一个可编程硬件模块，可高效地向NCA提供数据并虚拟化CPU核与NCA之间的接口。UTE将CPU核与多个NCA及缓存子系统连接，获取和预取加速器数据，并透明地向多个NCA调度任务。我们使用机器学习和科学计算中的多种重要内核评估了ATX NCA，结果表明ATX NCA相比各种CPU集成加速器方案可将这些内核加速1.3–18×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2B](index.md) · [返回 ISCA 2026](../index.md)
