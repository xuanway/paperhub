---
title: "Rethinking Compression for CXL Memory Expanders at Hyperscale"
description: "MICRO 2026 · Session 5C · 重新思考超大规模场景中 CXL 内存扩展器的压缩技术"
tags:
  - "MICRO2026"
  - "CXL"
---

# Rethinking Compression for CXL Memory Expanders at Hyperscale

**中文标题：** 重新思考超大规模场景中 CXL 内存扩展器的压缩技术

**所属 Session：** [Session 5C](index.md) · [MICRO 2026](../index.md)

**作者：** Haneul Park, Grant Ayers, Nam Sung Kim, Philip Levis, Brian Morris

**来源：** MICRO 2026，pp. 1731–1745；[DOI](https://doi.org/10.1109/MICRO67795.2026.00124)

## 英文摘要

DRAM dominates the cost of datacenter servers, and recent AI-driven memory supply shortages are pushing costs even higher. OCP CXL memory expanders address this challenge by attaching legacy DRAM as a slower capacity tier and increasing effective capacity through hardware compression. This paper explores two critical design points of a memory expander: the compression algorithm and the block size. Using cold memory traces measured in a hyperscaler fleet, we show that a more complex algorithm (Zstd) increases effective capacity by 30% while simultaneously reducing access latency by 12% compared to LZ4. This overturns the conventional assumption that memory compression should favor simple algorithms to minimize decompression latency. More complex compression reduces DRAM traffic, which more than offsets the higher decompression time. We find that benchmarks widely used in tiered memory research exhibit fundamentally different locality from production cold memory, leading to potentially misleading design conclusions. To bridge this gap, we propose COLA, a parameterized model of COld memory LocAlity with an integrated trace generator that enables systematic exploration of diverse access patterns. The performance improvements hold across a wide range of access traces, suggesting that next-generation expanders should adopt different algorithms and block sizes. COLA is open-sourced at https://github.com/google-systems-research/cold-memory-model.

## 中文摘要

DRAM 在数据中心服务器的成本中占据主导地位，而最近人工智能驱动的内存供应短缺正在推高成本。 OCP CXL 内存扩展器通过将传统 DRAM 作为较慢的容量层附加并通过硬件压缩增加有效容量来解决这一挑战。本文探讨了内存扩展器的两个关键设计点：压缩算法和块大小。使用在超大规模集群中测量的冷内存跟踪，我们发现与 LZ4 相比，更复杂的算法 (Zstd) 将有效容量提高了 30%，同时将访问时延降低了 12%。这颠覆了内存压缩应该支持简单算法以最小化解压缩时延的传统假设。更复杂的压缩会减少 DRAM 流量，这足以抵消更长的解压缩时间。我们发现，分层内存研究中广泛使用的基准测试与生产冷内存表现出根本不同的局部性，从而导致潜在的误导性设计结论。为了弥补这一差距，我们提出了 COLA，这是一种 COld 内存局部性的参数化模型，具有集成的跟踪生成器，可以系统地探索不同的访问模式。性能改进适用于广泛的访问轨迹，这表明下一代扩展器应采用不同的算法和块大小。 COLA 在 https://github.com/google-systems-research/cold-memory-model 上开源。

## 中文关键词

分层内存；CXL；压缩；超大规模数据中心

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.22137537](https://doi.org/10.5281/zenodo.22137537)
- 代码仓库：[https://github.com/google-systems-research/cold-memory-model](https://github.com/google-systems-research/cold-memory-model)

以上入口来自论文正文或 Artifact 附录。

## 来源核对说明

公开内容包括 COLA、参数、生成轨迹和分析脚本；原始 Google 生产轨迹不公开。

[返回 Session 5C](index.md) · [MICRO 2026 主页](../index.md)
