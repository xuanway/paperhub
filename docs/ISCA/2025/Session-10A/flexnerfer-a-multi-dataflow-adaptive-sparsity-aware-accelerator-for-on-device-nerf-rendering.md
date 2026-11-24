---
title: "FlexNeRFer: A Multi-Dataflow, Adaptive Sparsity-Aware Accelerator for On-Device NeRF Rendering"
description: "ISCA 2025 · Session 10A · FlexNeRFer：面向设备端 NeRF 渲染的多数据流自适应稀疏感知加速器"
tags:
  - "ISCA2025"
  - "Session 10A"
  - "ML Accelerators IV"
---

# FlexNeRFer: A Multi-Dataflow, Adaptive Sparsity-Aware Accelerator for On-Device NeRF Rendering

**中文标题：** FlexNeRFer：面向设备端 NeRF 渲染的多数据流自适应稀疏感知加速器

**所属 Session：** [Session 10A](index.md) · [ISCA 2025](../index.md)

**作者：** Seock-Hwan Noh, Banseok Shin, Jeik Choi, Seungpyo Lee, Jaeha Kung, Yeseong Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731107) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Neural Radiance Fields (NeRF), an AI-driven approach for 3D view reconstruction, has demonstrated impressive performance, spark- ing active research across fields. As a result, a range of advanced NeRF models has emerged, leading on-device applications to in- creasingly adopt NeRF for highly realistic scene reconstructions. With the advent of diverse NeRF models, NeRF-based applications leverage a variety of NeRF frameworks, creating the need for hard- ware capable of efficiently supporting these models. However, GPUs fail to meet the performance, power, and area (PPA) cost demanded by these on-device applications, or are specialized for specific NeRF algorithms, resulting in lower efficiency when applied to other NeRF models. To address this limitation, in this work, we introduce FlexNeRFer, an energy-efficient versatile NeRF accelerator. The key components enabling the enhancement of FlexNeRFer include: i) a flexible network-on-chip (NoC) supporting multi-dataflow and sparsity on precision-scalable MAC array, and ii) efficient data stor- age using an optimal sparsity format based on the sparsity ratio and precision modes. To evaluate the effectiveness of FlexNeRFer, we performed a layout implementation using 28nm CMOS technol- ogy. Our evaluation shows that FlexNeRFer achieves 8.2∼243.3× speedup and 24.1∼520.3×improvement in energy efficiency over a GPU (i.e., NVIDIA RTX 2080 Ti), while demonstrating 4.2∼86.9× speedup and 2.3∼47.5×improvement in energy efficiency compared to a state-of-the-art NeRF accelerator (i.e., NeuRex).

## 中文摘要

神经辐射场（NeRF）是一种基于AI的三维视图重建方法，表现效果优异，催生了大量跨领域研究。目前已经涌现出多种进阶NeRF模型，端侧应用也越来越多地采用NeRF实现高真实感场景重建。
随着NeRF模型样，各类NeRF应用使用不同框架，这就要求硬件能够高效兼容多种模型。但GPU难以满足端侧应用对性能、功耗、面积（PPA）的约束；而现有的NeRF专用加速器大多针对某一种算法定制，迁移到其他NeRF模型时效率会大幅下降。针对该问题，本文提出FlexNeRFer，一款高能效、通用性强的NeRF加速器。

FlexNeRFer的核心创新包括两点：1）灵活片上网络（NoC），支持多数据流，配合精度可缩放的MAC阵列处理稀疏数据；2）根据稀疏率与精度模式选择最优稀疏编码格式，实现高效数据存储。

本文基于28nm CMOS工艺完成版图实现以验证FlexNeRFer。评测结果显示：相比NVIDIA RTX 2080 Ti GPU，FlexNeRFer提速8.2～243.3倍，能效提升24.1～520.3倍；对比前沿NeRF加速器NeuRex，提速4.2～86.9倍，能效提升2.3～47.5倍。

## 英文关键词

NeRF, On-Device NeRF Acceleration, Multi-Dataflow, Sparsity For- mat, Flexible Network-on-Chip, Bit-Scalable MAC Array

## 中文关键词

神经辐射场, 端侧NeRF加速, 多数据流, 稀疏格式, 灵活片上网络, 位宽可缩放乘累加阵列

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731107)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2025](../index.md)
