---
title: "DICE: Enabling Efficient General-Purpose SIMT Execution with Statically Scheduled Coarse-Grained Reconfigurable Arrays"
description: "ISCA 2026 · Session 10D · DICE: Enabling Efficient General-Purpose SIMT Execution with Statically Scheduled Coarse-Grained Reconfigurable Arrays"
tags:
  - "ISCA2026"
  - "Session 10D"
  - "Domain Specific Accelerators 3"
---

# DICE: Enabling Efficient General-Purpose SIMT Execution with Statically Scheduled Coarse-Grained Reconfigurable Arrays

**中文标题：** DICE: 以静态调度的粗粒度可重构阵列实现高效通用 SIMT 执行

**所属 Session：** [Session 10D](index.md) · [ISCA 2026](../index.md)

**作者：** Jiayi Wang, Ang Da Lu, Zhichen Zeng, Ang Li

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

While general-purpose graphics processing units (GPGPUs) dominate massively parallel computing through the single-instruction, multiple-thread (SIMT) programming model, their underlying single-instruction, multiple-data (SIMD) execution incurs substantial energy overhead from frequent register file (RF) accesses and complex control logic. We present DICE, a novel architecture that addresses these inefficiencies by replacing the SIMD backend with minimal-overhead, statically scheduled coarse-grained reconfigurable arrays (CGRAs) while preserving the well-known SIMT programming model. Unlike SIMD units that execute warps of threads in lockstep, DICE dispatches active threads in a pipelined manner onto the CGRA fabric, where data flows directly between processing elements (PEs), reducing RF accesses for intermediate values. Moreover, DICE organizes threads into groups larger than warps, reducing overhead by eliminating the warp-level control logic and further amortizing remaining control overhead across hundreds of threads. To handle operations with runtime dynamism, such as variable-latency memory loads and data-dependent control flow, while preserving static scheduling, DICE compiles programs into p-graphs by partitioning dynamic dependence edges across separate CGRA configurations. DICE further introduces several key optimizations: double-buffered configuration memory to hide reconfiguration latency, compile-time p-graph unrolling to enhance resource utilization, and a temporal memory coalescing unit (TMCU) to merge memory requests from consecutive, pipelined threads. Evaluations on Rodinia benchmarks in Accel-sim demonstrate that DICE reduces register file accesses by 68% on average. With equivalent computation and memory resources, DICE’s CGRA Processors (CPs) achieve a geometric mean of 1.77–1.90× dynamic energy efficiency and 42.0%–45.9% average power reduction compared to the modeled NVIDIA Turing Streaming Multiprocessors (SMs), while the full DICE system achieves performance comparable to the modeled Turing GPU baselines. DICE demonstrates that spatial pipeline execution can deliver substantial energy savings without sacrificing performance.

## 中文摘要

尽管通用图形处理器（GPGPU）通过单指令多线程（SIMT）编程模型主导着大规模并行计算，但其底层的单指令多数据（SIMD）执行因频繁的寄存器堆（RF）访问和复杂的控制逻辑而带来可观的能耗开销。我们提出 DICE，一种新颖的架构，通过用最小开销、静态调度的粗粒度可重构阵列（CGRA）替代 SIMD 后端，同时保留广为人知的 SIMT 编程模型，来解决这些低效问题。与以锁步方式执行线程 warp 的 SIMD 单元不同，DICE 以流水化方式将活跃线程派发到 CGRA 织物上，数据在处理单元（PE）之间直接流动，从而减少中间值的 RF 访问。此外，DICE 将线程组织成比 warp 更大的组，通过消除 warp 级控制逻辑来降低开销，并进一步将剩余的控制开销分摊到数百个线程上。为在保持静态调度的同时处理具有运行时动态性的操作（如可变延迟的内存加载和数据相关的控制流），DICE 通过将动态依赖边划分到不同的 CGRA 配置中，把程序编译为 p-graph。DICE 还引入若干关键优化：双缓冲配置存储器以隐藏重构延迟、编译期 p-graph 展开以提升资源利用率，以及时间内存合并单元（TMCU）以合并来自连续的、流水化线程的内存请求。在 Accel-sim 中对 Rodinia 基准的评估表明，DICE 平均减少 68% 的寄存器堆访问。在计算与内存资源相当的情况下，与所建模的 NVIDIA Turing 流多处理器（SM）相比，DICE 的 CGRA 处理器（CP）实现 1.77–1.90× 的几何平均动态能效和 42.0%–45.9% 的平均功耗降低，而完整的 DICE 系统达到与所建模的 Turing GPU 基线相当的性能。DICE 表明，空间流水线执行可以在不牺牲性能的情况下带来可观的能耗节省。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：jiayi-wang98/DICE-test-collection](https://github.com/jiayi-wang98/DICE-test-collection)
- [实验材料归档（Zenodo 19278715）](https://zenodo.org/records/19278715)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10D](index.md) · [返回 ISCA 2026](../index.md)
