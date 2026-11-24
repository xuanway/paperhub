---
title: "MagiCache: A Virtual In-Cache Computing Engine"
description: "ISCA 2025 · Session 9C · MagiCache: 虚拟片内计算引擎"
tags:
  - "ISCA2025"
  - "Session 9C"
  - "Memory Technology"
---

# MagiCache: A Virtual In-Cache Computing Engine

**中文标题：** MagiCache: 虚拟片内计算引擎

**所属 Session：** [Session 9C](index.md) · [ISCA 2025](../index.md)

**作者：** Renhao Fan, Yikai Cui, Weike Li, Mingyu Wang, Zhaolin Li

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731113) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The rise of data-parallel applications poses a significant challenge to the energy consumption of computing architectures. In-cache computation is a promising solution for achieving high parallelism and energy efficiency because it can eliminate data movement between the cache and the processor. Existing in-cache computing architectures transform a portion of cache arrays into computing arrays, with all rows of these arrays serving as computing lines. The remaining cache arrays are used as cachelines to store the data required by computing arrays or processors. However, in these array-level in-cache computing architectures, only a few computing lines in each computing array are active at runtime while the others are idle, which incurs severe cache capacity loss and space under- utilization. In addition, bursty memory accesses of data-parallel applications also cause significant in-cache data movement latency. To address these problems, we propose MagiCache, a virtual in-cache computing engine. First, we design a novel cacheline-level in-cache computing architecture in which each cache array can configure some rows as computing lines and the other rows as cachelines with negligible overhead. Second, a virtual engine is further designed on this novel architecture to dynamically allocate different rows of each array as computing lines or cachelines based on runtime computation and storage requirements, thus realizing efficient cacheline-level space management. Finally, we present an instruction chaining technique to overlap the bursty access latency by enabling asynchronous execution of computing arrays. Evaluation results show that MagiCache achieves a 1.19x-1.61x speedup over the state-of-the-art in-cache computing architectures with 6.5 KB of additional storage. Our cacheline-level space management improves cache utilization by 42% and reduces cache miss rate by 10%-40% over various memory access patterns. The instruction chaining technique also reduces the memory access time by 2%-27%.

## 中文摘要

数据并行类应用的兴起，给计算架构的能耗带来巨大挑战。缓存内计算（In-cache computation）是一种很有潜力的方案，能够消除缓存与处理器之间的数据搬运，从而获得高并行度与高能效。现有缓存内计算架构将一部分缓存阵列改造为计算阵列，该阵列内所有行都作为计算行；其余缓存阵列则作为普通缓存行，存放计算阵列或处理器所需的数据。

但这类阵列级缓存内计算架构存在缺陷：运行时每个计算阵列里往往只有少量计算行处于激活状态，其余计算行闲置，造成严重的缓存容量损失与空间利用率低下。此外，数据并行应用的突发式访存，也会带来显著的缓存内数据搬运延迟。

针对上述问题，本文提出MagiCache——一套虚拟化缓存内计算引擎。首先，设计一种全新的缓存行级缓存内计算架构：每个缓存阵列可以灵活配置部分行作为计算行、其余行作为普通缓存行，额外开销极低。其次，在该架构之上搭建虚拟化引擎，根据运行时的计算与存储需求，动态把阵列内不同行分配为计算行或缓存行，实现高效的缓存行级空间管理。最后，提出指令链技术，让计算阵列异步执行，掩盖突发访存的延迟。

评测结果表明：相比前沿缓存内计算架构，MagiCache仅增加6.5 KB存储开销，性能可提升1.19–1.61倍。本文的缓存行级空间管理方案在多种访存模式下，将缓存利用率提升42%，缓存失效率降低10%–40%；指令链技术可将访存时间减少2%–27%。

## 英文关键词

In-Cache Computation, Vector Processing

## 中文关键词

缓存内计算, 虚拟计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731113)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9C](index.md) · [返回 ISCA 2025](../index.md)
