---
title: "PARE: A Power and Area-Efficient Memory Controller for High-Bandwidth DRAM"
description: "MICRO 2026 · Session 8B · PARE：面向高带宽 DRAM 的功耗与面积高效内存控制器"
tags:
  - "MICRO2026"
  - "DRAM"
  - "Energy Efficiency"
---

# PARE: A Power and Area-Efficient Memory Controller for High-Bandwidth DRAM

**中文标题：** PARE：面向高带宽 DRAM 的功耗与面积高效内存控制器

**所属 Session：** [Session 8B](index.md) · [MICRO 2026](../index.md)

**作者：** Andre Green, Niladrish Chatterjee, Mike O'Connor, Ben Keller, David Nellans, Borivoje Nikolić

**来源：** MICRO 2026，pp. 2848–2863；[DOI](https://doi.org/10.1109/MICRO67795.2026.00193)

## 英文摘要

High-throughput processors, like GPUs, fundamentally depend on high-bandwidth DRAM to feed their parallel compute engines. To maximize effective bandwidth, modern GPU memory controllers sort incoming requests to exploit DRAM row-buffer locality across interleaved streams from parallel compute engines. Historically, this deep sorting has improved both bandwidth utilization and energy efficiency by reducing unnecessary DRAM row activations. In this work, we show that the shifting access patterns of modern ML and HPC workloads, combined with improving DRAM access energy efficiency, are eroding the benefits of these deep-sorting memory controller designs. By combining architectural simulation with high-level synthesis, we demonstrate that simple energy-optimized memory controllers can achieve near-parity performance with prior complex sorting controllers for many important datacenter workloads. Such ultra-efficient designs are increasingly critical as emerging technologies like high-bandwidth stacked 3D DRAM will likely render the overhead of traditional sorting memory controllers prohibitively large for tightly integrated GPU systems. Drawing on these insights, we first present PARE, an efficiency-optimized GPU memory controller that removes row-aware transaction sorting entirely. PARE remains close to a sorting controller for most workloads, but exposes losses in two bandwidth-sensitive kernels caused by premature row-miss commitment. We then present MS-PARE, which retains only a narrow row-hit check to avoid this hazard. Relative to the conventional sorting controller, MS-PARE reduces area by 73.3% and average controller energy across 14 workloads by 55%, while maintaining near-parity performance and supporting the extreme DRAM bandwidth demanded by next-generation GPU architectures.

## 中文摘要

高吞吐量处理器（例如 GPU）从根本上依赖高带宽 DRAM 来为其并行计算引擎提供支持。为了最大限度地提高有效带宽，现代 GPU 内存控制器对传入请求进行排序，以利用来自并行计算引擎的交错流的 DRAM 行缓冲区局部性。从历史上看，这种深度排序通过减少不必要的 DRAM 行激活，提高了带宽利用率和能效。在这项工作中，我们表明，现代 ML 和 HPC 工作负载的访问模式的变化，加上 DRAM 访问能效的提高，正在削弱这些深度排序内存控制器设计的优势。通过将架构仿真与高级综合相结合，我们证明了简单的能量优化内存控制器可以为许多重要的数据中心工作负载实现与先前的复杂排序控制器接近的性能。这种超高效的设计变得越来越重要，因为高带宽堆叠 3D DRAM 等新兴技术可能会导致传统排序内存控制器的开销对于紧密集成的 GPU 系统来说过于庞大。基于这些见解，我们首先提出 PARE，一种效率优化的 GPU 内存控制器，它完全消除了行感知事务排序。对于大多数工作负载，PARE 仍然接近排序控制器，但会暴露由于过早的行缺失承诺而导致的两个带宽敏感内核的损失。然后我们提出了 MS-PARE，它只保留狭窄的行命中检查来避免这种危险。相对于传统的分拣控制器，MS-PARE 将面积减少了 73.3%，将 14 个工作负载的平均控制器能耗减少了 55%，同时保持接近同等的性能并支持下一代 GPU 架构所需的极限 DRAM 带宽。

## 中文关键词

内存控制器；DRAM；GPU 架构；能效；高带宽内存；内存调度

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

## 来源核对说明

附录称开源内存控制器将发布到 NVIDIA NVLabs，但未给出具体仓库地址。可查看 [NVLabs](https://github.com/NVLabs)。

[返回 Session 8B](index.md) · [MICRO 2026 主页](../index.md)
