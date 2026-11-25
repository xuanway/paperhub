---
title: "ParlayANN: Scalable and Deterministic Parallel Graph-Based Approximate Nearest Neighbor Search Algorithms"
description: "PPoPP 2024 Session Parallel Algorithms：确定性并行图 ANNS 库，可扩展到十亿级数据集"
tags:
  - "PPoPP2024"
  - "Session-7"
  - "Parallel Algorithms"
  - "Approximate Nearest Neighbor Search"
  - "Deterministic Parallelism"
authors:
  - "Magdalen Dobson Manohar"
  - "Zheqi Shen"
  - "Guy E. Blelloch"
  - "Laxman Dhulipala"
  - "Yan Gu"
  - "Harsha Vardhan Simhadri"
  - "Yihan Sun"
session: "Session 7: Parallel Algorithms"
session_number: 7
session_chair: "Prashant Pandey"
date: "2024-03-05"
time: "14:20–14:40"
room: "Moorfoot"
doi: "10.1145/3627535.3638475"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# ParlayANN: Scalable and Deterministic Parallel Graph-Based Approximate Nearest Neighbor Search Algorithms

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">ParlayANN 是一个确定性并行图近似最近邻搜索算法库，为四种最先进图 ANNS 算法开发了新型并行实现，消除锁与顺序瓶颈，可扩展到十亿级数据集并保持确定性。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 7: Parallel Algorithms</p>
</div>

**作者**：Magdalen Dobson Manohar (Carnegie Mellon University); Zheqi Shen (University of California, Riverside); Guy E. Blelloch (Carnegie Mellon University); Laxman Dhulipala (University of Maryland, College Park); Yan Gu (University of California, Riverside); Harsha Vardhan Simhadri (Microsoft Research Lab India); Yihan Sun (University of California, Riverside)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 14:20–14:40 · Session 7: Parallel Algorithms（主席：Prashant Pandey）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638475) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Approximate nearest-neighbor search (ANNS) algorithms are a key part of the modern deep learning stack due to enabling efficient similarity search over high-dimensional vector space representations (i.e., embeddings) of data. Among various ANNS algorithms, graph-based algorithms are known to achieve the best throughput-recall tradeoffs. Despite the large scale of modern ANNS datasets, existing parallel graph-based implementations suffer from significant challenges to scale to large datasets due to heavy use of locks and other sequential bottlenecks, which 1) prevents them from efficiently scaling to a large number of processors, and 2) results in non-determinism that is undesirable in certain applications. In this paper, we introduce ParlayANN, a library of deterministic and parallel graph-based approximate nearest neighbor search algorithms, along with a set of useful tools for developing such algorithms. In this library, we develop novel parallel implementations for four state-of-the-art graph-based ANNS algorithms that scale to billion-scale datasets. Our algorithms are deterministic and achieve high scalability across a diverse set of challenging datasets. In addition to the new algorithmic ideas, we also conduct a detailed experimental study of our new algorithms as well as two existing non-graph approaches. Our experimental results both validate the effectiveness of our new techniques, and lead to a comprehensive comparison among ANNS algorithms on large scale datasets with a list of interesting findings.

## 中文摘要

近似最近邻搜索（ANNS）算法是现代深度学习栈的关键组成部分，因为它能够对数据的高维向量空间表示（即嵌入）进行高效的相似性搜索。在各种 ANNS 算法中，基于图的算法已知能够取得最佳的吞吐率—召回率权衡。尽管现代 ANNS 数据集规模巨大，现有的并行图实现由于大量使用锁和其他顺序瓶颈，在扩展到大规模数据集时面临严峻挑战，这 1) 使其无法高效扩展到大量处理器，2) 导致某些应用中不可接受的非确定性。本文提出 ParlayANN，一个确定性并行图近似最近邻搜索算法库，以及一组用于开发此类算法的有用工具。在该库中，我们为四种可扩展到十亿级数据集的最先进图 ANNS 算法开发了新颖的并行实现。我们的算法是确定性的，并在多种具有挑战性的数据集上实现了高可扩展性。除新的算法思想外，我们还对提出的新算法以及两种现有的非图方法进行了详细的实验研究。实验结果既验证了我们新技术的有效性，也在大规模数据集上对 ANNS 算法进行了全面比较，并得出一系列有趣的发现。

## 英文关键词

nearest neighbor search, vector search, parallel algorithms

## 中文关键词

最近邻搜索；向量搜索；并行算法

---

## 一句话总结

> ParlayANN 是一个确定性并行图近似最近邻搜索算法库，为四种最先进图 ANNS 算法开发了新型并行实现，消除锁与顺序瓶颈，可扩展到十亿级数据集并保持确定性。

## 研究问题

现有并行图 ANNS 实现大量使用锁和其他顺序瓶颈，难以高效扩展到大量处理器，并带来某些应用中不可接受的非确定性，使其无法支撑现代大规模数据集。

## 方法简述

- 提出 ParlayANN 库，为四种最先进的基于图的 ANNS 算法开发全新的并行实现，使其可扩展到十亿级数据集
- 设计确定性的并行化方案，消除锁及其他顺序瓶颈，从而在高并发下保持良好的可扩展性
- 提供一组配套工具，用于开发此类确定性与并行的图 ANNS 算法
- 将新算法与两种现有非图方法纳入统一的详细实验研究，在多样化挑战性数据集上做全面对比

## 主要结果

- 在多种具有挑战性的数据集上实现高可扩展性，同时保证结果是确定性的
- 所实现的算法可扩展到十亿（billion）规模的数据集
- 实验既验证了新技术（含非图方法对比）的有效性，也在大规模数据集上给出了 ANNS 算法的全面比较与一系列有趣发现

---

> 所属 Session：[Session 7: Parallel Algorithms](index.md) · 返回 [PPoPP 2024 总览](../index.md)
