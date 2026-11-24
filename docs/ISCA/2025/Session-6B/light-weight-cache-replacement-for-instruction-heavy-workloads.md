---
title: "Light-weight Cache Replacement for Instruction Heavy Workloads"
description: "ISCA 2025 · Session 6B · 面向指令密集型负载的轻量级缓存替换"
tags:
  - "ISCA2025"
  - "Session 6B"
  - "Microarchitecture II"
---

# Light-weight Cache Replacement for Instruction Heavy Workloads

**中文标题：** 面向指令密集型负载的轻量级缓存替换

**所属 Session：** [Session 6B](index.md) · [ISCA 2025](../index.md)

**作者：** Saba Mostofi, Setu Gupta, Ahmad Hassani, Krishnam Tibrewala, Elvira Teran, Paul Gratz, Daniel A. Jimenez

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730993) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The last-level cache (LLC) is the last chance for memory accesses from the processor to avoid the costly latency of accessing the main memory. In recent years, an increasing number of instruction heavy workloads have put pressure on the last-level cache. We find that, for instruction heavy workloads, a simple replacement policy with minimal overhead provides at least the same benefit as a state- of-the-art, high-overhead replacement policy in the presence of aggressive prefetching. Our proposal is based on specifying inser- tion and promotion vectors (IPVs) as a generalization of re-reference interval prediction (RRIP) in such a way that the space of feasible policies may be searched exhaustively to find the best policy for the training set of workloads. The policies are formulated to deliver the best performance taking into account demand and prefetch ac- cesses. We show that our technique, Prefetch Aware Coarse-grained Insertion and Promotion Vectors (PACIPV), improves performance over a state-of-the-art LLC replacement policy (Mockingjay) for in- struction heavy workloads, and remains competitive for data heavy workloads with significantly less hardware overhead. We show that RRIP-based IPVs are very easy to implement but outperform far more complex replacement policies. PACIPV achieves a speedup of 3.3% over the baseline of LRU, outperforming SRRIP by 1.1% and the much more hardware intensive Mockingjay by 0.1%.

## 中文摘要

末级缓存（LLC）是处理器访存时避开高延迟主存访问的最后一道屏障。近年来，指令密集型负载越来越多，给末级缓存带来巨大压力。本文发现：在激进预取机制开启的条件下，针对指令密集型负载，一种低开销的简单替换策略，性能至少可以和前沿、高开销的替换策略持平。
本文方案基于插入提升向量（IPV），它是重引用区间预测（RRIP）的泛化形式；通过IPV可以穷举搜索可行策略空间，找到适配训练负载集的最优策略。这些策略在设计时同时考虑按需访问与预取访问，以实现最优性能。

本文提出PACIPV（感知预取的粗粒度插入提升向量）：针对指令密集型负载，相比前沿末级缓存替换策略Mockingjay性能更优；对于数据密集型负载也保持可比性能，且硬件开销显著更低。研究表明基于RRIP的IPV实现简单，性能却优于复杂度高得多的替换策略。
以LRU为基线，PACIPV提速3.3%，相比SRRIP提升1.1%，相比硬件开销更大的Mockingjay提升0.1%。

## 英文关键词

Microarchitecture, Cache Management, Replacement Policy, Insertion Promotion Vectors, Last-Level Cache

## 中文关键词

微架构, 缓存管理, 替换策略, 插入提升向量, 末级缓存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730993)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2025](../index.md)
