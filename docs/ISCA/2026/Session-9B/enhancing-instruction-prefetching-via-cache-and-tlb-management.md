---
title: "Enhancing Instruction Prefetching via Cache and TLB Management"
description: "ISCA 2026 · Session 9B · Enhancing Instruction Prefetching via Cache and TLB Management"
tags:
  - "ISCA2026"
  - "Session 9B"
  - "Prefetching and Cache 2"
---

# Enhancing Instruction Prefetching via Cache and TLB Management

**中文标题：** 通过缓存与 TLB 管理增强指令预取

**所属 Session：** [Session 9B](index.md) · [ISCA 2026](../index.md)

**作者：** Alexandre Valentin Jamet, Dimitrios Chasapis, Georgios Vavouliotis, Marc Casas, Martí Torrents

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Modern server workloads have massive instruction footprints, exacerbating pressure on the processor front-end, and making techniques like L1 instruction (L1I) prefetching essential to alleviate this bottleneck. Although L1I prefetchers deliver significant performance gains, their full potential remains underutilized due to two main factors: i) L1I prefetch requests that cross page boundaries require address translation before being issued, and the latency involved in retrieving these translations undermines the timeliness of the L1I prefetches; ii) the reuse potential of code lines fetched in the cache hierarchy by L1I prefetches is highly variable—while a few lines are accessed multiple times, many are dead-on-arrival. This paper proposes the Instruction Prefetch Centric Cache and TLB Management (IP-CaT), a microarchitectural scheme orchestrating TLB and cache management to maximize the benefits of L1I prefetching. IP-CaT comprises two modules: i) the translation Prefetch Buffer (tPB), a small buffer located alongside the last-level TLB (sTLB) that accommodates translations fetched by L1I page-cross prefetches to reduce the address translation cost of L1I prefetching and ii) the Trimodal Instruction Prefetch Replacement Policy (TIPRP), a decision-tree based replacement policy for the L2 cache (L2C) specialized in the management of lines fetched by L1I prefetches. Our evaluation shows that IP-CaT delivers significant performance benefits when integrated with three state-of-the-art L1I prefetchers (EPI [1], FNL+MMA [2], Barc¸a [3]). For example, IP-CaT+EPI achieves a 6.1% geomean speedup over EPI across a set of 105 contemporary server workloads. We also show that IP-CaT outperforms the state-of-the-art instruction TLB prefetcher [4], the leading TLB replacement policy [5], and code-aware, prefetch-aware, and general-purpose cache replacement policies (Emissary [6], SHiP++ [7], Mockingjay [8]).

## 中文摘要

现代服务器工作负载具有庞大的指令足迹，加剧了对处理器前端的压力，使得 L1 指令（L1I）预取等技术成为缓解这一瓶颈的关键。尽管 L1I 预取器带来了显著的性能提升，但由于两个主要因素，其全部潜力仍未得到充分利用：i）跨越页边界的 L1I 预取请求在发出之前需要地址转换，而获取这些转换所需的延迟削弱了 L1I 预取的及时性；ii）由 L1I 预取在缓存层次结构中取出的代码行的重用潜力差异很大——少数行被多次访问，而许多行一到达就已无用。本文提出以指令预取为中心的缓存与 TLB 管理（IP-CaT），一种协调 TLB 和缓存管理的微架构方案，以最大化 L1I 预取的收益。IP-CaT 包含两个模块：i）转换预取缓冲区（tPB），一个位于末级 TLB（sTLB）旁边的小型缓冲区，用于容纳由 L1I 跨页预取获取的地址转换，以降低 L1I 预取的地址转换成本；ii）三模态指令预取替换策略（TIPRP），一种基于决策树的 L2 缓存（L2C）替换策略，专门用于管理由 L1I 预取取出的行。我们的评估表明，IP-CaT 与三种最先进的 L1I 预取器（EPI [1]、FNL+MMA [2]、Barça [3]）集成时可带来显著的性能收益。例如，IP-CaT+EPI 在一组 105 个当代服务器工作负载上相对于 EPI 实现了 6.1% 的几何平均加速。我们还表明，IP-CaT 优于最先进的指令 TLB 预取器 [4]、领先的 TLB 替换策略 [5]，以及代码感知、预取感知和通用缓存替换策略（Emissary [6]、SHiP++ [7]、Mockingjay [8]）。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9B](index.md) · [返回 ISCA 2026](../index.md)
