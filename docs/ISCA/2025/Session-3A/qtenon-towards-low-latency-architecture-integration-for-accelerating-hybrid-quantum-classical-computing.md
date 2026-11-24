---
title: "Qtenon: Towards Low-Latency Architecture Integration for Accelerating Hybrid Quantum-Classical Computing"
description: "ISCA 2025 · Session 3A · Qtenon: 低延迟架构集成加速混合量子-经典计算"
tags:
  - "ISCA2025"
  - "Session 3A"
  - "Quantum I"
---

# Qtenon: Towards Low-Latency Architecture Integration for Accelerating Hybrid Quantum-Classical Computing

**中文标题：** Qtenon: 低延迟架构集成加速混合量子-经典计算

**所属 Session：** [Session 3A](index.md) · [ISCA 2025](../index.md)

**作者：** Chenning Tao, Liqiang Lu, Size Zheng, Li-Wen Chang, Minghua Shen, Hanyu Zhang, Fangxin Liu, Kaiwen Zhou, Jianwei Yin

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731087) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Hybrid quantum-classical algorithms have shown great promise in
leveraging the computational potential of quantum systems. How-
ever, the efficiency of these algorithms is severely constrained by
the limitations of current quantum hardware architectures. These
architectures, which typically feature a decoupled design, lack both
hardware support for low-latency communication and software
support for fine-grained optimization.

In this paper, we propose Qtenon, a tightly coupled system for
efficient hybrid quantum-classical algorithm acceleration. Qtenon
is composed of both hardware part and software part. To enable
efficient communication and computation, the hardware part pro-
vides a unified memory hierarchy, an efficient quantum controller,
as well as a multi-stage processing pipeline. The unified memory
hierarchy functions as a communication buffer between host and
quantum accelerators, with dedicated data paths and interfaces pro-
vided by the quantum controller. The multi-stage pipeline leverages
hardware pipelines to fully exploit parallelism. To program hybrid
quantum-classical algorithms on the hardware, our software part
provides a set of instructions for data communication and compu-
tation. The instructions also enable fine-grained synchronization
and efficient scheduling for quantum-host interaction. We design
Qtenon as a RISC-V extended chip and implement it using Chisel. In
evaluation, we achieve up to 14.9×end-to-end speedup compared
to state-of-the-art work for hybrid quantum-classical algorithms.

## 中文摘要

混合量子-经典算法在挖掘量子系统计算潜力方面展现出巨大前景。然而，这类算法的执行效率受到当前量子硬件架构的严重制约。现有架构大多采用解耦设计，既缺少低延迟通信的硬件支撑，也缺少细粒度优化的软件支持。

本文提出Qtenon，一款用于高效加速混合量子-经典算法的紧耦合系统。Qtenon由硬件与软件两部分组成。为实现高效通信与计算，硬件层提供统一存储层次结构、高性能量子控制器以及多级处理流水线。统一存储层次充当主机与量子加速器之间的通信缓冲区，由量子控制器提供专用数据通路与接口；多级流水线依托硬件流水线充分挖掘并行性。为在该硬件上编写混合量子-经典算法，软件层提供一套面向数据通信与计算的指令集。这些指令同时支持细粒度同步，实现量子端与主机之间的高效调度。我们将Qtenon设计为RISC-V扩展芯片，并基于Chisel实现。评测结果表明，针对混合量子-经典算法，相比前沿工作，本系统最高可实现14.9倍端到端加速。

## 英文关键词

Quantum computing, Instruction set architecture (ISA), Quantum-classical hybrid computing, RISC-V

## 中文关键词

量子计算, 指令集架构, 量子经典混合计算, RISC-V

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731087)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2025](../index.md)
