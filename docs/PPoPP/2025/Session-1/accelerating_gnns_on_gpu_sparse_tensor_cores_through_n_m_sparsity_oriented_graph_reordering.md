---
title: "Accelerating GNNs on GPU Sparse Tensor Cores through N:M Sparsity-Oriented Graph Reordering"
description: "PPoPP 2025 Session 1（Graph Neural Networks）：无损图重排序对齐 N:M 稀疏模式，SpMM 最高 43× 加速"
tags:
  - "PPoPP2025"
  - "Session-1"
  - "Graph Neural Networks"
  - "Graph Reordering"
  - "Sparse Tensor Cores"
  - "SpMM"
authors:
  - "Jou-An Chen"
  - "Hsin-Hsuan Sung"
  - "Ruifeng Zhang"
  - "Ang Li"
  - "Xipeng Shen"
session: "Session 1: Graph Neural Networks"
session_number: 1
session_chair: "Miao Yin"
date: "2025-03-03"
time: "10:20–10:40"
room: "Acacia D"
doi: "10.1145/3710848.3710881"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Accelerating GNNs on GPU Sparse Tensor Cores through N:M Sparsity-Oriented Graph Reordering

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向 N:M 稀疏模式的图重排序算法，把 GNN 中不规则的稀疏图无损转换为 GPU 稀疏张量核可加速的 V:N:M 模式，并保持邻接矩阵对称性。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 1: Graph Neural Networks</p>
</div>

**作者**：Jou-An Chen, Hsin-Hsuan Sung, Ruifeng Zhang (North Carolina State University); Ang Li (PNNL and UW); Xipeng Shen (North Carolina State University)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 10:20–10:40 · Session 1: Graph Neural Networks（主席：Miao Yin）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710881) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出面向 N:M 稀疏模式的图重排序算法，把 GNN 中不规则的稀疏图无损转换为 GPU 稀疏张量核可加速的 V:N:M 模式，并保持邻接矩阵对称性。

## 研究问题

真实图往往稀疏且非零分布不规则，难以满足 Sparse Tensor Core 要求的 V:N:M 稀疏模式，导致 GNN 无法直接享受稀疏张量核加速。

## 方法简述

- 设计图重排序算法，按 N:M 分块重新排列节点，使非零元素尽量对齐硬件稀疏模式。
- 重排序过程保持邻接矩阵对称，使结果仍兼容依赖对称性的图算法。
- 在保持 GNN 精度的前提下实现无损优化。

## 主要结果

- 向量级 N:M 稀疏模式违规减少 98–100%，SuiteSparse 中合规图的比例从 5–9% 提升到 88.7–93.5%。
- A100 上 SpMM 相对 cuSPARSE 最高加速 43×，几何平均加速 2.3–7.5×。
- 真实图上的关键 GNN 图操作平均加速 3.5×，最高 8.6×。

<details>
<summary>原文摘要（英文）</summary>

Recent GPUs have introduced Sparse Tensor Cores (SPTC) to accelerate computations on sparse matrices meeting the N:M sparse patterns. Software tools expand the support to more general V:N:M patterns. Graphs in Graph Neural Networks (GNNs) are typically sparse, but the sparsity is often irregular, not conforming to the required V:N:M sparse patterns. This paper proposes a novel graph reordering algorithm to transform irregular graph data into the required sparse patterns for GNNs to benefit from SPTC. The optimization is lossless, maintaining the accuracy of GNN. It at the same time keeps the symmetry of the adjacency matrices of the graphs so that the same matrices can remain compatible with many symmetry-based graph algorithms. The optimization successfully removes 98-100% violations of the N:M sparse patterns at the vector level and increases the portion of conforming graphs in the SuiteSparse collection from 5-9% to 88.7-93.5%. On A100 GPUs, the optimization accelerates Sparse Matrix Matrix (SpMM) by up to 43X (a geomean speedup of 2.3X – 7.5X) over cuSPARSE and speeds up the key graph operations in GNNs on real graphs by as much as 8.6X (3.5X on average).

</details>

---

> 所属 Session：[Session 1: Graph Neural Networks](index.md) · 返回 [PPoPP 2025 总览](../index.md)
