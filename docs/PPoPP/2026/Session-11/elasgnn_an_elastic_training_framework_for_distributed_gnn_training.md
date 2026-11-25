---
title: "ElasGNN: An Elastic Training Framework for Distributed GNN Training"
description: "PPoPP 2026 Session 11（Graphs and Graph Neural Networks）：弹性扩缩容 + 图重划分降代价，缩短完成时间与 makespan"
tags:
  - "PPoPP2026"
  - "Session-11"
  - "Graphs and Graph Neural Networks"
  - "GNN Training"
  - "Elastic Training"
  - "Graph Repartitioning"
authors:
  - "Siqi Wang"
  - "Hailong Yang"
  - "Pengbo Wang"
  - "Hongliang Cao"
  - "Yufan Xu"
  - "Xuezhu Wang"
  - "Zhongzhi Luan"
  - "Yi Liu"
  - "Depei Qian"
session: "Session 11: Graphs and Graph Neural Networks"
session_number: 11
session_chair: "Ali Jannesari"
date: "2026-02-03"
time: "15:50–16:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786440"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# ElasGNN: An Elastic Training Framework for Distributed GNN Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 ElasGNN，弹性分布式 GNN 训练框架，通过弹性训练引擎、面向扩缩容的图重划分算法与代价感知调度器实现动态资源分配，缩短作业完成时间与 makespan。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 11: Graphs and Graph Neural Networks</p>
</div>

**作者**：Siqi Wang, Hailong Yang, Pengbo Wang, Hongliang Cao, Yufan Xu, Xuezhu Wang, Zhongzhi Luan, Yi Liu, and Depei Qian — Beihang University, China; Independent Researcher, USA

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 15:50–16:10 · Session 11: Graphs and Graph Neural Networks（主席：Ali Jannesari）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786440) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Graph Neural Networks (GNNs) have emerged as powerful machine learning models for numerous graph-based applications. However, existing GNN training frameworks cannot scale the training process elastically, resulting in poor training throughput and low cluster utilization. Although elastic training has been proposed for Deep Neural Networks (DNNs), it cannot be directly adopted to GNNs due to the prohibitive scaling cost and inefficient scheduling. In this paper, we present ElasGNN, an elastic GNN training framework that achieves efficient dynamic resource allocation for GNN jobs. ElasGNN proposes an efficient elastic training engine to achieve high-performant GNN job scaling and introduces novel graph repartitioning algorithms for both scale-in and scale-out processes to further minimize the scaling cost. Moreover, ElasGNN designs an efficient elastic scheduler, utilizing a scaling-cost-aware scheduling policy to improve the GPU utilization and system throughput. The experimental results show that the ElasGNN can achieve shorter job completion time and makespan for training jobs of diverse GNN models.

## 中文摘要

图神经网络（GNN）已成为众多基于图的应用中有力的机器学习模型。然而，现有的 GNN 训练框架无法弹性伸缩训练过程，导致训练吞吐不佳、集群利用率低。尽管针对深度神经网络（DNN）已提出弹性训练，但由于伸缩成本过高且调度效率低下，这些方法无法直接用于 GNN。本文提出 ElasGNN，一个弹性 GNN 训练框架，可为 GNN 作业实现高效的动态资源分配。ElasGNN 提出高效的弹性训练引擎，以实现高性能的 GNN 作业伸缩，并针对缩容（scale-in）与扩容（scale-out）过程引入了新的图重划分算法，进一步降低伸缩成本。此外，ElasGNN 设计了高效的弹性调度器，采用伸缩成本感知的调度策略，以提高 GPU 利用率与系统吞吐。实验结果表明，对于多种 GNN 模型的训练作业，ElasGNN 都能取得更短的作业完成时间与 makespan。

## 英文关键词

GNN Training, Elastic Training, Job Scaling

## 中文关键词

GNN 训练；弹性训练；作业伸缩

---

## 一句话总结

> 提出 ElasGNN，弹性分布式 GNN 训练框架，通过弹性训练引擎、面向扩缩容的图重划分算法与代价感知调度器实现动态资源分配，缩短作业完成时间与 makespan。

## 研究问题

现有 GNN 训练框架无法弹性伸缩，导致训练吞吐低、集群利用率低；DNN 的弹性训练方案又因扩缩容代价过高和调度低效，无法直接移植到 GNN。

## 方法简述

- 提出高效的弹性训练引擎，实现高性能的 GNN 作业扩缩容。
- 为缩容（scale-in）与扩容（scale-out）过程分别设计新的图重划分算法，进一步降低扩缩容代价。
- 设计高效弹性调度器，采用扩缩容代价感知的调度策略提升 GPU 利用率与系统吞吐。

## 主要结果

- 对多种 GNN 模型的训练作业取得更短的作业完成时间与 makespan。
- 提升 GPU 利用率与系统吞吐（摘要为定性结论）。

---

> 所属 Session：[Session 11: Graphs and Graph Neural Networks](index.md) · 返回 [PPoPP 2026 总览](../index.md)
