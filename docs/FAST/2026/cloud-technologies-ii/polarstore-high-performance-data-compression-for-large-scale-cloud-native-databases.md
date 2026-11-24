---
title: "PolarStore: High-Performance Data Compression for Large-Scale Cloud-Native Databases"
description: "FAST 2026 · Cloud Technologies II · 第 509–526 页"
tags:
  - "FAST2026"
  - "Cloud Technologies II"
---

# PolarStore: High-Performance Data Compression for Large-Scale Cloud-Native Databases

**中文标题**：PolarStore：面向大规模云原生数据库的高性能数据压缩

**Session**：Cloud Technologies II · 2026-02-26 09:00–10:20 · Chair：Uday Kiran Jonnala（Dell Technologies）

**作者**：Qingda Hu, Xinjun (Jimmy) Yang, Feifei Li, Junru Li, Ya Lin, Yuqi Zhou, Yicong Zhu, Junwei Zhang, Rongbiao Xie, Ling Zhou, Bin Wu, and Wenchao Zhou, Alibaba Cloud Computing

**会议**：FAST 2026 · Santa Clara, CA · 第 509–526 页

**论文类型**：Deployed-Systems Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/hu](https://www.usenix.org/conference/fast26/presentation/hu)

**论文 PDF**：[fast26-hu.pdf](https://www.usenix.org/system/files/fast26-hu.pdf)

---

## 英文摘要

In recent years, resource elasticity and cost optimization have become essential for RDBMSs. While cloud-native RDBMSs provide elastic computing resources via disaggregated computing and storage, storage costs remain a critical user concern. Consequently, data compression emerges as an effective strategy to reduce storage costs. However, existing compression approaches in RDBMSs present a stark trade-off: software-based approaches incur significant performance overheads, while hardware-based alternatives lack the flexibility required for diverse database workloads.

In this paper, we present PolarStore, a compressed shared storage system for cloud-native RDBMSs. PolarStore employs a dual-layer compression mechanism that combines in-storage compression in PolarCSD hardware with lightweight compression in software. This design leverages the strengths of both approaches. PolarStore also incorporates database-oriented optimizations to maintain high performance on critical I/O paths. Drawing from large-scale deployment experiences, we also introduce hardware improvements for PolarCSD to ensure host-level stability and propose a compression-aware scheduling scheme to improve cluster-level space efficiency. PolarStore is currently deployed on thousands of storage servers within PolarDB, managing over 100 PB of data. It achieves a compression ratio of 3.55 and reduces storage costs by approximately 60%. Remarkably, these savings are achieved while maintaining performance comparable to uncompressed clusters.

## 中文摘要

近年来，资源弹性和成本优化对关系型数据库管理系统（RDBMS）变得至关重要。云原生 RDBMS 通过计算与存储分离提供弹性计算资源，但存储成本仍是用户关注的关键问题。因此，数据压缩成为降低存储成本的有效策略。然而，RDBMS 中现有的压缩方法存在明显权衡：基于软件的方法会带来显著性能开销，而基于硬件的替代方案缺乏应对多样数据库负载所需的灵活性。

本文提出 PolarStore，一个面向云原生 RDBMS 的压缩共享存储系统。PolarStore 采用双层压缩机制，将 PolarCSD 硬件中的存储内压缩与软件中的轻量级压缩相结合。该设计兼取两类方法的优势。PolarStore 还引入面向数据库的优化，以在关键 I/O 路径上保持高性能。基于大规模部署经验，我们还为 PolarCSD 引入硬件改进以确保主机级稳定性，并提出一种压缩感知调度方案以提升集群级空间效率。PolarStore 目前已部署在 PolarDB 内的数千台存储服务器上，管理超过 100 PB 的数据。它实现了 3.55 的压缩比，并将存储成本降低约 60%。值得注意的是，这些节省是在保持与未压缩集群相当的性能的同时实现的。
