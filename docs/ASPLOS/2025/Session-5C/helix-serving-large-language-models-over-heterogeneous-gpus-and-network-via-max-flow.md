---
title: "Helix: Serving Large Language Models over Heterogeneous GPUs and Network via Max-Flow"
description: "ASPLOS 2025 · Session 5C · Helix：通过最大流在异构 GPU 与网络上服务大语言模型"
tags:
  - "ASPLOS2025"
  - "Session 5C"
  - "Large Language Models"
---

# Helix: Serving Large Language Models over Heterogeneous GPUs and Network via Max-Flow

**中文标题：** Helix：通过最大流在异构 GPU 与网络上服务大语言模型

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yixuan Mei (Carnegie Mellon University), Yonghao Zhuang (Carnegie Mellon University), Xupeng Miao (Carnegie Mellon University), Juncheng Yang (Carnegie Mellon University), Zhihao Jia (Carnegie Mellon University), Rashmi Vinayak (Carnegie Mellon University)

**单位：** Carnegie Mellon University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707215) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

This paper introduces Helix, a distributed system for highthroughput, low-latency large language model (LLM) serving in heterogeneous GPU clusters. The key idea behind Helix is to formulate inference computation of LLMs over heterogeneous GPUs and network connections as a max-flow problem on directed, weighted graphs, whose nodes represent GPU instances and edges capture both GPU and network heterogeneity through their capacities. Helix then uses a mixed integer linear programming (MILP) algorithm to discover highly optimized strategies to serve LLMs on heterogeneous GPUs. This approach allows Helix to jointly optimize model placement and request scheduling, two highly entangled tasks in heterogeneous LLM serving. Our evaluation on several heterogeneous clusters ranging from 24 to 42 GPU nodes shows that Helix improves serving throughput by up to 3.3× and reduces prompting and decoding latency by up to 66% and 24%, respectively, compared to existing approaches. Helix is

## 中文摘要

本文介绍 Helix，一个用于异构 GPU 集群中高吞吐、低时延大语言模型（LLM）服务的分布式系统。Helix 的核心思想是将异构 GPU 与网络连接上的 LLM 推理计算形式化为有向加权图上的最大流问题，其中节点表示 GPU 实例，边通过其容量刻画 GPU 与网络的异构性。随后，Helix 使用混合整数线性规划（MILP）算法来发现高度优化的策略，以在异构 GPU 上服务 LLM。该方法使 Helix 能够联合优化模型放置与请求调度这两个在异构 LLM 服务中高度纠缠的任务。我们在由 24 至 42 个 GPU 节点构成的多个异构集群上进行的评估表明，与现有方法相比，Helix 将服务吞吐提升至多 3.3×，并将 prompt 时延与解码时延分别最多降低 66% 和 24%。Helix 是

## 英文关键词

large language model serving, system for ML, distributed systems, cloud computing

## 中文关键词

大语言模型服务；机器学习系统；分布式系统；云计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707215)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2025](../index.md)
