---
title: "BQSim: GPU-accelerated Batch Quantum Circuit Simulation using Decision Diagram"
description: "ASPLOS 2025 · Session 1B · BQSim：基于决策图的 GPU 加速批量量子线路模拟"
tags:
  - "ASPLOS2025"
  - "Session 1B"
  - "Quantum Computing"
---

# BQSim: GPU-accelerated Batch Quantum Circuit Simulation using Decision Diagram

**中文标题：** BQSim：基于决策图的 GPU 加速批量量子线路模拟

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shui Jiang (The Chinese University of Hong Kong ,University of Wisconsin-Madison), Yi-Hua Chung (University of Wisconsin-Madison), Chih-Chun Chang (University of Wisconsin-Madison), Tsung-Yi Ho (The Chinese University of Hong Kong), Tsung-Wei Huang (University of Wisconsin-Madison)

**单位：** The Chinese University of Hong Kong ,University of Wisconsin-Madison；University of Wisconsin-Madison；The Chinese University of Hong Kong

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715984) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Quantum circuit simulation (QCS) plays an important role in the designs and analysis of a quantum algorithm, as it assists researchers in understanding how quantum operations work without accessing expensive quantum computers. Despite many QCS methods, they are largely limited to simulating one input at a time. However, many simulation-driven quantum computing applications, such as testing and verification, require simulating multiple inputs to reason a quantum algorithm under different scenarios. We refer to this type of QCS as batch quantum circuit simulation (BQCS). In this paper, we present BQSim, a GPU-accelerated batch quantum circuit simulator. BQSim is inspired by the state-of-the-art decision diagram (DD) that can compactly represent quantum gate matrices, but overcomes its limitation of CPU-centric simulation. Specifically, BQSim uses DD to optimize a quantum circuit for reduced BQCS computation and converts DD to a GPU-efficient data structure. Additionally, BQSim employs a task graph-based execution strategy to minimize repetitive kernel call overhead and efficiently overlap kernel execution with data movement. Compared with three state-of-the-art quantum circuit simulators, cuQuantum, Qiskit Aer, and FlatDD, BQSim is 3.25×, 159.06×, and 311.42× faster on average.

## 中文摘要

量子线路模拟（QCS）在量子算法的设计与分析中发挥着重要作用，因为它能帮助研究人员在无需使用昂贵量子计算机的情况下理解量子操作的工作机制。尽管已有许多 QCS 方法，但它们在很大程度上局限于一次只模拟一个输入。然而，许多由模拟驱动的量子计算应用（例如测试与验证）需要模拟多个输入，以便在不同场景下推理量子算法。我们将这类 QCS 称为批量量子线路模拟（BQCS）。本文提出 BQSim，一个 GPU 加速的批量量子线路模拟器。BQSim 受能够紧凑表示量子门矩阵的最先进决策图（DD）启发，但克服了其以 CPU 为中心的模拟局限。具体而言，BQSim 使用 DD 优化量子线路以减少 BQCS 的计算量，并将 DD 转换为对 GPU 高效的数据结构。此外，BQSim 采用基于任务图的执行策略，以最小化重复的内核调用开销，并高效地将内核执行与数据搬运重叠。与三种最先进的量子线路模拟器 cuQuantum、Qiskit Aer 和 FlatDD 相比，BQSim 平均分别快 3.25×、159.06× 和 311.42×。

## 英文关键词

Quantum Circuit Simulation; Decision Diagram; GPU; Task Graph

## 中文关键词

量子线路模拟；决策图；GPU；任务图

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715984)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2025](../index.md)
