---
title: "The Configuration Wall: Characterization and Elimination of Accelerator Configuration Overhead"
description: "ASPLOS 2026 · Session 8D · 配置墙：加速器配置开销的表征与消除"
tags:
  - "ASPLOS2026"
  - "Session 8D"
  - "Reconfigurable Architectures"
---

# The Configuration Wall: Characterization and Elimination of Accelerator Configuration Overhead

**中文标题：** 配置墙：加速器配置开销的表征与消除

**所属 Session：** [Session 8D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Josse Van Delm (KU Leuven), Anton Lydike (The University of Edinburgh), Joren Dumoulin (KU Leuven), Jonas Crols (KU Leuven), Xiaoling Yi (KU Leuven), Ryan Antonio (KU Leuven), Jackson Woodruff (The University of Edinburgh), Tobias Grosser (University of Cambridge), Marian Verhelst (KU Leuven)

**单位：** KU Leuven；The University of Edinburgh；University of Cambridge

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762225) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Contemporary compute platforms increasingly offload compute kernels from CPU to integrated hardware accelerators to reach maximum performance per Watt. Unfortunately, the time the CPU spends on setup control and synchronization has increased with growing accelerator complexity. For systems with complex accelerators, this means that performance can be configuration-bound. Faster accelerators are more severely impacted by this overlooked performance drop, which we call the configuration wall. Prior work evidences this wall and proposes ad-hoc solutions to reduce configuration overhead. However, these solutions are not universally applicable, nor do they offer comprehensive insights into the underlying causes of performance degradation. In this work, we first introduce a widely-applicable variant of the well-known roofline model to quantify when system performance is configuration-bound. To move systems out of the performance-bound region, we subsequently propose a domain-specific compiler abstraction and associated optimization passes. We implement the abstraction and passes in the MLIR compiler framework to run optimized binaries on open-source architectures to prove its effectiveness and generality. Experiments demonstrate a geomean performance boost of 2x on the open-source OpenGeMM system, by eliminating redundant configuration cycles and by automatically Our work provides key insights in how accelerator performance is affected by setup mechanisms, thereby facilitating automatic code generation for circumventing the configuration wall.

## 中文摘要

当代计算平台越来越多地把计算内核从 CPU 卸载到集成硬件加速器上，以达到每瓦最大性能。不幸的是，随着加速器复杂度不断提高，CPU 花在建立控制与同步上的时间也增加了。对于带有复杂加速器的系统，这意味着性能可能受配置限制（configuration-bound）。更快的加速器受这一被忽视的性能下降影响更为严重，我们将其称为配置墙。已有工作证实了这堵墙的存在，并提出了减少配置开销的临时性方案。然而，这些方案并非普遍适用，也未能对性能退化的根本原因提供全面的洞见。在本工作中，我们首先引入著名 roofline 模型的一个广泛适用的变体，用以量化系统性能何时受配置限制。为使系统脱离性能受限区域，我们随后提出一种领域专用编译器抽象及相关的优化遍（optimization passes）。我们在 MLIR 编译器框架中实现该抽象与这些优化遍，以在开源体系结构上运行优化后的二进制文件，从而证明其有效性与通用性。实验表明，通过消除冗余配置周期以及通过自动地，在开源 OpenGeMM 系统上实现了 2 倍的几何平均性能提升。我们的工作就加速器性能如何受建立机制（setup mechanisms）影响提供了关键洞见，从而有助于通过自动代码生成来规避配置墙。

## 英文关键词

Roofline Model, Configuration, Accelerators, Compilers, MLIR

## 中文关键词

Roofline 模型；配置；加速器；编译器；MLIR

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762225)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8D](index.md) · [返回 ASPLOS 2026](../index.md)
