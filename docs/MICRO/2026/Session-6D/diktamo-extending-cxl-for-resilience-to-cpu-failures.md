---
title: "DIKTAMO: Extending CXL for Resilience to CPU Failures"
description: "MICRO 2026 · Session 6D · DIKTAMO：扩展 CXL 以抵御 CPU 故障"
tags:
  - "MICRO2026"
  - "CXL"
---

# DIKTAMO: Extending CXL for Resilience to CPU Failures

**中文标题：** DIKTAMO：扩展 CXL 以抵御 CPU 故障

**所属 Session：** [Session 6D](index.md) · [MICRO 2026](../index.md)

**作者：** Antonis Psistakis, Burak Ocalan, Chloe Alverti, Fabien Chaix, Ramnatthan Alagappan, Josep Torrellas

**来源：** MICRO 2026，pp. 2247–2262；[DOI](https://doi.org/10.1109/MICRO67795.2026.00155)

## 英文摘要

Compute Express Link (CXL) 3.0 and beyond allows the compute nodes of a cluster to share data with hardware cache coherence and at the granularity of a cache line. This enables shared-memory semantics for distributed computing, but introduces a new resilience challenge: a node failure leads to the loss of the dirty data in its caches, corrupting application state. Sadly, the CXL specification does not consider processor failures. Moreover, when a component fails, the specification tries to isolate it and continue application execution; there is no attempt to bring the application to a consistent state—a step required to recover a shared-memory program. To address these limitations, this paper extends CXL to be resilient to node failures, and to correctly recover the application after node failures. We call the system DIKTAMO. To survive node failures, DIKTAMO augments the coherence transaction of a write with messages that propagate the update to a small set of other nodes (i.e., Replicas). Replicas save the update in a local hardware Logging Unit. Replication ensures resilience to node failures. Then, at regular intervals, the Logging Units dump the compressed updates to memory. After a node failure, recovery involves using the logs to bring the directory and memory to a correct state. Our evaluation with 16 4-core nodes shows that DIKTAMO enables fault-tolerant execution with 30% slowdown with 3 replicas (or 27% with 2 replicas) over a platform without fault-tolerance support. DIKTAMO is 2.82x faster than ensuring fault tolerance by using a write-through protocol.

## 中文摘要

Compute Express Link (CXL) 3.0 及更高版本允许集群的计算节点以硬件缓存一致性和缓存行的粒度共享数据。这为分布式计算启用了共享内存语义，但引入了新的弹性挑战：节点故障导致其缓存中的脏数据丢失，从而破坏应用程序状态。遗憾的是，CXL 规范没有考虑处理器故障。此外，当组件发生故障时，规范会尝试隔离它并继续应用程序执行；没有尝试使应用程序进入一致状态——这是恢复共享内存程序所需的步骤。为了解决这些限制，本文扩展了 CXL 以适应节点故障，并在节点故障后正确恢复应用程序。我们将该系统称为 DIKTAMO。为了在节点故障中幸存下来，DIKTAMO 通过将更新传播到一小组其他节点（即副本）的消息来增强写入的一致性事务。副本将更新保存在本地硬件记录单元中。复制可确保节点故障的恢复能力。然后，记录单元会定期将压缩的更新转储到内存中。节点发生故障后，恢复涉及使用日志将目录和内存恢复到正确状态。我们对 16 个 4 核节点的评估表明，DIKTAMO 能够实现容错执行，在没有容错支持的平台上，使用 3 个副本时速度减慢 30%（或使用 2 个副本时速度减慢 27%）。 DIKTAMO 比使用直写协议确保容错快 2.82 倍。

## 中文关键词

CXL；分布式共享内存；缓存一致性；容错；CPU 故障

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6D](index.md) · [MICRO 2026 主页](../index.md)
