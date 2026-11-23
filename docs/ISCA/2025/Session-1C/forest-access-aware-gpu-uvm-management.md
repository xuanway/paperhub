---
title: "Forest: Access-aware GPU UVM Management"
description: "ISCA 2025 · Session 1C · Forest: 访问感知的GPU统一虚拟内存管理"
tags:
  - "ISCA2025"
  - "Session 1C"
  - "GPUs & Ray Tracing"
---

# Forest: Access-aware GPU UVM Management

**中文标题：** Forest: 访问感知的GPU统一虚拟内存管理

**所属 Session：** [Session 1C](index.md) · [ISCA 2025](../index.md)

**作者：** Mao Lin, Yuan Feng, Guilherme Cox, Hyeran Jeon

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731047) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

With GPU unified virtual memory (UVM), CPU and GPU can share a flat virtual address space. UVM enables the GPUs to utilize the larger CPU system memory as an expanded memory space. However, UVM’s on-demand page migration is accompanied by expensive page fault handling overhead. To mitigate such overhead, tree-based neighboring prefetcher (TBNp) has been used by GPUs. TBNp effectively reduces page faults by exploiting locality at multiple levels. However, we observe its access-pattern oblivious design leads to excessive page thrashing and unnecessary migrations. In this paper, we tackle the inefficiencies with a novel access-aware UVM management, Forest. Forest uses a software-hardware codesign to configure the optimal tree prefetchers at runtime based on each data object’s access patterns. With the heterogeneous tree-based prefetching, Forest provides 1.86×and 1.39×speedups over the baseline TBNp and state-of-the-art optimization solutions, respectively. Forest also shows a 1.51×speedup for real-world deep learning models, including CNNs and Transformers.

## 中文摘要

借助GPU统一虚拟内存（UVM），CPU与GPU可以共享扁平化虚拟地址空间。UVM允许GPU将容量更大的CPU主存作为扩展存储空间使用。但UVM的按需页迁移会带来高昂的缺页处理开销。为缓解该开销，GPU已采用基于树结构的邻域预取器（TBNp）。TBNp通过挖掘多局部性特征，能够有效减少缺页。然而我们发现，该预取器无法感知访问模式，会引发严重的页抖动与不必要的页迁移。本文提出一种全新的访问感知型UVM管理机制Forest来解决上述低效问题。Forest采用软硬件协同设计，可在运行时根据各个数据对象的访问模式，配置最优的树形预取器。依托异构树形预取策略，Forest相比基线TBNp与当前最优优化方案分别实现1.86倍和1.39倍的加速。在CNN、Transformer等真实深度学习模型上，Forest同样取得1.51倍的性能提升。

## 英文关键词

Unified Virtual Memory, Prefetching, GPU, Memory Management

## 中文关键词

统一虚拟内存, 预取, GPU, 内存管理

## 代码与研究制品

- [代码仓库](https://github.com/MoCALabUCM/forest)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731047)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1C](index.md) · [返回 ISCA 2025](../index.md)
