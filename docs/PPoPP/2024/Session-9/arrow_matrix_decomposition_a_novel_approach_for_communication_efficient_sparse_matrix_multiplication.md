---
title: "Arrow Matrix Decomposition: A Novel Approach for Communication-Efficient Sparse Matrix Multiplication"
description: "PPoPP 2024 Session Linear Algebra：箭头矩阵分解实现通信规避 SpMM，亿级行矩阵上近线性强弱扩展"
tags:
  - "PPoPP2024"
  - "Session-9"
  - "Linear Algebra"
  - "SpMM"
  - "sparse linear algebra"
  - "graphs"
authors:
  - "Lukas Gianinazzi"
  - "Alexandros Nikolaos Ziogas"
  - "Piotr Luczynski"
  - "Langwen Huang"
  - "Saleh Ashkboosh"
  - "Florian Scheidl"
  - "Armon Carigiet"
  - "Chio Ge"
  - "Nabil Abubaker"
  - "Maciej Besta"
  - "Tal Ben-Nun"
  - "Torsten Hoefler"
session: "Session 9: Linear Algebra"
session_number: 9
session_chair: "I-Ting Angelina Lee"
date: "2024-03-06"
time: "10:40–11:00"
room: "Moorfoot"
doi: "10.1145/3627535.3638496"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Arrow Matrix Decomposition: A Novel Approach for Communication-Efficient Sparse Matrix Multiplication

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出将稀疏矩阵分解为少量经置换连接的箭头矩阵，实现通信规避的迭代 SpMM，使平面图等图族每次迭代通信量多项式级下降，亿行级矩阵上近线性扩展。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 9: Linear Algebra</p>
</div>

**作者**：Lukas Gianinazzi, Alexandros Nikolaos Ziogas, Piotr Luczynski, Langwen Huang, Saleh Ashkboosh, Florian Scheidl, Armon Carigiet, Chio Ge, Nabil Abubaker, Maciej Besta, Tal Ben-Nun, Torsten Hoefler (ETH Zurich)

**会议**：PPoPP 2024 · 2024 年 3 月 6 日 10:40–11:00 · Session 9: Linear Algebra（主席：I-Ting Angelina Lee）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638496) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

We propose a novel approach to iterated sparse matrix dense matrix multiplication, a fundamental computational kernel in scientific computing and graph neural network training. In cases where matrix sizes exceed the memory of a single compute node, data transfer becomes a bottleneck. An approach based on dense matrix multiplication algorithms leads to suboptimal scalability and fails to exploit the sparsity in the problem. To address these challenges, we propose decomposing the sparse matrix into a small number of highly structured matrices called arrow matrices, which are connected by permutations. Our approach enables communication-avoiding multiplications, achieving a polynomial reduction in communication volume per iteration for matrices corresponding to planar graphs and other minor-excluded families of graphs. Our evaluation demonstrates that our approach outperforms a state-of-the-art method for sparse matrix multiplication on matrices with hundreds of millions of rows, offering near-linear strong and weak scaling.

## 中文摘要

我们针对迭代稀疏矩阵-稠密矩阵乘法提出一种新方法，该内核是科学计算与图神经网络训练中的基础计算内核。当矩阵规模超出单个计算节点的内存时，数据传输成为瓶颈。基于稠密矩阵乘法算法的做法会导致次优的可扩展性，并且无法利用问题中的稀疏性。为应对这些挑战，我们提出将稀疏矩阵分解为少量高度结构化的矩阵，称为箭头矩阵（arrow matrices），它们通过置换相互连接。我们的方法实现了通信规避的乘法，对于对应平面图及其他 minor-excluded 图族的矩阵，每次迭代的通信量可实现多项式级下降。我们的评估表明，在行数达数亿的矩阵上，本方法优于最先进的稀疏矩阵乘法方法，并呈现接近线性的强扩展与弱扩展。

## 英文关键词

matrix multiplication, sparsity, sparse linear algebra, spmm, graphs, linear arrangement, power law

## 中文关键词

矩阵乘法；稀疏性；稀疏线性代数；SpMM；图；线性排列；幂律

---

## 一句话总结

> 提出将稀疏矩阵分解为少量经置换连接的箭头矩阵，实现通信规避的迭代 SpMM，使平面图等图族每次迭代通信量多项式级下降，亿行级矩阵上近线性扩展。

## 研究问题

当矩阵规模超出单个计算节点的内存时，数据传输成为瓶颈；而基于稠密矩阵乘法算法的做法可扩展性次优，且无法利用问题本身的稀疏性。

## 方法简述

- 提出将稀疏矩阵分解为少量高度结构化的箭头矩阵（arrow matrices），并通过置换把各箭头矩阵连接起来
- 采用通信规避（communication-avoiding）的乘法方式，降低每次迭代的通信量
- 对平面图及其他 minor-excluded 图族，使每次迭代的通信量取得多项式级下降

## 主要结果

- 在行数达数亿的矩阵上，优于最先进的稀疏矩阵乘法方法
- 强扩展与弱扩展均呈现接近线性的表现

---

> 所属 Session：[Session 9: Linear Algebra](index.md) · 返回 [PPoPP 2024 总览](../index.md)
