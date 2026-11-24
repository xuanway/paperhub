---
title: "Taking Analytic Databases to the Bank"
description: "ISCA 2026 · Session 3B · Taking Analytic Databases to the Bank"
tags:
  - "ISCA2026"
  - "Session 3B"
  - "DRAM and SRAM PIM/PNM"
---

# Taking Analytic Databases to the Bank

**中文标题：** 将分析型数据库带到 DRAM bank 层

**所属 Session：** [Session 3B](index.md) · [ISCA 2026](../index.md)

**作者：** Alexandar Devic, Martin Prammer, Kevin Gaffney, Siddhartha Balakrishna Rai, Anand Sivasubramaniam, Jignesh M. Patel, Ameen Akel

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The explosion of big data has spotlighted the bottlenecks of data movement in traditional von-Neumann architectures. Data analytic applications, such as online analytic query processing (OLAP) databases, are especially burdened by these bottlenecks, given that latency is a key driver in these workloads. Thus, these applications turn to specialized hardware to overcome these otherwise insurmountable challenges. While there are many hardware options, processing in memory (PIM) techniques have gained relevance due to their recent availability as commodity DDR DRAM devices and their relatively cheap expected cost (in terms of power, area, and monetary considerations). However, even with such prevalence, existing research has yet to explore the impact of PIM on end-to-end OLAP workloads fully. In this work, we consider every aspect within a database system; the storage and memory layout, operator implementation, and the data sharing considerations. In particular, we find that ensuring data layout interoperability between query operators is an under-explored consideration that has a significant impact on performance. Using the Star Schema Benchmark, we show that for conservative PIM hardware, up to 17.1× query latency improvement can be achieved over a state-of-the-art, CPU-focused DBMS.

## 中文摘要

大数据爆炸凸显了传统冯·诺依曼架构中数据移动的瓶颈。数据分析应用，如在线分析查询处理（OLAP）数据库，尤其受到这些瓶颈的困扰，因为延迟是这些工作负载的关键驱动因素。因此，这些应用转向专用硬件来克服这些原本难以逾越的挑战。虽然有许多硬件选择，但处理中内存（PIM）技术因其最近作为商用DDR DRAM设备的可用性及其相对低廉的预期成本（在功耗、面积和货币方面）而获得了关注。然而，即使有了这样的普及，现有研究仍未充分探索PIM对端到端OLAP工作负载的影响。在本文中，我们考虑了数据库系统内的每个方面：存储和内存布局、算子实现以及数据共享考量。特别是，我们发现确保查询算子之间的数据布局互操作性是一个未被充分探索的考量因素，它对性能有显著影响。使用星型模式基准测试，我们表明，对于保守的PIM硬件，与最先进的以CPU为中心的DBMS相比，可以实现高达17.1倍的查询延迟改善。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2026](../index.md)
