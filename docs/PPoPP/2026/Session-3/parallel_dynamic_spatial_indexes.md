---
title: "Parallel Dynamic Spatial Indexes"
description: "PPoPP 2026 Session 3（Concurrent Data Structures）：P-Orth 与 SPaC-tree：批量更新胜过并行 kd/Orth 树"
tags:
  - "PPoPP2026"
  - "Session-3"
  - "Concurrent Data Structures"
  - "Spatial Indexes"
  - "Parallel Batch Updates"
  - "R-Trees"
authors:
  - "Ziyang Men"
  - "Bo Huang"
  - "Yan Gu"
  - "Yihan Sun"
session: "Session 3: Concurrent Data Structures"
session_number: 3
session_chair: "Calin Cascaval"
date: "2026-02-02"
time: "15:10–15:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786412"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Parallel Dynamic Spatial Indexes

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">系统研究面向高动态负载的并行空间索引，提出并行 Orth 树 P-Orth 与并行 R 树/BVH 家族 SPaC-tree，批量更新优于现有并行索引且查询性能保持不退化。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 3: Concurrent Data Structures</p>
</div>

**作者**：Ziyang Men, Bo Huang, Yan Gu, and Yihan Sun — University of California at Riverside, USA

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 15:10–15:30 · Session 3: Concurrent Data Structures（主席：Calin Cascaval）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786412) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Maintaining spatial data (points in two or three dimensions) is crucial and has a wide range of applications, such as graphics, GIS, and robotics. To support efficient updates and queries on the spatial data, many data structures, called spatial indexes, have been proposed, e.g., 𝑘d-trees, oct/quadtrees (also called Orth-trees), R-trees, and bounding volume hierarchies (BVHs). In real-world applications, spatial datasets tend to be highly dynamic, requiring batch updates of points with low latency. This calls for efficient parallel batch updates on spatial indexes. Unfortunately, there is very little work that achieves this. In this paper, we systematically study parallel spatial indexes, with a special focus on achieving high-performance update performance for highly dynamic workloads. We select two types of spatial indexes that are considered optimized for low-latency updates: Orth-tree and R-tree/BVH. We propose two data structures: the P-Orth tree, a parallel Orth-tree, and the SPaC-tree family, a parallel R-tree/BVH. Both the P-Orth tree and the SPaC-tree deliver superior performance in batch updates compared to existing parallel 𝑘d-trees and Orth-trees, while preserving better or competitive query performance relative to their corresponding Orth-tree and R-tree counterparts. We also present comprehensive experiments comparing the performance of various parallel spatial indexes and share our findings at the end of the paper.

## 中文摘要

维护空间数据（二维或三维的点）至关重要，并且有着广泛的应用，例如图形学、GIS 与机器人。为支持对空间数据的高效更新与查询，人们提出了许多称为空间索引的数据结构，例如 kd 树、八叉/四叉树（也称为 Orth 树）、R 树以及包围体层次结构（BVH）。在实际应用中，空间数据集往往高度动态，需要以低延迟批量更新点，这就要求空间索引具备高效的并行批量更新能力。遗憾的是，能实现这一点的工作非常少。本文系统地研究并行空间索引，特别关注为高度动态的工作负载实现高性能的更新性能。我们选取了两类被认为针对低延迟更新做了优化的空间索引：Orth 树与 R 树/BVH。我们提出两种数据结构：P-Orth 树，一种并行 Orth 树；以及 SPaC 树族，一种并行 R 树/BVH。与现有的并行 kd 树和 Orth 树相比，P-Orth 树与 SPaC 树在批量更新上均表现出更优的性能，同时相对于各自对应的 Orth 树与 R 树对应实现，保持了更好或具有竞争力的查询性能。我们还给出了比较各种并行空间索引性能的全面实验，并在文末分享了我们的发现。

## 英文关键词

Spatial Indexes, Quad-tree, Oct-tree, R-tree

## 中文关键词

空间索引；四叉树（Quad-tree）；八叉树（Oct-tree）；R 树

---

## 一句话总结

> 系统研究面向高动态负载的并行空间索引，提出并行 Orth 树 P-Orth 与并行 R 树/BVH 家族 SPaC-tree，批量更新优于现有并行索引且查询性能保持不退化。

## 研究问题

真实空间数据集高度动态，需要低延迟的批量点更新，但面向并行批量更新的空间索引研究极少，缺乏高更新性能的方案。

## 方法简述

- 选取被认为针对低延迟更新优化的两类空间索引——Orth 树与 R 树/BVH——作为研究对象。
- 提出 P-Orth 树，即并行 Orth 树。
- 提出 SPaC-tree 家族，即并行 R 树/BVH。
- 设计并开展系统性实验，比较多种并行空间索引的性能，并在文末总结研究发现。

## 主要结果

- 与现有并行 kd 树和 Orth 树相比，P-Orth 树与 SPaC-tree 在批量更新上性能更优。
- 在批量更新占优的同时，相对各自对应的 Orth 树与 R 树，查询性能更好或具有竞争力。
- 给出多种并行空间索引的全面实验对比与经验性发现。

---

> 所属 Session：[Session 3: Concurrent Data Structures](index.md) · 返回 [PPoPP 2026 总览](../index.md)
