---
title: "Optimizing Datalog for the GPU"
description: "ASPLOS 2025 · Session 10A · 面向 GPU 的 Datalog 优化"
tags:
  - "ASPLOS2025"
  - "Session 10A"
  - "GPGPU"
---

# Optimizing Datalog for the GPU

**中文标题：** 面向 GPU 的 Datalog 优化

**所属 Session：** [Session 10A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yihao Sun (Syracuse University), Ahmedur Rahman Shovon (University of Illinois, Chicago), Thomas Gilray (Washington State University), Sidharth Kumar (University of Illinois, Chicago), Kristopher Micinski (Syracuse University)

**单位：** Syracuse University；University of Illinois, Chicago；Washington State University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707274) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Modern Datalog engines (e.g., LogicBlox, Soufflé, ddlog) enable their users to write declarative queries which compute recursive deductions over extensional facts, leaving high-performance operationalization (query planning, seminaïve evaluation, and parallelization) to the engine. Such engines form the backbone of modern high-throughput applications in static analysis, network monitoring, and socialmedia mining. In this paper, we present a methodology for implementing a modern in-memory Datalog engine on data center GPUs, allowing us to achieve significant (up to 45×) gains compared to Soufflé (a modern CPU-based engine) on context-sensitive points-to analysis of PostgreSQL. We present GPUlog, a Datalog engine backend that implements iterated relational algebra kernels over a novel rangeindexed data structure we call the hash-indexed sorted array (HISA). HISA combines the algorithmic benefits of incremental range-indexed relations with the raw computation throughput of operations over dense data structures. Our experiments show that GPUlog is significantly faster than CPU-based Datalog engines while achieving a favorable memory footprint compared to contemporary GPU-based joins.

## 中文摘要

现代 Datalog 引擎（如 LogicBlox、Soufflé、ddlog）让用户能够编写声明式查询，在外延事实上计算递归推导，而将高性能的算子化（查询规划、半朴素求值与并行化）留给引擎完成。此类引擎构成了静态分析、网络监控与社交媒体挖掘等现代高吞吐应用的骨干。本文提出一种在数据中心 GPU 上实现现代内存驻留 Datalog 引擎的方法，使我们在对 PostgreSQL 进行上下文敏感的指向分析时，相较 Soufflé（一种现代基于 CPU 的引擎）获得显著收益（最高 45 倍）。我们提出 GPUlog，一个 Datalog 引擎后端，它在一类我们称为哈希索引有序数组（HISA，hash-indexed sorted array）的新型范围索引数据结构上实现迭代的关系代数内核。HISA 将增量式范围索引关系的算法优势与稠密数据结构上运算的原始计算吞吐结合起来。我们的实验表明，GPUlog 显著快于基于 CPU 的 Datalog 引擎，同时与当代基于 GPU 的连接操作相比具有有利的内存占用。

## 英文关键词

Datalog, GPU, Analytic Databases

## 中文关键词

Datalog；GPU；分析型数据库

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707274)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10A](index.md) · [返回 ASPLOS 2025](../index.md)
