---
title: "CORD: Low-Latency, Bandwidth-Efficient and Scalable Release Consistency via Directory Ordering"
description: "ISCA 2025 · Session 7B · CORD：通过目录排序实现低延迟、带宽高效且可扩展的释放一致性"
tags:
  - "ISCA2025"
  - "Session 7B"
  - "Systems"
---

# CORD: Low-Latency, Bandwidth-Efficient and Scalable Release Consistency via Directory Ordering

**中文标题：** CORD：通过目录排序实现低延迟、带宽高效且可扩展的释放一致性

**所属 Session：** [Session 7B](index.md) · [ISCA 2025](../index.md)

**作者：** Yanpeng Yu, Nicolai Oswald, Anurag Khandelwal, Nicolai Oswald

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731074) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Increasingly, multi-processing unit (PU) systems (e.g., CPU-GPU, multi-CPU, multi-GPU, etc.) are embracing cache-coherent shared memory to facilitate inter-PU communication. The coherence pro- tocols in these systems support write-through accesses that place the data directly at the LLC to enable efficient producer-consumer communications pervasive in AI/ML workloads. Moreover, release consistency has emerged as the standard memory model in such systems due to its programming simplicity and ability to support high performance. In today’s multi-PU systems, the source pro- cessor that issues the writes also orders them to enforce release consistency, even for write-through accesses. Unfortunately, such source ordering of write-through operations results in unnecessary communications between the source processor and the LLC direc- tory, incurring significant performance, interconnect traffic, and energy overheads for multi-PU applications. To eliminate such communication, we present cord1, a novel cache coherence protocol that orders write-through accesses di- rectly at the cache directory. cord employs several novel mecha- nisms to minimize the metadata required for ordering traffic while efficiently scaling to multiple directories. Evaluations atop the gem5 simulator show that compared to source ordering, cord improves application performance by 24% and reduces traffic by 13% on av- erage while incurring < 1% storage, area, and power overheads. Compared to hand-optimized message-passing implementations, cord observes a mere 3% performance overhead and 6% more traffic on average with a significantly simpler programming model.

## 中文摘要

越来越多多处理单元（PU）系统（如CPU-GPU、多CPU、多GPU等）采用支持缓存一致性的共享内存，简化处理单元之间的数据通信。这类系统中的一致性协议支持直写访问，数据直接写入最后一级缓存（LLC），适配AI/ML负载中非常普遍的生产者-消费者通信。同时，发布一致性（release consistency）凭借编程简单、高性能的优势，成为这类系统主流内存模型。

在当前多PU系统中，由发起写操作的源处理器负责对写操作排序，保证发布一致性，直写访问也不例外。但这种由源端负责排序的直写机制，会造成源处理器与LLC目录之间不必要的通信，给多PU应用带来明显性能、互联带宽与功耗开销。

为消除这类冗余通信，本文提出cord1，一种新型缓存一致性协议，直接在缓存目录侧对直写访问做排序。cord采用多项创新机制，降低排序所需元数据量，并且可以扩展到多个目录节点。
基于gem5仿真器评测：对比源端排序方案，cord平均提升应用性能24%，流量减少13%，存储、面积、功耗开销均小于1%。对比人工优化的消息传递实现，cord性能仅平均下降3%，流量增加6%，但编程模型简单很多。

## 英文关键词

cache coherence protocol, memory consistency model, heterogeneous architecture

## 中文关键词

缓存一致性协议, 内存一致性模型, 异构架构

## 代码与研究制品

- [代码仓库](https://github.com/yale-nova/CORD)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731074)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2025](../index.md)
