---
title: "Kosmo: Efficient Online Miss Ratio Curve Generation for Eviction Policy Evaluation"
description: "FAST 2024 · Caching · 第 89–106 页"
tags:
  - "FAST2024"
  - "Caching"
---

# Kosmo: Efficient Online Miss Ratio Curve Generation for Eviction Policy Evaluation

**中文标题**：Kosmo：面向逐出策略评估的高效在线缺失率曲线生成

**Session**：Caching · 2024-02-27 14:00–15:15 · Chair：Carl Waldspurger（Carl Waldspurger Consulting）

**作者**：Kia Shakiba, Sari Sultan, and Michael Stumm, University of Toronto

**会议**：FAST 2024 · Santa Clara, CA · 第 89–106 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/shakiba](https://www.usenix.org/conference/fast24/presentation/shakiba)

**论文 PDF**：[fast24-shakiba.pdf](https://www.usenix.org/system/files/fast24-shakiba.pdf)

---

## 英文摘要

In-memory caches play an important role in reducing the load on backend storage servers for many workloads. Miss ratio curves (MRCs) are an important tool for configuring these caches with respect to cache size and eviction policy. MRCs provide insight into the trade-off between cache size (and thus costs) and miss ratio for a specific eviction policy. Over the years, many MRC-generation algorithms have been developed. However, to date, only Miniature Simulations is capable of efficiently generating MRCs for popular eviction policies, such as *Least Frequently Used* (LFU), *First-In-First-Out* (FIFO), 2Q, and *Least Recently/Frequently Used* (LRFU), that do not adhere to the inclusion property. One critical downside of Miniature Simulations is that it incurs significant memory overhead, precluding its use for online cache analysis at runtime in many cases.

In this paper, we introduce Kosmo, an MRC generation algorithm that allows for the simultaneous generation of MRCs for a variety of eviction policies that do not adhere to the inclusion property. We evaluate Kosmo using 52 publicly-accessible cache access traces with a total of roughly 126 billion accesses. Compared to Miniature Simulations configured with 100 simulated caches, Kosmo has lower memory overhead by a factor of 3.6 on average, and as high as 36, and a higher throughput by a factor of 1.3 making it far more suitable for online MRC generation.

## 中文摘要

内存缓存在降低许多负载对后端存储服务器压力方面发挥着重要作用。缺失率曲线（MRC）是配置这些缓存（涉及缓存大小和逐出策略）的重要工具。MRC 可揭示特定逐出策略下缓存大小（及其成本）与缺失率之间的权衡。多年来，人们开发了许多 MRC 生成算法。然而，迄今为止，只有 Miniature Simulations 能够为不满足包含属性的流行逐出策略（如 *最不经常使用*（LFU）、*先进先出*（FIFO）、2Q 和 *最近/最经常使用*（LRFU））高效生成 MRC。Miniature Simulations 的一个关键缺点是带来显著的内存开销，导致其在许多情况下无法用于运行时的在线缓存分析。

本文提出 Kosmo，一种 MRC 生成算法，可同时为多种不满足包含属性的逐出策略生成 MRC。我们使用 52 条公开可访问的缓存访问跟踪（总计约 1260 亿次访问）评估 Kosmo。与配置 100 个模拟缓存的 Miniature Simulations 相比，Kosmo 的内存开销平均低 3.6 倍，最高低 36 倍，吞吐量高 1.3 倍，因而更适合在线 MRC 生成。
