---
title: "Arborist: Algorithm-Hardware Co-Design for Fast and Efficient Motion Planning"
description: "MICRO 2026 · Session 2D · Arborist：面向快速高效运动规划的算法与硬件协同设计"
tags:
  - "MICRO2026"
  - "HW-SW Co-design"
---

# Arborist: Algorithm-Hardware Co-Design for Fast and Efficient Motion Planning

**中文标题：** Arborist：面向快速高效运动规划的算法与硬件协同设计

**所属 Session：** [Session 2D](index.md) · [MICRO 2026](../index.md)

**作者：** Yaotian Liu, Lingyi Huang, Zishen Wan, Bo Yuan, Cheng Tan, Jeff Jun Zhang

**来源：** MICRO 2026，pp. 818–833；[DOI](https://doi.org/10.1109/MICRO67795.2026.00068)

## 英文摘要

Real-time motion planning must execute under strict latency and energy constraints on resource-limited platforms. This paper presents Arborist, an algorithm-hardware co-design framework that accelerates Fast Marching Tree (FMT*) motion planning through synergistic algorithmic and architectural innovations. At the algorithm level, Arborist introduces safe multi-tree expansion with global competition management and cross-tree optimality checking to expose inter-tree parallelism while preserving path quality. At the architecture level, our proposed ArboristAccel integrates an Arborist Toolbox that provides hardware support for inter-tree parallelism; a KD-tree Subsystem for high-throughput near-neighbor search; a Parallel-Query Retrieval module that balances multi-bank memory accesses to alleviate system-level memory bandwidth bottlenecks; and a Look-ahead Planning Engine that exploits intra-tree parallelism while preserving path quality by in-order commit. Synthesized in 16 nm and operating at 500 MHz, ArboristAccel sustains more than 1000x speedup over CPU across all workloads, peaking at 2800x on 2D-Maze, and delivers geomean improvements of 8.8x speedup, 4.6x area efficiency, and 3.1x power efficiency over an FMT* ASIC baseline. The corresponding factors relative to a state-of-the-art RRT*-based MOPED accelerator are 8.6x, 1.0x, and 1.8x, at comparable path cost. To the best of our knowledge, ArboristAccel is the first dedicated hardware accelerator for FMT*-based motion planning.

## 中文摘要

实时运动规划必须在资源有限的平台上在严格的时延和能量限制下执行。本文介绍了 Arborist，这是一种算法-硬件协同设计框架，可通过协同算法和架构创新来加速快速行进树 (FMT*) 运动规划。在算法层面，Arborist 引入了具有全局竞争管理和跨树最优性检查的安全多树扩展，以暴露树间并行性，同时保持路径质量。在架构层面，我们提出的 ArboristAccel 集成了 Arborist Toolbox，为树间并行性提供硬件支持；用于高吞吐量近邻搜索的 KD 树子系统；并行查询检索模块，平衡多组内存访问以缓解系统级内存带宽瓶颈；前瞻规划引擎利用树内并行性，同时通过按序提交保持路径质量。 ArboristAccel 采用 16 nm 工艺合成，运行频率为 500 MHz，在所有工作负载中均能保持超过 CPU 1000 倍的加速，在 2D-Maze 上峰值达到 2800 倍，并且与 FMT* ASIC 基准相比，几何平均改进为 8.8 倍加速、4.6 倍面积效率和 3.1 倍功率效率。在路径成本相当的情况下，相对于最先进的基于 RRT* 的 MOPED 加速器的相应因子为 8.6 倍、1.0 倍和 1.8 倍。据我们所知，ArboristAccel 是首款用于基于 FMT* 的运动规划的专用硬件加速器。

## 中文关键词

运动规划；硬件加速；算法与硬件协同设计；快速行进树；专用架构

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.22313402](https://doi.org/10.5281/zenodo.22313402)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2D](index.md) · [MICRO 2026 主页](../index.md)
