---
title: "GRAINS: Enabling High-Performance and Low-Cost Graph-Based Genome Analysis via Storage-Aware Algorithm-Architecture Co-Design"
description: "ISCA 2026 · Session 4C · GRAINS: Enabling High-Performance and Low-Cost Graph-Based Genome Analysis via Storage-Aware Algorithm-Architecture Co-Design"
tags:
  - "ISCA2026"
  - "Session 4C"
  - "Domain Specific Accelerators 1"
---

# GRAINS: Enabling High-Performance and Low-Cost Graph-Based Genome Analysis via Storage-Aware Algorithm-Architecture Co-Design

**中文标题：** GRAINS: 通过存储感知的算法-架构协同设计实现高性能低成本图基因组分析

**所属 Session：** [Session 4C](index.md) · [ISCA 2026](../index.md)

**作者：** Nika Mansouri Ghiasi, Harun Mustafa, Talu Güloglu, Rakesh Nadig, Konstantina Koliogeorgi, Susana Rebolledo Ruiz, Marc Rautmann, Furkan Eris, Mohammad Sadrosadati, Jisung Park, Onur Mutlu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Graph-based representations of genome sequences have emerged as a powerful approach for representing massive genomic databases in an expressive and efficient way. Compared to traditional, linear genome sequences, genome graphs enable more accurate and efficient genome analyses, particularly in complex, population-scale settings (e.g., public health, precision medicine, and agriculture). Despite their benefits, analysis on large-scale genome graphs incurs significant data movement overhead from the storage system due to accessing large amounts of low-reuse data. Processing data directly inside the storage device, where data originally resides, can be a fundamental solution for mitigating this overhead. However, none of the existing tools for graph-based genome analysis can be efficiently used inside the storage system due to the limited internal hardware resources in modern SSDs. At the same time, prior storage-centric systems developed for (i) traditional, linear non-graph-based genome analysis or (ii) conventional, non-genomic graph analysis are not suitable for the unique data structures and access patterns of graph-based genome analysis. We propose GRAINS, the first system for analysis with large-scale genome graphs in storage. Through our detailed examination of typical analysis pipelines that operate on genome graphs, we perform storage-aware algorithm-architecture co-design to (i) make the graph-based genome analysis pipelines more storage-friendly and (ii) further improve performance, energy-efficiency, and cost via in-storage and in-flash processing. GRAINS’s co-design is based on three key aspects. First, we propose a new batching technique and execution flow, based on unique features of genome graphs, that reduces the number of random accesses to graph nodes. Second, via in-flash and in-storage processing, we avoid transferring low-reuse or unused flash pages, preventing SSD channel and external I/O bandwidth waste. Third, to leverage the full parallelism of flash dies during in-flash processing, we design an effective, yet lightweight, scheduling technique, enabled by re-purposing the existing SSD structures. GRAINS’s design is versatile and flexible as it supports key operations on genome graphs and can be integrated in various analysis pipelines. GRAINS provides 2.7×–47.8× speedup (4.4×–31.6× energy reduction) over the state-of-the-art software baselines, and 1.5×–17.0× speedup (3.1×–20.7× energy reduction) over a hardware-accelerated baseline.


## 中文摘要

基于图表示的基因组序列已成为以富有表现力且高效的方式表示大规模基因组数据库的有力方法。与传统线性基因组序列相比，基因组图能够实现更准确、更高效的基因组分析，尤其是在复杂的群体规模场景中（例如公共卫生、精准医疗和农业）。尽管具有这些优势，大规模基因组图上的分析会产生显著的存储系统数据搬移开销，因为需要访问大量低复用数据。直接在数据原始所在的存储设备内部处理数据，可以是缓解该开销的根本性解决方案。然而，由于现代 SSD 内部硬件资源有限，现有图基因组分析工具都无法在存储系统内高效使用。同时，此前为 (i) 传统线性非图基因组分析或 (ii) 常规非基因组图分析开发的以存储为中心的系统，并不适合图基因组分析特有的数据结构和访问模式。我们提出 GRAINS，这是首个在存储内进行大规模基因组图分析的系统。通过对运行在基因组图上的典型分析流水线进行细致考察，我们开展存储感知的算法-架构协同设计，以 (i) 使图基因组分析流水线更利于存储，并 (ii) 通过存储内与闪存内处理进一步提升性能、能效和成本。GRAINS 的协同设计基于三个关键方面。第一，基于基因组图的独特特性，我们提出一种新的批处理技术和执行流程，减少对图节点的随机访问次数。第二，通过闪存内与存储内处理，我们避免传输低复用或未使用的闪存页，防止 SSD 通道和外部 I/O 带宽浪费。第三，为在闪存内处理期间利用闪存 die 的全部并行性，我们通过复用现有 SSD 结构，设计了一种有效而轻量的调度技术。GRAINS 的设计通用且灵活，因为它支持基因组图上的关键操作，并可集成到各种分析流水线中。相比最先进的软件基线，GRAINS 提供 2.7×–47.8× 加速（能耗降低 4.4×–31.6×）；相比硬件加速基线，提供 1.5×–17.0× 加速（能耗降低 3.1×–20.7×）。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2026](../index.md)
