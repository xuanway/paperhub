---
title: "HybridTier: An Adaptive and Lightweight CXL-Memory Tiering System"
description: "ASPLOS 2026 · Session 1D · HybridTier：一种自适应且轻量级的 CXL 内存分层系统"
tags:
  - "ASPLOS2026"
  - "Session 1D"
  - "CXL & Memory Fabric"
---

# HybridTier: An Adaptive and Lightweight CXL-Memory Tiering System

**中文标题：** HybridTier：一种自适应且轻量级的 CXL 内存分层系统

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Kevin Song (University of Toronto), Jiacheng Yang (University of Toronto), Zixuan Wang (University of California San Diego), Jishen Zhao (UCSD), Sihang Liu (Waterloo), Gennady Pekhimenko (Univ. of Toronto / CentML)

**单位：** University of Toronto；University of California San Diego；UCSD；Waterloo；Univ. of Toronto / CentML

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736119) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Modern workloads are demanding increasingly larger memory capacity. Compute Express Link (CXL)-based memory tiering has emerged as a promising solution for addressing this problem by utilizing traditional DRAM alongside slowtier CXL memory devices. We analyze prior tiering systems and observe two challenges for high-performance memory tiering: adapting to skewed but dynamically varying data hotness distributions while minimizing memory and cache overhead due to tiering. To address these challenges, we propose HybridTier, an adaptive and lightweight tiering system for CXL memory. HybridTier tracks both long-term data access frequency and short-term access momentum simultaneously to accurately capture and adapt to shifting hotness distributions. HybridTier reduces the metadata memory overhead by tracking data accesses probabilistically, obtaining higher memory efficiency by trading off a small amount of tracking inaccuracy that has a negligible impact on application performance. To reduce cache overhead, HybridTier uses lightweight data structures that optimize for data locality to track data hotness. Our evaluations show that HybridTier outperforms prior systems by up to 91% (19% geomean), incurring 2.0 −7.8× less memory overhead and 1.7 −3.5× less cache misses.

## 中文摘要

现代工作负载对内存容量的需求日益增大。基于计算快速链路（CXL）的内存分层已成为应对这一问题的一种有前景的解决方案，它利用传统 DRAM 与慢速层 CXL 内存设备并存。我们分析了先前的分层系统，并观察到实现高性能内存分层面临两个挑战：在适应偏斜且动态变化的数据热度分布的同时，最小化由分层带来的内存与缓存开销。为应对这些挑战，我们提出 HybridTier，一种面向 CXL 内存的自适应且轻量级分层系统。HybridTier 同时跟踪长期数据访问频率和短期访问动量，以准确捕获并适应不断变化的热度分布。HybridTier 通过以概率方式跟踪数据访问来降低元数据内存开销，以少量对应用性能影响可忽略的跟踪不准确性为代价，获得更高的内存效率。为降低缓存开销，HybridTier 使用针对数据局部性优化的轻量级数据结构来跟踪数据热度。我们的评估表明，HybridTier 相较先前系统性能最高提升 91%（几何平均 19%），同时带来 2.0 −7.8 倍的内存开销降低和 1.7 −3.5 倍的缓存缺失降低。

## 英文关键词

Compute Express Link, Tiered Memory

## 中文关键词

计算快速链路；分层内存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736119)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 1D](index.md) · [返回 ASPLOS 2026](../index.md)
