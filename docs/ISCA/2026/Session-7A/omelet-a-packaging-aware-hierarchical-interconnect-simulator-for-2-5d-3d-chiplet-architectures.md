---
title: "Omelet: A Packaging-Aware Hierarchical Interconnect Simulator for 2.5D/3D Chiplet Architectures"
description: "ISCA 2026 · Session 7A · Omelet: A Packaging-Aware Hierarchical Interconnect Simulator for 2.5D/3D Chiplet Architectures"
tags:
  - "ISCA2026"
  - "Session 7A"
  - "Emerging Technologies: Chiplet, Wafer-Scale, etc."
---

# Omelet: A Packaging-Aware Hierarchical Interconnect Simulator for 2.5D/3D Chiplet Architectures

**中文标题：** Omelet: 面向 2.5D/3D chiplet 架构的封装感知层次化互连仿真器

**所属 Session：** [Session 7A](index.md) · [ISCA 2026](../index.md)

**作者：** Jiho Kim, Danish Baig, Faaiq Waqar, Ashita Victor, Shimeng Yu, Muhannad Bakir, Cong Hao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Monolithic integration of SoCs is reaching practical and economic limits, motivating the transition to disaggregated chiplet-based 2.5D/3D systems. In these systems, system performance depends not only on microarchitecture, but is tightly coupled to integration decisions such as stacking, interposers, and bonding methods. These packaging decisions directly shape communication characteristics, including link latency, bandwidth, energy, and I/O density. At the same time, communication is no longer confined to a uniform on-chip network. Instead, data movement traverses multiple interconnect domains, including on-chip wires, lateral interposer links, and vertical die-to-die connections. Since each domain is implemented using different physical technologies, they exhibit distinct electrical and communication characteristics, naturally forming a hierarchical interconnect structure. However, existing simulators rely on packaging-agnostic, decoupled abstractions that fail to capture technology-specific link behavior and cross-layer interactions. This disconnect obscures integration-driven bottlenecks and limits accurate system-level design space exploration. We present Omelet, a packaging-aware hierarchical interconnect simulator for 2.5D/3D chiplet systems. The simulator integrates intra-chiplet networks (Network-on-Chip, NoC), interposer-level communication (Network-on-Interposer, NoI), and vertical tier-to-tier links (Network-on-Layer, NoL) within a unified cycle-level framework, with link parameters derived from electromagnetic extraction and compact SPICE models of advanced packaging interconnects. This unified hierarchy enables architects to evaluate how packaging technologies, network architectures, and chiplet organizations jointly influence latency, congestion, and bottleneck formation in multi-chiplet 2.5D/3D systems. Omelet, with documentation and examples, is publicly available on GitHub.

## 中文摘要

SoC 的单片集成正逼近实际与经济的极限，推动着向基于 chiplet 的分解式 2.5D/3D 系统转型。在这类系统中，系统性能不仅取决于微架构，还与堆叠、中介层和键合方法等集成决策紧密耦合。这些封装决策直接塑造通信特征，包括链路延迟、带宽、能耗和 I/O 密度。与此同时，通信不再局限于均匀的片上网络，数据移动要穿越多个互连域，包括片上布线、横向中介层链路和垂直的 die-to-die 连接。由于每个域采用不同的物理技术实现，它们表现出各自不同的电气与通信特性，自然形成一种层次化互连结构。然而，现有仿真器依赖于与封装无关、相互解耦的抽象，无法刻画特定技术的链路行为和跨层交互。这种脱节掩盖了集成驱动的瓶颈，并限制了准确的系统级设计空间探索。我们提出 Omelet，一个面向 2.5D/3D chiplet 系统、封装感知的层次化互连仿真器。该仿真器在统一的周期级框架中集成了 chiplet 内网络（片上网络，NoC）、中介层级通信（中介层网络，NoI）以及垂直层间链路（层网络，NoL），其链路参数由先进封装互连的电磁提取与紧凑 SPICE 模型导出。这一统一的层次结构使架构师能够评估封装技术、网络架构和 chiplet 组织如何共同影响多 chiplet 2.5D/3D 系统中的延迟、拥塞和瓶颈形成。Omelet 及其文档和示例已在 GitHub 上公开。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：sharc-lab/Omelet](https://github.com/sharc-lab/Omelet)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2026](../index.md)
