---
title: "CREST: High-Performance Contention Resolution for Disaggregated Transactions"
description: "ASPLOS 2026 · Session 6D · CREST：面向分离式事务的高性能争用消解"
tags:
  - "ASPLOS2026"
  - "Session 6D"
  - "Disaggregated Memory Systems"
---

# CREST: High-Performance Contention Resolution for Disaggregated Transactions

**中文标题：** CREST：面向分离式事务的高性能争用消解

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Qihan Kang (Institute of Computing Technology, Chinese Academy of Sciences), Mi Zhang (Institute of Computing Technology, Chinese Academy of Sciences), Patrick P. C. Lee (The Chinese University of Hong Kong), Yongkang Hu (Institute of Computing Technology, Chinese Academy of Sciences)

**单位：** Institute of Computing Technology, Chinese Academy of Sciences；The Chinese University of Hong Kong

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790148) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Distributed transaction systems can leverage memory disaggregation for efficient resource scaling, yet they experience significant performance degradation under high-contention workloads. We present CREST, a disaggregated transaction system that efficiently manages high-contention transaction workloads in disaggregated memory architectures via three key techniques: (i) cell-level concurrency control, which achieves more fine-grained transaction concurrency than existing record-level approaches and reduces remote access latencies using a metadata-aggregated record structure; (ii) localized execution, which allows compute nodes to operate on local uncommitted results to reduce blocking time; and (iii) parallel commits, which parallelize commit operations under transaction dependencies. Evaluation shows that CREST achieves a throughput gain of up to 1.92× over state-of-the-art systems under high-contention workloads.

## 中文摘要

分布式事务系统能够利用内存分离实现高效的资源扩展，但在高争用负载下会出现显著的性能下降。我们提出 CREST，一个分离式事务系统，它通过三项关键技术，在分离式内存架构中高效管理高争用事务负载：（i）单元级并发控制，相比现有记录级方法实现了更细粒度的事务并发，并利用元数据聚合的记录结构降低远程访问延迟；（ii）本地化执行，允许计算节点基于本地未提交的结果进行操作，以减少阻塞时间；（iii）并行提交，在存在事务依赖的情况下将提交操作并行化。评估表明，在高争用负载下，CREST 相比最先进系统实现了最高 1.92× 的吞吐量提升。

## 英文关键词

Distributed transactions, disaggregated memory, RDMA

## 中文关键词

分布式事务；分离式内存；RDMA

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790148)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2026](../index.md)
