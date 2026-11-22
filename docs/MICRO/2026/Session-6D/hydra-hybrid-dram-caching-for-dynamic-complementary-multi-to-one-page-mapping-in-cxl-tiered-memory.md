---
title: "HYDRA: Hybrid DRAM Caching for Dynamic Complementary Multi-to-One Page Mapping in CXL Tiered Memory"
description: "MICRO 2026 · Session 6D · HYDRA：面向 CXL 分层内存中动态互补多对一页映射的混合 DRAM 缓存"
tags:
  - "MICRO2026"
  - "CXL"
  - "DRAM"
  - "Cache"
---

# HYDRA: Hybrid DRAM Caching for Dynamic Complementary Multi-to-One Page Mapping in CXL Tiered Memory

**中文标题：** HYDRA：面向 CXL 分层内存中动态互补多对一页映射的混合 DRAM 缓存

**所属 Session：** [Session 6D](index.md) · [MICRO 2026](../index.md)

**作者：** Gangqi Huang, Heiner Litz, Yuanchao Xu

**来源：** MICRO 2026，pp. 2216–2230；[DOI](https://doi.org/10.1109/MICRO67795.2026.00153)

## 英文摘要

CXL-enabled tiered memory combines high-capacity remote memory with limited host-side local DRAM caches. However, existing DRAM caching designs underutilize local DRAM due to coarse page-granularity management and intra-page sparsity, where only a subset of each page is frequently accessed. We observe that different pages often have complementary intra-page access patterns, enabling multiple remote pages to share one local DRAM cache page. Supporting such dynamic multi-to-one mapping is challenging because PT-based DRAM caches enforce dynamic one-to-one mappings, while tag-based designs rely on static mappings. We propose HYDRA, a DRAM caching architecture that enables dynamic complementary multi-to-one page mapping. HYDRA combines tag-based and page-table-based caching with an intermediate physical address space to support efficient multi-page sharing with low hardware overhead. It further introduces device-side cache management to learn intra-page access patterns and revoke ineffective mappings. Across memory-intensive workloads, HYDRA improves local DRAM cache utilization, reduces remote traffic, and outperforms prior DRAM caching designs.

## 中文摘要

支持 CXL 的分层内存将大容量远程内存与有限的主机端本地 DRAM 缓存相结合。然而，由于粗页粒度管理和页内稀疏性（仅频繁访问每个页的子集），现有 DRAM 缓存设计未充分利用本地 DRAM。我们观察到，不同的页面通常具有互补的页面内访问模式，从而使多个远程页面能够共享一个本地 DRAM 缓存页面。支持这种动态多对一映射具有挑战性，因为基于 PT 的 DRAM 缓存强制执行动态一对一映射，而基于标签的设计依赖于静态映射。我们提出了 HYDRA，这是一种 DRAM 缓存架构，可实现动态互补的多对一页面映射。 HYDRA 将基于标签和基于页表的缓存与中间物理地址空间相结合，以低硬件开销支持高效的多页面共享。它还引入了设备端缓存管理来学习页面内访问模式并撤销无效映射。在内存密集型工作负载中，HYDRA 提高了本地 DRAM 缓存利用率，减少了远程流量，并优于之前的 DRAM 缓存设计。

## 中文关键词

DRAM 缓存；分层内存；CXL；动态页映射

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6D](index.md) · [MICRO 2026 主页](../index.md)
