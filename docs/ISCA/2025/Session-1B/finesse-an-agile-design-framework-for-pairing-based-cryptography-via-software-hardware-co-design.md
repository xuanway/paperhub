---
title: "Finesse: An Agile Design Framework for Pairing-based Cryptography via Software/Hardware Co-Design"
description: "ISCA 2025 · Session 1B · Finesse: 配对密码软硬件协同设计框架"
tags:
  - "ISCA2025"
  - "Session 1B"
  - "Crypto & Fully Homomorphic Encryption"
---

# Finesse: An Agile Design Framework for Pairing-based Cryptography via Software/Hardware Co-Design

**中文标题：** Finesse: 配对密码软硬件协同设计框架

**所属 Session：** [Session 1B](index.md) · [ISCA 2025](../index.md)

**作者：** Tianwei Pan, Tianao Dai, Jianlei Yang, Hongbin Jing, Yang Su, Zeyu Hao, Xiaotao Jia, Chunming Hu, Weisheng Zhao

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731033) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Pairing-based cryptography (PBC) is crucial in modern cryptographic applications. With the rapid advancement of adversarial research and the growing diversity of application requirements, PBC accelerators need regular updates in algorithms, parameter configurations, and hardware design. However, traditional design methodologies face significant challenges, including prolonged design cycles, difficulties in balancing performance and flexibility, and insufficient support for potential architectural exploration.

To address these challenges, we introduce Finesse, an agile design framework based on co-design methodology. Finesse leverages a co-optimization cycle driven by a specialized compiler and a multi-granularity hardware simulator, enabling both optimized performance metrics and effective design space exploration. Furthermore, Finesse adopts a modular design flow to significantly shorten design cycles, while its versatile abstraction ensures flexibility across various curve families and hardware architectures.

Finesse offers flexibility, efficiency, and rapid prototyping, comparing with previous frameworks. With compilation times reduced to minutes, Finesse enables faster iteration cycles and streamlined hardware-software co-design. Experiments on popular curves demonstrate its effectiveness, achieving 34×improvement in throughput and 6.2×increase in area efficiency compared to previous flexible frameworks, while outperforming state-of-the-art non-flexible ASIC designs with a 3×gain in throughput and 3.2×improvement in area efficiency.

## 中文摘要

基于配对的密码学（PBC）在现代密码应用中至关重要。随着攻击研究快速发展以及应用需求日趋多样化，PBC加速器需要在算法、参数配置与硬件设计上持续迭代更新。然而传统设计方法面临诸多难题：设计周期漫长、性能与灵活性难以兼顾，同时对架构探索的支撑能力不足。

为解决上述问题，本文提出Finesse——一套基于协同设计思想的敏捷设计框架。Finesse依托专用编译器与多粒度硬件模拟器驱动的协同优化环路，既能获得最优性能指标，又可以高效开展设计空间探索。此外，Finesse采用模块化设计流程，大幅缩短设计周期；其通用抽象层可适配多种椭圆曲线簇与硬件架构，具备良好灵活性。

相较于现有框架，Finesse兼顾灵活性、执行效率与快速原型能力。它将编译耗时压缩至分钟级，支持更快的迭代周期与轻量化软硬件协同设计。在主流椭圆曲线上的实验验证了该框架的有效性：对比以往柔性框架，吞吐量提升34倍，面积效率提升6.2倍；同时相较于当前最优的非柔性ASIC设计，吞吐量提升3倍，面积效率提升3.2倍。

## 英文关键词

Agile design framework, pairing-based cryptography, hardware accelerator, software/hardware co-design

## 中文关键词

敏捷设计框架, 基于配对的密码学, 硬件加速器, 软硬件协同设计

## 代码与研究制品

- [代码仓库](https://github.com/BUAA-CI-LAB/Finesse)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731033)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1B](index.md) · [返回 ISCA 2025](../index.md)
