---
title: "Accurate & Scalable Time-Based Sampling of Full-System Simulation"
description: "MICRO 2026 · Session 3B · 精确且可扩展的全系统仿真时间采样"
tags:
  - "MICRO2026"
  - "Simulation"
---

# Accurate & Scalable Time-Based Sampling of Full-System Simulation

**中文标题：** 精确且可扩展的全系统仿真时间采样

**所属 Session：** [Session 3B](index.md) · [MICRO 2026](../index.md)

**作者：** Shanqing Lin, Yuanlong Li, Mohammad Alian, Babak Falsafi, Konrad Lai

**来源：** MICRO 2026，pp. 1006–1020；[DOI](https://doi.org/10.1109/MICRO67795.2026.00080)

## 英文摘要

Full-system timing simulation is essential for computer system design, spanning platforms from mobile devices to servers. However, simulating even a few seconds of execution remains impractical due to timing simulators' extremely slow speed. Instead, designers often resort to higher-level models or significantly shorten measurement windows, which often result in inconclusive design decisions. Time-based sampling has been shown to reduce measurement requirements in timing simulation by several orders of magnitude while providing bounded error with statistical confidence. When applying time-based sampling to full-system timing simulation, a key challenge is accurate and rapid reconstruction of architectural and microarchitectural state between measurement intervals, particularly for server workloads exhibiting highly variable performance—whether within a single tier, across multiple tiers, or in consolidated environments. In this paper, we present Chronos, an end-to-end checkpointed sampling framework for full-system timing simulation. Chronos leverages a linear regression model for timekeeping in functional simulation to reduce bias in reconstructed checkpoint state and employs a parallel functional simulator to regenerate system state at speeds that scale with the number of host cores.

## 中文摘要

全系统时序仿真对于计算机系统设计至关重要，涵盖从移动设备到服务器的平台。然而，由于时序模拟器的速度极慢，即使模拟几秒钟的执行仍然是不切实际的。相反，设计人员经常求助于更高级别的模型或显着缩短测量窗口，这通常会导致不确定的设计决策。基于时间的采样已被证明可以将时序仿真中的测量要求降低几个数量级，同时提供具有统计置信度的有限误差。将基于时间的采样应用于全系统时序仿真时，一个关键挑战是在测量间隔之间准确、快速地重建架构和微架构状态，特别是对于表现出高度可变性能的服务器工作负载——无论是在单层内、跨多个层还是在整合环境中。在本文中，我们提出了 Chronos，一种用于全系统时序仿真的端到端检查点采样框架。 Chronos 利用线性回归模型在功能模拟中进行计时，以减少重建检查点状态中的偏差，并采用并行功能模拟器以随主机内核数量扩展的速度重新生成系统状态。

## 中文关键词

全系统仿真；周期精确仿真；统计采样；并行仿真

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3B](index.md) · [MICRO 2026 主页](../index.md)
