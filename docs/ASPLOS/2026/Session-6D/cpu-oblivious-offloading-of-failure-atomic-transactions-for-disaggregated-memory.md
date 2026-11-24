---
title: "CPU-Oblivious Offloading of Failure-Atomic Transactions for Disaggregated Memory"
description: "ASPLOS 2026 · Session 6D · 面向分离式内存的 CPU 无关的失败原子事务卸载"
tags:
  - "ASPLOS2026"
  - "Session 6D"
  - "Disaggregated Memory Systems"
---

# CPU-Oblivious Offloading of Failure-Atomic Transactions for Disaggregated Memory

**中文标题：** 面向分离式内存的 CPU 无关的失败原子事务卸载

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Cheng Chen (Huazhong University of Science and Technology), Chencheng Ye (Huazhong University of Science and Technology), Yuanchao Xu (University of California, Santa Cruz), Xipeng Shen (North Carolina State University), Xiaofei Liao (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology), Wenbin Jiang (Huazhong University of Science and Technology), Yan Solihin (U. of Central Florida)

**单位：** Huazhong University of Science and Technology；University of California, Santa Cruz；North Carolina State University；U. of Central Florida

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790146) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Memory disaggregation introduces new challenges for application reliability, as compute server or interconnection failures can interrupt execution and lead to data inconsistency in the memory server. This paper presents Fanmem, a novel failure-atomic transaction system designed specifically for disaggregated memory architectures. Fanmem ensures data consistency in the presence of failures, drawing inspiration from persistent memory transactions while tailored for memory disaggregation. The key innovations of Fanmem include an asynchronous transaction model and the integration of a processing unit within the switch, enabling the offloading of time-consuming log persistency operations to the switch processing unit and significantly reducing the overhead on the compute servers. Evaluation confirms the effectiveness of Fanmem on two representative memory-disaggregated architectures. Compared to the state-of-the-art persistent memory transaction system, Fanmem achieves an average performance improvement of 1.2× and 1.7× on the respective architectures.

## 中文摘要

内存分离为应用可靠性带来了新的挑战，因为计算服务器或互连的故障可能中断执行，并导致内存服务器中的数据不一致。本文提出 Fanmem，一个专为分离式内存架构设计的新颖失败原子事务系统。Fanmem 在发生故障时确保数据一致性，其思路借鉴持久内存事务，同时针对内存分离进行了定制。Fanmem 的关键创新包括异步事务模型，以及在交换机内部集成处理单元，从而能够将耗时的日志持久化操作卸载到交换机处理单元，并显著降低计算服务器上的开销。评估确认了 Fanmem 在两种具有代表性的内存分离架构上的有效性。与最先进的持久内存事务系统相比，Fanmem 在两种架构上分别实现了平均 1.2 倍和 1.7 倍的性能提升。

## 英文关键词

Persistent Memory, Disaggregated Memory, Crash Consistency

## 中文关键词

持久内存；分离式内存；崩溃一致性

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790146)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2026](../index.md)
