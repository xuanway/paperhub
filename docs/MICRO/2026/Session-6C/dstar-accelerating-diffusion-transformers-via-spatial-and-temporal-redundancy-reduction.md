---
title: "DSTAR: Accelerating Diffusion Transformers via Spatial and Temporal Redundancy Reduction"
description: "MICRO 2026 · Session 6C · DSTAR：通过减少空间与时间冗余加速扩散 Transformer"
tags:
  - "MICRO2026"
---

# DSTAR: Accelerating Diffusion Transformers via Spatial and Temporal Redundancy Reduction

**中文标题：** DSTAR：通过减少空间与时间冗余加速扩散 Transformer

**所属 Session：** [Session 6C](index.md) · [MICRO 2026](../index.md)

**作者：** Chi Zhang, Jieru Zhao, Yu Feng, Chen Zhang, Quan Chen, Minyi Guo

**来源：** MICRO 2026，pp. 2147–2161；[DOI](https://doi.org/10.1109/MICRO67795.2026.00149)

## 英文摘要

Diffusion Transformers (DiTs) have been widely used in many tasks, including image synthesis, video generation, and content editing. However, their multi-iteration inference process leads to performance inefficiency and high energy consumption. Existing acceleration methods primarily focus on reducing temporal redundancy between adjacent timesteps, but often overlook the specific features of DiTs. As a result, these approaches either suffer from great accuracy degradation or fail to achieve high efficiency. We present DSTAR, a software-hardware co-design framework that accelerates DiT inference by reducing spatial and temporal redundancy. At the algorithmic level, DSTAR introduces a fine-grained mixed-precision quantization method for differential activations in linear operations, significantly increasing the proportion of low-bit computations. Additionally, DSTAR incorporates a sparse attention reuse mechanism to minimize redundant computation in attention layers. For architectural support, we design a specialized hardware accelerator which achieves high efficiency in both latency and energy consumption. Evaluation on seven typical DiTs demonstrates that DSTAR achieves up to 7.33× latency speedup and 41.89× energy savings compared to an NVIDIA A100 GPU, and achieves up to 2.54× latency speedup and 3.68× energy savings compared to SOTA accelerators, without accuracy degradation.

## 中文摘要

扩散Transformer (DiT) 已广泛应用于许多任务，包括图像合成、视频生成和内容编辑。然而，它们的多次迭代推理过程导致性能低效和高能耗。现有的加速方法主要侧重于减少相邻时间步之间的时间冗余，但常常忽略 DiT 的具体特征。因此，这些方法要么精度大幅下降，要么无法实现高效率。我们提出了 DSTAR，一种软件-硬件协同设计框架，可通过减少空间和时间冗余来加速 DiT 推理。在算法层面，DSTAR针对线性运算中的差分激活引入了细粒度混合精度量化方法，显着提高了低位计算的比例。此外，DSTAR 还采用了稀疏注意力重用机制，以最大限度地减少注意力层中的冗余计算。对于架构支持，我们设计了专门的硬件加速器，可以在时延和能耗方面实现高效率。对七个典型 DiT 的评估表明，与 NVIDIA A100 GPU 相比，DSTAR 实现了高达 7.33 倍的时延加速和 41.89 倍的节能；与 SOTA 加速器相比，实现了高达 2.54 倍的时延加速和 3.68 倍的节能，且精度没有下降。

## 中文关键词

扩散 Transformer；冗余消除；量化；加速器；时空复用

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6C](index.md) · [MICRO 2026 主页](../index.md)
