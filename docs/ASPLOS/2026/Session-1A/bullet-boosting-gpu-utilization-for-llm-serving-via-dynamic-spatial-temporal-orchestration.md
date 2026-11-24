---
title: "Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration"
description: "ASPLOS 2026 · Session 1A · Bullet：通过动态时空编排提升 LLM 服务中的 GPU 利用率"
tags:
  - "ASPLOS2026"
  - "Session 1A"
  - "LLM Serving: Throughput Optimization"
---

# Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration

**中文标题：** Bullet：通过动态时空编排提升 LLM 服务中的 GPU 利用率

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zejia Lin (Sun Yat-sen University), Hongxin Xu (Sun Yat-sen University), Guanyi Chen (Sun Yat-sen University), Zhiguang Chen (Sun Yat-sen University), Yutong Lu (Sun Yat-sen University), Xianwei Zhang (Sun Yat-sen University)

**单位：** Sun Yat-sen University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790135) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Modern large language model (LLM) serving systems confront inefficient GPU utilization due to the fundamental mismatch between compute-intensive prefill phase and memory-bound decode phase. While current practices attempt to address this by organizing these phases into hybrid batches, such solutions create an inefficient tradeoff that sacrifices either throughput or latency, leaving substantial GPU resources underutilized. For this, we identify two key root causes: 1) the prefill phase suffers from suboptimal compute utilization due to wave quantization and attention bottlenecks, and 2) hybrid batching disproportionately prioritizes latency over throughput, wasting both compute resources and memory bandwidth. To mitigate the issues, we present Bullet, a novel spatial-temporal orchestration system that eliminates these inefficiencies through fine-grained phase coordination. Bullet enables concurrent execution of prefill and decode requests, while dynamically provisioning GPU resources based on real-time performance modeling. By integrating SLO-aware scheduling and adaptive resource allocation, Bullet maximizes GPU utilization without compromising latency targets. Experimental evaluations on real-world workloads demonstrate that Bullet delivers 1.26× average throughput gains (up to 1.55×) over state-of-the-arts, while consistently meeting latency constraints.

## 中文摘要

现代大语言模型（LLM）服务系统面临 GPU 利用率低下的问题，其根源在于计算密集的预填充阶段与访存密集的解码阶段之间存在根本性的不匹配。当前实践试图通过将这两个阶段组织为混合批次来应对该问题，但此类方案造成了低效的权衡：或以牺牲吞吐为代价，或以牺牲延迟为代价，使大量 GPU 资源处于未充分利用状态。为此，我们识别出两个关键根因：1）预填充阶段受波量化（wave quantization）与注意力瓶颈影响，计算利用率欠佳；2）混合批处理过度偏重延迟而轻视吞吐，同时浪费了计算资源与内存带宽。为缓解这些问题，我们提出 Bullet，一种新颖的时空编排系统，通过细粒度的阶段协同消除上述低效。Bullet 支持预填充请求与解码请求的并发执行，并基于实时性能建模动态供给 GPU 资源。通过融合 SLO 感知调度与自适应资源分配，Bullet 在不牺牲延迟目标的前提下最大化 GPU 利用率。在真实工作负载上的实验评估表明，Bullet 相较当前最先进方案带来平均 1.26× 的吞吐提升（最高 1.55×），并始终满足延迟约束。

## 英文关键词

Large language models; GPU; Inference serving

## 中文关键词

大语言模型；GPU；推理服务

## 代码与研究制品

- [代码仓库](https://github.com/zejia-lin/BulletServe)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790135)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2026](../index.md)
