---
title: "Triage: An Adaptive Parallel Window Decoding Scheduler for Real-time Fault-Tolerant Quantum Computation"
description: "ISCA 2026 · Session 4D · Triage: An Adaptive Parallel Window Decoding Scheduler for Real-time Fault-Tolerant Quantum Computation"
tags:
  - "ISCA2026"
  - "Session 4D"
  - "Quantum 1"
---

# Triage: An Adaptive Parallel Window Decoding Scheduler for Real-time Fault-Tolerant Quantum Computation

**中文标题：** Triage: 面向实时容错量子计算的自适应并行窗口解码调度器

**所属 Session：** [Session 4D](index.md) · [ISCA 2026](../index.md)

**作者：** Jiahan Chen, Chenghong Zhu, Ge Bai, Xin Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Fault-tolerant quantum computation (FTQC) critically depends on real-time classical decoding, which is rapidly emerging as a system bottleneck. As quantum systems scale, decoding latency and throughput limitations lead to exponential syndrome backlogs and logical operation stalls. While hardware accelerators and parallel windowing offer pathways to speed up decoding, dynamically deploying a finite pool of decoders across a vast quantum error correction architecture remains an unresolved resource allocation problem. To address this, we formulate FTQC decoding as a constrained dynamic scheduling problem by utilizing a spatio-temporal framework based on slices. We propose Triage, a dual-mode architecture that mitigates operation stalls by adaptively combining a cost-efficient heuristic scheduler with a priority-aware emergency mode to rapidly resolve the causal cone of critical operations. Our evaluation shows that Triage maintains low algorithm stalls and logical error rates even under scarce classical resource constraints. Across various benchmarks, Triage achieves an average logical error rate reduction of 52.6% compared to standard temporal parallelism, enabling an efficient classical control plane for scalable FTQC architectures.


## 中文摘要

容错量子计算（FTQC）关键依赖于实时经典解码，而后者正迅速成为系统瓶颈。随着量子系统规模扩大，解码延迟和吞吐量限制导致综合征积压呈指数增长以及逻辑操作停顿。虽然硬件加速器和并行窗口（parallel windowing）为加快解码提供了途径，但在庞大的量子纠错架构中动态部署有限的解码器池仍是一个未解决的资源分配问题。为此，我们基于切片的时空框架，将 FTQC 解码表述为受约束的动态调度问题。我们提出 Triage，一种双模式架构，通过自适应地结合成本高效的启发式调度器与优先级感知的紧急模式，快速解决关键操作的因果锥，从而缓解操作停顿。我们的评估表明，即使在经典资源稀缺的约束下，Triage 仍能保持较低的算法停顿和逻辑错误率。在多种基准上，相比标准时间并行（temporal parallelism），Triage 平均降低逻辑错误率 52.6%，为可扩展的 FTQC 架构提供了高效的经典控制平面。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4D](index.md) · [返回 ISCA 2026](../index.md)
