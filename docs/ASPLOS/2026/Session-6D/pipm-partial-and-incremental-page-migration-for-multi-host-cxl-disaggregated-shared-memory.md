---
title: "PIPM: Partial and Incremental Page Migration for Multi-host CXL Disaggregated Shared Memory"
description: "ASPLOS 2026 · Session 6D · PIPM：面向多主机 CXL 分离式共享内存的部分与增量页迁移"
tags:
  - "ASPLOS2026"
  - "Session 6D"
  - "Disaggregated Memory Systems"
---

# PIPM: Partial and Incremental Page Migration for Multi-host CXL Disaggregated Shared Memory

**中文标题：** PIPM：面向多主机 CXL 分离式共享内存的部分与增量页迁移

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Gangqi Huang (University of California, Santa Cruz), Heiner Litz (University of California, Santa Cruz), Yuanchao Xu (University of California, Santa Cruz)

**单位：** University of California, Santa Cruz

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790203) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The emerging Compute Express Link (CXL) interconnect supports multi-host cache-coherent disaggregated shared memory (CXL-DSM). However, existing page migration approaches, designed primarily for single-host systems, are inefficient in multi-host CXL-DSM scenarios. To address this, we propose Partial and Incremental Page Migration (PIPM), a hardware-based solution that transparently leverages host-side local memory. PIPM is co-designed with the CXL multi-host coherence protocol, enabling coherent access to data residing in local DRAM. To overcome limitations of existing migration methods, PIPM supports fine-grained data migration and integrates hardware-based monitoring and decision-making mechanisms to optimize data placement. Evaluation results demonstrate that PIPM delivers performance improvements of up to 2.54× (1.86× on average) over the default multi-host CXL-DSM configuration.

## 中文摘要

新兴的 Compute Express Link (CXL) 互连支持多主机缓存一致的分离式共享内存（CXL-DSM）。然而，现有的页迁移方法主要针对单主机系统设计，在多主机 CXL-DSM 场景中效率低下。为解决这一问题，我们提出部分与增量页迁移（PIPM），一种基于硬件、可透明利用主机侧本地内存的解决方案。PIPM 与 CXL 多主机一致性协议协同设计，从而能够对驻留在本地 DRAM 中的数据进行一致性访问。为克服现有迁移方法的局限，PIPM 支持细粒度数据迁移，并集成了基于硬件的监控与决策机制以优化数据放置。评估结果表明，相较默认的多主机 CXL-DSM 配置，PIPM 带来最高 2.54×（平均 1.86×）的性能提升。

## 英文关键词

Distributed Shared Memory, Disaggregated Memory, Page Migration, Cache Coherency, Compute eXpress Link

## 中文关键词

分布式共享内存；分离式内存；页迁移；缓存一致性；Compute eXpress Link

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790203)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2026](../index.md)
