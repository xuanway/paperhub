---
title: "Don't Get Stuck in Traffic: A Case for Contention-Aware Translation Offloading"
description: "MICRO 2026 · Session 8B · Don't Get Stuck in Traffic：面向资源争用感知的地址转换卸载"
tags:
  - "MICRO2026"
---

# Don't Get Stuck in Traffic: A Case for Contention-Aware Translation Offloading

**中文标题：** Don't Get Stuck in Traffic：面向资源争用感知的地址转换卸载

**所属 Session：** [Session 8B](index.md) · [MICRO 2026](../index.md)

**作者：** Osang Kwon, Yongho Lee, Sungbin Jang, Kyeongchan Kim, Seokin Hong

**来源：** MICRO 2026，pp. 2909–2923；[DOI](https://doi.org/10.1109/MICRO67795.2026.00197)

## 英文摘要

CXL-based tiered memory is emerging as a promising approach for scaling memory capacity and bandwidth beyond the limits of conventional DRAM channels. In this architecture, local DRAM serves as the fast tier, while CXL-attached memory (CMM) provides capacity expansion. Consequently, performance increasingly depends on how effectively memory traffic is balanced across the two tiers. However, page tables remain in local DRAM, forcing all page walks to access the fast tier regardless of its contention level. These page walks increase contention in local DRAM and compete with regular data accesses. Under heavy contention, local DRAM latency can increase substantially and even exceed CMM latency. To tackle this problem, we propose CATO, a contention-aware translation offloading mechanism that adapts the translation path based on runtime tier latency. CATO periodically monitors the latency of local DRAM and CMM using low-overhead hardware counters, then selects the faster tier for address translation. On each TLB miss, the MMU follows this decision, either performing a conventional page-table walk in local DRAM or offloading the translation to CMM. To enable offloading, CATO maintains a compact, hash-indexed replica of last-level PTEs in a reserved region of CMM. Across memory-intensive and irregular workloads, CATO reduces translation latency by 33% and improves application performance by 15.8% on average. Even with Transparent Huge Pages (THP) enabled, which inherently reduces translation overhead, CATO still delivers a 7% performance improvement.

## 中文摘要

基于 CXL 的分层内存正在成为一种有前途的方法，可将内存容量和带宽扩展到传统 DRAM 通道的限制之外。在此架构中，本地 DRAM 作为快速层，而 CXL 附加内存 (CMM) 提供容量扩展。因此，性能越来越取决于两层之间内存流量的平衡效率。然而，页表保留在本地 DRAM 中，强制所有页遍历访问快速层，无论其争用级别如何。这些页表遍历增加了本地 DRAM 中的争用，并与常规数据访问竞争。在严重争用的情况下，本地 DRAM 时延可能会大幅增加，甚至超过 CMM 时延。为了解决这个问题，我们提出了 CATO，一种竞争感知的翻译卸载机制，可以根据运行时层时延来调整翻译路径。 CATO 使用低开销硬件计数器定期监控本地 DRAM 和 CMM 的时延，然后选择更快的层进行地址转换。每次 TLB 未命中时，MMU 都会遵循此决定，要么在本地 DRAM 中执行传统的页表遍历，要么将转换卸载到 CMM。为了实现卸载，CATO 在 CMM 的保留区域中维护最后一级 PTE 的紧凑、哈希索引副本。在内存密集型和不规则工作负载中，CATO 平均将翻译时延减少了 33%，并将应用程序性能提高了 15.8%。即使启用了透明大页 (THP)（本质上减少了转换开销），CATO 仍可实现 7% 的性能提升。

## 中文关键词

虚拟内存；页表遍历；分层内存；CXL 内存；争用感知卸载

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8B](index.md) · [MICRO 2026 主页](../index.md)
