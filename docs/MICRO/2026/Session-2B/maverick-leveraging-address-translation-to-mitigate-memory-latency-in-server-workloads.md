---
title: "Maverick: Leveraging Address Translation to Mitigate Memory Latency in Server Workloads"
description: "MICRO 2026 · Session 2B · Maverick：利用地址转换降低服务器工作负载的内存访问时延"
tags:
  - "MICRO2026"
  - "Quantum Computing"
  - "Address Translation"
---

# Maverick: Leveraging Address Translation to Mitigate Memory Latency in Server Workloads

**中文标题：** Maverick：利用地址转换降低服务器工作负载的内存访问时延

**所属 Session：** [Session 2B](index.md) · [MICRO 2026](../index.md)

**作者：** Ho Je Lee, Minchan Kim, Jaewon Kwon, Jain Koo, Yongju Lee, Won Hur, Jiwon Lee, Won Woo Ro

**来源：** MICRO 2026，pp. 660–675；[DOI](https://doi.org/10.1109/MICRO67795.2026.00058)

## 英文摘要

Long memory latency remains a major performance bottleneck in modern processors. To mitigate this cost, processors rely on the cache hierarchy, which is designed for low-latency access on a hit. On a miss, however, the request pays the lookup latency of each cache that misses before reaching a lower level in the memory hierarchy. This paper identifies two highly exploitable characteristics of address translation that can be used to eliminate part of the on-chip cache latency. First, when a translation misses in the TLB hierarchy, the resulting page walk fetches translation data such as page-table entries through the cache hierarchy. Because dedicated structures such as TLBs and page walk caches filter out high-locality translation accesses before cache access, page walk requests exhibit fundamentally different locality characteristics from instruction/data requests. Second, because address translation precedes dependent instruction and data accesses, the level at which a translation is resolved in the translation hierarchy correlates with the level at which the resulting instruction and data requests are ultimately served in the memory hierarchy. A similar trend also holds within the translation process itself, where later page walk requests follow the locality implied by the earlier translation requests. Based on these observations, we propose Maverick, a mechanism that exploits address translation to reduce on-chip cache-traversal latency for translations as well as instruction and data accesses, all of which are critical bottlenecks in server workloads. Maverick bypasses ineffective upper-level cache accesses for translation requests and uses translation-driven off-chip prediction to overlap long-latency memory accesses with cache traversal. Our evaluation with 359 Google server traces from the 4th Data Prefetching Championship shows that Maverick reduces stall cycles due to off-chip memory requests by 20.99% on average and improves geomean performance by 5.12%, outperforming prior off-chip predictors.

## 中文摘要

长内存时延仍然是现代处理器的主要性能瓶颈。为了降低这种成本，处理器依赖于缓存层次结构，该层次结构专为命中时的低时延访问而设计。然而，如果未命中，请求将在到达内存层次结构中的较低级别之前支付每个未命中缓存的查找时延。本文确定了地址转换的两个高度可利用的特性，可用于消除部分片上缓存时延。首先，当 TLB 层次结构中的转换未命中时，生成的页遍历会通过缓存层次结构获取转换数据，例如页表条目。由于 TLB 和页表遍历缓存等专用结构会在缓存访问之前过滤掉高局部性转换访问，因此页表遍历请求表现出与指令/数据请求根本不同的局部性特征。其次，因为地址转换先于相关指令和数据访问，所以在转换层次结构中解析转换的级别与最终在存储器层次结构中服务结果指令和数据请求的级别相关。类似的趋势也存在于地址转换过程本身中，其中后来的页表遍历请求遵循早期地址转换请求所暗示的位置。基于这些观察，我们提出了 Maverick，一种利用地址转换来减少转换以及指令和数据访问的片上缓存遍历时延的机制，所有这些都是服务器工作负载的关键瓶颈。 Maverick 绕过地址转换请求的无效上层缓存访问，并使用地址转换驱动的片外预测将长时延内存访问与缓存遍历重叠。我们对第四届数据预取锦标赛的 359 个 Google 服务器跟踪进行的评估表明，Maverick 将由于片外内存请求导致的停顿周期平均减少了 20.99%，并将几何平均性能提高了 5.12%，优于之前的片外预测器。

## 中文关键词

地址转换；内存层次结构；片外访问预测；服务器工作负载

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 2B](index.md) · [MICRO 2026 主页](../index.md)
