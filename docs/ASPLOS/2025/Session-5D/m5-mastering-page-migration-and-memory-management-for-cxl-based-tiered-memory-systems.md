---
title: "M5: Mastering Page Migration and Memory Management for CXL-based Tiered Memory Systems"
description: "ASPLOS 2025 · Session 5D · M5：面向基于 CXL 的分层内存系统的页迁移与内存管理"
tags:
  - "ASPLOS2025"
  - "Session 5D"
  - "CXL Storage"
---

# M5: Mastering Page Migration and Memory Management for CXL-based Tiered Memory Systems

**中文标题：** M5：面向基于 CXL 的分层内存系统的页迁移与内存管理

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yan Sun (University of Illinois Urbana-Champaign), Jongyul Kim (University of Illinois Urbana-Champaign), Zeduo Yu (University of Illinois Urbana-Champaign), Jiyuan Zhang (University of Illinois Urbana-Champaign), Siyuan Chai (University of Illinois Urbana-Champaign), Michael Jaemin Kim (Seoul National University), Hwayong Nam (Seoul National University), Jaehyun Park (Seoul National University), Eojin Na (Seoul National University), Yifan Yuan (Intel Labs), Ren Wang (Intel Labs), Jung Ho Ahn (Seoul National University), Tianyin Xu (University of Illinois Urbana-Champaign), Nam Sung Kim (University of Illinois Urbana-Champaign)

**单位：** University of Illinois Urbana-Champaign；Seoul National University；Intel Labs

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3711999) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

CXL has emerged as a promising memory interface that can cost-effectively expand the capacity and bandwidth of a memory system, complementing the traditional DDR interface. However, CXL DRAM presents 2–3× longer access latency than DDR DRAM, forming a tiered-memory system that demands an effective and efficient page-migration solution. Although many page-migration solutions have been proposed for past tiered-memory systems, they have achieved limited success. To tackle the challenge of managing tiered-memory systems, this work first presents a CXL-driven profiling solution to precisely and transparently count the number of accesses to every 4KB page and 64B word in CXL DRAM. Second, using the profiling solution, this work uncovers that (1) widely used CPU-driven page-migration solutions often identify warm pages as hot pages, and (2) certain applications have sparse hot pages, where only a small percentage of words in each of these pages are frequently accessed. Besides, this work demonstrates that the performance overhead of identifying hot pages is sometimes high enough to degrade application performance. Lastly, this work presents M5, a platform designed to facilitate the development of effective CXL-driven page-migration solutions, providing hardware-based hot-page and hot-word trackers in the CXL controller. On average, M5 can identify 47% hotter pages and offer 14% higher performance than the best CPU-driven page-migration solution, even with a simple policy.

## 中文摘要

CXL 已成为一种有前景的内存接口，能够以较低成本有效扩展内存系统的容量与带宽，并与传统 DDR 接口形成互补。然而，CXL DRAM 的访问延迟比 DDR DRAM 长 2–3 倍，由此构成分层内存系统，需要一种既有效又高效的页迁移方案。尽管针对以往的分层内存系统已提出许多页迁移方案，但它们取得的成效有限。为应对分层内存系统管理上的挑战，本工作首先提出一种由 CXL 驱动的剖析方案，能够精确且透明地统计对 CXL DRAM 中每个 4KB 页和 64B 字的访问次数。其次，借助该剖析方案，本工作揭示出：(1) 广泛使用的 CPU 驱动页迁移方案常常将温页（warm page）识别为热页（hot page）；(2) 某些应用的热页呈稀疏分布，即这些页中只有很小比例的字被频繁访问。此外，本工作还表明，识别热页的性能开销有时高到足以使应用性能下降。最后，本工作提出 M5，这是一个旨在促进有效的 CXL 驱动页迁移方案开发的平台，在 CXL 控制器中提供基于硬件的热页与热字跟踪器。平均而言，即便采用简单策略，M5 也能比最佳的 CPU 驱动页迁移方案多识别出 47% 的更热页，并提供高出 14% 的性能。

## 英文关键词

Compute Express Link, DRAM, Tiered Memory, Near Memory Processing, Page Migration

## 中文关键词

Compute Express Link；DRAM；分层内存；近内存处理；页迁移

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3711999)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2025](../index.md)
