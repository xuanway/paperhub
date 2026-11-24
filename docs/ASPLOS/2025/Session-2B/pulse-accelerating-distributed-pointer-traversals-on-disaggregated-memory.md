---
title: "pulse: Accelerating Distributed Pointer-Traversals on Disaggregated Memory"
description: "ASPLOS 2025 · Session 2B · pulse：加速分离式内存上的分布式指针遍历"
tags:
  - "ASPLOS2025"
  - "Session 2B"
  - "Distributed Computing"
---

# pulse: Accelerating Distributed Pointer-Traversals on Disaggregated Memory

**中文标题：** pulse：加速分离式内存上的分布式指针遍历

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yupeng Tang (Yale University), Seung-seob Lee (Yale University), Abhishek Bhattacharjee (Yale University), Anurag Khandelwal (Yale University)

**单位：** Yale University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707253) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Caches at CPU nodes in disaggregated memory architectures amortize the high data access latency over the network. However, such caches are fundamentally unable to improve performance for workloads requiring pointer traversals across linked data structures. We argue for accelerating these pointer traversals closer to disaggregated memory in a manner that preserves expressiveness for supporting various linked structures, ensures energy efficiency and performance, and supports distributed execution. We design pulse, a distributed pointer-traversal framework for rack-scale disaggregated memory to meet all the above requirements. Our evaluation of pulse shows that it enables low-latency, highthroughput, and energy-efficient execution for a wide range of pointer traversal workloads on disaggregated memory that fare poorly with caching alone.

## 中文摘要

在分离式内存架构中，CPU 节点上的缓存可将高昂的数据访问延迟分摊到网络上。然而，对于需要在链接数据结构之间进行指针遍历的工作负载，此类缓存从根本上无法改善其性能。我们主张将这类指针遍历加速到更靠近分离式内存的位置，既保留对多种链接结构的表达能力，又确保能效与性能，并支持分布式执行。我们设计了 pulse，一个面向机架级分离式内存的分布式指针遍历框架，以满足上述所有需求。对 pulse 的评估表明，对于仅依靠缓存表现不佳的各类分离式内存指针遍历工作负载，它都能实现低延迟、高吞吐且高能效的执行。

## 英文关键词

Disaggregated memory, Pointer-traversals, Nearmemory processing, Programmable networks, FPGAs

## 中文关键词

分离式内存；指针遍历；近内存处理；可编程网络；FPGA

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707253)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2025](../index.md)
