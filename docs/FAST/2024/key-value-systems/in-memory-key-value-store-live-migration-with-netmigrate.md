---
title: "In-Memory Key-Value Store Live Migration with NetMigrate"
description: "FAST 2024 · Key-Value Systems · 第 209–224 页"
tags:
  - "FAST2024"
  - "Key-Value Systems"
---

# In-Memory Key-Value Store Live Migration with NetMigrate

**中文标题**：使用 NetMigrate 的内存键值存储在线迁移

**Session**：Key-Value Systems · 2024-02-28 14:00–15:40 · Chair：Angela Demke Brown（University of Toronto）

**作者**：Zeying Zhu, University of Maryland; Yibo Zhao, Boston University; Zaoxing Liu, University of Maryland

**会议**：FAST 2024 · Santa Clara, CA · 第 209–224 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/zhu](https://www.usenix.org/conference/fast24/presentation/zhu)

**论文 PDF**：[fast24-zhu.pdf](https://www.usenix.org/system/files/fast24-zhu.pdf)

---

## 英文摘要

Distributed key-value stores today require frequent key-value shard migration between nodes to react to dynamic workload changes for load balancing, data locality, and service elasticity. In this paper, we propose NetMigrate, a live migration approach for in-memory key-value stores based on programmable network data planes. NetMigrate migrates shards between nodes with zero service interruption and minimal performance impact. During migration, the switch data plane monitors the migration process in a fine-grained manner and directs client queries to the right server in real time, eliminating the overhead of pulling data between nodes. We implement a NetMigrate prototype on a testbed consisting of a programmable switch and several commodity servers running Redis, and evaluate it under YCSB workloads. Our experiments demonstrate that NetMigrate improves the query throughput from 6.5% to 416% and maintains low access latency during migration, compared to the state-of-the-art migration approaches.

## 中文摘要

如今的分布式键值存储需要频繁在节点之间迁移键值分片，以应对动态负载变化，实现负载均衡、数据局部性和服务弹性。本文提出 NetMigrate，一种基于可编程网络数据平面的内存键值存储在线迁移方法。NetMigrate 以零服务中断和最小性能影响在节点之间迁移分片。迁移期间，交换机数据平面细粒度地监控迁移过程，并实时将客户端查询导向正确的服务器，从而消除节点之间拉取数据的开销。我们在由一台可编程交换机和多台运行 Redis 的商用服务器组成的测试床上实现 NetMigrate 原型，并在 YCSB 负载下对其进行评估。实验表明，与最先进的迁移方法相比，NetMigrate 将查询吞吐量提升 6.5% 至 416%，并在迁移期间保持低访问延迟。
