---
title: "Bishop: Sparsified Bundling Spiking Transformers on Heterogeneous Cores with Error-constrained Pruning"
description: "ISCA 2025 · Session 6A · Bishop：通过误差约束剪枝在异构核心上稀疏捆绑脉冲 Transformer"
tags:
  - "ISCA2025"
  - "Session 6A"
  - "ML Accelerators II"
---

# Bishop: Sparsified Bundling Spiking Transformers on Heterogeneous Cores with Error-constrained Pruning

**中文标题：** Bishop：通过误差约束剪枝在异构核心上稀疏捆绑脉冲 Transformer

**所属 Session：** [Session 6A](index.md) · [ISCA 2025](../index.md)

**作者：** Boxun Xu, Yuxuan Yin, Vikram Iyer, Peng Li

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731063) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Spiking neural networks(SNNs) have emerged as a promising so- lution for deployment on resource-constrained edge devices and neuromorphic hardware due to their low power consumption. Spik- ing transformers, which integrate attention mechanisms similar to those found in artificial neural networks (ANNs), have recently ex- hibited impressive performance. However, these models are large in size and involve high-volume computation in both time and space, posing significant challenges for efficient hardware acceleration. We present Bishop, the first dedicated hardware accelerator archi- tecture and HW/SW co-design framework for spiking transform- ers that optimally represents, manages, and processes spike-based workloads while exploring spatiotemporal sparsity and data reuse. Specifically, we introduce the concept of Token-Time Bundle (TTB), a container that bundles spiking data of a set of tokens over multiple time points. Our heterogeneous accelerator architecture Bishop concurrently processes workload packed in TTBs and explores intra- and inter-bundle multiple-bit weight reuse to significantly re- duce memory access. Bishop utilizes a stratifier, a dense core array, and a sparse core array to process MLP blocks and projection lay- ers. The stratifier routes high-density spiking activation workload to the dense core and low-density counterpart to the sparse core, ensuring optimized processing tailored to the given spatiotemporal sparsity level. To further reduce data access and computation, we introduce a novel Bundle Sparsity-Aware (BSA) training pipeline that enhances not only the overall but also structured TTB-level firing sparsity. Moreover, the processing efficiency of self-attention layers is boosted by the proposed Error-Constrained TTB Pruning (ECP), which trims activities in spiking queries, keys, and values both before and after the computation of spiking attention maps with a well-defined error bound. Finally, we design a reconfigurable TTB spiking attention core to efficiently compute spiking attention maps by executing highly simplified “AND” and “Accumulate” op- erations. On average, Bishop achieves a 5.91×speedup and 6.11× improvement in energy efficiency over previous SNN accelerators, while delivering higher accuracy across multiple datasets.

## 中文摘要

脉冲神经网络（SNN）功耗低，非常适合部署在资源受限的边缘设备与神经形态硬件上。脉冲Transformer借鉴人工神经网络（ANN）的注意力机制，近期取得了不错的效果。但这类模型规模大，时空维度计算量高，给高效硬件加速带来巨大挑战。

本文提出Bishop，首个面向脉冲Transformer的专用硬件加速器架构与软硬件协同设计框架，可对脉冲负载进行最优表示、管理与处理，充分挖掘时空稀疏性与数据复用。具体来说，本文提出Token-Time Bundle（TTB，令牌-时间束），将一组令牌在多个时间步上的脉冲数据打包存放。Bishop异构加速器可并行处理打包在TTB内的负载，并挖掘束内、束间的多比特权重复用，大幅减少访存。

Bishop包含分层调度器（stratifier）、稠密核阵列与稀疏核阵列，用于处理MLP模块与投影层。分层调度器将高密度脉冲激活负载分配给稠密核，低密度负载分配给稀疏核，根据时空稀疏度实现适配性最优处理。为进一步减少数据访问与计算量，本文提出Bundle Sparsity-Aware（BSA，束感知稀疏）训练流水线，提升整体稀疏度以及TTB粒度上的结构化发放稀疏性。此外，本文提出Error-Constrained TTB Pruning（ECP，带误差约束的TTB剪枝）提升自注意力层处理效率：在脉冲注意力图计算前后，对脉冲查询、键、值进行裁剪，并严格控制误差上限。最后，我们设计可重构TTB脉冲注意力核，通过极简的“与”和累加运算高效计算脉冲注意力图。 在多个数据集上，Bishop相比已有SNN加速器，平均提速5.91倍，能效提升6.11倍，同时保持更高精度。

## 英文关键词

Spiking Neural Networks, Neuromorphic Accelerators, Transformers, HW/SW Co-Design

## 中文关键词

脉冲神经网络, 神经形态加速器, Transformer, 软硬件协同设计

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731063)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2025](../index.md)
