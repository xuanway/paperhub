---
title: "Genesis: A Compiler for Hamiltonian Simulation on Hybrid CV-DV Quantum Computers"
description: "ISCA 2025 · Session 8B · Genesis: 混合CV-DV量子计算机的Hamiltonian模拟编译器"
tags:
  - "ISCA2025"
  - "Session 8B"
  - "Quantum III"
---

# Genesis: A Compiler for Hamiltonian Simulation on Hybrid CV-DV Quantum Computers

**中文标题：** Genesis: 混合CV-DV量子计算机的Hamiltonian模拟编译器

**所属 Session：** [Session 8B](index.md) · [ISCA 2025](../index.md)

**作者：** Zihan Chen, Jiakang Li, Minghao Guo, Henry Chen, Zirui Li, Joel Bierman, Yipeng Huang, Huiyang Zhou, Yuan Liu, Eddy Z. Zhang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731065) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

This paper introduces Genesis, the first compiler designed to sup- port Hamiltonian Simulation on hybrid continuous-variable (CV) and discrete-variable (DV) quantum computing systems. Genesis is a two-level compilation system. At the first level, it decomposes an input Hamiltonian into basis gates using the native instruction set of the target hybrid CV-DV quantum computer. At the second level, it tackles the mapping and routing of qumodes/qubits to implement long-range interactions for the gates decomposed from the first level. Rather than a typical implementation that relies on SWAP primitives similar to qubit-based (or DV-only) systems, we pro- pose an integrated design of connectivity-aware gate synthesis and beamsplitter SWAP insertion tailored for hybrid CV-DV systems. We also introduce an OpenQASM-like domain-specific language (DSL) named CVDV-QASM to represent Hamiltonian in terms of Pauli-exponentials and basic gate sequences from the hybrid CV- DV gate set. Genesis has successfully compiled several important Hamiltonians, including the Bose-Hubbard model, Z2−Higgs model, Hubbard-Holstein model, Heisenberg model and Electron-vibration coupling Hamiltonians, which are critical in domains like quan- tum field theory, condensed matter physics, and quantum chem- istry. Our implementation is available at Genesis-CVDV-Compiler[https://github.com/ruadapt/Genesis-CVDV-Compiler](https://github.com/ruadapt/Genesis-CVDV-Compiler).

## 中文摘要

本文介绍Genesis，首款面向连续变量（CV）-离散变量（DV）混合量子计算系统、支持哈密顿量模拟的编译器。Genesis是一套两级编译系统：第一级，它依托目标CV-DV混合量子计算机的原生指令集，将输入哈密顿量分解为基门；第二级，完成量子模式（qumode）与量子比特的映射和布线，实现第一级分解所得门所需的长程相互作用。
不同于纯量子比特（仅DV）系统里依赖SWAP原语的常规实现，本文面向CV-DV混合系统，设计了感知连接拓扑的门合成与分束器SWAP插入一体化方案。
同时，本文提出一种类似OpenQASM的领域专用语言CVDV-QASM，可基于泡利指数形式与CV-DV混合门集合的基础门序列来描述哈密顿量。
Genesis已成功编译多个重要哈密顿量，包括玻色-哈伯德模型、Z₂-希格斯模型、哈伯德-霍尔斯坦模型、海森堡模型以及电子-振动耦合哈密顿量，这些模型在量子场论、凝聚态物理、量子化学等领域至关重要。项目开源地址：https://github.com/ruadapt/Genesis-CVDV-Compiler

## 英文关键词

Quantum Computing, Hamiltonian Simulation, Hybrid CV-DV, Quantum Architecture, Compiler

## 中文关键词

量子计算, 哈密顿量模拟, 连续变量-离散变量混合, 量子架构, 编译器

## 代码与研究制品

- [代码仓库](https://github.com/ruadapt/Genesis-CVDV-Compiler)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731065)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8B](index.md) · [返回 ISCA 2025](../index.md)
