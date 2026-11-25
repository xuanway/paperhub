---
title: "Semi-StructMG: A Fast and Scalable Semi-Structured Algebraic Multigrid"
description: "PPoPP 2025 Session 11（Parallel Algorithms and Applications）：多维粗化 + 块间连接优化，六个测试问题均取得最快 time-to-solution"
tags:
  - "PPoPP2025"
  - "Session-11"
  - "Parallel Algorithms and Applications"
  - "Multigrid"
  - "Sparse Linear Systems"
  - "Scalability"
authors:
  - "Yi Zong"
  - "Chensong Zhang"
  - "Longjiang Mu"
  - "Jianchun Wang"
  - "Jian Sun"
  - "Xiaowen Xu"
  - "Xinliang Wang"
  - "Peinan Yu"
  - "Wei Xue"
session: "Session 11: Parallel Algorithms and Applications"
session_number: 11
session_chair: "Weicong Chen"
date: "2025-03-05"
time: "12:00–12:20"
room: "Acacia D"
doi: "10.1145/3710848.3710849"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Semi-StructMG: A Fast and Scalable Semi-Structured Algebraic Multigrid

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">设计并实现半结构化代数多重网格 Semi-StructMG，用多维粗化降低复杂度、简化通信，并针对块间连接优化平滑器与三重矩阵乘，在大规模并行下保持收敛。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 11: Parallel Algorithms and Applications</p>
</div>

**作者**：Yi Zong (Tsinghua University); Chensong Zhang (Academy of Mathematics and Systems Science); Longjiang Mu (Laoshan Laboratory); Jianchun Wang (China Ship Scientific Research Center); Jian Sun (CMA Earth System Modeling and Prediction Center); Xiaowen Xu (Institute of Applied Physics and Computational Mathematics); Xinliang Wang (Huawei Technologies Co., Ltd); Peinan Yu, Wei Xue (Tsinghua University)

**会议**：PPoPP 2025 · 2025 年 3 月 5 日 12:00–12:20 · Session 11: Parallel Algorithms and Applications（主席：Weicong Chen）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710849) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 设计并实现半结构化代数多重网格 Semi-StructMG，用多维粗化降低复杂度、简化通信，并针对块间连接优化平滑器与三重矩阵乘，在大规模并行下保持收敛。

## 研究问题

并行多重网格常用作大规模稀疏线性系统的预条件子，但多数实现依赖通用稀疏格式，难以达到最优性能；现有半结构化多重网格库在速度与可扩展性上仍有明显不足。

## 方法简述

- 采用多维粗化（multi-dimensional coarsening）降低复杂度并简化通信模式。
- 在平滑器与三重矩阵乘中专门处理块间连接（inter-block connections）的作用，以改善大规模并行下的收敛性。

## 主要结果

- 在两个基准问题和油藏模拟、船舶制造、数值天气预报、海洋建模四个真实应用上均取得最快的 time-to-solution。
- 相比 hypre 的 SSAMG、Split、BoomerAMG 平均加速 5.97×、15.2×、3.85×，并显著改善强/弱扩展效率。

<details>
<summary>原文摘要（英文）</summary>

Parallel multigrid methods are widely used as preconditioners for solving large sparse linear systems. Most multigrids rely on general sparse matrix formats, which prevent them from achieving optimal performance. There is an emerging trend towards semi-structured multigrids that balance flexibility with performance. However, existing libraries often fall short in terms of speed and scalability for semi-structured problems. To address these limitations, we have designed and implemented Semi-StructMG. It employs multi-dimensional coarsening to reduce complexity and simplify communication patterns. It also considers the special role of inter-block connections in smoothers and triple-matrix products to improve convergence under large-scale parallelism. We evaluated Semi-StructMG using two benchmark problems and four real-world applications from petroleum reservoir simulation, ship manufacturing, numerical weather prediction, and ocean modeling. Compared to hypre’s multigrids, Semi-StructMG achieves the fastest time-to-solution across all cases, with average speedups of 5.97x, 15.2x, and 3.85x over SSAMG, Split, and BoomerAMG, respectively. Additionally, This work is licensed under Semi-StructMG significantly improves both strong and weak scaling efficiencies in all tests. These results suggest that it can serve as an effective alternative to SSAMG and Split.

</details>

---

> 所属 Session：[Session 11: Parallel Algorithms and Applications](index.md) · 返回 [PPoPP 2025 总览](../index.md)
