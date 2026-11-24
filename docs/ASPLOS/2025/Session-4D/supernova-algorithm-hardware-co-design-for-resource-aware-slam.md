---
title: "SuperNoVA: Algorithm-Hardware Co-Design for Resource-Aware SLAM"
description: "ASPLOS 2025 · Session 4D · SuperNoVA：面向资源感知 SLAM 的算法-硬件协同设计"
tags:
  - "ASPLOS2025"
  - "Session 4D"
  - "Autonomous Systems"
---

# SuperNoVA: Algorithm-Hardware Co-Design for Resource-Aware SLAM

**中文标题：** SuperNoVA：面向资源感知 SLAM 的算法-硬件协同设计

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Seah Kim (University of California, Berkeley), Roger Hsiao (University of California, Berkeley), Borivoje Nikolić (University of California, Berkeley), James Demmel (University of California, Berkeley), Yakun Sophia Shao (University of California, Berkeley)

**单位：** University of California, Berkeley

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707258) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Simultaneous Localization and Mapping (SLAM) plays a crucial role in robotics, autonomous systems, and augmented and virtual reality (AR/VR) applications by enabling devices to understand and map unknown environments. However, deploying SLAM in AR/VR applications poses significant challenges, including the demand for high accuracy, real-time processing, and efficient resource utilization, especially on compact and lightweight devices. To address these challenges, we propose SuperNoVA, which enables highaccuracy, real-time, large-scale SLAM in resource-constrained settings through a full-stack system, spanning from algorithm to hardware. In particular, SuperNoVA dynamically constructs a subgraph to meet the latency target while preserving accuracy, virtualizes hardware resources for efficient graph processing, and implements a novel hardware architecture to accelerate the SLAM backend efficiently. Evaluation results demonstrate that, for a large-scale AR dataset, SuperNoVA reduces full SLAM backend computation latency by 89.5% compared to the baseline out-of-order CPU and 78.6% compared to the baseline embedded GPU, and reduces the maximum pose error by 89% over existing SLAM solutions, while always meeting the latency target.

## 中文摘要

同步定位与建图（SLAM）通过使设备理解并构建未知环境的地图，在机器人、自主系统以及增强现实与虚拟现实（AR/VR）应用中发挥着关键作用。然而，在 AR/VR 应用中部署 SLAM 面临显著挑战，包括对高精度、实时处理和高效资源利用的需求，在紧凑轻量设备上尤为突出。为应对这些挑战，我们提出 SuperNoVA，它通过从算法到硬件的全栈系统，在资源受限环境中实现高精度、实时、大规模的 SLAM。具体而言，SuperNoVA 动态构建子图以在保持精度的同时满足时延目标，虚拟化硬件资源以实现高效的图处理，并实现一种新颖的硬件架构来高效加速 SLAM 后端。评估结果表明，在大规模 AR 数据集上，SuperNoVA 相比基线乱序 CPU 将完整 SLAM 后端计算时延降低 89.5%，相比基线嵌入式 GPU 降低 78.6%，相比现有 SLAM 方案将最大位姿误差降低 89%，同时始终满足时延目标。

## 英文关键词

AR/VR, Robotics, SLAM, Accelerator, AlgorithmHardware Co-Design, Resource Management

## 中文关键词

AR/VR；机器人；SLAM；加速器；算法-硬件协同设计；资源管理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707258)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4D](index.md) · [返回 ASPLOS 2025](../index.md)
