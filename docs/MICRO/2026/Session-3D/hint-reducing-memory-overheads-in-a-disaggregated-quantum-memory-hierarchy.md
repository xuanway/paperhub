---
title: "HINT: Reducing Memory Overheads in a Disaggregated Quantum Memory Hierarchy"
description: "MICRO 2026 · Session 3D · HINT：降低分离式量子内存层次结构的内存开销"
tags:
  - "MICRO2026"
  - "Quantum Computing"
---

# HINT: Reducing Memory Overheads in a Disaggregated Quantum Memory Hierarchy

**中文标题：** HINT：降低分离式量子内存层次结构的内存开销

**所属 Session：** [Session 3D](index.md) · [MICRO 2026](../index.md)

**作者：** Suhas Vittal, Moinuddin Qureshi

**来源：** MICRO 2026，pp. 1284–1298；[DOI](https://doi.org/10.1109/MICRO67795.2026.00097)

## 英文摘要

Fault-Tolerant Quantum Computers (FTQCs) leverage error correction to protect program qubits throughout program execution. Modern FTQC architectures use the surface code for computation. However, as the surface code inefficiently stores program qubits, FTQCs instead use Quantum Low Density Parity Check (QLDPC) codes for efficiently storing idle program qubits. The surface code compute subsystem and QLDPC code memory subsystem effectively forms a memory hierarchy. Ideally, the compute subsystem should be fast to achieve high instruction throughput. Concurrently, memory subsystem should have high capacity to store many program qubits. Unfortunately, no single hardware platform currently supports both high instruction throughput and high capacity. In this paper, we study FTQCs with a disaggregated memory hierarchy, where the compute subsystem is implemented using hardware capable of high instruction throughput (e.g., superconducting) and the memory subsystem is implemented using hardware capable of achieving high capacity (e.g., neutral atom). In a disaggregated FTQC (DA-FTQC), the memory subsystem is 1000x slower than the compute subsystem. Thus, DA-FTQCs are 17.8x slower than an idealized (fast and high capacity) FTQC due to high memory access latency. We observe that the commonly used Earliest Instruction First (EIF) scheduler causes these high slowdowns due to its greedy scheduling decisions. To this end, we propose the High-Intensity (HINT) memory access scheduler. HINT optimizes the memory stream for compute intensity, or the amount of computation done per memory access. HINT improves compute intensity by 8.1x over EIF. HINT reduces the slowdowns of a DA-FTQC relative to ideal from 17.8x to 2.6x, bridging 90.4% of the performance gap.

## 中文摘要

容错量子计算机 (FTQC) 利用纠错来在整个程序执行过程中保护程序量子位。现代 FTQC 架构使用表面码进行计算。然而，由于表面码存储程序量子位的效率低下，FTQC 改为使用量子低密度奇偶校验 (QLDPC) 代码来有效存储空闲程序量子位。表面码计算子系统和QLDPC代码存储器子系统有效地形成存储器层次结构。理想情况下，计算子系统应该快速以实现高指令吞吐量。同时，存储子系统应该具有高容量来存储许多程序量子位。不幸的是，目前没有一个硬件平台能够同时支持高指令吞吐量和高容量。在本文中，我们研究具有分解内存层次结构的 FTQC，其中计算子系统是使用能够实现高指令吞吐量（例如超导）的硬件实现的，而内存子系统是使用能够实现高容量的硬件（例如中性原子）实现的。在分解的 FTQC (DA-FTQC) 中，内存子系统比计算子系统慢 1000 倍。因此，由于内存访问时延较高，DA-FTQC 比理想化（快速且高容量）的 FTQC 慢 17.8 倍。我们观察到，常用的最早指令优先 (EIF) 调度程序由于其贪婪的调度决策而导致速度大幅下降。为此，我们提出了高强度（HINT）内存访问调度程序。 HINT 针对计算强度或每次内存访问完成的计算量优化内存流。 HINT 的计算强度比 EIF 提高了 8.1 倍。 HINT 将 DA-FTQC 相对于理想情况的减速从 17.8 倍减少到 2.6 倍，缩小了 90.4% 的性能差距。

## 中文关键词

量子纠错；量子存储系统；量子编译；计算机体系结构；分离式内存层次

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3D](index.md) · [MICRO 2026 主页](../index.md)
