---
title: "Systematic CXL Memory Characterization and Performance Analysis at Scale"
description: "ASPLOS 2025 · Session 5D · 大规模 CXL 内存的系统化表征与性能分析"
tags:
  - "ASPLOS2025"
  - "Session 5D"
  - "CXL Storage"
---

# Systematic CXL Memory Characterization and Performance Analysis at Scale

**中文标题：** 大规模 CXL 内存的系统化表征与性能分析

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jinshu Liu (Virginia Tech), Hamid Hadian (Virginia Tech), Yuyue Wang (Virginia Tech), Daniel S. Berger (Microsoft and University of Washington), Marie Nguyen (Samsung), Xun Jian (Virginia Tech), Sam H. Noh (Virginia Tech), Huaicheng Li (Virginia Tech)

**单位：** Virginia Tech；Microsoft and University of Washington；Samsung

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715987) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Compute Express Link (CXL) has emerged as a pivotal interconnect for memory expansion. Despite its potential, the performance implications of CXL across devices, latency regimes, processors, and workloads remain underexplored. We present Melody, a framework for systematic characterization and analysis of CXL memory performance. Melody builds on an extensive evaluation spanning 265 workloads, 4 real CXL devices, 7 latency levels, and 5 CPU platforms. Melody yields many insights: workload sensitivity to sub-µs CXL latencies (140-410ns), the first disclosure of CXL tail latencies, CPU tolerance to CXL latencies, a novel approach (Spa) for pinpointing CXL bottlenecks, and CPU prefetcher inefficiencies under CXL.

## 中文摘要

Compute Express Link（CXL）已成为内存扩展的关键互连技术。尽管潜力可观，CXL 在不同设备、延迟区间、处理器与工作负载下的性能影响仍未被充分探索。我们提出 Melody，一个用于系统化表征与分析 CXL 内存性能的框架。Melody 建立在广泛的评估之上，覆盖 265 个工作负载、4 个真实 CXL 设备、7 个延迟等级和 5 个 CPU 平台。Melody 得出许多洞见：工作负载对亚微秒级 CXL 延迟（140-410ns）的敏感性、首次披露 CXL 尾部延迟、CPU 对 CXL 延迟的容忍度、一种用于精确定位 CXL 瓶颈的新方法（Spa），以及 CXL 下 CPU 预取器的低效问题。

## 英文关键词

Compute Express Link, CXL, Memory, Profiling

## 中文关键词

Compute Express Link；CXL；内存；性能剖析

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715987)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2025](../index.md)
