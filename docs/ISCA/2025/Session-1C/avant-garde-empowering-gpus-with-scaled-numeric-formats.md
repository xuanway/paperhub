---
title: "Avant-Garde: Empowering GPUs with Scaled Numeric Formats"
description: "ISCA 2025 · Session 1C · Avant-Garde: 为GPU赋能缩放数值格式"
tags:
  - "ISCA2025"
  - "Session 1C"
  - "GPUs & Ray Tracing"
---

# Avant-Garde: Empowering GPUs with Scaled Numeric Formats

**中文标题：** Avant-Garde: 为GPU赋能缩放数值格式

**所属 Session：** [Session 1C](index.md) · [ISCA 2025](../index.md)

**作者：** Minseong Gil, Dongho Ha, Simla Burcu Harma, Myung Kuk Yoon, Babak Falsafi, Won Woo Ro, Yunho Oh

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731100) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The escalating computational and memory demands of deep neural
networks have outpaced chip density improvements, making arith-
metic density a key bottleneck for GPUs. Scaled numeric formats,
such as FP8 and Microscaling (MX), improve arithmetic density
by applying adaptive scaling factors across varying block sizes
and multiple scaling hierarchies. Unfortunately, supporting diverse
scaled numeric formats often requires GPUs to rely on software-
based implementations, increasing instruction and register over-
head and degrading performance. We propose Avant-Garde, a GPU
microarchitecture that natively supports diverse scaled numeric
formats by converting them into a consistent single-level internal
representation. Avant-Garde integrates an Operand Transformer,
a hardware module that dynamically flattens multi-level scaling
formats into single-level internal representations, a novel Tensor
Core, and an optimized data layout to eliminate instruction and
register overhead. Our evaluations show that Avant-Garde achieves
up to 74% higher throughput and 44% lower execution time, while
maintaining accuracy within 0.2% compared to conventional GPUs.

## 中文摘要

深度神经网络持续增长的计算与存储需求已经超过芯片密度的提升速度，算术密度成为GPU的核心瓶颈。FP8、微缩放格式（MX）等缩放数值格式，通过在不同块大小与多层缩放层级上使用自适应缩放因子来提升算术密度。但遗憾的是，GPU若要支持多种缩放数值格式，大多只能依靠软件实现，这会引入额外的指令与寄存器开销，造成性能下降。本文提出Avant-Garde，一款GPU微架构，它将各类缩放数值格式转换为统一的单层内部表示，从而原生支持多种缩放数值格式。Avant-Garde集成操作数转换器（Operand Transformer）、新型张量核心以及优化的数据布局；其中操作数转换器作为硬件模块，能够动态地将多层缩放格式扁平化转换为单层内部表示，以此消除指令和寄存器开销。评测结果表明，相较于传统GPU，Avant-Garde最高可提升74%的吞吐量、降低44%的执行时间，同时精度损失控制在0.2%以内。

## 英文关键词

GPU, Deep Neural Network, Scaled Numeric Format

## 中文关键词

GPU, 深度神经网络, 缩放数值格式

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731100)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1C](index.md) · [返回 ISCA 2025](../index.md)
