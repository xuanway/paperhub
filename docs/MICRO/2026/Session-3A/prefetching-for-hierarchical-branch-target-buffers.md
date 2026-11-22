---
title: "Prefetching for Hierarchical Branch Target Buffers"
description: "MICRO 2026 · Session 3A · 面向分层分支目标缓冲区的预取"
tags:
  - "MICRO2026"
  - "Prefetching"
---

# Prefetching for Hierarchical Branch Target Buffers

**中文标题：** 面向分层分支目标缓冲区的预取

**所属 Session：** [Session 3A](index.md) · [MICRO 2026](../index.md)

**作者：** Yongjie Huang, Mária Ďuračková, Boris Grot, David Schall

**来源：** MICRO 2026，pp. 895–910；[DOI](https://doi.org/10.1109/MICRO67795.2026.00073)

## 英文摘要

High-performance CPUs rely on hierarchical branch prediction units (BPUs) to balance the large branch working sets of contemporary workloads against the single-cycle latency required to sustain high fetch throughput. Prior work has overlooked the importance of small, latency-critical L1-BTB and conditional predictor structures, leaving this aspect of microarchitecture unexplored. This paper presents a comprehensive characterization of hierarchical BPUs with an emphasis on L1 structures. We find that, relative to an ideal single-cycle BPU, an iso-capacity hierarchical BPU diminishes performance because the latency of L1 misses is often exposed to the fetch pipeline. L1-BTB misses are primarily responsible for performance degradation, even though nearly all branch targets are found in the L2-BTB. Our analysis reveals that L1-BTB misses commonly occur in back-to-back miss chains associated with transitions to new code regions. Branches immediately preceding such chains are often loop exits and function calls/returns, suggesting that inter-region control-flow transitions are a key source of exposed front-end latency. Motivated by this observation, we propose BTB-Ferret, a metadata-free prefetcher for the L1-BTB that exploits existing BTB metadata to avoid storage overheads. BTB-Ferret identifies conditional branches with bidirectional behaviour and function calls, and prefetches BTB entries from the L2-BTB along the alternate path to the predicted one, thereby anticipating upcoming branches. Given a 128-entry L1-BTB, BTB-Ferret covers 37.3% on average (51.9% max) of L1-BTB misses and improves performance by 1.7% on average (9.7% max) while enjoying a simple and low-cost design.

## 中文摘要

高性能 CPU 依靠分层分支预测单元 (BPU) 来平衡当代工作负载的大型分支工作集与维持高获取吞吐量所需的单周期时延。先前的工作忽略了小型、时延关键的 L1-BTB 和条件预测器结构的重要性，使得微架构的这一方面未被探索。本文对分层 BPU 进行了全面的表征，重点是 L1 结构。我们发现，相对于理想的单周期 BPU，等容量分层 BPU 会降低性能，因为 L1 未命中的时延经常暴露在获取管道中。尽管几乎所有分支目标都在 L2-BTB 中找到，但 L1-BTB 未命中是性能下降的主要原因。我们的分析表明，L1-BTB 缺失通常发生在与新代码区域转换相关的连续缺失链中。紧邻此类链之前的分支通常是循环退出和函数调用/返回，这表明区域间控制流转换是暴露的前端时延的关键来源。受这一观察的启发，我们提出了 BTB-Ferret，这是一种用于 L1-BTB 的无元数据预取器，它利用现有的 BTB 元数据来避免存储开销。 BTB-Ferret 识别具有双向行为和函数调用的条件分支，并沿着备用路径从 L2-BTB 预取 BTB 条目到预测条目，从而预测即将到来的分支。考虑到 128 个条目的 L1-BTB，BTB-Ferret 平均覆盖 37.3%（最大 51.9%）的 L1-BTB 未命中率，平均性能提高 1.7%（最大 9.7%），同时享受简单且低成本的设计。

## 中文关键词

分支目标缓冲区；分支预测；CPU 微架构；层次化预取

## 代码与研究制品

- 代码仓库：[https://github.com/yongjiehuang/BTB-Ferret](https://github.com/yongjiehuang/BTB-Ferret)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21478670](https://doi.org/10.5281/zenodo.21478670)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3A](index.md) · [MICRO 2026 主页](../index.md)
