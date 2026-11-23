---
title: "Profile-Guided Temporal Prefetching"
description: "ISCA 2025 · Session 4B · 配置文件引导的时序预取"
tags:
  - "ISCA2025"
  - "Session 4B"
  - "Microarchitecture I"
---

# Profile-Guided Temporal Prefetching

**中文标题：** 配置文件引导的时序预取

**所属 Session：** [Session 4B](index.md) · [ISCA 2025](../index.md)

**作者：** Mengming Li, Qijun Zhang, Yichuan Gao, Wenji Fang, Yao Lu, Yongqing Ren, Zhiyao Xie

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731070) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Temporal prefetching shows promise for handling irregular mem- ory access patterns, which are common in data-dependent and pointer-based data structures. Recent studies introduced on-chip metadata storage to reduce the memory traffic caused by access- ing metadata from off-chip DRAM. However, existing prefetching schemes struggle to efficiently utilize the limited on-chip storage. An alternative solution, software indirect access prefetching, re- mains ineffective for optimizing temporal prefetching. In this work, we propose Prophet—a hardware-software co- designed framework that leverages profile-guided methods to op- timize metadata storage management. Prophet profiles programs using counters instead of traces, injects hints into programs to guide metadata storage management, and dynamically tunes these hints to enable the optimized binary to adapt to different program inputs. Prophet is designed to coexist with existing hardware tem- poral prefetchers, delivering efficient, high-performance solutions for frequently executed workloads while preserving the original runtime scheme for less frequently executed workloads. Prophet outperforms the state-of-the-art temporal prefetcher, Triangel, by 14.23%, effectively addressing complex temporal patterns where prior profile-guided solutions fall short (only achieving 0.1% per- formance gain). Prophet delivers superior performance across all evaluated workload inputs, introducing negligible profiling, analy- sis, and instruction overhead.

## 中文摘要

时间预取在处理不规则访存模式方面很有潜力，这类访存广泛存在于数据依赖型、基于指针的数据结构中。现有研究引入片上元数据存储，减少从片外DRAM读取元数据带来的访存流量。但现有预取方案难以高效利用有限的片上存储；另一种方案——软件间接访问预取，对时间预取的优化效果也不佳。

本文提出Prophet，一款软硬件协同设计框架，基于剖面引导方法优化元数据存储管理。Prophet使用计数器而非访存轨迹对程序进行剖面采集，向程序注入提示信息以指导元数据存储管理，并动态调整提示，使优化后的二进制程序能够适配不同输入。Prophet可以和现有硬件时间预取器共存：对高频负载提供高性能优化方案，低频负载则保留原有运行机制。
Prophet对比当前最优时间预取器Triangel性能提升14.23%，能够处理复杂时间访存模式，而以往剖面引导方案在此类场景下效果很差（仅0.1%性能提升）。在所有测试负载输入下Prophet均表现更优，剖面采集、分析与指令开销极小。

## 英文关键词

Temporal Prefetching, Profile-Guided Optimization

## 中文关键词

时序预取, 剖析引导优化

## 代码与研究制品

- [代码仓库](https://github.com/hkust-zhiyao/Prophet)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731070)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4B](index.md) · [返回 ISCA 2025](../index.md)
