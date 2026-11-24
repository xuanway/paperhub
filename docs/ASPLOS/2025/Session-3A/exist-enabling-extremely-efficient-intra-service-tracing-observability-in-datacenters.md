---
title: "EXIST: Enabling Extremely Efficient Intra-Service Tracing Observability in Datacenters"
description: "ASPLOS 2025 · Session 3A · EXIST：在数据中心实现极致高效的服务内追踪可观测性"
tags:
  - "ASPLOS2025"
  - "Session 3A"
  - "Performance Analysis & Tracing"
---

# EXIST: Enabling Extremely Efficient Intra-Service Tracing Observability in Datacenters

**中文标题：** EXIST：在数据中心实现极致高效的服务内追踪可观测性

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Xinkai Wang (Shanghai Jiao Tong University), Xiaofeng Hou (Shanghai Jiao Tong University), Chao Li (Shanghai Jiao Tong University), Yuancheng Li (Shanghai Jiao Tong University), Du Liu (Shanghai Jiao Tong University), Guoyao Xu (Alibaba Group), Guodong Yang (Alibaba Group), Liping Zhang (Alibaba Group), Yuemin Wu (Alibaba Cloud), Xiaopeng Yuan (Alibaba Cloud), Quan Chen (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University；Alibaba Group；Alibaba Cloud

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716283) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The complexity of online applications is rapidly increasing, bringing more sophisticated performance anomalies in today's cloud datacenter. To fully understand application behaviors, we should obtain both inter-service communication data via RPC-level tracing and intra-service execution traces via application-level tracing to precisely reason about event causality. However, the average time overhead of existing intra-service tracing schemes on the traced applications is generally about 5-10%, possibly reaching 18% in the worst case. To realize practical intra-service tracing in shared and stressed datacenters, one must achieve extreme tracing efficiency with an overhead at the per-mille level. In this work, we present EXIST, an extremely efficient intra-service tracing system based on off-the-shelf hardware tracing capabilities. EXIST consists of three cooperative modules to pursue optimal trade-offs towards extremely low overhead. Firstly, it identifies and eliminates costly tracing control operations to guarantee the performance of the observed applications. Secondly, it allocates limited trace buffer space dynamically based on application status.. optimizes the trace coverage with cluster-level orchestration. We implement and evaluate EXIST on benchmark and real-world applications thoroughly. EXIST achieves 2-10× efficiency improvements compared to existing techniques and over 90% accuracy compared to exhaustive tracing reference. With extremely efficient intra-service tracing observability, we can achieve more explainable datacenter management.

## 中文摘要

在线应用的复杂度正在快速上升，在当今云数据中心中带来了更为复杂的性能异常。为了完整理解应用行为，我们需要同时通过 RPC 级追踪获取服务间通信数据、通过应用级追踪获取服务内执行轨迹，从而精确推断事件之间的因果关系。然而，现有服务内追踪方案在被追踪应用上的平均时间开销通常约为 5-10%，最坏情况下甚至可达 18%。要在共享且高负载的数据中心中实现实用的服务内追踪，必须达到极致的追踪效率，将开销控制在千分位水平。本文提出 EXIST，一个基于商用现成硬件追踪能力的极致高效服务内追踪系统。EXIST 由三个协同模块组成，以追求面向极低开销的最优权衡。首先，它识别并消除高开销的追踪控制操作，以保障被观测应用的性能。其次，它依据应用状态动态分配有限的追踪缓冲区空间，并通过集群级编排优化追踪覆盖率。我们在基准测试与真实应用上对 EXIST 进行了充分的实现与评估。与现有技术相比，EXIST 实现了 2-10 倍的效率提升，相对穷尽式追踪参考的精度超过 90%。凭借极致高效的服务内追踪可观测性，我们能够实现更具可解释性的数据中心管理。

## 英文关键词

Intra-Service Tracing; Observability; Facility Efficiency; Processor Trace; Shared Datacenter

## 中文关键词

服务内追踪；可观测性；设施效率；处理器追踪；共享数据中心

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716283)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2025](../index.md)
