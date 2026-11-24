---
title: "ELSA: An ELastic SNN Inference Architecture for Efficient Neuromorphic Computing"
description: "ISCA 2026 · Session 10B · ELSA: An ELastic SNN Inference Architecture for Efficient Neuromorphic Computing"
tags:
  - "ISCA2026"
  - "Session 10B"
  - "ML Accelerators 2"
---

# ELSA: An ELastic SNN Inference Architecture for Efficient Neuromorphic Computing

**中文标题：** ELSA: 面向高效神经形态计算的高弹性 SNN 推理架构

**所属 Session：** [Session 10B](index.md) · [ISCA 2026](../index.md)

**作者：** Kang You, Chen Nie, Lee Jun Yan, Ziling Wei, Cheng Zou, Zekai Xu, Yu Feng, Honglan Jiang, Zhezhi He

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Spiking neural networks (SNNs) exploit event-driven and addition-only computation to substantially improve efficiency for intelligent computation. A key temporal property of SNNs, elastic inference, allows outputs to emerge progressively, enabling responses to salient inputs much earlier than full evaluation. However, existing SNN-specific accelerators cannot capitalize on this property. Layer-by-layer designs emit outputs only after all layers are complete, while time-step-by-time-step designs rely on coarse-grained, layer-wise pipelines that require synchronizing all spines/tokens within a layer. This barrier prevents results from being forwarded immediately, delaying the earliest possible response and forfeiting the benefits of elastic inference. To address these challenges, we propose ELSA, a near-SRAM dataflow architecture that realizes true elastic inference through a fine-grained spine/token-wise pipeline and hardware optimizations tailored to SNNs. ELSA forwards each spine/token immediately upon production, forming a continuous streaming pipeline that substantially reduces the latency to the first response. To enhance this lightweight execution, ELSA introduces a bundled address event representation protocol to lower communication traffic of network-on-chip (NoC), and leverages mini-batch spiking Gustavson-product to cut memory access and exploit inherent sparsity. Combined with mapping and scheduling optimizations, ELSA achieves efficient, event-driven computation without compromising accuracy. Experiments show that SNNs can outperform quantized artificial neural networks (QANNs) while maintaining on-par accuracy. For a 4-bit ResNet-50, ELSA achieves 3.4× speedup and 13.6× higher energy efficiency over the SOTA QANN accelerator (ANT), and 2.9× speedup and 22.1× energy efficiency gains over the SOTA SNN accelerator (PAICORE).

## 中文摘要

脉冲神经网络（SNN）利用事件驱动和仅含加法的计算方式，大幅提升了智能计算的效率。SNN 的一个关键时间特性——弹性推理（elastic inference）——允许输出逐步显现，使得对显著输入的响应能够远早于完整评估而给出。然而，现有的 SNN 专用加速器无法利用这一特性。逐层（layer-by-layer）设计只有在所有层都完成后才输出结果，而逐时间步（time-step-by-time-step）设计依赖粗粒度的按层流水（layer-wise pipeline），要求同步一层内的所有 spine/token。这一障碍阻止了结果的即时转发，延迟了最早可能的响应，并丧失了弹性推理带来的收益。为应对这些挑战，我们提出 ELSA，一种近 SRAM（near-SRAM）数据流架构，通过细粒度的 spine/token 级流水以及针对 SNN 定制的硬件优化，实现真正的弹性推理。ELSA 在每个 spine/token 产生时立即转发，形成连续的流式流水线，大幅缩短首次响应的延迟。为增强这种轻量级执行，ELSA 引入捆绑式地址事件表示（bundled address event representation）协议以降低片上网络（NoC）的通信流量，并利用小批量脉冲 Gustavson 积（mini-batch spiking Gustavson-product）来减少内存访问并挖掘固有稀疏性。结合映射与调度优化，ELSA 在不损失精度的前提下实现高效的事件驱动计算。实验表明，SNN 可以在保持同等精度的同时优于量化人工神经网络（QANN）。对于 4-bit ResNet-50，ELSA 相比最先进的 QANN 加速器（ANT）实现 3.4× 加速和 13.6× 更高的能效，相比最先进的 SNN 加速器（PAICORE）实现 2.9× 加速和 22.1× 的能效提升。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：Intelligent-Computing-Research-Group/ELSA](https://github.com/Intelligent-Computing-Research-Group/ELSA)
- [实验材料归档（Zenodo 19449728）](https://zenodo.org/records/19449728)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10B](index.md) · [返回 ISCA 2026](../index.md)
