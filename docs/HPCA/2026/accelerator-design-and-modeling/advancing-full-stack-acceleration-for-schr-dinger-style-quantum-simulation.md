---
title: "Advancing Full-stack Acceleration for Schrödinger-Style Quantum Simulation"
description: "HPCA 2026 · Accelerator Design and Modeling"
tags:
  - "HPCA2026"
  - "Accelerator Design and Modeling"
---

# Advancing Full-stack Acceleration for Schrödinger-Style Quantum Simulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Accelerator Design and Modeling。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Accelerator Design and Modeling</p>
</div>

**论文链接**：
**作者**：Shuang Liang Imperial College London , Yuncheng Lu Imperial College London , Ce Guo Imperial College London , Paul H J Kelly Imperial College London , Wayne Luk Imperial College London , Hongxiang Fan Imperial College London
**会议**：HPCA 2026

---

## 中文标题

推进薛定谔式量子模拟的全栈加速

## 英文摘要

Recent developments in quantum hardware, including the scaling of physical qubits and advanced quantum error correction techniques, have increased the number of reliable logical qubits. However, this progress has introduced new challenges for quantum algorithm developers. Limited access to physical quantum machines and the insufficient performance of classical quantum simulators for near-term scales (∼30 logical qubits) hinder the simulation and validation of quantum algorithms. To address this urgent need for improving simulation performance, we propose a novel end-to-end full-stack solution for Schrödinger-style simulation that jointly explores algorithm, software, and hardware optimizations. At the algorithmic level, by identifying the inefficiency in executing complex signed permutations and complex unitary permutation gates, we introduce index redirection and pre-compute merging that significantly reduce data movement and computational complexity. At the hardware level, we propose a reconfigurable dataflow architecture with adaptive memory scheduling and swapping optimizations. At the software level, an end-to-end toolchain is introduced to jointly explore both algorithmic and hardware optimizations. A comprehensive evaluation across a large suite of quantum circuits demonstrates that our work achieves a maximum speedup exceeding 50× over the GPU-based Qiskit baseline.

## 中文摘要

量子硬件的最新进展——物理量子比特规模扩展与先进量子纠错技术——提升了可靠逻辑量子比特的数量，但也给量子算法开发者带来新挑战：物理量子机器访问受限，而经典量子模拟器在近期规模（约 30 个逻辑量子比特）下性能不足，阻碍了量子算法的模拟与验证。为满足提升模拟性能的迫切需求，我们提出一种新颖的端到端全栈薛定谔式模拟方案，联合探索算法、软件与硬件优化。算法层面，我们识别出执行复数带符号置换与复数酉置换门时的低效性，引入索引重定向与预计算合并，显著减少数据移动与计算复杂度。硬件层面，我们提出具有自适应内存调度与交换优化的可重构数据流架构。软件层面，引入端到端工具链以联合探索算法与硬件优化。在大量量子电路上的全面评估表明，我们的工作相比基于 GPU 的 Qiskit 基线最高取得超过 50 倍的加速比。
