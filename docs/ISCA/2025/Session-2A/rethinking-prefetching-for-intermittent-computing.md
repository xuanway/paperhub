---
title: "Rethinking Prefetching for Intermittent Computing"
description: "ISCA 2025 · Session 2A · 重新思考间歇计算中的预取"
tags:
  - "ISCA2025"
  - "Session 2A"
  - "Best Paper Nominees"
---

# Rethinking Prefetching for Intermittent Computing

**中文标题：** 重新思考间歇计算中的预取

**所属 Session：** [Session 2A](index.md) · [ISCA 2025](../index.md)

**作者：** Gan Fang, Jianping Zeng, Aditya Gupta, Changhee Jung

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731038) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Prefetching improves performance by reducing cache misses. However, conventional prefetchers are too aggressive to serve batteryless energy harvesting systems (EHSs) where energy efficiency is the utmost design priority due to weak input energy and the resulting frequent outages. To this end, this paper proposes IPEX, an Intermittence-aware Prefetching EXtension that can be integrated into existing prefetchers on EHSs. IPEX aims to avert useless prefetches by suppressing the prefetching of the cache blocks receiving no hit before their loss on power failure, which would otherwise waste harvested energy. At a proper moment before an upcoming outage, IPEX throttles the prefetch degree to target only those blocks that are likely to be used before the outage. That way IPEX saves energy and spends it on making further execution progress. Experimental results show that on average, IPEX reduces energy consumption by 7.86% (up to 21.64%) and improves performance by 8.96% (up to 23.49%) compared to a conventional prefetcher.

## 中文摘要

预取技术通过降低缓存缺失来提升性能。但传统预取器的预取策略过于激进，并不适合无电池能量采集系统（EHS）。这类系统输入能量微弱，频繁发生断电，能量效率是首要设计目标。为此，本文提出IPEX——一种感知间歇特性的预取扩展模块，可集成到能量采集系统现有的预取器中。IPEX的核心思路是避免无效预取：如果某个缓存块在断电丢失前不会被命中，则抑制对该块的预取，避免浪费采集到的能量。在即将断电前的合适时机，IPEX会限制预取度，仅预取断电前大概率会被访问的缓存块。借此，IPEX节约能量，并将能量用于推进程序执行。实验结果表明，相比传统预取器，IPEX平均降低7.86%的能耗（最高21.64%），同时性能平均提升8.96%（最高23.49%）。

## 英文关键词

Intermittent computing, prefetching, non-volatile memory, energy harvesting

## 中文关键词

间歇计算, 能量采集系统, 预取节流, 断电预测, 能耗优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731038)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 2A](index.md) · [返回 ISCA 2025](../index.md)
