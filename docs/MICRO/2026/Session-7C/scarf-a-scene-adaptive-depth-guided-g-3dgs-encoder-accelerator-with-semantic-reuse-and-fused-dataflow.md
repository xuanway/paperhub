---
title: "SCARF: A Scene-Adaptive Depth-Guided G-3DGS Encoder Accelerator with Semantic Reuse and Fused Dataflow"
description: "MICRO 2026 · Session 7C · SCARF：具备语义复用与融合数据流的场景自适应深度引导 G-3DGS 编码器加速器"
tags:
  - "MICRO2026"
---

# SCARF: A Scene-Adaptive Depth-Guided G-3DGS Encoder Accelerator with Semantic Reuse and Fused Dataflow

**中文标题：** SCARF：具备语义复用与融合数据流的场景自适应深度引导 G-3DGS 编码器加速器

**所属 Session：** [Session 7C](index.md) · [MICRO 2026](../index.md)

**作者：** Zirui Ma, Zhihua Fan, Haibin Wu, Wenxing Li, Fulin Zhang, Dongrui Fan, Xiaochun Ye, Wenming Li

**来源：** MICRO 2026，pp. 2512–2528；[DOI](https://doi.org/10.1109/MICRO67795.2026.00172)

## 英文摘要

Depth-guided, cost-volume-based Generalizable 3D Gaussian Splatting (G-3DGS) encoders reconstruct scenes as sets of Gaussian primitives directly from multi-view images without requiring per-scene optimization, thereby facilitating feed-forward novel-view synthesis on edge computing platforms. However, their shared encoder architecture presents two primary bottlenecks. First, the per-pixel depth search disregards semantic similarity within the 2D feature space, causing depth search operations to account for over 65% of memory traffic due to redundant exhaustive candidate scans. Second, the sequential pipeline of depth prediction followed by Gaussian generation neglects local 3D geometric continuity, resulting in more than 52% of generated Gaussians being redundant prior to instantiation. In this paper, we introduce SCARF, a dataflow-co-designed accelerator that aligns each bottleneck with a corresponding scene-level regularity. To mitigate the first bottleneck, Feature Similarity Depth Reuse reconceptualizes depth search as a problem of semantic locality: depth consistency is determined by affinity in feature space rather than physical address proximity. It transforms exhaustive per-pixel depth searches into anchor-centered local searches. To overcome the second bottleneck, Scene-Adaptive Early Sparsification disrupts the conventional serial depth-to-materialization boundary by probing each tile to infer local scene regularity. It then selectively activates only the minimally sufficient generation pathway, eliminating redundant Gaussian computations before primitive instantiation. On a 27.8 square millimeter 28 nm post-layout design, SCARF delivers a 2.94-fold geometric-mean end-to-end speedup with maximum PSNR degradation below 0.072 percent, 2.23 inferences per joule, and 34.5-fold GPU energy efficiency.

## 中文摘要

深度引导、基于成本体积的广义 3D 高斯泼溅 (G-3DGS) 编码器直接从多视图图像将场景重建为高斯基元集，无需按场景进行优化，从而促进边缘计算平台上的前馈新颖视图合成。然而，他们的共享编码器架构存在两个主要瓶颈。首先，每像素深度搜索忽略了 2D 特征空间内的语义相似性，导致深度搜索操作由于冗余的详尽候选扫描而占用了超过 65% 的内存流量。其次，深度预测的顺序管道和高斯生成忽略了局部 3D 几何连续性，导致超过 52% 的生成高斯在实例化之前是冗余的。在本文中，我们介绍了 SCARF，这是一种数据流共同设计的加速器，可将每个瓶颈与相应的场景级规律对齐。为了缓解第一个瓶颈，特征相似深度重用将深度搜索重新概念化为语义局部性问题：深度一致性是由特征空间中的亲和力而不是物理地址邻近性决定的。它将详尽的每像素深度搜索转换为以锚点为中心的局部搜索。为了克服第二个瓶颈，场景自适应早期稀疏化通过探测每个分块来推断局部场景规律性，破坏了传统的串行深度到具体化的边界。然后，它仅选择性地激活最低限度的足够生成路径，从而在原始实例化之前消除冗余的高斯计算。在 27.8 平方毫米 28 nm 后布局设计上，SCARF 实现了 2.94 倍几何平均端到端加速，最大 PSNR 下降低于 0.072%，每焦耳完成 2.23 次推理，能效达到 GPU 的 34.5 倍。

## 中文关键词

可泛化三维高斯泼溅；领域专用加速器；数据流优化；深度引导；语义复用

## 代码与研究制品

- 代码仓库：[https://github.com/MAdrid1011/SCARF](https://github.com/MAdrid1011/SCARF)
- 研究制品归档：[https://doi.org/10.5281/zenodo.22434931](https://doi.org/10.5281/zenodo.22434931)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 7C](index.md) · [MICRO 2026 主页](../index.md)
