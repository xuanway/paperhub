---
title: "AXLE: Coordinated Offloading with Asynchronous Back-Streaming in Computational Memory Systems"
description: "ISCA 2026 · Session 10C · AXLE: Coordinated Offloading with Asynchronous Back-Streaming in Computational Memory Systems"
tags:
  - "ISCA2026"
  - "Session 10C"
  - "PIM/PNM, cont."
---

# AXLE: Coordinated Offloading with Asynchronous Back-Streaming in Computational Memory Systems

**中文标题：** AXLE: 计算内存系统中基于异步回传的协同卸载

**所属 Session：** [Session 10C](index.md) · [ISCA 2026](../index.md)

**作者：** Suyeon Lee, Kangkyu Park, Kwangsik Shin, Ada Gavrilovska

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

CXL-based Computational Memory (CCM) enables near-memory processing within expanded remote memory, offering opportunities to address data movement costs in disaggregated memory systems and to accelerate overall performance. However, existing offloading mechanisms do not fully leverage the trade-offs of different offload models based on different CXL protocols. This work first examines these tradeoffs and their impact on end-to-end performance and system efficiency for workloads with diverse data and computation characteristics. We propose Asynchronous Back-Streaming, a new offloading protocol that coordinates CXL.io and CXL.mem to enable result back-streaming and asynchronous pipelining across CCM and host tasks. We further design AXLE, a system that realizes this protocol with lightweight host-CCM interaction. Overall, AXLE reduces end-to-end runtime by up to 50.14%, reduces CCM and host idle times by an average of 14.53× and 3.93×, respectively, and achieves up to 6× reduction in host core stall time.

## 中文摘要

基于 CXL 的计算内存（CCM）使得在扩展的远端内存中进行近内存处理成为可能，为解决分解式内存系统中的数据搬移开销、并加速整体性能提供了机会。然而，现有的卸载机制并未充分利用基于不同 CXL 协议的各类卸载模型之间的权衡。本工作首先考察这些权衡，以及它们对有不同数据与计算特征的工作负载在端到端性能和系统效率上的影响。我们提出异步回传（Asynchronous Back-Streaming），一种新的卸载协议，协同 CXL.io 与 CXL.mem，以实现结果回传以及 CCM 与主机任务之间的异步流水化。我们进一步设计了 AXLE，一个以轻量级主机–CCM 交互实现该协议的系统。总体而言，AXLE 将端到端运行时间最多降低 50.14%，将 CCM 与主机的空闲时间平均分别降低 14.53× 和 3.93×，并使主机核心停顿时间最多减少 6×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10C](index.md) · [返回 ISCA 2026](../index.md)
