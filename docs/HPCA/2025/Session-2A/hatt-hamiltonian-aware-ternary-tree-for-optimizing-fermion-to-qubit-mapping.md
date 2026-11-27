---
title: "HATT: Hamiltonian Aware Ternary Tree for Optimizing Fermion-to-Qubit Mapping"
description: "HPCA 2025 · Quantum Slots"
tags:
  - "HPCA2025"
  - "Quantum Slots"
---

# HATT: Hamiltonian Aware Ternary Tree for Optimizing Fermion-to-Qubit Mapping

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Quantum Slots。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Quantum Slots</p>
</div>

**论文链接**：
**作者**：Yuhao Liu (University of Pennsylvania), Kevin Yao (University of Pennsylvania), Jonathan Hong (University of Pennsylvania), Julien Froustey (University of California, Berkeley), Yunong Shi (AWS Quantum Technologies), Ermal Rrapaj (Lawrance Berkeley National Lab), Costin Iancu (Lawrance Berkeley National Lab), Gushu Li (University of Pennsylvania)
**会议**：HPCA 2025

---

## 中文标题

HATT：用于优化费米子-量子比特映射的哈密顿量感知三叉树

## 英文摘要

This paper introduces the Hamiltonian-Adaptive Ternary Tree (HATT) framework to compile optimized Fermion-to-qubit mapping for specific Fermionic Hamiltonians. In the simulation of Fermionic quantum systems, efficient Fermion-to-qubit mapping plays a critical role in transforming the Fermionic system into a qubit system. HATT utilizes ternary tree mapping and a bottom-up construction procedure to generate Hamiltonian aware Fermion-to-qubit mapping to reduce the Pauli weight of the qubit Hamiltonian, resulting in lower quantum simulation circuit overhead. Additionally, our optimizations retain the important vacuum state preservation property in our Fermion-to-qubit mapping and reduce the complexity of our algorithm from O(N4) to O(N3). Evaluations on various Fermionic systems demonstrate 5 ∼ 25% reduction in Pauli weight, gate count, and circuit depth, alongside excellent scalability to larger systems. Experiments on the Ionq device also show the advantages of HATT in noise resistance in quantum simulations.

## 中文摘要

本文提出哈密顿量自适应三叉树（HATT）框架，用于为特定的费米子哈密顿量编译优化的费米子-量子比特映射。在费米子量子系统模拟中，高效的费米子-量子比特映射对将费米子系统转换为量子比特系统至关重要。HATT 利用三叉树映射与自底向上的构造过程，生成哈密顿量感知的费米子-量子比特映射，以降低量子比特哈密顿量的泡利权重，从而减少量子模拟的线路开销。此外，我们的优化在映射中保留了重要的真空态保持特性，并将算法复杂度从 O(N4) 降至 O(N3)。在多种费米子系统上的评估显示，泡利权重、门数与线路深度降低 5∼25%，并且对更大系统具有出色的可扩展性。在 Ionq 器件上的实验也显示了 HATT 在量子模拟中抗噪声方面的优势。
