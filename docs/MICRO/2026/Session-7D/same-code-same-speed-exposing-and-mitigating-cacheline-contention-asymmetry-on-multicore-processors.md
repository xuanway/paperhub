---
title: "Same Code ≠ Same Speed: Exposing and Mitigating Cacheline Contention Asymmetry on Multicore Processors"
description: "MICRO 2026 · Session 7D · 相同代码不等于相同性能：揭示并缓解多核处理器上的缓存行争用不对称性"
tags:
  - "MICRO2026"
  - "Cache"
---

# Same Code ≠ Same Speed: Exposing and Mitigating Cacheline Contention Asymmetry on Multicore Processors

**中文标题：** 相同代码不等于相同性能：揭示并缓解多核处理器上的缓存行争用不对称性

**所属 Session：** [Session 7D](index.md) · [MICRO 2026](../index.md)

**作者：** Yu Fu, Kaichi Li, Kaihui Gao, Li Chen, Dan Li, Guo Chen

**来源：** MICRO 2026，pp. 2687–2702；[DOI](https://doi.org/10.1109/MICRO67795.2026.00183)

## 英文摘要

Shared-memory software commonly assumes that threads contending on the same synchronization hotspot make roughly equal progress. We show that this assumption can fail even within a single socket: repeated contention on a shared cacheline systematically favors some cores over others through the non-uniform coherence substrate. We call this effect non-uniform cacheline contention (NUCC), a form of intra-socket non-uniformity that extends beyond the conventional NUCA view of static cache access cost. In our measurements, the throughput ratio between the fastest and slowest cores reaches 1.45× under otherwise symmetric execution, with more extreme cases approaching starvation. Although individual ownership transfers appear irregular, the resulting skew is stable, reproducible, and predictable from the contention configuration: a shallow placement-aware predictor estimates the normalized steady-state throughput map with a mean absolute error (MAE) of 0.0207. Because many real software fast paths coordinate through one or a few hotspot cachelines, NUCC can directly shape fairness, effective throughput, and tail latency in deployed systems. To mitigate NUCC, we introduce Iso-Performance Domains (IPDs) and IPD-guided placement, a thread-placement method that minimizes throughput skew. In a real RDMA shared-queue-pair (SQP) fast path, IPD reduces throughput skew from 1.56× to approximately 1.05× and lowers p99 latency by up to 26% with no throughput loss. Together, these results show that NUCC is not just observable, but stable and predictable enough to guide practical mitigation.

## 中文摘要

共享内存软件通常假设在同一同步热点上竞争的线程取得大致相同的进度。我们证明，即使在单个套接字内，这种假设也可能失败：共享缓存行上的重复争用通过非均匀一致性基底系统地有利于某些核心而不是其他核心。我们将这种效应称为非均匀缓存行争用 (NUCC)，这是一种插槽内非均匀性形式，超出了静态缓存访问成本的传统 NUCA 视图。在我们的测量中，在对称执行情况下，最快和最慢核心之间的吞吐量比达到 1.45 倍，更极端的情况接近饥饿。尽管个人所有权转移看起来不规则，但由此产生的偏差是稳定的、可重复的，并且可以根据争用配置进行预测：浅层布局感知预测器以平均绝对误差 (MAE) 为 0.0207 来估计标准化稳态吞吐量图。由于许多真实的软件快速路径通过一个或几个热点缓存行进行协调，NUCC 可以直接塑造已部署系统中的公平性、有效吞吐量和尾部时延。为了缓解 NUCC，我们引入了 Iso 性能域 (IPD) 和 IPD 引导布局，这是一种可最大限度减少吞吐量偏差的线程布局方法。在真正的 RDMA 共享队列对 (SQP) 快速路径中，IPD 将吞吐量偏差从 1.56 倍减少到大约 1.05 倍，并将 p99 时延降低高达 26%，而没有吞吐量损失。总之，这些结果表明 NUCC 不仅是可观察的，而且足够稳定和可预测，足以指导实际的缓解措施。

## 中文关键词

非均匀缓存行争用；共享内存同步；多核系统；缓存一致性

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7D](index.md) · [MICRO 2026 主页](../index.md)
