---
title: "NetFED: Network-Aware Acceleration for Multi-Key Privacy-Preserving Federated Learning Aggregation"
description: "MICRO 2026 · Session 9D · NetFED：面向多密钥隐私保护联邦学习聚合的网络感知加速"
tags:
  - "MICRO2026"
---

# NetFED: Network-Aware Acceleration for Multi-Key Privacy-Preserving Federated Learning Aggregation

**中文标题：** NetFED：面向多密钥隐私保护联邦学习聚合的网络感知加速

**所属 Session：** [Session 9D](index.md) · [MICRO 2026](../index.md)

**作者：** Jaeho Jeon, Wonjin Shin, Sungwoong Yune, Joo-Young Kim

**来源：** MICRO 2026，pp. 3530–3544；[DOI](https://doi.org/10.1109/MICRO67795.2026.00235)

## 英文摘要

As AI models increasingly rely on user-generated data distributed across edge devices, Privacy-Preserving Federated Learning (PPFL) has emerged as a promising approach for secure model training. However, Homomorphic Encryption (HE)-based PPFL incurs substantial overhead because encrypted weights greatly inflate both network transfer and computation costs. Hierarchical Federated Learning (HFL) alleviates this burden by introducing intermediate edge servers, but it simply shifts the bottleneck of all HE aggregation to the edge servers. Moreover, edge-level PPFL must ensure cross-device privacy, requiring multi-key HE. Existing PPFL systems are ineffective in the multi-key setting because they overlook two critical aspects of network transfer. First, edge-device dropouts cause large data retransmissions. Second, prior designs primarily accelerate computation while neglecting opportunities to overlap communication with computation. To address these limitations, we introduce NetFED, a network-aware system for accelerating multi-key HE-based PPFL. At the algorithm level, NetFED optimizes the aggregation process by selecting a unified parameter configuration that works across various FL schemes, reducing the network transfer size. It further mitigates dropout-induced inefficiency by reducing retransmissions, decreasing the resulting round latency. At the hardware level, NetFED integrates aggregation cores with a network kernel on an FPGA. By streaming encrypted weights directly for HE aggregation, it accelerates memory-bound operations and enables overlapping computation and network transfer. A comprehensive evaluation on a realistic network environment demonstrates that NetFED accelerates each multi-key based PPFL round by 2.81× over a CPU-centric aggregator and by 1.66× over the state-of-the-art PPFL accelerator.

## 中文摘要

随着人工智能模型越来越依赖分布在边缘设备上的用户生成数据，隐私保护联合学习 (PPFL) 已成为安全模型训练的一种有前景的方法。然而，基于同态加密 (HE) 的 PPFL 会产生大量开销，因为加密权重大大增加了网络传输和计算成本。分层联邦学习（HFL）通过引入中间边缘服务器减轻了这种负担，但它只是将所有 HE 聚合的瓶颈转移到了边缘服务器。此外，边缘级PPFL必须保证跨设备隐私，需要多密钥HE。现有的 PPFL 系统在多密钥设置中效率低下，因为它们忽略了网络传输的两个关键方面。首先，边缘设备丢失会导致大量数据重传。其次，现有设计主要是加速计算，而忽略了通信与计算重叠的机会。为了解决这些限制，我们引入了 NetFED，这是一种网络感知系统，用于加速基于 HE 的多键 PPFL。在算法层面，NetFED 通过选择适用于各种 FL 方案的统一参数配置来优化聚合过程，从而减少网络传输大小。它通过减少重传、减少由此产生的轮次时延，进一步减轻了因丢包而导致的低效率。在硬件层面，NetFED 将聚合核心与 FPGA 上的网络内核集成在一起。通过直接流式传输加密权重进行 HE 聚合，它可以加速内存限制操作并实现重叠计算和网络传输。对真实网络环境的综合评估表明，NetFED 比以 CPU 为中心的聚合器将每个基于多密钥的 PPFL 回合加速 2.81 倍，比最先进的 PPFL 加速器加速 1.66 倍。

## 中文关键词

联邦学习；多密钥同态加密；硬件加速器；网内处理

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9D](index.md) · [MICRO 2026 主页](../index.md)
