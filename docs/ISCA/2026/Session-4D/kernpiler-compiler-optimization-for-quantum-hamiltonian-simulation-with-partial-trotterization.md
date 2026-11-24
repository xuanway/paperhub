---
title: "Kernpiler: Compiler Optimization for Quantum Hamiltonian Simulation with Partial Trotterization"
description: "ISCA 2026 · Session 4D · Kernpiler: Compiler Optimization for Quantum Hamiltonian Simulation with Partial Trotterization"
tags:
  - "ISCA2026"
  - "Session 4D"
  - "Quantum 1"
---

# Kernpiler: Compiler Optimization for Quantum Hamiltonian Simulation with Partial Trotterization

**中文标题：** Kernpiler: 面向部分 Trotter 化量子哈密顿量模拟的编译器优化

**所属 Session：** [Session 4D](index.md) · [ISCA 2026](../index.md)

**作者：** Ethan Decker, Lucas Goetz, Evan McKinney, Erik Gustafson, Junyu Zhou, Yuhao Liu, Alex K. Jones, Ang Li, Alexander Schuckert, Samuel Stein, Eleanor Crane, Gushu Li

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Quantum computing promises transformative impacts in simulating Hamiltonian dynamics, essential for studying physical systems inaccessible by classical computing. However, existing compilation techniques for Hamiltonian simulation — in particular the commonly used Trotter formulas — struggle to provide gate counts feasible on current quantum computers for beyond-classical simulations. We propose partial Trotterization, where sets of non-commuting Hamiltonian terms are directly compiled allowing for less error per Trotter step and therefore a reduction of Trotter steps overall. Furthermore, a suite of novel optimizations are introduced which complement the new partial Trotterization technique, including reinforcement learning for complex unitary decompositions and high level Hamiltonian analysis for unitary reduction. We demonstrate with numerical simulations across spin and fermionic Hamiltonians that compared to state of the art methods such as Qiskit’s Rustiq and Qiskit’s Paulievolutiongate, our novel compiler presents up to 10× gate and depth count reductions.


## 中文摘要

量子计算有望在模拟哈密顿量动力学方面带来变革性影响，这对研究经典计算无法企及的物理系统至关重要。然而，现有的哈密顿量模拟编译技术——尤其是常用的 Trotter 公式——难以为超越经典规模的模拟提供在当前量子计算机上可行的门数。我们提出部分 Trotter 化（partial Trotterization），即对非对易哈密顿量项集合直接编译，从而降低每个 Trotter 步的误差，进而减少总体 Trotter 步数。此外，我们引入一套新颖的优化来补充新的部分 Trotter 化技术，包括用于复杂酉分解的强化学习和用于酉约简的高层哈密顿量分析。我们通过自旋和费米子哈密顿量上的数值模拟表明，相比 Qiskit 的 Rustiq 和 Qiskit 的 Paulievolutiongate 等最先进方法，我们的新型编译器可实现最高 10× 的门数和深度降低。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [实验材料归档（Zenodo 19446464）](https://zenodo.org/records/19446464)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4D](index.md) · [返回 ISCA 2026](../index.md)
