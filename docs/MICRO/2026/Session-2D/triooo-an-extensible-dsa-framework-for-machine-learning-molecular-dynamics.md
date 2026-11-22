---
title: "TriOoO: An Extensible DSA Framework for Machine Learning Molecular Dynamics"
description: "MICRO 2026 · Session 2D · TriOoO：面向机器学习分子动力学的可扩展领域专用架构框架"
tags:
  - "MICRO2026"
---

# TriOoO: An Extensible DSA Framework for Machine Learning Molecular Dynamics

**中文标题：** TriOoO：面向机器学习分子动力学的可扩展领域专用架构框架

**所属 Session：** [Session 2D](index.md) · [MICRO 2026](../index.md)

**作者：** Zihan Yan, Ning Kang, Guojun Yuan, Yewen Li, YuanZhe Wang, Hao Zhang, Yachao Zhang, Guanglei Chen, Zejun Li, Zhan Wang, Dingwen Tao, Ninghui Sun, Guangming Tan

**来源：** MICRO 2026，pp. 770–786；[DOI](https://doi.org/10.1109/MICRO67795.2026.00065)

## 英文摘要

Machine Learning Molecular Dynamics (MLMD) merges the accuracy of ab initio methods with the efficiency of classical molecular dynamics. However, existing MLMD accelerators suffer from limited generality and scalability, as they are tightly coupled to specific MLMD implementations, support only a limited set of atom types, and depend heavily on on-chip SRAM resources. As a result, their applicability to complex systems, such as drug molecules and multi-component alloys, remains restricted. In this paper, we propose TriOoO, a decoupled and memory-efficient framework for scalable MLMD acceleration. First, TriOoO builds a decoupled datapath that separates reusable computation from implementation-specific logic, enabling support for different MLMD implementations within a unified framework. Second, to extend this framework to multi-type systems, TriOoO further introduces a locality-aware hierarchical storage pipeline that places hotspot and non-hotspot data across different memory levels. Third, on top of this hierarchy, TriOoO employs a triple out-of-order scheduling mechanism to hide off-chip access latency and reduce on-chip buffering overhead. Experiments show that our FPGA prototype and ASIC simulations reach 6.70–97.23 µs/day across different MLMD implementations, demonstrating speedups of 3.16×–603× over the state-of-the-art solutions.

## 中文摘要

机器学习分子动力学 (MLMD) 将从头计算方法的准确性与经典分子动力学的效率相结合。然而，现有的 MLMD 加速器的通用性和可扩展性有限，因为它们与特定的 MLMD 实现紧密耦合，仅支持有限的原子类型集，并且严重依赖片上 SRAM 资源。因此，它们在药物分子和多组分合金等复杂系统中的适用性仍然受到限制。在本文中，我们提出了 TriOoO，一种用于可扩展 MLMD 加速的解耦且内存高效的框架。首先，TriOoO 构建了一个解耦的数据路径，将可重用计算与特定于实现的逻辑分开，从而能够在统一框架内支持不同的 MLMD 实现。其次，为了将该框架扩展到多类型系统，TriOoO 进一步引入了局部感知分层存储管道，将热点和非热点数据放置在不同的内存级别上。第三，在此层次结构之上，TriOoO 采用三重乱序调度机制来隐藏片外访问时延并减少片上缓冲开销。实验表明，我们的 FPGA 原型和 ASIC 仿真在不同的 MLMD 实现中达到了 6.70–97.23 µs/天，与最先进的解决方案相比，速度提高了 3.16×–603×。

## 中文关键词

分子动力学；计算科学；加速器；领域专用架构

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/yyyyyyyyzh/TriOoO](https://github.com/yyyyyyyyzh/TriOoO)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2D](index.md) · [MICRO 2026 主页](../index.md)
