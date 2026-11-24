---
title: "Tela: A Temporal Load-Aware Cloud Virtual Disk Placement Scheme"
description: "ASPLOS 2025 · Session 4A · Tela：一种时序负载感知的云虚拟磁盘放置方案"
tags:
  - "ASPLOS2025"
  - "Session 4A"
  - "Cloud Computing 2"
---

# Tela: A Temporal Load-Aware Cloud Virtual Disk Placement Scheme

**中文标题：** Tela：一种时序负载感知的云虚拟磁盘放置方案

**所属 Session：** [Session 4A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Difan Tan (Huazhong University of Science and Technology), Jiawei Li (Huazhong University of Science and Technology), Hua Wang (Huazhong University of Science and Technology), Xiaoxiao Li (Huazhong University of Science and Technology), Wenbo Liu (Huazhong University of Science and Technology), Zijin Qin (Huazhong University of Science and Technology), Ke Zhou (Huazhong University of Science and Technology), Ming Xie (Tencent Inc.), Mengling Tao (Tencent Inc.)

**单位：** Huazhong University of Science and Technology；Tencent Inc.

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707252) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Cloud Block Storage (CBS) relies on Cloud Virtual Disks (CVDs) to provide block interfaces to Cloud Virtual Machines. The process of allocating user-subscribed CVDs to physical storage warehouses in cloud data centers, known as CVD placement, significantly impacts resource utilization, load balancing, and I/O performance. However, previous works have failed to account for temporal fluctuations in cloud loads, resulting in imbalanced loads, low resource utilization, and frequent warehouse overloads. To address these issues, we propose TELA, the first temporal load-aware CVD placement scheme. Using a series of interpretable models, TELA predicts the temporal load characteristics and values of CVDs, as well as potential peak loads in warehouses. Guided by these predictions, TELA places CVDs into warehouses according to their load patterns, aiming for peak shaving and load balancing while preventing overloads. Experimental results show that TELA significantly outperforms the state-of-the-art scheme, reducing overload occurrences by 86.8~93.8%, reducing P99 overload duration by 92.6%, and decreasing load imbalance by 36.7~44.4%.

## 中文摘要

云块存储（CBS）依赖云虚拟磁盘（CVD）为云虚拟机提供块接口。将用户订购的 CVD 分配到云数据中心的物理存储仓库的过程被称为 CVD 放置，它显著影响资源利用率、负载均衡和 I/O 性能。然而，已有工作未能考虑云负载的时序波动，导致负载不均衡、资源利用率低以及仓库频繁过载。为解决这些问题，我们提出 TELA，首个时序负载感知的 CVD 放置方案。TELA 使用一系列可解释模型预测 CVD 的时序负载特征与取值，以及仓库中潜在的峰值负载。在这些预测的引导下，TELA 依据 CVD 的负载模式将其放入仓库，旨在削峰和负载均衡，同时防止过载。实验结果表明，TELA 显著优于最先进的方案，将过载发生次数降低 86.8~93.8%，将 P99 过载持续时间降低 92.6%，并将负载不均衡度降低 36.7~44.4%。

## 英文关键词

Cloud Block Storage, Resource Management, Load Balancing

## 中文关键词

云块存储；资源管理；负载均衡

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707252)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4A](index.md) · [返回 ASPLOS 2025](../index.md)
