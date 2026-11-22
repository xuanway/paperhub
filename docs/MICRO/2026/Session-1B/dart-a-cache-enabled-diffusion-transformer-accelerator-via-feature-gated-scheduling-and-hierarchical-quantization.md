---
title: "DART: A Cache-Enabled Diffusion Transformer Accelerator via Feature-Gated Scheduling and Hierarchical Quantization"
description: "MICRO 2026 · Session 1B · DART：通过特征门控调度与分层量化实现缓存支持的扩散 Transformer 加速器"
tags:
  - "MICRO2026"
  - "Cache"
  - "Quantization"
---

# DART: A Cache-Enabled Diffusion Transformer Accelerator via Feature-Gated Scheduling and Hierarchical Quantization

**中文标题：** DART：通过特征门控调度与分层量化实现缓存支持的扩散 Transformer 加速器

**所属 Session：** [Session 1B](index.md) · [MICRO 2026](../index.md)

**作者：** Zihan Zou, Peng Zheng, Shun Zhang, Xinyang Chen, Jiaming Lin, Borui An, Yichen Hu, Xinming Yan, Xin Cao, Hao Cai, Bo Liu

**来源：** MICRO 2026，pp. 143–157；[DOI](https://doi.org/10.1109/MICRO67795.2026.00026)

## 英文摘要

Diffusion Transformers (DiTs) have revolutionized generative AI, but their iterative denoising process incurs severe computational overhead. Cache-enabled methods alleviate this by reusing features from previous timesteps. However, current approaches remain hardware-unfriendly because caching incurs heavy memory-access overhead, leading to three key challenges: 1) Inefficient fine-grained token refresh requires loading full weights for minor token updates; 2) Massive full-precision intermediate activations are cached, causing huge memory overhead; 3) Hardware under-utilization caused by dynamically shifting memory-bound and compute-bound bottlenecks in block operators. To this end, this paper proposes DART, an algorithm-hardware co-design framework for cache-enabled DiT acceleration, featuring three key innovations: 1) Feature-gated cache scheduling strategy to dynamically replace low-refresh-rate blocks with full reuse, eliminating redundant weight loading and computation; 2) Denoising-directed cache activation compression to exploit the directional and scale characteristics of cached branches for mixed-precision quantization; 3) Subspace Givens-Hadamard rotation chain to alleviate both computational and memory pressure while maintaining high model accuracy. These techniques, combined with custom accelerator designs, enable practical cache-enabled DiT acceleration. Extensive experiments on representative benchmarks show that DART achieves geometric-mean speedup and energy-efficiency ranges of 3.60–5.05× and 10.40–14.81× over the NVIDIA A100 GPU. Compared to the SOTA cache-enabled DiT accelerator, DART achieves a geometric-mean speedup of 1.78× and 37.7% energy savings.

## 中文摘要

扩散Transformer (DiT) 彻底改变了生成式人工智能，但其迭代去噪过程会产生严重的计算开销。支持缓存的方法通过重用之前时间步的特征来缓解这种情况。然而，当前的方法仍然对硬件不友好，因为缓存会产生大量的内存访问开销，从而导致三个关键挑战：1）低效的细粒度词元刷新需要加载较小词元更新的完整权重； 2）海量全精度中间激活被缓存，造成巨大的内存开销； 3) 由于动态转移块运算符中的内存限制和计算限制瓶颈而导致硬件利用率不足。为此，本文提出了DART，一种用于支持缓存的DiT加速的算法-硬件协同设计框架，具有三个关键创新：1）特征门控缓存调度策略，动态替换低刷新率块并充分重用，消除冗余的权重加载和计算； 2）去噪定向缓存激活压缩，利用缓存分支的方向和尺度特征进行混合精度量化； 3）子空间Givens-Hadamard旋转链减轻计算和内存压力，同时保持较高的模型精度。这些技术与定制加速器设计相结合，可实现实用的缓存 DiT 加速。对代表性基准的大量实验表明，DART 比 NVIDIA A100 GPU 实现了几何平均加速比和能效范围 3.60-5.05 倍和 10.40-14.81 倍。与支持 SOTA 缓存的 DiT 加速器相比，DART 实现了 1.78 倍的几何平均加速，并节省了 37.7% 的能源。

## 中文关键词

扩散 Transformer；硬件加速器；算法与硬件协同设计；层次化量化；特征缓存

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1B](index.md) · [MICRO 2026 主页](../index.md)
