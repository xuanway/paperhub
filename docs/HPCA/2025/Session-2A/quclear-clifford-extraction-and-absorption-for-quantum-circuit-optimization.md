---
title: "QuCLEAR: Clifford Extraction and Absorption for Quantum Circuit Optimization"
description: "HPCA 2025 · Quantum Slots"
tags:
  - "HPCA2025"
  - "Quantum Slots"
---

# QuCLEAR: Clifford Extraction and Absorption for Quantum Circuit Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Quantum Slots。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Quantum Slots</p>
</div>

**论文链接**：
**作者**：Ji Liu (Argonne National Laboratory), Alvin Gonzales (Argonne National Laboratory), Benchen Huang (University of Chicago), Zain H Saleem (Argonne National Laboratory), Paul Hovland (Argonne National Laboratory)
**会议**：HPCA 2025

---

## 中文标题

QuCLEAR：面向量子电路优化的 Clifford 提取与吸收

## 英文摘要

Quantum computing carries significant potential for addressing practical problems. However, currently available quantum devices suffer from noisy quantum gates, which degrade the fidelity of executed quantum circuits. Therefore, quantum circuit optimization is crucial for obtaining useful results. In this paper, we present QuCLEAR, a compilation framework designed to optimize quantum circuits. QuCLEAR significantly reduces both the two-qubit gate count and the circuit depth through two novel optimization steps. First, we introduce the concept of Clifford Extraction, which extracts Clifford subcircuits to the end of the circuit while optimizing the gates. Second, since Clifford circuits are classically simulatable, we propose Clifford Absorption, which efficiently processes the extracted Clifford subcircuits classically. We demonstrate our framework on quantum simulation circuits, which have wide-ranging applications in quantum chemistry simulation, many-body physics, and combinatorial optimization problems. Near-term algorithms such as VQE and QAOA also fall within this category. Experimental results across various benchmarks show that QuCLEAR achieves up to a 77.7% reduction in CNOT gate count and up to an 84.1% reduction in entangling depth compared with state-of-the-art methods.

## 中文摘要

量子计算在解决实际问题方面具有巨大潜力。然而，当前可用的量子设备受制于含噪声的量子门，会降低所执行量子电路的保真度。因此，量子电路优化对于获得有用的结果至关重要。本文提出 QuCLEAR，一个专为优化量子电路而设计的编译框架。QuCLEAR 通过两个新颖的优化步骤显著降低了双量子比特门数量与电路深度。首先，我们引入 Clifford 提取（Clifford Extraction）的概念，在优化门的同时将 Clifford 子电路提取到电路末端。其次，由于 Clifford 电路可在经典计算机上模拟，我们提出 Clifford 吸收（Clifford Absorption），以经典方式高效处理被提取出的 Clifford 子电路。我们在量子模拟电路上展示了该框架，此类电路在量子化学模拟、多体物理与组合优化问题中具有广泛应用。VQE、QAOA 等近期算法也属于这一范畴。跨多个基准的实验结果表明，与最先进方法相比，QuCLEAR 最高可将 CNOT 门数量减少 77.7%，并将纠缠深度最多减少 84.1%。
