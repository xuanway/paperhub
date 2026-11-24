---
title: "LOFT: A Lock-free and Adaptive Learned Index with High Scalability for Dynamic Workloads"
description: "EuroSys 2025 · ML Systems · Yuxuan Mo (Huazhong University of Science and Technology), Yu Hua (Huazhong Univ"
tags:
  - "EuroSys2025"
  - "ML Systems"
---

# LOFT: A Lock-free and Adaptive Learned Index with High Scalability for Dynamic Workloads

**中文标题：** 面向动态工作负载的高扩展性无锁自适应学习索引

**所属 Session：** [Session 4.1: ML Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：ML Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · ML Systems</p>
</div>

**作者**：Yuxuan Mo (Huazhong University of Science and Technology), Yu Hua (Huazhong University of Science and Technology)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717458)

## 英文摘要

In order to mitigate memory overheads and reduce data movements in the critical path, a computational and space-efficient learned index is promising to deliver high performance and complement traditional index structures, which unfortunately works well only in static workloads. In dynamic workloads, the learned indexes incur performance degradation with poor scalability due to inefficient data placement for newly inserted items and intensive lock contention. Furthermore, the model retraining is time-consuming and blocking, which hampers the performance of index operations. In order to meet the needs of dynamic workloads and efficient retraining, we propose LOFT, a highly scalable and adaptive learned index with lock-free design and self-tuning retraining technique to provide high throughput and low latency. LOFT enables all index operations to be concurrently executed in a lock-free manner by using Compare-and-Swap (CAS) primitive and an expanded learned bucket to handle the overflowed data. To minimize the impact of model retraining, LOFT leverages a shadow node to serve the clients’ requests and accelerates the retraining process with the aid of index operations. To accommodate dynamic workloads, LOFT determines when and how to perform retraining based on inferred access patterns. Our extensive evaluation on YCSB and real-world workloads demonstrates that LOFT effectively improves the performance by up to 14× than state-of-the-art designs.

## 中文摘要

为了降低内存开销并减少关键路径上的数据移动，一种计算和空间高效的学习索引有望提供高性能并补充传统索引结构，但遗憾的是它仅在静态工作负载下表现良好。在动态工作负载中，学习索引由于对新插入项的数据放置效率低下以及激烈的锁竞争，导致性能下降且可扩展性差。此外，模型重训练耗时且阻塞，妨碍了索引操作的性能。为满足动态工作负载和高效重训练的需求，我们提出 LOFT，一种高度可扩展且自适应的学习索引，采用无锁设计和自调优重训练技术，以提供高吞吐和低延迟。LOFT 通过使用比较并交换（CAS）原语和扩展的学习桶来处理溢出数据，使所有索引操作均能以无锁方式并发执行。为最小化模型重训练的影响，LOFT 利用影子节点服务客户端请求，并借助索引操作加速重训练过程。为适应动态工作负载，LOFT 基于推断出的访问模式决定何时以及如何执行重训练。我们在 YCSB 和真实工作负载上的大量评估表明，LOFT 相比最先进的设计将性能最高提升 14 倍。

**英文关键词：** learned index, dynamic workload, concurrency control

**中文关键词：** 学习索引、动态工作负载、并发控制

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
