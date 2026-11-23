---
title: "NMP-PaK: Near-Memory Processing Acceleration of Scalable De Novo Genome Assembly"
description: "ISCA 2025 · Session 9C · NMP-PaK: 近存处理加速可扩展从头基因组装"
tags:
  - "ISCA2025"
  - "Session 9C"
  - "Memory Technology"
---

# NMP-PaK: Near-Memory Processing Acceleration of Scalable De Novo Genome Assembly

**中文标题：** NMP-PaK: 近存处理加速可扩展从头基因组装

**所属 Session：** [Session 9C](index.md) · [ISCA 2025](../index.md)

**作者：** Heewoo Kim, Sanjay Sri Vallabh Singapuram, Haojie Ye, Joseph Izraelevitz, Trevor Mudge, Ronald Dreslinski, Nishil Talati

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731056) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

De novo assembly enables investigations of unknown genomes, paving the way for personalized medicine and disease management. However, it faces immense computational challenges arising from the excessive data volumes and algorithmic complexity. While state-of-the-art de novo assemblers utilize distributed sys- tems for extreme-scale genome assembly, they demand substantial computational and memory resources. They also fail to address the inherent challenges of de novo assembly, including a large mem- ory footprint, memory-bound behavior, and irregular data patterns stemming from complex, interdependent data structures. Given these challenges, de novo assembly merits a custom hardware so- lution, though existing approaches have not fully addressed the limitations. We propose NMP-PaK, a hardware-software co-designed sys- tem that accelerates scalable de novo genome assembly through near-memory processing (NMP). Our channel-level NMP archi- tecture addresses memory bottlenecks while providing sufficient scratchpad space for processing elements. Customized processing elements maximize parallelism while efficiently handling large data structures that are both dynamic and interdependent. Software optimizations include customized batch processing to reduce the memory footprint and hybrid CPU-NMP processing to address hardware underutilization caused by irregular data patterns. NMP-PaK conducts the same genome assembly while incurring a 14×smaller memory footprint compared to the state-of-the-art de novo assembly. Moreover, NMP-PaK delivers 16×and 5.7×per- formance improvements over the CPU and GPU baselines, respec- tively, with a 2.4×reduction in memory operations. Consequently, NMP-PaK achieves 8.3×greater throughput than state-of-the-art de novo assembly under the same resource constraints, showcasing its superior computational efficiency.

## 中文摘要

从头组装技术支持对未知基因组开展研究，为个性化医疗与疾病诊疗奠定基础。但该技术数据体量巨大、算法复杂度高，面临严峻的计算挑战。

当前主流从头组装工具依托分布式系统实现超大规模基因组组装，需要消耗大量算力与内存资源；同时仍无法解决从头组装本身固有的难题：内存占用高、访存受限，以及由复杂且相互依赖的数据结构带来的不规则访存特征。这些问题说明从头组装非常适合定制硬件加速，但现有方案仍存在明显短板。

本文提出NMP-PaK，一套软硬件协同设计的系统，基于近内存处理（NMP）实现可扩展的从头基因组组装加速。该通道级NMP架构缓解内存瓶颈，同时为处理单元提供充足的暂存空间；定制化处理单元充分挖掘并行度，高效处理动态、存在依赖关系的大型数据结构。软件层面优化包含定制批处理策略以降低内存占用，以及CPU-NMP混合处理，解决不规则数据模式造成的硬件利用率偏低问题。

在完成相同基因组组装任务的前提下，NMP-PaK的内存占用相比前沿从头组装工具缩小14倍；相比CPU基线提速16倍，相比GPU基线提速5.7倍，内存操作量减少2.4倍。在同等资源约束下，NMP-PaK的吞吐率达到前沿组装工具的8.3倍，展现出优异的计算效率。

## 英文关键词

De novo genome assembly, Near-memory processing, Hardware-software co-design

## 中文关键词

从头基因组组装, 近内存处理, 软硬件协同设计

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731056)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9C](index.md) · [返回 ISCA 2025](../index.md)
