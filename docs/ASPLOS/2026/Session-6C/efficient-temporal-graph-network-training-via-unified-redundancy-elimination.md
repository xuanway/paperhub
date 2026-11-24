---
title: "Efficient Temporal Graph Network Training via Unified Redundancy Elimination"
description: "ASPLOS 2026 · Session 6C · 通过统一冗余消除实现高效的时序图网络训练"
tags:
  - "ASPLOS2026"
  - "Session 6C"
  - "Graph & Sparse Computing"
---

# Efficient Temporal Graph Network Training via Unified Redundancy Elimination

**中文标题：** 通过统一冗余消除实现高效的时序图网络训练

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yiqing Wang (Beihang University), Hailong Yang (Beihang University), Kejie Ma (Beihang University), Enze Yu (Beihang University), Pengbo Wang (Beihang University), Xin You (Beihang University), Qingxiao Sun (Beihang University), Chenhao Xie (Beihang University), Zhongzhi Luan (Beihang University), Yi Liu (Beihang University), Depei Qian (Beihang University)

**单位：** Beihang University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790157) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Temporal Graph Network (TGN) is increasingly adopted to model evolving relationships in dynamic graphs. However, the training pipeline is plagued by pervasive redundancy in computation, storage, and data loading. These redundancies harm computational efficiency, exacerbate memory pressure, and induce excessive CPU-GPU data transfers. We present PULSE, an end-to-end TGN training framework that systematically eliminates redundancies guided by a unified minimal-unit principle. To realize such principle, PULSE defines three synergetic units: 1) the Minimal Input Unit (MIU) for component-wise deduplication and operator-level reconstruction of redundant computations, 2) the Minimal Storage Unit (MSU) for dependency-guided message reconstruction, only preserving irreproducible entries while enabling on-demand recovery of others, and 3) the Minimal Reuse Unit (MRU) for GPU memory management, combining a BlockPool-based buffer allocator with a bipartite temporal Experimental results on representative benchmarks demonstrate that PULSE improves training throughput by up to 6.67× over the state-of-the-art baselines.

## 中文摘要

时序图网络（TGN）正日益被用于建模动态图中不断演化的关系。然而，其训练流水线受到计算、存储和数据加载中普遍存在的冗余的困扰。这些冗余损害了计算效率、加剧了内存压力，并导致过多的 CPU-GPU 数据传输。我们提出 PULSE，一个端到端的 TGN 训练框架，它在统一的最小单元原则指导下系统性地消除冗余。为实现该原则，PULSE 定义了三个协同单元：1）最小输入单元（MIU），用于按分量去重以及对冗余计算进行算子级重构；2）最小存储单元（MSU），用于依赖引导的消息重构，仅保留不可复现的条目，同时支持其余条目的按需恢复；3）最小复用单元（MRU），用于 GPU 内存管理，将基于 BlockPool 的缓冲区分配器与二分时序（bipartite temporal）相结合。在代表性基准上的实验结果表明，PULSE 相比最先进的基线最高可将训练吞吐量提升 6.67×。

## 英文关键词

Temporal Graph Networks, Training System, Unified Redundancy Elimination

## 中文关键词

时序图网络；训练系统；统一冗余消除

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790157)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6C](index.md) · [返回 ASPLOS 2026](../index.md)
