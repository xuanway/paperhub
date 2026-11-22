---
title: "MORIA: Mining the Cache for Miss Parallelism"
description: "MICRO 2026 · Session 7D · MORIA：从缓存中挖掘未命中并行性"
tags:
  - "MICRO2026"
  - "Cache"
---

# MORIA: Mining the Cache for Miss Parallelism

**中文标题：** MORIA：从缓存中挖掘未命中并行性

**所属 Session：** [Session 7D](index.md) · [MICRO 2026](../index.md)

**作者：** Marina Vemmou, Alexandros Daglis

**来源：** MICRO 2026，pp. 2625–2639；[DOI](https://doi.org/10.1109/MICRO67795.2026.00179)

## 英文摘要

Memory-level parallelism is a primary determinant of single-thread CPU performance, yet it is limited by the number of Miss Status Handling Registers (MSHRs) in L1 caches. While the bandwidth-delay product of increasingly deep and complex memory systems continues to grow, L1 MSHR provisioning remains modest, causing frequent MSHR exhaustion and stalling the CPU even in the presence of available memory bandwidth. We find that modern workloads routinely exceed available MSHR capacity, exposing MSHRs as a critical and growing bottleneck. We propose MORIA, a technique that overcomes this limitation by virtualizing MSHRs within a minimally augmented L1 cache. MORIA dynamically repurposes cache lines to hold miss-tracking state when dedicated MSHRs are depleted, leveraging the high associativity and underutilized capacity of modern caches to provide scalable, on-demand miss handling. We present and evaluate two MORIA variants: a hybrid, which augments conventional MSHRs with an in-cache fallback, and a full in-cache, which eliminates dedicated MSHRs. Across 86 workloads, MORIA improves performance by 1.14x, on average, by eliminating MSHR-induced stalls, with modest area and energy overheads.

## 中文摘要

内存级并行性是单线程 CPU 性能的主要决定因素，但它受到 L1 缓存中未命中状态处理寄存器 (MSHR) 数量的限制。虽然日益深入和复杂的内存系统的带宽时延产物持续增长，但 L1 MSHR 配置仍然有限，导致频繁的 MSHR 耗尽，甚至在存在可用内存带宽的情况下也会导致 CPU 停止运行。我们发现，现代工作负载通常会超出可用的 MSHR 容量，从而使 MSHR 成为一个关键且日益严重的瓶颈。我们提出了 MORIA，这是一种通过在最小增强的 L1 缓存中虚拟化 MSHR 来克服这一限制的技术。当专用 MSHR 耗尽时，MORIA 动态地重新调整缓存线的用途以保持未命中跟踪状态，利用现代缓存的高关联性和未充分利用的容量来提供可扩展的按需未命中处理。我们提出并评估了两种 MORIA 变体：一种是混合型，它通过缓存内回退增强了传统的 MSHR；另一种是完全缓存型，它消除了专用的 MSHR。在 86 个工作负载中，MORIA 通过消除 MSHR 引起的停顿，平均将性能提高 1.14 倍，并具有适度的面积和能源开销。

## 中文关键词

未命中并行性；缓存内未命中状态处理寄存器；缓存设计

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7D](index.md) · [MICRO 2026 主页](../index.md)
