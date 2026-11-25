---
title: "Dynamic Detection of Inefficient Data Mapping Patterns in Heterogeneous OpenMP Applications"
description: "PPoPP 2026 Session 4（GPU and Heterogeneous Computing）：OMPT 动态检测低效数据映射，开销仅 5%，给出源码归因"
tags:
  - "PPoPP2026"
  - "Session-4"
  - "GPU and Heterogeneous Computing"
  - "OpenMP"
  - "Performance Analysis"
  - "Heterogeneous Computing"
authors:
  - "Luke Marzen"
  - "Junhyung Shim"
  - "Ali Jannesari"
session: "Session 4: GPU and Heterogeneous Computing"
session_number: 4
session_chair: "Frank Mueller"
date: "2026-02-02"
time: "16:10–16:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786454"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Dynamic Detection of Inefficient Data Mapping Patterns in Heterogeneous OpenMP Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出异构 OpenMP 应用的动态分析技术并实现工具 OMPDataPerf，自动检测低效数据传输与分配模式，几何平均运行时开销仅 5%。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 4: GPU and Heterogeneous Computing</p>
</div>

**作者**：Luke Marzen, Junhyung Shim, and Ali Jannesari — Iowa State University, USA

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 16:10–16:30 · Session 4: GPU and Heterogeneous Computing（主席：Frank Mueller）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786454) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

With the growing prevalence of heterogeneous computing, CPUs are increasingly being paired with accelerators to achieve new levels of performance and energy efficiency. However, data movement between devices remains a significant bottleneck, complicating application development. Existing performance tools require considerable programmer intervention to diagnose and locate data transfer inefficiencies. To address this, we propose dynamic analysis techniques to detect and profile inefficient data transfer and allocation patterns in heterogeneous applications. We implemented these techniques into OMPDataPerf, which provides detailed traces of problematic data mappings, source code attribution, and assessments of optimization potential in heterogeneous OpenMP applications. OMPDataPerf uses the OpenMP Tools Interface (OMPT) and incurs only a 5 % geometric-mean runtime overhead.

## 中文摘要

随着异构计算的日益普及，CPU 越来越多地与加速器配对使用，以在性能与能效上达到新的水平。然而，设备之间的数据移动仍是显著瓶颈，使应用开发变得复杂。现有性能工具需要程序员大量介入，才能诊断并定位数据传输的低效之处。为此，我们提出动态分析技术，用于检测并剖析异构应用中低效的数据传输与内存分配模式。我们将这些技术实现为 OMPDataPerf，它可提供问题数据映射的详细轨迹、源代码归因，以及对异构 OpenMP 应用中优化潜力的评估。OMPDataPerf 使用 OpenMP 工具接口（OMPT），仅带来 5% 的几何平均运行时开销。

## 英文关键词

Heterogeneous Computing, Performance Profiling, Dynamic Analysis, Data Transfer, GPUs, OpenMP

## 中文关键词

异构计算；性能剖析；动态分析；数据传输；GPU；OpenMP

---

## 一句话总结

> 提出异构 OpenMP 应用的动态分析技术并实现工具 OMPDataPerf，自动检测低效数据传输与分配模式，几何平均运行时开销仅 5%。

## 研究问题

异构计算中设备间的数据移动仍是主要瓶颈，而现有性能工具需要程序员大量介入，才能诊断并定位数据传输的低效问题。

## 方法简述

- 提出动态分析技术，检测并剖析异构应用中的低效数据传输与内存分配模式。
- 基于 OpenMP Tools Interface（OMPT）将上述技术实现为工具 OMPDataPerf。
- 设计输出有问题的数据映射详细轨迹、源代码归因以及优化潜力评估。

## 主要结果

- OMPDataPerf 仅引入 5% 的几何平均运行时开销。
- 能够定位有问题的数据映射，给出源码级归因并评估其优化潜力。

---

> 所属 Session：[Session 4: GPU and Heterogeneous Computing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
