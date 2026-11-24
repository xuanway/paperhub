---
title: "Five-Minute Rule 40 Years Later: A First-Principles Revisit for Modern Memory Hierarchy"
description: "ISCA 2026 · Session 2D · Five-Minute Rule 40 Years Later: A First-Principles Revisit for Modern Memory Hierarchy"
tags:
  - "ISCA2026"
  - "Session 2D"
  - "Storage"
---

# Five-Minute Rule 40 Years Later: A First-Principles Revisit for Modern Memory Hierarchy

**中文标题：** 40 年后的五分钟法则：面向现代内存层次结构的第一性原理重审

**所属 Session：** [Session 2D](index.md) · [ISCA 2026](../index.md)

**作者：** Tong Zhang, Vikram Sharma Mailthody, Fei Sun, Linsen Ma, Chris J. Newburn, Teresa Zhang, Yang Liu, Jiangpeng Li, Hao Zhong, Wen-Mei Hwu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

In 1987, Jim Gray and Gianfranco Putzolu introduced the five-minute rule, a simple, storage-memory-economics-based heuristic for deciding when data should live in DRAM rather than on storage. Subsequent revisits to the rule largely retained that economics-only view, leaving host costs, feasibility limits, and workload behavior out of scope. This paper revisits the rule from first principles, integrating host costs, DRAM bandwidth/capacity, and physics-grounded models of SSD performance and cost, and then embedding these elements in a constraint- and workload-aware framework that yields actionable provisioning guidance. We show that, for modern AI platforms, especially GPU-centric hosts paired with ultra-high-IOPS SSDs engineered for fine-grained random access, the DRAM↔flash caching threshold collapses from minutes to a few seconds. This shift reframes NAND flash memory as an active data tier and exposes a broad research space across the hardware–software stack. We further introduce MQSim-Next, a calibrated SSD simulator that supports validation and sensitivity analysis and facilitates future architectural and system research. Finally, we present two concrete case studies that showcase the software system design space opened by such memory hierarchy paradigm shift. Overall, we turn a classical heuristic into an actionable, feasibility-aware analysis and provisioning framework and set the stage for further research on AI-era memory hierarchy.

## 中文摘要

1987年，Jim Gray和Gianfranco Putzolu提出了五分钟法则，这是一种基于存储-内存经济学的简单启发式规则，用于判断数据应存放在DRAM中还是存储设备上。此后对该规则的重新审视大多保留了纯经济学的视角，未将主机成本、可行性限制和工作负载行为纳入考量。本文从第一性原理重新审视该法则，整合了主机成本、DRAM带宽/容量以及基于物理的SSD性能和成本模型，并将这些要素嵌入一个约束感知和工作负载感知的框架中，从而得出可操作的配置指导。我们发现，对于现代AI平台，尤其是以GPU为中心的主机配合专为细粒度随机访问设计的高IOPS SSD时，DRAM↔闪存缓存阈值从分钟级缩小到秒级。这一转变将NAND闪存重新定位为活跃数据层，并在整个软硬件栈中开辟了广阔的研究空间。我们进一步介绍了MQSim-Next，一个经校准的SSD模拟器，支持验证和敏感性分析，并促进未来的架构和系统研究。最后，我们通过两个具体案例研究展示了这种内存层次范式转换所带来的软件系统设计空间。总体而言，我们将经典启发式规则转化为一个可操作的、考虑可行性的分析和配置框架，为AI时代内存层次结构的进一步研究奠定了基础。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2D](index.md) · [返回 ISCA 2026](../index.md)
