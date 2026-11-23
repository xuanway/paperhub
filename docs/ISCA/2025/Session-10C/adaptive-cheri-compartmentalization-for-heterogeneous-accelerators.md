---
title: "Adaptive CHERI Compartmentalization for Heterogeneous Accelerators"
description: "ISCA 2025 · Session 10C · 面向异构加速器的自适应 CHERI 隔离"
tags:
  - "ISCA2025"
  - "Session 10C"
  - "Security"
---

# Adaptive CHERI Compartmentalization for Heterogeneous Accelerators

**中文标题：** 面向异构加速器的自适应 CHERI 隔离

**所属 Session：** [Session 10C](index.md) · [ISCA 2025](../index.md)

**作者：** Jianyi Cheng, A. Theodore Markettos, Alexandre Joannou, Paul Metzger, Matthew Naylor, Peter Rugg, Timothy M. Jones

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731062) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Hardware accelerators offer high performance and energy efficiency for specific tasks compared to general-purpose processors. However, current hardware accelerator designs focus primarily on perfor- mance, overlooking security. This poses significant security risks due to potential memory safety violations that can affect the entire hardware system. Existing methods either rely on Input-Output Memory Management Units (IOMMUs) for memory isolation be- tween memory pages, leading to vulnerabilities in intra-page mem- ory accesses, or modify an accelerator architecture for specialized memory protection, which requires significant effort and cannot scale across multiple diverse applications. In this paper, we propose a general method for fine-grained mem- ory protection in heterogeneous systems without modifying accel- erator architectures. We extend the Capability Hardware Enhanced RISC Instructions (CHERI) from CPUs to an adaptive hardware interface named CapChecker. The CapChecker imports capabilities from the CPU and guards memory accesses at the pointer level from CHERI-unaware accelerators as if they were CHERI-aware natively. Over a set of benchmarks on hardware accelerators in a heterogeneous system, our approach achieves fine-grained mem- ory protection, with a 1.4% performance overhead compared to CHERI-unaware accelerators on average.

## 中文摘要

相比通用处理器，硬件加速器能够为特定任务提供高性能与高能效。但当前硬件加速器设计大多优先考虑性能，忽视安全性。内存安全违规漏洞会危及整个硬件系统，由此带来严重的安全风险。现有方案要么依靠输入输出内存管理单元（IOMMU）实现页间内存隔离，无法防范页内访问漏洞；要么改造加速器架构来实现专用内存保护，开发成本高，难以适配多种不同应用。

本文提出一种面向异构系统的通用细粒度内存保护方案，**无需修改加速器本身架构**。我们将能力硬件增强RISC指令（CHERI）从CPU扩展到一个自适应硬件接口CapChecker。CapChecker从CPU接收能力指针，对不支持CHERI的加速器实施指针级内存访问管控，让这些加速器仿佛原生支持CHERI。在异构系统的加速器基准测试集上，该方案可以实现细粒度内存保护；相比不支持CHERI的加速器，平均性能开销仅1.4%。

## 英文关键词

Hardware Security, Memory Safety, Heterogeneous Systems

## 中文关键词

硬件安全, 内存安全, 异构系统

## 代码与研究制品

- [研究制品](https://zenodo.org/records/15100923)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731062)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10C](index.md) · [返回 ISCA 2025](../index.md)
