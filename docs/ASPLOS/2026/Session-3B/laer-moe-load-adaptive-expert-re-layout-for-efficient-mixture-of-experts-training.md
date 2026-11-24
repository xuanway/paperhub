---
title: "LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training"
description: "ASPLOS 2026 · Session 3B · LAER-MoE：面向高效混合专家训练的自适应负载专家重布局"
tags:
  - "ASPLOS2026"
  - "Session 3B"
  - "Mixture-of-Experts & Efficient Inference"
---

# LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training

**中文标题：** LAER-MoE：面向高效混合专家训练的自适应负载专家重布局

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xinyi Liu (Peking University), Yujie Wang (Peking University), Fangcheng Fu (Shanghai Jiao Tong University), Xuefeng Xiao (Bytedance Seed), Huixia Li (Bytedance Seed), Jiashi Li (Bytedance Seed), Bin Cui (Peking University)

**单位：** Peking University；Shanghai Jiao Tong University；Bytedance Seed

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790180) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Expert parallelism is vital for effectively training Mixtureof-Experts (MoE) models, enabling different devices to host distinct experts, with each device processing different input data. However, during expert parallel training, dynamic routing results in significant load imbalance among experts: a handful of overloaded experts hinder overall iteration, emerging as a training bottleneck. In this paper, we introduce LAER-MoE, an efficient MoE training framework. The core of LAER-MoE is a novel parallel paradigm, Fully Sharded Expert Parallel (FSEP), which fully partitions each expert parameter by the number of devices and restores partial experts at expert granularity through All-to-All communication during training. This allows for flexible re-layout of expert parameters during training to enhance load balancing. In particular, we perform fine-grained scheduling of communication operations to minimize communication overhead. Additionally, we develop a load balancing planner to formulate re-layout strategies of experts and routing schemes for tokens during training. We perform experiments on an A100 cluster, and the results indicate that our system achieves up to 1.69x acceleration compared to the current state-of-the-art training systems. Source code available at ∗School of Computer Science & Beijing Key Laboratory of Software and Hardware Cooperative Artificial Intelligence Systems, Peking University †School of Artificial Intelligence, Shanghai Jiao Tong University ‡Institute of Computational Social Science, Peking University (Qingdao)

## 中文摘要

专家并行对于有效训练混合专家（MoE）模型至关重要，它使不同设备托管不同的专家，并让每个设备处理不同的输入数据。然而，在专家并行训练过程中，动态路由会导致专家之间出现显著的负载不均衡：少数过载专家拖慢整体迭代，成为训练瓶颈。本文提出 LAER-MoE，一个高效的 MoE 训练框架。LAER-MoE 的核心是一种新颖的并行范式——完全分片专家并行（FSEP），它按设备数量对每个专家的参数进行完全切分，并在训练期间通过 All-to-All 通信以专家为粒度恢复部分专家。这使得训练期间可以灵活地重布局专家参数，从而增强负载均衡。特别地，我们对通信操作进行细粒度调度以最小化通信开销。此外，我们设计了一个负载均衡规划器，用于在训练期间制定专家的重布局策略和 token 的路由方案。我们在 A100 集群上进行了实验，结果表明我们的系统相比当前最先进的训练系统实现了最高 1.69 倍的加速。源代码可在∗北京大学计算机学院与软硬件协同人工智能系统北京重点实验室、†上海交通大学人工智能学院、‡北京大学（青岛）计算社会科学研究院获取。

## 英文关键词

Mixture-of-Experts, Load Balancing, Distributed Training, Expert Parallelism, Large Language Models

## 中文关键词

混合专家；负载均衡；分布式训练；专家并行；大语言模型

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790180)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2026](../index.md)
