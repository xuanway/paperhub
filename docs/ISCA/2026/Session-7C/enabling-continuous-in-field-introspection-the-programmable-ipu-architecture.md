---
title: "Enabling Continuous, In-Field Introspection: The Programmable IPU Architecture"
description: "ISCA 2026 · Session 7C · Enabling Continuous, In-Field Introspection: The Programmable IPU Architecture"
tags:
  - "ISCA2026"
  - "Session 7C"
  - "Domain Specific Accelerators 2"
---

# Enabling Continuous, In-Field Introspection: The Programmable IPU Architecture

**中文标题：** 实现持续的现场内省：可编程 IPU 架构

**所属 Session：** [Session 7C](index.md) · [ISCA 2026](../index.md)

**作者：** Ian McDougall, Shayne Wadle, Harish Babu Batchu, Karthikeyan Sankaralingam

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Modern silicon systems are increasingly opaque, leaving developers blind to in-field hardware behavior on real workloads. Existing introspection tools force a debilitating trade-off: fixed-function Performance Monitoring Units (PMUs) are low-overhead but lack programmability, while trace-based solutions are high-fidelity but incur prohibitive data and performance overhead, and have an accessibility challenge as well. This leaves a critical “capability gap,” with no solution offering programmability, low overhead, and real-time analysis simultaneously. This paper introduces the Introspection Processing Unit (IPU), a new, lightweight architectural primitive designed to fill this gap. The IPU is a novel hybrid microarchitecture, pairing a programmable RISC-V core with judiciously chosen microarchitectural accelerator extensions, including a tiny eFPGA. This hybrid design is our core insight, balancing the flexibility of software with the line-rate efficiency required for non-invasive introspection. We demonstrate the IPU’s power not through point solutions, but by showing its ability to perform classes of analysis previously considered intractable in the field. We show a single IPU architecture can perform: 1) Stateful Emulation: (e.g., A/B testing instruction prefetchers), 2) Software-Defined Performance Attribution (e.g., creating per-instruction cycle stacks), 3) Scalable, On-Chip Data Aggregation (e.g., fine-grained GPU utilization monitoring), and 4) Real-Time Component-Level Diagnosis (e.g., per-miss root-cause diagnosis of a prefetcher). Our complete RTL-level prototype, synthesized at 7nm, proves this new capability is practical, with an area overhead of < 1% and power consumption of < 25mW.

## 中文摘要

现代硅系统日益不透明，使开发者无法了解真实工作负载下的现场硬件行为。现有内省工具迫使用户做出不利的取舍：固定功能的性能监控单元（PMU）开销低但缺乏可编程性，而基于追踪的方案保真度高，却带来难以承受的数据与性能开销，并且还存在可访问性难题。这留下了一个关键的“能力鸿沟”：没有任何方案能同时提供可编程性、低开销和实时分析。本文提出内省处理单元（IPU），一种旨在填补这一空白的新颖轻量级架构原语。IPU 是一种新颖的混合微架构，将一个可编程 RISC-V 核与精心选择的微架构加速器扩展（包括一个小型 eFPGA）配对。这种混合设计是我们的核心洞见，它在软件灵活性与非侵入式内省所需的线速效率之间取得平衡。我们不是通过单点方案，而是通过展示 IPU 能够执行此前被认为在现场难以处理的多类分析，来证明其威力。我们表明单一 IPU 架构可以执行：1）有状态仿真（例如，对指令预取器进行 A/B 测试），2）软件定义性能归因（例如，创建逐指令的周期栈），3）可扩展的片上数据聚合（例如，细粒度 GPU 利用率监控），以及 4）实时组件级诊断（例如，预取器的逐缺失根因诊断）。我们完整的 RTL 级原型在 7nm 下综合，证明这一新能力是实用的，面积开销 < 1%，功耗 < 25mW。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2026](../index.md)
