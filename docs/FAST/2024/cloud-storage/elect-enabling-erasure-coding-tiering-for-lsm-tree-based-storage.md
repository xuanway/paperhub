---
title: "ELECT: Enabling Erasure Coding Tiering for LSM-tree-based Storage"
description: "FAST 2024 · Cloud Storage · 第 293–310 页"
tags:
  - "FAST2024"
  - "Cloud Storage"
---

# ELECT: Enabling Erasure Coding Tiering for LSM-tree-based Storage

**中文标题**：ELECT：为基于 LSM-tree 的存储启用纠删码分层

**Session**：Cloud Storage · 2024-02-29 09:00–10:15 · Chair：Young-ri Choi（UNIST (Ulsan National Institute of Science and Technology)）

**作者**：Yanjing Ren and Yuanming Ren, The Chinese University of Hong Kong; Xiaolu Li and Yuchong Hu, Huazhong University of Science and Technology; Jingwei Li, University of Electronic Science and Technology of China; Patrick P. C. Lee, The Chinese University of Hong Kong

**会议**：FAST 2024 · Santa Clara, CA · 第 293–310 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/ren](https://www.usenix.org/conference/fast24/presentation/ren)

**论文 PDF**：[fast24-ren.pdf](https://www.usenix.org/system/files/fast24-ren.pdf)

---

## 英文摘要

Given the skewed nature of practical key-value (KV) storage workloads, distributed KV stores can adopt a tiered approach to support fast data access in a hot tier and persistent storage in a cold tier. To provide data availability guarantees for the hot tier, existing distributed KV stores often rely on replication and incur prohibitively high redundancy overhead. Erasure coding provides a low-cost redundancy alternative, but incurs high access performance overhead. We present ELECT, a distributed KV store that enables erasure coding tiering based on the log-structured merge tree (LSM-tree), by adopting a hybrid redundancy approach that carefully combines replication and erasure coding with respect to the LSM-tree layout. ELECT incorporates hotness awareness and selectively converts data from replication to erasure coding in the hot tier and offloads data from the hot tier to the cold tier. It also provides a tunable approach to balance the trade-off between storage savings and access performance through a single user-configurable parameter. We implemented ELECT atop Cassandra, which is replication-based. Experiments on Alibaba Cloud show that ELECT achieves significant storage savings in the hot tier, while maintaining high performance and data availability guarantees, compared with Cassandra.

## 中文摘要

鉴于实际键值（KV）存储负载的偏斜特性，分布式 KV 存储可以采用分层方法，在热层支持快速数据访问，在冷层提供持久存储。为给热层提供数据可用性保证，现有分布式 KV 存储通常依赖副本，并带来过高的冗余开销。纠删码提供了一种低成本的冗余替代方案，但会带来较高的访问性能开销。我们提出 ELECT，一个基于日志结构合并树（LSM-tree）实现纠删码分层的分布式 KV 存储，它采用混合冗余方法，根据 LSM-tree 布局谨慎地结合副本与纠删码。ELECT 融入热度感知，在热层中选择性地将数据从副本转换为纠删码，并将数据从热层卸载到冷层。它还提供一种可调方法，通过单个用户可配置参数来平衡存储节省与访问性能之间的权衡。我们在基于副本的 Cassandra 之上实现 ELECT。在阿里云上的实验表明，与 Cassandra 相比，ELECT 在热层实现显著的存储节省，同时保持高性能和数据可用性保证。
