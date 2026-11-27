---
title: "Interleaved Logical Qubits in Atom Arrays"
description: "HPCA 2025 · Quantum Slots"
tags:
  - "HPCA2025"
  - "Quantum Slots"
---

# Interleaved Logical Qubits in Atom Arrays

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Quantum Slots。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Quantum Slots</p>
</div>

**论文链接**：
**作者**：Joshua Viszlai (University of Chicago), Sophia Fuhui Lin (University of Chicago), Siddharth Dangwal (University of Chicago), Conor Bradley (University of Chicago), Vikram Ramesh (University of Chicago), Jonathan Baker (University of Texas, Austin), Hannes Bernien (University of Chicago), Fred Chong (University of Chicago)
**会议**：HPCA 2025

---

## 中文标题

原子阵列中的交错逻辑量子比特

## 英文摘要

Neutral atom arrays have seen exciting progress as a platform for quantum computation. However, as we move towards the regime of fault-tolerance, the large-scale impact of fundamental features in these systems is not well-studied. In this work we point out that the use of movement in neutral atom arrays may set an unavoidable constraint on the speed of computation, erasing potential quantum advantage. As one solution, we propose a movement-free QEC architecture based on groups of interleaved surface codes. Our architecture enables fast, high-fidelity transversal CNOTs on surface codes in the same group. We also introduce interleaved lattice surgery to create high-capacity routing channels between groups. We validate our architecture through detailed numerical simulations of the underlying circuits and we evaluate its scalability through compilation of key benchmark applications. In regimes of high parallelism, we find our architecture leads to a ∼ 3× reduction in compute time. Our architecture leverages experimentally demonstrated dual-species atom arrays which exhibit asymmetric interaction strengths that scale with 1/r3 for interspecies interactions and with 1/r6 for standard, intraspecies interactions. We examine how such scalings enable interleaving with high fidelity and propose how error rates required for QEC could be achieved. We also evaluate the tolerance of our architecture to two-qubit gate fidelities. We find the advantage of interleaving admits sizable tolerances of ∼ 1× to 3× increase in error rates. We conclude the benefits of our proposed interleaved architecture grants strong motivation for future experimental efforts targeting longer range dual-species gates.

## 中文摘要

中性原子阵列作为量子计算平台已取得令人振奋的进展。然而，在迈向容错的过程中，这些系统基本特性的大规模影响尚未得到充分研究。本文指出，使用移动操作可能对计算速度造成不可避免的限制，从而抵消潜在的量子优势。为此，我们提出基于交错表面码组的无移动量子纠错（QEC）架构。我们的架构可在同一组内的表面码上实现快速、高保真的横向 CNOT。我们还引入交错格点手术，以在组之间创建高容量路由通道。我们通过对底层线路的详细数值模拟验证该架构，并通过编译关键基准应用评估其可扩展性。在高并行度情形下，我们发现该架构使计算时间减少约 3 倍。该架构利用了实验上已实现的双物种原子阵列，其种间相互作用强度随 1/r3 变化，而标准种内相互作用随 1/r6 变化。我们考察了这种标度关系如何支持高保真交错，并提出了实现 QEC 所需错误率的途径。我们还评估了对双量子比特门保真度的容忍度，发现交错可容忍约 1 倍至 3 倍的错误率上升。我们得出结论：交错架构的收益为未来更长程双物种门实验提供了强有力的动机。
