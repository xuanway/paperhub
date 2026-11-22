---
title: "FUSE: A Fragmentation-Free Spatial Multi-Tenant DNN Accelerator via Edge-Universal Graph"
description: "MICRO 2026 · Session 1D · FUSE：通过边通用图实现无碎片的空间多租户 DNN 加速器"
tags:
  - "MICRO2026"
  - "Graph Processing"
  - "Neural Networks"
---

# FUSE: A Fragmentation-Free Spatial Multi-Tenant DNN Accelerator via Edge-Universal Graph

**中文标题：** FUSE：通过边通用图实现无碎片的空间多租户 DNN 加速器

**所属 Session：** [Session 1D](index.md) · [MICRO 2026](../index.md)

**作者：** Zhihao Yang, Yongwei Zhao, Tianrui Ma, Yifan Hao, Zhe Fan, Rui Zhang, Zidong Du, Ling Li, Tianshi Chen, Yunji Chen

**来源：** MICRO 2026，pp. 359–373；[DOI](https://doi.org/10.1109/MICRO67795.2026.00040)

## 英文摘要

Multi-tenancy is critical for meeting the latency requirements of DNN models concurrently executing on a shared accelerator while improving hardware utilization. Existing accelerators achieve spatial multi-tenancy by dynamically co-locating tasks across tiles. However, to limit hardware cost, such co-location typically relies on constrained interconnects. As a result, data forwarding between some tiles can block forwarding between others, leaving many tiles underutilized_i.e., fragmentation. In this paper, we propose FUSE, a fragmentation-free spatial multi-tenant DNN accelerator that supports universal, non-blocking tile-to-tile data forwarding at negligible area overhead. Our key insight is that inter-tile data forwarding patterns are naturally acyclic, and can be modeled as Directed Acyclic Graphs (DAGs) instead of dense, bidirectional interconnects in conventional designs. Therefore, the data forwarding network can be built upon Valiant's Edge-Universal Graph (EUG), a graph construction that efficiently supports DAG embeddings. However, direct hardware implementation of EUG has historically been impractical due to its unbounded critical-path delays. We address this issue with a novel Temporal-Zone Timing method that bounds critical paths while preserving functional correctness. Built on this foundation, FUSE achieves efficient, fragmentation-free multi-tenancy. Post-layout evaluation shows that FUSE improves Quality-of-Service by 1.38x, throughput by 1.11x, and lowers area overhead from 19.33% to 6.44%, compared to the state-of-the-art accelerators.

## 中文摘要

多租户对于满足在共享加速器上同时执行的 DNN 模型的时延要求并同时提高硬件利用率至关重要。现有的加速器通过跨分块动态地共同定位任务来实现空间多租户。然而，为了限制硬件成本，这种共置通常依赖于受限的互连。结果，一些分块之间的数据转发可能会阻止其他分块之间的转发，从而导致许多分块未得到充分利用，即碎片。在本文中，我们提出了 FUSE，一种无碎片空间多租户 DNN 加速器，支持通用、非阻塞的分块到分块数据转发，且区域开销可以忽略不计。我们的主要见解是，分块间数据转发模式本质上是非循环的，并且可以建模为有向非循环图（DAG），而不是传统设计中的密集双向互连。因此，数据转发网络可以建立在 Valiant 的边缘通用图（EUG）之上，这是一种有效支持 DAG 嵌入的图结构。然而，由于其无限的关键路径时延，EUG 的直接硬件实施历来是不切实际的。我们通过一种新颖的时序区域定时方法来解决这个问题，该方法限制关键路径，同时保持功能正确性。在此基础上，FUSE 实现了高效、无碎片的多租户。布局后评估表明，与最先进的加速器相比，FUSE 将服务质量提高了 1.38 倍，吞吐量提高了 1.11 倍，并将面积开销从 19.33% 降低到 6.44%。

## 中文关键词

空间 DNN 任务共置；多租户深度神经网络加速；资源碎片；图映射

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1D](index.md) · [MICRO 2026 主页](../index.md)
