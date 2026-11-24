---
title: "DPack: Efficiency-Oriented Privacy Budget Scheduling"
description: "EuroSys 2025 · Security and Privacy · Pierre Tholoniat (Columbia University), Kelly Kostopoulou (Columbia University),"
tags:
  - "EuroSys2025"
  - "Security and Privacy"
---

# DPack: Efficiency-Oriented Privacy Budget Scheduling

**中文标题：** 面向效率的隐私预算调度

**所属 Session：** [Session 9.1: Security and Privacy](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Security and Privacy。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Security and Privacy</p>
</div>

**作者**：Pierre Tholoniat (Columbia University), Kelly Kostopoulou (Columbia University), Mosharaf Chowdhury (University of Michigan), Asaf Cidon (Columbia University), Roxana Geambasu (Columbia University), Mathias Lécuyer (University of British Columbia), Junfeng Yang (Columbia University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696096)

## 英文摘要

Machine learning (ML) models can leak information about users, and differential privacy (DP) provides a rigorous way to bound that leakage under a given budget. This DP budget can be regarded as a new type of computing resource in workloads of multiple ML models training on user data. Once it is used, the DP budget is forever consumed. Therefore, it is crucial to allocate it most efficiently to train as many models as possible. This paper presents a scheduler for the privacy resources that optimizes for efficiency. We formulate privacy scheduling as a new type of multidimensional knapsack problem, called privacy knapsack, which maximizes DP budget efficiency. We show that privacy knapsack is NP-hard, hence practical algorithms are necessarily approximate. We develop an approximation algorithm for privacy knapsack, DPack, and evaluate it on microbenchmarks and on a new, synthetic private-ML workload we developed from the Alibaba ML cluster trace. We show that DPack: (1) often approaches the efficiency-optimal schedule, (2) consistently schedules more tasks compared to a state-of-the-art privacy scheduling algorithm that focused on fairness instead of efficiency (1.3–1.7× in Alibaba, 1.0–2.6× in microbenchmarks), but (3) sacrifices some level of fairness for efficiency. Using DPack, DP ML operators should be able to train more models on the same amount of user data while offering the same privacy guarantee to their users.

## 中文摘要

机器学习（ML）模型可能泄露用户信息，而差分隐私（DP）提供了一种严格的方式来约束给定预算下的这种泄露。在多个 ML 模型基于用户数据训练的工作负载中，这一 DP 预算可视为一种新型计算资源。DP 预算一旦被使用便永久消耗。因此，如何以最高效率分配它以训练尽可能多的模型至关重要。本文提出一种面向隐私资源的调度器，以效率为优化目标。我们将隐私调度建模为一类新的多维背包问题，称为隐私背包，它最大化 DP 预算效率。我们证明隐私背包是 NP 难的，因此实用算法必然是近似算法。我们为隐私背包开发了一种近似算法 DPack，并在微基准测试以及我们基于阿里巴巴 ML 集群跟踪数据构建的新合成隐私 ML 工作负载上对其进行评估。我们表明 DPack：（1）常常接近效率最优的调度；（2）相比关注公平而非效率的最先进隐私调度算法始终调度更多任务（在阿里巴巴中为 1.3–1.7 倍，在微基准中为 1.0–2.6 倍），但（3）为效率牺牲了一定程度的公平性。借助 DPack，DP ML 运营者应能在相同数量的用户数据上训练更多模型，同时为用户提供同等的隐私保证。

**英文关键词：** Differential Privacy, Scheduling

**中文关键词：** 差分隐私、调度

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
