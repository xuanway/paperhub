---
title: "DMTree: Towards Efficient Tree Indexing on Disaggregated Memory via Compute-side Collaborative Design"
description: "FAST 2026 · Indexing · 第 149–166 页"
tags:
  - "FAST2026"
  - "Indexing"
---

# DMTree: Towards Efficient Tree Indexing on Disaggregated Memory via Compute-side Collaborative Design

**中文标题**：DMTree：通过计算侧协同设计实现分离式内存上的高效树索引

**Session**：Indexing · 2026-02-24 14:00–15:40 · Chair：Zhichao Cao（Arizona State University）

**作者**：Guoli Wei, University of Science and Technology of China; Yongkun Li, University of Science and Technology of China and Anhui Provincial Key Laboratory of High Performance Computing, USTC; Haoze Song, The University of Hong Kong; Tao Li and Lulu Yao, University of Science and Technology of China; Yinlong Xu, University of Science and Technology of China and Anhui Provincial Key Laboratory of High Performance Computing, USTC; Heming Cui, The University of Hong Kong

**会议**：FAST 2026 · Santa Clara, CA · 第 149–166 页

**获奖**：Distinguished Artifact Award

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/wei](https://www.usenix.org/conference/fast26/presentation/wei)

**论文 PDF**：[fast26-wei.pdf](https://www.usenix.org/system/files/fast26-wei.pdf)

---

## 英文摘要

Disaggregated memory (DM) separates computing and memory resources into distinct resource pools, enhancing resource utilization and scalability. However, this new architecture presents fundamental design challenges on range indexes. Existing works fail to achieve high performance: they either suffer from the network bandwidth bottleneck or are fragile due to high RDMA IOPS demands. The key reason is that they all follow a typical design paradigm that uses *private compute-side caching*, where each compute server holds a private cache space and aggressively consumes the bandwidth and IOPS between compute servers and memory servers.

We propose a new *compute-side collaborative design*. It offloads data locating and locking operations from memory servers to compute servers and thus fully utilizes unsaturated RDMA resources between compute servers to mitigate bottlenecks on memory servers. We implement a prototype called DMTree. Experiments show that DMTree outperforms existing state-of-the-art range indexes on DM for both point operations (i.e., searches, inserts, and updates) and range operations (i.e., scans) under various workloads and parameter settings.

## 中文摘要

分离式内存（DM）将计算资源和内存资源分离为不同的资源池，从而提升资源利用率和可扩展性。然而，这种新架构给范围索引带来了根本性的设计挑战。现有工作未能实现高性能：它们要么受制于网络带宽瓶颈，要么因高 RDMA IOPS 需求而变得脆弱。其关键原因在于，它们都遵循一种典型的设计范式，即使用计算侧私有缓存：每个计算服务器持有私有的缓存空间，并大量消耗计算服务器与内存服务器之间的带宽和 IOPS。

我们提出一种新的计算侧协同设计。它将数据定位和加锁操作从内存服务器卸载到计算服务器，从而充分利用计算服务器之间尚未饱和的 RDMA 资源，缓解内存服务器上的瓶颈。我们实现了一个名为 DMTree 的原型。实验表明，在各种负载和参数设置下，DMTree 在点操作（即查找、插入和更新）和范围操作（即扫描）方面均优于分离式内存上现有的最先进范围索引。
