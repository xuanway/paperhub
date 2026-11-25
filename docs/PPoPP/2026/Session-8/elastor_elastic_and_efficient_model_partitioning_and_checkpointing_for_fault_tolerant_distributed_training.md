---
title: "Elastor: Elastic and Efficient Model Partitioning and Checkpointing for Fault-Tolerant Distributed Training"
description: "PPoPP 2026 Session 8（Distributed Training）：异构划分+划分无关细粒度检查点，任意 GPU 数弹性恢复"
tags:
  - "PPoPP2026"
  - "Session-8"
  - "Distributed Training"
  - "fault tolerance"
  - "checkpointing"
  - "elastic training"
authors:
  - "Xuanyu Wang"
  - "Fangcheng Fu"
  - "Haoyang Li"
  - "Hao Ge"
  - "Sheng Lin"
  - "Jiawen Niu"
  - "Bin Cui"
session: "Session 8: Distributed Training"
session_number: 8
session_chair: "Bo Fang"
date: "2026-02-03"
time: "14:30–14:50"
room: "Balmoral"
doi: "10.1145/3774934.3786445"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Elastor: Elastic and Efficient Model Partitioning and Checkpointing for Fault-Tolerant Distributed Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出容错训练系统 Elastor，支持异构模型并行划分与划分无关的细粒度张量检查点，使训练可在任意数量 GPU 上弹性恢复并保持一致的训练效率。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 8: Distributed Training</p>
</div>

**作者**：Xuanyu Wang, Fangcheng Fu, Haoyang Li, Hao Ge, Sheng Lin, Jiawen Niu, and Bin Cui — Peking University, China; Shanghai Jiao Tong University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 14:30–14:50 · Session 8: Distributed Training（主席：Bo Fang）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786445) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Distributed deep learning (DL) training faces instability from GPU/node failures of multi-GPU clusters, necessitating robust fault recovery from model checkpoints. However, we find that existing works only consider node failures but fail to handle partial GPU unavailability, and they suffer from inefficient model checkpoint saving and loading, particularly when the GPU availability changes. This work presents Elastor, a fault-tolerant distributed DL training system featuring elastic and efficient model checkpointing. Firstly, to accommodate partial GPU unavailability, we manage to support heterogeneous model parallel partitioning to elastically resume training with any number of GPUs. Secondly, we devise a partition-agnostic and efficient model checkpointing method via fine-grained tensor splits to achieve seamless transitions across arbitrary partitioning. In addition, Elastor is equipped with a strategy searching algorithm that automatically discovers optimal model partitioning upon recovery as well as a meticulous overlapping design that minimizes the overhead caused by periodic model checkpointing and data preprocessing. Experimental results show that Elastor facilitates quick model checkpointing and failure recovery, while maintaining consistent training efficiency across varying GPU availability. Source code is available at https://github.com/PKU-DAIR/Hetu.

## 中文摘要

分布式深度学习（DL）训练因多 GPU 集群的 GPU/节点故障而不稳定，因此需要从模型检查点进行稳健的故障恢复。然而，我们发现已有工作仅考虑节点故障，未能处理部分 GPU 不可用的情况，而且模型检查点的保存与加载效率低下，在 GPU 可用性发生变化时尤为如此。本文提出 Elastor，一个具备弹性且高效的模型检查点能力的容错分布式 DL 训练系统。首先，为适应部分 GPU 不可用的情况，我们设法支持异构模型并行划分，从而能够以任意数量的 GPU 弹性地恢复训练。其次，我们通过细粒度张量切分，设计了一种与划分无关的高效模型检查点方法，实现任意划分之间的无缝切换。此外，Elastor 配备了策略搜索算法，可在恢复时自动发现最优模型划分，并采用精细的重叠设计，最小化周期性模型检查点与数据预处理带来的开销。实验结果表明，Elastor 支持快速的模型检查点与故障恢复，同时在 GPU 可用性变化时保持一致的训练效率。源码见 https://github.com/PKU-DAIR/Hetu。

## 英文关键词

Model Checkpointing, Fault Recovery, Parallel Strategies

## 中文关键词

模型检查点；故障恢复；并行策略

---

## 一句话总结

> 提出容错训练系统 Elastor，支持异构模型并行划分与划分无关的细粒度张量检查点，使训练可在任意数量 GPU 上弹性恢复并保持一致的训练效率。

## 研究问题

分布式训练受 GPU 与节点故障影响而不稳定，而现有工作只考虑节点故障、无法处理部分 GPU 不可用，且 GPU 可用性变化时检查点保存与加载效率低下。

## 方法简述

- 支持异构模型并行划分，使训练能以任意数量的 GPU 弹性恢复。
- 设计划分无关的高效检查点方法，通过细粒度张量切分实现任意划分之间的无缝切换。
- 提出策略搜索算法，在恢复时自动发现最优的模型划分方案。
- 采用精细的重叠设计，最小化周期性模型检查点与数据预处理带来的开销。

## 主要结果

- 实验表明 Elastor 能够实现快速的模型检查点与故障恢复，并在 GPU 可用性变化时保持一致的训练效率（摘要未给出具体量化数值）。

---

> 所属 Session：[Session 8: Distributed Training](index.md) · 返回 [PPoPP 2026 总览](../index.md)
