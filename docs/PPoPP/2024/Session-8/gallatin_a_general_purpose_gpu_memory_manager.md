---
title: "Gallatin: A General-Purpose GPU Memory Manager"
description: "PPoPP 2024 Session Optimizing for Memory：基于 vEB 树的通用 GPU 内存管理器，混合尺寸分配最高 264×"
tags:
  - "PPoPP2024"
  - "Session-8"
  - "Optimizing for Memory"
  - "GPU Memory Management"
  - "Concurrent Data Structures"
  - "van Emde Boas Tree"
authors:
  - "Hunter McCoy"
  - "Prashant Pandey"
session: "Session 8: Optimizing for Memory"
session_number: 8
session_chair: "Yan Gu"
date: "2024-03-05"
time: "16:50–17:10"
room: "Moorfoot"
doi: "10.1145/3627535.3638499"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Gallatin: A General-Purpose GPU Memory Manager

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Gallatin 是通用高性能 GPU 内存管理器，用 van Emde Boas 树管理任意大小内存对象，并给出支持常数时间插入、删除与后继操作的高并发 GPU vEB 树实现。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 8: Optimizing for Memory</p>
</div>

**作者**：Hunter McCoy, Prashant Pandey (University of Utah)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 16:50–17:10 · Session 8: Optimizing for Memory（主席：Yan Gu）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638499) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Dynamic memory management is critical for efficiently porting modern data processing pipelines to GPUs. However, building a general-purpose dynamic memory manager on GPUs is challenging due to the massive parallelism and weak memory coherence. Existing state-of-the-art GPU memory managers, Ouroboros and Reg-Eff, employ traditional data structures such as arrays and linked lists to manage memory objects. They build specialized pipelines to achieve performance for a fixed set of allocation sizes and fall back to the CUDA allocator for allocating large sizes. In the process, they lose general-purpose usability and fail to support critical applications such as streaming graph processing. In this paper, we introduce Gallatin, a general-purpose and high-performance GPU memory manager. Gallatin uses the van Emde Boas (vEB) tree data structure to manage memory objects efficiently and supports allocations of any size. Furthermore,wedevelopahighly-concurrentGPUimplemen-tation of the vEB tree which can be broadly used in other GPU applications. It supports constant time insertions, deletions, and successor operations for a given memory size. In our evaluation, we compare Gallatin with state-of-the-art specialized allocator variants. Gallatin is up to 374× faster onsingle-sizedallocationsandupto264×fasteronmixed-size allocations than the next-best allocator. In scalability benchmarks, Gallatin is up to 254× times faster than the next-best allocator as the number of threads increases. For the graph benchmarks, Gallatin is 1.5× faster than the state-of-the-art for bulk insertions, slightly faster for bulk deletions, and is 3× faster than the next-best allocator for all graph expansion tests.

## 中文摘要

动态内存管理对于将现代数据处理流水线高效移植到 GPU 至关重要。然而，由于大规模并行和弱内存一致性，在 GPU 上构建通用的动态内存管理器具有挑战性。现有的最先进 GPU 内存管理器 Ouroboros 和 Reg-Eff 采用数组和链表等传统数据结构来管理内存对象。它们构建专用流水线以针对一组固定的分配大小实现性能，并对大尺寸分配回退到 CUDA 分配器。在此过程中，它们失去了通用可用性，无法支持流式图处理等关键应用。本文提出 Gallatin，一个通用且高性能的 GPU 内存管理器。Gallatin 使用 van Emde Boas（vEB）树数据结构来高效管理内存对象，并支持任意大小的分配。此外，我们开发了一个高度并发的 vEB 树 GPU 实现，可广泛用于其他 GPU 应用。对于给定的内存大小，它支持常数时间的插入、删除和后继操作。在评估中，我们将 Gallatin 与最先进的专用分配器变体进行比较。与次优分配器相比，Gallatin 在单尺寸分配上最高快 374 倍，在混合尺寸分配上最高快 264 倍。在可扩展性基准中，随着线程数增加，Gallatin 最高比次优分配器快 254 倍。在图基准中，Gallatin 在批量插入上比最先进方案快 1.5 倍，在批量删除上略快，并且在所有图扩展测试中比次优分配器快 3 倍。

## 英文关键词

GPU; Memory allocation; Concurrent data structures; High performance computing

## 中文关键词

GPU；内存分配；并发数据结构；高性能计算

---

## 一句话总结

> Gallatin 是通用高性能 GPU 内存管理器，用 van Emde Boas 树管理任意大小内存对象，并给出支持常数时间插入、删除与后继操作的高并发 GPU vEB 树实现。

## 研究问题

GPU 上的大规模并行与弱内存一致性使通用动态内存管理器难以构建；Ouroboros、Reg-Eff 等现有最优方案用数组和链表为固定分配尺寸搭建专用流水线、大尺寸回退 CUDA 分配器，因而失去通用性，无法支持流式图处理等关键应用。

## 方法简述

- 提出 Gallatin 通用高性能 GPU 内存管理器，采用 van Emde Boas（vEB）树高效管理内存对象并支持任意大小分配
- 开发高度并发的 GPU vEB 树实现，可广泛用于其他 GPU 应用
- 设计使该树对给定内存大小支持常数时间的插入、删除与后继（successor）操作

## 主要结果

- 与次优分配器相比，单尺寸分配最高快 374 倍，混合尺寸分配最高快 264 倍
- 可扩展性基准中，随线程数增加最高比次优分配器快 254 倍
- 图基准中批量插入比最先进方案快 1.5 倍、批量删除略快，所有图扩展测试中比次优分配器快 3 倍

---

> 所属 Session：[Session 8: Optimizing for Memory](index.md) · 返回 [PPoPP 2024 总览](../index.md)
