---
title: "PACT: A Criticality-First Design for Tiered Memory"
description: "ASPLOS 2026 · Session 8C · PACT：一种面向分层内存的关键性优先设计"
tags:
  - "ASPLOS2026"
  - "Session 8C"
  - "Memory Hierarchy & Performance"
---

# PACT: A Criticality-First Design for Tiered Memory

**中文标题：** PACT：一种面向分层内存的关键性优先设计

**所属 Session：** [Session 8C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Hamid Hadian (Virginia Tech), Jinshu Liu (Virginia Tech), Hanchen Xu (Virginia Tech), Hansen Idden (Virginia Tech), Huaicheng Li (Virginia Tech)

**单位：** Virginia Tech

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790198) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Tiered memory systems typically place pages based on access frequency (hotness), yet frequency alone fails to capture the true performance impact. We present PACT, an online, pagegranular tiered memory design that elevates performance criticality to a first-class design principle. At its core is Per-page Access Criticality (PAC), a fine-grained metric that quantifies each page's contribution to application performance rather than merely counting accesses. PACT profiles PAC online using a lightweight analytical model that uniquely decomposes per-tier memory-level parallelism via hardware queue occupancy counters, enabling direct CPU stall attribution to individual pages. To handle highly skewed PAC distributions, PACT employs PAC-centric migration policies: eager demotion and adaptive promotion, to dynamically place performance-critical pages in DRAM. Across 13 workloads, PACT achieves up to 61% performance improvement over the best of 7 state-of-the-art tiering designs with up to 50× fewer migrations.

## 中文摘要

分层内存系统通常依据访问频率（热度）来放置页面，然而仅凭频率无法刻画真实的性能影响。我们提出 PACT，一种在线、页粒度的分层内存设计，将性能关键性提升为首要的设计原则。其核心是逐页访问关键性（Per-page Access Criticality，PAC），这一细粒度度量量化每个页面对应用性能的贡献，而不仅仅是统计访问次数。PACT 使用轻量级分析模型在线刻画 PAC，该模型通过硬件队列占用计数器以独特方式分解各层的内存级并行度，从而能够将 CPU 停顿直接归因到单个页面。为应对高度倾斜的 PAC 分布，PACT 采用以 PAC 为中心的迁移策略：积极降级与自适应提升，从而将性能关键页面动态放置到 DRAM 中。在 13 个负载上，PACT 相比 7 种最先进分层设计中的最优者取得最高 61% 的性能提升，同时迁移次数最多减少 50×。

## 英文关键词

Tiered Memory, Compute Express Link (CXL), Operating Systems

## 中文关键词

分层内存；Compute Express Link (CXL)；操作系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790198)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8C](index.md) · [返回 ASPLOS 2026](../index.md)
