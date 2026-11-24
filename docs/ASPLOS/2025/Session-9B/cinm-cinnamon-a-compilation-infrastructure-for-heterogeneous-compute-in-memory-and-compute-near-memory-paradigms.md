---
title: "CINM (Cinnamon): A Compilation Infrastructure for Heterogeneous Compute In-Memory and Compute Near-Memory Paradigms"
description: "ASPLOS 2025 · Session 9B · CINM（Cinnamon）：面向异构存内计算与近存计算范式的编译基础设施"
tags:
  - "ASPLOS2025"
  - "Session 9B"
  - "Processing in Memory"
---

# CINM (Cinnamon): A Compilation Infrastructure for Heterogeneous Compute In-Memory and Compute Near-Memory Paradigms

**中文标题：** CINM（Cinnamon）：面向异构存内计算与近存计算范式的编译基础设施

**所属 Session：** [Session 9B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Asif Ali Khan (Technische Universität Dresden), Hamid Farzaneh (Technische Universität Dresden), Karl Friedrich Alexander Friebel (Technische Universität Dresden), Clément Fournier (Technische Universität Dresden), Lorenzo Chelini (Intel), Jeronimo Castrillon (Technische Universität Dresden)

**单位：** Technische Universität Dresden；Intel

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674189) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The rise of data-intensive applications exposed the limitations of conventional processor-centric von-Neumann architectures that struggle to meet the off-chip memory bandwidth demand. Therefore, recent innovations in computer architecture advocate compute-in-memory (CIM) and compute-near-memory (CNM), non-von-Neumann paradigms achieving orders-ofmagnitude improvements in performance and energy consumption. Despite significant technological breakthroughs in the last few years, the programmability of these systems is still a serious challenge. Their programming models are too low-level and specific to particular system implementations. Since such future architectures are predicted to be highly heterogeneous, developing novel compiler abstractions and frameworks becomes necessary. To this end, we present CINM (Cinnamon), a first end-to-end compilation flow that leverages the hierarchical abstractions to generalize over different CIM and CNM devices and enable device-agnostic and deviceaware optimizations. Cinnamon progressively lowers input programs and performs optimizations at each level in the lowering pipeline. To show its efficacy, we evaluate CINM on a set of benchmarks for a real CNM system (UPMEM) and the memristors-based CIM accelerators. We show that Cinnamon, supporting multiple hardware targets, generates high-performance code comparable to or better than state-ofthe-art implementations.

## 中文摘要

数据密集型应用的兴起暴露了传统以处理器为中心的冯·诺依曼架构的局限——它们难以满足片外内存带宽需求。因此，近期计算机体系结构的创新倡导存内计算（CIM）与近存计算（CNM）这类非冯·诺依曼范式，在性能与能耗上取得数量级的提升。尽管过去几年取得了重大的技术突破，这些系统的可编程性仍是严峻挑战：其编程模型过于底层，且与特定系统实现紧密绑定。由于此类未来架构预计将高度异构，开发新颖的编译抽象与框架变得十分必要。为此，我们提出 CINM（Cinnamon），这是首个端到端编译流程，它利用层次化抽象对不同 CIM 与 CNM 设备进行泛化，并支持设备无关（device-agnostic）与设备感知（device-aware）的优化。Cinnamon 逐步降低（lower）输入程序，并在降低流水线的每一层执行优化。为展示其有效性，我们在面向真实 CNM 系统（UPMEM）与基于忆阻器的 CIM 加速器的一组基准测试上评估 CINM。结果表明，Cinnamon 支持多个硬件目标，能够生成与最先进实现相当或更优的高性能代码。

## 英文关键词

Hardware Emerging architectures, Hardware Emerging tools and methodologies, Hardware Emerging languages and compilers, Computing methodologies Parallel computing methodologies

## 中文关键词

硬件新兴架构；硬件新兴工具与方法；硬件新兴语言与编译器；计算方略：并行计算方略

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674189)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9B](index.md) · [返回 ASPLOS 2025](../index.md)
