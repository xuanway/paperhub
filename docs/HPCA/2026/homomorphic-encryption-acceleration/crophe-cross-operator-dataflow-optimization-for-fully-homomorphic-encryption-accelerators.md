---
title: "CROPHE: Cross-Operator Dataflow Optimization for Fully Homomorphic Encryption Accelerators"
description: "HPCA 2026 · Homomorphic Encryption Acceleration"
tags:
  - "HPCA2026"
  - "Homomorphic Encryption Acceleration"
---

# CROPHE: Cross-Operator Dataflow Optimization for Fully Homomorphic Encryption Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Homomorphic Encryption Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Homomorphic Encryption Acceleration</p>
</div>

**论文链接**：
**作者**：Xinhua Chen Fudan University , Jiangbin Dong Xi'an Jiaotong University , Hongren Zheng Tsinghua University , Tian Tang Tsinghua University , Mingyu Gao Tsinghua University
**会议**：HPCA 2026

---

## 中文标题

CROPHE：面向全同态加密加速器的跨算子数据流优化

## 英文摘要

Fully homomorphic encryption (FHE) enables the protection of data privacy at the cost of significantly higher computational demands. To alleviate its memory-bound bottlenecks, dataflow optimizations that maximize on-chip data reuse and minimize off-chip accesses could be leveraged. In this work, we exploit the opportunities of cross-operator dataflow optimizations in FHE accelerators, and propose a hardware-software co-design called CROPHE. On the hardware level, instead of overly-specialized functional units, CROPHE provisions a homogeneous and unified architecture that allows for flexible resource allocation and operator mapping. On the software level, the scheduling framework of CROPHE takes a comprehensive and systematic approach to explore various spatial and temporal data pipelining and sharing schemes across multiple operators, resulting in more efficient dataflow than prior work. We also propose novel cross-operator dataflow optimizations for the unique operators in FHE including number theoretic transforms and homomorphic rotations. The evaluation shows CROPHE significantly outperforms state-of-the-art designs by 1.77× to 4.86×.

## 中文摘要

全同态加密（FHE）能够保护数据隐私，但代价是计算需求显著提高。由于 FHE 的瓶颈主要来自访存，可采用最大化片上数据复用、最小化片外访问的数据流优化来缓解。本文挖掘 FHE 加速器中跨算子数据流优化的机会，提出一种软硬件协同设计 CROPHE。在硬件层面，CROPHE 不采用过度专用的功能单元，而是提供同构且统一的架构，允许灵活的资源分配与算子映射。在软件层面，CROPHE 的调度框架采用全面而系统的方法，探索跨多个算子的多种空间与时间维度的数据流水与共享方案，从而得到比已有工作更高效的数据流。我们还针对 FHE 特有的算子（包括数论变换与同态旋转）提出新颖的跨算子数据流优化。评测表明，CROPHE 显著优于最先进设计，加速比达 1.77 倍至 4.86 倍。
