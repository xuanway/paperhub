---
title: "NAQsim: Full-Stack Architecture Simulation Framework for Fast and Space-Efficient Neutral Atom Quantum Computing"
description: "MICRO 2026 · Session 3D · NAQsim：面向快速且空间高效的中性原子量子计算的全栈架构仿真框架"
tags:
  - "MICRO2026"
  - "Quantum Computing"
  - "Simulation"
---

# NAQsim: Full-Stack Architecture Simulation Framework for Fast and Space-Efficient Neutral Atom Quantum Computing

**中文标题：** NAQsim：面向快速且空间高效的中性原子量子计算的全栈架构仿真框架

**所属 Session：** [Session 3D](index.md) · [MICRO 2026](../index.md)

**作者：** Yosuke Ueno, Shinichi Sunami, Toshihide Hinokuma, Yasunari Suzuki, Akihisa Goban, Hayata Yamasaki, Teruo Tanimoto, Ilkwon Byun

**来源：** MICRO 2026，pp. 1196–1213；[DOI](https://doi.org/10.1109/MICRO67795.2026.00092)

## 英文摘要

Technological advances in neutral-atom platforms have opened a new path toward designing efficient protocols for fault-tolerant quantum computing (FTQC). However, each physical operation is still orders of magnitude slower than on other platforms, such as superconducting qubits. Therefore, architects must identify fast and efficient FTQC architectures, which require reliable modeling tools to explore various design choices across the software, classical hardware, and quantum device stacks of neutral-atom platforms. In this paper, we propose NAQsim, an open-source simulation framework for neutral-atom FTQC architectures based on transversal gates. As its key feature, NAQsim enables detailed full-stack architecture evaluation that opens opportunities to explore previously overlooked performance bottlenecks. As a first use case for NAQsim, we identify one such bottleneck, patch rotations, perform full-stack co-optimization, and finally derive a near-rotation-free architecture (D3-ROT). For practical FTQC benchmark workloads, D3-ROT achieves a 2.27× speedup from this single bottleneck alone, with minimal footprint overhead. These results point to a much broader space of full-stack optimizations that NAQsim makes accessible for transversal surface-code architectures and beyond.

## 中文摘要

中性原子平台的技术进步为设计高效的容错量子计算（FTQC）协议开辟了一条新途径。然而，每个物理操作仍然比其他平台（例如超导量子位）慢几个数量级。因此，架构师必须确定快速高效的 FTQC 架构，这需要可靠的建模工具来探索跨软件、经典硬件和中性原子平台的量子设备堆栈的各种设计选择。在本文中，我们提出了 NAQsim，这是一种基于横向门的中性原子 FTQC 架构的开源模拟框架。作为其关键功能，NAQsim 能够进行详细的全栈架构评估，为探索以前被忽视的性能瓶颈提供了机会。作为 NAQsim 的第一个用例，我们确定了一个这样的瓶颈：补丁轮换，执行全栈协同优化，并最终推导出近乎无轮换的架构 (D3-ROT)。对于实际的 FTQC 基准工作负载，D3-ROT 仅从这个单一瓶颈就实现了 2.27 倍的加速，并且占用空间最小。这些结果表明 NAQsim 可以为横向表面码架构及其他架构提供更广阔的全栈优化空间。

## 中文关键词

容错量子计算；中性原子量子计算；表面码；横向门；建模与仿真

## 代码与研究制品

- 代码仓库：[https://github.com/naqsim/naqsim](https://github.com/naqsim/naqsim)
- 研究制品归档：[https://doi.org/10.5281/zenodo.22684078](https://doi.org/10.5281/zenodo.22684078)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3D](index.md) · [MICRO 2026 主页](../index.md)
