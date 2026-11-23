---
title: "Constant-Rate Entanglement Distillation for Fast Quantum Interconnects"
description: "ISCA 2025 · Session 3A · 面向高速量子互连的恒定速率纠缠蒸馏"
tags:
  - "ISCA2025"
  - "Session 3A"
  - "Quantum I"
---

# Constant-Rate Entanglement Distillation for Fast Quantum Interconnects

**中文标题：** 面向高速量子互连的恒定速率纠缠蒸馏

**所属 Session：** [Session 3A](index.md) · [ISCA 2025](../index.md)

**作者：** Christopher Pattison, Gefen Baranes, Juan Pablo Bonilla Ataides, Mikhail D. Lukin, Hengyun Zhou

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731069) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Distributed quantum computing allows the modular construction of large-scale quantum computers and enables new protocols for blind quantum computation. However, such applications in the large-scale, fault-tolerant regime place stringent demands on the fidelity and rate of entanglement generation, which are not met by existing methods for quantum interconnects.

In this work, we develop constant-rate entanglement distillation methods to address this bottleneck in the setting of noisy local operations. By using a sequence of two-way entanglement distillation protocols based on quantum error detecting codes with increasing rate, and combining with standard fault tolerance techniques, we achieve constant-rate entanglement distillation. We show that the scheme has constant-rate in expectation, and further numerically optimize to achieve low practical overhead under memory constraints. We find that compared to existing quantum interconnect schemes, our methods reduce the communication overhead by more than 10×in relevant regimes, leading to a direct speed-up in the execution of distributed quantum algorithms.

## 中文摘要

分布式量子计算支持模块化搭建大规模量子计算机，还能够实现盲量子计算这类新型协议。但在大规模、容错的应用场景下，这类应用对纠缠生成的保真度与速率提出严苛要求，现有量子互连方案尚无法满足。

本文在带噪声局域操作的条件下，提出恒定速率纠缠蒸馏方法，以此突破该瓶颈。我们采用一组基于量子检错码、码率逐步提升的双向纠缠蒸馏协议，并结合标准容错技术，实现恒定速率的纠缠蒸馏。我们证明该方案在期望意义上具备恒定速率特性；同时开展数值优化，在存储约束下获得较低的实际开销。研究表明，在对应场景下，相较于现有量子互连方案，本文方法可将通信开销降低10倍以上，直接加快分布式量子算法的执行速度。

## 英文关键词

Quantum Computing, Quantum Error Correction, Quantum Networking, Distributed Quantum Computing

## 中文关键词

量子计算, 量子纠错, 量子网络, 分布式量子计算

## 代码与研究制品

- [代码仓库](https://github.com/gefenbaranes/ConstantRateDistillation)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731069)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2025](../index.md)
