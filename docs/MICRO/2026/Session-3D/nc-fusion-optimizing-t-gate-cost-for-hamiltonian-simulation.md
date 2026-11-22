---
title: "NC-Fusion: Optimizing T-Gate Cost for Hamiltonian Simulation"
description: "MICRO 2026 · Session 3D · NC-Fusion：优化哈密顿量模拟中的 T 门成本"
tags:
  - "MICRO2026"
  - "Quantum Computing"
  - "Simulation"
---

# NC-Fusion: Optimizing T-Gate Cost for Hamiltonian Simulation

**中文标题：** NC-Fusion：优化哈密顿量模拟中的 T 门成本

**所属 Session：** [Session 3D](index.md) · [MICRO 2026](../index.md)

**作者：** Yingheng Li, Xulong Tang, Paul Hovland, Ji Liu

**来源：** MICRO 2026，pp. 1233–1250；[DOI](https://doi.org/10.1109/MICRO67795.2026.00094)

## 英文摘要

Hamiltonian simulation is a key quantum algorithm for modeling complex systems. It is typically decomposed into a set of Pauli strings, each implemented as a Pauli Product Rotation (PPR), corresponding to an RZ rotation with surrounding Clifford gates. In fault-tolerant quantum computers, these RZ gates are synthesized into sequences of Clifford and T gates, where the T-gate count and T-gate depth are critical metrics. In this paper, we propose a compilation framework that reduces both the T-gate count and T-gate depth for Hamiltonian simulation through merging PPRs. Our approach partitions Pauli strings into groups and applies Clifford conjugation to map each group to operators acting on a small subset of qubits. This enables the PPRs within a group to be merged and synthesized as a single unitary under Clifford conjugation, reducing both T-gate count and depth. Experimental results show average reductions of 57.5%, 33.7%, and 45.0% in T-gate count, T-gate depth, and Clifford count, respectively, compared to the state-of-the-art Hamiltonian simulation compilation framework Phoenix.

## 中文摘要

哈密顿模拟是复杂系统建模的关键量子算法。它通常被分解为一组泡利弦，每个泡利弦都实现为泡利乘积旋转（PPR），对应于周围克利福德门的 RZ 旋转。在容错量子计算机中，这些 RZ 门被合成为 Clifford 门和 T 门序列，其中 T 门数量和 T 门深度是关键指标。在本文中，我们提出了一种编译框架，通过合并 PPR 来减少哈密顿模拟的 T 门数量和 T 门深度。我们的方法将泡利串划分为组，并应用 Clifford 共轭将每个组映射到作用于一小部分量子位的运算符。这使得组内的 PPR 能够在 Clifford 共轭下合并和合成为单个单一单元，从而减少 T 门数量和深度。实验结果表明，与最先进的哈密顿模拟编译框架 Phoenix 相比，T 门数量、T 门深度和 Clifford 数量平均分别减少了 57.5%、33.7% 和 45.0%。

## 中文关键词

哈密顿量模拟；量子编译；容错量子计算；酉算子综合；T 门数量优化

## 代码与研究制品

- 代码仓库：[https://github.com/PittYHL/NC-Fusion](https://github.com/PittYHL/NC-Fusion)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21545197](https://doi.org/10.5281/zenodo.21545197)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3D](index.md) · [MICRO 2026 主页](../index.md)
