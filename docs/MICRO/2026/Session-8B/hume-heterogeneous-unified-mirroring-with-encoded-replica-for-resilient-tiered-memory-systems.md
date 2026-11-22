---
title: "HUME: Heterogeneous Unified Mirroring with Encoded Replica for Resilient Tiered Memory Systems"
description: "MICRO 2026 · Session 8B · HUME：通过编码副本实现弹性分层内存系统的异构统一镜像"
tags:
  - "MICRO2026"
---

# HUME: Heterogeneous Unified Mirroring with Encoded Replica for Resilient Tiered Memory Systems

**中文标题：** HUME：通过编码副本实现弹性分层内存系统的异构统一镜像

**所属 Session：** [Session 8B](index.md) · [MICRO 2026](../index.md)

**作者：** Yixuan Liu, Zixiao Chen, Tong Zhao, Yunfei Gu, Chentao Wu, Xinfei Guo, Dongliang Xue, Jie Li, Minyi Guo, Junzhe Lv

**来源：** MICRO 2026，pp. 2864–2878；[DOI](https://doi.org/10.1109/MICRO67795.2026.00194)

## 英文摘要

Compute Express Link (CXL) enables cache-coherent memory expansion and hardware-based pooling. However, pooling memory across devices expands the fault domain, making device-level fault tolerance mechanisms such as Memory Mirroring essential for system resilience. At the same time, the inherent latency of the CXL interface requires Memory Tiering to maintain system performance. Existing methods that combine Mirroring and Tiering often suffer from significant performance overhead. In this paper, we propose Heterogeneous Unified Mirroring with Encoded Replica (HUME), an architecture for resilient tiered memory systems that decouples the placement of primary and secondary replicas. By placing primary replicas in Near Memory (NM) and secondary replicas in Far Memory (FM), HUME doubles the amount of hot data that can reside in NM and reduces migration overhead by moving only primary replicas. Furthermore, HUME uses pressure-aware read redirection to handle interconnect contention and applies fine-grained encoding to secondary replicas to protect against random DRAM faults. Results from joint simulation using ZSim and Ramulator2 indicate that HUME improves system performance by 16.5% over conventional Tiering with Mirroring systems and reduces the packet failure rate by a factor of 1.67 × 10^3.

## 中文摘要

Compute Express Link (CXL) 可实现缓存一致性内存扩展和基于硬件的池化。然而，跨设备的内存池扩展了故障域，使得内存镜像等设备级容错机制对于系统弹性至关重要。同时，CXL 接口固有的时延需要内存分层来维持系统性能。结合镜像和分层的现有方法通常会遭受巨大的性能开销。在本文中，我们提出了带有编码副本的异构统一镜像（HUME），这是一种用于弹性分层内存系统的架构，可解耦主副本和辅助副本的放置。通过将主副本放置在近内存 (NM) 中并将辅助副本放置在远内存 (FM) 中，HUME 使 NM 中可驻留的热数据量增加了一倍，并通过仅移动主副本来减少迁移开销。此外，HUME 使用压力感知读取重定向来处理互连争用，并对辅助副本应用细粒度编码以防止随机 DRAM 故障。使用 ZSim 和 Ramulator2 联合仿真的结果表明，HUME 比传统的 Tiering with Mirroring 系统性能提高了 16.5%，并将数据包失败率降低了 1.67 × 10^3。

## 中文关键词

DRAM；可靠性；纠错码；内存镜像；CXL；分层内存

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8B](index.md) · [MICRO 2026 主页](../index.md)
