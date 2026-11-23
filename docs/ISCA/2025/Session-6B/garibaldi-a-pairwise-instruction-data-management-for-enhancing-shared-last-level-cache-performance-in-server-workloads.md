---
title: "Garibaldi: A Pairwise Instruction-Data Management for Enhancing Shared Last-Level Cache Performance in Server Workloads"
description: "ISCA 2025 · Session 6B · Garibaldi：通过成对指令—数据管理提升服务器负载共享末级缓存性能"
tags:
  - "ISCA2025"
  - "Session 6B"
  - "Microarchitecture II"
---

# Garibaldi: A Pairwise Instruction-Data Management for Enhancing Shared Last-Level Cache Performance in Server Workloads

**中文标题：** Garibaldi：通过成对指令—数据管理提升服务器负载共享末级缓存性能

**所属 Session：** [Session 6B](index.md) · [ISCA 2025](../index.md)

**作者：** Jaewon Kwon, Yongju Lee, Jiwan Kim, Enhyeok Jang, Hongju Kal, Won Woo Ro

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731029) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Modern CPUs suffer from the frontend bottleneck because the in- struction footprint of server workloads exceeds the private cache capacity. Prior works have examined the CPU components or pri- vate cache to improve the instruction hit rate. The large footprint leads to significant cache misses not only in the core and faster-level cache but also in the last-level cache (LLC). We observe that even with an advanced branch predictor and instruction prefetching techniques, a considerable amount of instruction accesses descend to the LLC. However, state-of-the-art LLC designs with elaborate data management overlook handling the instruction misses that precede corresponding data accesses. Specifically, when an instruc- tion requiring numerous data accesses is missed, the frontend of a CPU should wait for the instruction fetch, regardless of how much data are present in the LLC. To preserve hot instructions in the LLC, we propose Garibaldi, a novel pairwise instruction-data management scheme. Garibaldi tracks the hotness of instruction accesses by coupling it with that of data accesses and adopts management techniques. On the one hand, this scheme includes a selective protection mechanism that prevents the cache evictions of high-cost instruction cachelines. On the other hand, in the case of unprotected instruction line misses, Garibaldi conservatively issues prefetch requests of the paired data lines while handling those misses. In our experiments, we evaluate Garibaldi with 16 server workloads on a 40-core machine. We also implement Garibaldi on top of a modern LLC design, including Mockingjay. Garibaldi improves 13.2% and 6.1% of CPU performance on baseline LLC design and Mockingjay, respectively.

## 中文摘要

现代CPU面临前端瓶颈：服务器负载的指令足迹超出私有缓存容量。已有研究针对CPU部件或私有缓存来提升指令命中率。巨大的指令足迹不仅会在核内、高速缓存中引发大量缓存缺失，也会出现在末级缓存（LLC）。我们观察到：即便配备先进分支预测器与指令预取技术，仍有相当多的指令访存请求落到末级缓存。然而，现有管理机制复杂的前沿末级缓存方案，忽略了在数据访问之前发生的指令缺失问题。具体来说，如果一条需要大量数据访问的指令发生缺失，无论末级缓存中是否已经存有对应数据，CPU前端都必须等待该指令取指完成。

为在末级缓存中留存热点指令，本文提出Garibaldi，一种全新的指令-数据配对管理策略。Garibaldi将指令访问热度与数据访问热度绑定跟踪，并配套对应的缓存管理手段。一方面，该策略包含选择性保护机制，避免高代价指令缓存行被替换逐出；另一方面，当未受保护的指令行发生缺失时，Garibaldi在处理该缺失的同时，保守地发起配对数据行的预取请求。
实验在一台40核机器上使用16个服务器负载开展测试，并将Garibaldi实现在包含Mockingjay在内的现代末级缓存架构之上。对比基线LLC设计，Garibaldi使CPU性能提升13.2%；对比Mockingjay，性能提升6.1%。

## 英文关键词

multi-core architectures, cache microarchitecture, instruction caching, frontend stalls, data center

## 中文关键词

众核架构, 缓存微架构, 指令缓存, 前端停顿, 数据中心

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731029)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2025](../index.md)
