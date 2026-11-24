---
title: "Parendi: Thousand-Way Parallel RTL Simulation"
description: "ASPLOS 2025 · Session 3D · Parendi：千路并行 RTL 仿真"
tags:
  - "ASPLOS2025"
  - "Session 3D"
  - "EDA"
---

# Parendi: Thousand-Way Parallel RTL Simulation

**中文标题：** Parendi：千路并行 RTL 仿真

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Mahyar Emami (EPFL), Thomas Bourgeat (EPFL), James R. Larus (EPFL)

**单位：** EPFL

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716010) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Hardware development critically depends on cycle-accurate RTL simulation. However, as chip complexity increases, conventional single-threaded simulation becomes impractical due to stagnant single-core performance. Parendi is an RTL simulator that addresses this challenge by exploiting the abundant fine-grained parallelism inherent in RTL simulation and efficiently mapping it onto the massively parallel Graphcore IPU (Intelligence Processing Unit) architecture. Parendi scales up to 5888 cores on 4 Graphcore IPU sockets. It allows us to run large RTL designs up to 4× faster than the most powerful state-of-the-art x64 multicore systems. To achieve this performance, we developed new partitioning and compilation techniques and carefully quantified the synchronization, communication, and computation costs of parallel RTL simulation: The paper comprehensively analyzes these factors and details the strategies that Parendi uses to optimize them.

## 中文摘要

硬件开发严重依赖周期精确的 RTL 仿真。然而，随着芯片复杂度提升，由于单核性能停滞，传统的单线程仿真变得不切实际。Parendi 是一款 RTL 仿真器，它通过利用 RTL 仿真固有的丰富细粒度并行性，并将其高效映射到大规模并行的 Graphcore IPU（Intelligence Processing Unit）架构上来应对这一挑战。Parendi 在 4 个 Graphcore IPU 插槽上可扩展到 5888 个核。它使我们能够以比最强大的先进 x64 多核系统快至多 4 倍的速度运行大型 RTL 设计。为实现这一性能，我们开发了新的划分与编译技术，并仔细量化了并行 RTL 仿真的同步、通信和计算开销：本文全面分析了这些因素，并详述了 Parendi 用于优化这些开销的策略。

## 英文关键词

Bulk-synchronous Parallel, RTL Simulation, Cycleaccurate, Partitioning, Submodular Load Balancing

## 中文关键词

块同步并行；RTL 仿真；周期精确；划分；子模负载均衡

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716010)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2025](../index.md)
