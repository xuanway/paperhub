---
title: "LIBRA: A High-Accuracy, Cost-Aware, and Coordinated Multi-GPU Page Prefetcher"
description: "ISCA 2026 · Session 9B · LIBRA: A High-Accuracy, Cost-Aware, and Coordinated Multi-GPU Page Prefetcher"
tags:
  - "ISCA2026"
  - "Session 9B"
  - "Prefetching and Cache 2"
---

# LIBRA: A High-Accuracy, Cost-Aware, and Coordinated Multi-GPU Page Prefetcher

**中文标题：** LIBRA: 高精度、成本感知且协同的多 GPU 页面预取器

**所属 Session：** [Session 9B](index.md) · [ISCA 2026](../index.md)

**作者：** Xiangyue Huang, Yanan Guo, Yuanchao Xu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Multi-GPU systems increasingly rely on unified virtual memory to satisfy the growing memory demands of modern applications. However, their performance is often limited by non-coherent Non-Uniform Memory Access overheads, where remote accesses are costly and page migration can introduce substantial data-movement overhead. Existing migration techniques are either reactive, placing migration on the critical path, or predictive but designed mainly for CPU-GPU settings. In multi-GPU environments, existing methods, such as NVIDIA’s Tree-Based Neighboring Prefetcher and its variants, suffer from low accuracy, overlook the trade-off between remote access and migration, and may cause ping-pong page movements across GPUs. To address these limitations, we propose LIBRA, an access-pattern-aware, cost-aware, and coordinated page prefetcher for multi-GPU systems. LIBRA uses stride-based prediction to identify GPU memory access patterns, estimates future access benefits to guide migration decisions, and coordinates requests across GPUs based on predicted demand and current page locations. Comprehensive evaluations demonstrate that LIBRA significantly improves performance, outperforming state-of-the-art reactive (GRIT) and predictive (Forest) migration methods by 30% and 35%, respectively.

## 中文摘要

多 GPU 系统越来越依赖统一虚拟内存来满足现代应用不断增长的内存需求。然而，其性能往往受限于非一致性非均匀内存访问开销，此类开销中远程访问代价高昂，且页面迁移会引入大量数据移动开销。现有的迁移技术要么是反应式的，将迁移置于关键路径上，要么是预测式的，但主要针对 CPU-GPU 场景设计。在多 GPU 环境中，现有方法（如 NVIDIA 的基于树的邻近预取器及其变体）存在精度低、忽视远程访问与迁移之间权衡的问题，并可能导致跨 GPU 的页面乒乓移动。为解决这些局限，我们提出 LIBRA，一个面向多 GPU 系统的访问模式感知、成本感知且协调的页面预取器。LIBRA 使用基于步长的预测来识别 GPU 内存访问模式，估计未来访问收益以指导迁移决策，并基于预测需求和当前页面位置在 GPU 之间协调请求。综合评估表明，LIBRA 显著提升了性能，分别比最先进的反应式（GRIT）和预测式（Forest）迁移方法高出 30% 和 35%。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9B](index.md) · [返回 ISCA 2026](../index.md)
