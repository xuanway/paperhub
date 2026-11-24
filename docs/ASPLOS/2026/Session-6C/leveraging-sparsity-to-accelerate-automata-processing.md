---
title: "Leveraging Sparsity to Accelerate Automata Processing"
description: "ASPLOS 2026 · Session 6C · 利用稀疏性加速自动机处理"
tags:
  - "ASPLOS2026"
  - "Session 6C"
  - "Graph & Sparse Computing"
---

# Leveraging Sparsity to Accelerate Automata Processing

**中文标题：** 利用稀疏性加速自动机处理

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xingran Du (MIT), Joel S. Emer (MIT/NVIDIA), Daniel Sanchez (MIT)

**单位：** MIT；MIT/NVIDIA

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736126) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

**出版标题：** Hopps: Leveraging Sparsity to Accelerate Automata Processing

## 英文摘要

Automata processing (AP) is a key kernel in data analytics and scientific computing. AP workloads process a stream of symbols with many automata (FSMs) in parallel, e.g., pattern-matching network traffic against many malicious strings. The need for high-performance AP has sparked the design of specialized accelerators. But prior AP accelerators are inefficient: AP workloads have substantial sparsity, but accelerators exploit no or limited sparsity. Specifically, each AP workload can be expressed as the concurrent traversal of all automata, which are encoded as graphs. But state-of-the-art accelerators store these graphs uncompressed, using bitsets. This allows the use of specialized memory crossbars that provide high parallelism and efficiency when graphs are dense. But many graphs are highly sparse, making crossbar-based accelerators inefficient. We present Hopps, the first automata processing accelerator that exploits sparse data representations. Hopps combines two types of processing units: one represents data uncompressed, which achieves high throughput but is space-inefficient, while the other uses a compressed-sparse representation, which achieves high space efficiency but lower and more variable throughput. To use Hopps well, we present a novel automata mapping algorithm that maps most work to high-throughput units, while keeping a large fraction of state in space-efficient units. Hopps's hybrid design relaxes several constraints in crossbar-based designs, allowing for more efficient high-throughput units (e.g., by using a large number of smaller crossbars). Thus, by making the uncommon case cheap, Hopps makes the common case even faster. We evaluate Hopps on AutomataZoo [44] benchmarks. Hopps outperforms prior state-of-the-art accelerators Impala and SpAP by gmean 2.5× and 2.2× when using equal area.

## 中文摘要

自动机处理（AP）是数据分析与科学计算中的一个关键内核。AP 工作负载用大量自动机（FSM）并行处理符号流，例如将网络流量与大量恶意字符串进行模式匹配。对高性能 AP 的需求催生了专用加速器的设计。但以往的 AP 加速器效率低下：AP 工作负载具有显著的稀疏性，而加速器却未利用或仅有限地利用这种稀疏性。具体而言，每个 AP 工作负载都可以表示为对所有自动机的并发遍历，而这些自动机被编码为图。但最先进的加速器使用位集（bitset）以未压缩的方式存储这些图，这使得可以采用专用内存交叉开关（crossbar），在图稠密时提供高并行性与高效率。然而许多图高度稀疏，使得基于交叉开关的加速器效率低下。我们提出 Hopps，首个利用稀疏数据表示的自动机处理加速器。Hopps 结合两类处理单元：一类以未压缩方式表示数据，可获得高吞吐但空间效率低；另一类使用压缩稀疏表示，可获得高空间效率但吞吐较低且波动更大。为用好 Hopps，我们提出一种新颖的自动机映射算法，将大部分工作映射到高吞吐单元，同时将很大一部分状态保留在空间高效的单元中。Hopps 的混合设计放宽了基于交叉开关设计中的若干约束，使高吞吐单元可以更高效（例如通过使用大量较小的交叉开关）。因此，通过让不常见的情形变得廉价，Hopps 让常见情形变得更快。我们在 AutomataZoo [44] 基准上评估 Hopps。在相同面积下，Hopps 相比此前最先进的加速器 Impala 与 SpAP 分别取得 gmean 2.5 倍与 2.2 倍的提升。

## 英文关键词

Sparsity; Accelerators; Automata Processing

## 中文关键词

稀疏性；加速器；自动机处理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736126)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。
> 论文集印刷标题：「Hopps: Leveraging Sparsity to Accelerate Automata Processing」。

[返回 Session 6C](index.md) · [返回 ASPLOS 2026](../index.md)
