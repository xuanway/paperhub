---
title: "Co-Exploration of RISC-V Processor Microarchitectures and FreeRTOS Extensions for Lower Context Switch Latency"
description: "ASPLOS 2026 · Session 7D · 面向更低上下文切换延迟的 RISC-V 处理器微架构与 FreeRTOS 扩展协同探索"
tags:
  - "ASPLOS2026"
  - "Session 7D"
  - "Processor Microarchitecture"
---

# Co-Exploration of RISC-V Processor Microarchitectures and FreeRTOS Extensions for Lower Context Switch Latency

**中文标题：** 面向更低上下文切换延迟的 RISC-V 处理器微架构与 FreeRTOS 扩展协同探索

**所属 Session：** [Session 7D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Markus Scheck (Technische Universität Darmstadt), Tammo Mürmann (Technische Universität Darmstadt), Andreas Koch (Technische Universität Darmstadt)

**单位：** Technische Universität Darmstadt

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790141) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Embedded real-time systems must respond to external events within tightly bounded timeframes to ensure safety, correctness, and reliability. While Real-Time Operating Systems (RTOSes) ease the development of complex applications by providing abstractions for multi-tasked execution, they introduce overheads in the form of task switching latency and jitter, which impact timing predictability. Minimizing these effects is essential for reducing response times and enabling robust worst-case timing analysis. We present RTOSUnit, a configurable hardware acceleration unit designed to reduce context-switch latency and jitter in embedded realtime systems. By integrating the RTOSUnit into three RISC-V cores of varying complexity, we demonstrate its portability. Through a range of configurations, from lightweight scheduling acceleration to full context-switch and -preloading support, RTOSUnit achieves up to 76 % reduction in mean context-switch latency and can be configured to completely eliminate jitter on selected cores. Area overheads in 22 nm ASIC implementations range from negligible (within EDA tool heuristics noise) to 44 %, with all configurations maintaining viable operating frequencies and power envelopes suitable for embedded systems. RTOSUnit offers a flexible and efficient, open-source1 foundation for hardware-assisted real-time scheduling, paving the way for broader integration into future embedded SoCs.

## 中文摘要

嵌入式实时系统必须在严格受限的时间范围内响应外部事件，以确保安全性、正确性与可靠性。实时操作系统（RTOS）通过为多任务执行提供抽象，简化了复杂应用的开发，但也以任务切换延迟和抖动的形式引入开销，从而影响时序可预测性。最小化这些影响对于缩短响应时间并实现稳健的最坏情况时序分析至关重要。我们提出 RTOSUnit，一个可配置的硬件加速单元，旨在降低嵌入式实时系统中的上下文切换延迟与抖动。通过将 RTOSUnit 集成到三个复杂度各异的 RISC-V 核中，我们展示了其可移植性。通过从轻量级调度加速到完整的上下文切换与预加载支持的一系列配置，RTOSUnit 最高可将平均上下文切换延迟降低 76 %，并可在选定的核上配置为完全消除抖动。22 nm ASIC 实现中的面积开销从可忽略（处于 EDA 工具启发式噪声范围内）到 44 % 不等，且所有配置都维持适用于嵌入式系统的可行工作频率与功耗包络。RTOSUnit 为硬件辅助实时调度提供了一个灵活、高效且开源的基础，为更广泛地集成到未来嵌入式 SoC 中铺平了道路。

## 英文关键词

FreeRTOS; Context-Switch; Latency; Jitter; RealTime; RTOS; RISC-V

## 中文关键词

FreeRTOS；上下文切换；延迟；抖动；实时；RTOS；RISC-V

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790141)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7D](index.md) · [返回 ASPLOS 2026](../index.md)
