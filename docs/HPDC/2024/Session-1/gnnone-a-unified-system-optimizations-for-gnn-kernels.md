---
title: "GNNOne: A Unified System Optimizations for GNN Kernels"
description: "HPDC 2024 · Session 1 — Compression and AI"
tags:
  - "HPDC2024"
  - "Session 1"
  - "Compression and AI"
---

# GNNOne: A Unified System Optimizations for GNN Kernels

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 1 — Compression and AI（2024年6月5日 11:20–13:00 · Session Chair：Domenico Talia）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 1</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658655)

**作者**：Yidong Gong, Pradeep Kumar

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 1 — Compression and AI（2024年6月5日 11:20–13:00 · Session Chair：Domenico Talia）

---

## 英文摘要

Graph Neural Networks (GNN) involve two basic sparse kernels, SDDMM and SpMM, on which all GNN models could be built. Prior works have explored piecemeal solutions by using different storage formats and computation paradigms, resulting in excess memory consumption, and have not yet realized their full potential. This paper, called GnnOne, studies these two basic sparse kernels in GPU and shows that they can be built on the same system design principle of data load being the limiting factor irrespective of their computing paradigms. Hence GnnOne presents a unified two-stage data-load design that provides greater performance through novel techniques of data-load balancing, data-load optimizations, and data-reuse. Such a unified design also enables the usage of a single sparse storage format to increase productivity, memory saving, and reduce maintenance. Evaluations show that the proposed system achieves an average speedup of 6.25× and 6.02× for SpMM and SDDMM over many prior works for different feature lengths. For GNN training, GnnOne achieves 2.01× average speedup over dgNN, 2.28× average speedup over DGL on 3 different GNN models.

## 中文摘要

图神经网络（GNN）涉及两个基本稀疏核：SDDMM 与 SpMM，所有 GNN 模型都可构建于其上。先前工作探索了使用不同存储格式与计算范式的零散方案，导致过多内存消耗，且尚未发挥其全部潜力。本文（称为 GnnOne）研究 GPU 上的这两个基本稀疏核，并表明无论采用何种计算范式，它们都可建立在同一个系统设计原则之上：数据加载是限制因素。因此，GnnOne 提出一种统一的两阶段数据加载设计，通过数据加载均衡、数据加载优化与数据复用等新技术提供更高性能。这种统一设计还使单一稀疏存储格式得以使用，从而提升生产力、节省内存并减少维护。评估表明，所提系统在不同特征长度下，SpMM 与 SDDMM 相比众多先前工作分别取得 6.25 倍和 6.02 倍的平均加速。在 GNN 训练方面，GnnOne 在 3 个不同 GNN 模型上相比 dgNN 平均加速 2.01 倍，相比 DGL 平均加速 2.28 倍。

## 英文关键词

Graph Neural Networks, GPU, Performance

## 中文关键词

图神经网络，GPU，性能

---

[← 返回 Session 1 — Compression and AI](index.md)
