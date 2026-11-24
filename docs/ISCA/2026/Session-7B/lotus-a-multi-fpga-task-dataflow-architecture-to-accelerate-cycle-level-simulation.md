---
title: "Lotus: A Multi-FPGA Task Dataflow Architecture to Accelerate Cycle-Level Simulation"
description: "ISCA 2026 · Session 7B · Lotus: A Multi-FPGA Task Dataflow Architecture to Accelerate Cycle-Level Simulation"
tags:
  - "ISCA2026"
  - "Session 7B"
  - "Performance Modeling / Datacenter"
---

# Lotus: A Multi-FPGA Task Dataflow Architecture to Accelerate Cycle-Level Simulation

**中文标题：** Lotus: 加速周期级仿真的多 FPGA 任务数据流架构

**所属 Session：** [Session 7B](index.md) · [ISCA 2026](../index.md)

**作者：** Fares Elsabbagh, Joel S. Emer, Daniel Sanchez

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Simulation is crucial to design and build hardware. But simulating large and complex digital designs is slow. Hardware emulators are the standard accelerator for cycle-level RTL simulation, but these systems are expensive, inefficient, slow to compile for, and limited to simulating RTL. Emulators consist of many chips, typically FPGAs, to which the design is compiled. Emulators are bottlenecked by communication, and use FPGAs at a fraction of their speed. We present Lotus, a large-scale architecture that accelerates cycle-level simulation. Lotus uses multiple FPGAs like emulators, but takes a different approach: rather than mapping logic directly to FPGAs, Lotus implements thousands of simple cores, along with hardware support that enables software simulation to scale. Lotus simulates digital systems by encoding them as large dataflow graphs of tiny tasks that run on these cores. Lotus uses dataflow execution to extract abundant parallelism; task priorities to focus work on the critical path; and selective execution to avoid ineffectual work. We contribute new implementations of these techniques that scale to multiple chips and require simple hardware. We also develop a compiler to use Lotus efficiently from high-level dataflow graphs. We build an implementation of Lotus using 8 FPGAs, featuring over two thousand cores. On several large designs, this Lotus prototype achieves speeds comparable to emulators, while reducing the number of FPGAs needed by up to 7.5× and improving performance per FPGA by up to 23×. Lotus is also 8× faster than a 128-core server. Overall, Lotus is the first system to show that software simulation can outperform emulators by leveraging large-scale parallelism.

## 中文摘要

仿真对于设计和构建硬件至关重要，但仿真大型复杂的数字设计非常缓慢。硬件仿真器是周期级 RTL 仿真的标准加速器，但这类系统价格昂贵、效率低下、编译慢，且仅限于仿真 RTL。仿真器由许多芯片（通常是 FPGA）组成，设计被编译到这些芯片上。仿真器受通信瓶颈制约，并且只能以 FPGA 速度的一小部分运行。我们提出 Lotus，一种加速周期级仿真的大规模架构。Lotus 像仿真器一样使用多个 FPGA，但采取了不同的方法：它不将逻辑直接映射到 FPGA，而是在其上实现数千个简单的核心，并提供使软件仿真得以扩展的硬件支持。Lotus 通过将数字系统编码为由运行在这些核心上的微小任务组成的大型数据流图来仿真数字系统。Lotus 利用数据流执行来提取丰富的并行性，利用任务优先级将工作聚焦于关键路径，并利用选择性执行来避免无效工作。我们贡献了这些技术的新实现，它们可扩展到多个芯片且只需简单的硬件。我们还开发了一个编译器，以便从高层数据流图高效地使用 Lotus。我们构建了一个使用 8 块 FPGA、拥有两千多个核心的 Lotus 实现。在若干大型设计上，该 Lotus 原型达到了与仿真器相当的速度，同时将所需 FPGA 数量最多减少 7.5×，并将每块 FPGA 的性能最多提升 23×。Lotus 还比 128 核服务器快 8×。总体而言，Lotus 是首个表明软件仿真可以借助大规模并行性超越仿真器的系统。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：LotusArch/lotus](https://github.com/LotusArch/lotus)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2026](../index.md)
