---
title: "DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization"
description: "MICRO 2026 · Session 2D · DeGS：通过解耦工作负载解析与重组实现可扩展三维高斯泼溅架构"
tags:
  - "MICRO2026"
---

# DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization

**中文标题：** DeGS：通过解耦工作负载解析与重组实现可扩展三维高斯泼溅架构

**所属 Session：** [Session 2D](index.md) · [MICRO 2026](../index.md)

**作者：** Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng

**来源：** MICRO 2026，pp. 848–862；[DOI](https://doi.org/10.1109/MICRO67795.2026.00070)

## 英文摘要

3D Gaussian Splatting (3DGS) has emerged as a leading technique for real-time novel view synthesis, yet existing 3DGS accelerators suffer from poor architectural scalability: increasing the number of PEs leads to marginal performance improvement during rendering. We identify that the root cause is the tightly coupled "checking-while-blending" dataflow, which exacerbates PE underutilization caused by spatial redundancy from irregular Gaussian coverage and temporal redundancy from asynchronous pixel-wise termination under parallel execution. To address this issue, we propose DeGS, a scalable architecture for efficient 3DGS inference. To systematically eliminate the redundancies inherent in rendering, DeGS exploits a decoupled dataflow, restructuring the coupled alpha-checking, transmittance checking, and alpha-blending of the standard rendering process into consecutive workload parsing, reorganization, and blending stages. This allows the fragmented, length-variable, and temporal-dependent workloads to be reorganized into compact, conflict-free, and dense workloads prior to blending, thereby significantly improving PE utilization during parallel blending. Implemented in 28 nm technology, DeGS achieves 2.36x-7.25x throughput, 1.82x-6.02x end-to-end speedup, and 1.59x-4.42x energy efficiency over state-of-the-art 3DGS accelerators (GSCore, GBU, GCC) across diverse scenes and resolutions (720p to 8K). Moreover, scaling from 16 to 1024 PEs, DeGS maintains over 80 percent PE utilization at high resolutions, significantly outperforming existing accelerators.

## 中文摘要

3D 高斯分布 (3DGS) 已成为实时新颖视图合成的领先技术，但现有 3DGS 加速器的架构可扩展性较差：增加 PE 数量会导致渲染过程中的边际性能提升。我们发现根本原因是紧密耦合的“混合时检查”数据流，这加剧了由于不规则高斯覆盖的空间冗余和并行执行下异步逐像素终止的时间冗余而导致的 PE 利用率不足。为了解决这个问题，我们提出了 DeGS，一种用于高效 3DGS 推理的可扩展架构。为了系统地消除渲染中固有的冗余，DeGS 利用解耦的数据流，将标准渲染过程的耦合 alpha 检查、透射率检查和 alpha 混合重组为连续的工作负载解析、重组和混合阶段。这允许在混合之前将碎片化、长度可变和时间相关的工作负载重新组织为紧凑、无冲突和密集的工作负载，从而显着提高并行混合期间的 PE 利用率。 DeGS 采用 28 nm 技术实现，在不同场景和分辨率（720p 至 8K）下，与最先进的 3DGS 加速器（GSCore、GBU、GCC）相比，吞吐量提高了 2.36x-7.25 倍，端到端加速提高了 1.82x-6.02 倍，能效提高了 1.59x-4.42 倍。此外，从 16 个 PE 扩展到 1024 个 PE 后，DeGS 在高分辨率下仍保持超过 80% 的 PE 利用率，显着优于现有加速器。

## 中文关键词

三维高斯泼溅；神经渲染；领域专用加速器；可扩展架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 2D](index.md) · [MICRO 2026 主页](../index.md)
