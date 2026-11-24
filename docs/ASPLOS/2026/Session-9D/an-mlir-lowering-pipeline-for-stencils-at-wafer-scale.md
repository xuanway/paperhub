---
title: "An MLIR Lowering Pipeline for Stencils at Wafer-Scale"
description: "ASPLOS 2026 · Session 9D · 面向晶圆级 Stencil 计算的 MLIR 降级流水线"
tags:
  - "ASPLOS2026"
  - "Session 9D"
  - "Network & Cloud Infrastructure"
---

# An MLIR Lowering Pipeline for Stencils at Wafer-Scale

**中文标题：** 面向晶圆级 Stencil 计算的 MLIR 降级流水线

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Nicolai Stawinoga (Technische Universität Berlin), David Katz (University of Edinburgh), Anton Lydike (University of Edinburgh), Justs Zarins (University of Edinburgh), Nick Brown (University of Edinburgh), George Bisbas (Imperial College London), Tobias Grosser (University of Cambridge)

**单位：** Technische Universität Berlin；University of Edinburgh；Imperial College London；University of Cambridge

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790124) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The Cerebras Wafer-Scale Engine (WSE) delivers performance at an unprecedented scale of over 900,000 compute units, all connected via a single-wafer on-chip interconnect. Initially designed for AI, the WSE architecture is also well-suited for High Performance Computing (HPC). However, its distributed asynchronous programming model diverges significantly from the simple sequential or bulk-synchronous programs that one would typically derive for a given mathematical program description. Targeting the WSE requires a bespoke re-implementation when porting existing code. The absence of WSE support in compilers such as MLIR, meant that there was little hope for automating this process. 

Stencils are ubiquitous in HPC, and in this paper we explore the hypothesis that domain specific information about  stencils can be leveraged by the compiler to automatically target the WSE without requiring application-level code changes. We present a compiler pipeline that transforms stencil-based kernels into highly optimized CSL code for the WSE, bridging the semantic gap between the mathematical representation of the problem and the WSE's asynchronous execution model. Based upon five benchmarks across three HPC programming technologies, running on both the Cerebras WSE2 and WSE3, our approach delivers comparable, if not slightly better, performance than manually optimized code. Furthermore, without requiring any application level code changes, performance on the WSE3 is around 14× faster than 128 Nvidia A100 GPUs and 20× faster than 128 nodes of a CPU-based Cray-EX supercomputer when using our approach.

## 中文摘要

Cerebras Wafer-Scale Engine（WSE）以超过 900,000 个计算单元的前所未有的规模提供性能，这些计算单元全部通过单一晶圆的片上互连相连。WSE 架构最初为 AI 设计，同时也非常适合高性能计算（HPC）。然而，其分布式异步编程模型与人们通常会针对给定数学问题描述推导出的简单顺序程序或批量同步程序存在显著差异。以 WSE 为目标意味着在移植现有代码时需要专门重新实现。由于 MLIR 等编译器缺乏对 WSE 的支持，自动化这一过程曾几乎没有希望。

Stencil 在 HPC 中无处不在，本文探索这样一个假设：关于 stencil 的领域特定信息可以被编译器利用，从而在无需修改应用级代码的情况下自动以 WSE 为目标。我们提出一条编译器流水线，将基于 stencil 的 kernel 转换为面向 WSE 的高度优化的 CSL 代码，弥合问题的数学表示与 WSE 异步执行模型之间的语义鸿沟。基于横跨三种 HPC 编程技术的五个基准测试，并在 Cerebras WSE2 与 WSE3 上运行，我们的方法取得了与手工优化代码相当、甚至略优的性能。此外，在无需任何应用级代码修改的情况下，使用我们的方法在 WSE3 上的性能比 128 块 Nvidia A100 GPU 快约 14×，比 128 个节点的基于 CPU 的 Cray-EX 超级计算机快约 20×。

## 英文关键词

Cerebras, Wafer Scale Engine, domain-specific languages, intermediate representations, stencil computations, MLIR, xDSL

## 中文关键词

Cerebras；Wafer Scale Engine；领域特定语言；中间表示；stencil 计算；MLIR；xDSL

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790124)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9D](index.md) · [返回 ASPLOS 2026](../index.md)
