---
title: "HYTE: Flexible Tiling for Sparse Accelerators via Hybrid Static-Dynamic Approaches"
description: "ISCA 2025 · Session 8C · HYTE：通过静态—动态混合方法为稀疏加速器实现灵活分块"
tags:
  - "ISCA2025"
  - "Session 8C"
  - "Domain Specific Accelerators II"
---

# HYTE: Flexible Tiling for Sparse Accelerators via Hybrid Static-Dynamic Approaches

**中文标题：** HYTE：通过静态—动态混合方法为稀疏加速器实现灵活分块

**所属 Session：** [Session 8C](index.md) · [ISCA 2025](../index.md)

**作者：** Xintong Li, Zhiyao Li, Mingyu Gao

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731044) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Specialized hardware accelerators are widely used for sparse ten- sor computations. For very large tensors that do not fit in on-chip buffers, tiling is a promising solution to improve data reuse on these sparse accelerators. Nevertheless, existing tiling strategies on sparse accelerators are either purely dynamic and suffering from high design complexity, or purely static and using simple heuristics with insufficient adaptivity. In addition, they have not extensively explored the full design space of tiling to identify the optimal schemes, nor have they supported efficient management of the non-negligible metadata needed for tiling. We propose HYTE, a hybrid static-dynamic framework to enable flexible and efficient tiling on sparse accelerators. HYTE relies on a static offline sched- uler to first identify a near-optimal initial tiling scheme through effective and lightweight sampling. The tile size and shape, the dimension iteration order across different tiles, and the buffer allo- cation policies can all be flexibly configured to adapt to the specific data sparsity patterns. Then at runtime, HYTE supports efficient management of the tiling metadata in both the off-chip memory and the on-chip buffer, as well as a technique of dynamic tuning on the tile shape to ensure high buffer utilization in the presence of highly varying local data patterns. Our evaluation shows that HYTE outperforms state-of-the-art sparse tiling strategies by 3.3× to 6.2×on average for diverse sparse matrices.

## 中文摘要

专用硬件加速器已广泛用于稀疏张量计算。当张量规模过大、无法全部放入片上缓存时，分块（tiling）是提升稀疏加速器数据复用率的有效手段。然而现有稀疏加速器分块策略要么是纯动态方案，设计复杂度很高；要么是纯静态方案，依赖简单启发式规则，自适应能力不足。此外，这些方案没有充分遍历分块设计空间以寻找最优策略，也缺少对分块所需元数据的高效管理机制。

本文提出HYTE，一种静态-动态混合框架，在稀疏加速器上实现灵活、高效的分块。HYTE先由离线静态调度器，通过轻量采样得到接近最优的初始分块方案；分块尺寸、分块形状、跨块维度迭代顺序以及缓存分配策略均可灵活配置，适配不同的数据稀疏模式。运行时，HYTE支持片外存储与片上缓存中分块元数据的高效管理，同时采用分块形状动态调优技术，在局部数据模式剧烈变化时保持较高缓存利用率。评测结果表明：在多种稀疏矩阵负载上，HYTE相比前沿稀疏分块策略，平均性能提升3.3–6.2倍。

## 英文关键词

sparse tensor algebra, hardware acceleration, tiling

## 中文关键词

稀疏张量代数, 硬件加速, 分块

## 代码与研究制品

- [代码仓库](https://github.com/tsinghua-ideal/HYTE-sim)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731044)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8C](index.md) · [返回 ISCA 2025](../index.md)
