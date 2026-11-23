---
title: "Caravan: A Hardware/Software Co-Design for Efficient SIMD Neighbor Search on Point Clouds"
description: "ISCA 2025 · Session 6B · Caravan：面向点云高效 SIMD 邻域搜索的软硬件协同设计"
tags:
  - "ISCA2025"
  - "Session 6B"
  - "Microarchitecture II"
---

# Caravan: A Hardware/Software Co-Design for Efficient SIMD Neighbor Search on Point Clouds

**中文标题：** Caravan：面向点云高效 SIMD 邻域搜索的软硬件协同设计

**所属 Session：** [Session 6B](index.md) · [ISCA 2025](../index.md)

**作者：** Pedro Henrique Exenberger Becker, Franyell Silfa, Jose Maria Arnau, Antonio Gonzalez

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731075) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Neighbor search is the backbone task for point cloud processing, which is widely employed in current 3D computer vision applica- tions. To be efficient, neighbor search relies on spatial data struc- tures such as k-d trees, to prune the search space. We found that consecutive neighbor search queries in point cloud processing are often similar, visiting k-d tree nodes with considerable resemblance. In this work, we show how to leverage this observation to effec- tively exploit the available CPU Vector Processing Unit (VPU) to cheaply speed up neighbor search. We devise our solution with a hardware/software co-design called Caravan. At the software level, Caravan-SW exploits this search similarity, gathering consecutive queries to search for their neighbors in parallel with SIMD instruc- tions. Yet, when the navigation of queries diverges, particularly in the deeper levels of the k-d tree, Caravan-SW faces sparsity and VPU lanes are underutilized. We tackle this with Caravan-HW, adding two new instructions that re-index valid vector elements and allow fast operand shuffling and dense SIMD operations to take place, suppressing the hard-to-predict runtime sparsity of Caravan- SW. With AVX512, Caravan-SW speeds up neighbor search by 4.05× (1.85×end-to-end) during point cloud segmentation in a commodity CPU. With the additional Caravan-HW support, the leaf processing part of neighbor search can be further optimized, boosting speed up to 5.19×(1.97×end-to-end), with minimal area costs of 0.032 mm2 . Our programmable and minimally intrusive solution has end-to-end benefits comparable to accelerators.

## 中文摘要

邻域搜索是点云处理的核心任务，广泛应用于当下三维计算机视觉场景。为提升搜索效率，邻域搜索通常依托k-d树这类空间数据结构裁剪搜索空间。本文观察到：点云处理中连续的邻域搜索查询具有相似性，访问的k-d树节点高度重合。基于该发现，本文提出软硬件协同方案Caravan，充分利用CPU向量处理单元（VPU），以较低代价加速邻域搜索。

软件侧Caravan-SW挖掘查询之间的相似性，聚合连续查询，借助SIMD指令并行完成邻域查找。但当查询路径发生分叉（尤其在k-d树较深层）时，Caravan-SW会遭遇稀疏问题，向量通道利用率低下。本文通过Caravan-HW解决该问题：新增两条指令，支持对有效向量元素重索引、快速操作数混排，实现稠密SIMD运算，掩盖Caravan-SW中难以预测的运行时稀疏性。

在商用CPU的AVX512平台上，仅使用Caravan-SW时，点云分割任务的邻域搜索算子提速4.05倍（端到端1.85倍）；叠加Caravan-HW硬件支持后，邻域搜索的叶子节点处理进一步优化，算子最高提速5.19倍（端到端1.97倍），硬件面积开销仅0.032 mm²。该方案可编程、对原有系统侵入性小，端到端收益可媲美专用加速器。

## 英文关键词

Nearest Neighbor Search, SIMD, 3D Computer Vision, Point Cloud, K-D Tree, ISA-Extension, Sparsity

## 中文关键词

最近邻搜索, 单指令多数据, 三维计算机视觉, 点云, K-D树, 指令集扩展, 稀疏性

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731075)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2025](../index.md)
