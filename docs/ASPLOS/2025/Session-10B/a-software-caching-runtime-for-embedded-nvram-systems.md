---
title: "A Software Caching Runtime for Embedded NVRAM Systems"
description: "ASPLOS 2025 · Session 10B · 面向嵌入式 NVRAM 系统的软件缓存运行时"
tags:
  - "ASPLOS2025"
  - "Session 10B"
  - "Solid State Storage"
---

# A Software Caching Runtime for Embedded NVRAM Systems

**中文标题：** 面向嵌入式 NVRAM 系统的软件缓存运行时

**所属 Session：** [Session 10B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Harrison Williams (Virginia Tech), Matthew Hicks (Virginia Tech)

**单位：** Virginia Tech

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674183) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Increasingly sophisticated low-power microcontrollers are at the heart of millions of IoT and edge computing deployments, with developers pushing large-scale data collection, processing, and inference to end nodes. Advanced workloads on resource-constrained systems depend on emerging technologies to meet performance and lifetime demands. High-performance Non-Volatile RAMs (NVRAMs) are one such technology enabling a new class of systems previously made impossible by memory limitations, including ultralow-power designs using program state non-volatility and sensing systems storing and processing large blocks of data. Unfortunately, existing NVRAM significantly underperforms SRAM's access latency/energy cost and flash's read performance—condemning systems dependent on NVRAM to pay a steep energy and time penalty for software execution. We observe that this performance penalty stems predominately from instruction fetches into NVRAM, which represent >75% of memory accesses in typical embedded software. To eliminate this performance bottleneck, we propose SwapRAM, a new operating model for NVRAM-based platforms which repurposes underutilized SRAM as an instruction cache, maximizing the proportion of accesses directed towards higher-performance SRAM. SwapRAM consists of a set of compile-time code transformations and a runtime management system that transparently and dynamically copies code into SRAM throughout execution, with an extensible logic to delay eviction of hot code. Across nine embedded benchmarks running on a real FRAM platform, SwapRAM's software-based design increases execution speed by up to 46% (average 26%) and reduces energy consumption by up to 36% (average 24%) compared to a baseline system using the existing hardware cache.

## 中文摘要

日益复杂的低功耗微控制器是数以百万计的物联网与边缘计算部署的核心，开发者正将大规模数据采集、处理与推理推向终端节点。资源受限系统上的高级工作负载依赖新兴技术来满足性能与寿命需求。高性能非易失性 RAM（NVRAM）正是这样一种技术，它使一类此前因内存限制而无法实现的系统成为可能，包括利用程序状态非易失性的超低功耗设计，以及存储并处理大块数据的感知系统。不幸的是，现有 NVRAM 在访问延迟/能耗方面显著逊于 SRAM，在读性能方面逊于 flash——这使得依赖 NVRAM 的系统不得不为软件执行付出高昂的能耗与时间代价。我们观察到，这一性能代价主要源于对 NVRAM 的取指，在典型嵌入式软件中这类访问占内存访问的 75% 以上。为消除该性能瓶颈，我们提出了 SwapRAM，一种面向基于 NVRAM 的平台的新运行模型，它将未被充分利用的 SRAM 重新用作指令缓存，从而最大化指向更高性能 SRAM 的访问比例。SwapRAM 由一组编译时代码变换和一个运行时管理系统组成，后者在整个执行过程中透明且动态地将代码复制到 SRAM，并具备可扩展的逻辑来延迟热代码的驱逐。在真实 FRAM 平台上运行的九个嵌入式基准测试中，与使用现有硬件缓存的基线系统相比，SwapRAM 的基于软件的设计将执行速度最高提升 46%（平均 26%），并将能耗最高降低 36%（平均 24%）。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674183)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10B](index.md) · [返回 ASPLOS 2025](../index.md)
