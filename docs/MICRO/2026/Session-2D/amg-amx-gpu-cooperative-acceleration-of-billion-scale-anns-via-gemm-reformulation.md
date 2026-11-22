---
title: "AMG: AMX-GPU Cooperative Acceleration of Billion-Scale ANNS via GEMM Reformulation"
description: "MICRO 2026 · Session 2D · AMG：通过 GEMM 重构实现十亿规模近似最近邻搜索的 AMX-GPU 协同加速"
tags:
  - "MICRO2026"
  - "GPU"
---

# AMG: AMX-GPU Cooperative Acceleration of Billion-Scale ANNS via GEMM Reformulation

**中文标题：** AMG：通过 GEMM 重构实现十亿规模近似最近邻搜索的 AMX-GPU 协同加速

**所属 Session：** [Session 2D](index.md) · [MICRO 2026](../index.md)

**作者：** Minho Kim, Houxiang Ji, Hwanjun Lee, Jaeyoung Kang, Sungju Kim, Hyunkyun Shin, Daehoon Kim, Nam Sung Kim

**来源：** MICRO 2026，pp. 787–802；[DOI](https://doi.org/10.1109/MICRO67795.2026.00066)

## 英文摘要

Billion-scale Approximate Nearest Neighbor Search (ANNS) is a core bottleneck in modern Retrieval-Augmented Generation (RAG) systems, yet existing GPU-centric designs remain fundamentally constrained by GPU memory capacity and PCIe bandwidth: over 80% of end-to-end query latency is spent on host–device transfers rather than computation. Meanwhile, emerging on-chip matrix engines such as Intel's Advanced Matrix Extensions (AMX) offer substantial compute density, enabling CPU participation to alleviate the PCIe bottleneck. However, they have seen limited success in ANNS due to the dominance of memory-bound GEMV operations, which limit effective utilization of such compute units. This paper presents AMG, to the best of our knowledge, the first framework that makes AMX genuinely useful for ANNS acceleration and effectively alleviates the PCIe bottleneck of single-GPU systems. AMG introduces query grouping, a key algorithmic reformulation that converts fragmented per-query GEMVs into large, compute-bound GEMMs, enabling both AMX and GPUs to operate at high utilization, while substantially reducing data transfer volume by offloading a portion of computation to AMX. AMG further performs shape-aware heterogeneous scheduling, GPU pipelining, and GPU-resident cluster caching, achieving fine-grained AMX–GPU cooperation with minimal runtime overhead. Evaluations on billion-scale datasets show that AMG achieves 2.1–8.8× higher throughput than the state-of-the-art single-GPU design and up to 26.6× over a GEMV-based CPU-only baseline, while preserving high recall rates.

## 中文摘要

数十亿级的近似最近邻搜索 (ANNS) 是现代检索增强生成 (RAG) 系统的核心瓶颈，但现有的以 GPU 为中心的设计仍然从根本上受到 GPU 内存容量和 PCIe 带宽的限制：超过 80% 的端到端查询时延花费在主机设备传输上，而不是计算上。与此同时，新兴的片上矩阵引擎（例如英特尔的高级矩阵扩展 (AMX)）提供了巨大的计算密度，使 CPU 参与能够缓解 PCIe 瓶颈。然而，由于内存限制的 GEMV 操作占主导地位，限制了此类计算单元的有效利用，他们在 ANNS 中取得的成功有限。据我们所知，本文介绍了 AMG，这是第一个使 AMX 真正可用于 ANNS 加速并有效缓解单 GPU 系统的 PCIe 瓶颈的框架。 AMG 引入了查询分组，这是一种关键的算法重构，可将碎片化的每个查询 GEMV 转换为大型计算密集型 GEMM，使 AMX 和 GPU 能够以高利用率运行，同时通过将部分计算卸载到 AMX 来大幅减少数据传输量。 AMG 进一步执行形状感知异构调度、GPU 流水线和 GPU 驻留集群缓存，以最小的运行时开销实现细粒度的 AMX-GPU 协作。对十亿级数据集的评估表明，AMG 的吞吐量比最先进的单 GPU 设计高出 2.1–8.8 倍，比基于 GEMV 的纯 CPU 基线高出 26.6 倍，同时保持高召回率。

## 中文关键词

近似最近邻搜索；异构计算；片上加速器；AMX；矩阵乘法

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/minlno/MICRO-2026-AMG](https://github.com/minlno/MICRO-2026-AMG)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21523619](https://doi.org/10.5281/zenodo.21523619)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2D](index.md) · [MICRO 2026 主页](../index.md)
