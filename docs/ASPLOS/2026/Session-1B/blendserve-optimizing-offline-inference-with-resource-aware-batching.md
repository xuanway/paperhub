---
title: "BlendServe: Optimizing Offline Inference with Resource-Aware Batching"
description: "ASPLOS 2026 · Session 1B · BlendServe：以资源感知批处理优化离线推理"
tags:
  - "ASPLOS2026"
  - "Session 1B"
  - "LLM Serving: Latency & Scheduling"
---

# BlendServe: Optimizing Offline Inference with Resource-Aware Batching

**中文标题：** BlendServe：以资源感知批处理优化离线推理

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yilong Zhao (University of California, Berkeley), Shuo Yang (University of California, Berkeley), Kan Zhu (University of Washington), Lianmin Zheng (UC Berkeley), Baris Kasikci (University of Washington), Yifan Qiao (UC Berkeley), Yang Zhou (UC Berkeley and UC Davis), Jiarong Xing (UC Berkeley and Rice University), Ion Stoica (UC Berkeley)

**单位：** University of California, Berkeley；University of Washington；UC Berkeley；UC Berkeley and UC Davis；UC Berkeley and Rice University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790133) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Offline batch inference is gaining popularity as a cost-effective solution for latency-insensitive tasks, such as model evaluation and data curation. As the latency objective is highly relaxed, maximizing throughput becomes the primary goal in offline inference. Previous studies focused solely on optimizing throughput within a batch. However, the diverse resource demands (compute-intensive vs. memory-intensive) across a wide range of applications make these approaches less effective, as imbalanced resource demands between batches restrict optimization opportunities. Our insight for achieving optimal throughput is to reorder requests into batches that mix compute- and memory-intensive workloads to maximize resource overlap. However, such a request schedule can conflict with the schedule that maximizes prefix sharing, a widely-used performance optimization, causing suboptimal inference throughput. In this paper, we first build a performance model to analyze request resource demands. Based on it, we design BlendServe, which harmonizes both resource overlapping and prefix sharing to maximize throughput. BlendServe organizes all requests using a resource-aware prefix tree and proposes a dual scanning algorithm to obtain the request schedule. Our evaluation on various models and workloads shows that BlendServe can achieve up to 90% of the optimal throughput.

## 中文摘要

离线批量推理正作为一种面向延迟不敏感任务（如模型评估与数据整理）的高性价比方案而日益流行。由于延迟目标被大幅放宽，最大化吞吐量成为离线推理的首要目标。以往的研究仅关注在单个批次内优化吞吐量。然而，各类应用中多样的资源需求（计算密集型与内存密集型）使这些方法效果不佳，因为批次之间不均衡的资源需求限制了优化机会。我们实现最优吞吐量的洞见在于：将请求重排为混合计算密集型与内存密集型工作负载的批次，以最大化资源重叠。然而，这样的请求调度可能与最大化前缀共享（一种广泛使用的性能优化）的调度相冲突，导致推理吞吐量次优。本文首先构建性能模型来分析请求的资源需求。基于该模型，我们设计了 BlendServe，它协调资源重叠与前缀共享以最大化吞吐量。BlendServe 使用资源感知前缀树组织所有请求，并提出一种双重扫描算法来获得请求调度。在多种模型与工作负载上的评估表明，BlendServe 可达到最优吞吐量的最高 90%。

## 英文关键词

Large Language Models; Offline Inference

## 中文关键词

大语言模型；离线推理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790133)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2026](../index.md)
