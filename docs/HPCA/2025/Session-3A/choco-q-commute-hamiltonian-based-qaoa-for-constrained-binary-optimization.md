---
title: "Choco-Q: Commute Hamiltonian-based QAOA for Constrained Binary Optimization"
description: "HPCA 2025 · Quantum Slots"
tags:
  - "HPCA2025"
  - "Quantum Slots"
---

# Choco-Q: Commute Hamiltonian-based QAOA for Constrained Binary Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Quantum Slots。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Quantum Slots</p>
</div>

**论文链接**：
**作者**：Debin Xiang (Zhejiang University), Qifan Jiang (Zhejiang University), Liqiang Lu (Zhejiang University), Siwei Tan (Zhejiang University), Jianwei Yin (Zhejiang University)
**会议**：HPCA 2025

---

## 中文标题

Choco-Q：面向受约束二进制优化的基于对易哈密顿量的 QAOA

## 英文摘要

Constrained binary optimization aims to find an optimal assignment to minimize or maximize the objective meanwhile satisfying the constraints, which is a representative NP problem in various domains, including transportation, scheduling, and economy. Quantum approximate optimization algorithms (QAOA) provide a promising methodology for solving this problem by exploiting the parallelism of quantum entanglement. However, existing QAOA approaches based on penalty-term or Hamiltonian simulation fail to thoroughly encode the constraints, leading to extremely low success rate and long searching latency. This paper proposes Choco-Q, a formal and universal framework for constrained binary optimization problems, which comprehensively covers all constraints and exhibits high deployability for current quantum devices. The main innovation of Choco-Q is to embed the commute Hamiltonian as the driver Hamiltonian, resulting in a much more general encoding formulation that can deal with arbitrary linear constraints. Leveraging the arithmetic features of commute Hamiltonian, we propose three optimization techniques to squeeze the overall circuit complexity, including Hamiltonian serialization, equivalent decomposition, and variable elimination. The serialization mechanism transforms the original Hamiltonian into smaller ones. Our decomposition methods only take linear time complexity, achieving end-to-end acceleration. Experiments demonstrate that Choco-Q shows more than 235× algorithmic improvement in successfully finding the optimal solution, and achieves 4.69× end-to-end acceleration, compared to prior QAOA designs.

## 中文摘要

受约束二进制优化旨在寻找使目标最小或最大、同时满足约束的最优赋值，是交通、调度、经济等领域中一类代表性的 NP 问题。量子近似优化算法（QAOA）利用量子纠缠的并行性，为求解该问题提供了有前景的方法。然而，现有基于惩罚项或哈密顿量模拟的 QAOA 方法无法彻底编码约束，导致成功率极低、搜索时延长。本文提出 Choco-Q，一个面向受约束二进制优化问题的形式化通用框架，它全面覆盖各种约束，并对当前量子器件具有很高的可部署性。Choco-Q 的核心创新在于将对易哈密顿量作为驱动哈密顿量嵌入，从而得到可处理任意线性约束的更通用编码形式。利用对易哈密顿量的算术特性，我们提出三种优化技术来压缩整体线路复杂度，包括哈密顿量串行化、等价分解与变量消去。串行化机制将原哈密顿量转化为更小的哈密顿量；我们的分解方法仅具线性时间复杂度，实现了端到端加速。实验表明，相比已有 QAOA 设计，Choco-Q 在成功找到最优解上取得超过 235 倍的算法改进，并实现 4.69 倍的端到端加速。
