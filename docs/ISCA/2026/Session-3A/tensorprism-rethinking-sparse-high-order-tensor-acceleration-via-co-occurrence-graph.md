---
title: "TensorPrism: Rethinking Sparse High-order Tensor Acceleration via Co-occurrence Graph"
description: "ISCA 2026 · Session 3A · TensorPrism: Rethinking Sparse High-order Tensor Acceleration via Co-occurrence Graph"
tags:
  - "ISCA2026"
  - "Session 3A"
  - "ML Accelerators 1"
---

# TensorPrism: Rethinking Sparse High-order Tensor Acceleration via Co-occurrence Graph

**中文标题：** TensorPrism: 通过共现图重新思考稀疏高阶张量加速

**所属 Session：** [Session 3A](index.md) · [ISCA 2026](../index.md)

**作者：** Fangzhou Ye, Shilin Tian, Amir Ghazizadeh Ahsaei, Hao Zheng

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Sparse high-order tensors are a key computational primitive across diverse domains, including large language models, scientific computing, recommendation systems, and multi-dimensional signal processing. Existing work primarily relies on tensor contraction to unfold high-order tensors into two-dimensional sparse–dense matrix multiplications (SpMM), enabling direct reuse of well-studied SpMM optimization techniques. A complementary line of research adopts tensor-native approaches, which operate directly on the multi-dimensional tensor structure to improve data locality. However, both unfolding-based and tensor-native techniques are inefficient to fully exploit data reuse in sparse high-order tensor computations, due to (1) the expansion of matrix dimensions and (2) missed reuse opportunities across different tensor modes. In this paper, we posit that matricization dismantles high-dimensional data reuse, erasing the correlations among nonzero elements across multiple tensor modes. We propose TensorPrism, a novel acceleration framework for sparse high-order tensor computation based on a co-occurrence graph abstraction. The central idea is to transform a high-order tensor into a co-occurrence graph that captures nonzero correlations across all tensor dimensions. Building on this abstraction, TensorPrism introduces three key designs. First, we formulate a co-occurrence graph representation that redefines dataflow and tiling to improve data reuse. Second, we introduce a new dataflow strategy that enhances reuse opportunities across tensor modes. Finally, we provide an efficient accelerator design tailored to the graph-based computation. Our evaluation shows that TensorPrism delivers performance speedups of 2.22×, 2.40×, 1.71×, and 1.76× over state-of-the-art designs SPADE [1], HotTiles [2], GSpTC [3], and TCP [4], respectively.

## 中文摘要

稀疏高阶张量是跨多个领域的关键计算原语，包括大语言模型、科学计算、推荐系统和多维信号处理。现有工作主要依赖张量收缩将高阶张量展开为二维稀疏-稠密矩阵乘法（SpMM），从而直接复用已深入研究过的SpMM优化技术。另一条研究路线采用张量原生方法，直接在多维张量结构上操作以改善数据局部性。然而，基于展开和张量原生的技术都无法充分利用稀疏高阶张量计算中的数据复用，原因在于（1）矩阵维度的扩展和（2）跨不同张量模的复用机会丢失。在本文中，我们论证了矩阵化破坏了高维数据的复用，抹去了跨多个张量模的非零元素之间的相关性。我们提出TensorPrism，一种基于共现图抽象的稀疏高阶张量计算的新型加速框架。其核心思想是将高阶张量转换为捕获所有张量维度上非零相关性的共现图。在此抽象基础上，TensorPrism引入了三个关键设计。首先，我们制定了一种重新定义数据流和分块的共现图表示，以改善数据复用。其次，我们引入了一种新的数据流策略，增强了跨张量模的复用机会。最后，我们提供了一种针对基于图的计算量身定制的高效加速器设计。我们的评估表明，与最先进的设计SPADE [1]、HotTiles [2]、GSpTC [3]和TCP [4]相比，TensorPrism分别实现了2.22×、2.40×、1.71×和1.76×的性能加速。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2026](../index.md)
