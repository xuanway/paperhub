---
title: "Affinity-based Optimizations for TFHE on Processing-in-DRAM"
description: "ASPLOS 2025 · Session 1D · 面向 DRAM 内计算的 TFHE 亲和性优化"
tags:
  - "ASPLOS2025"
  - "Session 1D"
  - "Homomorphic Encryption"
---

# Affinity-based Optimizations for TFHE on Processing-in-DRAM

**中文标题：** 面向 DRAM 内计算的 TFHE 亲和性优化

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Kevin Nam (Department of Electrical and Computer Engineering (ECE), Seoul National University,Inter-university Semiconductor Research Center (ISRC), Seoul National University), Heonhui Jung (Department of Electrical and Computer Engineering (ECE), Seoul National University,Inter-university Semiconductor Research Center (ISRC), Seoul National University), Hyunyoung Oh (Department of AI·Software, Gachon University), Yunheung Paek (Department of Electrical and Computer Engineering (ECE), Seoul National University,Inter-university Semiconductor Research Center (ISRC), Seoul National University)

**单位：** ECE；ISRC；Department of AI·Software, Gachon University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716246) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Processing-in-memory (PIM) architectures are promising for accelerating intensive workloads due to their high internal bandwidth. This paper introduces a technique for accelerating Fully Homomorphic Encryption over the Torus (TFHE), a promising yet intensive application, on a realistic PIM system. Existing TFHE accelerators focus on exploiting parallelism, often overlooking data affinity, which leads to performance degradation in PIM due to excessive remote data accesses (RDAs). To address this, we present an affinity-based approach that optimizes the computation of TFHE on PIM. We apply algorithmic optimizations to TFHE, enabling PIM to effectively leverage its high internal bandwidth. We analyze the affinity patterns in the sub-tasks of TFHE and develop an offline scheduler that exploits our analysis to find optimal scheduling, minimizing RDAs while maintaining sufficient parallelism. To demonstrate the practicality of our work, we design a variant of an existing PIM-HBM device with minimal hardware modifications, and perform evaluations over a real FPGA-based PIM system. Our experiments demonstrate that our affinity-based optimizations outperform prior TFHE accelerators by 4.24-209× for real-world benchmarks.

## 中文摘要

内存内计算（PIM）架构凭借其高内部带宽，在加速计算密集型负载方面颇具前景。本文提出一种在真实 PIM 系统上加速环上全同态加密（TFHE）的技术，TFHE 是一种颇具前景但计算密集的应用。现有的 TFHE 加速器侧重于发掘并行性，往往忽视了数据亲和性，这在 PIM 中会因过多的远程数据访问（RDA）而导致性能下降。为解决这一问题，我们提出一种基于亲和性的方法，用于优化 TFHE 在 PIM 上的计算。我们对 TFHE 施加算法级优化，使 PIM 能够有效利用其高内部带宽。我们分析了 TFHE 各子任务中的亲和性模式，并开发了一个离线调度器，利用我们的分析结果寻找最优调度，在保持足够并行性的同时最小化 RDA。为证明本工作的实用性，我们设计了一种仅需极少硬件改动的现有 PIM-HBM 器件变体，并在真实的基于 FPGA 的 PIM 系统上进行了评估。实验表明，对于真实世界基准测试，我们基于亲和性的优化相比先前的 TFHE 加速器实现了 4.24–209× 的性能提升。

## 英文关键词

Homomorphic Encryption; TFHE; PIM

## 中文关键词

同态加密；TFHE；PIM

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716246)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2025](../index.md)
