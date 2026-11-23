---
title: "Assassyn: A Unified Abstraction for Architectural Simulation and Implementation"
description: "ISCA 2025 · Session 8A · Assassyn：面向体系结构仿真与实现的统一抽象"
tags:
  - "ISCA2025"
  - "Session 8A"
  - "Performance and Modeling"
---

# Assassyn: A Unified Abstraction for Architectural Simulation and Implementation

**中文标题：** Assassyn：面向体系结构仿真与实现的统一抽象

**所属 Session：** [Session 8A](index.md) · [ISCA 2025](../index.md)

**作者：** Jian Weng, Boyang Han, Derui Gao, Ruijie Gao, Wanning Zhang, An Zhong, Ceyu Xu, Jihao Xin, Yangzhixin Luo, Lisa Wu Wills, Marco Canini

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731004) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The continuous growth of on-chip transistors driven by technol- ogy scaling urges architecture developers to design and implement novel architectures to effectively utilize the excessive on-chip re- sources. Due to the challenges of programming in register-transfer level (RTL) languages, performance modeling based on simulation is typically developed alongside hardware implementation, allowing the exploration of high-level design decisions before dealing with the error-prone, low-level RTL details. However, this approach also introduces new challenges in coordinating across multiple teams to align implementation details separate codebases. In this paper, we address this issue by presenting Assassyn, a unified, high-level, and general-purpose programming framework for architectural simulation and implementation. By taking ad- vantage of the concept of asynchronous event handling, a widely existing behavior in both hardware design and implementation and software engineering, a general-purpose, and high-level pro- gramming abstraction is proposed to mitigate the difficulties of RTL programming. Moreover, the unified programming interface naturally enables an accurate and faithful alignment between the simulation-based performance modeling and RTL implementation. Our evaluation demonstrates that Assassyn’s high-level program- ming interface is sufficiently expressive to implement a wide range of architectures, from architectural components, and application- specific accelerators, to designs as complicated as out-of-order CPUs. All the generated simulators perfectly align with the gener- ated RTL behavior, while achieving 2.2-8.1×simulation speedup, and requiring 70% lines of code. The generated RTL achieves com- parable perf/area compared to handcrafted RTL, and 6×perf/area compared to high-level synthesis generated RTL code by introduc- ing by mean 1.26×lines of code overhead.

## 中文摘要

工艺缩放带来片上晶体管数量持续增长，这要求体系结构研究者设计并实现新型架构，高效利用充裕的片上资源。寄存器传输级（RTL）语言编程门槛高，因此研究者通常会在硬件实现的同步开发仿真性能模型，在进入容易出错的底层RTL细节之前，先对高层设计方案进行探索。但这种方式也带来新难题：多团队协同开发时，需要在相互独立的代码库之间对齐实现细节。

本文提出Assassyn，一套统一、高层、通用的编程框架，同时支持架构仿真与硬件实现。框架利用异步事件处理思想——该行为在硬件设计、工程实现与软件工程中广泛存在——提出通用高层编程抽象，降低RTL编程难度。此外，统一编程接口天然保证基于仿真的性能模型与RTL实现能够精准、一致地对齐。

评测表明：Assassyn的高层编程接口表达能力充足，可实现各类架构，从小型架构组件、专用加速器，直至乱序CPU这类复杂设计。由该框架生成的仿真器与生成的RTL行为完全一致，仿真速度提升2.2–8.1倍，代码行数仅为原有方案的70%。生成的RTL在性能面积比上和手写RTL相当；相比高层综合（HLS）生成的RTL，性能面积比提升6倍，代码行数平均仅增加1.26倍。

## 英文关键词

Performance Modeling and Simulation, Open-source Hardware, High-level Hardware Description Language

## 中文关键词

性能建模与仿真, 开源硬件, 高级硬件描述语言

## 代码与研究制品

- [代码仓库](https://github.com/Synthesys-Lab/assassyn)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731004)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8A](index.md) · [返回 ISCA 2025](../index.md)
