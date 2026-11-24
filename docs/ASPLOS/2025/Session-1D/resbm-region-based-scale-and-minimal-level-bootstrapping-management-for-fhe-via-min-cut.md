---
title: "ReSBM: Region-based Scale and Minimal-Level Bootstrapping Management for FHE via Min-Cut"
description: "ASPLOS 2025 · Session 1D · ReSBM：通过最小割实现 FHE 中基于区域的尺度与最小层级自举管理"
tags:
  - "ASPLOS2025"
  - "Session 1D"
  - "Homomorphic Encryption"
---

# ReSBM: Region-based Scale and Minimal-Level Bootstrapping Management for FHE via Min-Cut

**中文标题：** ReSBM：通过最小割实现 FHE 中基于区域的尺度与最小层级自举管理

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yan Liu (Ant Group), Jianxin Lai (Ant Group), Long Li (Ant Group), Tianxiang Sui (Ant Group), Linjie Xiao (Ant Group), Peng Yuan (Ant Group), Xiaojing Zhang (Ant Group), Qing Zhu (Ant Group), Wenguang Chen (Tsinghua University,Ant Group), Jingling Xue (UNSW)

**单位：** Ant Group；Tsinghua University,Ant Group；UNSW

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707276) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The RNS-CKKS scheme in Fully Homomorphic Encryption (FHE) supports crucial features for privacy-preserving machine learning, such as fixed-point arithmetic and SIMDstyle vectorization. Yet, managing the escalation of ciphertext scales from homomorphic multiplications, which risks capacity overflow, along with bootstrapping, presents significant challenges. These complexities are exacerbated by the need to efficiently handle scale and bootstrapping at compile time while ensuring rapid encrypted inference. In this paper, we present ReSBM, a novel compiler technique that simultaneously optimizes scale and bootstrapping for encrypted inference under RNS-CKKS. By partitioning a program's data flow graph (DFG) into regions with a uniform multiplicative depth of one, ReSBM ensures that placements of Scale Management Operations (SMOs) and bootstraps affect only the latency of a region, not the scales and levels of its live-out ciphertexts. Our region-based approach tackles the NP-hard challenge of optimal bootstrapping placement with hierarchical strategies: (1) optimal intra-region SMO and bootstrapping placement using min-cut, (2) bootstrapping-guided rescaling region identification across a sequence of regions, culminating in tentative bootstrapping at two terminal regions, and (3) minimal-level bootstrap placement across the DFG, elevating ciphertexts only to the necessary minimal *Corresponding author. Attribution International 4.0 License.. Validation across a variety of complex models on CPUs shows that ReSBM not only compiles these models more rapidly than a leading method but also boosts encrypted inference efficiency by an average of 12.1% when compared to another leading method. Consequently, ReSBM substantially improves the practical deployment of large models for encrypted inference, surpassing existing methods in terms of both compilation speed and inference performance.

## 中文摘要

全同态加密（FHE）中的 RNS-CKKS 方案支持隐私保护机器学习所需的关键特性，例如定点算术和 SIMD 风格向量化。然而，管理同态乘法引起的密文尺度升级（存在容量溢出风险）以及自举，带来了重大挑战。这些复杂性还因需要在编译期高效处理尺度与自举、同时确保快速的加密推理而进一步加剧。在本文中，我们提出 ReSBM，一种新颖的编译器技术，可在 RNS-CKKS 下同时优化加密推理的尺度与自举。通过将程序的数据流图（DFG）划分为乘法深度统一为 1 的区域，ReSBM 确保尺度管理操作（SMO）与自举的放置只影响某个区域的延迟，而不影响其活出（live-out）密文的尺度与层级。我们的区域化方法以分层策略应对最优自举放置这一 NP 难问题：(1) 使用最小割实现区域内的最优 SMO 与自举放置；(2) 在由一系列区域构成的序列上进行自举引导的重缩放区域识别，最终在两个末端区域进行试探性自举；(3) 在整个 DFG 上进行最小层级自举放置，仅将密文提升至必要的最小层级。在 CPU 上对多种复杂模型的验证表明，ReSBM 不仅比一种领先方法更快地编译这些模型，而且与另一种领先方法相比，将加密推理效率平均提升 12.1%。因此，ReSBM 显著改善了大模型加密推理的实际部署，在编译速度和推理性能两方面都优于现有方法。

## 英文关键词

FHE, CKKS, RNS-CKKS, Machine Learning, Scale Management, Bootstrapping

## 中文关键词

FHE；CKKS；RNS-CKKS；机器学习；尺度管理；自举

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707276)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2025](../index.md)
