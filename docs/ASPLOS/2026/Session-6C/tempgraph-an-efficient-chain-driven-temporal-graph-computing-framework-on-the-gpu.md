---
title: "TempGraph: An Efficient Chain-driven Temporal Graph Computing Framework on the GPU"
description: "ASPLOS 2026 · Session 6C · TempGraph：一种高效的基于 GPU 的链驱动时序图计算框架"
tags:
  - "ASPLOS2026"
  - "Session 6C"
  - "Graph & Sparse Computing"
---

# TempGraph: An Efficient Chain-driven Temporal Graph Computing Framework on the GPU

**中文标题：** TempGraph：一种高效的基于 GPU 的链驱动时序图计算框架

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jin Zhao (Huazhong University of Science and Technology), Qian Wang (Huazhong University of Science and Technology), Ligang He (University of Warwick), Yu Zhang (Huazhong University of Science and Technology), Sheng Di (Argonne National Laboratory), Bingsheng He (National University of Singapore), Xinlei Wang (Huazhong University of Science and Technology), Hui Yu (Huazhong University of Science and Technology), Hao Qi (Huazhong University of Science and Technology), Longlong Lin (Southwest University), Linchen Yu (Huazhong University of Science and Technology), Xiaofei Liao (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology)

**单位：** Huazhong University of Science and Technology；University of Warwick；Argonne National Laboratory；National University of Singapore；Southwest University

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736116) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Tackling temporal path problems in temporal graphs is essential for time-sensitive applications. Although many solutions have been proposed to handle temporal path problems, due to the intrinsic time constraints, these solutions require the vertices of the temporal graph to be sequentially handled along the time-dependent chains (i.e., the temporal dependencies between these vertices) to form the temporal path. This sequential temporal nature poses the challenges of poor parallelism and slow convergence speed, preventing existing solutions from fully leveraging the massive parallelism and high internal bandwidth of GPU to handle temporal path problems. To overcome these challenges, this paper proposes TempGraph, an efficient chain-driven GPU-based temporal graph computing framework. Specifically, it transforms the temporal graph into a set of disjoint time-dependent chains that can elegantly expose the temporal dependency between the vertices while facilitating the fast path exploration along these chains over GPU. Furthermore, TempGraph employs a novel Generate-Activate-Compute execution model to decouple the temporal dependency between different chains through maintaining a set of shortcuts for them, which enables multiple chains to be concurrently handled by massive GPU threads, achieving fast convergence speed and high parallelism on the GPU. Experiments on an A100 GPU show that TempGraph outperforms the state-of-the-art GPU-based solutions by 3.0-16.2×. Besides, TempGraph on an A100 GPU gains 33.9-368.9× speedups compared to the cutting-edge CPU-based system TeGraph on a 128-core CPU machine.

## 中文摘要

解决时序图中的时序路径问题对时间敏感型应用至关重要。尽管已有许多方案被提出用于处理时序路径问题，但由于内在的时间约束，这些方案要求时序图的顶点沿时间相关链（即这些顶点之间的时序依赖关系）被顺序处理，以形成时序路径。这种顺序时序特性带来了并行性差与收敛速度慢的挑战，使现有方案无法充分利用 GPU 的大规模并行性与高内部带宽来处理时序路径问题。为克服这些挑战，本文提出 TempGraph，一种高效的、链驱动的、基于 GPU 的时序图计算框架。具体而言，它将时序图转换为一组互不相交的时间相关链，这些链能够优雅地揭示顶点之间的时序依赖关系，同时便于在 GPU 上沿这些链进行快速的路径探索。此外，TempGraph 采用一种新颖的 Generate-Activate-Compute 执行模型，通过为不同的链维护一组快捷方式（shortcut）来解耦不同链之间的时序依赖，使多条链能够被大量 GPU 线程并发处理，从而在 GPU 上实现快速的收敛速度与高并行性。在 A100 GPU 上的实验表明，TempGraph 相比最先进的基于 GPU 的方案取得 3.0-16.2× 的性能提升。此外，在 A100 GPU 上的 TempGraph 相比在 128 核 CPU 机器上运行的前沿基于 CPU 的系统 TeGraph，取得 33.9-368.9× 的加速。

## 英文关键词

Temporal graph computing; GPU; Data parallelism; Convergence speed

## 中文关键词

时序图计算；GPU；数据并行；收敛速度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736116)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 6C](index.md) · [返回 ASPLOS 2026](../index.md)
