---
title: "Fusion: An Analytics Object Store Optimized for Query Pushdown"
description: "ASPLOS 2025 · Session 4C · Fusion：面向查询下推优化的分析型对象存储"
tags:
  - "ASPLOS2025"
  - "Session 4C"
  - "Potpourri 1"
---

# Fusion: An Analytics Object Store Optimized for Query Pushdown

**中文标题：** Fusion：面向查询下推优化的分析型对象存储

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jianan Lu (Princeton University), Ashwini Raina (Princeton University), Asaf Cidon (Columbia University), Michael J. Freedman (Princeton University)

**单位：** Princeton University；Columbia University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707234) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The prevalence of disaggregated storage in public clouds has led to increased latency in modern OLAP cloud databases, particularly when handling ad-hoc and highly-selective queries on large objects. To address this, cloud databases have adopted computation pushdown, executing query predicates closer to the storage layer. However, existing pushdown solutions are inefficient in erasure-coded storage. Cloud storage employs erasure coding that partitions analytics file objects into fixed-sized blocks and distributes them across storage nodes. Consequently, when a specific part of the object is queried, the storage system must reassemble the object across nodes, incurring significant network latency. In this work, we present Fusion, an object store for analytics that is optimized for query pushdown on erasurecoded data. It co-designs its erasure coding and file placement topologies, taking into account popular analytics file formats (e.g., Parquet). Fusion employs a novel stripe construction algorithm that prevents fragmentation of computable units within an object, and minimizes storage overhead during erasure coding. Compared to existing erasure-coded stores, Fusion improves median and tail latency by 64% and 81%, respectively, on TPC-H, and up to 40% and 48% respectively, on real-world SQL queries. Fusion achieves this while incurring a modest 1.2% storage overhead compared to the optimal.

## 中文摘要

公共云中分离式存储的普及使现代 OLAP 云数据库的延迟上升，尤其是在处理针对大对象的即席查询与高选择性查询时。为解决这一问题，云数据库采用了计算下推，将查询谓词下推到更靠近存储层的位置执行。然而，现有的下推方案在纠删码存储中效率低下。云存储采用纠删码，将分析文件对象切分为固定大小的块并分布到各存储节点上。因此，当查询该对象的某个特定部分时，存储系统必须跨节点重新组装该对象，从而带来显著的网络延迟。在本工作中，我们提出 Fusion，一种面向分析的对象存储，针对纠删码数据上的查询下推进行了优化。它协同设计纠删码与文件放置拓扑，并将流行的分析文件格式（如 Parquet）纳入考量。Fusion 采用一种新颖的条带构建算法，防止对象内可计算单元的碎片化，并在纠删码过程中最小化存储开销。与现有的纠删码存储相比，Fusion 在 TPC-H 上将中位延迟与尾延迟分别改善 64% 和 81%，在真实世界 SQL 查询上分别最多改善 40% 和 48%。Fusion 在实现这些效果的同时，相对于最优情况仅带来 1.2% 的适度存储开销。

## 英文关键词

data analytics; erasure codes; distributed storage

## 中文关键词

数据分析；纠删码；分布式存储

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707234)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2025](../index.md)
