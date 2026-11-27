---
title: "Reuse-Aware Compilation for Zoned Quantum Architectures Based on Neutral Atoms"
description: "HPCA 2025 · Quantum Slots"
tags:
  - "HPCA2025"
  - "Quantum Slots"
---

# Reuse-Aware Compilation for Zoned Quantum Architectures Based on Neutral Atoms

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Quantum Slots。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Quantum Slots</p>
</div>

**论文链接**：
**作者**：Wan-Hsuan Lin (UCLA), Daniel Bochen Tan (UCLA), Jason Cong (UCLA)
**会议**：HPCA 2025

---

## 中文标题

面向基于中性原子的分区量子架构的复用感知编译

## 英文摘要

Quantum computing architectures based on neutral atoms offer large scales and high-fidelity operations. They can be heterogeneous, with different zones for storage, entangling operations, and readout. Zoned architectures improve computation fidelity by shielding idling qubits in storage from side-effect noise, unlike monolithic architectures where all operations occur in a single zone. However, supporting these flexible architectures with efficient compilation remains challenging. In this paper, we propose ZAC, a scalable compiler for zoned architectures. ZAC minimizes data movement overhead between zones with qubit reuse, i.e., keeping them in the entanglement zone if an immediate entangling operation is pending. Other innovations include novel data placement and instruction scheduling strategies in ZAC, a flexible specification of zoned architectures, and an intermediate representation for zoned architectures, ZAIR. Our evaluation shows that zoned architectures equipped with ZAC achieve a 22x improvement in fidelity compared to monolithic architectures. Moreover, ZAC is shown to have a 10% fidelity gap on average compared to the ideal solution. This significant performance enhancement enables more efficient and reliable quantum circuit execution, enabling advancements in quantum algorithms and applications. ZAC is open source at https://github.com/UCLA-VAST/ZAC

## 中文摘要

基于中性原子的量子计算架构可提供大规模与高保真度的操作。它们可以是异构的，为存储、纠缠操作与读出设置不同的分区。与所有操作都在单一分区内进行的单片架构不同，分区架构通过将空闲量子比特屏蔽在存储区、使其免受副作用噪声影响，从而提升计算保真度。然而，用高效的编译来支持这些灵活的架构仍然具有挑战性。本文提出 ZAC，一个面向分区架构的可扩展编译器。ZAC 通过量子比特复用最小化分区之间的数据移动开销，即若紧接着有纠缠操作待执行，就将量子比特保留在纠缠区。其他创新包括 ZAC 中新颖的数据放置与指令调度策略、对分区架构的灵活描述，以及面向分区架构的中间表示 ZAIR。我们的评估表明，配备 ZAC 的分区架构相比单片架构可将保真度提升 22 倍。此外，ZAC 与理想方案相比平均仅有 10% 的保真度差距。这一显著的性能提升使量子电路执行更加高效可靠，并推动量子算法与应用的发展。ZAC 已在 https://github.com/UCLA-VAST/ZAC 开源。
