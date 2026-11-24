---
title: "MinFlow: High-performance and Cost-efficient Data Passing for I/O-intensive Stateful Serverless Analytics"
description: "FAST 2024 · Cloud Storage · 第 311–328 页"
tags:
  - "FAST2024"
  - "Cloud Storage"
---

# MinFlow: High-performance and Cost-efficient Data Passing for I/O-intensive Stateful Serverless Analytics

**中文标题**：MinFlow：面向 I/O 密集型有状态无服务器分析的高性能低成本数据传递

**Session**：Cloud Storage · 2024-02-29 09:00–10:15 · Chair：Young-ri Choi（UNIST (Ulsan National Institute of Science and Technology)）

**作者**：Tao Li, Yongkun Li, and Wenzhe Zhu, University of Science and Technology of China; Yinlong Xu, Anhui Province Key Laboratory of High Performance Computing, University of Science and Technology of China; John C. S. Lui, The Chinese University of Hong Kong

**会议**：FAST 2024 · Santa Clara, CA · 第 311–328 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/li](https://www.usenix.org/conference/fast24/presentation/li)

**论文 PDF**：[fast24-li.pdf](https://www.usenix.org/system/files/fast24-li.pdf)

---

## 英文摘要

Serverless computing has revolutionized application deployment, obviating traditional infrastructure management and dynamically allocating resources on demand. A significant use case is I/O-intensive applications like data analytics, which widely employ the pivotal "shuffle" operation. Unfortunately, the shuffle operation poses severe challenges due to the massive PUT/GET requests to remote storage, especially in high-parallelism scenarios, leading to high performance degradation and storage cost. Existing designs optimize the data passing performance from multiple aspects, while they operate in an isolated way, thus still introducing unforeseen performance bottlenecks and bypassing untapped optimization opportunities. In this paper, we develop MinFlow, a holistic data passing framework for I/O-intensive serverless analytics jobs. MinFlow first rapidly generates numerous feasible multi-level data passing topologies with much fewer PUT/GET operations, then it leverages an interleaved partitioning strategy to divide the topology DAG into small-size bipartite sub-graphs to optimize function scheduling, further reducing over half of the transmitted data to remote storage. Moreover, MinFlow also develops a precise model to determine the optimal configuration, thus minimizing data passing time under practical function deployments. We implement a prototype of MinFlow, and extensive experiments show that MinFlow significantly outperforms state-of-the-art systems, FaaSFlow and Lambada, in both the job completion time and storage cost.

## 中文摘要

无服务器计算彻底改变了应用部署方式，免除了传统基础设施管理，并按需动态分配资源。一个重要的用例是数据分析等 I/O 密集型应用，这类应用广泛使用关键的“shuffle”操作。遗憾的是，shuffle 操作因向远程存储发出大量 PUT/GET 请求而带来严峻挑战，在高并行场景下尤为突出，导致性能严重下降和存储成本上升。现有设计从多个方面优化数据传递性能，但它们彼此孤立，因而仍会引入意想不到的性能瓶颈，并错失尚未利用的优化机会。本文提出 MinFlow，一个面向 I/O 密集型无服务器分析作业的整体数据传递框架。MinFlow 首先快速生成大量可行的多级数据传递拓扑，这些拓扑使用少得多的 PUT/GET 操作；然后利用交错分区策略将拓扑 DAG 划分为小规模二分图，以优化函数调度，进一步将传输到远程存储的数据减少一半以上。此外，MinFlow 还开发了一个精确模型来确定最优配置，从而在实际函数部署下最小化数据传递时间。我们实现了 MinFlow 原型，大量实验表明，MinFlow 在作业完成时间和存储成本两方面均显著优于最先进的系统 FaaSFlow 和 Lambada。
