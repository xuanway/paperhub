---
title: "Composing Distributed Computations Through Task and Kernel Fusion"
description: "ASPLOS 2025 · Session 2B · 通过任务融合与内核融合组合分布式计算"
tags:
  - "ASPLOS2025"
  - "Session 2B"
  - "Distributed Computing"
---

# Composing Distributed Computations Through Task and Kernel Fusion

**中文标题：** 通过任务融合与内核融合组合分布式计算

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Rohan Yadav (Stanford University), Shiv Sundram (Stanford University), Wonchan Lee (NVIDIA), Michael Garland (NVIDIA), Michael Bauer (NVIDIA), Alex Aiken (Stanford University), Fredrik Kjolstad (Stanford University)

**单位：** Stanford University；NVIDIA

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707216) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

We introduce Diffuse, a system that dynamically performs task and kernel fusion in distributed, task-based runtime systems. The key component of Diffuse is an intermediate representation of distributed computation that enables the necessary analyses for the fusion of distributed tasks to be performed in a scalable manner. We pair task fusion with a JIT compiler to fuse together the kernels within fused tasks. We show empirically that Diffuse's intermediate representation is general enough to be a target for two real-world, task-based libraries (cuPyNumeric and Legate Sparse), letting Diffuse find optimization opportunities across function and library boundaries. Diffuse accelerates unmodified applications developed by composing task-based libraries by 1.86x on average (geo-mean), and by between 0.93x–10.7x on up to 128 GPUs. Diffuse also finds optimization opportunities missed by the original application developers, enabling highlevel Python programs to match or exceed the performance of an explicitly parallel MPI library.

## 中文摘要

我们介绍 Diffuse，一个在分布式、基于任务的运行时系统中动态执行任务融合与内核融合的系统。Diffuse 的关键组件是一种分布式计算的中间表示，它使融合分布式任务所需的各项分析能够以可扩展的方式完成。我们将任务融合与 JIT 编译器相结合，把融合后任务内部的各个内核融合在一起。我们通过实验表明，Diffuse 的中间表示足够通用，可以作为两个真实世界、基于任务的库（cuPyNumeric 和 Legate Sparse）的编译目标，使 Diffuse 能够跨越函数与库的边界发现优化机会。Diffuse 将那些通过组合基于任务的库而开发、未经修改的应用平均加速 1.86 倍（几何平均），并在多达 128 块 GPU 上加速 0.93 倍至 10.7 倍。Diffuse 还发现了原应用开发者所遗漏的优化机会，使高层 Python 程序能够达到或超过显式并行 MPI 库的性能。

## 英文关键词

Distributed Programming; Composable Software

## 中文关键词

分布式编程；可组合软件

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707216)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2025](../index.md)
