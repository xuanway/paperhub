---
title: "TUSQ: Tracking, Uncomputation, and Sampling for Noisy Quantum Simulation"
description: "ISCA 2026 · Session 9C · TUSQ: Tracking, Uncomputation, and Sampling for Noisy Quantum Simulation"
tags:
  - "ISCA2026"
  - "Session 9C"
  - "Quantum 3"
---

# TUSQ: Tracking, Uncomputation, and Sampling for Noisy Quantum Simulation

**中文标题：** TUSQ: 面向含噪量子仿真的跟踪、逆计算与采样

**所属 Session：** [Session 9C](index.md) · [ISCA 2026](../index.md)

**作者：** Siddharth Dangwal, Tina Oberoi, Ajay Sailopal, Dhirpal Shah, Frederic T. Chong

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Quantum computers have improved in size and quality in recent years, enabling the execution of complex circuits. However, for most researchers, access to compute time is limited. This necessitates the development of simulators that mimic noisy quantum hardware accurately and scalably. The ideal way to simulate noisy systems is via Density Matrix Simulation (DMS). However, its high memory footprint limits its scalability. Consequently, noisy simulations are performed in two steps: (a) sampling multiple circuits with fixed noisy gates from the stochastic noise channels, (b) performing the State Vector Simulations (SVS) of these circuits and averaging their output to obtain the effective noisy simulation result. This often leads to a substantial increase in compute overhead, slowing down the simulation. Existing methods solve this problem by caching critical intermediate results in memory and reusing them. However, when a simulation task is both compute and memory-intensive, we need to eliminate computational overheads without incurring extra memory overheads. To enable fast simulation in the compute and memory bound regime, we propose TUSQ - Tracking, Uncomputation, and Sampling for Noisy Quantum Simulation. TUSQ is composed of two modules: the Error Characterization Module (ECM), and Depth First Tree Traversal (DFTT). The ECM characterizes errors so that the simulator can eliminate redundant circuit instances (via ER Tallying and ER Commutation), followed by importance sampling (in the Pruning stage), significantly reducing the number of circuits to be simulated relative to the baseline strategy of simulating all circuits. This is followed by DFTT, which computes the statevectors for these sampled circuits efficiently by taking advantage of circuit similarity, representing similar circuits in a tree and using computation and uncomputation to traverse the tree efficiently. TUSQ is evaluated for a total of 198 benchmarks, executed for 1 million shots and reports an average speedup of 59.06× and 13.38× over Qiskit and CUDA-Q, with a maximum speedup of 7878.03× and 439.38× respectively. We also compare TUSQ against TQSim in the time and memory critical regime. We observe an average and maximum speedup of 39.32× and 3134.31×, respectively.

## 中文摘要

近年来，量子计算机在规模和性能上有所提升，使得复杂线路的执行成为可能。然而，对大多数研究者而言，可用的计算时间有限。这就需要开发能够准确且可扩展地模拟含噪量子硬件的仿真器。模拟含噪系统的理想方法是密度矩阵仿真（DMS）。然而，其高昂的内存占用限制了其可扩展性。因此，含噪仿真分两步进行：(a) 从随机噪声信道中对多个带有固定噪声门的线路进行采样；(b) 对这些线路执行状态向量仿真（SVS），并对其输出取平均以获得有效的含噪仿真结果。这通常会导致计算开销大幅增加，拖慢仿真速度。现有方法通过在内存中缓存关键中间结果并重用来解决该问题。然而，当仿真任务同时是计算密集和内存密集时，我们需要在不产生额外内存开销的前提下消除计算开销。为在计算和内存受限的情形下实现快速仿真，我们提出 TUSQ——面向含噪量子仿真的跟踪、逆计算与采样。TUSQ 由两个模块组成：错误表征模块（ECM）和深度优先树遍历（DFTT）。ECM 对错误进行表征，使仿真器能够（通过 ER 计数和 ER 对易）消除冗余线路实例，随后在剪枝阶段进行重要性采样，与模拟所有线路的基线策略相比，显著减少了需要仿真的线路数量。之后，DFTT 通过利用线路相似性为这些采样线路高效计算状态向量，将相似线路表示为树，并使用计算和逆计算高效遍历该树。TUSQ 在共计 198 个基准上进行了评估，执行 100 万次采样，报告称相对于 Qiskit 和 CUDA-Q 的平均加速分别为 59.06 倍和 13.38 倍，最大加速分别为 7878.03 倍和 439.38 倍。我们还在时间和内存关键的情形下将 TUSQ 与 TQSim 进行了比较，观察到平均加速 39.32 倍、最大加速 3134.31 倍。

## 代码与研究制品

论文指向以下 TUSQ 项目仓库。核查时仓库仅包含 README、许可证和 .gitignore，尚未看到程序源码，不能据此认定实现已完整公开。

- [代码仓库：tinaoberoi/TUSQ](https://github.com/tinaoberoi/TUSQ)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9C](index.md) · [返回 ISCA 2026](../index.md)
