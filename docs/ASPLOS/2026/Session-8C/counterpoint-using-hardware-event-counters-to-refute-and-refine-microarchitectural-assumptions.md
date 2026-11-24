---
title: "CounterPoint: Using Hardware Event Counters to Refute and Refine Microarchitectural Assumptions"
description: "ASPLOS 2026 · Session 8C · CounterPoint：利用硬件事件计数器反驳并修正微架构假设"
tags:
  - "ASPLOS2026"
  - "Session 8C"
  - "Memory Hierarchy & Performance"
---

# CounterPoint: Using Hardware Event Counters to Refute and Refine Microarchitectural Assumptions

**中文标题：** CounterPoint：利用硬件事件计数器反驳并修正微架构假设

**所属 Session：** [Session 8C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Nick Lindsay (Yale University), Caroline Trippel (Stanford University), Anurag Khandelwal (Yale University), Abhishek Bhattacharjee (Yale University)

**单位：** Yale University；Stanford University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790145) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Hardware event counters offer the potential to reveal not only performance bottlenecks but also detailed microarchitectural behavior. In practice, this promise is undermined by their vague specifications, opaque designs, and multiplexing noise, making event counter data hard to interpret. We introduce CounterPoint, a framework that tests userspecified microarchitectural models—expressed as 𝜇path Decision Diagrams—for consistency with performance counter data. When mismatches occur, CounterPoint pinpoints plausible microarchitectural features that could explain them, using multi-dimensional counter confidence regions to mitigate multiplexing noise. We apply CounterPoint to the Haswell Memory Management Unit as a case study, shedding light on multiple undocumented and underdocumented microarchitectural behaviors. These include a load–store queue-side TLB prefetcher, merging page table walkers, abortable page table walks, and more. Overall, CounterPoint helps experts reconcile noisy hardware performance counter measurements with their mental model of the microarchitecture— uncovering subtle, previously hidden hardware features along the way.

## 中文摘要

硬件事件计数器不仅有望揭示性能瓶颈，还能揭示详细的微架构行为。在实践中，这一前景被其模糊的规格说明、不透明的设计以及多路复用噪声所削弱，使得事件计数器数据难以解读。我们提出 CounterPoint，一个检验用户指定的微架构模型（以 𝜇path 决策图表示）与性能计数器数据是否一致的框架。当出现不一致时，CounterPoint 会指出能够解释这些不一致的合理微架构特征，并利用多维计数器置信区域来缓解多路复用噪声。我们以 Haswell 内存管理单元为案例应用 CounterPoint，揭示了多项未被记录和记录不足的微架构行为。这些行为包括位于加载–存储队列一侧的 TLB 预取器、合并的页表遍历器、可中止的页表遍历等。总体而言，CounterPoint 帮助专家将含噪的硬件性能计数器测量结果与其微架构心智模型相协调，并在此过程中发现细微的、此前隐藏的硬件特性。

## 英文关键词

hardware event counters; address translation

## 中文关键词

硬件事件计数器；地址转换

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790145)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8C](index.md) · [返回 ASPLOS 2026](../index.md)
