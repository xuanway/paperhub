---
title: "Load and MLP-Aware Thread Orchestration for Recommendation Systems Inference on CPUs"
description: "ASPLOS 2025 · Session 6A · 面向 CPU 上推荐系统推理的负载与 MLP 感知线程编排"
tags:
  - "ASPLOS2025"
  - "Session 6A"
  - "ML Systems 2"
---

# Load and MLP-Aware Thread Orchestration for Recommendation Systems Inference on CPUs

**中文标题：** 面向 CPU 上推荐系统推理的负载与 MLP 感知线程编排

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Rishabh Jain (The Pennsylvania State University), Teyuh Chou (Advanced Micro Devices, Inc.), Onur Kayiran (Advanced Micro Devices, Inc.), John Kalamatianos (Advanced Micro Devices, Inc.), Gabriel H. Loh (Advanced Micro Devices, Inc.), Mahmut T. Kandemir (The Pennsylvania State University), Chita R. Das (The Pennsylvania State University)

**单位：** The Pennsylvania State University；Advanced Micro Devices, Inc.

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716003) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Recommendation models can enhance consumer experiences and are one of the most frequently used machine learning models in data centers. The deep learning recommendation model (DLRM) is one such key workload. While DLRMs are often trained using GPUs, CPUs can be a cost-effective solution for inference. Therefore, optimizing DLRM inference for CPUs is an important research problem with significant business value. In this work, we identify several shortcomings of existing DLRM parallelization techniques, which can include load imbalance across CPU chiplets, suboptimal core allocation for embedding tables, and inefficient utilization of memorylevel parallelism (MLP) resources. We propose a novel thread scheduler, called “Balance,” that addresses those shortcomings by (1) minimizing core allocation per embedding table to maximize core utilization, (2) using MLP-aware task scheduling based on the characteristics of the embedding tables to better utilize memory bandwidth, and (3) combining work stealing and table reordering mechanisms to reduce load imbalance across CPU chiplets. We evaluate Balance on real hardware with production DLRM traces and demonstrate up to a 1.67× higher speedup over prior state-of-the-art DLRM parallelization techniques with 96 cores. Further, Balance consistently achieves 1.22× higher performance over a range of batch sizes.

## 中文摘要

推荐模型能够提升消费者体验，是数据中心中最常用的机器学习模型之一。深度学习推荐模型（DLRM）正是这样一类关键工作负载。虽然 DLRM 通常使用 GPU 进行训练，但 CPU 可以是具有成本效益的推理方案。因此，针对 CPU 优化 DLRM 推理是一个具有重大商业价值的重要研究问题。在本工作中，我们指出现有 DLRM 并行化技术的若干不足，可能包括 CPU chiplet 之间的负载不均衡、嵌入表的核心分配次优，以及内存级并行（MLP）资源利用低效。我们提出一种新颖的线程调度器，称为“Balance”，它通过以下方式解决这些不足：（1）最小化每个嵌入表的核心分配，以最大化核心利用率；（2）基于嵌入表的特征采用 MLP 感知的任务调度，以更好地利用内存带宽；（3）结合工作窃取与表重排序机制，以减少 CPU chiplet 之间的负载不均衡。我们在真实硬件上使用生产环境的 DLRM 跟踪对 Balance 进行评估，结果表明：在 96 核上，相较先前最先进的 DLRM 并行化技术最高可实现 1.67 倍的加速。此外，Balance 在一系列批大小下始终实现 1.22 倍的性能提升。

## 英文关键词

Recommendation Systems, Embedding Bag Kernel, Parallelization, Memory Bound, Multi-cores, Thread Scheduling, Load Balancing

## 中文关键词

推荐系统；Embedding Bag 内核；并行化；内存受限；多核；线程调度；负载均衡

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716003)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6A](index.md) · [返回 ASPLOS 2025](../index.md)
