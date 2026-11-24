---
title: "Don't Repeat Yourself! Coarse-Grained Circuit Deduplication to Accelerate RTL Simulation"
description: "ASPLOS 2025 · Session 3D · 不要重复自己！粗粒度电路去重加速 RTL 仿真"
tags:
  - "ASPLOS2025"
  - "Session 3D"
  - "EDA"
---

# Don't Repeat Yourself! Coarse-Grained Circuit Deduplication to Accelerate RTL Simulation

**中文标题：** 不要重复自己！粗粒度电路去重加速 RTL 仿真

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Haoyuan Wang (UC Santa Cruz), Thomas Nijssen (UC Santa Cruz), Scott Beamer (UC Santa Cruz)

**单位：** UC Santa Cruz

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674184) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Designing a digital integrated circuit requires many register transfer level (RTL) simulations for design, debugging, and especially verification. To cope with the slow speed of RTL simulation, industry frequently uses private server farms to run many simulations in parallel. Surprisingly, the implications of parallel runs of different RTL simulations have not been extensively explored. Moreover, in modern digital hardware, there is a growing trend to replicate components to scale out. However, the potential for circuit deduplication has been mostly overlooked. In this work, we pinpoint the shared last-level cache as the primary bottleneck impacting the throughput of RTL simulation. To address this issue, we propose a coarse-grained circuit deduplication strategy integrated into an RTL simulator. Our method involves identifying multiple instances of a single module within a digital circuit and creating shared code that can be applied to all of these instances. Our approach reduces the cache footprint by increasing code reuse, which consequently benefits processor components such as caches and branch predictors. Our experiments demonstrate that deduplication can bring up to 1.95× speedup in a single simulation, and achieve up to 2.09× overall RTL simulation throughput.

## 中文摘要

设计数字集成电路需要为设计、调试、尤其是验证进行大量寄存器传输级（RTL）仿真。为应对 RTL 仿真缓慢的速度，工业界经常使用私有服务器集群并行运行大量仿真。令人惊讶的是，不同 RTL 仿真并行运行所带来的影响尚未得到充分探索。此外，在现代数字硬件中，为横向扩展而复制组件的趋势日益明显。然而，电路去重的潜力在很大程度上被忽视了。在本工作中，我们指出共享的末级缓存是影响 RTL 仿真吞吐率的主要瓶颈。为解决这一问题，我们提出一种集成到 RTL 仿真器中的粗粒度电路去重策略。我们的方法包括识别数字电路中单个模块的多个实例，并创建可应用于所有这些实例的共享代码。我们的方法通过提高代码复用降低了缓存占用，从而使缓存和分支预测器等处理器组件受益。我们的实验表明，去重可在单次仿真中带来高达 1.95× 的加速，并实现高达 2.09× 的总体 RTL 仿真吞吐率。

## 英文关键词

RTL simulation, simulation throughput, deduplication

## 中文关键词

RTL 仿真；仿真吞吐率；去重

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674184)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2025](../index.md)
