---
title: "æSIP: µArch-aware ASIP-ISA Co-Design via Program Synthesis, Equality Saturation, and External Don’t Cares"
description: "ISCA 2026 · Session 6C · æSIP: µArch-aware ASIP-ISA Co-Design via Program Synthesis, Equality Saturation, and External Don’t Cares"
tags:
  - "ISCA2026"
  - "Session 6C"
  - "GPUs and Compilation"
---

# æSIP: µArch-aware ASIP-ISA Co-Design via Program Synthesis, Equality Saturation, and External Don’t Cares

**中文标题：** æSIP: 通过程序综合、等式饱和与外部无关项的 µArch 感知 ASIP-ISA 协同设计

**所属 Session：** [Session 6C](index.md) · [ISCA 2026](../index.md)

**作者：** Haoran “Allen” Jin, Jirong Yang, Barry Lyu, Ruijie “Jerry” Gao, Nathan Bleier

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

An increasing number of applications, including implantables, IoT devices, and printed electronics, impose stringent power and area constraints. With the end of Dennard scaling, Application Specific Instruction Processors (ASIPs) have emerged as a promising solution, reducing power consumption and silicon area by sacrificing generality compared to general-purpose processors. However, existing approaches predominantly optimize hardware through software profiling, potentially overlooking optimization opportunities through software rewriting. We propose æSIP, a hardware-software co-optimization framework for efficient ASIP design. Our framework leverages e-graph data structures to explore semantically equivalent software implementations through rewriting rules derived from program synthesis. We employ a divide-and-conquer approach that performs local saturation at basic-block granularity followed by Integer Linear Programming (ILP)-based global extraction at whole-program scope, enabling scalability to real-world applications. We develop a don’t care-based hardware optimizer that automatically generates ASIP designs for each equivalent program variant, enabling agile design space exploration. We further incorporate a constraint-based sharing algorithm that clusters applications with similar characteristics and limits the number of ASIP variants, thereby enabling efficient reuse across workloads and balancing area/power efficiency with NRE cost.

To our knowledge, this represents the first systematic hardware–software co-design framework for agile multi-objective ASIP development. Experimental evaluation on widely used embedded benchmark suites, MiBench and Embench, demonstrates geometric mean area reduction of 17.0% and power savings of 12.3% compared to state-of-the-art ASIP generators. When energy is the optimization objective, æSIP achieves geometric mean energy reductions of 4.1% (CMOS 130 nm) and 6.3% (Inkjet Printed Electronics process). Furthermore, æSIP enables generalization across diverse workloads while preserving specialization. Our trade-off analysis shows that with only five shared ASIPs, æSIP achieves a 17.3% area reduction with 11.9% latency overhead, compared to 22.4% area reduction and 15.1% latency overhead under full per-application specialization.

## 中文摘要

越来越多的应用，包括植入式设备、物联网设备和印刷电子，施加了严格的功耗与面积约束。随着 Dennard 缩放的终结，专用指令处理器（ASIP）已成为一种有前景的解决方案，通过牺牲相对于通用处理器的通用性来降低功耗和硅面积。然而，现有方法主要通过软件剖析来优化硬件，可能忽视通过软件改写实现的优化机会。我们提出 æSIP，一个用于高效 ASIP 设计的软硬件协同优化框架。我们的框架利用 e-graph 数据结构，通过源自程序综合的重写规则来探索语义等价的软件实现。我们采用分治方法，在基本块粒度上执行局部饱和，随后在整个程序范围进行基于整数线性规划（ILP）的全局提取，从而可扩展到真实应用。我们开发了一个基于无关项（don't care）的硬件优化器，可为每个等价程序变体自动生成 ASIP 设计，实现敏捷的设计空间探索。我们进一步引入基于约束的共享算法，将特征相似的应用聚类并限制 ASIP 变体数量，从而实现跨工作负载的高效复用，并在面积/能效与 NRE 成本之间取得平衡。

据我们所知，这是首个用于敏捷多目标 ASIP 开发的系统性软硬件协同设计框架。在广泛使用的嵌入式基准套件 MiBench 和 Embench 上的实验评估表明，与最先进的 ASIP 生成器相比，几何平均面积减少 17.0%，功耗节省 12.3%。当以能量为优化目标时，æSIP 实现几何平均能量降低 4.1%（CMOS 130 nm）和 6.3%（喷墨印刷电子工艺）。此外，æSIP 在保持专用性的同时可泛化到多样化工作负载。我们的权衡分析显示，仅使用 5 个共享 ASIP 时，æSIP 实现 17.3% 的面积缩减和 11.9% 的延迟开销，而完全按应用专用化时为 22.4% 的面积缩减和 15.1% 的延迟开销。


## 代码与研究制品

已开源：[æSIP 官方代码仓库](https://github.com/CrucibleComputingGroup/aesip)（GPL-3.0）。论文第 3 页明确给出该仓库链接。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2026](../index.md)
