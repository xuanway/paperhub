---
title: "CODA: Algorithm-Hardware Co-Design for Edge Video Diffusion via NMP-Enabled Compute-Cache Operator Disaggregation"
description: "MICRO 2026 · Session 6D · CODA：通过近存处理支持的计算与缓存算子分离，实现边缘视频扩散的算法与硬件协同设计"
tags:
  - "MICRO2026"
  - "Cache"
  - "HW-SW Co-design"
---

# CODA: Algorithm-Hardware Co-Design for Edge Video Diffusion via NMP-Enabled Compute-Cache Operator Disaggregation

**中文标题：** CODA：通过近存处理支持的计算与缓存算子分离，实现边缘视频扩散的算法与硬件协同设计

**所属 Session：** [Session 6D](index.md) · [MICRO 2026](../index.md)

**作者：** Yuanpeng Zhang, YuXuan Wu, Yitong Xiao, Chenhao Xue, Yi Ren, Cong Li, Yihan Yin, Dimin Niu, Guangyu Sun

**来源：** MICRO 2026，pp. 2231–2246；[DOI](https://doi.org/10.1109/MICRO67795.2026.00154)

## 英文摘要

Deploying Video Diffusion Models (VDMs) on edge devices is appealing for localized and privacy-preserving generation, but their iterative Transformer-based denoising remains too slow for practical local inference. Cross-Timestep Caching (CTC) has emerged as a promising direction for reducing redundant computation, reusing activations across adjacent denoising steps rather than modifying model weights, while largely preserving generation fidelity. However, on memory-constrained edge GPUs, CTC requires a massive cache footprint that quickly exceeds on-device VRAM and forces the cache into host memory. More fundamentally, cache operators remain tightly interleaved and chain-dependent with native compute operators, so naive near-memory offloading still incurs repeated PCIe exchanges for residual and fusion computations, turning cache reuse into a communication- and serialization-bound execution flow. We therefore propose CODA, an algorithm-hardware co-designed architecture centered on Compute-Cache Operator Disaggregation. CODA separates dense compute paths and memory-bound cache paths across the xPU and a lightweight DIMM-side near-memory engine, reorganizes fragmented cache activity into hardware-friendly coalesced segments, and exploits Classifier-Free Guidance (CFG) branch independence to overlap xPU compute with cache-side execution. Experiments show that CODA achieves up to 1.80× end-to-end speedup and 1.74× higher energy efficiency, while preserving competitive generation quality compared with a state-of-the-art caching algorithm.

## 中文摘要

在边缘设备上部署视频扩散模型 (VDM) 对于本地化和隐私保护生成很有吸引力，但其基于 Transformer 的迭代去噪对于实际本地推理来说仍然太慢。跨时间步缓存（CTC）已成为减少冗余计算的一个有前途的方向，在相邻的去噪步骤中重用激活而不是修改模型权重，同时在很大程度上保持生成保真度。然而，在内存受限的边缘 GPU 上，CTC 需要大量的缓存占用空间，该占用空间很快就会超过设备上的 VRAM，并强制将缓存放入主机内存中。更根本的是，缓存运算符与本机计算运算符保持紧密交错和链依赖，因此简单的近内存卸载仍然会导致重复的 PCIe 交换以进行残差和融合计算，从而将缓存重用转变为通信和序列化绑定的执行流。因此，我们提出了 CODA，一种以计算缓存运算符分解为中心的算法硬件协同设计架构。 CODA 将 xPU 上的密集计算路径和内存绑定缓存路径与轻量级 DIMM 端近内存引擎分开，将碎片化缓存活动重新组织为硬件友好的合并段，并利用无分类器指导 (CFG) 分支独立性将 xPU 计算与缓存端执行重叠。实验表明，与最先进的缓存算法相比，CODA 实现了高达 1.80 倍的端到端加速和 1.74 倍的能效，同时保持了有竞争力的生成质量。

## 中文关键词

视频扩散模型；近存处理；算法与硬件协同设计；端侧推理；算子解耦

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6D](index.md) · [MICRO 2026 主页](../index.md)
