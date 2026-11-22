---
title: "Performance Verification of the AmpereOne® CPU Core"
description: "MICRO 2026 · Session 1C · AmpereOne® CPU 核心的性能验证"
tags:
  - "MICRO2026"
---

# Performance Verification of the AmpereOne® CPU Core

**中文标题：** AmpereOne® CPU 核心的性能验证

**所属 Session：** [Session 1C](index.md) · [MICRO 2026](../index.md)

**作者：** Doa'a Al-Otoom, Nicholas Kelly, Aaron Lindsay, Agreen Ahmadi, Ananth Kumar, Anthony Faubert, Benjamin Chaffin, Bret Toll, Eric Wallace, Lucas Crowthers, Mark Charney, Michael Chin, Michael Spradling, Scott Witscher, Sriyash Caculo, Syed Fakhri, Vivek Kothapalli, William Freelove, Mahesh Madhav

**来源：** MICRO 2026，pp. 300–314；[DOI](https://doi.org/10.1109/MICRO67795.2026.00036)

## 英文摘要

As process technology scaling slows, microarchitectural innovation has become the primary driver of performance gains, making pre-silicon Performance Verification (PV) more critical than ever. This paper presents the industrial-scale PV methodology applied across four generations of the AmpereOne® custom CPU core, centered on the cycle-accurate correlation of the RTL design against a trace-driven performance model. The methodology integrates data-driven workload curation, a high-frequency daily regression system, and a unified event-stream framework for analysis. We demonstrate this methodology through case studies of the Branch Prediction Unit and L2 Prefetcher, highlighting a hierarchical strategy that first isolates individual units for focused correlation before proceeding to full-core verification. The results demonstrate that this disciplined, iterative process is indispensable for avoiding costly post-silicon bugs and ensuring complex processors meet their performance targets. We end with a look towards the future of PV in the microprocessor industry.

## 中文摘要

随着工艺技术扩展速度放缓，微架构创新已成为性能提升的主要驱动力，使得投片前性能验证 (PV) 比以往任何时候都更加重要。本文介绍了应用于四代 AmpereOne® 定制 CPU 内核的工业规模 PV 方法，重点是 RTL 设计与跟踪驱动性能模型的周期精确相关性。该方法集成了数据驱动的工作负载管理、高频每日回归系统和统一的事件流分析框架。我们通过分支预测单元和 L2 预取器的案例研究演示了这种方法，强调了一种分层策略，该策略首先隔离各个单元以实现重点关联，然后再进行全核心验证。结果表明，这种严格的迭代过程对于避免代价高昂的硅后缺陷和确保复杂处理器满足其性能目标是必不可少的。最后我们展望了微处理器行业性能验证的未来。

## 中文关键词

AmpereOne 处理器；性能验证；CPU 微架构；验证方法

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1C](index.md) · [MICRO 2026 主页](../index.md)
