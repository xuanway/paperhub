---
title: "MTIA 300: Meta’s First Training Chip Featuring Built-in NICs and Collective Offloading Engines"
description: "ISCA 2026 · Session 5B · MTIA 300: Meta’s First Training Chip Featuring Built-in NICs and Collective Offloading Engines"
tags:
  - "ISCA2026"
  - "Session 5B"
  - "Industry Track 2"
---

# MTIA 300: Meta’s First Training Chip Featuring Built-in NICs and Collective Offloading Engines

**中文标题：** MTIA 300: Meta 首款内置 NIC 与集合通信卸载引擎的训练芯片

**所属 Session：** [Session 5B](index.md) · [ISCA 2026](../index.md)

**作者：** MTIA Team

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

We present MTIA 300, Meta’s first AI training chip optimized for Deep Learning Recommendation Models (DLRMs). Unlike GenAI training, DLRM training requires modest FLOPS but large memory, high network bandwidth, and frequent collective communication; this combination often leads to low accelerator utilization. MTIA 300 addresses these challenges with three key innovations: (1) built-in NIC chiplets with 12×800 Gbps RDMA NICs to ensure high network performance and eliminate PCIe overhead; (2) dedicated message engines for collective offloading, delivering throughput comparable to compute engines while using only one-third of the chip area; and (3) near-memory compute, placing message engines close to HBM, cache, and I/O, with specialized hardware to accelerate reduction-based collectives such as ReduceScatter. While motivated by DLRMs, these broadly applicable design principles carry over to subsequent MTIA generations (MTIA 400, 450, and 500) optimized for GenAI models. To our knowledge, MTIA 300 is the first accelerator with built-in NIC chiplets and general-purpose collective offloading engines, enabling efficient scale-up and scale-out communication. Furthermore, while MTIA 300’s combination of moderate FLOPS and higher HBM bandwidth and capacity was initially optimized for training DLRMs, these characteristics make it effective for GenAI inference. Performance evaluation shows that MTIA 300 is competitive with same-generation GPUs while offering cost advantages.

## 中文摘要

我们介绍 MTIA 300，这是 Meta 首款面向深度学习推荐模型（DLRM）优化的 AI 训练芯片。与生成式 AI 训练不同，DLRM 训练所需的浮点算力不高，但需要大容量内存、高网络带宽和频繁的集合通信；这种组合往往导致加速器利用率偏低。MTIA 300 通过三项关键创新应对这些挑战：(1) 内置 NIC 芯粒，提供 12×800 Gbps 的 RDMA 网卡，以确保高网络性能并消除 PCIe 开销；(2) 用于集合通信卸载的专用消息引擎，在仅占用三分之一芯片面积的情况下提供与计算引擎相当的吞吐；(3) 近内存计算，将消息引擎置于 HBM、缓存和 I/O 附近，并配以专用硬件来加速 ReduceScatter 等基于归约的集合操作。虽然这些设计的出发点来自 DLRM，但这些广泛适用的设计原则延续到了后续为生成式 AI 模型优化的 MTIA 世代（MTIA 400、450 和 500）。据我们所知，MTIA 300 是首款内置 NIC 芯粒与通用集合通信卸载引擎的加速器，可实现高效的纵向扩展（scale-up）与横向扩展（scale-out）通信。此外，尽管 MTIA 300“适中算力搭配更高 HBM 带宽与容量”的组合最初是为 DLRM 训练而优化，但这些特性也使其在生成式 AI 推理中表现出色。性能评估表明，MTIA 300 与同代 GPU 具有竞争力，同时具备成本优势。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2026](../index.md)
