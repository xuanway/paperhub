---
title: "Enhancing CGRA Efficiency Through Aligned Compute and Communication Provisioning"
description: "ASPLOS 2025 · Session 2C · 通过对齐计算与通信供给提升 CGRA 效率"
tags:
  - "ASPLOS2025"
  - "Session 2C"
  - "Accelerators"
---

# Enhancing CGRA Efficiency Through Aligned Compute and Communication Provisioning

**中文标题：** 通过对齐计算与通信供给提升 CGRA 效率

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zhaoying Li (National University of Singapore), Pranav Dangi (National University of Singapore), Chenyang Yin (Peking University), Thilini Kaushalya Bandara (National University of Singapore), Rohan Juneja (National University of Singapore), Cheng Tan (Google), Zhenyu Bai (National University of Singapore), Tulika Mitra (National University of Singapore)

**单位：** National University of Singapore；Peking University；Google

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707230) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Coarse-grained Reconfigurable Arrays (CGRAs) are domainagnostic accelerators that enhance the energy efficiency of resource-constrained edge devices. The CGRA landscape is diverse, exhibiting trade-offs between performance, efficiency, and architectural specialization. However, CGRAs often overprovision communication resources relative to their modest computing capabilities. This occurs because the theoretically provisioned programmability for CGRAs often proves superfluous in practical implementations. In this paper, we propose Plaid, a novel CGRA architecture and compiler that aligns compute and communication capabilities, thereby significantly improving energy and area efficiency while preserving its generality and performance. We demonstrate that the dataflow graph, representing the target application, can be decomposed into smaller, recurring communication patterns called motifs. The primary contribution is the identification of these structural motifs within the dataflow graphs and the development of an efficient collective execution and routing strategy tailored to these motifs. The Plaid architecture employs a novel collective processing unit that can execute multiple operations of a motif and route related data dependencies together. The Plaid compiler can hierarchically map the dataflow graph and judiciously schedule the motifs. Our design achieves a 43% reduction 0 License. ared to the baseline high-performance spatio-temporal CGRA, all while preserving its generality and performance levels. In comparison to the baseline energy-efficient spatial CGRA, Plaid offers a 1.4× performance improvement and a 48% area savings, with almost the same power.

## 中文摘要

粗粒度可重构阵列（CGRA）是与领域无关的加速器，可提升资源受限边缘设备的能效。CGRA 的设计空间十分多样，在性能、效率与架构专用化之间呈现出不同权衡。然而，CGRA 往往相对于其有限的算力而过度供给通信资源。这是因为 CGRA 理论上供给的可编程性在实际实现中常常显得多余。本文提出 Plaid，一种新颖的 CGRA 架构与编译器，它对计算能力与通信能力进行对齐，从而在保持通用性与性能的同时显著提升能效与面积效率。我们证明，表示目标应用的数据流图可以分解为更小、重复出现的通信模式，称为 motif。本文的主要贡献是识别数据流图中的这些结构性 motif，并针对这些 motif 开发高效的集合执行与路由策略。Plaid 架构采用新颖的集合处理单元，可以执行一个 motif 的多个操作，并将相关的数据依赖一起路由。Plaid 编译器可以层次化地映射数据流图，并对这些 motif 进行合理调度。与基线的高性能时空 CGRA 相比，我们的设计实现了 43% 的降低，同时保持其通用性与性能水平。与基线的节能型空间 CGRA 相比，Plaid 提供 1.4× 的性能提升和 48% 的面积节省，功耗几乎相同。

## 英文关键词

Dataflow computing, Coarse-Grained Reconfigurable Array (CGRA), Motifs

## 中文关键词

数据流计算；粗粒度可重构阵列（CGRA）；Motif

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707230)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2025](../index.md)
