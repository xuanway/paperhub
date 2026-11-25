---
title: "Popcorn: Accelerating Kernel K-means on GPUs through Sparse Linear Algebra"
description: "PPoPP 2025 Session 10（GPU II）：SpMM/SpMV 表述 Kernel K-means，比 CPU 最高 123.8×"
tags:
  - "PPoPP2025"
  - "Session-10"
  - "GPU II"
  - "Kernel K-means"
  - "Sparse Linear Algebra"
  - "GPU"
authors:
  - "Julian Bellavita"
  - "Thomas Pasquali"
  - "Laura Del Rio"
  - "Flavio Vella"
  - "Giulia Guidi"
session: "Session 10: GPU II"
session_number: 10
session_chair: "Zhijia Zhao"
date: "2025-03-05"
time: "10:00–10:20"
room: "Acacia D"
doi: "10.1145/3710848.3710887"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Popcorn: Accelerating Kernel K-means on GPUs through Sparse Linear Algebra

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出用稀疏-稠密矩阵乘（SpMM）与稀疏矩阵-向量乘（SpMV）表述 Kernel K-means，并据此实现首个开源 GPU 版 Kernel K-means——Popcorn。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 10: GPU II</p>
</div>

**作者**：Julian Bellavita (Cornell University); Thomas Pasquali, Laura Del Rio, Flavio Vella (University of Trento); Giulia Guidi (Cornell University)

**会议**：PPoPP 2025 · 2025 年 3 月 5 日 10:00–10:20 · Session 10: GPU II（主席：Zhijia Zhao）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710887) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出用稀疏-稠密矩阵乘（SpMM）与稀疏矩阵-向量乘（SpMV）表述 Kernel K-means，并据此实现首个开源 GPU 版 Kernel K-means——Popcorn。

## 研究问题

Kernel K-means 能识别非线性可分的簇，但计算量随数据规模二次增长，在 CPU 上即使中等规模数据集也要数分钟。

## 方法简述

- 把 Kernel K-means 的计算重构为 SpMM 与 SpMV 稀疏线性代数运算。
- 借助稀疏矩阵运算以很小的编程代价实现 GPU 版本。

## 主要结果

- 相比 CPU 版 Kernel K-means 最高加速 123.8×。
- 相比不使用稀疏矩阵计算的 GPU 版 Kernel K-means 最高加速 2.6×。

<details>
<summary>原文摘要（英文）</summary>

K-means is a popular clustering algorithm with significant applications in numerous scientific and engineering areas. One drawback of K-means is its inability to identify nonlinearly separable clusters, which may lead to inaccurate solutions in certain cases. Kernel K-means is a variant of classical K-means that can find non-linearly separable clusters. However, it scales quadratically with respect to the size of the dataset, taking several minutes to cluster even medium-sized datasets on traditional CPU-based machines. In this paper, we present a formulation of Kernel K-means using sparse-dense matrix multiplication (SpMM) and sparse matrix-vector multiplication (SpMV), and we show that our formulation enables the rapid implementation of a fast GPU-based version of Kernel K-means with little programming effort. Our implementation, named Popcorn, is the first open-source GPU-based implementation of Kernel K-means. Popcorn achieves a speedup of up to 123.8× over a CPU implementation of Kernel K-means and a speedup of up to 2.6× over a GPU implementation of Kernel K-means that does not use sparse matrix computations. Our results support the effectiveness of sparse matrices as tools for efficient parallel programming.

</details>

---

> 所属 Session：[Session 10: GPU II](index.md) · 返回 [PPoPP 2025 总览](../index.md)
