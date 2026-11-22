---
title: "GadIR: A Spatial-Topology Preserving Compiler for Quantum Many-Body Systems Simulation"
description: "MICRO 2026 · Session 3D · GadIR：面向量子多体系统仿真的空间拓扑保持编译器"
tags:
  - "MICRO2026"
  - "Quantum Computing"
  - "Simulation"
  - "Compiler"
---

# GadIR: A Spatial-Topology Preserving Compiler for Quantum Many-Body Systems Simulation

**中文标题：** GadIR：面向量子多体系统仿真的空间拓扑保持编译器

**所属 Session：** [Session 3D](index.md) · [MICRO 2026](../index.md)

**作者：** Xiangyu Ren, Yuexun Huang, Zhaohui Yang, Yuchen Zhu, Tsung-Wei Huang, Tsung-Yi Ho, Zhiding Liang, Antonio Barbalace

**来源：** MICRO 2026，pp. 1214–1232；[DOI](https://doi.org/10.1109/MICRO67795.2026.00093)

## 英文摘要

Simulating quantum many-body systems has been one of the most important applications of quantum computation. For simulation, the Hamiltonian of a physical system is compiled into quantum programs with native instructions for quantum hardware. In previous works, the Hamiltonian is represented as Pauli strings, then compiled and optimized based on the quantum circuit model. Such representation paradigm neglects the spatial topology of original physical models, which is vital information to reducing the overhead of compiling many-body systems Hamiltonians. To address such neglect, we introduce a spatial-topology preserving compiler for quantum many-body simulation. Using Pauli gadgets as the representations of the Hamiltonian, we introduce our intermediate representation – GadIR, to preserve the spatial-topology information of original physical models. Our compiler frontend performs the group reduction algorithm based on Pauli gadget model, which is a hardware-independent optimization. Our compiler backend performs trotterization and scheduling on Pauli gadgets, then synthesizes the Pauli gadgets into hardware-native quantum programs. We evaluate our compiler on all the canonical quantum many-body system models, while achieving a significant reduction on compilation overhead regarding four major quantum architectures. Overall, our spatial-topology preserving IR exploits the compilation optimization space for quantum many-body systems Hamiltonian.

## 中文摘要

模拟量子多体系统一直是量子计算最重要的应用之一。为了进行模拟，物理系统的哈密顿量被编译成具有量子硬件本机指令的量子程序。在之前的工作中，哈密顿量被表示为泡利弦，然后基于量子电路模型进行编译和优化。这种表示范式忽略了原始物理模型的空间拓扑，这对于减少编译多体系统哈密顿量的开销是至关重要的信息。为了解决这种忽视问题，我们引入了一种用于量子多体模拟的空间拓扑保留编译器。使用泡利小工具作为哈密顿量的表示，我们引入了我们的中间表示 - GadIR，以保留原始物理模型的空间拓扑信息。我们的编译器前端执行基于 Pauli gadget 模型的组缩减算法，这是一种独立于硬件的优化。我们的编译器后端对 Pauli gadget 执行 trotterization 和调度，然后将 Pauli gadget 合成为硬件本机量子程序。我们在所有规范量子多体系统模型上评估我们的编译器，同时显着减少四种主要量子架构的编译开销。总体而言，我们的空间拓扑保留 IR 利用了量子多体系统哈密顿量的编译优化空间。

## 中文关键词

量子计算；量子编译；量子编程语言；多体系统；空间拓扑

## 代码与研究制品

- 代码仓库：[https://github.com/xiyurain/GadIR](https://github.com/xiyurain/GadIR)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21550065](https://doi.org/10.5281/zenodo.21550065)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3D](index.md) · [MICRO 2026 主页](../index.md)
