---
title: "HATT: 面向化学模拟的Fermion-to-Qubit映射优化"
description: "HPCA 2025论文解读：HATT提出基于Hamiltonian结构感知的三叉树Fermion-to-Qubit映射，减少量子化学模拟电路的量子门数量，实现更高效的量子计算资源利用。"
tags: ["HPCA2025", "量子计算", "Fermion-to-Qubit", "量子化学", "编译优化", "UPenn"]
---

# HATT: Hamiltonian Aware Ternary Tree for Optimizing Fermion-to-Qubit Mapping

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">HATT 针对量子化学模拟中 Fermion-to-Qubit 映射问题，提出基于 Hamiltonian 结构的三叉树（Ternary Tree）编码方案，通过感知分子 Hamiltonian 的稀疏性减少量子门数量，相比 Jordan-Wigner 编码减少 40%+ 门操作。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · 量子化学 · Fermion-to-Qubit · Hamiltonian 模拟 · 量子编译 · UPenn</p>
</div>

**作者**：Yuhao Liu, Kevin Yao, Jonathan Hong, Julien Froustey, Yunong Shi, Ermal Rrapaj, Costin Iancu, Gushu Li  
**机构**：University of Pennsylvania; University of California, Berkeley; AWS Quantum Technologies; Lawrence Berkeley National Laboratory  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> 量子化学模拟需要将分子 Hamiltonian（费米子表示）编码到量子比特上，标准 Jordan-Wigner（JW）编码对每个费米子算符需要 O(N) 门；HATT 利用 Hamiltonian 的稀疏结构设计三叉树编码，将门深度降低 40%+。

## 背景与动机

- **量子化学应用**：量子计算机的"杀手级应用"之一是模拟分子/材料的电子结构，对新型材料发现和药物设计有重大意义
- **Fermion-to-Qubit 映射瓶颈**：分子 Hamiltonian 由费米子算符表达，需要映射到量子比特算符。JW 编码产生大量 Pauli 串，导致电路门数随分子大小急剧增加
- **稀疏 Hamiltonian 的机会**：真实分子 Hamiltonian 通常稀疏，许多 Pauli 串的系数为零，可以利用这种稀疏性减少电路操作

## HATT 方法

### 三叉树编码结构

- 传统二叉树（Parity/BK 编码）每个节点对应 1 个量子比特
- HATT 三叉树中，每个非叶节点对应 3 个量子比特，允许更灵活的父-子关系编码
- 通过分析目标 Hamiltonian 的 Pauli 权重分布，构建最优三叉树拓扑

### Hamiltonian 感知优化

1. 分析目标 Hamiltonian 中所有 Pauli 串的频次
2. 高频 Pauli 串优先分配到树的低深度节点（减少 CNOT 开销）
3. 动态规划求解最优树结构

## 实验结果

| 分子 | JW 门深度 | BK 门深度 | HATT 门深度 | HATT vs JW |
|------|---------|---------|-----------|------------|
| H2O (8 qubits) | 142 | 98 | 83 | 41.5% 减少 |
| LiH (12 qubits) | 2840 | 1820 | 1510 | 46.8% 减少 |
| BeH2 (14 qubits) | 5680 | 3620 | 2970 | 47.7% 减少 |

## 核心亮点

1. 三叉树结构比二叉树更灵活，可以更好地适配不规则 Hamiltonian 结构
2. 与标准量子编译器（Qiskit、Tket）兼容，HATT 作为预处理步骤无需修改后端编译器
3. 在近期量子设备（NISQ）和容错量子计算机上均适用

## 局限性

- 最优三叉树构建的计算复杂度为 O(N^3)，对超大分子（N > 100 轨道）需启发式近似
- 仅适用于量子化学模拟，对其他量子算法（QFT、QAOA）帮助有限
