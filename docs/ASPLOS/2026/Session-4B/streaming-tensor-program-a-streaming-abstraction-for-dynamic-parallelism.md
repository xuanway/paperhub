---
title: "Streaming Tensor Program: A streaming abstraction for dynamic parallelism"
description: "ASPLOS 2026 · Session 4B · Streaming Tensor Program：面向动态并行的流式抽象"
tags:
  - "ASPLOS2026"
  - "Session 4B"
  - "ML Compilers & Tensor Programs"
---

# Streaming Tensor Program: A streaming abstraction for dynamic parallelism

**中文标题：** Streaming Tensor Program：面向动态并行的流式抽象

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Gina Sohn (Stanford University), Genghan Zhang (Stanford University), Konstantin Hossfeld (Stanford University), Jungwoo Kim (Stanford University), Nathan Sobotka (Stanford University), Nathan Zhang (SambaNova Systems), Olivia Hsu (Stanford University), Kunle Olukotun (Stanford University)

**单位：** Stanford University；SambaNova Systems

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790229) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

**出版标题：** Streaming Tensor Programs: A Streaming Abstraction for Dynamic Parallelism

## 英文摘要

Dynamic behaviors are becoming prevalent in tensor applications, like machine learning, where many widely used models contain data-dependent tensor shapes and control flow. However, the limited expressiveness of prior programming abstractions for spatial dataflow accelerators (SDAs) forces these dynamic behaviors to be implemented statically and/or unoptimized. To address these challenges, we present Streaming Tensor Programs (STeP), a streaming abstraction that enables dynamic tensor workloads to run efficiently on SDAs. STeP introduces flexible routing operators, an explicit memory hierarchy, and symbolic-shape semantics that expose dynamic data rates and tensor dimensions. These capabilities unlock new optimizations, like dynamic tiling, dynamic parallelization, and configuration time-multiplexing, that adapt SDA execution to dynamic behaviors while preserving dataflow efficiency. Using a cycle-approximate simulator on representative LLM layers and a full model with real-world traces, STeP enables: dynamic tiling that breaks the Paretooptimal frontier from prior work, dynamic parallelization that improves latency by ∼2.72x, and configuration timemultiplexing that increases compute utilization by ∼2.64x over prior SDA abstractions and their implementations.

## 中文摘要

在机器学习等张量应用中，动态行为正变得普遍，许多广泛使用的模型包含依赖数据的张量形状和控制流。然而，先前的空间数据流加速器（SDA）编程抽象表达力有限，迫使这些动态行为以静态和/或未优化的方式实现。为应对这些挑战，我们提出 Streaming Tensor Programs（STeP），这是一种流式抽象，使动态张量工作负载能够在 SDA 上高效运行。STeP 引入了灵活的路由算子、显式的存储层次结构，以及能够暴露动态数据速率和张量维度的符号形状语义。这些能力解锁了新的优化，如动态分块、动态并行化和配置时分复用，它们在保持数据流效率的同时使 SDA 执行适应动态行为。在代表性 LLM 层以及带有真实负载轨迹的完整模型上使用周期近似模拟器，STeP 实现了：打破先前工作 Pareto 最优前沿的动态分块、将延迟改善约 2.72 倍的动态并行化，以及相对于先前 SDA 抽象及其实现将计算利用率提升约 2.64 倍的配置时分复用。

## 英文关键词

Streaming Abstraction; Dataflow Programming; Spatial Dataflow Accelerator; Dynamic Tensor Applications

## 中文关键词

流式抽象；数据流编程；空间数据流加速器；动态张量应用

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790229)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2026](../index.md)
