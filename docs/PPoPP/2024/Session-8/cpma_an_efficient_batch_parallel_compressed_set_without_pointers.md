---
title: "CPMA: An Efficient Batch-Parallel Compressed Set Without Pointers"
description: "PPoPP 2024 Session Optimizing for Memory：无指针的批并行压缩 PMA，批量插入 3×、范围查询 4× 吞吐"
tags:
  - "PPoPP2024"
  - "Session-8"
  - "Optimizing for Memory"
  - "Packed Memory Array"
  - "Batch-Parallel"
  - "Compression"
authors:
  - "Brian Wheatman"
  - "Randal Burns"
  - "Aydin Buluc"
  - "Helen Xu"
session: "Session 8: Optimizing for Memory"
session_number: 8
session_chair: "Yan Gu"
date: "2024-03-05"
time: "16:30–16:50"
room: "Moorfoot"
doi: "10.1145/3627535.3638492"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# CPMA: An Efficient Batch-Parallel Compressed Set Without Pointers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出批并行压缩紧凑内存数组 CPMA，在 PMA 基础上优化缓存友好性，突破更新与扫描之间的取舍，批量插入与范围查询吞吐分别比压缩 PaC-tree 快 3 倍和 4 倍。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 8: Optimizing for Memory</p>
</div>

**作者**：Brian Wheatman, Randal Burns (Johns Hopkins University); Aydin Buluc (Lawrence Berkeley National Laboratory); Helen Xu (Georgia Institute of Technology)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 16:30–16:50 · Session 8: Optimizing for Memory（主席：Yan Gu）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638492) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

This paper introduces the batch-parallel Compressed Packed Memory Array (CPMA), a compressed, dynamic, ordered set data structure based on the Packed Memory Array (PMA). Traditionally, batch-parallel sets are built on pointer-based data structures such as trees because pointer-based structures enable fast parallel unions via pointer manipulation.Whencomparedwithcache-optimizedtrees,PMAswere slower to update but faster to scan. The batch-parallel CPMA overcomes this tradeoff between updates and scans by optimizing for cache-friendliness. On average, the CPMA achieves 3× faster batch-insert throughput and 4× faster range-query throughput compared with compressed PaC-trees, a state-of-the-art batch-parallel set library based on cache-optimized trees. We further evaluate the CPMA compared with compressed PaC-trees and Aspen, a state-of-the-art system, on a realworld application of dynamic-graph processing. The CPMA is on average 1.2× faster on a suite of graph algorithms and 2× faster on batch inserts when compared with compressed PaC-trees. Furthermore, the CPMA is on average 1.3× faster on graph algorithms and 2× faster on batch inserts compared with Aspen.

## 中文摘要

本文提出批并行压缩紧凑内存数组（CPMA），一种基于紧凑内存数组（PMA）的压缩、动态、有序集合数据结构。传统上，批并行集合构建在基于指针的数据结构（如树）之上，因为基于指针的结构可通过指针操作实现快速的并行并集。与缓存优化的树相比，PMA 更新较慢但扫描更快。批并行 CPMA 通过针对缓存友好性进行优化，克服了更新与扫描之间的这一取舍。平均而言，与压缩 PaC-tree（基于缓存优化树的最先进批并行集合库）相比，CPMA 的批量插入吞吐快 3 倍，范围查询吞吐快 4 倍。我们进一步在动态图处理这一真实应用上，将 CPMA 与压缩 PaC-tree 以及最先进系统 Aspen 进行了对比评估。在一套图算法上，CPMA 平均比压缩 PaC-tree 快 1.2 倍，批量插入快 2 倍。此外，与 Aspen 相比，CPMA 在图算法上平均快 1.3 倍，批量插入快 2 倍。

## 英文关键词

packed memory array, batch-parallel, compression, data structures, dynamic graphs

## 中文关键词

紧凑内存数组（PMA）；批并行；压缩；数据结构；动态图

---

## 一句话总结

> 提出批并行压缩紧凑内存数组 CPMA，在 PMA 基础上优化缓存友好性，突破更新与扫描之间的取舍，批量插入与范围查询吞吐分别比压缩 PaC-tree 快 3 倍和 4 倍。

## 研究问题

批并行集合通常依赖树等基于指针的结构以获得快速并行并集；而与缓存优化的树相比，PMA 虽然扫描更快，但更新更慢，二者之间存在难以兼顾的取舍。

## 方法简述

- 提出批并行压缩紧凑内存数组（CPMA），一种基于 PMA 的压缩、动态、有序集合数据结构
- 通过面向缓存友好性的优化，克服批量更新与扫描之间的传统取舍
- 在动态图处理这一真实应用中，将 CPMA 与压缩 PaC-tree 及最先进系统 Aspen 进行对比评测

## 主要结果

- 相比压缩 PaC-tree（基于缓存优化树的最先进批并行集合库），批量插入吞吐平均快 3 倍，范围查询吞吐平均快 4 倍
- 在一套图算法上平均快 1.2 倍、批量插入快 2 倍（对比压缩 PaC-tree）
- 相比 Aspen，图算法上平均快 1.3 倍、批量插入快 2 倍

---

> 所属 Session：[Session 8: Optimizing for Memory](index.md) · 返回 [PPoPP 2024 总览](../index.md)
