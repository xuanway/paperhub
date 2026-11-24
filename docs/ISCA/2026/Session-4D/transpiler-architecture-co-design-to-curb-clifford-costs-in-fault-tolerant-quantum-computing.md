---
title: "Transpiler-Architecture Co-Design to Curb Clifford Costs in Fault-Tolerant Quantum Computing"
description: "ISCA 2026 · Session 4D · Transpiler-Architecture Co-Design to Curb Clifford Costs in Fault-Tolerant Quantum Computing"
tags:
  - "ISCA2026"
  - "Session 4D"
  - "Quantum 1"
---

# Transpiler-Architecture Co-Design to Curb Clifford Costs in Fault-Tolerant Quantum Computing

**中文标题：** 转译器-架构协同设计以抑制容错量子计算中的 Clifford 开销

**所属 Session：** [Session 4D](index.md) · [ISCA 2026](../index.md)

**作者：** Meng Wang, Chenxu Liu, Samuel Stein, Yufei Ding, Poulami Das, Prashant J. Nair, Ang Li

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Quantum Error Correction (QEC) codes form the foundation of Fault-Tolerant Quantum Computing (FTQC) and predominantly use the Clifford+T gate set. Recently, Clifford operations have become the key performance bottleneck in implementing QEC. While state-of-the-art approaches like Pauli-Based Compilation (PBC) reduce Clifford overhead by transforming Clifford gates into Pauli measurements, they do so at the cost of gate-level parallelism, inflating circuit depth and execution times. To overcome these limitations, we introduce TACO, a Transpiler–Architecture Co-design framework that tackles the Clifford bottleneck through circuit and architectural optimization. TACO uses FTQC insights to guide hardware-aware Clifford gate elimination and circuit restructuring, and leverages the resulting optimized circuits to refine architectural design. TACO applies FTQC-specific transformations to aggressively reduce Clifford overhead from rotation synthesis and Toffoli decompositions, while preserving gate-level parallelism. The resulting architecture is optimized for the locality and data-movement patterns of these circuits, enabling high-throughput, resource-efficient execution. Our evaluation across diverse benchmarks shows that TACO achieves up to 21.9× (mean 4.4×) reduction in execution time compared to the state-of-the-art baseline.


## 中文摘要

量子纠错（QEC）码构成容错量子计算（FTQC）的基础，并主要使用 Clifford+T 门集。近来，Clifford 操作已成为实现 QEC 的关键性能瓶颈。虽然基于 Pauli 的编译（PBC）等最先进方法通过将 Clifford 门转换为 Pauli 测量来降低 Clifford 开销，但它们以牺牲门级并行性为代价，进而增大电路深度和执行时间。为克服这些限制，我们提出 TACO，一个转译器-架构协同设计框架，通过电路和架构优化来解决 Clifford 瓶颈。TACO 利用 FTQC 洞见指导硬件感知的 Clifford 门消除和电路重构，并利用所得的优化电路来改进架构设计。TACO 应用 FTQC 专用变换，在保持门级并行性的同时大幅降低旋转合成和 Toffoli 分解带来的 Clifford 开销。由此得到的架构针对这些电路的局部性和数据搬移模式进行优化，实现高吞吐、资源高效的执行。我们在多种基准上的评估表明，相比最先进基线，TACO 的执行时间最多减少 21.9×（平均 4.4×）。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：pnnl/nwqec](https://github.com/pnnl/nwqec)
- [实验材料归档（Zenodo 19449157）](https://zenodo.org/records/19449157)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4D](index.md) · [返回 ISCA 2026](../index.md)
