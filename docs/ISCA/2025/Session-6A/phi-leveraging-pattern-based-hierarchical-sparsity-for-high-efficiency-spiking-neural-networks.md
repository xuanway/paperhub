---
title: "Phi: Leveraging Pattern-based Hierarchical Sparsity for High-Efficiency Spiking Neural Networks"
description: "ISCA 2025 · Session 6A · Phi：利用基于模式的层次稀疏性实现高效脉冲神经网络"
tags:
  - "ISCA2025"
  - "Session 6A"
  - "ML Accelerators II"
---

# Phi: Leveraging Pattern-based Hierarchical Sparsity for High-Efficiency Spiking Neural Networks

**中文标题：** Phi：利用基于模式的层次稀疏性实现高效脉冲神经网络

**所属 Session：** [Session 6A](index.md) · [ISCA 2025](../index.md)

**作者：** Chiyue Wei, Bowen Duan, Cong Guo, Jingyang Zhang, Qingyue Song, Hai (Helen) Li, Yiran Chen

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731035) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Spiking Neural Networks (SNNs) are gaining attention for their energy efficiency and biological plausibility, utilizing 0-1 activation sparsity through spike-driven computation. While existing SNN accelerators exploit this sparsity to skip zero computations, they often overlook the unique distribution patterns inherent in binary activations. In this work, we observe that particular patterns exist in spike activations, which we can utilize to reduce the substantial computation of SNN models. Based on these findings, we propose a novel pattern-based hierarchical sparsity framework, termed Phi, to optimize computation. Phi introduces a two-level sparsity hierarchy: Level 1 exhibits vector-wise sparsity by representing activations with pre-defined patterns, allowing for offline pre-computation with weights and significantly reducing most runtime computation. Level 2 features element-wise sparsity by complementing the Level 1 matrix, using a highly sparse matrix to further reduce computation while main- taining accuracy. We present an algorithm-hardware co-design approach. Algorithmically, we employ a k-means-based pattern selection method to identify representative patterns and introduce a pattern-aware fine-tuning technique to enhance Level 2 sparsity. Architecturally, we design Phi, a dedicated hardware architecture that efficiently processes the two levels of Phi sparsity on the fly. Ex- tensive experiments demonstrate that Phi achieves a 3.45×speedup and a 4.93×improvement in energy efficiency compared to state- of-the-art SNN accelerators, showcasing the effectiveness of our framework in optimizing SNN computation.

## 中文摘要

脉冲神经网络（SNN）凭借高能效与生物可解释性受到广泛关注，依靠脉冲驱动计算，天然具备0-1激活稀疏特性。现有SNN加速器利用该稀疏性跳过零值计算，但往往忽略二值激活本身独特的分布模式。本文观察到脉冲激活存在可挖掘的特征模式，并以此降低SNN模型的计算量。基于该发现，本文提出一种全新的基于模式的分层稀疏框架Phi，用于计算优化。

Phi构建两层稀疏层次：第一层是向量级稀疏，使用预定义模式表征激活值，支持与权重提前离线预计算，大幅削减绝大多数运行时计算；第二层是元素级稀疏，作为第一层矩阵的补充，借助高稀疏矩阵进一步削减计算量，同时保证精度。
本文采用算法-硬件协同设计思路：算法层面，基于k-means挑选代表性模式，并提出感知模式的微调策略，提升第二层稀疏度；架构层面，设计专用硬件架构Phi，实时高效处理这两层稀疏。
大量实验表明，对比前沿SNN加速器，Phi最高提速3.45倍，能效提升4.93倍，验证了该框架优化SNN计算的有效性。

## 英文关键词

Spiking Neural Networks, Accelerator, Hierarchical Sparsity

## 中文关键词

脉冲神经网络, 加速器, 分层稀疏性

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731035)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2025](../index.md)
