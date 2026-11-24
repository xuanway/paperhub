---
title: "Stramash: A Fused-kernel Operating System For Cache-Coherent, Heterogeneous-ISA Platforms"
description: "ASPLOS 2025 · Session 8C · Stramash：面向缓存一致异构 ISA 平台的融合内核操作系统"
tags:
  - "ASPLOS2025"
  - "Session 8C"
  - "Potpourri 2"
---

# Stramash: A Fused-kernel Operating System For Cache-Coherent, Heterogeneous-ISA Platforms

**中文标题：** Stramash：面向缓存一致异构 ISA 平台的融合内核操作系统

**所属 Session：** [Session 8C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Tong Xing (The University of Edinburgh), Cong Xiong (Imperial College London), Tianrui Wei (UC Berkeley), April Sanchez (Google), Binoy Ravindran (Virginia Tech), Jonathan Balkind (UC Santa Barbara), Antonio Barbalace (The University of Edinburgh)

**单位：** The University of Edinburgh；Imperial College London；UC Berkeley；Google；Virginia Tech；UC Santa Barbara

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716275) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

We live in the world of heterogeneous computing. With specialised elements reaching all aspects of our computer systems and their prevalence only growing, we must act to rein in their inherent complexity. One area that has seen significantly less investment in terms of development is heterogeneous-ISA systems, specifically because of complexity. To date, heterogeneous-ISA processors have required significant software overheads, workarounds, and coordination layers, making the development of more advanced software hard, and motivating little further development of more advanced hardware. In this paper, we take a fused approach to heterogeneity, and introduce a new operating system (OS) design, the fused-kernel OS, which goes beyond the multiple-kernel OS design, exploiting cache-coherent shared memory among heterogeneous-ISA CPUs as a first principle – introducing a set of new OS kernel mechanisms. We built a prototype fusedkernel OS, Stramash-Linux, to demonstrate the applicability of our design to monolithic OS kernels. We profile Stramash OS components on real hardware but tested them on an architectural simulator – Stramash-QEMU, which we design and build. Our evaluation begins by validating the accuracy of our simulator,achieving an average of less than 4% errors. We then perform a direct comparison between our fused-kernelOSand state-of-the-art multiple-kernel OS designs. Results demonstrate speedups ofup to2.1× on NPBbenchmarks. Further, we provide an in-depth analysis of the differences and trade-offs between fused-kernel and multiple-kernel OS designs. ∗Cong Xiong w

## 中文摘要

我们生活在一个异构计算的世界中。随着专用部件渗透到计算机系统的各个方面、其普及程度只增不减，我们必须采取行动来约束其固有的复杂性。异构 ISA 系统是投入明显不足的一个领域，原因正是其复杂性。迄今为止，异构 ISA 处理器需要大量的软件开销、变通方案与协调层，这使得开发更先进的软件变得困难，也导致更先进硬件的进一步开发缺乏动力。本文采用融合的方式处理异构性，并提出一种新的操作系统（OS）设计——融合内核 OS，它超越了多内核 OS 设计，将异构 ISA CPU 之间的缓存一致共享内存作为首要原则加以利用，并引入一组新的 OS 内核机制。我们构建了融合内核 OS 的原型 Stramash-Linux，以证明我们的设计适用于单体 OS 内核。我们在真实硬件上对 Stramash OS 的各个组件进行剖析，但在一套由我们设计并构建的体系结构模拟器 Stramash-QEMU 上对它们进行测试。我们的评估首先验证模拟器的准确性，平均误差低于 4%。随后，我们在融合内核 OS 与最先进的多内核 OS 设计之间进行直接比较。结果表明，在 NPB 基准测试上最高可获得 2.1 倍的加速。此外，我们深入分析了融合内核与多内核 OS 设计之间的差异与权衡。

## 英文关键词

OperatingSystems,Multiple-Kernel,Fused-kernel, Simulation,Heterogeneous,CacheCoherent,SharedMemory

## 中文关键词

操作系统；多内核；融合内核；模拟；异构；缓存一致；共享内存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716275)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8C](index.md) · [返回 ASPLOS 2025](../index.md)
