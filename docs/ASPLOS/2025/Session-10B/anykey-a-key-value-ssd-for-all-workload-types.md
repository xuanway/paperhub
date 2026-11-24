---
title: "AnyKey: A Key-Value SSD for All Workload Types"
description: "ASPLOS 2025 · Session 10B · AnyKey：面向所有工作负载类型的键值 SSD"
tags:
  - "ASPLOS2025"
  - "Session 10B"
  - "Solid State Storage"
---

# AnyKey: A Key-Value SSD for All Workload Types

**中文标题：** AnyKey：面向所有工作负载类型的键值 SSD

**所属 Session：** [Session 10B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Chanyoung Park (Hanyang University), Jungho Lee (Hanyang University), Chun-Yi Liu (Micron Technology Inc.), Kyungtae Kang (Hanyang Univeristy), Mahmut Taylan Kandemir (Pennsylvania State University), Wonil Choi (Hanyang University)

**单位：** Hanyang University；Micron Technology Inc.；Hanyang Univeristy；Pennsylvania State University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707279) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Key-value solid-state drives (KV-SSDs) are considered as a potential storage solution for large-scale key-value (KV) store applications. Unfortunately, the existing KV-SSD designs are tuned for a specific type of workload, namely, those in which the size of the values are much larger than the size of the keys. Interestingly, there also exists another type of workload, in practice, in which the sizes of keys are relatively large. We reevaluate the current KV-SSD designs using such unexplored workloads and document their significantly-degraded performance. Observing that the performance problem stems from the increased size of the metadata, we subsequently propose a novel KV-SSD design, called AnyKey, which prevents the size of the metadata from increasing under varying sizes of keys. Our detailed evaluation using a wide range of real-life workloads indicates that AnyKey outperforms the state-ofthe-art KV-SSD design under different types of workloads with varying sizes of keys and values.

## 中文摘要

键值固态盘（KV-SSD）被视为大规模键值（KV）存储应用的一种潜在存储方案。但现有的 KV-SSD 设计针对某一特定类型的工作负载进行调优，即值的大小远大于键的大小的工作负载。有趣的是，实践中还存在另一类工作负载，其中键的尺寸相对较大。我们利用这类尚未被探索的工作负载重新评估了当前的 KV-SSD 设计，并记录了其性能的显著退化。观察到该性能问题源于元数据规模的增大，我们进而提出了一种新的 KV-SSD 设计，称为 AnyKey，它能够在键尺寸变化的情况下避免元数据规模的增长。我们使用大量真实工作负载进行的详细评估表明，在键和值尺寸各不相同的不同类型工作负载下，AnyKey 均优于最先进的 KV-SSD 设计。

## 英文关键词

Key-value solid-state drive, log-structured mergetree, storage management software, tail latency

## 中文关键词

键值固态盘；日志结构合并树；存储管理软件；尾延迟

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707279)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10B](index.md) · [返回 ASPLOS 2025](../index.md)
