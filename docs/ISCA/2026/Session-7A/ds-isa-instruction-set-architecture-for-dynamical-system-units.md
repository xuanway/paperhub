---
title: "DS-ISA: Instruction Set Architecture for Dynamical System Units"
description: "ISCA 2026 · Session 7A · DS-ISA: Instruction Set Architecture for Dynamical System Units"
tags:
  - "ISCA2026"
  - "Session 7A"
  - "Emerging Technologies: Chiplet, Wafer-Scale, etc."
---

# DS-ISA: Instruction Set Architecture for Dynamical System Units

**中文标题：** DS-ISA: 面向动力系统单元的指令集架构

**所属 Session：** [Session 7A](index.md) · [ISCA 2026](../index.md)

**作者：** Chunshu Wu, Ruibing Song, Chuan Liu, Tong Geng, Ang Li

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Dynamical System Units (DSUs), leveraging CMOS-compatible electronics and natural energy evolution, represent a promising post-Moore computing paradigm with potentially 105 energy-efficiency gains. However, the absence of standardized abstraction layers severely limits their programmability and broad adoption. In this paper, we present a fundamental effort to establish the first Instruction Set Architecture (ISA) for DSUs. This is achieved by comprehensively analyzing DSU execution patterns and fundamental functional operations across various application scenarios. Our analysis identifies a unified load-lock-evolve-store execution model. Based on this model, we propose a 9-instruction ISA that provides the desired abstraction and flexibility. Building on this ISA, we propose a supporting microarchitecture for DSU control. In particular, this work introduces a new group-based execution model and a two-level masking scheme to support effective resource sharing and unique execution patterns. By providing the ISA and the supporting microarchitecture, this work lays the foundation for constructing a software stack for DSUs.

## 中文摘要

动力系统单元（DSU）借助 CMOS 兼容的电子器件与自然能量演化，代表了一种有前景的后摩尔计算范式，其能效提升潜力可达 10⁵ 倍。然而，标准化抽象层的缺失严重限制了其可编程性与广泛采用。本文提出一项基础性工作，旨在为 DSU 建立首个指令集架构（ISA）。这通过全面分析各类应用场景下的 DSU 执行模式与基本功能操作来实现。我们的分析识别出一种统一的“加载-锁定-演化-存储”（load-lock-evolve-store）执行模型。基于该模型，我们提出一个包含 9 条指令的 ISA，提供了所需的抽象与灵活性。在此 ISA 基础之上，我们提出一种用于 DSU 控制的支撑微架构。特别地，本工作引入一种新的基于组的执行模型和一种两级掩码方案，以支持有效的资源共享和独特的执行模式。通过提供 ISA 及支撑微架构，本工作为构建 DSU 的软件栈奠定了基础。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2026](../index.md)
