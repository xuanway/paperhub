---
title: "TAC: Cache-Based System for Accelerating Billion-Scale GNN Training on Multi-GPU Platform"
description: "PPoPP 2026 Session 11（Graphs and Graph Neural Networks）：数据亲和 + 稀疏感知算子，多基准超越 SOTA 缓存系统"
tags:
  - "PPoPP2026"
  - "Session-11"
  - "Graphs and Graph Neural Networks"
  - "GNN Training"
  - "Cache"
  - "Multi-GPU"
authors:
  - "Zhiqiang Liang"
  - "Hongyu Gao"
  - "Jue Wang"
  - "Fang Liu"
  - "Xingguo Shi"
  - "Junyu Gu"
  - "Peng Di"
  - "Sian Li"
  - "Lei Tang"
  - "Chunbao Zhou"
  - "Lian Zhao"
  - "Yangang Wang"
  - "Xuebin Chi"
session: "Session 11: Graphs and Graph Neural Networks"
session_number: 11
session_chair: "Ali Jannesari"
date: "2026-02-03"
time: "16:30–16:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786460"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# TAC: Cache-Based System for Accelerating Billion-Scale GNN Training on Multi-GPU Platform

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 TAC，面向十亿级图多 GPU 训练的缓存加速系统，用数据亲和性优化、自适应稀疏算子与细粒度流水线充分利用缓存数据分布特性，显著超越现有系统。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 11: Graphs and Graph Neural Networks</p>
</div>

**作者**：Zhiqiang Liang, Hongyu Gao, Jue Wang, Fang Liu, Xingguo Shi, Junyu Gu, Peng Di, Sian Li, Lei Tang, Chunbao Zhou, Lian Zhao, Yangang Wang, and Xuebin Chi — Computer Network Information Center at Chinese Academy of Sciences, China; University of Chinese Academy of Sciences, China; Ant Group, China; UNSW, Australia

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 16:30–16:50 · Session 11: Graphs and Graph Neural Networks（主席：Ali Jannesari）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786460) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Graph neural networks (GNNs) have been proven to have increasingly widespread applications in the real world. In the mainstream mini-batch training mode, multiple cache-based GNN training acceleration systems have been proposed because of the possibility of selecting the same vertex multiple times during the sampling process. However, on ultra-large scale graphs, especially those exhibiting power-law characteristics, these systems are difficult to fully utilize the distribution characteristics of cached data, which limits training performance. To this end, we propose TAC, a GNN training acceleration system that fully exploits the distribution characteristics of cached data to optimize both data transmission and computational efficiency. Specifically, we have designed a data affinity optimization algorithm that significantly enhances the locality of cache access. Secondly, an adaptive sparse matrix operator for sparsity perception is proposed, which dynamically selects the optimal computing mode based on the location of data. Finally, we have constructed a fine-grained training pipeline that maximizes system parallelism by hiding the sampling and computation. The experimental results show that TAC significantly outperforms existing state-of-the-art cache acceleration systems on multiple benchmark datasets, demonstrating higher training efficiency.

## 中文摘要

图神经网络（GNN）已被证明在真实世界中有着日益广泛的应用。在主流的 mini-batch 训练模式下，由于采样过程中同一顶点可能被多次选中，已有多个基于缓存的 GNN 训练加速系统被提出。然而在超大规模图上，尤其是呈现幂律特征的图，这些系统难以充分利用缓存数据的分布特征，从而限制了训练性能。为此，我们提出 TAC，一个充分利用缓存数据分布特征来同时优化数据传输与计算效率的 GNN 训练加速系统。具体而言，我们设计了一种数据亲和性优化算法，显著增强缓存访问的局部性。其次，提出了面向稀疏性感知的自适应稀疏矩阵算子，它根据数据所在位置动态选择最优计算模式。最后，我们构建了细粒度的训练流水线，通过隐藏采样与计算来最大化系统并行度。实验结果表明，TAC 在多个基准数据集上显著优于现有最先进的缓存加速系统，展现出更高的训练效率。

## 英文关键词

Graph Neural Networks, Cache-based System, Sparse Matrix-Matrix Multiplication, Pipeline

## 中文关键词

图神经网络；基于缓存的系统；稀疏矩阵乘法（SpMM）；流水线

---

## 一句话总结

> 提出 TAC，面向十亿级图多 GPU 训练的缓存加速系统，用数据亲和性优化、自适应稀疏算子与细粒度流水线充分利用缓存数据分布特性，显著超越现有系统。

## 研究问题

在超大规模图、尤其呈幂律分布的图上，现有基于缓存的 GNN 训练加速系统难以充分利用缓存数据的分布特性，限制了训练性能。

## 方法简述

- 设计数据亲和性优化算法，显著增强缓存访问的局部性。
- 提出稀疏度感知的自适应稀疏矩阵算子，根据数据所在位置动态选择最优计算模式。
- 构建细粒度训练流水线，通过隐藏采样与计算来最大化系统并行度。

## 主要结果

- 在多个基准数据集上显著优于现有最先进的缓存加速系统，训练效率更高（摘要为定性结论）。
- 细粒度流水线通过隐藏采样与计算提升系统并行度，缓存数据分布特性被充分利用。

---

> 所属 Session：[Session 11: Graphs and Graph Neural Networks](index.md) · 返回 [PPoPP 2026 总览](../index.md)
