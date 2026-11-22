---
title: "RAIL: A Reconfigurable Spatial Accelerator for Linear-Time Sequence Model Inference"
description: "MICRO 2026 · Session 1D · RAIL：面向线性时间序列模型推理的可重构空间加速器"
tags:
  - "MICRO2026"
  - "Reconfigurable Computing"
---

# RAIL: A Reconfigurable Spatial Accelerator for Linear-Time Sequence Model Inference

**中文标题：** RAIL：面向线性时间序列模型推理的可重构空间加速器

**所属 Session：** [Session 1D](index.md) · [MICRO 2026](../index.md)

**作者：** Xinyu Zhu, Qinggang Wang, Wenju Zhao, Bing Zhu, Runze Wang, Long Zheng, Xiaofei Liao, Hai Jin, Jingling Xue

**来源：** MICRO 2026，pp. 374–388；[DOI](https://doi.org/10.1109/MICRO67795.2026.00041)

## 英文摘要

Linear-time sequence models (LSMs)—including state space models, linear attention, and modern RNNs—are promising post-Transformer architectures for long-context modeling. However, large-scale inference is bottlenecked by the state-update layer, whose limited temporal locality of hidden states leads to excessive HBM traffic and makes it bandwidth-bound. While prefetch-driven inter-layer fusion can improve bandwidth utilization by overlapping hidden-state prefetching with linear-layer execution, existing GPUs and accelerators struggle to exploit it effectively: redundant shared-memory operations and limited tiling flexibility result in imbalanced and underfilled software pipelines. This paper presents RAIL, a software-hardware co-designed framework for efficient LSM inference. RAIL introduces a reconfigurable spatial architecture with a fused systolic dataflow that performs end-to-end state updates while minimizing redundant operand movement and maximizing on-chip reuse across diverse model shapes and algorithmic variants. It adopts a coarse-grained organization that enables flexible tiling and high pipeline utilization with low synchronization overhead. To further improve utilization, RAIL incorporates a lightweight counter-based tagging mechanism that triggers vector operations on partial array results, enabling fine-grained array-vector overlap. On the software side, RAIL employs a multi-tile interleaved pipeline to provide highly parallel processing across hardware units. We implement RAIL in synthesizable RTL and evaluate it on a range of LSM workloads, achieving an average 2.56x speedup over the NVIDIA H200 GPU and 1.83x over the state-of-the-art accelerator HLX.

## 中文摘要

线性时间序列模型 (LSM)——包括状态空间模型、线性注意力和现代 RNN——是用于长上下文建模的有前景的后 Transformer 架构。然而，大规模推理受到状态更新层的瓶颈，其隐藏状态的有限时间局部性导致过多的 HBM 流量并使其受到带宽限制。虽然预取驱动的层间融合可以通过将隐藏状态预取与线性层执行重叠来提高带宽利用率，但现有的 GPU 和加速器很难有效地利用它：冗余的共享内存操作和有限的平铺灵活性导致不平衡和未充分填充的软件管道。本文提出了 RAIL，这是一种用于高效 LSM 推理的软件-硬件共同设计的框架。 RAIL 引入了具有融合脉动数据流的可重构空间架构，该架构执行端到端状态更新，同时最大限度地减少冗余操作数移动并最大限度地提高跨不同模型形状和算法变体的片上重用。它采用粗粒度组织，可实现灵活的平铺和高管道利用率，同时同步开销低。为了进一步提高利用率，RAIL 采用了一种轻量级的基于计数器的标记机制，可以触发对部分数组结果的向量操作，从而实现细粒度的数组向量重叠。在软件方面，RAIL 采用多块交错管道来提供跨硬件单元的高度并行处理。我们在可综合 RTL 中实现 RAIL，并在一系列 LSM 工作负载上对其进行评估，与 NVIDIA H200 GPU 相比平均加速 2.56 倍，比最先进的加速器 HLX 平均加速 1.83 倍。

## 中文关键词

线性时间序列模型；状态空间模型；加速器架构；软硬件协同设计；空间架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1D](index.md) · [MICRO 2026 主页](../index.md)
