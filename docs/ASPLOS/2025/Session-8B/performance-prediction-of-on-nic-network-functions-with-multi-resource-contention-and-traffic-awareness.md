---
title: "Performance Prediction of On-NIC Network Functions with Multi-Resource Contention and Traffic Awareness"
description: "ASPLOS 2025 · Session 8B · 面向 SmartNIC 网络功能的多资源竞争与流量感知性能预测"
tags:
  - "ASPLOS2025"
  - "Session 8B"
  - "Networking"
---

# Performance Prediction of On-NIC Network Functions with Multi-Resource Contention and Traffic Awareness

**中文标题：** 面向 SmartNIC 网络功能的多资源竞争与流量感知性能预测

**所属 Session：** [Session 8B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shaofeng Wu (The Chinese University of Hong Kong), Qiang Su (The Chinese University of Hong Kong), Zhixiong Niu (Microsoft Research), Hong Xu (The Chinese University of Hong Kong)

**单位：** The Chinese University of Hong Kong；Microsoft Research

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707232) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Network function (NF) offloading on SmartNICs has been widely used in modern data centers, offering benefits in host resource saving and programmability. Co-running NFs on the same SmartNICs can cause performance interference due to contention of onboard resources. To meet performance SLAs while ensuring efficient resource management, operators need mechanisms to predict NF performance under such contention. However, existing solutions lack SmartNICspecific knowledge and exhibit limited traffic awareness, leading to poor accuracy for on-NIC NFs. This paper proposes Yala, a novel performance predictive system for on-NIC NFs. Yala builds upon the key observation that co-located NFs contend for multiple resources, including onboard accelerators and the memory subsystem. It also facilitates traffic awareness according to the behaviors of individual resources to maintain accuracy as the external traffic attributes vary. Evaluation using BlueField-2 SmartNICs shows that Yala improves the prediction accuracy by 78.8% and reduces SLA violations by 92.2% compared to state-of-the-art approaches, and enables new practical usecases.

## 中文摘要

在现代数据中心中，将网络功能（NF）卸载到 SmartNIC 上已被广泛采用，在节省主机资源和可编程性方面具有优势。在同一块 SmartNIC 上共同运行多个 NF 会因板载资源竞争而造成性能干扰。为在满足性能 SLA 的同时保证高效的资源管理，运维人员需要能够在此类竞争下预测 NF 性能的机制。然而，现有方案缺乏针对 SmartNIC 的专门知识，且流量感知能力有限，导致对片上 NF 的预测精度较差。本文提出 Yala，一种面向片上 NF 的新型性能预测系统。Yala 建立在这样一个关键观察之上：共置的 NF 会竞争多种资源，包括板载加速器和存储子系统。它还依据各个单独资源的行为实现流量感知，从而在外部流量特征变化时保持精度。基于 BlueField-2 SmartNIC 的评估表明，与最先进的方法相比，Yala 将预测精度提升了 78.8%，并将 SLA 违例减少了 92.2%，同时支撑了新的实用场景。

## 英文关键词

Network Function, SmartNIC, Resource Contention, Performance Prediction

## 中文关键词

网络功能；SmartNIC；资源竞争；性能预测

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707232)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8B](index.md) · [返回 ASPLOS 2025](../index.md)
